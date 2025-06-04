class Node:
	
	def __init__(self,value):
		self.data = value
		self.next = None
		
class LinkedList():
	
	def searching(self,item):
		curr= self.head
		pos = 0
		
		while curr != None:
			if curr.data == item:
				return pos
				
			curr = curr.next 
			pos=pos + 1
			
		return "Not Found"
		
	def __getitem__(self,index):
		curr = self.head 
		pos = 0
		while curr != None :
			if pos == index:
				return curr.data 
				
			curr = curr.next 
			pos = pos + 1
			
		return "Intem not found"
