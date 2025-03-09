"""
Module to refresh the RAG database with the latest information
available in the Nostr network about the Snoqualmie Valley
Marketplace.
"""

import uuid
from os import getenv
from pathlib import Path
from typing import Optional

from agno.agent import Agent, AgentKnowledge  # type: ignore
from agno.embedder.openai import OpenAIEmbedder
from agno.models.openai import OpenAIChat  # type: ignore
from agno.vectordb.pgvector import PgVector, SearchType
from dotenv import load_dotenv
from pgvector.sqlalchemy import Vector  # Correct import for vector storage
from sqlalchemy import Column, String, Text, create_engine
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.sql import text
from synvya_sdk import NostrKeys, Profile, generate_keys
from synvya_sdk.agno import BuyerTools

# Get directory where the script is located
script_dir = Path(__file__).parent
# Load .env from the script's directory
load_dotenv(script_dir / ".env")

# Load or generate keys
NSEC = getenv("AGENT_KEY")
if NSEC is None:
    keys = generate_keys(env_var="AGENT_KEY", env_path=script_dir / ".env")
else:
    keys = NostrKeys.from_private_key(NSEC)

# Load or use default relay
RELAY = getenv("RELAY")
if RELAY is None:
    RELAY = "wss://relay.damus.io"

# Load OpenAI API key
OPENAI_API_KEY = getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Load database credentials
DB_USERNAME = getenv("DB_USERNAME")
if DB_USERNAME is None:
    raise ValueError("DB_USERNAME environment variable is not set")

DB_PASSWORD = getenv("DB_PASSWORD")
if DB_PASSWORD is None:
    raise ValueError("DB_PASSWORD environment variable is not set")

DB_HOST = getenv("DB_HOST")
if DB_HOST is None:
    raise ValueError("DB_HOST environment variable is not set")

DB_PORT = getenv("DB_PORT")
if DB_PORT is None:
    raise ValueError("DB_PORT environment variable is not set")

DB_NAME = getenv("DB_NAME")
if DB_NAME is None:
    raise ValueError("DB_NAME environment variable is not set")

profile = Profile(keys.get_public_key())

# Initialize database connection
db_url = (
    f"postgresql+psycopg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


try:
    engine = create_engine(db_url)
    with engine.connect() as connection:
        print("✅ Successfully connected to the database!")
except Exception as e:
    print(f"❌ Database connection error: {e}")
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Seller(Base):
    """
    SQLAlchemy model for table `sellers` in the nostr schema.
    """

    __tablename__ = "sellers"
    __table_args__ = {"schema": "nostr"}  # If the table is inside the 'nostr' schema

    id = Column(
        String, primary_key=True, default=lambda: str(uuid.uuid4())
    )  # UUID primary key
    name = Column(Text, nullable=True)
    meta_data = Column(JSONB, default={})
    filters = Column(JSONB, default={})
    content = Column(Text, nullable=True)
    embedding: Optional[Vector] = Column(Vector(1536), nullable=True)
    usage = Column(JSONB, default={})
    content_hash = Column(Text, nullable=True)

    def __repr__(self) -> str:
        """
        Return a string representation of the Seller object.
        """
        return f"<Seller(id={self.id}, name={self.name})>"


# Function to drop and recreate the table
def reset_database() -> None:
    """
    Drop and recreate all tables in the database.
    """
    with engine.connect() as conn:
        # Enable pgvector extension
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
        conn.commit()

    # Drop and recreate all tables
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


# reset_database()

vector_db = PgVector(
    table_name="sellers",
    db_url=db_url,
    schema="nostr",
    search_type=SearchType.vector,
    embedder=OpenAIEmbedder(),
)


knowledge_base = AgentKnowledge(vector_db=vector_db)

agent = Agent(
    name=f"Database Refreshing Agent",
    model=OpenAIChat(id="gpt-4o-mini", api_key=OPENAI_API_KEY),
    tools=[
        BuyerTools(
            knowledge_base=knowledge_base,
            relay=RELAY,
            private_key=keys.get_private_key(),
        )
    ],
    add_history_to_messages=True,
    num_history_responses=10,
    read_chat_history=True,
    read_tool_call_history=True,
    knowledge=knowledge_base,
    show_tool_calls=False,
    debug_mode=False,
    # async_mode=True,
    instructions=[
        """
        You are an agent that populates its knowledge base with the
        information available in the Nostr network about the Snoqualmie
        Valley Marketplace.
        
        You will use BuyerTools todownload all sellers from the marketplace named "Historic Downtown
        Snoqualmie" by the owner with the public key
        "npub1nar4a3vv59qkzdlskcgxrctkw9f0ekjgqaxn8vd0y82f9kdve9rqwjcurn"
        and store them in your knowledge base.

        You will then use BuyerTools to download all the stalls and all the products
        from each seller and store them in your knowledge base.

        If you get an error downloading the sellers, stalls, or products,
        wait for one second and try again for the requests that failed.

        Once you're done share the results with the user:
         - The number of sellers stored your the knowledge base.
         - For each seller, the name of the stalls and the products stored
           in your knowledge base.

        """.strip(),
    ],
)


response = agent.run(
    "Proceed to download all sellers from the marketplace as instructed"
)  # Get response from agent
print(f"\n🤖 Database Refreshing Agent: {response.get_content_as_string()}\n")
