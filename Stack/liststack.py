# Stack implemented with a List
class Stack:
    def __init__(self, data = None) -> None:
        if data:
            self.stack = data
        else:
            self.stack = []
    def push(self, value) -> None:
        self.stack.insert(0, value)
    def pop(self):
        if self.stack:
            popped = self.stack[0]
            self.stack = self.stack[1:len(self.stack)]
            return popped
        else:
            print("Err: You cannot pop from an empty stack.")
            return
    def isEmpty(self):
        return "True" if len(self.stack) == 0 else "False"
    def peek(self):
        return self.stack[0]
    def length(self):
        return len(self.stack)
    
    # for testing purposes, not typically found in stack implementation
    def display(self) -> None:
        for val in self.stack:
            print(val, end=", ")

# Testing
stackA = Stack()
stackA.push("apple")
stackA.push("banana")
stackA.push("cream")
stackA.push("dog")
stackA.display()
print(f"\nLength of stackA: {stackA.length()}")
popped = stackA.pop()
stackA.display()
print(f"\nLength of stackA: {stackA.length()}")
print(f"Popped element: {popped}")
print(f"Top element: {stackA.peek()}")
print(f"Is stackaA empty? : {stackA.isEmpty()}")
stackB = Stack()
print(f"Is stackB empty? : {stackB.isEmpty()}")
stackC = Stack([9,3,4])
stackC.display()
print(f"\nIs stackC empty? : {stackC.isEmpty()}")

        