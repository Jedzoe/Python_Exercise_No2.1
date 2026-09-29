# customer.py

from menu import menu


class Customer:

    def __init__(self):
        self.orders = {}

    def take_order(self):
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

            if item in self.orders:
                self.orders[item] += quantity
            else:
                self.orders[item] = quantity

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

    def calculate_total(self):
        subtotal = 0

        for item, quantity in self.orders.items():
            subtotal += menu[item] * quantity

        if subtotal >= 500:
            discount = subtotal * 0.10
        elif subtotal >= 300:
            discount = subtotal * 0.05
        else:
            discount = 0

        total = subtotal - discount

        return subtotal, discount, total

    def print_receipt(self, subtotal, discount, total):
        print("===================================")
        print("        TANSHONG'S FAST FOOD       ")
        print("          OFFICIAL RECEIPT         ")
        print("===================================")
        print(f"{'ITEM':<10}{'QTY':>5}{'PRICE':>10}{'TOTAL':>10}")
        print("-----------------------------------")

        for item, quantity in self.orders.items():
            price = menu[item]
            item_total = price * quantity

            print(
                f"{item:<9}"
                f"{quantity:>5}"
                f"{price:>11.2f}"
                f"{item_total:>10.2f}"
            )

        print("-----------------------------------")
        print(f"{'Subtotal:':<27}{subtotal:>8.2f}")
        print(f"{'Discount:':<27}{discount:>8.2f}")
        print(f"{'TOTAL:':<27}{total:>8.2f}")
        print("===================================")
        print("       Thank you for ordering!")
        print("===================================")