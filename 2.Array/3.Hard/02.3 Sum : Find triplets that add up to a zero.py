#3 Sum : Find triplets that add up to a zero

#Brute Force Approach

def triplate(n,arr):
	# check all possibel triplates:
	st = set()
	
	for i in range(n):
		for j in range(i+1,n):
			for k in range(j+1,n):
				if arr[i] + arr[j] + arr[k] == 0:
					temp = [arr[i],arr[j],arr[k]]
					temp.sort()
					st.add(tuple(temp))
	
	# store the element in answer
	
	ans = [list (item) for item in st]
	return ans 
	
	
# Better Approach using HAshSet 

def triplate(n,arr):
	st = set()
	
	for i in range(n):
		hashset = set()
		for j in range(i+1,n):
			# calculate the 3rd element
			third = - (arr[i] - arr[j])
			
			# Find the element in the set 
			if third in hashset:
				temp = [arr[i],arr[j],third]
				temp.sort()
				st.add(tuple(temp))
			hashset.add(arr[j])
	
	# store the element in the answer 
	ans = list(st)
	return ans 
	
	
# Optimal Approach Using the two pointer 

def triplate(n,arr):
	ans = []
	arr.sort()
	for i in range(n):
		# Remove duplicates for the current element
		if i != 0 and arr[i] != arr[i-1]:
			continue
		
		j = i+1
		k = n-1
		while j < k:
			total_sum = arr[i] + arr[j] + arr[k]
			
			if total_sum < 0:
				j+=1    # Move the left pointer to the right
			elif total_sum > 0:
				k-=1    # Move the right pointer to the left
			else:
				temp = [arr[i],arr[j],arr[k]]
				ans.append(temp)
				
				# Skip duplicates for the second element
				while j < k and arr[j] == arr[j-1]:
					j += 1
				# Skip duplicates for the third element
				while j < k and arr[k] == arr[k+1]:
					k-=1
	return ans 
