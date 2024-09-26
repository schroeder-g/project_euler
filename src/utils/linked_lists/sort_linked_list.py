class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


one = ListNode(1)
two = ListNode(2)
four = ListNode(4)

one.next = two
two.next = four


def insertValueIntoSortedLinkedList(l, value):
    list_counter = 0
    current_n = l

    # if list is blank, create a new linked list node pointing to nothing
    if not current_n:
        new_node = ListNode(value)
        return new_node

    while current_n is not None:
        print(current_n.value)
        next_n = current_n.next
        prev_n = current_n

        # If at head & the param val is a smaller num,
        if list_counter == 0 and current_n.value > value:
            # Create new_node(arg) at beginning of list
            new_node = ListNode(value)
            # Point new node's link to current list item. It's the new head
            new_node.next = current_n
            print(new_node, new_node.value, new_node.next)
            return new_node

        # if the param is larger than the current value and the next value...
        if next_n and current_n.value < value < next_n.value:
            new_node = ListNode(value)

            # link it to the original value's next and point it to the ''next value''.
            new_node.next = prev_n.next
            prev_n.next = new_node
            print(new_node, new_node.value, new_node.next.value)
        # if at end of list...
        if current_n.value < value and current_n.next is None:
            new_node = ListNode(value)

            current_n.next = new_node

            print(new_node, new_node.value, new_node.next)

        list_counter += 1
        current_n = next_n
    return l


print(insertValueIntoSortedLinkedList(None, -100))
