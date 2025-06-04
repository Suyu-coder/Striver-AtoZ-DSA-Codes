# Insertion Sort Algorithm
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Place the key at its correct position
        arr[j + 1] = key

# Example usage of insertion sort
arr3 = [23, 42, 13, 56, 75, 33]
insertion_sort(arr3)
print("Insertion Sort Result:", arr3)
