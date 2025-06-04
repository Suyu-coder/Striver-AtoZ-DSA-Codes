# Intersection Of Two Sorted Arrays 
# ********************************* Brute force **************************

def find_array_intersection(arr,n,brr,m):
	ans = 0
	vis = []
	for i in range(n):
		for j in range(m):
			if arr[i] == brr[j] and vis[j] == 0:
				ans.append(arr[i])
				vis[j] = 1
				break
			if brr[j] > arr[i]: break
	return ans 
	
	
#********************** Optimal Rule *****************
# ************* using two pointer ********************
def find_array_intersection(arr,n,brr,m):
	i,j = 0,0
	ans = []
	while(i<n and j<m):
		if arr[i]<brr[j]:
			i+=1
		elif brr[j]<arr[i]:
			j+=1
		else:
			ans.append(arr[i])
			i += 1
			j += 1
			
	return ans
	
