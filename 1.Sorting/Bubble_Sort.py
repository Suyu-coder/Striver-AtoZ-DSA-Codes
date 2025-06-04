# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Traverse the array from 0 to n-i-1
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, then the array is already sorted
        if not swapped:
            break

# Example usage of bubble sort
arr2 = [23, 42, 13, 56, 75, 33]
bubble_sort(arr2)
print("Bubble Sort Result:", arr2)
