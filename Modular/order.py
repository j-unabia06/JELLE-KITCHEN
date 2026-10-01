from input_util import ask_yes_no, enter_quantity


def create_order(menu):

    order_details = []

    while True:

        selected_item, category = choose_item(menu)

        quantity = enter_quantity()

        price = menu[category][selected_item]

        order_details.append(
            (selected_item, quantity, price)
        )

        print(
            f"\n{quantity} x {selected_item} "
            f"has been added to your order."
        )

        if not ask_yes_no(
            "Would you like to order another item?"
        ):
            break

    return order_details


def calculate_total(order_details):

    receipt_details = []
    subtotal = 0.00

    for item, quantity, price in order_details:

        item_total = quantity * price

        receipt_details.append(
            (item, quantity, price, item_total)
        )

        subtotal += item_total

    return receipt_details, subtotal