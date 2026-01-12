"""8. Menu-Driven Notification System
Create a base class Notification.
Derived classes: SMSNotification, EmailNotification.
Use method overriding.
Menu options:
1. Choose notification type
2. Send notification
3. Exit
"""


class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self, message):
        # Base method to be overridden
        return f"Sending generic notification to {self.recipient}: {message}"


# Hierarchical Inheritance: Specialized delivery methods
class SMSNotification(Notification):
    def send(self, message):
        return (
            f"📱 [SMS] Sent to {self.recipient}: '{message}' (Carrier rates may apply)"
        )


class EmailNotification(Notification):
    def send(self, message):
        return (
            f"📧 [Email] Sent to {self.recipient}: '{message}' (Subject: System Alert)"
        )


def notification_menu():
    notifier = None

    while True:
        print("\n--- Notification System ---")
        print("1. Choose Notification Type")
        print("2. Send Notification")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            print("\nSelect Channel: 1. SMS | 2. Email")
            n_type = input("Choice: ")
            recipient = input("Enter Recipient (Phone/Email): ")

            if n_type == "1":
                notifier = SMSNotification(recipient)
            elif n_type == "2":
                notifier = EmailNotification(recipient)
            else:
                print("Invalid channel selected.")
                continue

            print(f"Channel set to {type(notifier).__name__}.")

        elif choice == "2":
            if notifier:
                msg = input("Enter your message: ")
                print("\n" + notifier.send(msg))
            else:
                print("\nError: Please configure notification type first (Option 1).")

        elif choice == "3":
            print("Shutting down notification system...")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    notification_menu()
