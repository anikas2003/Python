# Queue implemented with a list
class Queue:
    def __init__(self, data = None) -> None:
        if data:
            self.queue = data
        else:
            self.queue = []
    def enqueue(self, value) -> None:
        self.queue.append(value)
    def dequeue(self):
        if self.queue:
            dequeued = self.queue[0]
            self.queue = self.queue[1:len(self.queue)]
            return dequeued
        else:
            print("Err: You cannot dequeue from an empty queue.")
            return
    def isEmpty(self) -> None:
        return True if len(self.queue) == 0 else False
    def peek(self):
        return self.stack[0]
    def length(self):
        return len(self.queue)
    def display(self):
        for val in self.queue:
            print(val, end=", ")
    
# Testing
queueA = Queue()
queueA.dequeue()
queueA.enqueue(5)
queueA.display()
print("\n")
queueA.enqueue(6)
queueA.enqueue(7)
queueA.enqueue(17)
queueA.enqueue(3)
queueA.display()
print("\n")
queueA.dequeue()
queueA.display()
print("\n")
queueA.dequeue()
queueA.display()
print("\n")
    