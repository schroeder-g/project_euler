class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def print_list(head):
    k = head
    while k:
        print(k.data, end="-> ")
        k = k.next
    print("None")


# sorts two linked lists in increasing order, merging their nodes
def sorted_merge(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    if l1.data <= l2.data:
        ans = l1
        ans.next = sorted_merge(l1.next, l2)
    else:
        ans = l2
        ans.next = sorted_merge(l1, l2.next)

    return ans


def split_in_half(head):
    if head is None or head.next is None:
        return head, None

    slow, fast = head, head.next

    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next

    ans = head, slow.next
    slow.next = None

    return ans


def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    left, right = split_in_half(head)

    left, right = merge_sort_linked_list(left), merge_sort_linked_list(right)

    return sorted_merge(left, right)


if __name__ == "__main__":

    # input keys
    keys = [8, 6, 4, 9, 3, 1]

    head = None
    for key in keys:
        head = ListNode(key, head)

    # sort the list
    head = merge_sort_linked_list(head)

    # print the sorted list
    print_list(head)
