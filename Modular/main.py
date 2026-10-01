from menu import FOOD_MENU, RESTAURANT_NAME, display_menu
from input_util import ask_yes_no
from order import create_order, calculate_total
from discount import apply_discount
from receipt import print_receipt


def run_program():

    display_menu(FOOD_MENU)

    place_order = ask_yes_no(
        "Would you like to place an order?"
    )

    if not place_order:

        print()
        print(
            f"Thank you for visiting "
            f"{RESTAURANT_NAME}!"
        )
        print("Have a wonderful day!")

        return

    print()

    customer_order = create_order(FOOD_MENU)

    receipt_details, subtotal = calculate_total(
        customer_order
    )

    discount_amount, discount_label = apply_discount(
        subtotal
    )

    final_total = subtotal - discount_amount

    print_receipt(
        receipt_details,
        subtotal,
        discount_amount,
        discount_label,
        final_total
    )


if __name__ == "__main__":
    run_program()