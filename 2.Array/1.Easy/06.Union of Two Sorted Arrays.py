# Union of Two Sorted Arrays
#************************* Brote force **********************************

def find_union(arr1,arr2):
	s = set()
	union = []
	
	for num in arr1:
		s.add(num)
		
	for num in arr2:
		s.add(num)
		
	for num in s:
		union.append(num)
		
	return union 


# ***************************** Optimized solution ***********************
# *************************** Using two pointer **************************

def find_union(arr1,arr2):
	i,j = 0,0
	union = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i]<= arr2[j]:
			if len(union) == 0 or union[-1] != arr1[i]:
				union.append(arr1[i])
			i += 1
		else:
			if len(union) == 0 or union[-1] != arr2[j]:
				union.append(arr2[j])
			j += 1
			
	# if any elemet left in arr1
	while i < len(arr1):
		if union[-1] != arr1[i]:
			union.append(arr1[i])
		i += 1
	
	# if any element left in arr2
	while j < len(len(arr2)):
		if union[-1] != arr2[j]:
			union.append(arr2[j])
		j += 1
		
	return union 
