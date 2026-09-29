# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.arr = [0] * size
#         self.top = -1

#     def push(self, x):
#         if self.top == self.size - 1:
#             return

#         self.top += 1
#         self.arr[self.top] = x

#     def pop(self):
#         if self.top == -1:
#             return -1

#         ele = self.arr[self.top]
#         self.top -= 1
#         return ele

#     def peek(self):
#         if self.top == -1:
#             return -1

#         return self.arr[self.top]

#     def isEmpty(self):
#         return self.top == -1

#     def isFull(self):
#         return self.top == self.size - 1


# if __name__ == '__main__':
#     s = Stack(5)

#     s.push(10)
#     s.push(20)
#     s.push(30)

#     print("Top element:", s.peek())
#     print("Popped:", s.pop())
#     print("Popped:", s.pop())
#     print("Is empty:", s.isEmpty())

class Stack:
    def __init__(self, size):
        self.size = size 
        self.arr =[0]*size 
        self.top =-1 

def push(self,x):
    if self.top ==
                                                                      self.size -1 :
        return 
    
    self.top += 1 
    self.arr[self.top] = x
    
def pop(self):
    if self.top == -1:
        return -1 
    ele = self.arr[self.top]
    self.top -= 1 
    return ele 
    
    



































