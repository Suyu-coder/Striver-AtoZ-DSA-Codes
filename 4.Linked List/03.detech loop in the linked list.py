# detech loop in the linked list 

class Node:
	def __init__(self,data):
		self.data = data
		self.next = next
		
class linked_list:
	# by using the set 
	def detect_loop(head):
		temp = head
		node_set = set()
		
		while temp is not None:
			if temp is node_set:
				return True 
		
		node_set.add(temp)
		temp = temp.next 
		
		return False
	
	
# by using dict 
def detect_loop(head):
    # Initialize a pointer 'temp' at the head of the linked list
    temp = head
    # Create a dictionary to keep track of encountered nodes
    node_dict = {}

    # Traverse the linked list
    while temp is not None:
        # If the node is already in the dictionary, there is a loop
        if temp in node_dict:
            return True
        # Store the current node in the dictionary
        node_dict[temp] = 1
        # Move to the next node
        temp = temp.next

    # If the list is successfully traversed without a loop, return false
    return False
	
	
# -----------------------------------------------------------------------------------------
# optimal approach (using two piointer)(tortoise and hare algorithm )


class Node:
	def __init__(self,data):
		self.data= data 
		self.next =None 
		
class linkedlist:
	def detect_cycle(head):
		slow = head
		fast = head 
		
		while fast is not None or fast.next is not None:
			slow = slow.next
			fast = fast.next.next 
			
			if fast == slow:
				return True 
		return False
