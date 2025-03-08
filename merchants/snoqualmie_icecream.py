"""
Basic data for the Snoqualmie Ice Cream merchant.
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

ENV_KEY = "SNOQUALMIE_ICE_CREAM_AGENT_KEY"

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
SNOQUALMIE_ICE_CREAM_NAME = "Snoqualmie Ice Cream"
SNOQUALMIE_ICE_CREAM_DESCRIPTION = "Ice Cream"

SNOQUALMIE_ICE_CREAM_PICTURE = "https://i.nostr.build/Qm7GmKk2hQRHTSrq.png"
SNOQUALMIE_ICE_CREAM_BANNER = "https://i.nostr.build/F5eWFEXtxRP5bo6S.png"
SNOQUALMIE_ICE_CREAM_CURRENCY = "USD"
SNOQUALMIE_ICE_CREAM_GEOHASH = "C23Q7U36W"
SNOQUALMIE_ICE_CREAM_WEBSITE = "https://www.snoqualmieicecream.com/"

# --*-- Stall for ride at 11am
SNOQUALMIE_ICE_CREAM_STALL_NAME = "Snoqualmie Ice Cream"
SNOQUALMIE_ICE_CREAM_STALL_ID = "snoqualmie-ice-cream-stall-snoqualmie"
SNOQUALMIE_ICE_CREAM_STALL_DESCRIPTION = """
Snoqualmie Ice Cream is in business to create the very best, all-natural ice cream,
custard, gelato and sorbet. 
 
Everything we make is as perfect as possible, while taking care of our customers,
employees, community, and environment.

Address: 8102 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
SNOQUALMIE_ICE_CREAM_SHIPPING_ZONE_NAME = "Worldwide"
SNOQUALMIE_ICE_CREAM_SHIPPING_ZONE_ID = "snoqualmie-ice-cream-sz"
SNOQUALMIE_ICE_CREAM_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_snoqualmie_ice_cream = StallShippingMethod(
    ssm_id=SNOQUALMIE_ICE_CREAM_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=SNOQUALMIE_ICE_CREAM_SHIPPING_ZONE_NAME,
    ssm_regions=SNOQUALMIE_ICE_CREAM_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_snoqualmie_ice_cream = ProductShippingCost(
    psc_id=SNOQUALMIE_ICE_CREAM_SHIPPING_ZONE_ID, psc_cost=0
)

# --*-- define stalls (using ShippingMethod)
snoqualmie_ice_cream_stall = Stall(
    id=SNOQUALMIE_ICE_CREAM_STALL_ID,
    name=SNOQUALMIE_ICE_CREAM_STALL_NAME,
    description=SNOQUALMIE_ICE_CREAM_STALL_DESCRIPTION,
    currency=SNOQUALMIE_ICE_CREAM_CURRENCY,
    shipping=[shipping_method_snoqualmie_ice_cream],
    geohash=SNOQUALMIE_ICE_CREAM_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(SNOQUALMIE_ICE_CREAM_NAME)
profile.set_about(SNOQUALMIE_ICE_CREAM_DESCRIPTION)
profile.set_banner(SNOQUALMIE_ICE_CREAM_BANNER)
profile.set_picture(SNOQUALMIE_ICE_CREAM_PICTURE)
profile.set_website(SNOQUALMIE_ICE_CREAM_WEBSITE)

stalls = [snoqualmie_ice_cream_stall]
products: list[Product] = []
