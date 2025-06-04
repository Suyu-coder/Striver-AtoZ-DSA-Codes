
class Node:
	
	def __init__(self,Value):
		self.data = Value 
		self.next = None
		
class Linkedlist:
	
	def __init__(self):
		self.head = None
		self.n = 0
		
	# clear The Linked List 
	
	def clear(self):
		self.head = None 
		self.n = 0
		
	# delete a head from linked list  (Deleting from the head)
	
	def delete_head(self):
		
		if self.head == None:
			return 'Empty linked list'
			
		# If linked list is not empty
		
		self.head = self.head.next 
		self.n = self.n - 1
		
	# deleteing from the talil in linked list  
	
	def pop(self):
		if self.head == None :
			#empty 
			return "Empty linked list "
		
		curr = self.head 
		
		# linked list mai 1 item hoga to 
		if curr.next == None :
			# agar sirf headf ho hoga means 1 item hoga to 
			
			return self.delete_head()
			
		# agar uparka dono bhi nahi huaa to loop run hoga 	
		while curr.next.next != None :
			curr = curr.next
		
		curr.next = None 
		self.n = self.n - 1
	
	# delete a specific item in linked list 
	
	def Remove(self,value):
		
		# check the head is none or not
		if self.head == None:
			return 'Empty linked list'
			
		# if you want to remove the head then (means only 1 item present in Linkedlist then )
		if self.head.data == value:
			return self.delete_head()
			
		# if both condition not run then start from here
			
		curr = self.head
		
		while curr.next != None :
			if curr.next.data == value:
				break 
			
			curr = curr.next
			
		#(here gettin a two condition )
		#1. Item nahi mila
		if curr.next == None:
			return "Not Found"
		#2. Item mil gaya 
		else:
			curr.next = curr.next.next
			self.n = self.n -1
