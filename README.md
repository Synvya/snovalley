## Snoqualmie Valley Chamber of Commerce Tourist Agent


## Installation
Create a virtual environment:
```shell
python -m venv venv
source venv/bin/activate
```

Install dependencies:
```shell
pip install -r requirements.txt
```

Run the scripts:
```shell
# Publishes information to Nostr network
python publish_merchants.py

# Populates RAG database with Nostr data
python refresh_database.py
```

