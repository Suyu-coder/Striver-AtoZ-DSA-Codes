# Two Sum : Check if a pair with given sum exists in Array

#Naive Approach(Brute-force approach): 
def two_sum(n, arr, target):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return "YES"
    return "NO"

# here returning the index 

def two_sum(arr,target):
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]+arr[j] == target:
				return [i,j]
	return []
	
arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))


# Better Approach (Using HJashing)

def two_sum(n, arr, target):
    # Dictionary to store the elements of the array and their indices
    mpp = {}
    
    # Iterate through the array
    for i in range(n):
        num = arr[i]
        more_needed = target - num
        
        # Check if the complement (target - num) exists in the dictionary
        if more_needed in mpp:
            return "YES"
        
        # Store the current element and its index in the dictionary
        mpp[num] = i
    
    # If no such pair is found, return "NO"
    return "NO"


#Optimized Approach(using two-pointer): 

def two_sum(arr,target):
	arr.sort()
	left =0 
	right = len(arr)-1
	while left <=right:
		sum = arr[left] + arr[right]
		if sum == target:
			return "Yes"
		elif sum < target:
			left +=1
		else:
			right-=1
	return "No"
	
arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))

#TC = O(N) + O(NlogN)  # nlogn for sorting 


# returrning the index 
def two_sum(arr, target):
    original_arr = list(arr)
    arr.sort()
    left, right = 0, len(arr) - 1
    
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            index1 = original_arr.index(arr[left])
            index2 = original_arr.index(arr[right]) if arr[left] != arr[right] else original_arr.index(arr[right], index1 + 1)
            return (index1, index2)
        elif sum < target:
            left += 1
        else:
            right -= 1
    
    return (-1, -1)
