import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import mysql.connector
from mysql.connector import Error
from main_state_districts import states_and_districts

def show_check_inn_table(root):
    def search():
        search_term = search_var.get().strip().lower()
        for i, row in enumerate(table_data):
            if search_term in str(row).lower():
                tree_view.selection_set(tree_view.get_children()[i])
                tree_view.see(tree_view.get_children()[i])
                break

    def generate_receipt():
        selected_item = tree_view.selection()
        if selected_item:
            selected_data = tree_view.item(selected_item)['values']
            # Implement receipt generation with selected_data

    def edit_data():
        selected_item = tree_view.selection()
        if selected_item:
            selected_data = tree_view.item(selected_item)['values']
            # Implement edit functionality for selected_data

    def delete_data():
        selected_item = tree_view.selection()
        if selected_item:
            selected_data = tree_view.item(selected_item)['values']
            # Implement delete functionality for selected_data

    def fetch_check_inn_data():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='HOTEL_MANAGEMENT'
            )
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM check_inn_table')
            data = cursor.fetchall()
            connection.close()
            return data
        except mysql.connector.Error as error:
            print(f"Error fetching data: {error}")
            return []

    def populate_table():
        nonlocal table_data
        table_data = fetch_check_inn_data()
        tree_view.delete(*tree_view.get_children())
        for row in table_data:
            tree_view.insert("", "end", values=row)


    
    def check_inn_window():

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

    root = tk.Tk()
    root.title("Check Inn Table")
    root.geometry("800x600")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    search_var = tk.StringVar()
    search_entry = ttk.Entry(frame, textvariable=search_var)
    search_entry.pack(padx=10, pady=10)

    search_button = ttk.Button(frame, text="Search", command=search)
    search_button.pack(padx=10, pady=5)

    tree_view = ttk.Treeview(frame, columns=("Name", "Address", "Number", "Duration", "RoomType", "PaymentMode"))
    tree_view.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    tree_view.heading("#0", text="ID")
    tree_view.column("#0", width=50)

    tree_view["show"] = "headings"
    for col in ("Name", "Address", "Number", "Duration", "RoomType", "PaymentMode"):
        tree_view.heading(col, text=col)
        tree_view.column(col, width=100)

    scroll_y = ttk.Scrollbar(tree_view, orient=tk.VERTICAL, command=tree_view.yview)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    tree_view.configure(yscrollcommand=scroll_y.set)

    scroll_x = ttk.Scrollbar(tree_view, orient=tk.HORIZONTAL, command=tree_view.xview)
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
    tree_view.configure(xscrollcommand=scroll_x.set)

    table_data = fetch_check_inn_data()
    populate_table()

    check_inn_view_add_button = ttk.Button(root, text="CHECK INN", command= check_inn_window)
    check_inn_view_add_button.pack(padx=10, pady=5)

    # receipt_button = ttk.Button(root, text="Generate Receipt", command=generate_receipt)
    # receipt_button.pack(padx=10, pady=5)

    # edit_button = ttk.Button(root, text="Edit", command=edit_data)
    # edit_button.pack(padx=10, pady=5)

    # delete_button = ttk.Button(root, text="Delete", command=delete_data)
    # delete_button.pack(padx=10, pady=5)

def main():
    root = tk.Tk()
    show_check_inn_table(root)
    root.mainloop()

if __name__ == "__main__":
    main()
