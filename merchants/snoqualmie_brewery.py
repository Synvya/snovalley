"""
Basic data for the Snoqualmie Brewery merchant.
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

ENV_KEY = "SNOQUALMIE_BREWERY_AGENT_KEY"

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
SNOQUALMIE_BREWERY_NAME = "Snoqualmie Falls Brewery"
SNOQUALMIE_BREWERY_DESCRIPTION = (
    "Making fresh, flavorful, and balanced beers since 1997!"
)

SNOQUALMIE_BREWERY_PICTURE = "https://i.nostr.build/o3hnaswrF6XmhvYa.png"
SNOQUALMIE_BREWERY_BANNER = "https://i.nostr.build/zqM3DdXP5GxeuWPl.jpg"
SNOQUALMIE_BREWERY_CURRENCY = "USD"
SNOQUALMIE_BREWERY_GEOHASH = "C23Q7U36W"
SNOQUALMIE_BREWERY_WEBSITE = "https://fallsbrew.com"

# --*-- Stall for ride at 11am
SNOQUALMIE_BREWERY_STALL_NAME = "Snoqualmie Falls Brewery"
SNOQUALMIE_BREWERY_STALL_ID = "snoqualmie-brewery-stall-snoqualmie"
SNOQUALMIE_BREWERY_STALL_DESCRIPTION = """
Snoqualmie Falls Brewery is a small, independent craft brewery located
in historic downtown Snoqualmie, Wash. In 1997, five beer geeks founded
the company and started brewing beer. 

Address: 8032 Falls Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
SNOQUALMIE_BREWERY_SHIPPING_ZONE_NAME = "Worldwide"
SNOQUALMIE_BREWERY_SHIPPING_ZONE_ID = "snoqualmie-brewery-sz"
SNOQUALMIE_BREWERY_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
# shipping_method_snoqualmie_brewery = (
#     ShippingMethod(id=SNOQUALMIE_BREWERY_SHIPPING_ZONE_ID, cost=0)
#     .name(SNOQUALMIE_BREWERY_SHIPPING_ZONE_NAME)
#     .regions(SNOQUALMIE_BREWERY_SHIPPING_ZONE_REGIONS)
# )

shipping_method = StallShippingMethod(
    ssm_id=SNOQUALMIE_BREWERY_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=SNOQUALMIE_BREWERY_SHIPPING_ZONE_NAME,
    ssm_regions=SNOQUALMIE_BREWERY_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
# shipping_cost_snoqualmie_brewery = ShippingCost(
#     id=SNOQUALMIE_BREWERY_SHIPPING_ZONE_ID, cost=0
# )

shipping_cost = ProductShippingCost(
    psc_id=SNOQUALMIE_BREWERY_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
# snoqualmie_brewery_stall = MerchantStall(
#     id=SNOQUALMIE_BREWERY_STALL_ID,
#     name=SNOQUALMIE_BREWERY_STALL_NAME,
#     description=SNOQUALMIE_BREWERY_STALL_DESCRIPTION,
#     currency=SNOQUALMIE_BREWERY_CURRENCY,
#     shipping=[shipping_method],
#     geohash=SNOQUALMIE_BREWERY_GEOHASH,
# )
snoqualmie_brewery_stall = Stall(
    id=SNOQUALMIE_BREWERY_STALL_ID,
    name=SNOQUALMIE_BREWERY_STALL_NAME,
    description=SNOQUALMIE_BREWERY_STALL_DESCRIPTION,
    currency=SNOQUALMIE_BREWERY_CURRENCY,
    shipping=[shipping_method],
    geohash=SNOQUALMIE_BREWERY_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(SNOQUALMIE_BREWERY_NAME)
profile.set_about(SNOQUALMIE_BREWERY_DESCRIPTION)
profile.set_banner(SNOQUALMIE_BREWERY_BANNER)
profile.set_picture(SNOQUALMIE_BREWERY_PICTURE)
profile.set_website(SNOQUALMIE_BREWERY_WEBSITE)

stalls = [snoqualmie_brewery_stall]
products: list[Product] = []
