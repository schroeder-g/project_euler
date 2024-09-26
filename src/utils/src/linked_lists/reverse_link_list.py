# A single node of a singly Linked List
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


def reverseLinkedList(l):
    reversed_nodes_counter = len(l)
    current = l
    previous = None
    if l is None or l.next is None or l == []:
        return l
    else:
        while reversed_nodes_counter > 0:
            newly_aligned_node = current
            current = current.next
            current.next = previous
            previous = newly_aligned_node

            reversed_nodes_counter -= 1


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
