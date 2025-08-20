class CarNode:
    def __init__(self, car_number):
        self.car_number = car_number
        self.next = None


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = None

    def park_car(self, car_number):
        if self.size >= self.capacity:
            print("Parking Lot is Full!")
            return

        new_car = CarNode(car_number)
        new_car.next = self.head
        self.head = new_car
        self.size += 1

        print(f"Car {car_number} parked successfully.")
        self.save_to_file(car_number, "PARKED")

    def remove_car(self, car_number):
        prev = None
        current = self.head

        while current is not None:
            if current.car_number == car_number:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                self.size -= 1
                print(f"Car {car_number} exited successfully.")
                self.save_to_file(car_number, "EXITED")
                return
            prev = current
            current = current.next

        print("⚠️ Car not found in the parking lot.")

    def display_cars(self):
        if self.head is None:
            print("Parking Lot is empty.")
            return

        print("\n Currently Parked Cars:")
        current = self.head
        while current:
            print(f"- {current.car_number}")
            current = current.next

    def save_to_file(self, car_number, action):
        with open("parking_history.txt", "a") as f:
            f.write(f"{car_number} - {action}\n")

if __name__ == "__main__":
    lot_capacity = int(input("Enter Parking Lot Capacity: "))
    parking_lot = ParkingLot(lot_capacity)

    while True:
        print("\n=== Smart Parking Lot ===")
        print("1. Park a Car")
        print("2. Remove a Car")
        print("3. Display Parked Cars")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            car_no = input("Enter Car Number: ")
            parking_lot.park_car(car_no)
        elif choice == "2":
            car_no = input("Enter Car Number to Remove: ")
            parking_lot.remove_car(car_no)
        elif choice == "3":
            parking_lot.display_cars()
        elif choice == "4":
            print("Exiting Parking Lot System...")
            break
        else:
            print("Invalid choice! Try again.")
