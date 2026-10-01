def ask_yes_no(question):

    while True:

        answer = input(question + " (yes/no): ").strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def enter_quantity():

    while True:

        quantity = input("Enter quantity: ").strip()

        if quantity.isdigit() and int(quantity) > 0:
            return int(quantity)

        print("Please enter a valid quantity.")