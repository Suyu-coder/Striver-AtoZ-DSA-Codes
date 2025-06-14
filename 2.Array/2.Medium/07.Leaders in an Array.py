# Leaders in an Array

#Brute Force Approach

def printLeadersBruteForce(arr,n):
	ans = []
	
	for i in range(n):
		leader = True
		
		# Checking whether arr[i] is greater than all 
        # the elements in its right side
		for j in range(i+1,n):
			if arr[j] > arr[i]:
				# If any element found is greater than current leader,
                # curr element is not the leader.
				leader = False
				break
		# push the all teh elementi in ans array 
		if leader:
			ans.append(arr[i])
	return ans 
	
	
#Optimal Approach

def printLeaders(arr,n):
	ans  = []
	# Last element of an array is always a leader,
    # push into ans array.
	
	max_ele = arr[n-1]
	ans.append(arr[n-1])
	# Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
	
	for i in range (n-2,-1,-1): # running loop end to start 
		if arr[i] > max_ele:
			ans.append(arr[i])
			max_ele = arr[i]
	
	return ans 
	

# Main function
if __name__ == '__main__':
    # Array Initialization
    n = 6
    arr = [10, 22, 12, 3, 0, 6]

    ans = printLeadersBruteForce(arr, n)

    for i in range(len(ans)):
        print(ans[i], end=" ")

    print()
