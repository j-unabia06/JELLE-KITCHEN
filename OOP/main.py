import datetime


class Restaurant:

    def __init__(self):
        self.name = "JELLE'S KITCHEN"

        self.food_menu = {
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

        self.discount_limit = 1000.00
        self.regular_discount = 0.10
        self.senior_pwd_discount = 0.20

    def display_header(self, title):

        print("=" * 50)
        print(title.center(50))
        print("=" * 50)

    def display_menu(self):

        self.display_header(
            self.name + " MENU"
        )

        for category, items in self.food_menu.items():

            print()
            print(f"--- {category} ---")

            for item, price in items.items():

                print(
                    f"{item:<30} "
                    f"PHP {price:>8.2f}"
                )

        print()
        print("-" * 50)

    def ask_yes_no(self, question):

        while True:

            answer = input(
                question + " (yes/no): "
            ).strip().lower()

            if answer in ("yes", "y"):
                return True

            elif answer in ("no", "n"):
                return False

            print("Please enter yes or no.")

    def choose_item(self):

        while True:

            selected_item = input(
                "Enter item name: "
            ).strip()

            for category, items in self.food_menu.items():

                for item in items:

                    if item.lower() == selected_item.lower():
                        return item, category

            print("Item not found.")
            print("Please choose an item from the menu.")

    def enter_quantity(self):

        while True:

            quantity = input(
                "Enter quantity: "
            ).strip()

            if quantity.isdigit() and int(quantity) > 0:
                return int(quantity)

            print("Please enter a valid quantity.")

    def create_order(self):

        order_details = []

        while True:

            item, category = self.choose_item()

            quantity = self.enter_quantity()

            price = self.food_menu[category][item]

            order_details.append(
                (item, quantity, price)
            )

            print(
                f"\n{quantity} x {item} "
                f"has been added to your order."
            )

            if not self.ask_yes_no(
                "Would you like to order another item?"
            ):
                break

        return order_details

    def calculate_total(self, order_details):

        receipt_details = []
        subtotal = 0.00

        for item, quantity, price in order_details:

            item_total = quantity * price

            receipt_details.append(
                (item, quantity, price, item_total)
            )

            subtotal += item_total

        return receipt_details, subtotal

    def apply_discount(self, subtotal):

        is_senior_pwd = self.ask_yes_no(
            "Are you a Senior Citizen or PWD?"
        )

        if is_senior_pwd:

            discount_amount = (
                subtotal * self.senior_pwd_discount
            )

            discount_label = (
                f"Senior/PWD Discount "
                f"({int(self.senior_pwd_discount * 100)}%)"
            )

        elif subtotal >= self.discount_limit:

            discount_amount = (
                subtotal * self.regular_discount
            )

            discount_label = (
                f"Regular Discount "
                f"({int(self.regular_discount * 100)}%)"
            )

        else:

            discount_amount = 0.00
            discount_label = "No Discount"

        return discount_amount, discount_label

    def print_receipt(
        self,
        receipt_details,
        subtotal,
        discount_amount,
        discount_label,
        final_total
    ):

        print()

        self.display_header(self.name)

        print(
            "123 Main Street, Minglanilla, Cebu"
            .center(50)
        )

        current_date = datetime.datetime.now()

        print(
            current_date.strftime(
                "%d/%m/%Y %H:%M:%S"
            ).center(50)
        )

        print("-" * 50)

        print(
            f"{'ITEM':<20}"
            f"{'QTY':>6}"
            f"{'PRICE':>11}"
            f"{'TOTAL':>11}"
        )

        print("-" * 50)

        for item, quantity, price, item_total in receipt_details:

            print(
                f"{item:<20}"
                f"{quantity:>6}"
                f"{price:>11.2f}"
                f"{item_total:>11.2f}"
            )

        print("-" * 50)

        print(
            f"{'SUBTOTAL':<37}"
            f"{subtotal:>13.2f}"
        )

        print(
            f"{discount_label:<37}"
            f"{-discount_amount:>13.2f}"
        )

        print("-" * 50)

        print(
            f"{'TOTAL AMOUNT':<37}"
            f"{final_total:>13.2f}"
        )

        print("=" * 50)

        print(
            "Thank you for dining with us!"
            .center(50)
        )

        print(
            "We hope to see you again!"
            .center(50)
        )

        print("=" * 50)

    def run_program(self):

        self.display_menu()

        place_order = self.ask_yes_no(
            "Would you like to place an order?"
        )

        if not place_order:

            print()
            print(
                f"Thank you for visiting "
                f"{self.name}!"
            )
            print("Have a wonderful day!")

            return

        print()

        customer_order = self.create_order()

        receipt_details, subtotal = (
            self.calculate_total(customer_order)
        )

        discount_amount, discount_label = (
            self.apply_discount(subtotal)
        )

        final_total = subtotal - discount_amount

        self.print_receipt(
            receipt_details,
            subtotal,
            discount_amount,
            discount_label,
            final_total
        )


restaurant = Restaurant()
restaurant.run_program()