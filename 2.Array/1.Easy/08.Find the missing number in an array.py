#Find the missing number in an array
# ********************************* Brute force **************************

def missing_number(a,N):
	# outer loop that runs from 1 to N
	
	for i in range(1,N+1):
		# flag variable is check the element is exit or not 
		flag = 0
		
		# search element using linear search 
		for j in range(len(a)):
			if a[j] == i:
				# i is present in the array 
				flag = 1
				break
				
		# check the element is missing 
		
	if flag ==0:
		return i
		
#**************** Better approach using Hash ******************************

def missing_number(a,N):
	hash  = [0] * (N+1) # hash array 
	
	# sorting the frequencies
	for i in range (N-1):
		hash[a[i]] +=1 
		# checking the frequencies for numbers 1 to N 
		
		for i in range (1,N+1):
			if hash[i] == 0:
				return i
				
		# the following line will never execute 
		# it is just to avoid varning 
		
	return -1
	
#*************************** Optimal Number ****************************
# ********************* Using sum method *************************

def missing_number(a,N):
	# summation of first N numbers 
	sum = (N * (N+1))//2
	
	# summation of arr array
	s2 = sum (a)
	
	missingNum = sum - s2
	return missingNum
	
#********************** using XOR method **************************

def missing_number(a, N):
    xor1 = 0
    xor2 = 0

    for i in range(N - 1):
        xor2 = xor2 ^ a[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number
	
	
#***********************************************************************
def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)


if __name__ == '__main__':
    main()
