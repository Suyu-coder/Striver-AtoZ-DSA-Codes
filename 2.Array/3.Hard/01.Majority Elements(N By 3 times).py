#Majority Elements(&gt;N/3 times) | Find the elements that appears more than N/3 times in the array 

#Brute Force Approach

def majority_element(lst):
	n = len(lst) 
	ls = [] # list of the answer 
	
	for i in range(n):
		# selected element is lst[i]:
        # Checking if lst[i] is not already
        # a part of the answer:
		
		if len(ls) == 0 or ls[0] != lst[i]:
			cnt = 0
			for j in range(n):
				#counting the frequency of lst[i]
				if lst[j] == lst[i]:
					cnt +=1
				
			# check the frequency ios greater than n/3
			if cnt > (n//3):
				ls.append(lst[i])
				
		if len(ls) == 2:
			break
			
	return ls 

#Better Approach (Using Hashing): 

def majority_element(nums):
	n = len(nums)
	result = []
	count_map = {}
	
	# minimum occurance for a majority element 
	mini = n // 3 + 1
	
	# counting the occurance of each element 
	for num in nums:
		count_map[nums] = count_map.get(num,0) + 1
		
		#checking if num is majority element
		
		if count_map[nums] == mini:
			result.append(num)
		if len(result) == 2:
			break
	return result 


#Optimal Approach (Extended Boyer Moore’s Voting Algorithm): 

def majority_element(nums):
	n = len(nums)
	cnt1,cnt2 = 0,0
	el1,el2 = None,None
	
	# Applying the extended Boyer-Moore Voting Algorithm
	for num in nums:
		if cnt1 == 0 and num != el2:
			el1 ,cnt1 = num , 1
		elif cnt2 == 0 and num != el1:
			el2,cnt2 = num,1
		elif num == el1:
			cnt1+=1
		elif num == el2:
			cnt2 += 1
		else:
			cnt1 -= 1
			cnt2 -= 1
			
    # Manually check if the stored elements in el1 and el2 are the majority elements
	cnt1 , cnt2 = 0,0
	for num in nums:
		if num == el1:
			cnt1+=1
		if num == el2:
			cnt2+=1
			
	result = []
	mini = n // 3 + 1
	if cnt1 >= mini:
		result.append(el1)
	if cnt2 >= mini:
		result.append(el2)
	
	return result
	

if __name__ == "__main__":
    arr = [11, 33, 33, 11, 33, 11]
    ans = majority_element(arr)
    print("The majority elements are:", ans)
