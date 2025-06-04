#Count Subarray sum Equals K

#Brute Force Approach

def find_all_subarrays_with_given_sum(arr, k):
    n = len(arr)  # size of the given array
    cnt = 0  # Number of subarrays

    for i in range(n):  # starting index i
        for j in range(i, n):  # ending index j

            # calculate the sum of subarray [i...j]
            sum = 0
            for K in range(i, j + 1):
                sum += arr[K]

            # Increase the count if sum == k
            if sum == k:
                cnt += 1

    return cnt	
			
			
#Better Approach

def findAllSubarraysWithGivenSum(arr,k):
	n = len(arr)
	cnt = 0
	
	for i in range(n):
		subarray_sum = 0
		for j in range(i,n):
			# calculate the sum of subarray [i...j]
			subarray_sum += arr[j]
			
			# Increase the count if sum == k.
		if subarray_sum == k:
			cnt += 1
	return cnt		

#Optimal Approach
#In this approach, we are going to use the concept of the prefix sum to solve this problem. Here, the prefix sum of a subarray ending at index i simply means the sum of all the elements of that subarray.


from collections import defaultdict

def findAllSubarraysWithGivenSum(arr,k):
	n = len(arr)
	mpp = defaultdict(int)
	preSum = 0
	cnt = 0
	
	mpp[0] = 1  # setting 0 to the map
	for i in range(n):
		
		# add the current sum to prefix element 
		preSum += arr[i]
		
		# calculate x-k
		remove = preSum - k
		
		# add teh numbert of subarray to be removed 
		
		cnt += mpp[remove]
		
		# update the count of prefix sum 
		# in the map 
		
		mpp[preSum] += 1
		
	return cnt 
