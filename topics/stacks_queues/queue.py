class Queue:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue
    
    def enqueue(self, item):
        self.stack1.append(item)
    
    def dequeue(self):
        if not self.stack2:  # Transfer stack1 to stack2 if empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:  # Queue is empty
            return None
        return self.stack2.pop()

# Test the queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Dequeued:", q.dequeue())  # Output: Dequeued: 1
print("Dequeued:", q.dequeue())  # Output: Dequeued: 2
q.enqueue(4)
print("Dequeued:", q.dequeue())  # Output: Dequeued: 3