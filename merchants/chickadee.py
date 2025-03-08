"""
Basic data for the Chickadee Bake Shop merchant.
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

ENV_KEY = "CHICKADEE_AGENT_KEY"

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
CHICKADEE_NAME = "Chickadee Bake Shop"
CHICKADEE_DESCRIPTION = "Bake Shop"

CHICKADEE_PICTURE = "https://i.nostr.build/8YZQI9x9RXqwUCtC.png"
CHICKADEE_BANNER = "https://i.nostr.build/iotxojKQBfzZZM5X.png"
CHICKADEE_CURRENCY = "USD"
CHICKADEE_GEOHASH = "C23Q7U36W"
CHICKADEE_WEBSITE = "https://www.chickadeebakeshop.com/"

# --*-- Stall for ride at 11am
CHICKADEE_STALL_NAME = "Chickadee Bake Shop"
CHICKADEE_STALL_ID = "chickadee-stall-snoqualmie"
CHICKADEE_STALL_DESCRIPTION = """
Chickadee Bakeshop is two friends with a passion for baking and delivering goodness
directly to you. Visit our bakery and pie shop in downtown Snoqualmie.

Address: 8103 Falls Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
CHICKADEE_SHIPPING_ZONE_NAME = "Worldwide"
CHICKADEE_SHIPPING_ZONE_ID = "chickadee-sz"
CHICKADEE_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_chickadee = StallShippingMethod(
    ssm_id=CHICKADEE_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=CHICKADEE_SHIPPING_ZONE_NAME,
    ssm_regions=CHICKADEE_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_chickadee = ProductShippingCost(
    psc_id=CHICKADEE_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
chickadee_stall = Stall(
    id=CHICKADEE_STALL_ID,
    name=CHICKADEE_STALL_NAME,
    description=CHICKADEE_STALL_DESCRIPTION,
    currency=CHICKADEE_CURRENCY,
    shipping=[shipping_method_chickadee],
    geohash=CHICKADEE_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(CHICKADEE_NAME)
profile.set_about(CHICKADEE_DESCRIPTION)
profile.set_banner(CHICKADEE_BANNER)
profile.set_picture(CHICKADEE_PICTURE)
profile.set_website(CHICKADEE_WEBSITE)

stalls = [chickadee_stall]
products: list[Product] = []
