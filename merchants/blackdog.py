"""
Basic data for the Black Dog Arts Cafe merchant.
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

ENV_KEY = "BLACKDOG_AGENT_KEY"

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
BLACKDOG_NAME = "Black Dog Arts Cafe"
BLACKDOG_DESCRIPTION = "Vegetarian Restaurant, Entertainment, Shop"

BLACKDOG_PICTURE = "https://i.nostr.build/joXJhvUxy55JDKyl.png"
BLACKDOG_BANNER = "https://i.nostr.build/swN8VU8YsekDrCvC.jpg"
BLACKDOG_CURRENCY = "USD"
BLACKDOG_GEOHASH = "C23Q7U36W"
BLACKDOG_WEBSITE = "https://www.blackdogsnoqualmie.com/"

# --*-- Stall for ride at 11am
BLACKDOG_STALL_NAME = "Black Dog Arts Cafe"
BLACKDOG_STALL_ID = "blackdog-stall-snoqualmie"
BLACKDOG_STALL_DESCRIPTION = """
Our mission is to serve healthy handcrafted vegetarian food in an environment that supports the arts

Address: 8062 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
BLACKDOG_SHIPPING_ZONE_NAME = "Worldwide"
BLACKDOG_SHIPPING_ZONE_ID = "blackdog-sz"
BLACKDOG_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method = StallShippingMethod(
    ssm_id=BLACKDOG_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=BLACKDOG_SHIPPING_ZONE_NAME,
    ssm_regions=BLACKDOG_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost = ProductShippingCost(
    psc_id=BLACKDOG_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
blackdog_stall = Stall(
    id=BLACKDOG_STALL_ID,
    name=BLACKDOG_STALL_NAME,
    description=BLACKDOG_STALL_DESCRIPTION,
    currency=BLACKDOG_CURRENCY,
    shipping=[shipping_method],
    geohash=BLACKDOG_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(BLACKDOG_NAME)
profile.set_about(BLACKDOG_DESCRIPTION)
profile.set_banner(BLACKDOG_BANNER)
profile.set_picture(BLACKDOG_PICTURE)
profile.set_website(BLACKDOG_WEBSITE)

stalls = [blackdog_stall]
products: list[Product] = []
