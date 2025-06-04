# Selection Sort Algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the current index is the minimum
        mini = i
        for j in range(i + 1, n):
            # Find the index of the minimum element in the remaining unsorted array
            if arr[j] < arr[mini]:
                mini = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[mini] = arr[mini], arr[i]

# Example usage of selection sort
arr1 = [12, 43, 24, 64, 332, 67, 5]
selection_sort(arr1)
print("Selection Sort Result:", arr1)
