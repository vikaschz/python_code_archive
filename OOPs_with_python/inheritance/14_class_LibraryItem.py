"""
Create a base class LibraryItem with title. Derive Book and Magazine classes.
"""


class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already currently unavailable.")

    def return_item(self):
        self.is_checked_out = False
        print(f"'{self.title}' has been returned.")


class Book(LibraryItem):
    def __init__(self, title, author, isbn):

        super().__init__(title)
        self.author = author
        self.isbn = isbn

    def display_info(self):
        status = "Available" if not self.is_checked_out else "Checked Out"
        print(f"Book: {self.title} by {self.author} (ISBN: {self.isbn}) - [{status}]")


class Magazine(LibraryItem):
    def __init__(self, title, issue_number, month):

        super().__init__(title)
        self.issue_number = issue_number
        self.month = month

    def display_info(self):
        status = "Available" if not self.is_checked_out else "Checked Out"
        print(
            f"Magazine: {self.title} Issue #{self.issue_number} ({self.month}) - [{status}]"
        )


my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
my_mag = Magazine("National Geographic", 142, "December")

print("--- Library Inventory ---")
my_book.display_info()
my_mag.display_info()

print("\n--- Transaction ---")
my_book.check_out()
my_book.display_info()
