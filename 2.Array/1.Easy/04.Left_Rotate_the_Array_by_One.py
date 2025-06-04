# Left Rotate the Array by One 

# ---------------- Better Solution ----------------

def solve(arr, n):
    # Store the first element in a temporary variable
    temp = arr[0]

    # Shift all elements one position to the left
    for i in range(n - 1):
        arr[i] = arr[i + 1]

    # Place the first element at the end of the array
    arr[n - 1] = temp

    # Print the rotated array
    for i in range(n):
        print(arr[i], end=" ")

# Example usage
n = 5
arr = [1, 2, 3, 4, 5]
solve(arr, n)


# ---------------- Optimal Solution ----------------

def left_Rotate_The_Array_By_One(arr, n):
    # Store the first element
    temp = arr[0]

    # Shift all elements one position to the left
    for i in range(1, n):
        arr[i - 1] = arr[i]

    # Place the first element at the end
    arr[n - 1] = temp

    # Return the rotated array
    return arr

# Example usage
arr2 = [10, 20, 30, 40, 50]
n2 = len(arr2)
rotated_arr = left_Rotate_The_Array_By_One(arr2, n2)
print("\nOptimal Left Rotation by One:", rotated_arr)
