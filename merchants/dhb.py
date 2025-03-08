"""
Sample data for the Dark Horse Brew Coffee merchant.
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

ENV_KEY = "DHB_AGENT_KEY"

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
DHB_NAME = "Dark Horse Brew Coffee"
DHB_DESCRIPTION = """
    Great tasting coffee should be accessible to our locals all year round.
    Address: 7936 Railroad Ave, Snoqualmie, WA 98065
    """
DHB_PICTURE = "https://i.nostr.build/CgcwPCWXMjUCtELW.png"
DHB_CURRENCY = "USD"
DHB_GEOHASH = "C23Q7U36W"
DHB_WEBSITE = "https://darkhorsebrew.coffee/"
DHB_BANNER = "https://i.nostr.build/0vTXOv8DGSwINuqT.jpg"

# --*-- Define Shipping methods for stalls (nostr SDK type)
# --*-- Stall for ride at 11am
DHB_STALL_NAME = "Dark Horse Brew Coffee"
DHB_STALL_ID = "dhb-stall-snoqualmie"  # "212a26qV"
DHB_STALL_DESCRIPTION = """
Dark Horse Brew is made up of a passionate team of coffee lovers who believe that great 
tasting coffee should be accessible to our locals all year round. With drive-thru and
walk-up coffee stands in both downtown Snoqualmie WA and downtown Redmond WA so you can
always grab a quality drink or snack for your morning commute, on your lunch break, or
even on your way home. Whatever the occasion, we're here to offer best-in-service coffee
products for you whenever you need it.

Address: 7936 Railroad Ave, Snoqualmie, WA 98065
""".strip()

# --*-- Shipping info
DHB_SHIPPING_ZONE_NAME = "Drive Thru"
DHB_SHIPPING_ZONE_ID = "dhb-sz"
DHB_SHIPPING_ZONE_REGIONS = ["Drive Thru"]

# --*-- DHB Product info
DHB_PRODUCT_ID_LATTE = "dhb-latte"
DHB_PRODUCT_IMAGE_LATTE = "https://i.nostr.build/1X2TmBCnXxEFsbzU.png"
DHB_QUANTITY_LATTE = 90
DHB_PRODUCT_NAME_LATTE = "Dark Horse Brew Latte"
DHB_PRODUCT_DESCRIPTION_LATTE = "A latte with a shot of espresso and a layer of foam."
DHB_PRODUCT_PRICE_LATTE = 5

DHB_PRODUCT_ID_AMERICANO = "dhb-americano"
DHB_PRODUCT_IMAGE_AMERICANO = "https://i.nostr.build/0wXLDAPGpMf2Z0i5.jpg"
DHB_QUANTITY_AMERICANO = 90
DHB_PRODUCT_NAME_AMERICANO = "Dark Horse Brew Americano"
DHB_PRODUCT_DESCRIPTION_AMERICANO = "Thursday is Americano Day! $2.00"
DHB_PRODUCT_PRICE_AMERICANO = 5

DHB_PRODUCT_ID_MOCHA = "dhb-mocha"
DHB_PRODUCT_IMAGE_MOCHA = "https://i.nostr.build/0vc1IsrKKMOtlGbE.jpg"
DHB_QUANTITY_MOCHA = 90
DHB_PRODUCT_NAME_MOCHA = "Dark Horse Brew Mocha"
DHB_PRODUCT_DESCRIPTION_MOCHA = "Monday is Mocha Day! $3.00"
DHB_PRODUCT_PRICE_MOCHA = 6


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_dhb = StallShippingMethod(
    ssm_id=DHB_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=DHB_SHIPPING_ZONE_NAME,
    ssm_regions=DHB_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_dhb = ProductShippingCost(
    psc_id=DHB_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
dhb_stall = Stall(
    id=DHB_STALL_ID,
    name=DHB_STALL_NAME,
    description=DHB_STALL_DESCRIPTION,
    currency=DHB_CURRENCY,
    shipping=[shipping_method_dhb],
    geohash=DHB_GEOHASH,
)

# --*-- define products (using ShippingZone)
dhb_latte = Product(
    id=DHB_PRODUCT_ID_LATTE,
    stall_id=DHB_STALL_ID,
    name=DHB_PRODUCT_NAME_LATTE,
    description=DHB_PRODUCT_DESCRIPTION_LATTE,
    images=[DHB_PRODUCT_IMAGE_LATTE],
    currency=DHB_CURRENCY,
    price=DHB_PRODUCT_PRICE_LATTE,
    quantity=DHB_QUANTITY_LATTE,
    shipping=[shipping_cost_dhb],
    categories=["coffee", "latte"],
    specs=[
        ["temperature", "hot"],
        ["temperature", "cold"],
        ["size", "small"],
        ["size", "medium"],
        ["size", "large"],
    ],
)

dhb_americano = Product(
    id=DHB_PRODUCT_ID_AMERICANO,
    stall_id=DHB_STALL_ID,
    name=DHB_PRODUCT_NAME_AMERICANO,
    description=DHB_PRODUCT_DESCRIPTION_AMERICANO,
    images=[DHB_PRODUCT_IMAGE_AMERICANO],
    currency=DHB_CURRENCY,
    price=DHB_PRODUCT_PRICE_AMERICANO,
    quantity=DHB_QUANTITY_AMERICANO,
    shipping=[shipping_cost_dhb],
    categories=["coffee", "americano"],
    specs=[
        ["temperature", "hot"],
        ["temperature", "cold"],
        ["size", "small"],
        ["size", "medium"],
        ["size", "large"],
    ],
)

dhb_mocha = Product(
    id=DHB_PRODUCT_ID_MOCHA,
    stall_id=DHB_STALL_ID,
    name=DHB_PRODUCT_NAME_MOCHA,
    description=DHB_PRODUCT_DESCRIPTION_MOCHA,
    images=[DHB_PRODUCT_IMAGE_MOCHA],
    currency=DHB_CURRENCY,
    price=DHB_PRODUCT_PRICE_MOCHA,
    quantity=DHB_QUANTITY_MOCHA,
    shipping=[shipping_cost_dhb],
    categories=["coffee", "mocha"],
    specs=[
        ["temperature", "hot"],
        ["temperature", "cold"],
        ["size", "small"],
        ["size", "medium"],
        ["size", "large"],
    ],
)

profile = Profile(keys.get_public_key())
profile.set_name(DHB_NAME)
profile.set_about(DHB_DESCRIPTION)
profile.set_picture(DHB_PICTURE)
profile.set_website(DHB_WEBSITE)
profile.set_banner(DHB_BANNER)

stalls = [dhb_stall]
products: list[Product] = [dhb_latte, dhb_americano, dhb_mocha]
