# Linked Lists
from typing import List, Any

# Linked lists are a collection of Nodes
# They start with the "head" node and end with next pointing to None
class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data : List[Any] = None) -> None:
        if data:
            new_node = Node(data[len(data)-1])
            self.head = new_node
            for i in range(len(data)-2, -1, -1):
                new_node = Node(data[i])
                new_node.next = self.head
                self.head = new_node
        else: 
            self.head = data


    # insert a node at the beginning of the list
    def insertAtBeginning(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # delete the first node of the list
    def deleteFirst(self) -> None:
        list = self.head

        if list is not None:
            self.head = list.next
        else:
            print("Err: Cannot delete from an empty list.")
 
    # insert a node at the end of the list
    def insertAtEnd(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            traverser = self.head
            while traverser.next:
                traverser = traverser.next
            traverser.next = new_node

    # delete the last node 
    def deleteLast(self) -> None:
        if self.head is not None:
            traverser = self.head
            pre_traverser = traverser
            while traverser.next:
                pre_traverser = traverser
                traverser = traverser.next
            if (pre_traverser.next == None):
                self.head = None
            else:
                pre_traverser.next = None
        else:
            print("Err: Cannot delete from an empty list.")

    # update node at specific position
    def updateNode(self, data, index) -> None:
        if self.head is None:
            print("Err: There are no nodes to update, the list is empty.")
        else:
            nodetbUpdated = self.head
            for i in range (0, index):
                if nodetbUpdated.next:
                    nodetbUpdated = nodetbUpdated.next
                else:
                    print(f"Err: The index you've provided is out of bounds. Index {index} is out of bounds.")
                    return
            if nodetbUpdated:
                nodetbUpdated.data = data


    # insert node at specific position
    def insertNode(self, data, index) -> None:
        if self.head is None:
            if index != 0:
                print("Err: You cannot insert data at any other index than 0 as the list is currently empty.")
            else:
                self.insertAtBeginning(data)
            return
        if index == 0:
            self.insertAtBeginning(data)
            return
        if index > (self.length() - 1) or index < 0:
            print(f"Err: Invalid index. Index {index} is out of bounds.")
            return
        traverser = self.head
        pre_traverser = traverser
        for i in range (0, index):
            pre_traverser = traverser
            traverser = traverser.next
        insert = Node(data, traverser)
        pre_traverser.next = insert

    # get node given index (for stack/queue operations)
    def getValue(self, index):
        if self.head is None:
            print("Err: You cannot get value from an empty list.")
            return 
        if index > self.length() or index < 0:
            print("Err: The index you've provided is too high or low.")
            return
        else:
            if index == 0:
                return self.head.data
            curr = self.head
            for i in range(0, index):
                curr = curr.next
            return curr.data
        

    # delete node at specific position
    def deleteNode(self, index) -> None:
        if self.head is None:
            print("Err: You cannot delete from an empty list.")
            return
        else:
            if index == 0:
                self.deleteFirst()
            nodetbDeleted = self.head
            prev = nodetbDeleted
            for i in range (0, index):
                if nodetbDeleted.next:
                    prev = nodetbDeleted
                    nodetbDeleted = nodetbDeleted.next
                else:
                    print(f"Err: The index you've provided is out of bounds. Index {index} is out of bounds.")
                    return
            if nodetbDeleted:
                prev.next = nodetbDeleted.next


    # get length of linked list
    def length(self) -> int:
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.next
        return count


    # print the linked list
    def display(self) -> None :
        list = self.head
        while list:
            print(f"{list.data}", end=" -> ")
            list = list.next
        print("None")
        # print(f"Length: {self.length()}")
    

