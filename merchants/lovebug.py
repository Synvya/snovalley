"""
Basic data for the Love Bug Pet Boutique merchant.
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

ENV_KEY = "LOVEBUG_AGENT_KEY"

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
LOVEBUG_NAME = "Love Bug Pet Boutique"
LOVEBUG_DESCRIPTION = "Dog day care center."

LOVEBUG_PICTURE = "https://i.nostr.build/mVlAe7zNoB9VuSHY.png"
LOVEBUG_BANNER = "https://i.nostr.build/srUldnGcysCye6Ce.jpg"
LOVEBUG_CURRENCY = "USD"
LOVEBUG_GEOHASH = "C23Q7U36W"
LOVEBUG_WEBSITE = "https://www.facebook.com/lovebugpetbtq"

# --*-- Stall for ride at 11am
LOVEBUG_STALL_NAME = "Love Bug Pet Boutique"
LOVEBUG_STALL_ID = "lovebug-stall-snoqualmie"
LOVEBUG_STALL_DESCRIPTION = """
We are a locally owned small business offering pet supplies and services
to Snoqualmie Valley.

Address: 8030 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
LOVEBUG_SHIPPING_ZONE_NAME = "Worldwide"
LOVEBUG_SHIPPING_ZONE_ID = "lovebug-sz"
LOVEBUG_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_lovebug = StallShippingMethod(
    ssm_id=LOVEBUG_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=LOVEBUG_SHIPPING_ZONE_NAME,
    ssm_regions=LOVEBUG_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_lovebug = ProductShippingCost(
    psc_id=LOVEBUG_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
lovebug_stall = Stall(
    id=LOVEBUG_STALL_ID,
    name=LOVEBUG_STALL_NAME,
    description=LOVEBUG_STALL_DESCRIPTION,
    currency=LOVEBUG_CURRENCY,
    shipping=[shipping_method_lovebug],
    geohash=LOVEBUG_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(LOVEBUG_NAME)
profile.set_about(LOVEBUG_DESCRIPTION)
profile.set_banner(LOVEBUG_BANNER)
profile.set_picture(LOVEBUG_PICTURE)
profile.set_website(LOVEBUG_WEBSITE)

stalls = [lovebug_stall]
products: list[Product] = []
