class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

test_ll = LinkedList()
test_ll.head = Node(1)
second = Node(2)
third = Node(3)

test_ll.head.next = second
second.next = third

test_ll.printList()