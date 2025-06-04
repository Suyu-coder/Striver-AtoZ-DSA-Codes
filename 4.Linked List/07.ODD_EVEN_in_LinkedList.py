# Need to watch do again 

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
	def segrate_odd_even(head):
		arr = []
		temp = head 
		while temp is not None or temp.next is not None:
			arr.append(temp.data)
			
