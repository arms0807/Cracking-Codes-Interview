'''Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop. '''
# 1) fast and slow pointers. If there is a loop, the 2 pointers should meet together.
#    If the address of the 2 pointers are the same, it means there is a loop.
#    If not then no loop in the list.
# 2) use one hashset to check if the visiting node is in the set or not.
#    If yes, then there is a loop. If not, then no.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycleHashset(self, head: ListNode) -> bool:
        visited = set()
        while head:
            visited.add(head)
            head = head.next
            if head in visited:
                return True
        return False

    def hasCycleTwoPointers(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False