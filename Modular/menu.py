RESTAURANT_NAME = "JELLE'S KITCHEN"

FOOD_MENU = {
    "MAIN COURSES": {
        "Burger": 150.00,
        "Fried Chicken": 140.00,
        "Spaghetti": 120.00,
        "Pizza": 180.00,
        "Steak": 250.00,
        "Chicken Sandwich": 130.00,
        "French Fries": 80.00,
        "Chicken Wings": 160.00,
        "Fish and Chips": 170.00,
        "Grilled Chicken": 150.00
    },

    "DESSERTS": {
        "Ice Cream": 70.00,
        "Chocolate Cake": 100.00,
        "Cheesecake": 120.00,
        "Donut": 60.00,
        "Brownie": 80.00
    },

    "DRINKS": {
        "Coca-Cola": 50.00,
        "Iced Tea": 50.00,
        "Lemonade": 60.00,
        "Milkshake": 90.00,
        "Hot Coffee": 70.00
    }
}


DISCOUNT_LIMIT = 1000.00
REGULAR_DISCOUNT = 0.10
SENIOR_PWD_DISCOUNT = 0.20


def display_header(title):
    width = 50

    print("=" * width)
    print(title.center(width))
    print("=" * width)


def display_menu(menu):

    display_header(RESTAURANT_NAME + " MENU")

    for category, items in menu.items():

        print()
        print(f"--- {category} ---")

        for item, price in items.items():
            print(f"{item:<30} PHP {price:>8.2f}")

    print()
    print("-" * 50)


def choose_item(menu):

    while True:

        selected_item = input("Enter item name: ").strip()

        for category, items in menu.items():

            for item in items:

                if item.lower() == selected_item.lower():
                    return item, category

        print("Item not found.")
        print("Please choose an item from the menu.")