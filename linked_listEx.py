class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def addStudent(self, roll_no, name, marks):
        new_node = Node(roll_no, name, marks)
        if self.head is None:
            self.head = new_node
            print("Student added successfully.")
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        print("Student added successfully.")

    def displayStudents(self):
        if self.head is None:
            print("Student list is empty.")
            return
        current = self.head
        while current is not None:
            print("Roll No:", current.roll_no, "| Name:", current.name, "| Marks:", current.marks)
            current = current.next

    def searchStudent(self, roll_no):
        current = self.head
        while current is not None:
            if current.roll_no == roll_no:
                print("Student Found!")
                print("Roll No:", current.roll_no)
                print("Name:", current.name)
                print("Marks:", current.marks)
                return
            current = current.next
        print("Student not found.")

    def updateStudent(self, roll_no):
        current = self.head
        while current is not None:
            if current.roll_no == roll_no:
                current.name = input("Enter new name: ")
                current.marks = float(input("Enter new marks: "))
                print("Student updated successfully.")
                return
            current = current.next
        print("Student not found.")

    def deleteStudent(self, roll_no):
        if self.head is None:
            print("Student list is empty.")
            return
        if self.head.roll_no == roll_no:
            self.head = self.head.next
            print("Student deleted successfully.")
            return
        current = self.head
        while current.next is not None:
            if current.next.roll_no == roll_no:
                current.next = current.next.next
                print("Student deleted successfully.")
                return
            current = current.next
        print("Student not found.")

    def sortByMarks(self, ascending=True):
        current = self.head
        while current is not None:
            next_node = current.next
            while next_node is not None:
                if (ascending and current.marks > next_node.marks) or (not ascending and current.marks < next_node.marks):
                    current.roll_no, next_node.roll_no = next_node.roll_no, current.roll_no
                    current.name, next_node.name = next_node.name, current.name
                    current.marks, next_node.marks = next_node.marks, current.marks
                next_node = next_node.next
            current = current.next

    def sortByRollNo(self, ascending=True):
        current = self.head
        while current is not None:
            next_node = current.next
            while next_node is not None:
                if (ascending and current.roll_no > next_node.roll_no) or (not ascending and current.roll_no < next_node.roll_no):
                    current.roll_no, next_node.roll_no = next_node.roll_no, current.roll_no
                    current.name, next_node.name = next_node.name, current.name
                    current.marks, next_node.marks = next_node.marks, current.marks
                next_node = next_node.next
            current = current.next

students = StudentLinkedList()

while True:
    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display Students")
    print("6. Sort by Marks Ascending")
    print("7. Sort by Marks Descending")
    print("8. Sort by Roll No Ascending")
    print("9. Sort by Roll No Descending")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        students.addStudent(roll_no, name, marks)

    elif choice == 2:
        roll_no = int(input("Enter Roll No to delete: "))
        students.deleteStudent(roll_no)

    elif choice == 3:
        roll_no = int(input("Enter Roll No to update: "))
        students.updateStudent(roll_no)

    elif choice == 4:
        roll_no = int(input("Enter Roll No to search: "))
        students.searchStudent(roll_no)

    elif choice == 5:
        students.displayStudents()

    elif choice == 6:
        students.sortByMarks(True)
        students.displayStudents()

    elif choice == 7:
        students.sortByMarks(False)
        students.displayStudents()

    elif choice == 8:
        students.sortByRollNo(True)
        students.displayStudents()

    elif choice == 9:
        students.sortByRollNo(False)
        students.displayStudents()

    elif choice == 10:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
