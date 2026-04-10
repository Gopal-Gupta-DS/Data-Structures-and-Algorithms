# ------------------------------------------------------------
# Check if any subsequence with sum = k exists
# Return any ONE valid subsequence
# ------------------------------------------------------------

def check_subsequence(index, total, subset):
    # --------------------------------------------------------
    # Base Case 1: Found valid subsequence
    # --------------------------------------------------------
    if total == k:
        result.append(subset.copy())
        return True

    # --------------------------------------------------------
    # Base Case 2: Prune if sum exceeds k
    # --------------------------------------------------------
    if total > k:
        return False

    # --------------------------------------------------------
    # Base Case 3: End of array
    # --------------------------------------------------------
    if index >= len(nums):
        return False

    # --------------------------------------------------------
    # Choice 1: Pick current element
    # --------------------------------------------------------
    subset.append(nums[index])
    pick = check_subsequence(index + 1, total + nums[index], subset)

    # Early stopping if solution found
    if pick:
        return True

    # Backtrack
    subset.pop()

    # --------------------------------------------------------
    # Choice 2: Do NOT pick current element
    # --------------------------------------------------------
    not_pick = check_subsequence(index + 1, total, subset)

    return not_pick


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
nums = [5, 9, 4]
k = 9
result = []

exists = check_subsequence(0, 0, [])

print("Exists:", exists)
print("One valid subsequence:", result)
