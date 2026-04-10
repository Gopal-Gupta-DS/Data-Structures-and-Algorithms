# 📘 Explanation: Subsequence Sum Exists (Return One)

## 🔍 Problem Understanding
We need to check whether **at least one subsequence** exists whose sum equals `k`.

Unlike the previous problem:
- ❌ We DO NOT need all subsets
- ✅ We STOP as soon as we find one valid answer

---

## 🧠 Approach: Backtracking with Early Stopping

At each index, we have two choices:
1. Pick the element
2. Do not pick the element

---

## ⚡ Key Optimization: Early Return

As soon as we find:
total == k

We:
- Store the subset
- Return `True`
- Stop further recursion

---

## 🌳 Recursion Flow
```
For nums = [5, 9, 4]:
graph TD

A["Start: [] , sum=0"]

A --> B["Pick 5 → [5], sum=5"]
A --> C["Not Pick 5 → [], sum=0"]

%% LEFT SUBTREE (Picked 5)
B --> D["Pick 9 → [5,9], sum=14 ❌"]
B --> E["Not Pick 9 → [5], sum=5"]

E --> F["Pick 4 → [5,4], sum=9 ✅"]
E --> G["Not Pick 4 → [5], sum=5 ❌"]

%% RIGHT SUBTREE (Did NOT pick 5)
C --> H["Pick 9 → [9], sum=9 ✅"]
C --> I["Not Pick 9 → [], sum=0"]

I --> J["Pick 4 → [4], sum=4 ❌"]
I --> K["Not Pick 4 → [], sum=0 ❌"]
```

---

## ⚙️ Algorithm Steps

1. Start recursion from index 0
2. If total == k:
   - Save subset
   - Return True
3. If total > k:
   - Stop (pruning)
4. Try:
   - Include current element
   - If found → return True immediately
5. Backtrack and try exclude
6. Return False if no solution

---

## 🧪 Dry Run

Input:
nums = [5, 9, 4], k = 9

Execution:
- Pick 5 → sum = 5
  - Pick 9 → sum = 14 ❌
  - Skip 9 → Pick 4 → sum = 9 ✅

Output:
Exists: True  
Subsequence: [5,4]

---

## ⏱️ Complexity Analysis

### Time Complexity:
O(2^n) (worst case)

BUT practically faster due to early stopping

### Space Complexity:
O(n) (recursion stack + subset)

---

## 🚀 Key Insights

- This is an optimized version of Subset Sum
- Uses **boolean return to stop recursion early**
- Very common interview pattern:
  - "Return ANY one solution"
  - "Check existence"

---

## 🔁 Comparison with Previous Problem

| Problem Type | Output | Optimization |
|-------------|--------|-------------|
| Subset Sum (All) | All subsets | No early stop |
| Subsequence Exists | One subset | Early stop ✅ |

---

## 🔥 Pro Tip

If interviewer asks:
- “Return count” → use integer counter
- “Return all” → remove early return
- “Return one” → use boolean + early stop (this approach)
