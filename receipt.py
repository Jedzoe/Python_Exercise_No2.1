# receipt.py
from menu import menu


def print_receipt(orders, subtotal, discount, total):
    print("===================================")
    print("        TANSHONG'S FAST FOOD       ")
    print("          OFFICIAL RECEIPT         ")
    print("===================================")
    print(f"{'ITEM':<10}{'QTY':>5}{'PRICE':>10}{'TOTAL':>10}")
    print("-----------------------------------")

    for item, quantity in orders.items():
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
