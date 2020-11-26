'''Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.'''

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