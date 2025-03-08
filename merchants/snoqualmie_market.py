"""
Basic data for the Snoqualmie Market merchant.
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

ENV_KEY = "SNOQUALMIE_MARKET_AGENT_KEY"

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
SNOQUALMIE_MARKET_NAME = "Snoqualmie Market"
SNOQUALMIE_MARKET_DESCRIPTION = "Grocery and convenience store"

SNOQUALMIE_MARKET_PICTURE = "https://i.nostr.build/HdCUjYckpcVOOiBm.png"
SNOQUALMIE_MARKET_BANNER = "https://i.nostr.build/7qKa02p5kEVffOIb.jpg"
SNOQUALMIE_MARKET_CURRENCY = "USD"
SNOQUALMIE_MARKET_GEOHASH = "C23Q7U36W"
SNOQUALMIE_MARKET_WEBSITE = "https://www.facebook.com/snoqualmiemarket"

# --*-- Stall for ride at 11am
SNOQUALMIE_MARKET_STALL_NAME = "Snoqualmie Market"
SNOQUALMIE_MARKET_STALL_ID = "snoqualmie-market-stall-snoqualmie"
SNOQUALMIE_MARKET_STALL_DESCRIPTION = """
A legendary store where we offer an outstanding selection of ice cold beer, wines,
cold beverages, groceries, tobacco products, with a friendly smile.

Address: 8030 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
SNOQUALMIE_MARKET_SHIPPING_ZONE_NAME = "Worldwide"
SNOQUALMIE_MARKET_SHIPPING_ZONE_ID = "snoqualmie-market-sz"
SNOQUALMIE_MARKET_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_snoqualmie_market = StallShippingMethod(
    ssm_id=SNOQUALMIE_MARKET_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=SNOQUALMIE_MARKET_SHIPPING_ZONE_NAME,
    ssm_regions=SNOQUALMIE_MARKET_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_snoqualmie_market = ProductShippingCost(
    psc_id=SNOQUALMIE_MARKET_SHIPPING_ZONE_ID, psc_cost=0
)

# --*-- define stalls (using ShippingMethod)
snoqualmie_market_stall = Stall(
    id=SNOQUALMIE_MARKET_STALL_ID,
    name=SNOQUALMIE_MARKET_STALL_NAME,
    description=SNOQUALMIE_MARKET_STALL_DESCRIPTION,
    currency=SNOQUALMIE_MARKET_CURRENCY,
    shipping=[shipping_method_snoqualmie_market],
    geohash=SNOQUALMIE_MARKET_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(SNOQUALMIE_MARKET_NAME)
profile.set_about(SNOQUALMIE_MARKET_DESCRIPTION)
profile.set_banner(SNOQUALMIE_MARKET_BANNER)
profile.set_picture(SNOQUALMIE_MARKET_PICTURE)
profile.set_website(SNOQUALMIE_MARKET_WEBSITE)

stalls = [snoqualmie_market_stall]
products: list[Product] = []
