#Count the number of subarrays with given xor K

#Naive Approach (Brute-force): 

def subarrays_with_xor_k(a, k):
	n = len(a)
	cnt = 0 
	
	# Generating a subarray 
	for i in range(n):
		for j in range(i,n):
			
			# calculate the XOR of all elkement
			xorr = 0
			for k in range(i,j+1):
				xorr = xorr ^ a[k]
				
			# check the XOR and count
			if xorr == k:
				cnt += 1
	
	return cnt 
	
# Better Approach

def subarrays_with_xor_k(a,k):
	n = len(a)
	cnt = 0
	
	# Generating a subarray 
	for i in range(n):
		for j in range(i,n):
			
			# calculate XOR of all elements:
			xorr = xorr ^ a[j]
		
		#check the XOR and count
		if xorr == k:
			cnt+=1
	return cnt 
			
# Optimal Approach(Using Hashing): 

def subarrays_with_xor_k(a,k):
	n = len(a)
	xr = 0
	sum_index_map = {}
	sum_index_map[xr] = 1 # setting the value of 0
	cnt = 0
	
	for i in range(n):
		# prefix XOR till index i
		xr ^= a[i]
		
		# by formula x= xr^k
		x = xr ^ k
		
		#add the occurance of xr^k to the count
		cnt += sum_index_map.get(x,0)
		
		# insert the prefix xor till index i into dictory 
		sum_index_map[xr] = sum_index_map.get(xr,0) + 1
		
	return cnt 
	
	
if __name__ == "__main__":
    arr = [4, 2, 2, 6, 4]
    k = 6
    ans = subarrays_with_xor_k(arr, k)
    print("The number of subarrays with XOR k is:", ans)
