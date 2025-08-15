from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_maker_menu = Menu()
coffee_maker_item = MenuItem()

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
    else:
        #Validate choice.
        required_resources = [coffee_maker_menu.find_drink(choice)]
        print(required_resources)
        print("Thank you for choosing.")
        #Check resources.

        #Take payment.
        # payment_received += money_machine.process_coins()
        # print(payment_received)

        money_machine.make_payment(3)

        #Process payment.
        ##Get Cost
        resources = coffee_maker.is_resource_sufficient(choice)
        if resources:
            print ("Resources available!")
        else:
            print ("You don't have enough resources. Call the administrator.")

