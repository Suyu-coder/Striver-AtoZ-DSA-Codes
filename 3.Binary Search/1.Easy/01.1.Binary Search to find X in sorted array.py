# --------------------------- Iterative Implementation ---------------------------

def binarySearchIterative(nums, target):
    low = 0
    high = len(nums) - 1

    # Loop until the search space is exhausted
    while low <= high:
        mid = (low + high) // 2  # Corrected syntax error

        if nums[mid] == target:
            return mid  # Target found
        elif target > nums[mid]:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found


# --------------------------- Recursive Implementation ---------------------------

def binarySearchRecursive(nums, low, high, target):
    if low > high:
        return -1  # Base case: target not found

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid  # Target found
    elif target > nums[mid]:
        return binarySearchRecursive(nums, mid + 1, high, target)  # Search right half
    else:
        return binarySearchRecursive(nums, low, mid - 1, target)  # Search left half


# Wrapper function for recursive search
def search(nums, target):
    return binarySearchRecursive(nums, 0, len(nums) - 1, target)


# --------------------------- Test the Functions ---------------------------

if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13]
    target = 7

    print("Iterative Search Result:", binarySearchIterative(nums, target))
    print("Recursive Search Result:", search(nums, target))
