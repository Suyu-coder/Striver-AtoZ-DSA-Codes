# Search Insert Position similarly like lower bound in binary search

#Brute Force Approach

def SearchInsertPosition(arr,n,x):
    for i in range(n):
        if arr[i] >= x:
            # lower bound found 
            return i
    return n 

# Optimal Approach (Using Binary Search): 

def SearchInsertPosition(arr,n,x):
    low = 0
    high = n-1
    ans = n

    while low <= high:
        mid = (low+high) // 2

        # may be an answer 
        if arr[mid] >= x:
            ans = mid 
            # looking for smaller index 
            high = mid-1 
        else:
            low = mid +1
    return ans 


if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = SearchInsertPosition(arr, n, x)
    print("The lower bound is the index:", ind)
