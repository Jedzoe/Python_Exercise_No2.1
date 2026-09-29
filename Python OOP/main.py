# main.py

from menu import menu
from customer import Customer


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

    # Create Customer object
    customer = Customer()

    # Customer takes the order
    customer.take_order()

    if len(customer.orders) == 0:
        print("No orders were made.")
        return

    # Calculate the bill
    subtotal, discount, total = customer.calculate_total()

    # Print receipt
    customer.print_receipt(
        subtotal,
        discount,
        total
    )


if __name__ == "__main__":
    main()