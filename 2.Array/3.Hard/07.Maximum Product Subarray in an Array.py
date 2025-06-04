# Maximum Product Subarray in an Array

# --------------------------- Brute Force Approach ---------------------------

def maxProductSubArrayBruteForce(nums):
    n = len(nums)
    result = float('-inf')

    # Try every subarray and calculate the product
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j + 1):
                prod *= nums[k]
            result = max(result, prod)

    return result


# --------------------------- Better Approach ---------------------------

def maxProductSubArrayBetter(nums):
    n = len(nums)
    result = nums[0]

    # For each starting index, multiply elements forward
    for i in range(n):
        prod = nums[i]
        result = max(result, prod)
        for j in range(i + 1, n):
            prod *= nums[j]
            result = max(result, prod)

    return result


# --------------------------- Optimal Approach ---------------------------

def maxProductSubArrayOptimal(nums):
    n = len(nums)
    prefix = 1   # Product from the start
    suffix = 1   # Product from the end
    ans = float('-inf')

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= nums[i]
        suffix *= nums[n - 1 - i]
        ans = max(ans, prefix, suffix)

    return ans


# --------------------------- Main Function ---------------------------

def main():
    arr = [1, 2, -3, 0, -4, -5]

    print("Brute Force Result:", maxProductSubArrayBruteForce(arr))
    print("Better Approach Result:", maxProductSubArrayBetter(arr))
    print("Optimal Approach Result:", maxProductSubArrayOptimal(arr))


if __name__ == "__main__":
    main()
