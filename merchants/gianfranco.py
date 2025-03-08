"""
Basic data for the Gianfranco Ristorante merchant.
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

ENV_KEY = "GIANFRANCO_AGENT_KEY"

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
GIANFRANCO_NAME = "Gianfranco Ristorante Italiano"
GIANFRANCO_DESCRIPTION = "Escape to Southern Italy for an Evening"

GIANFRANCO_PICTURE = "https://i.nostr.build/m11QH1plBBEV7uKb.jpg"
GIANFRANCO_BANNER = "https://i.nostr.build/6Ld7J15owwOooAOf.jpg"
GIANFRANCO_CURRENCY = "USD"
GIANFRANCO_GEOHASH = "C23Q7U36W"
GIANFRANCO_WEBSITE = "https://www.gianfrancosnoqualmie.com/"

# --*-- Stall for ride at 11am
GIANFRANCO_STALL_NAME = "Gianfranco Ristorante"
GIANFRANCO_STALL_ID = "gianfranco-stall-snoqualmie"
GIANFRANCO_STALL_DESCRIPTION = """
Small family run restaurant with authentic family friendly Italian dining.
Extensive Italian wine list. Service bar with sodas, wine, beer and cocktails.
Gluten-free pasta and pizza crust.

Address: 8150 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
GIANFRANCO_SHIPPING_ZONE_NAME = "Worldwide"
GIANFRANCO_SHIPPING_ZONE_ID = "gianfranco-sz"
GIANFRANCO_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_gianfranco = StallShippingMethod(
    ssm_id=GIANFRANCO_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=GIANFRANCO_SHIPPING_ZONE_NAME,
    ssm_regions=GIANFRANCO_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_gianfranco = ProductShippingCost(
    psc_id=GIANFRANCO_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
gianfranco_stall = Stall(
    id=GIANFRANCO_STALL_ID,
    name=GIANFRANCO_STALL_NAME,
    description=GIANFRANCO_STALL_DESCRIPTION,
    currency=GIANFRANCO_CURRENCY,
    shipping=[shipping_method_gianfranco],
    geohash=GIANFRANCO_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(GIANFRANCO_NAME)
profile.set_about(GIANFRANCO_DESCRIPTION)
profile.set_banner(GIANFRANCO_BANNER)
profile.set_picture(GIANFRANCO_PICTURE)
profile.set_website(GIANFRANCO_WEBSITE)

stalls = [gianfranco_stall]
products: list[Product] = []
