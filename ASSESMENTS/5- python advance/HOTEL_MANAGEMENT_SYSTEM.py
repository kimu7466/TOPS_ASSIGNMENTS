import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import mysql.connector
from mysql.connector import Error
from main_state_districts import states_and_districts
from GET_INFO_OF_ANY_GUEST import search_by_number
from SHOW_GUEST_LISTS import show_check_inn_table


class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")

        self.create_main_interface()
#############################################################################################
# ============================ <button3> ==============================
        def create_room_table(self):
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='HOTEL_MANAGEMENT'
                )
                cursor = connection.cursor()

                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS room_table (
                        room_number INT AUTO_INCREMENT PRIMARY KEY,
                        room_charges DECIMAL(10, 2),
                        availability ENUM('Available', 'Booked') DEFAULT 'Available'
                    )
                ''')

                connection.close()
            except mysql.connector.Error as error:
                print(f"Error creating room table: {error}")

        def toggle_availability(self, room_number, current_status):
            new_status = 'Booked' if current_status == 'Available' else 'Available'
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='HOTEL_MANAGEMENT'
                )
                cursor = connection.cursor()
                update_query = "UPDATE room_table SET availability = %s WHERE room_number = %s"
                cursor.execute(update_query, (new_status, room_number))
                connection.commit()
                connection.close()
            except mysql.connector.Error as error:
                print(f"Error toggling room availability: {error}")

    def open_room_management(self):
        # def toggle(room_number, current_status):
        #     self.toggle_availability(room_number, current_status)
        #     update_buttons()

        # def update_buttons():
        #     for btn, status in room_buttons:
        #         btn.destroy()

            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='HOTEL_MANAGEMENT'
                )
                cursor = connection.cursor()
                cursor.execute("SELECT room_number, availability FROM room_table")
                rooms = cursor.fetchall()

            except mysql.connector.Error as error:
                print(f"Error fetching room data: {error}")

            root = tk.Tk()
            root.title("Room Management")
            root.geometry("800x600+0+0")

            room_frame = tk.Frame(root,bd=10,relief="groove")
            room_frame.pack()
            

            # room_buttons = update_buttons()

            root.mainloop()

# ============================</button3> ==============================
            
# ============================= <button2> =======================

    def open_show_check_inn_table(self):
        show_check_inn_table(self.root)

# ================================= </button2> ============================
# ================================= < MAIN FIRST INTERFACE > ============================

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

        button1 = tk.Button(left_frame, text="1. CHECK INN", command=self.open_registration, width=50, height=5)
        button1.pack(padx=20, pady=5)

        button2 = tk.Button(left_frame, text="2. SHOW GUEST LIST", command=self.open_show_check_inn_table, width=50, height=5)
        button2.pack(padx=20, pady=5)

        button3 = tk.Button(left_frame, text="3. CHECK OUT", command=self.open_room_management, width=50, height=5)
        button3.pack(padx=20, pady=5)

        button4 = tk.Button(left_frame, text="4. GET INFO OF ANY GUEST", command=search_by_number, width=50, height=5)
        button4.pack(padx=20, pady=5)

        button5 = tk.Button(left_frame, text="5. EXIT", command=self.root.quit, width=50, height=5)
        button5.pack(padx=20, pady=5)

# ================================= < /MAIN FIRST INTERFACE > ============================


# ============================== BUTTON 1.CHECH_INN ============================
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
            create_database_if_not_exists("HOTEL_MANAGEMENT") 
            create_table_if_not_exists("HOTEL_MANAGEMENT", "registration_table") 

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
                database="HOTEL_MANAGEMENT"  
            )

            cursor = mydb.cursor()

            cursor.execute("SHOW COLUMNS FROM registration_table LIKE 'email'")
            result = cursor.fetchone()

            if not result:
                alter_query = "ALTER TABLE registration_table ADD COLUMN Gender VARCHAR(255);"
                cursor.execute(alter_query)

            sql = "INSERT INTO registration_table (guest_name, contact, email, gender, city, state) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, contact, email, gender, city, state)
            cursor.execute(sql, values)
            mydb.commit()

            cursor.close()
            mydb.close()
            
        label_heading = tk.Label(register_window, bg="orange", fg='white', text="Please enter details below",padx=130,pady=10,font=("arial",15))
        label_heading.grid(row=0, column=0, columnspan=2)

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

        for i, option in enumerate(gender_options):
            Gender_button = tk.Radiobutton(right_frame, text=option, variable=gender_var, value=option, command=lambda opt=option: select_gender(opt))
            Gender_button.grid(row=3, column=0+i, sticky="w")

        state_options = list(states_and_districts.keys())
        global state_combobox
        state_combobox = ttk.Combobox(right_frame, values=state_options, state="readonly")
        state_combobox.grid(row=4, column=0, sticky="w", padx=20, pady=10)
        state_combobox.bind("<<ComboboxSelected>>", update_districts)

        global district_combobox
        district_combobox = ttk.Combobox(right_frame, state="readonly")
        district_combobox.grid(row=5, column=0, sticky="w", padx=20, pady=10)

        error_label = tk.Label(register_window, text="", fg="red")
        error_label.grid(row=6, column=0, columnspan=2)

        register_button = tk.Button(register_window, text="Register", command=insert_data, bg="orange", fg="black")
        register_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

def update_districts(event):
    selected_state = state_combobox.get()
    districts = states_and_districts.get(selected_state, [])
    district_combobox['values'] = districts

#  ============================= </BUTTON 1> ===========================


def main():
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
