# Testing...
from LinkedList.linkedlists import LinkedList

print("Contsructing an empty linked list: ")
list1 = LinkedList()
list1.display()
print("\n")

print("Constructing a linked list with user input: ")
list2 = LinkedList([56, 7, 8, -2, 4, -1, 0])
list2.display()
print("\n")

print("Adding values 45 and 67 to the beginning of the linked list: ")
list2.insertAtBeginning(45)
list2.display()
list2.insertAtBeginning(67)
list2.display()
print("\n")

print("Adding values 4 and 7 to the end of the linked list: ")
list2.insertAtEnd(4)
list2.display()
list2.insertAtEnd(7)
list2.display()
print("\n")

print("Deleting 3 values from the end of the list: ")
list2.deleteLast()
list2.display()
list2.deleteLast()
list2.display()
list2.deleteLast()
list2.display()
print("\n")


print("Deleting 1 value from the beginning of the list: ")
list2.deleteFirst()
list2.display()
print("\n")

print("Trying to delete from an empty list: ")
list1.deleteLast()
list1.display()
print("\n")

print("Updating the 5th value (index 4) in a list from -2 to 12: ")
list2.updateNode(12, 4)
list2.display()
print("\n")

print("Updating an out of bounds value: ")
list2.updateNode(12, 10)
list2.display()
print("\n")

print("Inserting 8 at index 0 and inserting -34 at index 6 ")
list2.insertNode(8, 0)
list2.display()
list2.insertNode(-34, 6)
list2.display()
print("\n")


print("Inserting a value in a list far out of the lists bounds: ")
list2.insertNode(12, -100)
list2.display()
list2.insertNode(12, 100)
list2.display()
print("\n")

print("Deleting the value at index 2")
list2.deleteNode(2)
list2.display()
print("\n")

print("Getting the current length of the list: ")
list2_length = list2.length()
print(list2_length)
print("\n")