# Problem 2811

- Domain: `coding`

## Problem

```text
You are given two integers, n and k.
An array of distinct positive integers is called a k-avoiding array if there does not exist any pair of distinct elements that sum to k.
Return the minimum possible sum of a k-avoiding array of length n.
 
Example 1:

Input: n = 5, k = 4
Output: 18
Explanation: Consider the k-avoiding array [1,2,4,5,6], which has a sum of 18.
It can be proven that there is no k-avoiding array with a sum less than 18.

Example 2:

Input: n = 2, k = 6
Output: 3
Explanation: We can construct the array [1,2], which has a sum of 3.
It can be proven that there is no k-avoiding array with a sum less than 3.

 
Constraints:

1 <= n, k <= 50
```

### Starter Code

```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
```

### Test Cases

```json
[
  {
    "input": "5\n4",
    "output": "18",
    "testtype": "functional"
  },
  {
    "input": "2\n6",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "2\n3",
    "output": "4",
    "testtype": "functional"
  },
  {
    "input": "3\n5",
    "output": "8",
    "testtype": "functional"
  },
  {
    "input": "1\n1",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "1\n2",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "4\n5",
    "output": "14",
    "testtype": "functional"
  },
  {
    "input": "7\n9",
    "output": "40",
    "testtype": "functional"
  },
  {
    "input": "4\n3",
    "output": "13",
    "testtype": "functional"
  },
  {
    "input": "5\n4",
    "output": "18",
    "testtype": "functional"
  },
  {
    "input": "38\n49",
    "output": "1077",
    "testtype": "functional"
  },
  {
    "input": "40\n41",
    "output": "1220",
    "testtype": "functional"
  },
  {
    "input": "47\n28",
    "output": "1557",
    "testtype": "functional"
  },
  {
    "input": "45\n89",
    "output": "1079",
    "testtype": "functional"
  }
]
```

## Generation

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
You are given two integers, n and k.
An array of distinct positive integers is called a k-avoiding array if there does not exist any pair of distinct elements that sum to k.
Return the minimum possible sum of a k-avoiding array of length n.
 
Example 1:

Input: n = 5, k = 4
Output: 18
Explanation: Consider the k-avoiding array [1,2,4,5,6], which has a sum of 18.
It can be proven that there is no k-avoiding array with a sum less than 18.

Example 2:

Input: n = 2, k = 6
Output: 3
Explanation: We can construct the array [1,2], which has a sum of 3.
It can be proven that there is no k-avoiding array with a sum less than 3.

 
Constraints:

1 <= n, k <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # For k-avoiding with distinct positive integers:
        # If we take the smallest possible numbers [1..n] we may violate sums==k.
        # Greedy characterization:
        # To minimize sum, choose smallest numbers but never allow x and k-x both present.
        #
        # Optimal construction:
        # - First choose all numbers i = 1..n such that i < k - i (i <= (k-1)/2) are safe.
        # - Whenever we'd need a number x >= k/2, ensure its complement k-x is not already chosen.
        #
        # Equivalent simpler known solution for this problem:
        # Build array as:
        #   Start with i=1 and take i unless (k-i) is already taken.
        # Since n,k <= 50, we can do this directly efficiently.
        taken = set()
        x = 1
        total = 0
        while len(taken) < n:
            if k - x not in taken:  # would create a pair summing to k if complement is present
                taken.add(x)
                total += x
            x += 1
        return total
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy construction:
        # To minimize sum with all pair sums != k, we must avoid having x and (k-x)
        # both present. The minimum strategy is to take the smallest numbers:
        # 1,2,3,...,n except when a number would force its complement (k-x)
        # to be included too. The optimal resulting set is:
        # - 1..m where m = min(n, k//2 + (1 if k odd else 0))?
        #
        # Easier known construction for this problem:
        # Build numbers in increasing order but skip any number x such that (k-x)
        # is already chosen.
        chosen = set()
        s = 0
        x = 1
        while len(chosen) < n:
            if k - x not in chosen:
                chosen.add(x)
                s += x
            x += 1
        return s
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy works: pick smallest possible numbers without ever creating
        # a forbidden pair (x + y == k). Optimal construction:
        # if x is chosen, y = k - x must be avoided; equivalently, among
        # the numbers 1..k-1, we can use at most one from each pair summing to k.
        #
        # The minimum sum can be constructed as:
        # - Take the first m positive integers avoiding complements to k,
        # - Once we use all numbers < k, we can continue with k, k+1, ...
        #
        # For 1 <= x <= k-1, we must not select both x and (k-x).
        # Using smallest choices gives:
        # chosen numbers are:
        #   1, 2, ..., floor((k-1)/2)  plus possibly (k+1)/2 + 1? Actually:
        # We can select the smallest set of size t from {1..k-1} with the rule
        # that it contains at most one from each pair {x, k-x}.
        #
        # It turns out the minimal k-avoiding set of size n is:
        #   if n <= ceil((k-1)/2): take 1..n
        #   else: take 1..(k-1)//2, then jump to k+1, k+2, ... as needed.
        #
        # However easiest robust formula:
        # For i from 1 to n:
        #   choose the smallest positive integer that doesn't violate any existing choice.
        # This is safe under given constraints (n,k<=50).
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if (k - x) not in chosen:
                chosen.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Key idea:
        # For a chosen smallest element x, we cannot include k-x.
        # To minimize the total sum, we take the smallest possible numbers
        # while ensuring we never take a forbidden complement for any chosen element.
        #
        # The optimal construction is:
        # [1, 2, 3, ..., n] if this never creates a forbidden pair.
        # If a pair (i, k-i) would occur, we "skip" the larger conflicting numbers,
        # effectively using the rule:
        # answer = sum_{i=1..n} i + count_of_skips * k
        #
        # A simpler equivalent closed form:
        # Build the optimal set greedily with a boolean forbidden array for complements.
        # With constraints up to 50, this is fast and safe.

        used = set()
        total = 0
        cur = 1

        while len(used) < n:
            if k - cur in used:
                cur += 1
                continue
            used.add(cur)
            total += cur
            cur += 1

        return total
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # We need n distinct positive integers with no pair summing to k.
        # Minimize sum -> start from 1 upward, but whenever adding x would create
        # a forbidden pair with an already chosen y = k - x, we skip.
        chosen = set()
        total = 0
        x = 1
        while len(chosen) < n:
            if k - x not in chosen:
                chosen.add(x)
                total += x
            x += 1
        return total
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Choose the smallest n positive integers that avoid having two distinct
        # elements summing to k. This can be achieved greedily:
        # - If we take x, we cannot take k-x (unless k-x == x, which isn't possible
        #   with distinct elements).
        # For minimal total sum, the optimal set is:
        # {1, 2, ..., n} if it doesn't contain such a forbidden pair,
        # otherwise we "skip" elements that would form the forbidden pair with
        # already chosen ones, starting from the top side.
        #
        # Known construction for this LeetCode problem:
        # Build the array using the rule:
        # For i in [0..n-1], pick i+1, and whenever it would conflict with a
        # previously picked value that sums to k, replace it by (k - (i+1)).
        #
        # However an easier equivalent greedy:
        # Start from smallest possible values, and whenever x causes a conflict
        # with existing y (x + y == k), we instead take the smallest unused value
        # greater than x that still avoids conflicts. With n,k<=50, brute over
        # candidate numbers is safe.
        #
        # We'll implement straightforward greedy with a set and increasing candidate.

        chosen = set()
        s = 0
        x = 1
        while len(chosen) < n:
            ok = True
            for y in chosen:
                if x + y == k:
                    ok = False
                    break
            if ok:
                chosen.add(x)
                s += x
            x += 1
        return s
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Optimal construction:
        # Use smallest positives [1,2,3,...] but avoid having x + y == k.
        #
        # Greedy idea:
        # For each candidate smallest number i, we may need to shift it upward
        # if it would create a forbidden pair with some already chosen number.
        #
        # A simpler known optimal approach:
        # The minimum sum is achieved by taking numbers as:
        # 1..n, but whenever a number x has its complement (k-x) available and
        # chosen, we must replace one of them to break the sum-to-k constraint.
        #
        # We can model this directly with a greedy set:
        chosen = set()
        total = 0
        x = 1
        while len(chosen) < n:
            # If x would pair with existing y to make k, skip x.
            if (k - x) not in chosen:
                chosen.add(x)
                total += x
            x += 1
        return total
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy/known construction:
        # Take the smallest numbers, but once you reach a value x where some chosen y would make x+y=k,
        # you must skip that complement.
        # The optimal k-avoiding array is achieved by taking:
        # [1, 2, ..., n] if no conflicts, but more generally:
        # for i from 1..n, choose i unless i > k - chosen, etc.
        #
        # There is a simpler closed form:
        # - If 2*i == k, only one of i and k-i can be used (but distinctness already handles it)
        # - Optimal strategy: pick the smallest n positive integers such that no two sum to k.
        #
        # We can construct it directly with a set while keeping it minimal (n,k <= 50 so this is safe).
        chosen = []
        used = set()
        x = 1
        while len(chosen) < n:
            if (k - x) not in used:
                chosen.append(x)
                used.add(x)
            x += 1

        return sum(chosen)
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Use the fact that the minimum-sum k-avoiding set is achieved by:
        # take the smallest possible numbers, avoiding any pair that sums to k.
        #
        # Construct greedily:
        # Start from 1 upward, add x if there is no y already chosen with x + y == k.
        # This works because choosing the smallest available number always yields
        # the lexicographically smallest (hence minimum-sum) valid set.
        
        chosen = set()
        s = 0
        x = 1
        while len(chosen) < n:
            # if k-x is already chosen, then x would form a forbidden pair
            if k - x not in chosen:
                chosen.add(x)
                s += x
            x += 1
        return s
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Choose the smallest possible distinct positive integers,
        # but ensure we never pick a pair (a, b) with a + b == k.
        #
        # Greedy: build the answer from smallest upward.
        # When considering x, it's forbidden only if there exists y already chosen
        # such that x + y == k <=> y == k - x.
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if (k - x) not in chosen:
                chosen.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 1.0000 | `full` |
| 1 | 1.0000 | `full` |
| 2 | 1.0000 | `full` |
| 3 | 1.0000 | `full` |
| 4 | 1.0000 | `full` |
| 5 | 1.0000 | `full` |
| 6 | 1.0000 | `full` |
| 7 | 1.0000 | `full` |
| 8 | 1.0000 | `full` |
| 9 | 1.0000 | `full` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 1</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 2</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 3</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 4</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 5</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 6</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 8</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 9</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

## Memory

- Skipped: `true`
- Reason: `insufficient_tiers`

### Grouped Solutions

#### Tier: `full`

<details>
<summary>full attempt 1</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # For k-avoiding with distinct positive integers:
        # If we take the smallest possible numbers [1..n] we may violate sums==k.
        # Greedy characterization:
        # To minimize sum, choose smallest numbers but never allow x and k-x both present.
        #
        # Optimal construction:
        # - First choose all numbers i = 1..n such that i < k - i (i <= (k-1)/2) are safe.
        # - Whenever we'd need a number x >= k/2, ensure its complement k-x is not already chosen.
        #
        # Equivalent simpler known solution for this problem:
        # Build array as:
        #   Start with i=1 and take i unless (k-i) is already taken.
        # Since n,k <= 50, we can do this directly efficiently.
        taken = set()
        x = 1
        total = 0
        while len(taken) < n:
            if k - x not in taken:  # would create a pair summing to k if complement is present
                taken.add(x)
                total += x
            x += 1
        return total
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy construction:
        # To minimize sum with all pair sums != k, we must avoid having x and (k-x)
        # both present. The minimum strategy is to take the smallest numbers:
        # 1,2,3,...,n except when a number would force its complement (k-x)
        # to be included too. The optimal resulting set is:
        # - 1..m where m = min(n, k//2 + (1 if k odd else 0))?
        #
        # Easier known construction for this problem:
        # Build numbers in increasing order but skip any number x such that (k-x)
        # is already chosen.
        chosen = set()
        s = 0
        x = 1
        while len(chosen) < n:
            if k - x not in chosen:
                chosen.add(x)
                s += x
            x += 1
        return s
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy works: pick smallest possible numbers without ever creating
        # a forbidden pair (x + y == k). Optimal construction:
        # if x is chosen, y = k - x must be avoided; equivalently, among
        # the numbers 1..k-1, we can use at most one from each pair summing to k.
        #
        # The minimum sum can be constructed as:
        # - Take the first m positive integers avoiding complements to k,
        # - Once we use all numbers < k, we can continue with k, k+1, ...
        #
        # For 1 <= x <= k-1, we must not select both x and (k-x).
        # Using smallest choices gives:
        # chosen numbers are:
        #   1, 2, ..., floor((k-1)/2)  plus possibly (k+1)/2 + 1? Actually:
        # We can select the smallest set of size t from {1..k-1} with the rule
        # that it contains at most one from each pair {x, k-x}.
        #
        # It turns out the minimal k-avoiding set of size n is:
        #   if n <= ceil((k-1)/2): take 1..n
        #   else: take 1..(k-1)//2, then jump to k+1, k+2, ... as needed.
        #
        # However easiest robust formula:
        # For i from 1 to n:
        #   choose the smallest positive integer that doesn't violate any existing choice.
        # This is safe under given constraints (n,k<=50).
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if (k - x) not in chosen:
                chosen.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Key idea:
        # For a chosen smallest element x, we cannot include k-x.
        # To minimize the total sum, we take the smallest possible numbers
        # while ensuring we never take a forbidden complement for any chosen element.
        #
        # The optimal construction is:
        # [1, 2, 3, ..., n] if this never creates a forbidden pair.
        # If a pair (i, k-i) would occur, we "skip" the larger conflicting numbers,
        # effectively using the rule:
        # answer = sum_{i=1..n} i + count_of_skips * k
        #
        # A simpler equivalent closed form:
        # Build the optimal set greedily with a boolean forbidden array for complements.
        # With constraints up to 50, this is fast and safe.

        used = set()
        total = 0
        cur = 1

        while len(used) < n:
            if k - cur in used:
                cur += 1
                continue
            used.add(cur)
            total += cur
            cur += 1

        return total
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # We need n distinct positive integers with no pair summing to k.
        # Minimize sum -> start from 1 upward, but whenever adding x would create
        # a forbidden pair with an already chosen y = k - x, we skip.
        chosen = set()
        total = 0
        x = 1
        while len(chosen) < n:
            if k - x not in chosen:
                chosen.add(x)
                total += x
            x += 1
        return total
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Choose the smallest n positive integers that avoid having two distinct
        # elements summing to k. This can be achieved greedily:
        # - If we take x, we cannot take k-x (unless k-x == x, which isn't possible
        #   with distinct elements).
        # For minimal total sum, the optimal set is:
        # {1, 2, ..., n} if it doesn't contain such a forbidden pair,
        # otherwise we "skip" elements that would form the forbidden pair with
        # already chosen ones, starting from the top side.
        #
        # Known construction for this LeetCode problem:
        # Build the array using the rule:
        # For i in [0..n-1], pick i+1, and whenever it would conflict with a
        # previously picked value that sums to k, replace it by (k - (i+1)).
        #
        # However an easier equivalent greedy:
        # Start from smallest possible values, and whenever x causes a conflict
        # with existing y (x + y == k), we instead take the smallest unused value
        # greater than x that still avoids conflicts. With n,k<=50, brute over
        # candidate numbers is safe.
        #
        # We'll implement straightforward greedy with a set and increasing candidate.

        chosen = set()
        s = 0
        x = 1
        while len(chosen) < n:
            ok = True
            for y in chosen:
                if x + y == k:
                    ok = False
                    break
            if ok:
                chosen.add(x)
                s += x
            x += 1
        return s
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Optimal construction:
        # Use smallest positives [1,2,3,...] but avoid having x + y == k.
        #
        # Greedy idea:
        # For each candidate smallest number i, we may need to shift it upward
        # if it would create a forbidden pair with some already chosen number.
        #
        # A simpler known optimal approach:
        # The minimum sum is achieved by taking numbers as:
        # 1..n, but whenever a number x has its complement (k-x) available and
        # chosen, we must replace one of them to break the sum-to-k constraint.
        #
        # We can model this directly with a greedy set:
        chosen = set()
        total = 0
        x = 1
        while len(chosen) < n:
            # If x would pair with existing y to make k, skip x.
            if (k - x) not in chosen:
                chosen.add(x)
                total += x
            x += 1
        return total
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy/known construction:
        # Take the smallest numbers, but once you reach a value x where some chosen y would make x+y=k,
        # you must skip that complement.
        # The optimal k-avoiding array is achieved by taking:
        # [1, 2, ..., n] if no conflicts, but more generally:
        # for i from 1..n, choose i unless i > k - chosen, etc.
        #
        # There is a simpler closed form:
        # - If 2*i == k, only one of i and k-i can be used (but distinctness already handles it)
        # - Optimal strategy: pick the smallest n positive integers such that no two sum to k.
        #
        # We can construct it directly with a set while keeping it minimal (n,k <= 50 so this is safe).
        chosen = []
        used = set()
        x = 1
        while len(chosen) < n:
            if (k - x) not in used:
                chosen.append(x)
                used.add(x)
            x += 1

        return sum(chosen)
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Use the fact that the minimum-sum k-avoiding set is achieved by:
        # take the smallest possible numbers, avoiding any pair that sums to k.
        #
        # Construct greedily:
        # Start from 1 upward, add x if there is no y already chosen with x + y == k.
        # This works because choosing the smallest available number always yields
        # the lexicographically smallest (hence minimum-sum) valid set.
        
        chosen = set()
        s = 0
        x = 1
        while len(chosen) < n:
            # if k-x is already chosen, then x would form a forbidden pair
            if k - x not in chosen:
                chosen.add(x)
                s += x
            x += 1
        return s
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Choose the smallest possible distinct positive integers,
        # but ensure we never pick a pair (a, b) with a + b == k.
        #
        # Greedy: build the answer from smallest upward.
        # When considering x, it's forbidden only if there exists y already chosen
        # such that x + y == k <=> y == k - x.
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if (k - x) not in chosen:
                chosen.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

## Evaluation

- Baseline pass@1: `0.6000`
- Augmented pass@1: `0.6000`
- Improvement: `+0.0000`

- Augmented outputs reused baseline generations because no memory was available.

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
You are given two integers, n and k.
An array of distinct positive integers is called a k-avoiding array if there does not exist any pair of distinct elements that sum to k.
Return the minimum possible sum of a k-avoiding array of length n.
 
Example 1:

Input: n = 5, k = 4
Output: 18
Explanation: Consider the k-avoiding array [1,2,4,5,6], which has a sum of 18.
It can be proven that there is no k-avoiding array with a sum less than 18.

Example 2:

Input: n = 2, k = 6
Output: 3
Explanation: We can construct the array [1,2], which has a sum of 3.
It can be proven that there is no k-avoiding array with a sum less than 3.

 
Constraints:

1 <= n, k <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # If k is 1 or 2, then any two distinct positive integers sum >= 3,
        # so when k <= 2, there can be no forbidden pair; smallest sum is 1..n.
        if k <= 2:
            return n * (n + 1) // 2

        # Otherwise, the optimal construction is:
        # take the smallest i in {1..n} but avoid picking both x and k-x.
        # The known greedy/minimal-sum result for this constraint is:
        #   - choose numbers 1..n' where n' = min(n, k-1)
        #   - if n > k-1, we must include additional numbers, and they can start
        #     from k+1, ensuring no pair sums to k.
        #
        # This leads to:
        # If n <= k-1: answer is sum(1..n)
        # Else: answer is sum(1..(k-1)) + sum((k+1)..(k+(n-(k-1))))
        if n <= k - 1:
            return n * (n + 1) // 2

        first_part = (k - 1) * k // 2  # sum 1..k-1
        m = n - (k - 1)                 # how many extra numbers needed

        # extra numbers are: k+1, k+2, ..., k+m
        # sum = (k+1 + k+m) * m / 2 = (2k + m + 1) * m / 2
        extra_part = (2 * k + m + 1) * m // 2

        return first_part + extra_part
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Minimal sum is achieved by taking the smallest possible n distinct
        # positive integers, while ensuring no two sum to k.
        #
        # For any chosen x < k, the number k-x is forbidden.
        # Greedy: try numbers in increasing order and keep the ones that are allowed.
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if x not in chosen and (k - x) not in chosen:
                chosen.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # To minimize the sum with distinct positive integers and no pair summing to k,
        # we can take as many small integers as possible, but we must avoid choosing
        # both x and k-x for any x.
        #
        # The optimal construction:
        # - Choose the smallest possible positive integers, ensuring we never pick
        #   a number whose complement to k is already chosen.
        #
        # With this greedy, the resulting set is provably minimal.
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if x not in chosen and (k - x) not in chosen:
                chosen.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy construction:
        # - Start from 1,2,3,... (distinct positives).
        # - But you must avoid any pair (x, k-x). That means you can keep at most
        #   one number from each complementary pair {i, k-i}.
        # - The minimal-sum strategy is to take the smallest available numbers,
        #   skipping a value i if k-i was already taken.
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if (k - x) in chosen:
                x += 1
                continue
            chosen.add(x)
            ans += x
            x += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Choose the smallest possible distinct positive integers while ensuring
        # no two sum to k. The optimal strategy is:
        # 1) Take all integers from 1 up to floor((k-1)/2).
        #    Any two among these are < k, so they cannot sum to k.
        # 2) For the remaining elements, we must take numbers > k/2.
        #    To minimize the sum, we take the smallest available such numbers:
        #    k - i for i in taken small set, and also i > k - i (i.e., > k/2).
        #
        # This simplifies to the known greedy/minimization outcome:
        # Answer = sum of first n numbers, except when a number x would force
        # its complement (k-x) to be in the set; we avoid those by taking the
        # maximal safe prefix then smallest from the complementary side.
        #
        # Implementation using the explicit optimal construction:
        limit = (k - 1) // 2  # largest x such that x + (k-x) > k-1
        res = 0

        # First, take 1..limit (all safe among themselves)
        take_small = min(n, limit)
        for i in range(1, take_small + 1):
            res += i

        if take_small == n:
            return res

        # Need more numbers; take the smallest numbers > limit
        # that do not create a pair summing to k with chosen small numbers.
        # Since we already took 1..take_small, we must avoid selecting any
        # number y such that k - y is in [1..take_small].
        # That means y cannot be in [k - take_small .. k - 1].
        remaining = n - take_small
        start = limit + 1

        y = start
        while remaining > 0:
            # If k - y is among chosen small numbers, skip y.
            # chosen small numbers are 1..take_small
            if 1 <= k - y <= take_small:
                y += 1
                continue
            res += y
            remaining -= 1
            y += 1

        return res
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        """
        Minimum sum of n distinct positive integers with no two summing to k.

        Key idea:
        - Let m = k//2.
        - Numbers 1..m can all be used together without creating a pair summing to k.
          (If i <= m, then k-i >= m; for i != k-i you'd need the other number which
           is > m.)
        - After that, the remaining choices must avoid complements to already chosen
          numbers. The greedy optimal construction is:
            choose 1..m, then k-m+1, k-m+2, ...
          until we have n numbers.
        This yields the minimal possible sum.
        """
        m = k // 2
        arr = []

        # Take all safe small numbers
        small_cnt = min(n, m)
        for i in range(1, small_cnt + 1):
            arr.append(i)

        # If more needed, take the next block from the top side:
        # smallest number > m whose complement to k isn't in arr
        cur = k - m + 1  # first in the upper block
        while len(arr) < n:
            arr.append(cur)
            cur += 1

        return sum(arr)
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy construction:
        # Pick the smallest possible positive integers while ensuring no pair sums to k.
        # The optimal set is:
        # [1, 2, ..., n] if 2n < k
        # otherwise it uses numbers from the left side but avoids complements summing to k,
        # resulting in:
        # [1, 2, ..., k//2] plus shifted numbers for the remaining elements.
        if n <= 0:
            return 0

        # If smallest n numbers already don't create a k-sum pair
        # then answer is their sum.
        # Any pair among 1..n would sum to <= 2n.
        if 2 * n < k:
            return n * (n + 1) // 2

        # For the general case, consider choosing numbers as:
        # 1..m where m = k//2 are always safe among themselves (since 2*i <= k-1 when i<=k//2).
        m = k // 2
        if n <= m:
            return n * (n + 1) // 2

        # Need (n - m) more numbers. To avoid sums to k,
        # for each x chosen as t = m + 1, ..., we must ensure x + y != k for any chosen y in [1..m].
        # The best way (min sum) is to take consecutive numbers starting from k - m + 1
        # which are exactly complements avoidance.
        # The known optimal closed form:
        # Answer = sum(1..m) + sum((k - m + 1)..(k - m + (n-m)))
        extra = n - m
        start = k - m + 1
        end = start + extra - 1
        return m * (m + 1) // 2 + (start + end) * extra // 2
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy construction:
        # To minimize the sum, we take the smallest possible distinct positives.
        # If some chosen x forces (k-x) to appear later, we must avoid that.
        # Optimal known pattern:
        # - Choose as many as possible from the range [1, k-1]
        # - For the rest, continue with numbers starting from k+1 upwards,
        #   because all numbers > k cannot form sum k with any positive integer.
        
        # If n <= k-1, we can take [1..n] (no pair sums to k because both would be < k)
        if n <= k - 1:
            return n * (n + 1) // 2

        # Otherwise, take all [1..k-1]
        # Their sum is (k-1)*k/2, and they are pairwise distinct.
        base = (k - 1) * k // 2
        remaining = n - (k - 1)

        # Now add the smallest remaining distinct positives that are > k
        # These are: k+1, k+2, ..., k+remaining
        first = k + 1
        last = k + remaining
        extra = (first + last) * remaining // 2
        return base + extra
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # If we pick the smallest possible distinct positive integers [1..n],
        # some pairs might sum to k. To avoid that, we must adjust numbers
        # that would create forbidden sums.
        #
        # Observations:
        # - For any x in the final set, k-x cannot also be in the set.
        # - To minimize the total sum, we always prefer smaller unused numbers.
        #
        # Optimal construction:
        # - Sort by increasing value; greedily take smallest available values
        #   that don't violate the "sum to k" restriction.
        #
        # For n,k <= 50, a simple greedy with a boolean "used" is sufficient.
        
        used = [False] * (200)  # enough since n,k<=50 and answer is small
        arr = []
        
        # We'll try values starting from 1 upward until we collect n numbers.
        x = 1
        while len(arr) < n:
            # check if x is forbidden with any existing element y where x+y==k
            forbidden = False
            y = k - x
            if y > 0 and y < len(used) and used[y]:
                forbidden = True
            if not forbidden and not used[x]:
                used[x] = True
                arr.append(x)
            x += 1
        
        return sum(arr)
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Use greedy construction: for i-th element (0-indexed) choose smallest
        # positive integer that doesn't create a forbidden pair with any previous element.
        used = set()
        ans = 0
        x = 1
        while len(used) < n:
            # If there exists y in used with y + x == k, then x is forbidden.
            if (k - x) not in used:
                used.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

#### Baseline Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.2143 | `partial` |
| 1 | 1.0000 | `full` |
| 2 | 1.0000 | `full` |
| 3 | 1.0000 | `full` |
| 4 | 1.0000 | `full` |
| 5 | 0.2857 | `partial` |
| 6 | 0.2857 | `partial` |
| 7 | 0.1429 | `partial` |
| 8 | 1.0000 | `full` |
| 9 | 1.0000 | `full` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 3,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "18",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": false,
      "expected": "4",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "8",
      "actual": "6",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "14",
      "actual": "10",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "28",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "13",
      "actual": "12",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1077",
      "actual": "741",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1220",
      "actual": "820",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1557",
      "actual": "1148",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1079",
      "actual": "1035",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 1</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 2</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 3</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 4</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 5</summary>

```json
{
  "passed": 4,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "18",
      "actual": "15",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": false,
      "expected": "8",
      "actual": "7",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "14",
      "actual": "12",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "31",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "15",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1077",
      "actual": "755",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1220",
      "actual": "840",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1557",
      "actual": "1128",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1079",
      "actual": "1036",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 6</summary>

```json
{
  "passed": 4,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "18",
      "actual": "15",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": false,
      "expected": "8",
      "actual": "7",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "14",
      "actual": "12",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "31",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "15",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1077",
      "actual": "755",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1220",
      "actual": "840",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1557",
      "actual": "1128",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1079",
      "actual": "1036",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "passed": 2,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "18",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": false,
      "expected": "4",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "8",
      "actual": "6",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "14",
      "actual": "10",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "28",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "13",
      "actual": "12",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1077",
      "actual": "741",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1220",
      "actual": "820",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1557",
      "actual": "1148",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1079",
      "actual": "1035",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 8</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 9</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

### Augmented

#### Outputs

<details>
<summary>Augmented generation 1</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # If k is 1 or 2, then any two distinct positive integers sum >= 3,
        # so when k <= 2, there can be no forbidden pair; smallest sum is 1..n.
        if k <= 2:
            return n * (n + 1) // 2

        # Otherwise, the optimal construction is:
        # take the smallest i in {1..n} but avoid picking both x and k-x.
        # The known greedy/minimal-sum result for this constraint is:
        #   - choose numbers 1..n' where n' = min(n, k-1)
        #   - if n > k-1, we must include additional numbers, and they can start
        #     from k+1, ensuring no pair sums to k.
        #
        # This leads to:
        # If n <= k-1: answer is sum(1..n)
        # Else: answer is sum(1..(k-1)) + sum((k+1)..(k+(n-(k-1))))
        if n <= k - 1:
            return n * (n + 1) // 2

        first_part = (k - 1) * k // 2  # sum 1..k-1
        m = n - (k - 1)                 # how many extra numbers needed

        # extra numbers are: k+1, k+2, ..., k+m
        # sum = (k+1 + k+m) * m / 2 = (2k + m + 1) * m / 2
        extra_part = (2 * k + m + 1) * m // 2

        return first_part + extra_part
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Minimal sum is achieved by taking the smallest possible n distinct
        # positive integers, while ensuring no two sum to k.
        #
        # For any chosen x < k, the number k-x is forbidden.
        # Greedy: try numbers in increasing order and keep the ones that are allowed.
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if x not in chosen and (k - x) not in chosen:
                chosen.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # To minimize the sum with distinct positive integers and no pair summing to k,
        # we can take as many small integers as possible, but we must avoid choosing
        # both x and k-x for any x.
        #
        # The optimal construction:
        # - Choose the smallest possible positive integers, ensuring we never pick
        #   a number whose complement to k is already chosen.
        #
        # With this greedy, the resulting set is provably minimal.
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if x not in chosen and (k - x) not in chosen:
                chosen.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy construction:
        # - Start from 1,2,3,... (distinct positives).
        # - But you must avoid any pair (x, k-x). That means you can keep at most
        #   one number from each complementary pair {i, k-i}.
        # - The minimal-sum strategy is to take the smallest available numbers,
        #   skipping a value i if k-i was already taken.
        chosen = set()
        ans = 0
        x = 1
        while len(chosen) < n:
            if (k - x) in chosen:
                x += 1
                continue
            chosen.add(x)
            ans += x
            x += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Choose the smallest possible distinct positive integers while ensuring
        # no two sum to k. The optimal strategy is:
        # 1) Take all integers from 1 up to floor((k-1)/2).
        #    Any two among these are < k, so they cannot sum to k.
        # 2) For the remaining elements, we must take numbers > k/2.
        #    To minimize the sum, we take the smallest available such numbers:
        #    k - i for i in taken small set, and also i > k - i (i.e., > k/2).
        #
        # This simplifies to the known greedy/minimization outcome:
        # Answer = sum of first n numbers, except when a number x would force
        # its complement (k-x) to be in the set; we avoid those by taking the
        # maximal safe prefix then smallest from the complementary side.
        #
        # Implementation using the explicit optimal construction:
        limit = (k - 1) // 2  # largest x such that x + (k-x) > k-1
        res = 0

        # First, take 1..limit (all safe among themselves)
        take_small = min(n, limit)
        for i in range(1, take_small + 1):
            res += i

        if take_small == n:
            return res

        # Need more numbers; take the smallest numbers > limit
        # that do not create a pair summing to k with chosen small numbers.
        # Since we already took 1..take_small, we must avoid selecting any
        # number y such that k - y is in [1..take_small].
        # That means y cannot be in [k - take_small .. k - 1].
        remaining = n - take_small
        start = limit + 1

        y = start
        while remaining > 0:
            # If k - y is among chosen small numbers, skip y.
            # chosen small numbers are 1..take_small
            if 1 <= k - y <= take_small:
                y += 1
                continue
            res += y
            remaining -= 1
            y += 1

        return res
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        """
        Minimum sum of n distinct positive integers with no two summing to k.

        Key idea:
        - Let m = k//2.
        - Numbers 1..m can all be used together without creating a pair summing to k.
          (If i <= m, then k-i >= m; for i != k-i you'd need the other number which
           is > m.)
        - After that, the remaining choices must avoid complements to already chosen
          numbers. The greedy optimal construction is:
            choose 1..m, then k-m+1, k-m+2, ...
          until we have n numbers.
        This yields the minimal possible sum.
        """
        m = k // 2
        arr = []

        # Take all safe small numbers
        small_cnt = min(n, m)
        for i in range(1, small_cnt + 1):
            arr.append(i)

        # If more needed, take the next block from the top side:
        # smallest number > m whose complement to k isn't in arr
        cur = k - m + 1  # first in the upper block
        while len(arr) < n:
            arr.append(cur)
            cur += 1

        return sum(arr)
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy construction:
        # Pick the smallest possible positive integers while ensuring no pair sums to k.
        # The optimal set is:
        # [1, 2, ..., n] if 2n < k
        # otherwise it uses numbers from the left side but avoids complements summing to k,
        # resulting in:
        # [1, 2, ..., k//2] plus shifted numbers for the remaining elements.
        if n <= 0:
            return 0

        # If smallest n numbers already don't create a k-sum pair
        # then answer is their sum.
        # Any pair among 1..n would sum to <= 2n.
        if 2 * n < k:
            return n * (n + 1) // 2

        # For the general case, consider choosing numbers as:
        # 1..m where m = k//2 are always safe among themselves (since 2*i <= k-1 when i<=k//2).
        m = k // 2
        if n <= m:
            return n * (n + 1) // 2

        # Need (n - m) more numbers. To avoid sums to k,
        # for each x chosen as t = m + 1, ..., we must ensure x + y != k for any chosen y in [1..m].
        # The best way (min sum) is to take consecutive numbers starting from k - m + 1
        # which are exactly complements avoidance.
        # The known optimal closed form:
        # Answer = sum(1..m) + sum((k - m + 1)..(k - m + (n-m)))
        extra = n - m
        start = k - m + 1
        end = start + extra - 1
        return m * (m + 1) // 2 + (start + end) * extra // 2
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Greedy construction:
        # To minimize the sum, we take the smallest possible distinct positives.
        # If some chosen x forces (k-x) to appear later, we must avoid that.
        # Optimal known pattern:
        # - Choose as many as possible from the range [1, k-1]
        # - For the rest, continue with numbers starting from k+1 upwards,
        #   because all numbers > k cannot form sum k with any positive integer.
        
        # If n <= k-1, we can take [1..n] (no pair sums to k because both would be < k)
        if n <= k - 1:
            return n * (n + 1) // 2

        # Otherwise, take all [1..k-1]
        # Their sum is (k-1)*k/2, and they are pairwise distinct.
        base = (k - 1) * k // 2
        remaining = n - (k - 1)

        # Now add the smallest remaining distinct positives that are > k
        # These are: k+1, k+2, ..., k+remaining
        first = k + 1
        last = k + remaining
        extra = (first + last) * remaining // 2
        return base + extra
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # If we pick the smallest possible distinct positive integers [1..n],
        # some pairs might sum to k. To avoid that, we must adjust numbers
        # that would create forbidden sums.
        #
        # Observations:
        # - For any x in the final set, k-x cannot also be in the set.
        # - To minimize the total sum, we always prefer smaller unused numbers.
        #
        # Optimal construction:
        # - Sort by increasing value; greedily take smallest available values
        #   that don't violate the "sum to k" restriction.
        #
        # For n,k <= 50, a simple greedy with a boolean "used" is sufficient.
        
        used = [False] * (200)  # enough since n,k<=50 and answer is small
        arr = []
        
        # We'll try values starting from 1 upward until we collect n numbers.
        x = 1
        while len(arr) < n:
            # check if x is forbidden with any existing element y where x+y==k
            forbidden = False
            y = k - x
            if y > 0 and y < len(used) and used[y]:
                forbidden = True
            if not forbidden and not used[x]:
                used[x] = True
                arr.append(x)
            x += 1
        
        return sum(arr)
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Use greedy construction: for i-th element (0-indexed) choose smallest
        # positive integer that doesn't create a forbidden pair with any previous element.
        used = set()
        ans = 0
        x = 1
        while len(used) < n:
            # If there exists y in used with y + x == k, then x is forbidden.
            if (k - x) not in used:
                used.add(x)
                ans += x
            x += 1
        return ans
```
```

</details>

#### Augmented Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.2143 | `partial` |
| 1 | 1.0000 | `full` |
| 2 | 1.0000 | `full` |
| 3 | 1.0000 | `full` |
| 4 | 1.0000 | `full` |
| 5 | 0.2857 | `partial` |
| 6 | 0.2857 | `partial` |
| 7 | 0.1429 | `partial` |
| 8 | 1.0000 | `full` |
| 9 | 1.0000 | `full` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 3,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "18",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": false,
      "expected": "4",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "8",
      "actual": "6",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "14",
      "actual": "10",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "28",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "13",
      "actual": "12",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1077",
      "actual": "741",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1220",
      "actual": "820",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1557",
      "actual": "1148",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1079",
      "actual": "1035",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 1</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 2</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 3</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 4</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 5</summary>

```json
{
  "passed": 4,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "18",
      "actual": "15",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": false,
      "expected": "8",
      "actual": "7",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "14",
      "actual": "12",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "31",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "15",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1077",
      "actual": "755",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1220",
      "actual": "840",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1557",
      "actual": "1128",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1079",
      "actual": "1036",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 6</summary>

```json
{
  "passed": 4,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "18",
      "actual": "15",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": false,
      "expected": "8",
      "actual": "7",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "14",
      "actual": "12",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "31",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "15",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1077",
      "actual": "755",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1220",
      "actual": "840",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1557",
      "actual": "1128",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1079",
      "actual": "1036",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "passed": 2,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "18",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": false,
      "expected": "4",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "8",
      "actual": "6",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "14",
      "actual": "10",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "28",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "13",
      "actual": "12",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1077",
      "actual": "741",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1220",
      "actual": "820",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1557",
      "actual": "1148",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1079",
      "actual": "1035",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 8</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 9</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    },
    {
      "passed": true,
      "expected": "13",
      "actual": "13",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1077",
      "actual": "1077",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1220",
      "actual": "1220",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1557",
      "actual": "1557",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1079",
      "actual": "1079",
      "error": ""
    }
  ]
}
```

</details>
