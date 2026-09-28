# billing.py
from menu import menu


def calculate_total(orders):
    subtotal = 0

    for item, quantity in orders.items():
        subtotal += menu[item] * quantity

    # Apply discount based on the subtotal
    if subtotal >= 500:
        discount = subtotal * 0.10
    elif subtotal >= 300:
        discount = subtotal * 0.05
    else:
        discount = 0

    total = subtotal - discount

    return subtotal, discount, total
