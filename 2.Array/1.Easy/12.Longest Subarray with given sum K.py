#Naive Approach (Brute-force approach):  
 
def getlongestSubarray(arr,k):
	n = len(arr)
	length = 0
	
	for i in range(n):  # starting index
		for j in range(i,n): #ending index 
			
			# add all teh elements of 
			# subarray = arr[i...j]:
			
			s = 0
			for num in range(i,j+1):
				s+=arr[num]
				
			if s == k:
				length = max(length , j-i+1)
	return length
	

#Optimizing the Naive Approach (Using two loops):  

def getlongestSubarray(arr,k):
	n = len(arr)
	length = 0
	
	for i in range(n):  # starting index
		for j in range(i,n): #ending index 
			
			# add all teh elements of 
			# subarray = arr[i...j]:
			
			s +=a[j]
			
			if s == k:
				lenght = max(length , j-i+1)
	return length 
	
# Optimal Approach (Using 2 pointers): 

def getlongestSubarray(arr,k):
	n = len(a)
	left , right  = 0,0
	sum = a[0]          #Initialize the current sum
	maxLen = 0       # Initialize the maximum length of subarray
	
	while right<n:
		# If sum > k, reduce the subarray from left until sum becomes less or equal to k
		while left <= right and sum > k:
			sum -=a[left]     ## Subtract the element at the left pointer from the current sum
			left += 1     # Move the left pointer to the right
			
		if sum == k:
			maxLen = max(maxLen , right -left +1)
		
		right +=1
		if right < n:
			sum +=a[right]
			
	return maxLen
