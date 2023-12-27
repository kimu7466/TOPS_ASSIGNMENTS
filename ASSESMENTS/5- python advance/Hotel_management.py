import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Room:
    def __init__(self, room_number, capacity, price):
        self.room_number = room_number
        self.capacity = capacity
        self.price = price
        self.is_occupied = False
        self.guest = None

    def occupy_room(self, guest):
        if not self.is_occupied:
            self.is_occupied = True
            self.guest = guest
            return f"Room {self.room_number} has been occupied by {guest.name}"
        else:
            return f"Room {self.room_number} is already occupied"

    def vacate_room(self):
        if self.is_occupied:
            self.is_occupied = False
            return f"Room {self.room_number} has been vacated"
        else:
            return f"Room {self.room_number} is already vacant"

    def generate_receipt(self):
        if self.is_occupied:
            receipt = f"Receipt for Room {self.room_number}:\n"
            receipt += f"Guest: {self.guest.name}\n"
            receipt += f"Room Price: ${self.price}\n"
            return receipt
        else:
            return f"No guest in Room {self.room_number}"


class Guest:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number


class Hotel:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="your_host",
            user="root",
            password="root",
            database="hotel"
        )
        self.cursor = self.db.cursor()
        self.rooms = {}

    def add_room(self, room):
        query = "INSERT INTO rooms (room_number, capacity, price, is_occupied, guest_name) VALUES (%s, %s, %s, %s, %s)"
        values = (room.room_number, room.capacity, room.price, room.is_occupied, None)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Room {room.room_number} has been added to the hotel."

    def get_total_guests(self):
        self.cursor.execute("SELECT COUNT(*) FROM rooms WHERE is_occupied = 1")
        total_guests = self.cursor.fetchone()[0]
        return f"Total Guests: {total_guests}"

    def occupy_room(self, room_number, guest):
        query = "UPDATE rooms SET is_occupied = 1, guest_name = %s WHERE room_number = %s"
        values = (guest.name, room_number)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Room {room_number} has been occupied by {guest.name}"

    def vacate_room(self, room_number):
        query = "UPDATE rooms SET is_occupied = 0, guest_name = NULL WHERE room_number = %s"
        values = (room_number,)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Room {room_number} has been vacated"

    def generate_receipt(self, room_number):
        query = "SELECT guest_name FROM rooms WHERE room_number = %s"
        values = (room_number,)
        self.cursor.execute(query, values)
        guest_name = self.cursor.fetchone()[0]
        
        if guest_name:
            receipt = f"Receipt for Room {room_number}:\n"
            receipt += f"Guest: {guest_name}\n"
            # Fetch room price from database or use a predefined value from Room class
            # Add room price to the receipt
            return receipt
        else:
            return f"No guest in Room {room_number}"


class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        
        self.hotel = Hotel()
        
        # ... (GUI elements remain unchanged)

    def add_room(self):
        room_number = int(self.room_number_entry.get())
        capacity = int(self.capacity_entry.get())
        price = float(self.price_entry.get())
        
        room = Room(room_number, capacity, price)
        result = self.hotel.add_room(room)
        messagebox.showinfo("Add Room", result)

    def occupy_room(self):
        room_number = int(self.occupy_room_number_entry.get())
        guest_name = self.guest_name_entry.get()
        guest_age = int(self.guest_age_entry.get())
        guest_phone = self.guest_phone_entry.get()
        
        guest = Guest(guest_name, guest_age, guest_phone)
        result = self.hotel.occupy_room(room_number, guest)
        messagebox.showinfo("Occupy Room", result)

    def vacate_room(self):
        room_number = int(self.vacate_room_number_entry.get())
        result = self.hotel.vacate_room(room_number)
        messagebox.showinfo("Vacate Room", result)

    def display_total_guests(self):
        total_guests = self.hotel.get_total_guests()
        messagebox.showinfo("Total Guests", total_guests)

    def generate_receipt(self):
        room_number = int(self.receipt_room_number_entry.get())
        receipt = self.hotel.generate_receipt(room_number)
        messagebox.showinfo("Receipt", receipt)


if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()
