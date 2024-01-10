import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import mysql.connector
from mysql.connector import Error
from main_state_districts import states_and_districts
from show_guest_list import search_by_number

class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")

        self.create_main_interface()

    def create_main_interface(self):
        welcome_heading = tk.Label(self.root, text="WELCOME", font=("Arial", 50, "bold"))
        welcome_heading.pack(padx=20, pady=20)

        frame2 = tk.Frame(self.root, width=100, height=200)
        frame2.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        right_frame = tk.Frame(self.root, width=100, height=200)
        right_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        heading1 = tk.Label(right_frame, text="HOTEL MANAGEMENT", font=("bolden", 50, "bold"))
        heading1.pack(padx=20, pady=20)

        heading2 = tk.Label(right_frame, text="PYTHON TKINTER", font=("bolden", 60, "bold"))
        heading2.pack(padx=20, pady=20)

        heading3 = tk.Label(right_frame, text="GUI", font=("bolden", 100, "bold"))
        heading3.pack(padx=20, pady=20)

        left_frame = tk.Frame(self.root, width=200, height=100)
        left_frame.pack(side="bottom", padx=10, pady=10, fill="both", expand=True)

        button1 = tk.Button(left_frame, text="1. CHECK INN", command=self.check_inn_window, width=50, height=5)
        button1.pack(padx=20, pady=5)

        button2 = tk.Button(
    left_frame,
    text="2. SHOW GUEST LIST",
    command=search_by_number,  
    width=50,
    height=5
)
        button2.pack(padx=20, pady=5)


        button3 = tk.Button(left_frame, text="3. CHECK OUT", width=50, height=5)
        button3.pack(padx=20, pady=5)

        button4 = tk.Button(left_frame, text="4. GET INFO OF ANY GUEST", command=self.open_registration, width=50, height=5)
        button4.pack(padx=20, pady=5)

        button5 = tk.Button(left_frame, text="5. EXIT", command=self.root.quit, width=50, height=5)
        button5.pack(padx=20, pady=5)

    def check_inn_window(self):

        def create_database():
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root'
                )
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS HOTEL_MANAGEMENT")
                connection.close()
            except mysql.connector.Error as error:
                print(f"Error creating database: {error}")

        def create_table():
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='HOTEL_MANAGEMENT'
                )
                cursor = connection.cursor()

                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS check_inn_table (
                        ID INT AUTO_INCREMENT PRIMARY KEY,
                        Name VARCHAR(255),
                        Address VARCHAR(255),
                        Number VARCHAR(20),
                        Duration INT,
                        RoomType VARCHAR(50),
                        PaymentMode VARCHAR(50)
                    )
                ''')

                connection.close()
            except mysql.connector.Error as error:
                print(f"Error creating table: {error}")

        def save_to_database(name, address, number, duration, room_type, payment_mode):
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='hotel_management'
                )
                cursor = connection.cursor()

                insert_query = '''
                    INSERT INTO check_inn_table (Name, Address, Number, Duration, RoomType, PaymentMode)
                    VALUES (%s, %s, %s, %s, %s, %s)
                '''
                cursor.execute(insert_query, (name, address, number, duration, room_type, payment_mode))

                connection.commit()
                connection.close()
                scrolled_text.insert(tk.END, "\n Data saved to the database.\n")
            except mysql.connector.Error as error:
                scrolled_text.insert(tk.END, f"Error: {error}\n")

        create_database()
        create_table()

        def on_room_type_select(value):
            room_type_var.set(value)

        def on_payment_mode_select(value):
            payment_mode_var.set(value)
    
        def submit_clicked():
            room_type = room_type_var.get()
            payment_mode = payment_mode_var.get()

            name = name_entry.get().strip()
            address = address_entry.get().strip()
            number = number_entry.get().strip()
            duration = duration_entry.get().strip()
        
            save_to_database(name, address, number, duration, room_type, payment_mode)

        def validate_mobile_number(number):
            return len(number) == 10 and number.isdigit()

        def name_ok_clicked():
            name = name_entry.get()
            if name.strip() != "":
                scrolled_text.insert(tk.END, "\nName has been inputted.")
            else:
                scrolled_text.insert(tk.END, "\nPlease enter a valid name.")

        def address_ok_clicked():
            address = address_entry.get()
            if address.strip() != "":
                scrolled_text.insert(tk.END, "\nAddress has been inputted.")
            else:
                scrolled_text.insert(tk.END, "\nPlease enter a valid address.")

        def number_ok_clicked():
            number = number_entry.get()
            if validate_mobile_number(number):
                scrolled_text.insert(tk.END, "\nMobile number has been inputted.")
            else:
                scrolled_text.insert(tk.END, "\nPlease enter a valid mobile number.")

        def duration_ok_clicked():
            duration = duration_entry.get()
            if duration.strip() != "":
                scrolled_text.insert(tk.END, "\nDuration has been inputted.")
            else:
                scrolled_text.insert(tk.END, "\nPlease enter a valid duration.")

        root = tk.Tk()
        root.title("HOTEL MANAGEMENT SYSTEM")
        
        top_frame = tk.Frame(root, padx=20, pady=10, bd=15, relief="ridge")
        top_frame.pack(side=tk.TOP, fill=tk.X)

        middle_frame = tk.Frame(root, bd=15 , relief="ridge")
        middle_frame.pack(expand=True, fill=tk.BOTH)

        global bottom_frame
        bottom_frame = tk.Frame(root, padx=20, pady=50, bd=15, relief="ridge")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        label_heading_top = tk.Label(top_frame, text="YOU CLICKED ON        :       CHECK IN", font=("Arial", 45, "bold"), fg="black")
        label_heading_top.pack()

        name_label = tk.Label(middle_frame, text="ENETR YOUR NAME", font=("Arial", 25,"bold"))
        name_label.grid(row=0, column=0, sticky="w")

        address_label = tk.Label(middle_frame, text="ENTER YOUR ADDRESS", font=("Arial", 25,"bold"))
        address_label.grid(row=1, column=0, sticky="w")
        
        number_label = tk.Label(middle_frame, text="ENTER YOUR NUMBER", font=("Arial", 25,"bold"))
        number_label.grid(row=2, column=0, sticky="w")
        
        duration_label = tk.Label(middle_frame, text="NUMBER OF DAYS", font=("Arial", 25,"bold"))
        duration_label.grid(row=3, column=0, sticky="w")

        rname_label = tk.Label(middle_frame, text=":", font=("Arial", 25,"bold"))
        rname_label.grid(row=0, column=1, sticky="w")

        raddress_label = tk.Label(middle_frame, text=":", font=("Arial", 25,"bold"))
        raddress_label.grid(row=1, column=1, sticky="w")
        
        rnumber_label = tk.Label(middle_frame, text=":", font=("Arial", 25,"bold"))
        rnumber_label.grid(row=2, column=1, sticky="w")
        
        rduration_label = tk.Label(middle_frame, text=":", font=("Arial", 25,"bold"))
        rduration_label.grid(row=3, column=1, sticky="w")

        global name_entry
        name_entry = tk.Entry(middle_frame, font=("Arial", 22),width=40)
        name_entry.grid(row=0, column=2, padx=10,columnspan=2 )

        name_ok = tk.Button(middle_frame, text="OK", font=("Arial", 18, "bold"),command=name_ok_clicked)
        name_ok.grid(row=0, column=4, padx=10,  sticky="e")
        
        global address_entry
        address_entry = tk.Entry(middle_frame, font=("Arial", 22),width=40)
        address_entry.grid(row=1, column=2, padx=10, columnspan=2)
        
        address_ok = tk.Button(middle_frame, text="OK", font=("Arial", 18, "bold"),command=address_ok_clicked)
        address_ok.grid(row=1, column=4, padx=10,  sticky="e")
        
        global number_entry
        number_entry = tk.Entry(middle_frame, font=("Arial", 22),width=40)
        number_entry.grid(row=2, column=2, padx=10, columnspan=2)
        
        number_ok = tk.Button(middle_frame, text="OK", font=("Arial", 18, "bold",),command=number_ok_clicked)
        number_ok.grid(row=2, column=4, padx=10,  sticky="e")
        
        global duration_entry
        duration_entry = tk.Entry(middle_frame, font=("Arial", 22),width=40)
        duration_entry.grid(row=3, column=2, padx=10,columnspan=2 )
        
        duration_ok = tk.Button(middle_frame, text="OK", font=("Arial", 18, "bold"),command=duration_ok_clicked)
        duration_ok.grid(row=3, column=4, padx=10,  sticky="e")

        choose_room = tk.Label(middle_frame, text="CHOOSE YOUR ROOM", font=("Arial", 25,"bold"))
        choose_room.grid(row=4, column=0, sticky="nsew",columnspan=3)

        global payment_mode_var
        global room_type_var
        room_type_var = tk.StringVar()
        payment_mode_var = tk.StringVar()

        deluxe_checkbox = tk.Checkbutton(middle_frame, text="DELUXE", font=("Arial", 22, "bold"),
                                        variable=room_type_var, onvalue="DELUXE", offvalue="", command=lambda: on_room_type_select("DELUXE"))
        deluxe_checkbox.grid(row=5, column=0, sticky="w", padx=150)

        general_checkbox = tk.Checkbutton(middle_frame, text="GENERAL", font=("Arial", 22, "bold"),
                                        variable=room_type_var, onvalue="GENERAL", offvalue="", command=lambda: on_room_type_select("GENERAL"))
        general_checkbox.grid(row=5, column=2, sticky="w", padx=150)

        full_deluxe_checkbox = tk.Checkbutton(middle_frame, text="FULL DELUXE", font=("Arial", 22, "bold"),
                                            variable=room_type_var, onvalue="FULL DELUXE", offvalue="", command=lambda: on_room_type_select("FULL DELUXE"))
        full_deluxe_checkbox.grid(row=6, column=0, sticky="w", padx=150)

        joint_checkbox = tk.Checkbutton(middle_frame, text="JOINT", font=("Arial", 22, "bold"),
                                        variable=room_type_var, onvalue="JOINT", offvalue="", command=lambda: on_room_type_select("JOINT"))
        joint_checkbox.grid(row=6, column=2, sticky="w", padx=150)

        choose_payment = tk.Label(middle_frame, text="CHOOSE PAYMENT METHOD", font=("Arial", 25,"bold"))
        choose_payment.grid(row=8, column=0, sticky="nsew",columnspan=3)

        cash_checkbox = tk.Checkbutton(middle_frame, text="By cash", font=("Arial", 22),
                                        variable=payment_mode_var, onvalue="By cash", offvalue="", command=lambda: on_payment_mode_select("By cash"))
        cash_checkbox.grid(row=9, column=0, sticky="w", padx=150)

        card_checkbox = tk.Checkbutton(middle_frame, text="By credit/debit card", font=("Arial", 22),
                                    variable=payment_mode_var, onvalue="By credit/debit card", offvalue="", command=lambda: on_payment_mode_select("By credit/debit card"))
        card_checkbox.grid(row=9, column=2, sticky="w", padx=150)

        submit_button = tk.Button(middle_frame, text="SUBMIT", font=("Arial", 25, "bold"), command=submit_clicked)
        submit_button.grid(row=5, column=3, rowspan=2, padx=5,  sticky="w")
        submit_button.config(height=3,width=10)

        global scrolled_text
        scrolled_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
        scrolled_text.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=20, pady=10)

        root.mainloop()

    def open_registration(self):
        register_window = tk.Tk()
        register_window.title("Registration Form")
        register_window.geometry("480x550")

        def create_database_if_not_exists(database_name):
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root"
                )

                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_management")
                print("Database created successfully (if it didn't exist)")
            except Error as e:
                print(f"Error creating database: {e}")
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        def create_table_if_not_exists(database_name, table_name):
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="hotel_management"
                )

                cursor = mydb.cursor()
                cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
                result = cursor.fetchone()

                if not result:
                    create_table_query = (
                        f"CREATE TABLE {table_name} "
                        "(id INT AUTO_INCREMENT PRIMARY KEY, "
                        "guest_name VARCHAR(255), "
                        "contact VARCHAR(255), "
                        "email VARCHAR(255), "
                        "gender VARCHAR(255), "
                        "city VARCHAR(255), "
                        "state VARCHAR(255))"
                    )
                    cursor.execute(create_table_query)
                    print("Table created successfully (if it didn't exist)")
            except Error as e:
                print(f"Error creating table: {e}")
            finally:
                if mydb.is_connected():
                    cursor.close()
                    mydb.close()

        def check_create_database_table():
            create_database_if_not_exists("HOTEL_MANAGEMENT")  # Replace with your actual database name
            create_table_if_not_exists("HOTEL_MANAGEMENT", "registration_table")  # Use consistent table name

        check_create_database_table()

        def insert_data():
            name = entry_name.get()
            contact = entry_contact.get()
            email = entry_email.get()
            gender = gender_var.get()
            city = district_combobox.get()
            state = state_combobox.get()

            if not (name and contact and email and city and state):
                error_label.config(text="Fill empty fields!!!", fg="red")
                return


            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="HOTEL_MANAGEMENT"  # Replace with your actual database name
            )

            cursor = mydb.cursor()

            # Check if 'email' column exists before altering the table
            cursor.execute("SHOW COLUMNS FROM registration_table LIKE 'email'")
            result = cursor.fetchone()

            if not result:
                # Alter the table to add the 'Gender' column
                alter_query = "ALTER TABLE registration_table ADD COLUMN Gender VARCHAR(255);"
                cursor.execute(alter_query)

            # Insert data into the table
            sql = "INSERT INTO registration_table (guest_name, contact, email, gender, city, state) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, contact, email, gender, city, state)
            cursor.execute(sql, values)
            mydb.commit()

            cursor.close()
            mydb.close()
            
        # Top heading label
        label_heading = tk.Label(register_window, bg="orange", fg='white', text="Please enter details below",padx=130,pady=10,font=("arial",15))
        label_heading.grid(row=0, column=0, columnspan=2)

        # Left side labels
        left_frame = tk.Frame(register_window)
        left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        label_name = tk.Label(left_frame, text="Name* :",padx=20, pady=10)
        label_name.grid(row=0, column=0, sticky="w")

        label_contact = tk.Label(left_frame, text="Contact* :", padx=20, pady=10)
        label_contact.grid(row=1, column=0, sticky="w")

        label_email = tk.Label(left_frame, text="Email* :", padx=20, pady=10)
        label_email.grid(row=2, column=0, sticky="w")

        label_gender = tk.Label(left_frame, text="Gender* :", padx=20, pady=10)
        label_gender.grid(row=3, column=0, sticky="w")

        label_State = tk.Label(left_frame, text="State* :", padx=20, pady=10)
        label_State.grid(row=4, column=0, sticky="w")

        label_City = tk.Label(left_frame, text="City* :", padx=20, pady=10)
        label_City.grid(row=5, column=0, sticky="w")

        # Right side entry fields
        right_frame = tk.Frame(register_window)
        right_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        entry_name = tk.Entry(right_frame)
        entry_name.grid(row=0, column=0, sticky="w", padx=20, pady=10,columnspan=2)

        entry_contact = tk.Entry(right_frame)
        entry_contact.grid(row=1, column=0, sticky="w", padx=20, pady=10,columnspan=2)

        entry_email = tk.Entry(right_frame)
        entry_email.grid(row=2, column=0, sticky="w", padx=20, pady=10,columnspan=2)

        gender_options = ['Male', 'Female']
        gender_var = tk.StringVar(value="Male")

        def select_gender(option):
            gender_var.set(option)

        # Adjust the row for the radio buttons to be in one column
        for i, option in enumerate(gender_options):
            Gender_button = tk.Radiobutton(right_frame, text=option, variable=gender_var, value=option, command=lambda opt=option: select_gender(opt))
            Gender_button.grid(row=3, column=0+i, sticky="w")

        # State dropdown
        state_options = list(states_and_districts.keys())
        global state_combobox
        state_combobox = ttk.Combobox(right_frame, values=state_options, state="readonly")
        state_combobox.grid(row=4, column=0, sticky="w", padx=20, pady=10)
        state_combobox.bind("<<ComboboxSelected>>", update_districts)

        # District dropdown
        global district_combobox
        district_combobox = ttk.Combobox(right_frame, state="readonly")
        district_combobox.grid(row=5, column=0, sticky="w", padx=20, pady=10)

        error_label = tk.Label(register_window, text="", fg="red")
        error_label.grid(row=6, column=0, columnspan=2)

        # Button to register
        register_button = tk.Button(register_window, text="Register", command=insert_data, bg="orange", fg="black")
        register_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

def update_districts(event):
    # Create a function to update the districts based on the selected state
    selected_state = state_combobox.get()
    districts = states_and_districts.get(selected_state, [])
    district_combobox['values'] = districts

def main():
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
