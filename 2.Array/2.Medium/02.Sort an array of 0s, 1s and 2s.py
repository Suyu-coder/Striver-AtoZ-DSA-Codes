# Sort an array of 0s, 1s and 2s 
# Brute Force Approach and better approach 

def sortArray(arr):
	cnt0 = 0
	cnt1 = 0
	cnt2 = 0
	
	for num in arr:
		if num == 0:
			cnt0 += 1
		elif num == 1:
			cnt1 += 1
		else:
			cnt2 += 1
	
	for i in range(cnt0):
		arr[i] = 0
	
	for i in range(cnt0, cnt0 + cnt1):
		arr[i] = 1
		
	for i in range(cnt0+cnt1 , len(arr)):
		arr[i] = 2
		
n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)

#Optimal Approach
#Dutch National flag algorithm. 

def sortArray(arr):
	low = 0
	mid = 0
	high = len(arr)-1
	
	while mid <= high:
		if arr[mid] == 0:
			arr[low],arr[mid] = arr[mid],arr[low]
			low += 1
			mid += 1
		elif arr[mid] == 1:
			mid += 1
		else:
			arr[mid],arr[high] = arr[high],arr[mid]
			high -= 1

n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
