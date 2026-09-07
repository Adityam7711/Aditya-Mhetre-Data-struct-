# python
class TextEditor:

    def __init__(self):
        # Current document
        self.document = ""

        # Stack for undo
        self.undo_stack = []

        # Stack for redo
        self.redo_stack = []   

    # Make a new change
    def make_change(self, new_text):

        # Save current document before changing
        self.undo_stack.append(self.document)

        # Change the document
        self.document = new_text

        # New change means redo history is removed
        self.redo_stack.clear()

        print("Change saved.")

    # Undo
    def undo(self):

        # Check if there is anything to undo
        if len(self.undo_stack) == 0:
            print("Nothing to undo.")
            return

        # Save current document for redo
        self.redo_stack.append(self.document)

        # Get previous document
        self.document = self.undo_stack.pop()

        print("Undo successful.")

    # Redo
    def redo(self):

        # Check if there is anything to redo
        if len(self.redo_stack) == 0:
            print("Nothing to redo.")
            return

        # Save current document for undo
        self.undo_stack.append(self.document)

        # Get document from redo stack
        self.document = self.redo_stack.pop()

        print("Redo successful.")

    # Display document
    def display(self):
        print("\nCurrent Document:")
        print(self.document)


# Create editor
editor = TextEditor()


# Menu
while True:

    print("\n===== TEXT EDITOR =====")
    print("1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        text = input("Enter new text: ")
        editor.make_change(text)

    elif choice == "2":

        editor.undo()

    elif choice == "3":

        editor.redo()

    elif choice == "4":

        editor.display()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")

