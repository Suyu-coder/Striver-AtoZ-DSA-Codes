# delete middle node of the linked list 

#------------------ Broute Force ---------------------------------
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class LinkedList:
	def delete_middle(head):
		# Initialize a temporary node
		# to traverse the linked list
		temp = head
		
		# Variable to hold the number
		# of nodes in the linked list
		n = 0
		
		# Loop to count the number of
		# nodes in the linked list
		while temp is not None:
			n += 1
			temp = temp.next
		
		# Calculate the index of the middle node
		res = n // 2
		
		# Reset the temporary node to
		# the beginning of the linked list
		temp = head
		
		# Loop to find the
		# middle node to delete
		while temp is not None:
			res -= 1
			
			# If the middle node is found
			if res == 0:
				
				# Create a pointer
				# to the middle node
				middle = temp.next
				
				# Adjust pointers to
				# skip the middle node
				temp.next = temp.next.next
				
				# Delete the middle node
				# (Python handles memory management)
				# No explicit free() needed
				
				# Exit the loop after
				# deleting the middle node
				break
			
			# Move to the next node
			# in the linked list
			temp = temp.next
		
		# Return the head of the
		# modified linked list
		return head
	
#------------------ Broute Force --------------------------------- 

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
class LinkedList:
	def delete_middle(head):
    # If the list is empty or has only one node, return None
		if head is None or head.next is None:
			return None
	
		# Initialize slow and fast pointers
		slow = head
		fast = head.next.next
	
		# Move 'fast' pointer twice as fast as 'slow'
		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next
	
		# Delete the middle node by skipping it
		slow.next = slow.next.next
		return head
	
