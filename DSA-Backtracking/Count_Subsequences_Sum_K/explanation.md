# 📘 Explanation: Count Subsequences with Sum = K

## 🔍 Problem Understanding
We need to count how many subsequences exist such that their sum equals `k`.

Unlike previous problems:
- ❌ Do not store subsets
- ❌ Do not stop early
- ✅ Explore all possibilities and count

---

## 🧠 Approach: Backtracking (Counting)

At each index, we have two choices:
1. Pick the element
2. Do not pick the element

We recursively explore both and sum the results.

---

## 🌳 Recursion Flow (Concept)

Each node splits into:
- Pick → add value
- Not Pick → skip value

---

## ⚙️ Algorithm Steps

1. Start from index 0 with total = 0
2. If total == k:
   - Return 1 (one valid subsequence found)
3. If total > k:
   - Return 0 (prune)
4. If index == len(nums):
   - Return 0
5. Recursively:
   - pick = include element
   - not_pick = exclude element
6. Return:
   pick + not_pick

---

## 🧪 Dry Run

Input:
nums = [1,3,2,1], k = 3

Valid subsequences:
- [1,2]
- [3]
- [2,1]

Output:
3

---

## ⏱️ Complexity Analysis

### Time Complexity:
O(2^n)

(We explore all subsequences)

### Space Complexity:
O(n) (recursion stack)

---

## 🚀 Key Insights

- This is a **counting version of subset problems**
- No early stopping → must explore full tree
- Pattern:
  - Return 1 → valid
  - Return 0 → invalid
  - Combine using addition

---

## 🔁 Comparison with Other Variants

| Problem Type | Return Type | Optimization |
|-------------|------------|-------------|
| Return All Subsequences | List | No pruning |
| Return One Subsequence | Boolean | Early stop |
| Count Subsequences | Integer | Full traversal |

---

## 🔥 Pro Tips

- If constraints increase → use DP (Memoization)
- This is same as:
  - Subset Sum Count
  - Target Sum problem (variation)

---

## ⚡ Optimization Idea (Advanced)

Use memoization:

dp[index][total] → store computed results

Reduces complexity to:
O(n * k)
