# Floor and Ceil of sorted Array 
# Floor --- > (largest no in array <= x)
# ceil ---- > (smallest no in array >= x)

# Floor Array

def findFloor(arr,n,x):
    low  = 0
    high = n-1 
    ans = -1 
    
    while low <= high:
        mid = (low+high)//2

        # may be an answer 
        if arr[mid] <= x:
            ans = arr[mid]

            # look for the smallaer index 
            low = mid +1
        else:
            high = mid - 1
    return ans 


# ceil of array 
# it is si,ilarly like a upper bound

def findCeil(arr,n,x):
    low = 0
    high = n-1 
    ans  =  -1 

    while low <= high:
        mid  = (low+high) // 2

        if arr[mid] >= x:
            ans = arr[mid]

            # look for the smaller index 
            high = mid-1 
        else:
            low = mid +1
    return ans


def getFloorAndCeil(arr, n, x):
    f = findFloor(arr, n, x)
    c = findCeil(arr, n, x)
    return (f, c)


arr = [3, 4, 4, 7, 8, 10]
n = 6
