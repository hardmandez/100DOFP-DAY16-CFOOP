from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_maker_menu = Menu()
# coffee_maker_menu_item = MenuItem()
choice = ""


# Get users input.

# choice = input(f"Make a drink selection {coffee_maker_menu.get_items()}.")
while choice != coffee_maker_menu.find_drink(choice) or choice != "off" or choice != "report":
    choice = input(f"Make a drink selection {coffee_maker_menu.get_items()}.")



