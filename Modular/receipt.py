import datetime

from menu import RESTAURANT_NAME, display_header


def print_receipt(
    receipt_details,
    subtotal,
    discount_amount,
    discount_label,
    final_total
):

    print()

    display_header(RESTAURANT_NAME)

    print("123 Main Street, Minglanilla, Cebu".center(50))

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
        "Thank you for dining with us!".center(50)
    )

    print(
        "We hope to see you again!".center(50)
    )

    print("=" * 50)