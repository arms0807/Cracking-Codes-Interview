'''Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. 
Note that the intersection is defined based on reference, not value. 
That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting. 

1 -> 2 -> 3 -> 4
                \
                  5 -> 7 -> 8
                 / 
     3 -> 4 -> 6

ans is 5.
'''
# it's irreasonable to check the value since the values can be duplicate so have to check the address of the nodes.
# 1) use a set to store the address of the iterated nodes from a list.
#    iterates the other one and see if the address is in the set. If so, then this will be the intersection.
#    this is from front to end
# 2) stack from end to front. We can find the intersection by checking the current nodes are having different address. Then the previous node
#    is the intersection

class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

class Solution:
    def getIntersectionNodeStack(self, headA: ListNode, headB: ListNode) -> ListNode:
        stackA, stackB = [], []
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
        pre = None
        while stackA and stackB:
            nodeA, nodeB = stackA.pop(), stackB.pop()
            if nodeA == nodeB:
                pre = nodeA
        return pre

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next
        while headB:
            if headB in visited:
                return headB
            headB = headB.next
        return None
        