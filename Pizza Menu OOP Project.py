# Trial 2Python Pizza Code. Build an automatic pizza order program.
print("Thank you for choosing Python Pizza Deliveries!\n")

# Define a BASE CLASS for menu items
class MenuItem:
    # constructor "__init__" that initializes the name and price attributes.
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # method to display the menu item details
    def display(self):
        print(f'{self.name}..... ${self.price}')


# Define a SUBCLASS for extra items, inheriting from MenuItem
class Extra(MenuItem):
    def __init__(self, name, price):
        # Call the constructor of the base and prepend "Extra" to the name
        super().__init__(f'Extra {name}', price)


# Define a class for a menu, with a list of menu items
class Menu:
    def __init__(self, name, items, start_number = 1):
        self.name = name
        self.items = items          
        self.start_number = start_number

    def display(self):
        # Display the menu name and iterate over each item to display details
        print(f'{self.name} Menu:')
        for i, item in enumerate (self.items, start = self.start_number):
            print(f'{i}. ', end = ' ')
            item.display()
        print()

# Define a class to represent orders
class Order:
    def __init__(self, pizza, size, extras):
        self.pizza = pizza
        self.size = size
        self.extras = extras
    
    def display(self):
        print(f'Total Order: {self.pizza.name} ({self.size.name})')

        if self.extras:
            print('Extra Toppings: ')
            for extra in self.extras:
                print(f' {extra.name} (${extra.price})')
        

    


# Create instances of Menu, MenuItem, and Extra to represent different menus and items
pizza_menu = Menu("Pizza", [
    MenuItem("Margherita", 10),
    MenuItem("Pepperon", 12),
    MenuItem("Veggie", 14),
    MenuItem("Meat Lover", 16)
], start_number= 1) # Start numbering from 1

extra_menu = Menu("Extras", [
    Extra("Pepperoni", 3),
    Extra("Vegetables", 5),
    Extra("Cheese", 6),
    Extra("Prosciutto", 7)
])

size_menu = Menu("Sizes", [
    MenuItem("Medium", 5),
    MenuItem("Large", 7)
])

# Display each menu
pizza_menu.display()
size_menu.display()
extra_menu.display()


# bill to iterate total price
bill = 0

# list to store orders
orders_list = []

# Create a while loop for the order-making process
# Ask for pizza choice
while True:
    try:
        # converts input into integers, catches non-numeric input.
        pizza_choice = int(input(f'1. Choose your pizza from our Pizza menu (1-{len(pizza_menu.items)}).\nYour pizza choice: '))
        if 1 <= pizza_choice <= len(pizza_menu.items):
            selected_pizza = pizza_menu.items[pizza_choice -1]
            bill += selected_pizza.price
            print(f'Order: {selected_pizza.name}, ${selected_pizza.price}.\n')

            # Break out of the pizza order loop after successful order
            break
        else:
            print("Invalid pizza number choice. Please choose 1, 2, 3, or 4\n")

    except ValueError:
        # Tells user to try again if ValueError is caught
        print("Wrong input. Please choose 1, 2, 3, or 4\n")

# Ask for sizes
while True:
    size_choice = input("2. Do you want to upgrade pizza sizes? (y, n)\n").lower()

    if size_choice == "y":
        print("Choose upgrade size: (1)Medium or (2)Large")
        for i, size_item in enumerate(size_menu.items, start=1):
            print(f'{i}. {size_item.name}.... (${size_item.price})')

        try:
            size_upgrade = int(input("Size: "))
            if 1 <= size_upgrade <= len(size_menu.items):
                selected_size = size_menu.items[size_upgrade -1]
                bill += selected_size.price
                print(f'Order upgraded to: {selected_size.name}, ${selected_size.price}.\n')
                break  # Exit the size upgrade loop if the input is valid
            else:
                print("Invalid size choice. Please choose 1 or 2.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    elif size_choice == "n":
        print("No additional size upgrade.\n")
        break  # Exit the size upgrade loop if the input is 'n'
    else:
        print("Invalid. Please choose 'y' or 'n'\n")


# Ask for extra toppings
while True: 
    try:
        toppings_choice = input("3. Do you want to add extra toppings? (y, n)\n").lower()
        
        if toppings_choice == 'y':
            print("Choose extra toppings: \n")
            selected_extra_toppings = []  # Store selected extra toppings for the current order
            for i, extra_item in enumerate(extra_menu.items, start=1):
                print(f'{i}. {extra_item.name}.... (${extra_item.price})')
                  
            while True:
                try:
                    extra_toppings_choice = int(input("Extra Topping: "))
                    if 1 <= extra_toppings_choice <= len(extra_menu.items):
                        selected_extra_topping = extra_menu.items[extra_toppings_choice - 1]
                        bill += selected_extra_topping.price
                        print(f'Extra Topping added: {selected_extra_topping.name}, ${selected_extra_topping.price}\n')
                        selected_extra_toppings.append(selected_extra_topping)

                    else:
                        print("Invalid choice. Please choose a valid option.\n")

                    # Ask if the user wants to add more extra toppings
                    more_toppings_choice = input("Add more extra toppings? (y, n)\n").lower()
                    if more_toppings_choice == 'n':
                        break  # Exit the inner loop if the user chooses 'n'

                except ValueError:
                    print("Invalid input. Please type the number.\n")
                
            current_order = Order(selected_pizza, selected_size, selected_extra_toppings)
            orders_list.append(current_order)

        elif toppings_choice == 'n':
            print("No additional toppings upgrade.\n")     
            break  # Exit the size upgrade loop if the input is 'n'

        else:
              print("Invalid. Please choose 'y' or 'n")
              break  # Exit the size upgrade loop if the input is 'n'
    except ValueError:
        print("Wrong input. Please choose 1, 2, 3, or 4\n")


current_order = Order(selected_pizza, selected_size, [])
orders_list.append(current_order)

# Display the current bill
for order in orders_list:
    order.display()
    print(f'Total Price: ${bill}\n')