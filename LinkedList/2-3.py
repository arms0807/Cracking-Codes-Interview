'''Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.'''

# Can use slow and fast pointers. The fast one can go two nodes in one time, and the slow one go one at a time.
# When the fast go to the end, the position of the slow one will arrive at the middle position. 
# We can delete it with 2 ways
# 1. use another pointer to record the previous node of the slow one. Then use the pre node to point to the slow.next
# 2. without using the pre node. We can modify the value of slow node with the value of fast node. 
# Then point the slow.next to the fast.next. Then fast.next = None.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # The solution in the book is confusing. It only show how to deal with delete a Node when we don't have access to the whole list.

    def deleteMiddle(self, root):
        #This is the solution for the case that when you are able to access to the list
        fast = slow = root
        pre = None
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        if pre:
            pre.next = slow.next
        return root
    
    def show(self, root):
        while root:
            print(root.val, end=" ")
            root = root.next
        print()

n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(4)
Solution().show(n1)
Solution().show(Solution().deleteMiddle(n1))