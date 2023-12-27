# TO GET VIEW_STOCK IN DICTIONRY

import datetime

# Function to read fruit stock data from the text file
def read_from_text_file(filename):
    new_fruit_stock = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the first line as it contains header information
            fruit, details = line.strip().split(': ')
            fruit_name = fruit
            quantity, price = details.split(', ')
            quantity = float(quantity.split('- ')[1].split(' kg')[0])
            price = float(price.split('- ')[1].split(' per kg')[0])
            new_fruit_stock[fruit_name] = {'quantity': quantity, 'price': price}
    return new_fruit_stock
 
# Initial fruit stock data
fruit_stock = read_from_text_file('fruit_stock.txt')

def display_manager_menu():
    print("\n\n\t\t\t Fruit Market Manager\n")
    print("\t\t\t 1) Add Fruit Stock")
    print("\t\t\t 2) View Fruit Stock")
    print("\t\t\t 3) Update Fruit Stock\n")

# Function to write fruit stock data to the text file
def write_to_text_file(filename):
    with open(filename, 'w') as file:
        file.write("Fruit Stock:\n")
        for fruit, details in fruit_stock.items():
            file.write(f"{fruit}: Quantity - {details['quantity']} kg, Price - {details['price']} per kg\n")

# Function to create log file for manager operations
def create_log_file(operation, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a') as file:
        file.write(f"{timestamp}: {operation} - {message}\n")

# Function to add fruit stock with handling for non-numerical input
def add_fruit_stock():
    while True:
        fruit_name = input("Enter fruit name: ")

        # Handling for quantity input
        while True:
            try:
                quantity = float(input("Enter quantity (in kg): "))
                break  # Break the loop if input is successfully converted to float
            except ValueError:
                print("Please enter a valid numerical input for quantity.")

        # Handling for price input
        while True:
            try:
                price = float(input("Enter price (per kg): "))
                break  # Break the loop if input is successfully converted to float
            except ValueError:
                print("Please enter a valid numerical input for price.")

        if fruit_name in fruit_stock:
            fruit_stock[fruit_name]['quantity'] += quantity
            fruit_stock[fruit_name]['price'] = price
        else:
            fruit_stock[fruit_name] = {'quantity': quantity, 'price': price}

        print(f"{quantity} kg of {fruit_name} added to stock at {price} per kg.")

        # Logging the add operation
        message = f"Added {quantity} kg of {fruit_name} at {price} per kg."
        create_log_file("ADD", message)

        choice = input("Do you want to perform more operations? (y/n): ")
        if choice.lower() != 'y':
            break


# Function to view fruit stock in dictionary format
def view_fruit_stock():
    all_fruits = {}  # Initialize a dictionary for all fruits
    if not fruit_stock:
        print("Fruit stock is empty.")
    else:
        print("Fruit Stock:\n")
        for fruit, details in fruit_stock.items():
            print(f"{fruit}: Quantity - {details['quantity']} kg, Price - {details['price']} per kg\n")
            all_fruits[fruit] = details  # Add each fruit to the dictionary

        # Print the dictionary containing all fruits and their details
        print("\nAll Fruits in Dictionary Format:")
        print(all_fruits)


# Function to update fruit stock with handling for non-numerical input
def update_fruit_stock():
    while True:
        fruit_name = input("Enter fruit name to update: ")
        if fruit_name in fruit_stock:
            # Handling for updating quantity input
            while True:
                try:
                    new_quantity = float(input("Enter new quantity (in kg): "))
                    break  # Break the loop if input is successfully converted to float
                except ValueError:
                    print("Please enter a valid numerical input for quantity.")

            fruit_stock[fruit_name]['quantity'] = new_quantity
            print(f"{fruit_name} stock updated to {new_quantity} kg.")

            # Handling for updating price input
            while True:
                try:
                    new_price = float(input("Enter new price (per kg): "))
                    break  # Break the loop if input is successfully converted to float
                except ValueError:
                    print("Please enter a valid numerical input for price.")

            fruit_stock[fruit_name]['price'] = new_price
            print(f"{fruit_name} price updated to {new_price} kg.")

            # Logging the update operation
            message = f"Updated {fruit_name} stock to {new_quantity} kg and price to {new_price} per kg."
            create_log_file("UPDATE", message)

            choice = input("Do you want to perform more operations? (y/n): ")
            if choice.lower() != 'y':
                break
        else:
            print(f"{fruit_name} not found in stock.")
            break


# Function to save fruit stock to file and log changes
def save_fruit_stock_to_file():
    write_to_text_file('fruit_stock.txt')
    for fruit, details in fruit_stock.items():
        message = f"Status for {fruit} has been changed in stock. Changes: price {details['price']} & quantity {details['quantity']}"
        create_log_file("STATUS_CHANGE", message)

# Function to manage operations
def manage_operations():
    while True:
        display_manager_menu()
        choice = input("Enter your choice (1/2/3 - Add/View/Update; Any other key to exit): ")
        
        if choice == '1':
            add_fruit_stock()
        elif choice == '2':
            view_fruit_stock()
        elif choice == '3':
            update_fruit_stock()
        else:
            print("Exiting...")
            break

        save_fruit_stock_to_file()  # Save stock changes after each operation

# Running the manager to perform operations and log changes
if __name__ == "__main__":
    manage_operations()

