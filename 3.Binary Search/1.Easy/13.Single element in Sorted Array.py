# Single element in Sorted Array

#Naive Approach (Brute force): 

def smallestDivisor(arr,limit):
	n = len(arr)
	maxi = max(arr)

	for d in range(1,maxi+1):
		sum = 0
		for i in range(n):
			sum += math.celi(arr[i]/d)
		if sum <= limit:
			return d
	
	return -1 
# Optimal Approach(Using Binary Search): 

import math

def sumByD(arr, div):
    n = len(arr)  # size of array
    # Find the summation of division values
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum

def smallestDivisor(arr, limit):
    n = len(arr)
    if n > limit:
        return -1
    low = 1
    high = max(arr)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        if sumByD(arr, mid) <= limit:
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)
