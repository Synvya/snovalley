"""
Basic data for the Sigillo merchant.
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

ENV_KEY = "SIGILLO_AGENT_KEY"

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
SIGILLO_NAME = "Sigillo Cellars"
SIGILLO_DESCRIPTION = "Sigillo Cellars Tasting Room"

SIGILLO_PICTURE = "https://i.nostr.build/But0aueJliWlopsG.png"
SIGILLO_BANNER = "https://i.nostr.build/c5IfN5Kj3k0Qt5OI.png"
SIGILLO_CURRENCY = "USD"
SIGILLO_GEOHASH = "C23Q7U36W"
SIGILLO_WEBSITE = "http://www.sigillocellars.com/"

# --*-- Stall for ride at 11am
SIGILLO_STALL_NAME = "Sigillo Cellars Tasting Room"
SIGILLO_STALL_ID = "sigillo-stall-snoqualmie"
SIGILLO_STALL_DESCRIPTION = """
Join us at our tasting room in the beautiful historic Sunset Theater in downtown Snoqualmie.
We offer light fare for those who want a longer experience and 
an outdoor seating area for those wanting to enjoy the Mt. Si view.
Live entertainment in the evenings. 

Address: 8086 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
SIGILLO_SHIPPING_ZONE_NAME = "Worldwide"
SIGILLO_SHIPPING_ZONE_ID = "sigillo-sz"
SIGILLO_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_sigillo = StallShippingMethod(
    ssm_id=SIGILLO_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=SIGILLO_SHIPPING_ZONE_NAME,
    ssm_regions=SIGILLO_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_sigillo = ProductShippingCost(
    psc_id=SIGILLO_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
sigillo_stall = Stall(
    id=SIGILLO_STALL_ID,
    name=SIGILLO_STALL_NAME,
    description=SIGILLO_STALL_DESCRIPTION,
    currency=SIGILLO_CURRENCY,
    shipping=[shipping_method_sigillo],
    geohash=SIGILLO_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(SIGILLO_NAME)
profile.set_about(SIGILLO_DESCRIPTION)
profile.set_banner(SIGILLO_BANNER)
profile.set_picture(SIGILLO_PICTURE)
profile.set_website(SIGILLO_WEBSITE)

stalls = [sigillo_stall]
products: list[Product] = []
