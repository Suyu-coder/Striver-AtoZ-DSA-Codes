#Move all Zeros to the end of the array

# --------------------------- Brute Force Approach ---------------------------

def moveZerosBruteForce(n: int, a: list[int]) -> list[int]:
    # Temporary array to store non-zero elements
    temp = []

    # Copy non-zero elements from original array to temp
    for i in range(n):
        if a[i] != 0:
            temp.append(a[i])

    # Count of non-zero elements
    nz = len(temp)

    # Copy non-zero elements back to the original array
    for i in range(nz):
        a[i] = temp[i]

    # Fill the remaining positions with zeros
    for i in range(nz, n):
        a[i] = 0

    return a


# --------------------------- Optimal Approach (Two Pointer) ---------------------------

def moveZerosOptimal(n: int, a: list[int]) -> list[int]:
    j = -1  # Pointer to track the first zero

    # Find the index of the first zero
    for i in range(n):
        if a[i] == 0:
            j = i
            break

    # If there are no zeros, return the array as is
    if j == -1:
        return a

    # Traverse the array from the next index
    for i in range(j + 1, n):
        # If a non-zero element is found, swap it with the element at index j
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1  # Move j to the next zero position

    return a


# --------------------------- Test the Functions ---------------------------

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = len(arr)

# Test Brute Force
print("Brute Force Result:")
result_brute = moveZerosBruteForce(n, arr.copy())
print(result_brute)

# Test Optimal
print("Optimal Result:")
result_optimal = moveZerosOptimal(n, arr.copy())
print(result_optimal)
