# Search element in rotated sorted array

#Here we are using linear search O(n)
def search(arr,n,k):
    for i in range(n):
        if arr[i] == k:
            return True
    return False


# Optimised way 
def search(arr,n,k):
    low = 0
    high  = n-1 
    while low <= high:
        mid = (low + high)//2

        # if mid point is a target then 
        if arr[mid] == k:
            return True

        # edge case 

        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high += 1
            continue

        # Here we are identify which parte is sorted the then seach and elemenate 
        # if left part is sorted 
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element is exist
                high = mid-1 
            else:
                # element is does not exist
                low = mid + 1
        # if right part is sorted 
        else:
            if arr[mid] <= k and k <= arr[high]:
                # element is exist 
                low = mid + 1
            else:
                high = mid - 1
    return False 

if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)
