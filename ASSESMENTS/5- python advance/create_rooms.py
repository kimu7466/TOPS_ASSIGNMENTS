"""
    RUN this programe atleast once to create rooms data in your database.
    this will add four rooms at once.
    if you want to add more rooms. you can add more rooms but make sure to change room names in the query for identify individual. otherwise it will create rooms with the same name.

    I'll add a option for that in my next update.
    thank you
  """
import tkinter as tk
import mysql.connector


def room_status():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    # Create the 'new_hotel' database if it doesn't exist
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_management")

    # Close connection
    cursor.close()
    conn.close()

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hotel_management"
    )




    c = conn.cursor()

    # Create a table for rooms with an ID, room number, and availability column
    c.execute('''CREATE TABLE IF NOT EXISTS rooms 
                (id INT AUTO_INCREMENT PRIMARY KEY, room_number VARCHAR(20), availability VARCHAR(20))''')

    # Insert sample data
    c.execute("INSERT INTO rooms (room_number, availability) VALUES ('DELUXE_2', 'Available')")
    c.execute("INSERT INTO rooms (room_number, availability) VALUES ('GENERAL_2', 'Booked')")
    c.execute("INSERT INTO rooms (room_number, availability) VALUES ('FULL DELUXE', 'Available')")
    c.execute("INSERT INTO rooms (room_number, availability) VALUES ('JOINT', 'Available')")
    # Add more sample data as needed

    conn.commit()

    # Function to update room availability
    def update_availability(room_number):
        c.execute("SELECT availability FROM rooms WHERE room_number=%s", (room_number,))
        current_availability = c.fetchone()[0]

        new_availability = 'Available' if current_availability == 'Booked' else 'Booked'
        c.execute("UPDATE rooms SET availability=%s WHERE room_number=%s", (new_availability, room_number))
        conn.commit()
        display_rooms()

    # Function to display room availability
    def display_rooms():
        c.execute("SELECT room_number, availability FROM rooms")
        rooms = c.fetchall()

        for idx, (room_number, availability) in enumerate(rooms):
            label = tk.Label(root, text=f"Room {room_number}: {availability}")
            label.grid(row=idx+1, column=0, pady=5)

            button = tk.Button(root, text="Toggle", command=lambda num=room_number: update_availability(num))
            button.grid(row=idx+1, column=1, padx=5)

    # Tkinter window setup
    root = tk.Tk()
    root.title("Hotel Management System")

    # Display room availability
    display_rooms()

    root.mainloop()

    # Close database connection
    conn.close()


room_status()