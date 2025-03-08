"""
Basic data for the Carmichael's Hardware merchant.
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

ENV_KEY = "CARMICHAELS_AGENT_KEY"

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
CARMICHAELS_NAME = "Carmichael's Hardware Store"
CARMICHAELS_DESCRIPTION = "Carmichael's Hardware Store"

CARMICHAELS_PICTURE = "https://i.nostr.build/J926Lnl3ErgiToeB.png"
CARMICHAELS_BANNER = "https://i.nostr.build/M2Qxp1VN8R0HBIqA.png"
CARMICHAELS_CURRENCY = "USD"
CARMICHAELS_GEOHASH = "C23Q7U36W"
CARMICHAELS_WEBSITE = (
    "https://www.facebook.com/pages/Carmichael's%20True%20Value/1645251882413999/"
)

# --*-- Stall for ride at 11am
CARMICHAELS_STALL_NAME = "Carmichael's Hardware Store"
CARMICHAELS_STALL_ID = "carmichaels-stall-snoqualmie"
CARMICHAELS_STALL_DESCRIPTION = """
Serving the communnity for over 100 years.
Hardware, building materials, gifts, home decor, home improvement, retail, toys

Address: 8150 Falls Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
CARMICHAELS_SHIPPING_ZONE_NAME = "Worldwide"
CARMICHAELS_SHIPPING_ZONE_ID = "carmichaels-sz"
CARMICHAELS_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method = StallShippingMethod(
    ssm_id=CARMICHAELS_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=CARMICHAELS_SHIPPING_ZONE_NAME,
    ssm_regions=CARMICHAELS_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost = ProductShippingCost(
    psc_id=CARMICHAELS_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
carmichaels_stall = Stall(
    id=CARMICHAELS_STALL_ID,
    name=CARMICHAELS_STALL_NAME,
    description=CARMICHAELS_STALL_DESCRIPTION,
    currency=CARMICHAELS_CURRENCY,
    shipping=[shipping_method],
    geohash=CARMICHAELS_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(CARMICHAELS_NAME)
profile.set_about(CARMICHAELS_DESCRIPTION)
profile.set_banner(CARMICHAELS_BANNER)
profile.set_picture(CARMICHAELS_PICTURE)
profile.set_website(CARMICHAELS_WEBSITE)

stalls = [carmichaels_stall]
products: list[Product] = []
