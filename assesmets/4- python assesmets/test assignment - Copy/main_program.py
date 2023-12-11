import fruit_manager
import customer

def display_customer_menu():
    customer.print_hello()

def home():
    print("\n\n\t\t\t WELCOME TO THE FRUIT MARKET\n")
    print("\t\t\t 1) MANAGER")
    print("\t\t\t 2) CUSTOMER\n")
    print("\t\t\t 0) exit \n")

def run():
    try:
        x = int(input("select your role : "))
        if x == 1:
            fruit_manager.display_manager_menu()
            y = int(input("enter your choice : "))
            if y == 1:
                fruit_manager.add_fruit_stock()
                home()
                run()
            elif y == 2:
                fruit_manager.view_fruit_stock()
                main_menu = input("enter anything for main menu ")
                if main_menu == '1':
                    home()
                    run()
                else:
                    home()
                    run()
            elif y == 3:
                fruit_manager.update_fruit_stock()
                home()
                run()
            else:
                print("you have entered an incorrect input, \n please select from below option.")
                home()
                run()
        elif x == 2:
            customer.print_hello()
            main_menu = input("enter anything for main menu ")
            if main_menu == '1':
                home()
                run()
            else:
                home()
                run()
        elif x == 0:
            print("thanks for coming, visit again.")
        else:
            print("Invalid choice! Please select 1 or 2.")
            home()
            run()
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        home()
        run()

home()
run()
