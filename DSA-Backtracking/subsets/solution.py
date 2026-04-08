"""
Problem: Subsets (Backtracking)
Author: Your Name
Approach: Backtracking (Include / Exclude)
Time Complexity: O(2^n * n)
Space Complexity: O(n)
"""

def subsets(nums):
    result = []

    def backtrack(index, subset):
        # Base case: store result
        if index == len(nums):
            result.append(subset.copy())
            return

        # 1. Include current element
        subset.append(nums[index])
        backtrack(index + 1, subset)

        # 2. Backtrack (remove element)
        subset.pop()

        # 3. Exclude current element
        backtrack(index + 1, subset)

    backtrack(0, [])
    return result


# Driver Code
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(subsets(nums))
