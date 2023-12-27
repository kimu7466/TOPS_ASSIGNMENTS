class Room:
    def __init__(self, room_number, capacity, price, is_occupied=False):
        self.room_number = room_number
        self.capacity = capacity
        self.price = price
        self.is_occupied = is_occupied
        self.guest = None

    def occupy_room(self, guest):
        if not self.is_occupied:
            self.is_occupied = True
            self.guest = guest
            print(f"Room {self.room_number} has been occupied by {guest.name}")
        else:
            print(f"Room {self.room_number} is already occupied")

    def vacate_room(self):
        if self.is_occupied:
            self.is_occupied = False
            print(f"Room {self.room_number} has been vacated")
            self.guest = None
        else:
            print(f"Room {self.room_number} is already vacant")


class Guest:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number


# Creating rooms
rooms = [
    Room(101, 2, 100),
    Room(102, 3, 150),
    Room(103, 4, 200)
]

# Creating guests
guest1 = Guest("John Doe", 30, "123-456-7890")
guest2 = Guest("Jane Smith", 25, "987-654-3210")

# Demonstration
rooms[0].occupy_room(guest1)
rooms[1].occupy_room(guest2)
rooms[2].occupy_room(guest1)  # This will not work since room 103 is already occupied

rooms[0].vacate_room()
rooms[2].occupy_room(guest2)  # Now, room 103 can be occupied by another guest
