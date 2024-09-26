class ListNode(object):
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


l1_head = ListNode(0)

l2_head = ListNode(2)

l1_head.next = None
l2_head.next = None


def mergeTwoLinkedLists(l1, l2):
    myList = []
    hasNotMerged = 1
    # Ensure neither list is empty
    if l2 and not l1:
        return l2
    if l1 and not l2:
        return l1
    if not l1 and not l2:
        return
    else:
        current_n = l1

        # append l2
        if current_n.next is None and hasNotMerged:
            current_n.next = l2
            hasNotMerged -= 1

        else:
            while current_n.next is not None:

                current_n = current_n.next

                # Merge Linked List 2 onto the end of Linked List 1
                if current_n.next is None and hasNotMerged:
                    current_n.next = l2
                    hasNotMerged -= 1

        # Return to beginning of list
        current_n = l1

        # This loop moves all values less than next value forward.
        while current_n:
            next_n = current_n.next

            myList.append(current_n)
            current_n = next_n

        sorted_list = sorted(myList, key=lambda nodule: nodule.value)
        sorted_list[-1].next = None
        for index, node in enumerate(sorted_list[:-1:]):
            node.next = sorted_list[index + 1]

        return sorted_list[0]


print(mergeTwoLinkedLists(l1_head, l2_head))
