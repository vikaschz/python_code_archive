"""7. Menu-Driven Membership System
Create a base class Member.
Derived classes: SilverMember, GoldMember, PlatinumMember.
Demonstrate hierarchical inheritance.
Menu options:
1. Choose membership
2. View benefits
3. Exit
"""


class Member:
    def __init__(self, name):
        self.name = name
        self.membership_type = "Standard"

    def get_benefits(self):
        return "Basic access to the club facilities."


# Hierarchical Inheritance: Multiple tiers inheriting from Member
class SilverMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.membership_type = "Silver"

    def get_benefits(self):
        return "Silver Perks: 5% discount on all services and free locker access."


class GoldMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.membership_type = "Gold"

    def get_benefits(self):
        return "Gold Perks: 15% discount, priority booking, and free guest passes."


class PlatinumMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.membership_type = "Platinum"

    def get_benefits(self):
        return "Platinum Perks: 25% discount, 24/7 VIP lounge access, and personal concierge."


def membership_menu():
    current_user = None

    while True:
        print("\n--- Membership Management System ---")
        print("1. Choose Membership")
        print("2. View Benefits")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            name = input("Enter Member Name: ")
            print("\nSelect Tier: 1. Silver | 2. Gold | 3. Platinum")
            tier = input("Choice: ")

            if tier == "1":
                current_user = SilverMember(name)
            elif tier == "2":
                current_user = GoldMember(name)
            elif tier == "3":
                current_user = PlatinumMember(name)
            else:
                print("Invalid tier. Please try again.")
                continue

            print(
                f"Welcome, {name}! Your {current_user.membership_type} account is active."
            )

        elif choice == "2":
            if current_user:
                print(f"\n--- Benefit Summary for {current_user.name} ---")
                print(f"Status: {current_user.membership_type}")
                print(f"Benefits: {current_user.get_benefits()}")
            else:
                print("\nNo membership found. Please register first (Option 1).")

        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    membership_menu()
