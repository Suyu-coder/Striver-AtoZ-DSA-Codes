# Stock Buy And Sell

#Brute Force Approach

def maxProfit(arr):
	maxPro = 0
	n = len(arr)
	
	for i in range(n):
		for j in range (i+1, n):
			if arr[j] > arr[i]:
				maxPro = max(arr[j]-arr[i] , maxPro)
				
	return maxPro
	
	
# Optimal Approach

def maxProfit(arr):
	maxPro = 0
	minPrice = float('inf')
	
	for i in range(len(arr)):
		minPrice = min ( minPrice , arr[i] )
		maxPro = max (maxPro , arr[i] - minPrice)
	return maxPro
	
if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    maxPro = maxProfit(arr)
    print("Max profit is: ", maxPro)
