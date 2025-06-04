#Remove N-th node from the end of a Linked List 
#----------------------------- Broute Force -------------------------------

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Linkedlist:
	def DeleteNthNodefromEnd(head, N):
		if head is None:
			return None
		cnt = 0
		temp = head
	
		# Count the number of nodes in the linked list
		while temp is not None:
			cnt += 1
			temp = temp.next
	
		# If N equals the total number of nodes, delete the head
		if cnt == N:
			newhead = head.next
			head = None
			return newhead
	
		# Calculate the position of the node to delete (res)
		res = cnt - N
		temp = head
	
		# Traverse to the node just before the one to delete
		while temp is not None:
			res -= 1
			if res == 0:
				break
			temp = temp.next
	
		# Delete the Nth node from the end
		delNode = temp.next
		temp.next = temp.next.next
		delNode = None
		return head
		
# Time Complexity: O(L)+O(L-N),
# Space Complexity:  O(1) 

#-------------------------- Optimal Solution ----------------------------------
class Node:
	def __init__(self,data):
		self.data = data 
		self.nrxt = None
	
class LinkedList:
	def DeleteNthNodefromEnd(head, N):
		# Create two pointers, fastp and slowp
		fastp = head
		slowp = head
	
		# Move the fastp pointer N nodes ahead
		for i in range(N):
			fastp = fastp.next
	
		# If fastp becomes None, the Nth node from the end is the head
		if fastp is None:
			return head.next
	
		# Move both pointers until fastp reaches the end
		while fastp.next is not None:
			fastp = fastp.next
			slowp = slowp.next
	
		# Delete the Nth node from the end
		delNode = slowp.next
		slowp.next = slowp.next.next
		delNode = None
		return head
