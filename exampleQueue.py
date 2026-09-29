class CallQueue:

    def __init__(self):
        # Create a fixed-size array for storing calls.
        self.queue = [None] * 10

        # front points to the first call.
        # -1 means the queue is currently empty.
        self.front = -1

        # rear points to the last call.
        # -1 means no call has been added yet.
        self.rear = -1

    def isQueueEmpty(self):

        # If front is -1, there is no call in the queue.
        if self.front == -1:
            return True
        else:
            return False

    def addCall(self, customerID, callTime):

        # Check if the queue is full.
        if self.rear == 9:
            print("Queue is full.")
            return

        # If this is the first call,
        # set front to position 0.
        if self.front == -1:
            self.front = 0

        # Move rear one position forward.
        self.rear = self.rear + 1

        # Store the call at the rear position.
        self.queue[self.rear] = [customerID, callTime]

        print("Call added.")

    def answerCall(self):

        # First check whether the queue is empty.
        if self.isQueueEmpty():
            print("Queue is empty.")
            return

        # Get the call at the front.
        call = self.queue[self.front]

        # Display the call being answered.
        print("Answering Customer ID:", call[0])
        print("Call Time:", call[1], "minutes")

        # Remove the call logically by moving front forward.
        self.front = self.front + 1

        # If front has crossed rear,
        # there are no calls left.
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

cq.answerCall()

cq.viewQueue()

print("Is queue empty?", cq.isQueueEmpty())
