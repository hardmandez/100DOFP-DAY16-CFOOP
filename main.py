from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_maker_menu = Menu()
# coffee_maker_menu_item = MenuItem()
choice = ""
machine_on = True

# Get users input.
while machine_on:

    choice = input(f"Make a drink selection {coffee_maker_menu.get_items()}.").lower()

    #Check input
    if choice == "off":
        print("Powering off...")
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_maker_menu.find_drink(choice)
        print("Thank you for choosing.")
        payment = money_machine.make_payment()

