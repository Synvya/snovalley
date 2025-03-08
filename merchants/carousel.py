"""
Basic data for the Carousel merchant.
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

ENV_KEY = "CAROUSEL_AGENT_KEY"

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
CAROUSEL_NAME = "Carousel"
CAROUSEL_DESCRIPTION = "Gift Shop"

CAROUSEL_PICTURE = "https://i.nostr.build/IDbydi8XvTNflEQO.png"
CAROUSEL_BANNER = "https://i.nostr.build/xIP9X9nAwJl4WXH5.png"
CAROUSEL_CURRENCY = "USD"
CAROUSEL_GEOHASH = "C23Q7U36W"
CAROUSEL_WEBSITE = "http://www.instagram.com/carousel_snoqualmie"

# --*-- Stall for ride at 11am
CAROUSEL_STALL_NAME = "Carousel Gift Shop"
CAROUSEL_STALL_ID = "carousel-stall-snoqualmie"
CAROUSEL_STALL_DESCRIPTION = """
Gift shop

Address: 8002 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
CAROUSEL_SHIPPING_ZONE_NAME = "Worldwide"
CAROUSEL_SHIPPING_ZONE_ID = "carousel-sz"
CAROUSEL_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_carousel = StallShippingMethod(
    ssm_id=CAROUSEL_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=CAROUSEL_SHIPPING_ZONE_NAME,
    ssm_regions=CAROUSEL_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_carousel = ProductShippingCost(
    psc_id=CAROUSEL_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
carousel_stall = Stall(
    id=CAROUSEL_STALL_ID,
    name=CAROUSEL_STALL_NAME,
    description=CAROUSEL_STALL_DESCRIPTION,
    currency=CAROUSEL_CURRENCY,
    shipping=[shipping_method_carousel],
    geohash=CAROUSEL_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(CAROUSEL_NAME)
profile.set_about(CAROUSEL_DESCRIPTION)
profile.set_banner(CAROUSEL_BANNER)
profile.set_picture(CAROUSEL_PICTURE)
profile.set_website(CAROUSEL_WEBSITE)

stalls = [carousel_stall]
products: list[Product] = []
