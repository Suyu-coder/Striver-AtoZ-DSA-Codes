# first and last occurance of array 

def firstOccurance(arr,n,k):
    low = 0 
    high =  n-1 
    first = -1 

    while low <= high:
        mid = (low + high) //2

        if arr[mid] == k:
            first = mid

            # looking for small index 
            high = mid-1
        elif arr[mid] < k:
            low = mid + 1   # look on the right
        else: 
            high = mid - 1  # look on the left 

    return first 


def last_Occurance(arr,n,k):
    low = 0 
    high = n-1 
    last = -1 

    while low <= high:
        mid =  (low+high) // 2

        if arr[mid] == k:
            last = mid 

            # looking for large index
            low = mid + 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid -1
    return last 


def firstAndLastPosition(arr, n, k):
    first = firstOccurance(arr, n, k)
    if first == -1:
        return (-1, -1)
    last = last_Occurance(arr, n, k)
    return (first, last)

def count(arr: [int], n: int, x: int) -> int:
    first, last = firstAndLastPosition(arr, n, x)
    if first == -1:
        return 0
    return last - first + 1
