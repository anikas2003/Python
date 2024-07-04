from LinkedList.linkedlists import LinkedList

class Stack:
    def __init__(self, stack = None) -> None:
        if stack:
            self.stack = LinkedList(stack)
        else:
            self.stack = LinkedList()
    def push(self, data) -> None:
        self.stack.insertAtBeginning(data)
    def pop(self):
        popped = self.stack.getValue(0)
        self.stack.deleteFirst()
        return popped
    def isEmpty(self):
        return "True" if self.stack.length() == 0 else "False"
    def length(self):
        return self.stack.length()
    def display(self):
        return self.stack.display()
    
# Same testing as liststack.py
stackA = Stack()
stackA.push("apple")
stackA.push("banana")
stackA.push("cream")
stackA.push("dog")
stackA.display()
print(f"Length of stackA: {stackA.length()}")
popped = stackA.pop()
stackA.display()
print(f"Length of stackA: {stackA.length()}")
print(f"Popped element: {popped}")
print(f"Is stackaA empty? : {stackA.isEmpty()}")
stackB = Stack()
print(f"Is stackaB empty? : {stackB.isEmpty()}")
stackC = Stack([9,3,4])
stackC.display()
print(f"\nIs stackC empty? : {stackC.isEmpty()}")