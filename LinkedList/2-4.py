'''Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 - > 10 -> 2 -> 1 [partition = 5)
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8 '''

# (Not Recommended)
# 1. The Naive way is to fetch all the value from the linked list into a list collection. Then sort it and create them back to the linkedlist.
# 2. use stack to get the last node, then use while loop to check the first node
# stack through the input list
# while pointer != stack.pop():
#    if stack.pop().val < partition and pointer.val >= partition:
#       swap(stack.pop(), pointer)
#   elif stack.pop().val >= partiton:
#       stack.pop()
#   elif pointer.val < partition:
#       pointer = pointer.next
# 3. 
import collections

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def solutionFromBook(self, root, partition):
        # Instead of using extra space, we can create a new list for the answer
        start_start = start = start_end = None
        end_start = end = end_end = None
        while root:
            if root.val < partition:
                if not start_start:
                    start_start = root
                start_end = root
                if start:
                    start.next = start_end
                start = start_end
            else:
                if not end_start:
                    end_start = root
                end_end = root
                if end:
                    end.next = end_end
                end = end_end
            root = root.next
        start_end.next = end_start
        return start_start


    def swapWithPartitionNoSpace(self, root, partition):
        #  Time Complexity O(N^2) where N is the length of root, Space Complexity O(1).
        if not root:
            return root
        small = large = root
        while small:
            if small.val < partition:
                small = small.next
            else:
                large = small.next
                while large and large.val >= partition:
                    large = large.next
                if not large:
                    return root
                large.val, small.val = small.val, large.val
        return root
                

    def swapWithPartitionOpt(self, root, partition):
        #  Time Complexity O(2N) where N is the length of root, Space Complexity O(N) the N is the same as the Time one.
        if not root:
            return root
        head = root
        deque = collections.deque()
        while head:
            deque.append(head)
            head = head.next
        left = right = None
        while len(deque) > 0:
            if not left and not right:
                left = deque.popleft()
                right = deque.pop()
            if left.val >= partition and right.val < partition:
                left.val, right.val = right.val, left.val
            elif deque and left.val < partition:
                left = deque.popleft()
            elif deque and right.val >= partition:
                right = deque.pop()
        return root
            

    def swapWithPartition(self, root, partition):
        # Time Complexity O(2N) where N is the length of root, Space Complexity O(2N) the N is the same as the Time one.
        if not root: 
            return root
        head = root
        visit = set()
        stack = []
        while head:
            stack.append(head)
            head = head.next
        head = root
        last = stack.pop()
        while head:
            visit.add(last)
            visit.add(head)
            if last.val < partition and head.val >= partition:
                last.val, head.val = head.val, last.val
            elif last.val >= partition:
                last = stack.pop()
                if last in visit:
                    break
            elif head.val < partition:
                head = head.next
                if head in visit:
                    break
        return root

    def print(self, root):
        while root:
            print(root.val, end=" ")
            root = root.next
        print()

n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(4)
n1.next.next.next.next = Node(5)
n1.next.next.next.next.next = Node(6)
n1.next.next.next.next.next.next = Node(7)
n1.next.next.next.next.next.next.next = Node(8)
Solution().print(n1)
Solution().print(Solution().swapWithPartitionOpt(n1, 5))
Solution().print(Solution().swapWithPartition(n1, 5))
Solution().print(Solution().solutionFromBook(n1, 5))
