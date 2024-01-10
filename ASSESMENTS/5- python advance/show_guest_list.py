import tkinter as tk
import mysql.connector
from tkinter import scrolledtext

def search_by_number():
    def search_clicked():
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
                
                select_query = "SELECT * FROM check_inn_table WHERE Number = %s"
                cursor.execute(select_query, (searched_number,))
                
                result = cursor.fetchone()

                if result:
                    scrolled_text.insert(tk.END, f"\nFound Details: {result}\n")
                else:
                    scrolled_text.insert(tk.END, "\nNo details found for the given number.\n")

                connection.close()
            except mysql.connector.Error as error:
                scrolled_text.insert(tk.END, f"Error: {error}\n")
        else:
            scrolled_text.insert(tk.END, "\nPlease enter a number to search.\n")

    search_window = tk.Tk()
    search_window.title("Search by Number")
    
    search_label = tk.Label(search_window, text="Enter Number to Search:", font=("Arial", 18))
    search_label.pack(padx=10, pady=10)

    search_entry = tk.Entry(search_window, font=("Arial", 16))
    search_entry.pack(padx=10, pady=5)

    search_button = tk.Button(search_window, text="Search", font=("Arial", 18), command=search_clicked)
    search_button.pack(padx=10, pady=5)

    scrolled_text = scrolledtext.ScrolledText(search_window, wrap=tk.WORD, width=60, height=10)
    scrolled_text.pack(padx=10, pady=10)
