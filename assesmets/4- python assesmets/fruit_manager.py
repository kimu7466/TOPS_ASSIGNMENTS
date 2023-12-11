import datetime


# fruit_manager.py

# Dictionary to store fruit stock (initially empty)
# fruit_stock = {}
fruit_stock = {'apple': {'quantity': 10, 'price': 2.5}, 'banana': {'quantity': 15, 'price': 1.8}}

def display_manager_menu():
    print("\n\n\t\t\t Fruit Market Manager\n")
    print("\t\t\t 1) Add Fruit Stock")
    print("\t\t\t 2) View Fruit Stock")
    print("\t\t\t 3) Update Fruit Stock\n")

    pass

def write_to_the_text_file(filename):
    with open(filename, 'w') as file:
        file.write("fruit stock : \n")
        for fruit, details in fruit_stock.items():
            file.write(f"{fruit}: Quantity - {details['quantity']} kg, Price - {details['price']} per kg\n")


# Function to add fruit stock
def add_fruit_stock():
    while True:
        fruit_name = input("Enter fruit name: ")
        quantity = float(input("Enter quantity (in kg): "))
        price = float(input("Enter price (per kg): "))
        
        if fruit_name in fruit_stock:
            fruit_stock[fruit_name]['quantity'] += quantity
            fruit_stock[fruit_name]['price'] = price
        else:
            fruit_stock[fruit_name] = {'quantity': quantity, 'price': price}
        
        print(f"{quantity} kg of {fruit_name} added to stock at {price} per kg.")
        
        choice = input("Do you want to perform more operations? (y/n): ")
        if choice.lower() != 'y':
            break        
        
        pass

# Function to view fruit stock
def view_fruit_stock():
    if not fruit_stock:
        print("Fruit stock is empty.")
    else:
        print("Fruit Stock:\n")
        for fruit, details in fruit_stock.items():
            print(f"{fruit}: Quantity - {details['quantity']} kg, \n Price - {details['price']} per kg \n\n")

        pass

# Function to update fruit stock
def update_fruit_stock():

    while True:
        fruit_name = input("Enter fruit name to update: ")
        if fruit_name in fruit_stock:
            new_quantity = float(input("Enter new quantity (in kg): "))
            fruit_stock[fruit_name]['quantity'] = new_quantity
            print(f"{fruit_name} stock updated to {new_quantity} kg.")
            
            new_price = float(input("Enter new price (per kg): "))
            fruit_stock[fruit_name]['price'] = new_price
            print(f"{fruit_name} price updated to {new_price} kg.")

            choice = input("Do you want to perform more operations? (y/n): ")
            if choice.lower() != 'y':
                break        

        else:
            print(f"{fruit_name} not found in stock.")

        pass


def create_log_file(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a') as file:
        file.write(f"{timestamp}: {message}\n")

# If this module is run directly, execute a simple test scenario
if __name__ == "__main__":
    add_fruit_stock()
    view_fruit_stock()
    