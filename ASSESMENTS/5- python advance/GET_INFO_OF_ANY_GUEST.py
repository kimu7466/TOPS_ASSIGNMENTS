# import tkinter as tk
# from tkinter import ttk
# import mysql.connector
# from tkinter import scrolledtext

# def search_by_number():
#     def clear_table():
#         for item in tree.get_children():
#             tree.delete(item)

#     def search_clicked():
#         clear_table()

#         searched_number = search_entry.get().strip()
#         if searched_number:
#             try:
#                 connection = mysql.connector.connect(
#                     host='localhost',
#                     user='root',
#                     password='root',
#                     database='HOTEL_MANAGEMENT'
#                 )
#                 cursor = connection.cursor()
                
#                 select_query = "SELECT * FROM check_inn_table"
#                 cursor.execute(select_query)
                
#                 results = cursor.fetchall()

#                 if results:
#                     for row in results:
#                         tree.insert('', 'end', values=row)
#                 else:
#                     scrolled_text.insert(tk.END, "\nNo data found.\n")

#                 connection.close()
#             except mysql.connector.Error as error:
#                 scrolled_text.insert(tk.END, f"Error: {error}\n")
#         else:
#             scrolled_text.insert(tk.END, "\nPlease enter a number to search.\n")

#     def generate_receipt():
#         selected_item = tree.focus()  # Get the selected row
#         if selected_item:
#             item = tree.item(selected_item)
#             values = item['values']
#             receipt_text.delete(1.0, tk.END)  # Clear the text field
#             for index, col in enumerate(columns):
#                 receipt_text.insert(tk.END, f"{col}: {values[index]}\n")

#     search_window = tk.Tk()
#     search_window.title("Search by Number")

#     left_frame = tk.Frame(search_window)
#     left_frame.pack(side=tk.LEFT, padx=10, pady=10)

#     search_label = tk.Label(left_frame, text="Enter Number to Search:", font=("Arial", 18))
#     search_label.pack(padx=10, pady=10)

#     search_entry = tk.Entry(left_frame, font=("Arial", 16))
#     search_entry.pack(padx=10, pady=5)

#     search_button = tk.Button(left_frame, text="Search", font=("Arial", 18), command=search_clicked)
#     search_button.pack(padx=10, pady=5)

#     scrolled_text = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=60, height=10)
#     scrolled_text.pack(padx=10, pady=10)

#     right_frame = tk.Frame(search_window, bg="orange")
#     right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

#     columns = ('ID', 'Name', 'Email', 'Phone', 'City', 'Country')  # Replace with your column names
#     tree = ttk.Treeview(right_frame, columns=columns, show='headings')
#     tree.pack()

#     for col in columns:
#         tree.heading(col, text=col)

#     receipt_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=40, height=20)
#     receipt_text.pack(padx=10, pady=10)

#     generate_receipt_button = tk.Button(right_frame, text="Generate Receipt", font=("Arial", 14), command=generate_receipt)
#     generate_receipt_button.pack(padx=10, pady=5)

#     search_window.mainloop()

# # Call the function to run the application
# search_by_number()






import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import scrolledtext

def search_by_number():
    def clear_table():
        for item in tree.get_children():
            tree.delete(item)

    def search_clicked():
        clear_table()

        searched_number = search_entry.get().strip()
        if searched_number:
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='HOTEL_MANAGEMENT'
                )
                cursor = connection.cursor()
                
                select_query = "SELECT * FROM check_inn_table"
                cursor.execute(select_query)
                
                results = cursor.fetchall()

                if results:
                    for row in results:
                        tree.insert('', 'end', values=row)
                else:
                    scrolled_text.insert(tk.END, "\nNo data found.\n")

                connection.close()
            except mysql.connector.Error as error:
                scrolled_text.insert(tk.END, f"Error: {error}\n")
        else:
            scrolled_text.insert(tk.END, "\nPlease enter a number to search.\n")

    def generate_receipt():
        selected_item = tree.focus()  # Get the selected row
        if selected_item:
            item = tree.item(selected_item)
            values = item['values']
            receipt_text.delete(1.0, tk.END)  # Clear the text field
            for index, col in enumerate(columns):
                receipt_text.insert(tk.END, f"{col}: {values[index]}\n")

    search_window = tk.Tk()
    search_window.title("Search by Number")

    left_frame = tk.Frame(search_window)
    left_frame.pack(side=tk.LEFT, padx=10, pady=10)

    search_label = tk.Label(left_frame, text="Enter Number to Search:", font=("Arial", 18))
    search_label.pack(padx=10, pady=10)

    search_entry = tk.Entry(left_frame, font=("Arial", 16))
    search_entry.pack(padx=10, pady=5)

    search_button = tk.Button(left_frame, text="Search", font=("Arial", 18), command=search_clicked)
    search_button.pack(padx=10, pady=5)

    scrolled_text = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=60, height=10)
    scrolled_text.pack(padx=10, pady=10)

    right_frame = tk.Frame(search_window, bg="orange")
    right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

    columns = ('ID', 'Name', 'Email', 'Phone', 'City', 'Country')  # Replace with your column names
    tree = ttk.Treeview(right_frame, columns=columns, show='headings')
    tree.pack()

    for col in columns:
        tree.heading(col, text=col)

    receipt_text = tk.Text(right_frame, wrap=tk.WORD, width=40, height=20)
    receipt_text.pack(padx=10, pady=10)

    generate_receipt_button = tk.Button(right_frame, text="Generate Receipt", font=("Arial", 14), command=generate_receipt)
    generate_receipt_button.pack(padx=10, pady=5)

    search_window.mainloop()

# Call the function to run the application
# search_by_number()
