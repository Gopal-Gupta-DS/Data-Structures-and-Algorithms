# 🧠 Explanation: Subsets using Backtracking

## 🔹 Core Idea
Each element has 2 choices:
- Include
- Exclude

Total subsets = 2^n

---

## 🔹 Approach
We use recursion and backtracking:
1. Include element
2. Recurse
3. Remove element (backtrack)
4. Exclude element

---

## 🔹 Dry Run (nums = [1,2])

Start: []

Include 1 → [1]
    Include 2 → [1,2]
    Exclude 2 → [1]

Exclude 1 → []
    Include 2 → [2]
    Exclude 2 → []

---

## 🔹 Edge Cases
- Empty input → `[[]]`
- Single element → `[[], [x]]`
- Duplicates → Need special handling

---

## 🔹 Complexity
- Time: O(2^n * n)
- Space: O(n)
