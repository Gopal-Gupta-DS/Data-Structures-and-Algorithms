# ------------------------------------------------------------
# Count number of subsequences with sum = k
# ------------------------------------------------------------

def subsequence_count(index: int, total: int):
    # --------------------------------------------------------
    # Base Case 1: Found valid subsequence
    # --------------------------------------------------------
    if total == k:
        return 1

    # --------------------------------------------------------
    # Base Case 2: Prune if sum exceeds k
    # --------------------------------------------------------
    if total > k:
        return 0

    # --------------------------------------------------------
    # Base Case 3: End of array
    # --------------------------------------------------------
    if index >= len(nums):
        return 0

    # --------------------------------------------------------
    # Choice 1: Pick current element
    # --------------------------------------------------------
    pick = subsequence_count(index + 1, total + nums[index])

    # --------------------------------------------------------
    # Choice 2: Do NOT pick current element
    # --------------------------------------------------------
    not_pick = subsequence_count(index + 1, total)

    # Total ways = sum of both choices
    return pick + not_pick


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
nums = [1, 3, 2, 1]
k = 3

print("Count of subsequences with sum =", k, ":", subsequence_count(0, 0))
