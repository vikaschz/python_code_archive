"""10. Menu-Driven Transport Booking System
Create a base class Transport.
Derived classes: Bus, Train, Flight.
Menu options:
1. Choose transport
2. Book ticket
3. Exit
"""


class Transport:
    def __init__(self, mode_name, price_per_seat):
        self.mode_name = mode_name
        self.price_per_seat = price_per_seat

    def book_ticket(self, seats):
        # Base method to be overridden
        pass


# Hierarchical Inheritance: Multiple transport modes from one parent
class Bus(Transport):
    def __init__(self):
        super().__init__("Bus", 50)

    def book_ticket(self, seats):
        total = seats * self.price_per_seat
        return f"🚌 Bus Ticket Confirmed!\nSeats: {seats}\nRoute: Local Terminal\nTotal Cost: ${total}"


class Train(Transport):
    def __init__(self):
        super().__init__("Train", 120)

    def book_ticket(self, seats):
        total = seats * self.price_per_seat
        return f"🚆 Train Ticket Confirmed!\nSeats: {seats}\nCoach: Sleeper Class\nTotal Cost: ${total}"


class Flight(Transport):
    def __init__(self):
        super().__init__("Flight", 450)

    def book_ticket(self, seats):
        total = seats * self.price_per_seat
        return f"✈️ Flight Ticket Confirmed!\nSeats: {seats}\nClass: Economy\nTotal Cost: ${total}"


def booking_menu():
    selected_transport = None

    while True:
        print("\n--- Transport Booking System ---")
        print("1. Choose Transport")
        print("2. Book Ticket")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            print(
                "\nAvailable Modes: 1. Bus ($50) | 2. Train ($120) | 3. Flight ($450)"
            )
            t_choice = input("Select Mode: ")

            if t_choice == "1":
                selected_transport = Bus()
            elif t_choice == "2":
                selected_transport = Train()
            elif t_choice == "3":
                selected_transport = Flight()
            else:
                print("Invalid selection.")
                continue

            print(f"Current selection: {selected_transport.mode_name}")

        elif choice == "2":
            if selected_transport:
                try:
                    num_seats = int(input("Enter number of seats: "))
                    if num_seats > 0:
                        print("\n" + selected_transport.book_ticket(num_seats))
                    else:
                        print("Please enter a valid number of seats.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("\nError: Please choose a transport mode first (Option 1).")

        elif choice == "3":
            print("Thank you for using our booking system!")
            break
        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    booking_menu()
