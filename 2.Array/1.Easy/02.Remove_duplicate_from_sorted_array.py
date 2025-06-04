# *************** Brute Force Solution *******************

def remove_duplicates_brute(arr):
    # Convert the list to a set to remove duplicates (unordered)
    unique_elements = set(arr)
    # Convert back to list (note: order is not preserved)
    return list(unique_elements)

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    # This will raise an error because the function name is incorrect
    # Corrected function call below
    result = remove_duplicates_brute(arr)
    print("The array after removing duplicate elements is:")
    for num in result:
        print(num, end=" ")

print("\n")

# *************** Optimal Solution *******************

def remove_duplicates_optimal(arr):
    # If the array is empty, return 0
    if not arr:
        return 0

    # Initialize the index for the unique elements
    i = 0

    # Traverse the array starting from the second element
    for j in range(1, len(arr)):
        # If the current element is not equal to the last unique element
        if arr[i] != arr[j]:
            i += 1  # Move the unique index forward
            arr[i] = arr[j]  # Update the position with the new unique element

    # Return the count of unique elements
    return i + 1

# Example usage of optimal solution
arr2 = [1, 1, 2, 2, 2, 3, 3]
k = remove_duplicates_optimal(arr2)
print("The array after removing duplicate elements is:")
for i in range(k):
    print(arr2[i], end=" ")
