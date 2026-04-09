# ------------------------------------------------------------
# Subset Sum using Backtracking
# ------------------------------------------------------------

def backtrack(index, total, subset):
    # Base Case 1: If sum exceeds target, stop exploring
    if total > k:
        return

    # Base Case 2: If all elements are processed
    if index == len(nums):
        if total == k:
            result.append(subset.copy())  # store valid subset
        return

    # --------------------------------------------------------
    # Choice 1: Include current element
    # --------------------------------------------------------
    subset.append(nums[index])
    backtrack(index + 1, total + nums[index], subset)

    # Backtrack (undo choice)
    subset.pop()

    # --------------------------------------------------------
    # Choice 2: Exclude current element
    # --------------------------------------------------------
    backtrack(index + 1, total, subset)


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
nums = [5, 9, 4]
k = 9
result = []

backtrack(0, 0, [])

print("Subsets with sum =", k, ":", result)
