## Snoqualmie Valley Chamber of Commerce Tourist Agent

## Merchant Information
All merchant information is in the folder [merchants](https://github.com/Synvya/snovalley/tree/main/merchants). 

The script `publish_merchants.py` imports ONE file from the folder and publishes the information contained in that file.

Run `publish_merchants.py` as many times as needed and then call `refresh_database.py` once. You have the option to wipe out the database before refreshing it by removing the comment on the following line in `refresh_database.py`:
```python
# reset_database()
```


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

Populate environment variables
```shell
cp ~/.env.example .env
vim .env
```

Run the scripts:
```shell
# Publishes information to Nostr network
python publish_merchants.py

# Populates RAG database with Nostr data
python refresh_database.py
```

