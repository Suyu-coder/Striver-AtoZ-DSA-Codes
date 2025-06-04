# Single element in Sorted Array

	#Naive Approach (Brute force 1): 
def findPeakElement(arr):
	n = len(arr)
	
	for i in range(n):
		if (i == 0 or arr[i-1] < arr[i]) and (i == n-1 or arr[i+1] > arr[i]):
			return i
			
	return -1
	
	
# Optimal Approach(Using Binary Search): 




def findPeakElement(arr: [int]) -> int:
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1
		
	# here trimming down the array 
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the peak:
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid

        # If we are in the left:
        if arr[mid] > arr[mid - 1]:
            low = mid + 1

        # If we are in the right:
        # Or, arr[mid] is a common point:
        else:
            high = mid - 1

    # Dummy return statement
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = findPeakElement(arr)
print("The peak is at index:", ans)
