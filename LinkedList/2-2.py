# Return Kth to Last: 
# Implement an algorithm to find the kth to last element of a singly linked list.

# 1) don't know the length -> first get the length of the list -> iterate it to len() - k
# 2) if we know the length									   -> iterate it to len() - k
# 3) since we don't know the length of the list, we can use dfs to reach to the end 
# then count the number if it's K then means it's the answer
# 4) we can use 2 pointers. First pointer can run first K elements. The second one can go
# from the header then the both pointers can run simultaneously. When the first one to the 
# end the second one will be the answer.

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution:
	def returnKthToLast(self, head, k):
		# Naive solution
		temp = head
		l = self.count(temp)
		run = l-k
		while run > 1:
			head = head.next
			run -= 1
		return head.val

	def count(self, head):
		length = 0
		while head:
			length+=1
			head = head.next
		return length

N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5

print(Solution().returnKthToLast(N1, 1))