#Find the number that appears once, and the other numbers twice

#***************** Brute force **********************************

def getSingleElement(arr):
	# size of the array 
	n = len(arr)
	
	# run the loop for selecting element
	
	for i in range(n):
		num = arr[i] # selected element 
		cnt = 0
		
		# find the occurance using linear search
		for j in range(n):
			if arr[j] == num:
				cnt +=1
				
		# if the occurance is 1 then return the number 
		
		if cnt == 1:
			return num 
	# this line will not execute
	#If the array contain the single element
	return -1 
	
#************************************Better solution **********************
# ********************** using the hashing method *******************

def getSingleElement(arr):
	n = len(arr)
	
	# find the maximum elemenet 
	maxi = max(arr)
	
	# declare the hash array of size maxi + 1
	# and trghen hash the given array 
	
	hash = [0] * (maxi + 1)
	for num in arr : 
		hash[num] +=1
		
	# find the single element and the return the answer 
	for num in arr:
		if hash[num] == 1:
			return num
			
	# this line will not execute
	#If the array contain the single element
	return -1 
	
	
#************************************Better solution **********************
# ********************** using the hashing using map data streacurte *******************

def get_single_element(arr):
	n = len(arr)
	
	# declare the hash map 
	# and hash the given array 
	hashmap = {}
	for num in arr : 
		hashmap[num] = hashmap.get(num,0) + 1
		
	# find thge single element and retuen trhe answer 
	for num , count in hashmap.items():
		if count == 1:
			return num
	# this line will not execute
	#If the array contain the single element
	return -1 
	
	
#************************************Optimal and best solution **********************
# ********************** using XOR method *******************

def getSingleElemet(arr):
	# XOR all teh element
	
	xorr = 0
	for num in arr:
		xorr ^= num
	return xorr
	
# Driver code for all 
def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)

if __name__ == "__main__":
    main()
