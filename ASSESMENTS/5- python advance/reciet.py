import tkinter as tk
from tkinter import messagebox

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
        self.rooms = {}

    def add_room(self, room):
        if room.room_number not in self.rooms:
            self.rooms[room.room_number] = room
            return f"Room {room.room_number} has been added to the hotel."
        else:
            return f"Room {room.room_number} already exists in the hotel."

    def get_total_guests(self):
        occupied_rooms = sum(room.is_occupied for room in self.rooms.values())
        return f"Total Guests: {occupied_rooms}"

    def occupy_room(self, room_number, guest):
        room = self.rooms.get(room_number)
        if room:
            return room.occupy_room(guest)
        else:
            return f"Room {room_number} does not exist."

    def vacate_room(self, room_number):
        room = self.rooms.get(room_number)
        if room:
            return room.vacate_room()
        else:
            return f"Room {room_number} does not exist."

    def generate_receipt(self, room_number):
        room = self.rooms.get(room_number)
        if room:
            return room.generate_receipt()
        else:
            return f"Room {room_number} does not exist."


class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        
        self.hotel = Hotel()
        
        self.label = tk.Label(root, text="Hotel Management System")
        self.label.pack()

        # Add Room Section
        self.room_number_label = tk.Label(root, text="Room Number:")
        self.room_number_label.pack()
        self.room_number_entry = tk.Entry(root)
        self.room_number_entry.pack()

        self.capacity_label = tk.Label(root, text="Capacity:")
        self.capacity_label.pack()
        self.capacity_entry = tk.Entry(root)
        self.capacity_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.add_room_button = tk.Button(root, text="Add Room", command=self.add_room)
        self.add_room_button.pack()

        # Occupy Room Section
        self.occupy_room_label = tk.Label(root, text="Occupy Room:")
        self.occupy_room_label.pack()
        self.occupy_room_number_entry = tk.Entry(root)
        self.occupy_room_number_entry.pack()

        self.guest_name_label = tk.Label(root, text="Guest Name:")
        self.guest_name_label.pack()
        self.guest_name_entry = tk.Entry(root)
        self.guest_name_entry.pack()

        self.guest_age_label = tk.Label(root, text="Guest Age:")
        self.guest_age_label.pack()
        self.guest_age_entry = tk.Entry(root)
        self.guest_age_entry.pack()

        self.guest_phone_label = tk.Label(root, text="Guest Phone:")
        self.guest_phone_label.pack()
        self.guest_phone_entry = tk.Entry(root)
        self.guest_phone_entry.pack()

        self.occupy_room_button = tk.Button(root, text="Occupy Room", command=self.occupy_room)
        self.occupy_room_button.pack()

        # Vacate Room Section
        self.vacate_room_label = tk.Label(root, text="Vacate Room:")
        self.vacate_room_label.pack()
        self.vacate_room_number_entry = tk.Entry(root)
        self.vacate_room_number_entry.pack()

        self.vacate_room_button = tk.Button(root, text="Vacate Room", command=self.vacate_room)
        self.vacate_room_button.pack()

        # Total Guests Section
        self.total_guests_button = tk.Button(root, text="Total Guests", command=self.display_total_guests)
        self.total_guests_button.pack()

        # Generate Receipt Section
        self.generate_receipt_label = tk.Label(root, text="Generate Receipt:")
        self.generate_receipt_label.pack()
        self.receipt_room_number_entry = tk.Entry(root)
        self.receipt_room_number_entry.pack()

        self.generate_receipt_button = tk.Button(root, text="Generate Receipt", command=self.generate_receipt)
        self.generate_receipt_button.pack()

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
