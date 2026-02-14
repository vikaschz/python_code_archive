"""Create a base class Notification with send(). Derive SMSNotification, EmailNotification, and PushNotification. Send notifications polymorphically."""
class Notification:
    def send(self, message):
        raise NotImplementedError("Subclass must implement send()")

class SMSNotification(Notification):
    def send(self, message):
        print("Sending SMS:", message)

class EmailNotification(Notification):
    def send(self, message):
        print("Sending Email:", message)

class PushNotification(Notification):
    def send(self, message):
        print("Sending Push Notification:", message)

def notify_all(notifications, message):
    for n in notifications:
        n.send(message)

notifications = [
    SMSNotification(),
    EmailNotification(),
    PushNotification()
]

notify_all(notifications, "Exam starts at 9 AM")
