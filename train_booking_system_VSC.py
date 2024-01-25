'''train trial code 2'''

import sys
import random

# Intialize a variable for the passenger ticket
booking_data = []
booking_list = []

# Create dictionary in the global scope
# timetable must be a global variable
timetable = {
        'Malmö': {'Departure': '08:00', 'Arrival': '10:00'},
        'Uppsala': {'Departure': '08:00', 'Arrival': '09:30'},
        'Helsingborg': {'Departure': '09:00', 'Arrival': '11:00'},
        'Linköping': {'Departure': '10:00', 'Arrival': '11:30'},
        'Göteborg': {'Departure': '11:00', 'Arrival': '13:00'},
        'Karlstad': {'Departure': '19:00', 'Arrival': '21:00'},
        'Lund': {'Departure': '20:00', 'Arrival': '22:00'},
        'Jönköping': {'Departure': '20:00', 'Arrival': '22:00'},     
    }

fares = {
    'adult': 400,
    'child': 200,
    'pension': 300,
    'student': 300
}


# Create the display menu for the train trips
def display_timetable(timetable):      
   
    # prints the header
    print("\nTrain Timetable:")

    # print a dictionary, line by line, using for loop & dict.items()
    for city, times in timetable.items():
        # iterate over the keys and values in the dictionary
        departure = times['Departure']
        arrival = times['Arrival']
        
        # print timeline dictionary line by line
        print(f'{city}: Departure - {departure}, Arrival - {arrival}')

# Create the display menu for the train fares
def display_fares(fares):
    print("Train Fares")
    
    for passenger, price in fares.items():
        print(f'{passenger}: {price} SEK')

# Function to book train ticket
def book():
    while True:
        print("\nBook Train Ticket Menu selected. First, please choose your destination city.")
        for city in timetable:
            print(city)
        
        # Prompt user input for destination
        while True:
            destination_input = input("Please choose from the destinations. Please type your destination:  ")

            try:
                destination_input = (destination_input)
                
                if destination_input in timetable:
                    destination_key = f'[{destination_input}]'
                    select_destination = timetable.get(destination_key)
                    print(f'Destination City: {destination_key}') 
                    break 
                            
            except ValueError:
                print("Invalid Input. Please type your destination.")
        
        # Now, outside the inner loop, prompt user for passenger type
        passenger_input = input("Enter passenger type: 'adult, child, pension, student': ")

        # Check if the passenger type is in the fares dictionary
        if passenger_input.lower() in fares:
            # Retrieve the price from the fares dictionary
            price = fares[passenger_input.lower()]

        # Generate a random booking number
        booking_number = random.randint(1000, 9999)

        # Add booking information to the booking_data list
        booking_data.append({
                'BookingNumber': booking_number,
                'Destination City': destination_input,
                'PassengerType': passenger_input,
                'Price': price
            })
        
        # Add booking number to the booking_list
        booking_list.append(booking_number)

        # Print a summary of the ticket order
        print(f'\nTicket booked successfully!\nPlease give your booking number to the counter to pay and verify your ticket.\nBooking Number: {booking_number}')
        print(f'Destination: {destination_input}')
        print(f'Passenger Type: {passenger_input}')
        print(f'Price: {price} SEK')
        break  # Exit the loop after successful booking


# Function to cancel train booking
def cancel():
    print("\nTrain Booking Cancellation Menu")

    try:
        booking_number_input = int(input(" Type your booking number here: \n"))


        # check first if booking number is valid
        if booking_number_input in booking_list:
            # Retrieve the booking data using the booking number
            booking = next(item for item in booking_data if item["BookingNumber"] == booking_number_input)
            print("Booking Information:")
            print(f'Booking Number: {booking["BookingNumber"]}')
            print(f'Destination: {booking["Destination City"]}')
            print(f'Passenger Type: {booking["PassengerType"]}')
            print(f'Price: {booking["Price"]} SEK') 

                # Confirm cancellation
            confirmation = input("Do you really want to cancel this booking? (yes/no): ").lower()

            if confirmation == 'yes':
                print(f'Booking {booking_number_input} cancelled.\n')
                booking_data.remove(booking)
                return
            
            elif confirmation == 'no':
                print("Cancellation aborted.\n")
                return
            
            else:
                print("Type (yes/no)\n")
                

        print("Invalid booking number. Please try again.")
            
    except ValueError:
        print("Invalid booking number. Please try again")
    

# Function to exit the program
def exit_program():
    print("Program terminates")
    sys.exit()

while True:
    # Display menu and get user input
    option = input("\nMenu:\n [1] Display train timetable and passenger fares \n [2] Book a Ticket\n [3] Cancel Train Booking \n [4] Terminate Program \n Enter number here:  ")

    try:
        # converts input into integers, catches non-numeric input.
        option = int(option)

        if option == 1:
            display_timetable(timetable)
            print("\n")
            display_fares(fares)

            # Ask prompt if user wants to return to main menu
            return_menu = input("***Press any key to return to main menu. Press 'n' to exit***:  ").lower()
            if return_menu != 'n':
                print("Go back to main menu")
                continue
            elif return_menu == 'n':
                print("Booking stops. Goodbye!")
                break

        elif option == 2:
            book()

            # Ask prompt if user wants to return to main menu
            return_menu = input("***Press any key to return to main menu. Press 'n' to exit***:  ").lower()
            if return_menu != 'n':
                print("Go back to main menu")
                continue
            elif return_menu == 'n':
                print("Booking stops. Goodbye!")
                break

        elif option == 3:
            cancel()
        elif option == 4:
            exit_program()
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4")

    except ValueError:
        # Tells user to try again if ValueError is caught
        print("Wrong input. Please choose 1, 2, 3, or 4") 
