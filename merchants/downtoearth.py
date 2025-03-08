"""
Basic data for the Down To Earth merchant.
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

ENV_KEY = "DOWNTOTHEARTH_AGENT_KEY"

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
DOWNTOTHEARTH_NAME = "Down To Earth Flowers & Gifts"
DOWNTOTHEARTH_DESCRIPTION = ""

DOWNTOTHEARTH_PICTURE = "https://i.nostr.build/a0QVO9FtB2EMulJd.png"
DOWNTOTHEARTH_BANNER = "https://i.nostr.build/IlCdlWJlKbUJns2D.jpg"
DOWNTOTHEARTH_CURRENCY = "USD"
DOWNTOTHEARTH_GEOHASH = "C23Q7U36W"
DOWNTOTHEARTH_WEBSITE = "https://snoqualmieflowers.com/"

# --*-- Stall for ride at 11am
DOWNTOTHEARTH_STALL_NAME = "Down To Earth Flowers & Gifts"
DOWNTOTHEARTH_STALL_ID = "downtoearth-stall-snoqualmie"
DOWNTOTHEARTH_STALL_DESCRIPTION = """
Founded in 2000, Down to Earth is a boutique florist, gift and plant shop
located in the heart of Historic Downtown Snoqualmie, Washington.

We offer pick-ups and delivery to the Snoqualmie Valley and surrounding
areas Mondays through Saturdays.

Address: 8096 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
DOWNTOTHEARTH_SHIPPING_ZONE_NAME = "Worldwide"
DOWNTOTHEARTH_SHIPPING_ZONE_ID = "downtoearth-sz"
DOWNTOTHEARTH_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_downtoearth = StallShippingMethod(
    ssm_id=DOWNTOTHEARTH_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=DOWNTOTHEARTH_SHIPPING_ZONE_NAME,
    ssm_regions=DOWNTOTHEARTH_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_downtoearth = ProductShippingCost(
    psc_id=DOWNTOTHEARTH_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
downtoearth_stall = Stall(
    id=DOWNTOTHEARTH_STALL_ID,
    name=DOWNTOTHEARTH_STALL_NAME,
    description=DOWNTOTHEARTH_STALL_DESCRIPTION,
    currency=DOWNTOTHEARTH_CURRENCY,
    shipping=[shipping_method_downtoearth],
    geohash=DOWNTOTHEARTH_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(DOWNTOTHEARTH_NAME)
profile.set_about(DOWNTOTHEARTH_DESCRIPTION)
profile.set_banner(DOWNTOTHEARTH_BANNER)
profile.set_picture(DOWNTOTHEARTH_PICTURE)
profile.set_website(DOWNTOTHEARTH_WEBSITE)

stalls = [downtoearth_stall]
products: list[Product] = []
