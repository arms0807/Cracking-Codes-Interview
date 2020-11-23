class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution:
	def remove_Duplicate(self, head):
		#  Solution without extra space
		temp = head
		while temp:
			runner = temp
			while runner.next:
				if runner.next.val == temp.val:
					runner.next = runner.next.next
				else:
					runner = runner.next
			temp = temp.next
		return head

	def remove_Duplicate_Extra_Space(self, head):
		#  Solution with extra space
		d = set()
		root = head
		while head:
			if head.val not in d:
				d.add(head.val)
				pre = head
			else:
				pre.next = head.next
				head = pre.next
		return root

	def run(self, head):
		while head:
			print(head.val, end = "->")
			head = head.next
		print("None")

N0 = Node(1)
N1 = Node(1)
N2 = Node(1)
N3 = Node(1)
N4 = Node(1)
N0.next = N1
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = Node(1)
Solution().run(N0)
temp = Solution().remove_Duplicate_Extra_Space(N0)
Solution().run(temp)