# find the length of loop of linked list 

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
class Linkedlist:
	def find_length(slow, fast):
    
    # count to keep track of 
    # nodes encountered in loop
    cnt = 1
    
    # move fast by one step
    fast = fast.next
    
    # traverse fast till it 
    # reaches back to slow
    while slow != fast:
        
        # at each node increase
        # count by 1 and move fast
        # forward by one step
        
        cnt += 1
        fast = fast.next
    
    # loop terminates when fast reaches
    # slow again and the count is returned
    return cnt
    
# Function to find the length
# of the loop in a linked list
	def length_of_loop(head):
		slow = head
		fast = head
    
		# Step 1: Traverse the list to detect a loop
		while fast is not None and fast.next is not None:
			# Move slow one step
			slow = slow.next
			# Move fast two steps
			fast = fast.next.next
        
			# Step 2: If the slow and fast pointers
			# meet, there is a loop
			if slow == fast:
				# return the number of nodes
				# in the loop
				return find_length(slow, fast)
    
		return 0
		
#----------------------- oR brouete Force ------------------------------------

		
class Linkedlist:	
	def length_of_loop(head):
		visited_nodes = {}
		temp = head
		timer = 0

		while temp is not None:
			if temp in visited_nodes:
				loop_length = timer - visited_nodes[temp]
				return loop_length
			visited_nodes[temp] = timer
			temp = temp.next
			timer += 1

		return 0
		
#Time Complexity: O(N)
#Space Complexity: O(N)

#------------------------------------ Optimal solution -----------------------------------

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None 
	
class linkedlist:
	def find_loop_length(head):
    slow = head
    fast = head

    # Step 1: Traverse the list to detect a loop
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next     
        # Move fast two steps
        fast = fast.next.next  

        # Step 2: If the slow and fast
        # pointers meet, there is a loop
        if slow == fast:
            # Initialize the loop length
            length = 1  
             # Move fast one step
            fast = fast.next 

            # Step 4: Initialize a counter
            # and traverse using the fast pointer
            while slow != fast:
                # Move fast one step
                fast = fast.next  
                # Increment the counter
                length += 1  

            # Step 6: Return the 
            # length of the loop
            return length

    # Step 3: If the fast pointer
    # reaches the end, there is no loop
    return 0 
