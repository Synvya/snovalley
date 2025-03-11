"""
Sample data for the Copperstone merchant.
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

ENV_KEY = "COPPERSTONE_AGENT_KEY"

# Get directory where the script is located
script_dir = Path(__file__).parent
# Load .env from the script's directory
load_dotenv(script_dir / "../.env")

# Load or generate keys
nsec = getenv(ENV_KEY)
if nsec is None:
    keys = generate_keys(env_var=ENV_KEY, env_path=script_dir / "../.env")
else:
    keys = NostrKeys.from_private_key(nsec)

# --*-- Merchant info
COPPERSTONE_NAME = "Copperstone"
COPPERSTONE_DESCRIPTION = "Copperstone Family Spaguetti Restaurant"
COPPERSTONE_PICTURE = "https://i.nostr.build/bBJwcS75wKhGtbhV.png"
COPPERSTONE_CURRENCY = "USD"
COPPERSTONE_GEOHASH = "C23Q7U36W"
COPPERSTONE_WEBSITE = "https://www.copperstonepasta.com/"
COPPERSTONE_BANNER = "https://i.nostr.build/nd2xUvv1s99vy6hD.jpg"

# --*-- Stall for ride at 11am
COPPERSTONE_STALL_NAME = "Copperstone"
COPPERSTONE_STALL_ID = "copperstone-stall-snoqualmie"
COPPERSTONE_STALL_DESCRIPTION = """
Italian dining with a warm environment, impeccable service & friendly staff. Serving
large, family-style portions that accommodate a wide variety of tastes. No Dish is
pre-cooked.... we take pride in serving you fresh, simply delicious cuisine!
Pizza, pasta, salads, desserts, drinks, and more!
Opening Hours:
 - Monday Closed 
 - Tuesday-Thursday 11:30AM – 8:30PM
 - Friday & Saturday 11:30AM – 9:30PM
 - Sunday 11:30AM – 8:30PM
Address: 8072 Railroad Ave, Snoqualmie, WA 98065
""".strip()

# --*-- Shipping info
COPPERSTONE_SHIPPING_ZONE_NAME = "Worldwide"
COPPERSTONE_SHIPPING_ZONE_ID = "copperstone-sz"
COPPERSTONE_SHIPPING_ZONE_REGIONS = ["Eat Here", "Take Out"]

# --*-- Copperstone Product info
COPPERSTONE_PRODUCT_ID_RESERVATION = "copperstone-reservation"
COPPERSTONE_PRODUCT_IMAGE_RESERVATION = "https://i.nostr.build/y0oziHDngPjjDbGO.png"
COPPERSTONE_QUANTITY_RESERVATION = 90
COPPERSTONE_PRODUCT_NAME_RESERVATION = "Dine in reservation"
COPPERSTONE_PRODUCT_DESCRIPTION_RESERVATION = (
    "Dine in reservation for Copperstone Family Spaguetti Restaurant"
)
COPPERSTONE_PRODUCT_PRICE_RESERVATION = 0

COPPERSTONE_PRODUCT_ID_PIZZA_PEPPERONI = "copperstone-pizza-pepperoni"
COPPERSTONE_PRODUCT_IMAGE_PIZZA_PEPPERONI = "https://i.nostr.build/L8nCZQ2yYWrNEYOq.jpg"
COPPERSTONE_QUANTITY_PIZZA_PEPPERONI = 90
COPPERSTONE_PRODUCT_NAME_PIZZA_PEPPERONI = "Pizza Spicy Pepperoni"
COPPERSTONE_PRODUCT_DESCRIPTION_PIZZA_PEPPERONI = (
    "Pepperoni, Mozzarella & marinara sauce"
)
COPPERSTONE_PRODUCT_PRICE_PIZZA_PEPPERONI = 22

COPPERSTONE_PRODUCT_ID_ALFREDO = "copperstone-alfredo"
COPPERSTONE_PRODUCT_IMAGE_ALFREDO = "https://i.nostr.build/gsY29K4PZIITHxWX.jpg"
COPPERSTONE_QUANTITY_ALFREDO = 90
COPPERSTONE_PRODUCT_NAME_ALFREDO = "Classic Alfredo"
COPPERSTONE_PRODUCT_DESCRIPTION_ALFREDO = (
    "Fettuccine in rich garlic cream sauce & Parmesan"
)
COPPERSTONE_PRODUCT_PRICE_ALFREDO = 18


# --*-- Define Shipping methods for stalls (nostr SDK type)
shipping_method_copperstone = StallShippingMethod(
    ssm_id=COPPERSTONE_SHIPPING_ZONE_ID,
    ssm_cost=0,
    ssm_name=COPPERSTONE_SHIPPING_ZONE_NAME,
    ssm_regions=COPPERSTONE_SHIPPING_ZONE_REGIONS,
)

# --*-- Define Shipping costs for products (nostr SDK type)
shipping_cost_copperstone = ProductShippingCost(
    psc_id=COPPERSTONE_SHIPPING_ZONE_ID,
    psc_cost=0,
)

# --*-- define stalls (using ShippingMethod)
copperstone_stall = Stall(
    id=COPPERSTONE_STALL_ID,
    name=COPPERSTONE_STALL_NAME,
    description=COPPERSTONE_STALL_DESCRIPTION,
    currency=COPPERSTONE_CURRENCY,
    shipping=[shipping_method_copperstone],
    geohash=COPPERSTONE_GEOHASH,
)

# --*-- define products (using ShippingZone)
copperstone_reservation = Product(
    id=COPPERSTONE_PRODUCT_ID_RESERVATION,
    stall_id=COPPERSTONE_STALL_ID,
    name=COPPERSTONE_PRODUCT_NAME_RESERVATION,
    description=COPPERSTONE_PRODUCT_DESCRIPTION_RESERVATION,
    images=[COPPERSTONE_PRODUCT_IMAGE_RESERVATION],
    currency=COPPERSTONE_CURRENCY,
    price=COPPERSTONE_PRODUCT_PRICE_RESERVATION,
    quantity=COPPERSTONE_QUANTITY_RESERVATION,
    shipping=[shipping_cost_copperstone],
    categories=["reservation", "italian", "lunch", "dinner", "tourism"],
    specs=[
        ["menu", "starters"],
        ["menu", "pasta"],
        ["menu", "salads"],
        ["menu", "desserts"],
        ["menu", "drinks"],
    ],
)

copperstone_pizza_pepperoni = Product(
    id=COPPERSTONE_PRODUCT_ID_PIZZA_PEPPERONI,
    stall_id=COPPERSTONE_STALL_ID,
    name=COPPERSTONE_PRODUCT_NAME_PIZZA_PEPPERONI,
    description=COPPERSTONE_PRODUCT_DESCRIPTION_PIZZA_PEPPERONI,
    images=[COPPERSTONE_PRODUCT_IMAGE_PIZZA_PEPPERONI],
    currency=COPPERSTONE_CURRENCY,
    price=COPPERSTONE_PRODUCT_PRICE_PIZZA_PEPPERONI,
    quantity=COPPERSTONE_QUANTITY_PIZZA_PEPPERONI,
    shipping=[shipping_cost_copperstone],
    categories=["pizza", "pepperoni", "italian", "lunch", "dinner"],
    specs=[
        ["ingredients", "pepperoni"],
        ["ingredients", "mozzarella"],
        ["ingredients", "marinara sauce"],
    ],
)

copperstone_alfredo = Product(
    id=COPPERSTONE_PRODUCT_ID_ALFREDO,
    stall_id=COPPERSTONE_STALL_ID,
    name=COPPERSTONE_PRODUCT_NAME_ALFREDO,
    description=COPPERSTONE_PRODUCT_DESCRIPTION_ALFREDO,
    images=[COPPERSTONE_PRODUCT_IMAGE_ALFREDO],
    currency=COPPERSTONE_CURRENCY,
    price=COPPERSTONE_PRODUCT_PRICE_ALFREDO,
    quantity=COPPERSTONE_QUANTITY_ALFREDO,
    shipping=[shipping_cost_copperstone],
    categories=["pasta", "italian", "lunch", "dinner"],
    specs=[
        ["ingredients", "fettuccine"],
        ["ingredients", "garlic cream sauce"],
        ["ingredients", "parmesan"],
    ],
)

profile = Profile(keys.get_public_key())
profile.set_name(COPPERSTONE_NAME)
profile.set_about(COPPERSTONE_DESCRIPTION)
profile.set_picture(COPPERSTONE_PICTURE)
profile.set_website(COPPERSTONE_WEBSITE)
profile.set_banner(COPPERSTONE_BANNER)
stalls = [copperstone_stall]
products: list[Product] = [
    copperstone_reservation,
    copperstone_pizza_pepperoni,
    copperstone_alfredo,
]
