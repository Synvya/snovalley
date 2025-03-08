"""
Basic data for the Buckshot merchant.
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

ENV_KEY = "BUCKSHOT_AGENT_KEY"

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
BUCKSHOT_NAME = "Buckshot Honey"
BUCKSHOT_DESCRIPTION = "A BBQ joint in Snoqualmie, WA"

BUCKSHOT_PICTURE = "https://i.nostr.build/UmFLdRy9yiwoOwoX.png"
BUCKSHOT_BANNER = "https://i.nostr.build/25YV4kzYcT1E9SJB.jpg"
BUCKSHOT_CURRENCY = "USD"
BUCKSHOT_GEOHASH = "C23Q7U36W"
BUCKSHOT_WEBSITE = "https://buckshothoney.com"

# --*-- Stall for ride at 11am
BUCKSHOT_STALL_NAME = "Buckshot"
BUCKSHOT_STALL_ID = "buckshot-stall-snoqualmie"
BUCKSHOT_STALL_DESCRIPTION = """
A Cascadian BBQ joint with a full bar nestled in a turn of the century "old west" style bank in the center of Historic Snoqualmie, WA.

Address: 38767 SE River St, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
BUCKSHOT_SHIPPING_ZONE_NAME = "Worldwide"
BUCKSHOT_SHIPPING_ZONE_ID = "buckshot-sz"
BUCKSHOT_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method = StallShippingMethod(
    ssm_id=BUCKSHOT_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=BUCKSHOT_SHIPPING_ZONE_NAME,
    ssm_regions=BUCKSHOT_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost = ProductShippingCost(
    psc_id=BUCKSHOT_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
buckshot_stall = Stall(
    id=BUCKSHOT_STALL_ID,
    name=BUCKSHOT_STALL_NAME,
    description=BUCKSHOT_STALL_DESCRIPTION,
    currency=BUCKSHOT_CURRENCY,
    shipping=[shipping_method],
    geohash=BUCKSHOT_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(BUCKSHOT_NAME)
profile.set_about(BUCKSHOT_DESCRIPTION)
profile.set_banner(BUCKSHOT_BANNER)
profile.set_picture(BUCKSHOT_PICTURE)
profile.set_website(BUCKSHOT_WEBSITE)

stalls = [buckshot_stall]
products: list[Product] = []
