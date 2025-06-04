# Find the repeating and missing numbers
# Naive Approach (Brute force): 

def find_missing_and_repaeating_number(a):
	n = len(a)
	reapeating = -1
	missing = -1
	
	# find the reapeating and missing number 
	for i in range(1,n+1):
		# count the occurance
		
		cnt = a.count(i)
		if cnt == 2:
			reapeating = i
		elif cnt == 0:
			missing = i
			
		if reapeating != -1 and missing != -1 :
			break 
	return reapeating , missing


# anotehr Native fiunction answer 
def find_missing_repeating_numbers(a):
    n = len(a)  # size of the array
    repeating = -1
    missing = -1

    # Find the repeating and missing number:
    for i in range(1, n + 1):
        # Count the occurrences:
        cnt = 0
        for j in range(n):
            if a[j] == i:
                cnt += 1

        if cnt == 2:
            repeating = i
        elif cnt == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break

    return [repeating, missing]
	

# Better Approach (Using Hashing): 

def find_missing_and_repaeating_number(a):
	n = len(a)
	hash_array = [0] * (n+1) 
	
	# update the hash array
	for num in a:
		hash_array[num] +=1
		
	# Find the repeating and missing number:
	repeating = -1
	missing = -1
	for i in range(1,n+1):
		if hash_array[i] == 2:
			reapeating = i
		elif hash_array[i] == 0:
			missing = i
		
		if reapeating != -1 and missing != -1:
			break
			
	return repeating,missing
	 
# Optimal Approach 1 (Using Maths): 

def find_missing_and_repaeating_number(a):
	n = len(a)
	
	#find Sn and S2n
	sn = (n*(n+1))//2
	s2n = (n*(n+1) * (2*n+1)) // 6
	
	# calculate S and S2
	s = sum(a)
	s2 = sum(x*x for x in a)
	
	# s-sn = x-y
	val1 = s-sn
	
	#s2-s2n = x^2 - y^2
	val2 = s2-s2n 
	
	#find x+y = (x^2 - y^2)/(x-y)
	val2 = val2 // val1
	
	# find x and y : X = ((X + Y) + (X - Y)) / 2 and Y = X - (X - Y),
    # Here, X - Y = val1 and X + Y = val2:
	x = (val1+val2)//2
	y = x-val1
	
	return int(x),int(y)
	
	
	
	
def main():
    a = [3, 1, 2, 5, 4, 6, 7, 5]
    repeating, missing = find_missing_repeating_numbers(a)
    print(f"The repeating and missing numbers are: {{{repeating}, {missing}}}")

if __name__ == "__main__":
    main()
