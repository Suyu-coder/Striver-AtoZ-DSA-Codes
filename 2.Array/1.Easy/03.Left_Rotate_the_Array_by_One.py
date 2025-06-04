# Left Rotate the Array by k Places
# ****************** Brute Force Solution ******************

def left_rotate_the_array_by_k(arr, n, k):
    # Handle cases where k is greater than n
    k = k % n

    # Step 1: Store the first k elements in a temporary array
    temp = arr[:k]

    # Step 2: Shift the remaining elements to the left
    for i in range(n - k):
        arr[i] = arr[i + k]

    # Step 3: Copy the stored elements to the end of the array
    for i in range(k):
        arr[n - k + i] = temp[i]

    return arr

# Example usage
arr1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 2
print("Brute Force Left Rotation:", left_rotate_the_array_by_k(arr1, len(arr1), k1))

		
#***************************Optimal solution ********************

# ****************** Optimal Solution Using Reversal Algorithm ******************

def rotate(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is greater than the array length

    # Step 1: Reverse the entire array
    reverse(nums, 0, n - 1)

    # Step 2: Reverse the first n-k elements to restore their original order
    reverse(nums, 0, n - k - 1)

    # Step 3: Reverse the last k elements to restore their original order
    reverse(nums, n - k, n - 1)

# Helper function to reverse elements in-place between indices left and right
def reverse(nums, left, right):
    while left < right:
        # Swap the elements at the left and right indices
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Example usage
arr2 = [1, 2, 3, 4, 5, 6, 7]
k2 = 2
rotate(arr2, k2)
print("Optimal Left Rotation:", arr2)
