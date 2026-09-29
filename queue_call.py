'''A call center receives incoming calls, and each call is assigned a unique customer ID. The
calls are answered in the order they are received. Your task is to simulate the call queue of a
call center using a queue data structure.
        • addCall(customerID, callTime): Add a call to the queue with the customer ID and the
            call time (in minutes).
        • answerCall(): Answer and remove the first call from the queue.
        • viewQueue(): View all calls currently in the queue without removing them.
        • isQueueEmpty(): Check if the queue is empty.
'''

class CallQueue :
    def __init__(self):
        self.queue = [None]*10 
        self.front = -1 
        self.rear = -1 
        
    def isQueueEmpty(self):
        if  self.front == -1 :
           return True 
        else:
            return False
        
    def addCall(self, CustId , CallTime):
        if self.rear == 9:
            print("QUeue is full.")
            return 
        
        if self.front == -1 :
            self.front = 0
        self.rear = self.rear + 1
        self.queue[self.rear] = [CustId, CallTime]
        print("call added ") 
        
    def ansCall(self):
        if self.isQueueEmpty():
            print("Queue is empty.")
            return 
        call = self.queue[self.front]
        
        print("Answering Cust Id:",call[0]) 
        print("Call Time:", call[1], "minutes")    
        
        self.front = self.front + 1 
        
        if self.front > self.rear:
            self.front = -1 
            self.rear = -1 
        
    def viewQueue(self):

        # Check if queue is empty.
        if self.isQueueEmpty():
            print("Queue is empty.")
            return

        print("Current Queue:")

        # Start from front and go up to rear.
        i = self.front

        while i <= self.rear:

            # Get the call at position i.
            call = self.queue[i]

            # Display customer information.
            print(
                "Customer ID:", call[0],
                "| Call Time:", call[1], "minutes"
            )

            # Move to the next position.
            i = i + 1


# ----------------------------------------
# USING THE QUEUE
# ----------------------------------------

cq = CallQueue()

cq.addCall(101, 5)
cq.addCall(102, 8)
cq.addCall(103, 12)

cq.viewQueue()

cq.ans                                                                                                                                                Call()

cq.viewQueue()

print("Is queue empty?", cq.isQueueEmpty())

