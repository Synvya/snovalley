"""
Basic data for the Snoqualmie Treading Co merchant.
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

ENV_KEY = "SNOQUALMIE_TRADING_AGENT_KEY"

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
SNOQUALMIE_TRADING_NAME = "Snoqualmie Trading Co"
SNOQUALMIE_TRADING_DESCRIPTION = "Gifts, souvenirs, and more."

SNOQUALMIE_TRADING_PICTURE = "https://i.nostr.build/8ZrAZeARe4am6ENb.png"
SNOQUALMIE_TRADING_BANNER = "https://i.nostr.build/TXSd1nVC8ckyjzEN.jpg"
SNOQUALMIE_TRADING_CURRENCY = "USD"
SNOQUALMIE_TRADING_GEOHASH = "C23Q7U36W"
SNOQUALMIE_TRADING_WEBSITE = "https://www.snoqualmietradingco.com/"

# --*-- Stall for ride at 11am
SNOQUALMIE_TRADING_STALL_NAME = "Snoqualmie Trading Co"
SNOQUALMIE_TRADING_STALL_ID = "snoqualmie-trading-co-stall-snoqualmie"
SNOQUALMIE_TRADING_STALL_DESCRIPTION = """
We are a mercantile located near Snoqualmie Falls in historic downtown Snoqualmie, Washington.

Address: 8112 Railroad Ave SE, Snoqualmie, WA, United States
""".strip()

# --*-- Shipping info
SNOQUALMIE_TRADING_SHIPPING_ZONE_NAME = "Worldwide"
SNOQUALMIE_TRADING_SHIPPING_ZONE_ID = "snoqualmie-trading-co-sz"
SNOQUALMIE_TRADING_SHIPPING_ZONE_REGIONS = ["Worldwide delivery"]


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_snoqualmie_trading = StallShippingMethod(
    ssm_id=SNOQUALMIE_TRADING_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=SNOQUALMIE_TRADING_SHIPPING_ZONE_NAME,
    ssm_regions=SNOQUALMIE_TRADING_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_snoqualmie_trading = ProductShippingCost(
    psc_id=SNOQUALMIE_TRADING_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
snoqualmie_trading_stall = Stall(
    id=SNOQUALMIE_TRADING_STALL_ID,
    name=SNOQUALMIE_TRADING_STALL_NAME,
    description=SNOQUALMIE_TRADING_STALL_DESCRIPTION,
    currency=SNOQUALMIE_TRADING_CURRENCY,
    shipping=[shipping_method_snoqualmie_trading],
    geohash=SNOQUALMIE_TRADING_GEOHASH,
)

# --*-- define products (using ShippingZone)


profile = Profile(keys.get_public_key())
profile.set_name(SNOQUALMIE_TRADING_NAME)
profile.set_about(SNOQUALMIE_TRADING_DESCRIPTION)
profile.set_banner(SNOQUALMIE_TRADING_BANNER)
profile.set_picture(SNOQUALMIE_TRADING_PICTURE)
profile.set_website(SNOQUALMIE_TRADING_WEBSITE)

stalls = [snoqualmie_trading_stall]
products: list[Product] = []
