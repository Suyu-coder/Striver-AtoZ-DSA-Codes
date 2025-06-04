#Longest Consecutive Sequence in an Array

#Brute Force Approach

def linearsearch(a,num):
	n = len(a)
	for i in range(n):
		if a[i] == num:
			return True 
	return False
	
def longestSuccessiveElement(a):
	n = len(a)
	longest = 1
	
	# pick an element and search for its consecutive numbers
	for i in range(n):
		x = a[i]
		cnt = 1
		# search for consecutive numbers using linear search
		while linearsearch(a,x+1):
			x += 1
			cnt += 1
		
		longest = max(longest,cnt)
	return longest 
	
#Better Approach(Using sorting): 

def longestSuccessiveElement(a):
	n = len(a)
	if n == 0:
		return 0
	
	a.sort()
	lastSmaller = float('-inf')
	cnt = 0
	longest = 1
	
	# find longest sequence
	for i in range(n):
		if a[i] - 1 == lastSmaller:
			# a[i] is the next element of the
            # current sequence
			cnt += 1
			lastSmaller = a[i]
		elif a[i] != lastSmaller:
			cnt = 1
			lastSmaller = a[i]
		longest = max(longest,cnt)
	return longest
	
	
#Optimal Approach(Using Set data structure): 

def longestSuccessiveElement(a):
	n = len(a)
	if n == 0:
		return 0
	
	longest = 1
	st = set()
	
	# put all the array elements into set
	for i in range(n):
		st.add(a[i])
	
	# find the longest sequences
	for it in st:
		# if 'it' is a starting numbers
		if it-1 not in st:
			# find the consective number
			cnt = 1
			x = it
			while x+1 in st:
				x+=1
				cnt+=1
			longest = max(longest , cnt)
	return longest
	
	
	
a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)
