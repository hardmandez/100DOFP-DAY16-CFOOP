from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_maker_menu = Menu()
# coffee_maker_item = MenuItem()

payment_received = 0


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
    elif choice in coffee_maker_menu.get_items():
        #Check resources.
        drink_order = coffee_maker_menu.find_drink(choice)
        machine_has_resources = coffee_maker.is_resource_sufficient(drink_order)
        if machine_has_resources:
            payment_received = money_machine.make_payment(drink_order.cost)
            if payment_received:
                coffee_maker.make_coffee(drink_order)
    else:
        print("Invalid choice.")
