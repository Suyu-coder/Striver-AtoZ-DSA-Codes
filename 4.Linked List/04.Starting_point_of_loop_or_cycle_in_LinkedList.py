
# starting point of loinked list 

class Node:
	def __init__(self,data):
		self.data = data 
		self.next = None

class LinkedList:
	def detect_loop(head):
    # Use temp to traverse the linked list
    temp = head
    
    # Dictionary to store all visited nodes
    node_map = {}
    
    # Traverse the list using temp
    while temp is not None:
        # Check if temp has been encountered again
        if temp in node_map:
            # A loop is detected, hence return temp
            return temp
        
        # Store temp as visited
        node_map[temp] = True
        
        # Iterate through the list
        temp = temp.next

    # If no loop is detected, return None
    return None
		
		
#--------------------------------------------------------------------
# optimal opproach (using two piointer)(tortoise and hare algorithm )

class Node:
	def __init__(self,data):
		self.data = data 
		self.next = None 
		
class Linkedlist:
	def first_node(head):
    # Initialize a slow and fast
    # pointers to the head of the list
    slow = head
    fast = head

    # Phase 1: Detect the loop
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next

        # Move fast two steps
        fast = fast.next.next

        # If slow and fast meet,
        # a loop is detected
        if slow == fast:
            # Reset the slow pointer
            # to the head of the list
            slow = head

            # Phase 2: Find the first
            # node of the loop
            while slow != fast:
                # Move slow and fast one
                # step at a time
                slow = slow.next
                fast = fast.next

                # When slow and fast meet again,
                # it's the first node of the loop
            return slow

    # If no loop is found, return None
    return None
						
		
# --------------------------- Node Definition ---------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# --------------------------- Brute Force Approach (Using Hashing) ---------------------------

class LinkedList:
    @staticmethod
    def detect_loop(head):
        # Use a dictionary to store visited nodes
        visited = {}

        current = head
        while current is not None:
            # If node is already visited, loop detected
            if current in visited:
                return current  # Starting point of the loop

            # Mark current node as visited
            visited[current] = True
            current = current.next

        # No loop found
        return None


# --------------------------- Optimal Approach (Floyd’s Cycle Detection) ---------------------------

class LinkedListOptimal:
    @staticmethod
    def first_node(head):
        slow = head
        fast = head

        # Phase 1: Detect if a loop exists
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Loop detected
            if slow == fast:
                # Phase 2: Find the starting node of the loop
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # Starting point of the loop

        # No loop found
        return None
