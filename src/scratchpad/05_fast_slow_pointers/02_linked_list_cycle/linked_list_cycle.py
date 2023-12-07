class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedListCycle:
    @staticmethod
    def has_cycle(head):
        return False

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print("LinkedList has cycle:", LinkedListCycle.has_cycle(head))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle:", LinkedListCycle.has_cycle(head))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle:", LinkedListCycle.has_cycle(head))
