'''Create a Student Record Management System using linked list
    • Use a singly/doubly linked list to store student data (Roll No, Name, Marks).
    • Perform operations: Add, Delete, Update, Search, and Sort.
    • Display records in ascending/descending order based on marks or roll number.'''
      
class Node:
    def __init__(self, roll_no , name , marks):
        self.roll_no = roll_no 
        self.name = name 
        self.marks = marks 
        self.next = None     
    
class StudentLinkedList:
    
    def __init__(self):
        self.head = None 
        
    def addStudent(self , roll_no , name , marks ):
        new_node = Node(roll_no , name , marks)
        
        if self.head is None:
            self.head = new_node
            print("Student added successfully.")
            return 
        
        current = self.head
         
        while current.next is not None:
            current = self.next 
            
        current.next = new_node
        print("Student added successfully.")
    
    def displayStudent(self):
        if self.head is None:
            print("Student list is empty.")
            return 
        current = self.head 
        while current is not None:
            print("Roll no:",current.roll_no)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    