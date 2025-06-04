##Find the Majority Element that occurs more than N/2 times
#Brute Force Approach


def majority_element(arr):
	n = len(arr)
	
	for i in range(n):
		cnt = 0
		# Selected element is arr[i]
		for j in range(n):
			# Counting the frequency of arr[i]
			if arr[j] == arr[i]:
				cnt +=1
				
		#check the frequency is greater than n/2
		if cnt > (n//2):
			return arr[i]
	return -1	


arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)



#Better Approach

def majority_element(arr):
    # size of the given array:
    n = len(arr)

    # declaring a dictionary:
    count = {}

    # storing the elements with its occurrence:
    for num in arr:
        count[num] = count.get(num, 0) + 1

    # searching for the majority element:
    for num, freq in count.items():
        if freq > n // 2:
            return num

    return -1
	
# Time Complexity: O(N*logN) + O(N) (hashing + for loop )
# space = O(N)


#Optimal Approach: Moore’s Voting Algorithm:

def majorityElement(arr):
	n = len(arr)
	cnt = 0
	ele = None
	
	# apply the algorithm
	for i in range(n):
		if cnt == 0:
			cnt = 1
			ele = arr[i]
		elif ele == arr[i]:
			cnt +=1
		else:
			cnt -=1
    # Checking if the stored element is the majority element
	cnt1 = 0
	# manually checking the ele is majority or not 
	for i in range(n):
		if arr[i] == ele:
			cnt1+=1
	
	if cnt1>(n/2):
		return ele 
	return -1 
	
arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)
