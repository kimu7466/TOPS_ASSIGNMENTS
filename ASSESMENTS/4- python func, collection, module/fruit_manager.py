import datetime


def read_from_text_file(filename):
    new_fruit_stock = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  
            fruit, details = line.strip().split(': ')
            fruit_name = fruit
            quantity, price = details.split(', ')
            quantity = float(quantity.split('- ')[1].split(' kg')[0])
            price = float(price.split('- ')[1].split(' per kg')[0])
            new_fruit_stock[fruit_name] = {'quantity': quantity, 'price': price}
    return new_fruit_stock
 

fruit_stock = read_from_text_file('fruit_stock.txt')

def display_manager_menu():
    print("\n\n\t\t\t Fruit Market Manager\n")
    print("\t\t\t 1) Add Fruit Stock")
    print("\t\t\t 2) View Fruit Stock")
    print("\t\t\t 3) Update Fruit Stock\n")


def write_to_text_file(filename):
    with open(filename, 'w') as file:
        file.write("Fruit Stock:\n")
        for fruit, details in fruit_stock.items():
            file.write(f"{fruit}: Quantity - {details['quantity']} kg, Price - {details['price']} per kg\n")


def create_log_file(operation, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a') as file:
        file.write(f"{timestamp}: {operation} - {message}\n")


def add_fruit_stock():
    while True:
        fruit_name = input("Enter fruit name: ")

        
        while True:
            try:
                quantity = float(input("Enter quantity (in kg): "))
                break  
            except ValueError:
                print("Please enter a valid numerical input for quantity.")

        
        while True:
            try:
                price = float(input("Enter price (per kg): "))
                break  
            except ValueError:
                print("Please enter a valid numerical input for price.")

        if fruit_name in fruit_stock:
            fruit_stock[fruit_name]['quantity'] += quantity
            fruit_stock[fruit_name]['price'] = price
        else:
            fruit_stock[fruit_name] = {'quantity': quantity, 'price': price}

        print(f"{quantity} kg of {fruit_name} added to stock at {price} per kg.")

        
        message = f"Added {quantity} kg of {fruit_name} at {price} per kg."
        create_log_file("ADD", message)

        choice = input("Do you want to perform more operations? (y/n): ")
        if choice.lower() != 'y':
            break



def view_fruit_stock():
    all_fruits = {}  
    if not fruit_stock:
        print("Fruit stock is empty.")
    else:
        print("Fruit Stock:\n")
        for fruit, details in fruit_stock.items():
            print(f"{fruit}: Quantity - {details['quantity']} kg, Price - {details['price']} per kg\n")
            all_fruits[fruit] = details  

        
        print("\nAll Fruits in Dictionary Format:")
        print(all_fruits)



def update_fruit_stock():
    while True:
        fruit_name = input("Enter fruit name to update: ")
        if fruit_name in fruit_stock:
            
            while True:
                try:
                    new_quantity = float(input("Enter new quantity (in kg): "))
                    break  
                except ValueError:
                    print("Please enter a valid numerical input for quantity.")

            fruit_stock[fruit_name]['quantity'] = new_quantity
            print(f"{fruit_name} stock updated to {new_quantity} kg.")

            
            while True:
                try:
                    new_price = float(input("Enter new price (per kg): "))
                    break  
                except ValueError:
                    print("Please enter a valid numerical input for price.")

            fruit_stock[fruit_name]['price'] = new_price
            print(f"{fruit_name} price updated to {new_price} kg.")

            
            message = f"Updated {fruit_name} stock to {new_quantity} kg and price to {new_price} per kg."
            create_log_file("UPDATE", message)

            choice = input("Do you want to perform more operations? (y/n): ")
            if choice.lower() != 'y':
                break
        else:
            print(f"{fruit_name} not found in stock.")
            break



def save_fruit_stock_to_file():
    write_to_text_file('fruit_stock.txt')
    for fruit, details in fruit_stock.items():
        message = f"Status for {fruit} has been changed in stock. Changes: price {details['price']} & quantity {details['quantity']}"
        create_log_file("STATUS_CHANGE", message)


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

        save_fruit_stock_to_file()  


if __name__ == "__main__":
    manage_operations()

