
# Middle of linked list 

# Broute Force solution 

class node:
	def __init__(self,data):
		self.data = data 
		self.next = None 
	
class LinkedList:	
	# function to find the middle element 
	def find_middle(head):
		# If the list is empty or has only 
		# one element, return the head
		# as it's the middle.
		
		if head is None or head.next is None:
			return head 
			
		temp = head 
		count = 0 
		
		#countng the number of node in linked list 
		
		while temp is not None:
			count +=1
			temp = temp.next 
			
		mid = count // 2 + 1
		temp = head 
		
		# here travesrsinfg for the middle node 
		while temp is not None:
			mid = mid - 1
			
			# checking the middle position is reached 
			if mid == 0:
				break 
			
			temp = temp.next 
		return temp 
		
# Time Complexity: O(N+N/2) 
# Space Complexity : O(1)

# Optimal solution ( tortose and Hare Algorithm)

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None 
		
class LinkedList:
	def find_middle(head):
		slow = head 
		fast = head 
		
		while fast is not None or fast.next is not None:
			# Move fast two steps.
			fast = fast.next.next
			# Move slow one step.
			slow = slow.next 
			
		# here slow will be middle node 
		return slow 
	
# Time Complexity: O(N/2)
# Space Complexity : O(1)	
	
	
	
# Creating a sample linked list: 
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Find the middle node
middle_node = find_middle(head)

# Display the value of the middle node
print("The middle node value is:", middle_node.data)
