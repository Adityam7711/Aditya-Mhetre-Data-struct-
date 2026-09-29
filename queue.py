
Max = 6
queue = []

def enqueue():
    if(len(queue) == Max):
        print("queue is overflow")
    else:
        element = int(input("Enter element to insert into queue: "))
        queue.append(element)
        print(element, "element insert successfully")
       
def deueue():
    if(len(queue) == 0):
        print("queue is empty")
        return
    element = queue.pop(0)
    print(element, "element delete successfully")
    
    
def peek():
    if(len(queue) == 0):
        print("queue is empty")
    else:
        print(queue[0], "top most element in queue")
        
def size():
    if(len(queue) == 0):
        print("queue is empty")
    else:
        print(len(queue))
        
def empty():
    if(len(queue) == 0):
        print("queue is empty")
    else:
        print("queue is not empty")
        
def full():
    if(len(queue) == Max):
        print("queue is full")
    else:
        print("queue is not full")
        
def display():
    if(len(queue) == 0):
        print("queue is empty")
    else:
        print(queue)
        
        
while True:
    print("qyeue using python list")
    print("\n1.enqueue \n2.dequeue \n 3.peek \n4.size \n5.empty \n6.full \n7.display")
    choice=input(int("enter your choice"))
    if choice=="1":
        enqueue()
    elif choice=="2":
        deueue()
    elif choice=="3":
        peek()
    elif choice=="4":
        size()
    elif choice=="5":
        empty()
    elif choice=="6":
        full()
    elif choice=="7":
        display()
    elif choice=="8":
        print("program is terminated")
        break
    else:
        print("Invalid choice")
        
