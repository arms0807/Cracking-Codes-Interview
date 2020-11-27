'''Palindrome: Implement a function to check if a linked list is a palindrome. '''
# 1 -> 2 -> 3 -> 2 -> 1
# 1 -> 2 -> 3 -> 3 -> 2 -> 1
# extra space : 1. use an array to store the values of nodes. Then use 2 pointers to check if it is palindrome. O(N) for both space and time.
#               2. check the half size of nodes of the list. Reverse the half then check if it's palindrome by stack.
# reverse the list : then go one by one to see if it's palindrom
# recursive method : Advanced, though it will cost O(N) space. It's easy to think it in stack then try to implement it in recursive way.
import copy

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def recursive(self, head):
        self.temp = head
        def dfs(cur = head):
            if cur:
                if not dfs(cur.next):
                    return False
                if cur.val != self.temp.val:
                    return False
                self.temp = self.temp.next
            return True
        return dfs()

    def checkWithReverse(self, head):
        reversed_head = self.reverse(head)
        self.print(head)
        while head:
            if head.val != reversed_head.val:
                return False
            head = head.next
            reversed_head = reversed_head.next
        return True

    def reverse(self, head):
        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        # 5 -> 4 -> 3 -> 2 -> 1 -> None
        # copy.deepcopy() important since the type of passing value to function is the combination of pass by value and pass by reference
        # for the mutable type is always pass by ref, which means if you try to modify it in this function the original value in the calling method
        # will also be modified.
        self.temp = head
        pre = None
        cur = self.temp
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

    def print(self, head):
        while head:
            print(head.val, end = " ")
            head = head.next

    def checkWithArray(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.checkIfPalindrome(arr)
    
    def checkIfPalindrome(self, arr):
        for index in range(len(arr)//2):
            if arr[index] != arr[len(arr)-index-1]:
                return False
        return True

n1 = Node(1)
n1.next = Node(1)
n1.next.next = Node(2)
n1.next.next.next = Node(1)
n1.next.next.next.next = Node(1)
print(Solution().checkWithReverse(n1))
n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(3)
n1.next.next.next.next = Node(2)
n1.next.next.next.next.next = Node(1)
print(Solution().checkWithReverse(n1))
n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(3)
n1.next.next.next.next = Node(2)
n1.next.next.next.next.next = Node(5)
print(Solution().checkWithReverse(n1))