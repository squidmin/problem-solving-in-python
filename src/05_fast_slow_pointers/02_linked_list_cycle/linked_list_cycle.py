class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedListCycle:
    @staticmethod
    def has_cycle(head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True  # found the cycle
        return False


if __name__ == "__main__":
    head = ListNode(2)
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(6)
    head.next.next.next.next.next = ListNode(7)
    print("LinkedList has cycle:", LinkedListCycle.has_cycle(head))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle:", LinkedListCycle.has_cycle(head))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle:", LinkedListCycle.has_cycle(head))
