# Merge Overlapping Sub-intervals

#Naive Approach (Brute-force): 

def merge_overlapping_interval(arr):
	n = len(arr)
	
	arr.sort()
	ans = []
	
	for i in range (n):
		start = arr[i][0]
		end = arr[i][1]
		
		# skip all the mergered interval 
		if ans and end <= ans[-1][1]:
			continue
		
		# check the rest of the intervals
		for j in range(i+1,n):
			if arr[j][0] <= end :
				end = max(end,arr[j][1])
			else:
				break
		
		ans.append([start,end])
	return ans 
	
#Optimal Approach: 

def merge_overlapping_interval(arr):
	n = len(arr)
	arr.sort()
	
	ans = []
	
	for i in range(n):
		# if the current interval does not lie in the last ingerval 
		if not ans or arr[i][0] > ans[-1][1]:
			ans.append(arr[i])
			
		# if the current interval lies in the last interval
		else:
			ans [-1][1] = max(ans[-1][1], arr[i][1])
	return ans 
	
if __name__ == '__main__':
    arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
    ans = merge_overlapping_interval(arr)
    print("The merged intervals are:")
    for it in ans:
        print(f"[{it[0]}, {it[1]}]", end=" ")
    print()
