# main.py
from menu import menu
from order import take_order
from billing import calculate_total
from receipt import print_receipt


def display_menu():
    print("================================")
    print("      TANSHONG'S FAST FOOD      ")
    print("              MENU              ")
    print("================================")

    for item, price in menu.items():
        print(f"  {item:<21} ₱{price:.2f}")

    print("================================")


def main():
    display_menu()

    choice = input("Do you want to order? (yes/no): ").lower()

    while choice not in ["yes", "no"]:
        print("Please enter yes or no.")
        choice = input(
            "Do you want to order? (yes/no): "
        ).lower()

    if choice == "no":
        print("Thank you! Have a nice day!")
        return

    orders = take_order()

    if len(orders) == 0:
        print("No orders were made.")
        return

    subtotal, discount, total = calculate_total(orders)

    print_receipt(orders, subtotal, discount, total)


if __name__ == "__main__":
    main()
