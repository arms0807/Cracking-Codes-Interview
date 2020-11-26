'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1 's digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295. Output:2 -> 1 -> 9.Thatis,912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. Output:9 -> 1 -> 2.Thatis,912.'''

# Follow up
# stack them first
# pop them and add them if there is additional then keep adding to the front
# while root1 and root2:
#	stack1.append(root1 if root1)
#	stack2.append(root2 if root2)
# addition = 0
# cur = pre = None
# while stack1 or stack2 or addition == 1:
#	value1 = stack1 pop, value2 = stack2 pop
#	value = value1 + value2 + additional
#	additional = 1 if value >= 10 else 0
#	value = value-10 if value>=10 else value
#	cur = Node(value)
#	cur.next = pre	
#	pre = cur
# return cur

# add = 0, ans = head = None
# while(list1 or list2 or addition==1):
#	v = list1.val if list1 + list2.val if list2 + addition
#	addition = 1 if v >= 10 else 0
# 	v = v-10 if v >= 10 else v
#	if not ans:
#		ans = new Node(v)
#	else:
#		ans.next = new Node(v)
#		ans = ans.next
#	if list1:
#		list1 = list1.next
#	if list2:
#		list2 = list2.next


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution:
	def followUp(self, root1, root2):
		stack1 = stack2 = []
		while root1 or root2:
			if root1:
				stack1.append(root1)
				root1 = root1.next
			if root2:
				stack2.append(root2)
				root2 = root2.next
		cur = pre = None
		additional = 0
		while stack1 or stack2 or additional == 1:
			node1, node2 = stack1.pop() if stack1 else None, stack2.pop() if stack2 else None
			value = (node1.val if node1 else 0) + (node2.val if node2 else 0) + additional
			additional = 1 if value >= 10 else 0
			value = value-10 if value >= 10 else value
			cur = Node(value)
			cur.next = pre
			pre = cur
		return cur

	def addTwoList(self, root1, root2):
		addition = 0
		head = ans = None
		while root1 or root2 or addition == 1:
			value = (root1.val if root1 else 0) + (root2.val if root2 else 0) + addition
			addition = 1 if value >= 10 else 0
			value = value-10 if value >= 10 else value
			if not ans:
				ans = Node(value)
				head = ans
			else:
				ans.next = Node(value)
				ans = ans.next
			if root1:
				root1 = root1.next
			if root2:
				root2 = root2.next
		return head

	def print(self, root):
		while root:
			print(root.val, end=" ")
			root = root.next
		print()

n1 = Node(7)
n1.next = Node(1)
n1.next.next = Node(6)
n2 = Node(5)
n2.next = Node(9)
n2.next.next = Node(2)
Solution().print(Solution().addTwoList(n1, n2))
n1 = Node(6)
n1.next = Node(1)
n1.next.next = Node(7)
n2 = Node(2)
n2.next = Node(9)
Solution().print(Solution().followUp(n1, n2))