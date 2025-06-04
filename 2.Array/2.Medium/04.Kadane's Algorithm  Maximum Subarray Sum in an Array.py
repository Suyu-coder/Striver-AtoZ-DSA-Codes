# Kadane's Algorithm  Maximum Subarray Sum in an Array

# Brute Force Approach

def maxSubarraySum(arr,n):
	maxi = -sys.maxsize - 1 
	
	for i in range(n):
		for j in range(i,n):
			summ = 0
			
			# add all teh elememnt of subnarray
			for k in range(i, j+1):
				summ += arr[k]
			maxi = max(maxi,summ)
			
	return maxi
	
# Better Approach

def maxSubarraySum(arr,n):
	maxi = -sys.maxsize - 1
	
	for i in range(n):
		sum = 0
		for j in range (i,n):
			#current subarray = arr[i.....j]
			
			# add the current element arr[j]
			# to the sum i.e sum of arr[i...j-1]
			
			sum += arr[j]
			maxi = max(maxi,sum)
	return maxi

# Optimal Approach
# Kadane Algorithm
	
import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    current_sum = 0

    for i in range(n):
        # If current_sum < 0: discard the sum calculated
        if current_sum < 0:
            current_sum = 0

        current_sum += arr[i]
        if current_sum > maxi:
            maxi = current_sum

    # To consider the sum of the empty subarray
    # uncomment the following check:
    # if maxi < 0: maxi = 0

    return maxi	
	
#Followup Approach
# Kadane Algorithm return tha array 
# here using the silding window 

def maxSubarraySum(arr,n):
	maxi = -sys.maxsize - 1
	sum = 0
	
	start = 0
	ansStart , ansEnd = -1,-1
	
	for i in range(n):
		if sum == 0 :
			start = i # starting inmdex
		
		sum += arr[i]
		
		if sum > maxi:
			maxi = sum
			
			ansStart = start
			ansEnd = i
		# If sum < 0: discard the sum calculated
		if sum < 0:
			sum = 0
	return maxi 
		
