class Node:
	def __init__(self,value):
		self.data = value 
		self.next = None 

class Linkedlist:

	def __init__(self):
		
		#to create a Empty Linked list 
		self.head = None
		# No of nodes in the LL 
		self.n = 0
		
	# printting of the length of the linked list 
	
	def __len__(self):
		return self.n 
		
	# insert the node from Head
	
	def insert_head(self,value):
		# new Node creattion 
		new_node = Node(value)
		# create a connection 
		new_node.next = self.head 
		#rewassign head 
		self.head= new_node 
		# increments by 1
		self.n = self.n+1
		
	def traverse(self):
		curr = self.head
		while curr != None:
			print(curr.data)
			curr = curr.next
			
	# Another way of printing 
	def __str__(self):
		curr = self.head
		result = ''
		while curr != None:
			result = result + str(curr.data) + '->'
		return result[:-2]
		
	
	def append(self,value):
		new_node = Node(value)
		
		if self.head == None:
			self.head = new_node
			self.n = self.n + 1
			
		return 
		
		curr = curr.head
		while curr.next != None:
			curr = curr.next
		
		# You are at the last node 
		curr.next = new_node
		self.n = self.n + 1
		
	def insert_after(self,after,value):
		new_node = Node(value)
		
		curr = self.head
		
		while curr != None:
			if curr.data == after:
				break 
				
			curr = curr.next 
		 # case 1 break -> then item mil gaya --> curr is Not None
			
			if curr != None:
				new_node.next = curr.next 
				curr.next = new_node
				self.n = self.n + 1
		# if curr is None then run else condition 
			else:
				return 'Item Not Found'
