from input_util import ask_yes_no
from menu import DISCOUNT_LIMIT
from menu import REGULAR_DISCOUNT
from menu import SENIOR_PWD_DISCOUNT


def apply_discount(subtotal):

    is_senior_pwd = ask_yes_no(
        "Are you a Senior Citizen or PWD?"
    )

    if is_senior_pwd:

        discount_amount = (
            subtotal * SENIOR_PWD_DISCOUNT
        )

        discount_label = "Senior/PWD Discount (20%)"

    elif subtotal >= DISCOUNT_LIMIT:

        discount_amount = (
            subtotal * REGULAR_DISCOUNT
        )

        discount_label = "Regular Discount (10%)"

    else:

        discount_amount = 0.00
        discount_label = "No Discount"

    return discount_amount, discount_label