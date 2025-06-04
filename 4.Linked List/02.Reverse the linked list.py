
# Reverse the linked list 

class Node:
	def __init__(self,data):
		self.data = data 
		self.next = None
		
class Linked_list:
	def reverseLinkedList(head):
		temp = head 
		stack = []
		
		while temp is not None:
			stack.append(temp.data)
			
			temp = temp.next
			
		temp = head 
		while temp is not None:
			temp.data = stack.pop()
			
			temp = temp.next
		
		return head 
		
	def print_Linkedlist(head):
		temp = head 
		while temp is not None:
			print(temp.data , end = " ")
			temp = temp.next 
		print()
		
#Time Complexity: O(2N) 
#Space Complexity: O(N)


# optimal solution (3 pointer approach / link changes approach)

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None 
		
class Linked_list:
	
	def reverseLinkedList(head):
		temp = head 
		prev = None
		
		while temp is not None:
			# Store the next node in 'front'
			# to preserve the reference
			front= temp.next 
			
			# Reverse the direction of the current
			# node's 'next' pointer to point to 'prev'
			temp.next = prev 
			
			# Move 'prev' to the current 
			# node, for the next iteration
			prev = temp 
			
			# Move 'temp' to 'front' node
			# advancing traversal
			temp = front 
			
		# Return the new head
		# of the reversed linked list
		return  prev 
		
#Time Complexity: O(N) 
#Space Complexity: O(1)
