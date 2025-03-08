"""
Basic data for the Art Gallery of Snoqualmie Valley merchant.
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

ENV_KEY = "AGSV_AGENT_KEY"

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
AGSV_NAME = "Art Gallery of Snoqualmie Valley"
AGSV_DESCRIPTION = "Artist run gallery in historic downtown Snoqualmie"

AGSV_PICTURE = "https://i.nostr.build/HQosCIbQZyOFBfgP.png"
AGSV_BANNER = "https://i.nostr.build/OVxQzujBLEdw8spT.jpg"
AGSV_CURRENCY = "USD"
AGSV_GEOHASH = "C23Q7U36W"
AGSV_WEBSITE = "https://www.artgalleryofsnovalley.com/"

# --*-- Stall for ride at 11am
AGSV_STALL_NAME = "Art Gallery of Snoqualmie Valley"
AGSV_STALL_ID = "agsv-stall-snoqualmie"
AGSV_STALL_DESCRIPTION = """
Welcome to the Art Gallery of SnoValley, an artist-run gallery in historic downtown Snoqualmie featuring paintings in a variety of media, designer jewelry, art glass, woodwork, ceramics and sculpture created by local artists. Exhibited artwork represents a wide range of prices and includes many items suitable for gift giving.
Owned and operated by the Mt Si Artist Guild. Please drop in!

Address: 8130 Railroad Ave, Suite 101, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
AGSV_SHIPPING_ZONE_NAME = "Worldwide"
AGSV_SHIPPING_ZONE_ID = "agsv-sz"
AGSV_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_agsv = StallShippingMethod(
    ssm_id=AGSV_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=AGSV_SHIPPING_ZONE_NAME,
    ssm_regions=AGSV_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_agsv = ProductShippingCost(
    psc_id=AGSV_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
agsv_stall = Stall(
    id=AGSV_STALL_ID,
    name=AGSV_STALL_NAME,
    description=AGSV_STALL_DESCRIPTION,
    currency=AGSV_CURRENCY,
    shipping=[shipping_method_agsv],
    geohash=AGSV_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(AGSV_NAME)
profile.set_about(AGSV_DESCRIPTION)
profile.set_banner(AGSV_BANNER)
profile.set_picture(AGSV_PICTURE)
profile.set_website(AGSV_WEBSITE)

stalls = [agsv_stall]
products: list[Product] = []
