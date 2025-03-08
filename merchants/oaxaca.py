"""
Basic data for the Oaxaca merchant.
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

ENV_KEY = "OAXACA_AGENT_KEY"

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
OAXACA_NAME = "Caadxi Oaxaca"
OAXACA_DESCRIPTION = "Authentic Southern Mexican Restaurant"

OAXACA_PICTURE = "https://i.nostr.build/XOnDJ9dgzOnycuIS.png"
OAXACA_BANNER = "https://i.nostr.build/kqscVlquZOCBXOpU.jpg"
OAXACA_CURRENCY = "USD"
OAXACA_GEOHASH = "C23Q7U36W"
OAXACA_WEBSITE = "https://caadxioaxaca.com/"

# --*-- Stall for ride at 11am
OAXACA_STALL_NAME = "Oaxaca"
OAXACA_STALL_ID = "oaxaca-stall-snoqualmie"
OAXACA_STALL_DESCRIPTION = """
Caadxi Oaxaca is an authentic Mexican restaurant in the picturesque City
of Snoqualmie. Family-owned and operated we offer a full bar including
regional mezcal and tequila and a variety of foods for every diet.

Address: 8030 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
OAXACA_SHIPPING_ZONE_NAME = "Worldwide"
OAXACA_SHIPPING_ZONE_ID = "oaxaca-sz"
OAXACA_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_oaxaca = StallShippingMethod(
    ssm_id=OAXACA_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=OAXACA_SHIPPING_ZONE_NAME,
    ssm_regions=OAXACA_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_oaxaca = ProductShippingCost(
    psc_id=OAXACA_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
oaxaca_stall = Stall(
    id=OAXACA_STALL_ID,
    name=OAXACA_STALL_NAME,
    description=OAXACA_STALL_DESCRIPTION,
    currency=OAXACA_CURRENCY,
    shipping=[shipping_method_oaxaca],
    geohash=OAXACA_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(OAXACA_NAME)
profile.set_about(OAXACA_DESCRIPTION)
profile.set_banner(OAXACA_BANNER)
profile.set_picture(OAXACA_PICTURE)
profile.set_website(OAXACA_WEBSITE)

stalls = [oaxaca_stall]
products: list[Product] = []
