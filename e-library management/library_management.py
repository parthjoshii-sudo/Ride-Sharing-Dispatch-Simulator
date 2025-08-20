class BookNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class Library:
    def __init__(self):
        self.head = None
        self.undo_stack = []

    def add_book(self, title):
        new_book = BookNode(title)
        new_book.next = self.head
        self.head = new_book
        self.undo_stack.append(("remove", title))
        print(f"Book '{title}' added.")

    def borrow_book(self, title):
        prev = None
        curr = self.head
        while curr:
            if curr.title == title:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                self.undo_stack.append(("add", title))
                print(f"Book '{title}' borrowed.")
                return
            prev = curr
            curr = curr.next
        print("Book not found!")

    def return_book(self, title):
        self.add_book(title)
        self.undo_stack.pop()  

    def undo_last(self):
        if not self.undo_stack:
            print("No actions to undo.")
            return
        action, title = self.undo_stack.pop()
        if action == "remove":
            self.borrow_book(title)
        elif action == "add":
            self.add_book(title)
        print(f"Last action undone: {action} {title}")

    def display_books(self):
        if not self.head:
            print("No books in library.")
            return
        print("\nBooks in Library:")
        curr = self.head
        while curr:
            print(f"- {curr.title}")
            curr = curr.next

library = Library()

while True:
    print("\n=== Library Menu ===")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Undo Last Action")
    print("5. Display Books")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        library.add_book(title)
    elif choice == "2":
        title = input("Enter Book Title to Borrow: ")
        library.borrow_book(title)
    elif choice == "3":
        title = input("Enter Book Title to Return: ")
        library.return_book(title)
    elif choice == "4":
        library.undo_last()
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
