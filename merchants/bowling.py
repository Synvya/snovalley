"""
Basic data for the Bowling Alley merchant.
"""

from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from synvya_sdk import (
    NostrKeys,
    Product,
    ProductShippingCost,
    Profile,
    Stall,
    StallShippingMethod,
    generate_keys,
)

ENV_KEY = "BOWLING_AGENT_KEY"

# Get directory where the script is located
script_dir = Path(__file__).parent
# Load .env from the script's directory
load_dotenv(script_dir / "../.env")

# Load or generate keys
NSEC = getenv(ENV_KEY)
if NSEC is None:
    keys = generate_keys(env_var=ENV_KEY, env_path=script_dir / "../.env")
else:
    keys = NostrKeys.from_private_key(NSEC)

# --*-- Merchant info
BOWLING_NAME = "Snoqualmie Bowling Alley"
BOWLING_DESCRIPTION = "Historic Bowling Alley, open since 1955."

BOWLING_PICTURE = "https://i.nostr.build/ozUdRQjPwae7VgbH.png"
BOWLING_BANNER = "https://i.nostr.build/RsQvGu4piVXvdzng.png"
BOWLING_CURRENCY = "USD"
BOWLING_GEOHASH = "C23Q7U36W"
BOWLING_WEBSITE = "https://snoqualmiebowling.com/"

# --*-- Stall for ride at 11am
BOWLING_STALL_NAME = "Snoqualmie Bowling Alley"
BOWLING_STALL_ID = "bowling-stall-snoqualmie"
BOWLING_STALL_DESCRIPTION = """
Experience bowling the classic way. Enjoy a nostalgic bowling experience 
in a popular spot wth the community since 1955.

Address: 7940 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
BOWLING_SHIPPING_ZONE_NAME = "Worldwide"
BOWLING_SHIPPING_ZONE_ID = "bowling-sz"
BOWLING_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method = StallShippingMethod(
    ssm_id=BOWLING_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=BOWLING_SHIPPING_ZONE_NAME,
    ssm_regions=BOWLING_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost = ProductShippingCost(
    psc_id=BOWLING_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
bowling_stall = Stall(
    id=BOWLING_STALL_ID,
    name=BOWLING_STALL_NAME,
    description=BOWLING_STALL_DESCRIPTION,
    currency=BOWLING_CURRENCY,
    shipping=[shipping_method],
    geohash=BOWLING_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(BOWLING_NAME)
profile.set_about(BOWLING_DESCRIPTION)
profile.set_banner(BOWLING_BANNER)
profile.set_picture(BOWLING_PICTURE)
profile.set_website(BOWLING_WEBSITE)

stalls = [bowling_stall]
products: list[Product] = []
