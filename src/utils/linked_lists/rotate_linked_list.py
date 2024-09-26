class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_linked_list_counter_clockwise(head, k):
    if k == 0:
        return

    current = head

    # Move pointer to end of the list
    while current.next:
        current = current.next

    # Make a temporary cycle, connecting tail to head.
    current.next = head

    # shift pointer the target number of spaces, k, forward.
    for _ in range(k):
        current = current.next

    # change head node to the value after k. Break cycle.
    head = current.next
    current.next = None

    return head


n6 = Node(6)
n5 = Node(5, n6)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
head = Node(0, n1)


def print_list(node):
    while node != None:
        print(node.val, end=" ")
        node = node.next


print_list(head)
head = rotate_linked_list_counter_clockwise(head, 3)
print("\n")
print_list(head)
