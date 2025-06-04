# *************** Find the Largest Element in an Array *******************

def largest(arr, n):
    # Initialize the first element as the largest
    lar = arr[0]
    for i in range(1, n):
        # Update lar if a larger element is found
        if lar < arr[i]:
            lar = arr[i]
    return lar

# Input from user
arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    arr.append(ele)

print("Input array:", arr)
ans = largest(arr, n)
print("Largest element is:", ans)

# ---------------------------------------------------------------------

# *************** Find Largest Element Using Sorting *******************

def sort_arr(arr):
    # Sort the array and return the last element (largest)
    arr.sort()
    return arr[-1]

# ---------------------------------------------------------------------

# *************** Find the Second Largest Element *******************

def second_largest(arr, n):
    if n < 2:
        return -1  # Not enough elements for second largest

    large = float('-inf')
    second_largest = float('-inf')

    for i in range(n):
        if arr[i] > large:
            second_largest = large
            large = arr[i]
        elif arr[i] > second_largest and arr[i] != large:
            second_largest = arr[i]

    return second_largest

# ---------------------------------------------------------------------

# *************** Find the Second Smallest Element *******************

def second_smallest(arr, n):
    if n < 2:
        return -1  # Not enough elements for second smallest

    small = float('inf')
    second_small = float('inf')

    for i in range(n):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]

    return second_small

# ---------------------------------------------------------------------

# *************** Check if the Array is Sorted *******************

def isSorted(arr, n):
    for i in range(1, n):
        # If any element is smaller than the previous one, it's not sorted
        if arr[i] < arr[i - 1]:
            return False
    return True

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print("Is the array sorted?", "True" if isSorted(arr, n) else "False")
