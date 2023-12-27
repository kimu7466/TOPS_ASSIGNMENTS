import fruit_manager

def home():
    print("\n\n\t\t\t WELCOME TO THE FRUIT MARKET\n")
    print("\t\t\t 1) MANAGER")
    print("\t\t\t 2) CUSTOMER\n")
    print("\t\t\t 0) exit \n")

def run():
    try:
        while True:
            home()
            x = input("Select your role: ")
            
            if x == "1":
                fruit_manager.manage_operations()
            elif x == "2":
                # Perform operations for customer module
                print("Customer operations not implemented yet.")
                # Add your customer operations here
            elif x == "0":
                print("Thanks for coming, visit again.")
                break
            else:
                print("Invalid choice! Please select 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    run()

