"""
Basic data for the Bindlestick merchant.
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

ENV_KEY = "BINDLESTICK_AGENT_KEY"

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
BINDLESTICK_NAME = "Bindlestick"
BINDLESTICK_DESCRIPTION = "Coffee & Ale House"

BINDLESTICK_PICTURE = "https://i.nostr.build/WR181h1Hu6FkmsUb.png"
BINDLESTICK_BANNER = "https://i.nostr.build/8lJORhEUwNjyPWuT.jpg"
BINDLESTICK_CURRENCY = "USD"
BINDLESTICK_GEOHASH = "C23Q7U36W"
BINDLESTICK_WEBSITE = "https://bindlestick.org/"

# --*-- Stall for ride at 11am
BINDLESTICK_STALL_NAME = "Bindlestick"
BINDLESTICK_STALL_ID = "bindlestick-stall-snoqualmie"
BINDLESTICK_STALL_DESCRIPTION = """
Downtown Snoqualmie’s historic destination for brunch, lunch, late night cocktails, coffee & company

Address: 8010 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
BINDLESTICK_SHIPPING_ZONE_NAME = "Worldwide"
BINDLESTICK_SHIPPING_ZONE_ID = "bindlestick-sz"
BINDLESTICK_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method = StallShippingMethod(
    ssm_id=BINDLESTICK_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=BINDLESTICK_SHIPPING_ZONE_NAME,
    ssm_regions=BINDLESTICK_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost = ProductShippingCost(
    psc_id=BINDLESTICK_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
bindlestick_stall = Stall(
    id=BINDLESTICK_STALL_ID,
    name=BINDLESTICK_STALL_NAME,
    description=BINDLESTICK_STALL_DESCRIPTION,
    currency=BINDLESTICK_CURRENCY,
    shipping=[shipping_method],
    geohash=BINDLESTICK_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(BINDLESTICK_NAME)
profile.set_about(BINDLESTICK_DESCRIPTION)
profile.set_banner(BINDLESTICK_BANNER)
profile.set_picture(BINDLESTICK_PICTURE)
profile.set_website(BINDLESTICK_WEBSITE)

stalls = [bindlestick_stall]
products: list[Product] = []
