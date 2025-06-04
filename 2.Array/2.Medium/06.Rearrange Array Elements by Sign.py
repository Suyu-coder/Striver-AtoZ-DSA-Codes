#Rearrange Array Elements by Sign

#Brute Force Method
def rearrange_by_sign(A):
	pos = []
	neg = []
	
	# Segregate the array into positives and negatives.
	for i in range(len(A)):
		if A[i] > 0:
			pos.append(A[i])
		else:
			neg.append(A[i])
	# Positives on even indices, negatives on odd.
	
	for i in range(len(pos)):
		A[2*i] = pos[i]
	for i in range(len(neg)):
		A[2*i + 1] = neg[i]
	
	return A
	
#Optimal Method

def Rearrange_by_sign(A):
	n = len(A)
	
	# Define array for storing the ans separately.
	ans = [0] *n
	
	# positive elements start from 0 and negative from 1.
	posIndex , negIndex = 0,1
	
	for i in range(n):
		# Fill negative elements in odd indices and inc by 2.
		if A[i] < 0:
			ans[negIndex] = A[i]
			negIndex += 2
			
		# Fill positive elements in even indices and inc by 2.
		else:
			ans[posIndex] = A[i]
			posIndex += 2
	return ans 


A = [1, 2, -4, -5]
ans = rearrange_by_sign(A)

for i in range(len(ans)):
    print(ans[i], end=" ") 


# Output: 1,-4, 2, -5
