# order.py

from Modular.menu import menu


def take_order():
    orders = {}

    while True:
        item = input("Enter menu item: ").title()

        if item not in menu:
            print("Item not found. Please choose from the menu.")
            continue

        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    break
                else:
                    print("Quantity must be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

        if item in orders:
            orders[item] += quantity
        else:
            orders[item] = quantity

        another = input(
            "Do you want to order another item? (yes/no): "
        ).lower()

        while another not in ["yes", "no"]:
            print("Please enter yes or no.")
            another = input(
                "Do you want to order another item? (yes/no): "
            ).lower()

        if another == "no":
            break

    return orders
