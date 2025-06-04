# Single element in Sorted Array

#Naive Approach (Brute force 1): 
def singleNonduplicate(arr):
	n = len(arr)
	if n == 1:
		return arr[0]
		
	for i in range(n):
		# Check for first index
		if i == 0:
			if arr[i] != arr[i+1]:
				return arr[i]
		# Check for last index
		elif i == n-1:
			if arr[i] != arr[i-1]:
				return arr[i]
		# Check for middle index
		else:
			if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
				return arr[i]
	return -1 

#Naive Approach (Brute force 2): 

def singleNonduplicate(arr):
	n = len(arr)
	ans = 0
	for i in range (n):
		ans = ans ^ arr[i]
	return ans

# Optimal Approach(Using Binary Search): 




def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]
		
	# here trimminig down the array start the 1 indeext and end at second last index 
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the single element:
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        # We are in the left:
		# if the mid present at odd index then it not similar to previous Or
		# if the mid present at even index then it not similar to next
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            # Eliminate the left half:
            low = mid + 1
		
        # We are in the right:
        else:
            # Eliminate the right half:
            high = mid - 1

    # Dummy return statement:
    return -1



arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)
