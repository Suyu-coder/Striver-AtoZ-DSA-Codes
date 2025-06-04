
# Broute Force------------------------------------------------------

class Node:
	def __init__(self,data):
		self.data=  data 
		self.next = None
		
class Linkedlist:
	def is_palindrome(head):
		# Initialize an empty stack to store node data
		stack = []
		temp = head
	
		# Traverse the linked list and push data onto the stack
		while temp is not None:
			stack.append(temp.data)
			temp = temp.next
	
		# Reset temp to the head of the linked list
		temp = head
	
		# Compare the data from the stack with the linked list nodes
		while temp is not None:
			if temp.data != stack.pop():
				# If data doesn't match, it's not a palindrome
				return False
			temp = temp.next
	
		# If all data matches, it's a palindrome
		return True

	def print_linked_list(head):
		temp = head
		# Traverse the linked list and print each node's data
		while temp is not None:
			print(temp.data, end=" ")
			temp = temp.next
		print()
		
		
# Time Complexity: O(2 * N)
# Space Complexity: O(N)

#-------------------------- Optimal Solution -------------------------------

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
class LinkedList:
	def reverse_linked_list(head):
		prev = None
		current = head
	
		while current is not None:
			next_node = current.next  # Store the next node
			current.next = prev  # Reverse the link
			prev = current  # Move prev to current node
			current = next_node  # Move to the next node
	
		return prev  # New head of the reversed list

	def is_palindrome(head):
		# Check if the linked list is empty or has only one node
		if head is None or head.next is None:
			return True
	
		# Initialize two pointers, slow and fast, to find the middle of the linked list
		slow = head
		fast = head
	
		# Traverse the linked list to find the middle using slow and fast pointers
		while fast.next is not None and fast.next.next is not None:
			slow = slow.next  # Move slow pointer one step at a time
			fast = fast.next.next  # Move fast pointer two steps at a time
	
		# Reverse the second half of the linked list starting from the middle
		new_head = reverse_linked_list(slow.next)
	
		# Pointer to the first half
		first = head
	
		# Pointer to the reversed second half
		second = new_head
		while second is not None:
			# Compare data values of nodes from both halves
			if first.data != second.data:
				# Reverse the second half back to its original state
				reverse_linked_list(new_head)
				return False  # Not a palindrome
	
			first = first.next  # Move the first pointer
			second = second.next  # Move the second pointer
	
		# Reverse the second half back to its original state
		reverse_linked_list(new_head)
		return True  # The linked list is a palindrome
		
		
# Time Complexity: O (2* N) 
# Space Complexity: O(1)
