# Minimum in Rotated Sorted Array

#Naive Approach (Brute force): 

import sys
def findMin(arr):
    n = len(arr)
    mini = sys.maxSize

    for i in range(n):
        # always keep the minium 
        mini = mini(mini , arr[i])
    return mini 

# Optimal Approach(Using Binary Search): 

def findMin(arr):
    low = 0
    high = len(arr) -1 
    ans = sys.maxSize

    while low <= high:
        mid = (low+high) //2

        # if the left part is sorted
        if arr[low] <= arr[mid]:
            ans = min(ans,arr[low])
            # elemanate the left half 
            low = mid +1
        # if the left part is sorted
        else:
            ans = min(ans,arr[mid])
            ## eliminate right half
            high = mid - 1
    return ans 

# Further optimized (Its not necessary to do )
# If want to learn then you can do 

def findMin(arr):
    low = 0
    high = len(arr) -1 
    ans = sys.maxSize

    while low <= high:
        mid = (low+high) //2

        # search space is already sorted
        # then arr[low] will always be
        # the minimum in that search space:
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break

        # if the left part is sorted
        if arr[low] <= arr[mid]:
            ans = min(ans,arr[low])
            # elemanate the left half 
            low = mid +1
        # if the left part is sorted
        else:
            ans = min(ans,arr[mid])
            ## eliminate right half
            high = mid - 1
    return ans 




if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findMin(arr)
    print("The minimum element is:", ans)
