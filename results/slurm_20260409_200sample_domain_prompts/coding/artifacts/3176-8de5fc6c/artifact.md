# Problem 3176

- Domain: `coding`

## Problem

```text
You are given a 0-indexed array nums of integers.
A triplet of indices (i, j, k) is a mountain if:

i < j < k
nums[i] < nums[j] and nums[k] < nums[j]

Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.
 
Example 1:

Input: nums = [8,6,1,5,3]
Output: 9
Explanation: Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
- 2 < 3 < 4
- nums[2] < nums[3] and nums[4] < nums[3]
And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.

Example 2:

Input: nums = [5,4,8,7,10,2]
Output: 13
Explanation: Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
- 1 < 3 < 5
- nums[1] < nums[3] and nums[5] < nums[3]
And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.

Example 3:

Input: nums = [6,5,4,3,4,5]
Output: -1
Explanation: It can be shown that there are no mountain triplets in nums.

 
Constraints:

3 <= nums.length <= 50
1 <= nums[i] <= 50
```

### Starter Code

```python
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[8, 6, 1, 5, 3]",
    "output": "9",
    "testtype": "functional"
  },
  {
    "input": "[5, 4, 8, 7, 10, 2]",
    "output": "13",
    "testtype": "functional"
  },
  {
    "input": "[6, 5, 4, 3, 4, 5]",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "[3, 2, 1]",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "[1, 2, 3]",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "[1, 50, 1]",
    "output": "52",
    "testtype": "functional"
  },
  {
    "input": "[3, 4, 12]",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "[1, 44, 12]",
    "output": "57",
    "testtype": "functional"
  },
  {
    "input": "[41, 48, 2]",
    "output": "91",
    "testtype": "functional"
  },
  {
    "input": "[25, 3, 38]",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "[14, 33, 39]",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "[11, 37, 44, 48, 12, 25, 8, 21, 11, 45, 28, 48, 20, 1, 9, 12, 10, 23, 20, 29, 18, 4, 28, 16, 31, 37, 39, 40, 45, 28, 10, 16, 4, 47, 50, 35, 50, 8, 48, 28, 39, 16, 30, 17, 50, 47, 35, 45, 35, 32]",
    "output": "14",
    "testtype": "functional"
  },
  {
    "input": "[33, 50, 24, 11, 45, 44, 43, 45, 27, 43, 45, 19, 37, 37, 31, 32, 16, 23, 9, 9, 6, 19, 30, 20, 50, 31, 16, 36, 21, 22, 37, 16, 11, 12, 31, 21, 3, 25, 31, 20, 45, 2, 44, 31, 40, 41, 23, 25, 2, 10]",
    "output": "19",
    "testtype": "functional"
  },
  {
    "input": "[19, 12, 34, 1, 21, 23, 34, 36, 10, 2, 34, 41, 29, 48, 39, 41, 42, 28, 27, 22, 10, 50, 1, 13, 26, 17, 13, 31, 33, 49, 37, 32, 39, 26, 13, 38, 27, 39, 6, 43, 33, 46, 50, 15, 43, 44, 26, 5, 42, 40]",
    "output": "4",
    "testtype": "functional"
  },
  {
    "input": "[25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]",
    "output": "-1",
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
You are given a 0-indexed array nums of integers.
A triplet of indices (i, j, k) is a mountain if:

i < j < k
nums[i] < nums[j] and nums[k] < nums[j]

Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.
 
Example 1:

Input: nums = [8,6,1,5,3]
Output: 9
Explanation: Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
- 2 < 3 < 4
- nums[2] < nums[3] and nums[4] < nums[3]
And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.

Example 2:

Input: nums = [5,4,8,7,10,2]
Output: 13
Explanation: Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
- 1 < 3 < 5
- nums[1] < nums[3] and nums[5] < nums[3]
And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.

Example 3:

Input: nums = [6,5,4,3,4,5]
Output: -1
Explanation: It can be shown that there are no mountain triplets in nums.

 
Constraints:

3 <= nums.length <= 50
1 <= nums[i] <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # min_left[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        # min_right[k] = minimum nums[k] for k>j with nums[k] < nums[j]
        min_left = [INF] * n
        min_seen = [INF] * 51  # values are in [1..50]
        
        for j in range(n):
            v = nums[j]
            if v > 1:
                min_left[j] = min(min_seen[1:v])  # min nums[i] < v
            min_seen[v] = min(min_seen[v], v)

        min_right = [INF] * n
        min_seen = [INF] * 51
        for j in range(n - 1, -1, -1):
            v = nums[j]
            if v > 1:
                min_right[j] = min(min_seen[1:v])  # min nums[k] < v to the right
            min_seen[v] = min(min_seen[v], v)

        for j in range(n):
            if min_left[j] != INF and min_right[j] != INF:
                total = min_left[j] + nums[j] + min_right[j]
                if total < ans:
                    ans = total

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left_min[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        left_min = [INF] * n
        best = INF

        # Precompute left_min
        for j in range(n):
            x = nums[j]
            mn = INF
            for i in range(j):
                if nums[i] < x:
                    mn = min(mn, nums[i])
            left_min[j] = mn

        # For each middle j, find minimum nums[k] for k>j with nums[k] < nums[j]
        for j in range(1, n - 1):
            if left_min[j] == INF:
                continue
            x = nums[j]
            mn_right = INF
            for k in range(j + 1, n):
                if nums[k] < x:
                    mn_right = min(mn_right, nums[k])
            if mn_right != INF:
                best = min(best, left_min[j] + x + mn_right)

        return -1 if best == INF else best
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # bestL[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        bestL = [INF] * n
        # bestR[j] = minimum nums[k] for k>j with nums[k] < nums[j]
        bestR = [INF] * n

        # nums[i] are in [1..50], so use Fenwick-like min prefix by value.
        # For each possible value v, store the minimum seen index/value that equals v.
        # We can just track minimum numbers by value; then query all < nums[j].
        maxv = 50
        min_by_val = [INF] * (maxv + 1)

        # Compute bestL
        for j in range(n):
            x = nums[j]
            # query min_by_val[1..x-1]
            mn = INF
            for v in range(1, x):
                if min_by_val[v] < mn:
                    mn = min_by_val[v]
            bestL[j] = mn
            if nums[j] < min_by_val[x]:
                min_by_val[x] = nums[j]

        # Compute bestR (from right)
        min_by_val = [INF] * (maxv + 1)
        for j in range(n - 1, -1, -1):
            x = nums[j]
            mn = INF
            for v in range(1, x):
                if min_by_val[v] < mn:
                    mn = min_by_val[v]
            bestR[j] = mn
            if nums[j] < min_by_val[x]:
                min_by_val[x] = nums[j]

        ans = INF
        for j in range(n):
            if bestL[j] < INF and bestR[j] < INF:
                ans = min(ans, bestL[j] + nums[j] + bestR[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # best_left[v] = minimum value nums[i] with i < j and nums[i] == v
        best_left = [INF] * 51
        # We'll scan j from left to right, keeping best_left for nums[i] < nums[j].
        # For the right side, for each j we need min nums[k] for k > j with nums[k] < nums[j].
        # Precompute right_min_smaller[j][?] efficiently via suffix minima by value.
        # Since values are in [1,50], we can compute right_min[v] = minimum nums[k] to the right with nums[k] == v.
        right_min = [INF] * 51

        # Initialize suffix mins for k > j with j at 1 (we'll update as j moves).
        # Easier: maintain right_min for indices strictly greater than current j.
        # Start with last element as part of suffix, then adjust.
        right_min = [INF] * 51
        for idx in range(2, n):  # indices > 1
            right_min[nums[idx]] = min(right_min[nums[idx]], nums[idx])

        def min_suffix_smaller(val: int) -> int:
            # minimal value among right_min[x] for x < val
            m = INF
            # values range 1..50
            for x in range(1, val):
                if right_min[x] < m:
                    m = right_min[x]
            return m

        # Now iterate j from 1 to n-2
        for j in range(1, n - 1):
            vj = nums[j]

            left_smaller = INF
            for x in range(1, vj):
                left_smaller = min(left_smaller, best_left[x])

            right_smaller = min_suffix_smaller(vj)

            if left_smaller != INF and right_smaller != INF:
                ans = min(ans, left_smaller + vj + right_smaller)

            # Move j forward:
            # Current j becomes part of left for future iterations, and part of suffix for past ones.
            # Update best_left with nums[j]
            best_left[vj] = min(best_left[vj], vj)

            # Update suffix minima: remove index j+1? Our suffix currently represents indices > j.
            # We built initial suffix for j=1 as indices 2..n-1.
            # Before next iteration (j+1), suffix should represent indices > (j+1), i.e., indices j+2..n-1.
            # So we need to "remove" nums[j+1] from right_min, but we only stored minima by value,
            # which can't be removed easily.
            #
            # Instead, do a value-based DP without removals: precompute for each position j
            # the minimum value to the right that is < nums[j] using suffix arrays.
            #
            # Hence, break and switch to precomputed approach.

        # Recompute properly using precomputed suffix minima by value.
        # values are small (1..50), so do O(n*50) which is fine for n<=50.

        # left_best_min[v] while scanning
        ans = INF
        best_left = [INF] * 51

        # Precompute for each position j:
        # right_best_smaller[j] = min nums[k] for k>j with nums[k] < nums[j]
        right_best = [INF] * 51
        right_best_smaller = [INF] * n

        # Build suffix counts/minima
        for j in range(n - 2, -1, -1):
            v = nums[j + 1]
            right_best[v] = min(right_best[v], v)
            # query for position j
            cur = nums[j]
            m = INF
            for x in range(1, cur):
                m = min(m, right_best[x])
            right_best_smaller[j] = m

        for j in range(1, n - 1):
            vj = nums[j]
            left_min = INF
            for x in range(1, vj):
                left_min = min(left_min, best_left[x])
            right_min = right_best_smaller[j]
            if left_min != INF and right_min != INF:
                ans = min(ans, left_min + vj + right_min)
            best_left[vj] = min(best_left[vj], vj)

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9

        # min_left[j] = minimum nums[i] such that i < j and nums[i] < nums[j]
        min_left = [INF] * n
        for j in range(n):
            best = INF
            for i in range(j):
                if nums[i] < nums[j]:
                    best = min(best, nums[i])
            min_left[j] = best

        # min_right[j] = minimum nums[k] such that k > j and nums[k] < nums[j]
        min_right = [INF] * n
        for j in range(n - 1, -1, -1):
            best = INF
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    best = min(best, nums[k])
            min_right[j] = best

        ans = INF
        for j in range(n):
            if min_left[j] != INF and min_right[j] != INF:
                ans = min(ans, min_left[j] + nums[j] + min_right[j])

        return ans if ans != INF else -1
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF

        # left_best[j]: minimum possible nums[i] for i<j with nums[i] < nums[j]
        # right_best[j]: minimum possible nums[k] for k>j with nums[k] < nums[j]
        left_best = [INF] * n
        right_best = [INF] * n

        # Values are in [1..50], so we can use frequency-less min tracking.
        left_min_by_val = [INF] * 51  # left_min_by_val[v] = min nums[i] encountered with nums[i] == v

        for j in range(n):
            v = nums[j]
            # best among values < v
            best = INF
            for x in range(1, v):
                if left_min_by_val[x] < best:
                    best = left_min_by_val[x]
            left_best[j] = best

            # update encountered value v
            if nums[j] < left_min_by_val[v]:
                left_min_by_val[v] = nums[j]

        right_min_by_val = [INF] * 51
        for j in range(n - 1, -1, -1):
            v = nums[j]
            best = INF
            for x in range(1, v):
                if right_min_by_val[x] < best:
                    best = right_min_by_val[x]
            right_best[j] = best

            if nums[j] < right_min_by_val[v]:
                right_min_by_val[v] = nums[j]

        for j in range(1, n - 1):
            if left_best[j] != INF and right_best[j] != INF:
                ans = min(ans, left_best[j] + nums[j] + right_best[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left_min[j] = minimum nums[i] with i<j and nums[i] < nums[j]
        left_min = [INF] * n
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if nums[i] < left_min[j]:
                        left_min[j] = nums[i]

        # right_min[j] = minimum nums[k] with k>j and nums[k] < nums[j]
        right_min = [INF] * n
        for j in range(n):
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    if nums[k] < right_min[j]:
                        right_min[j] = nums[k]

        ans = INF
        for j in range(n):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        # left_min[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        # right_min[j] = minimum nums[k] for k>j with nums[k] < nums[j]
        left_min = [INF] * n
        right_min = [INF] * n

        # Since nums[i] in [1..50], we can track minimum value seen for each number.
        left_best = [INF] * 51
        for j in range(n):
            x = nums[j]
            best = min(left_best[1:x]) if x > 1 else INF
            left_min[j] = best
            left_best[x] = min(left_best[x], x)

        right_best = [INF] * 51
        for j in range(n - 1, -1, -1):
            x = nums[j]
            best = min(right_best[1:x]) if x > 1 else INF
            right_min[j] = best
            right_best[x] = min(right_best[x], x)

        ans = INF
        for j in range(n):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        # Try each position j as the mountain peak.
        for j in range(1, n - 1):
            best_left = float('inf')   # min nums[i] with i < j and nums[i] < nums[j]
            best_right = float('inf')  # min nums[k] with k > j and nums[k] < nums[j]

            for i in range(j):
                if nums[i] < nums[j]:
                    best_left = min(best_left, nums[i])

            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    best_right = min(best_right, nums[k])

            if best_left != float('inf') and best_right != float('inf'):
                ans = min(ans, best_left + nums[j] + best_right)

        return -1 if ans == float('inf') else ans
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left_min[j] = minimum value nums[i] for i<j with nums[i] < nums[j]
        # right_min[j] = minimum value nums[k] for k>j with nums[k] < nums[j]
        left_min = [INF] * n
        right_min = [INF] * n

        # Since nums[i] are in [1..50], we can use prefix/suffix minima by value.
        # Maintain best[v] = minimum nums[i] seen so far with value exactly v (or at least).
        # We'll query over values < nums[j].
        best_left = [INF] * 51
        for j in range(n):
            x = nums[j]
            left_best = INF
            for v in range(1, x):
                if best_left[v] < left_best:
                    left_best = best_left[v]
            left_min[j] = left_best
            best_left[x] = min(best_left[x], x)

        best_right = [INF] * 51
        for j in range(n - 1, -1, -1):
            x = nums[j]
            right_best = INF
            for v in range(1, x):
                if best_right[v] < right_best:
                    right_best = best_right[v]
            right_min[j] = right_best
            best_right[x] = min(best_right[x], x)

        ans = INF
        for j in range(1, n - 1):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 1.0000 | `full` |
| 1 | 1.0000 | `full` |
| 2 | 1.0000 | `full` |
| 3 | 0.8000 | `partial` |
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 12,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "52",
      "actual": "-1",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "57",
      "actual": "-1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "91",
      "actual": "-1",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    }
  ]
}
```

</details>

## Memory

- Skipped: `false`

### Prompt

```text
## Guidelines
You need to extract and summarize useful insights in the format of memory items based on comparing the successful and unsuccessful solution attempts below.
The goal of summarized memory items is to be GENERALIZABLE and TRANSFERABLE — each insight must be useful not just for this problem, but for a broad class of similar problems. Write each memory as advice that would help someone who has never seen this specific problem.

## Important notes
- You must first think about why certain attempts succeeded and others failed, then summarize the insights.
- You can extract multiple memory items from the comparison. Each should capture a distinct, independent insight.
- Prioritize GENERAL META-REASONING techniques over object-level hints. Favor principles about representation choice, constraint formalization, invariant selection, validation, decomposition, debugging, or algorithm selection.
- Convert failure observations into POSITIVE reusable guidance. Do not write memories that are just restatements of one wrong step.
- Do NOT mention specific values, answers, variable names, or problem-specific details. Every memory item must stand on its own as a general problem-solving principle or technique that transfers across different problems in the same domain.
- Avoid narrow one-off tricks unless they clearly transfer to a recurring class of problems. Fewer high-quality memories are better than many repetitive ones.
- Emphasize high-level strategies that would still make sense on a different problem in the same domain.

## Examples of good meta-reasoning memories
- Title: Constraint-First Reformulation
  Description: Turn informal requirements into explicit constraints before solving.
  Content: Rewrite vague conditions as equations, inequalities, parity rules, or state constraints. Use those formal constraints to guide the solution and reject invalid branches early.
- Title: Validate Risky Transformations
  Description: Check any step that can introduce invalid candidates against the original problem.
  Content: Squaring, dividing, relaxing constraints, or compressing state can create artifacts that look valid only in the transformed setting. Add a direct verification pass against the original conditions before committing to an answer.
- Title: Model the Smallest Faithful State
  Description: Reduce the problem to the minimal state that still determines future decisions.
  Content: If only parity, remainder class, last element, or turn matters, build the reasoning or DP around that reduced state instead of the full object. This shrinks search and makes transitions easier to verify.

### Problem
You are given a 0-indexed array nums of integers.
A triplet of indices (i, j, k) is a mountain if:

i < j < k
nums[i] < nums[j] and nums[k] < nums[j]

Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.
 
Example 1:

Input: nums = [8,6,1,5,3]
Output: 9
Explanation: Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
- 2 < 3 < 4
- nums[2] < nums[3] and nums[4] < nums[3]
And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.

Example 2:

Input: nums = [5,4,8,7,10,2]
Output: 13
Explanation: Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
- 1 < 3 < 5
- nums[1] < nums[3] and nums[5] < nums[3]
And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.

Example 3:

Input: nums = [6,5,4,3,4,5]
Output: -1
Explanation: It can be shown that there are no mountain triplets in nums.

 
Constraints:

3 <= nums.length <= 50
1 <= nums[i] <= 50

### Solutions
#### Correct
Attempt 1
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # min_left[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        # min_right[k] = minimum nums[k] for k>j with nums[k] < nums[j]
        min_left = [INF] * n
        min_seen = [INF] * 51  # values are in [1..50]
        
        for j in range(n):
            v = nums[j]
            if v > 1:
                min_left[j] = min(min_seen[1:v])  # min nums[i] < v
            min_seen[v] = min(min_seen[v], v)

        min_right = [INF] * n
        min_seen = [INF] * 51
        for j in range(n - 1, -1, -1):
            v = nums[j]
            if v > 1:
                min_right[j] = min(min_seen[1:v])  # min nums[k] < v to the right
            min_seen[v] = min(min_seen[v], v)

        for j in range(n):
            if min_left[j] != INF and min_right[j] != INF:
                total = min_left[j] + nums[j] + min_right[j]
                if total < ans:
                    ans = total

        return -1 if ans == INF else ans
```

Attempt 2
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left_min[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        left_min = [INF] * n
        best = INF

        # Precompute left_min
        for j in range(n):
            x = nums[j]
            mn = INF
            for i in range(j):
                if nums[i] < x:
                    mn = min(mn, nums[i])
            left_min[j] = mn

        # For each middle j, find minimum nums[k] for k>j with nums[k] < nums[j]
        for j in range(1, n - 1):
            if left_min[j] == INF:
                continue
            x = nums[j]
            mn_right = INF
            for k in range(j + 1, n):
                if nums[k] < x:
                    mn_right = min(mn_right, nums[k])
            if mn_right != INF:
                best = min(best, left_min[j] + x + mn_right)

        return -1 if best == INF else best
```

Attempt 3
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # bestL[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        bestL = [INF] * n
        # bestR[j] = minimum nums[k] for k>j with nums[k] < nums[j]
        bestR = [INF] * n

        # nums[i] are in [1..50], so use Fenwick-like min prefix by value.
        # For each possible value v, store the minimum seen index/value that equals v.
        # We can just track minimum numbers by value; then query all < nums[j].
        maxv = 50
        min_by_val = [INF] * (maxv + 1)

        # Compute bestL
        for j in range(n):
            x = nums[j]
            # query min_by_val[1..x-1]
            mn = INF
            for v in range(1, x):
                if min_by_val[v] < mn:
                    mn = min_by_val[v]
            bestL[j] = mn
            if nums[j] < min_by_val[x]:
                min_by_val[x] = nums[j]

        # Compute bestR (from right)
        min_by_val = [INF] * (maxv + 1)
        for j in range(n - 1, -1, -1):
            x = nums[j]
            mn = INF
            for v in range(1, x):
                if min_by_val[v] < mn:
                    mn = min_by_val[v]
            bestR[j] = mn
            if nums[j] < min_by_val[x]:
                min_by_val[x] = nums[j]

        ans = INF
        for j in range(n):
            if bestL[j] < INF and bestR[j] < INF:
                ans = min(ans, bestL[j] + nums[j] + bestR[j])

        return -1 if ans == INF else ans
```

Attempt 4
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9

        # min_left[j] = minimum nums[i] such that i < j and nums[i] < nums[j]
        min_left = [INF] * n
        for j in range(n):
            best = INF
            for i in range(j):
                if nums[i] < nums[j]:
                    best = min(best, nums[i])
            min_left[j] = best

        # min_right[j] = minimum nums[k] such that k > j and nums[k] < nums[j]
        min_right = [INF] * n
        for j in range(n - 1, -1, -1):
            best = INF
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    best = min(best, nums[k])
            min_right[j] = best

        ans = INF
        for j in range(n):
            if min_left[j] != INF and min_right[j] != INF:
                ans = min(ans, min_left[j] + nums[j] + min_right[j])

        return ans if ans != INF else -1
```

Attempt 5
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF

        # left_best[j]: minimum possible nums[i] for i<j with nums[i] < nums[j]
        # right_best[j]: minimum possible nums[k] for k>j with nums[k] < nums[j]
        left_best = [INF] * n
        right_best = [INF] * n

        # Values are in [1..50], so we can use frequency-less min tracking.
        left_min_by_val = [INF] * 51  # left_min_by_val[v] = min nums[i] encountered with nums[i] == v

        for j in range(n):
            v = nums[j]
            # best among values < v
            best = INF
            for x in range(1, v):
                if left_min_by_val[x] < best:
                    best = left_min_by_val[x]
            left_best[j] = best

            # update encountered value v
            if nums[j] < left_min_by_val[v]:
                left_min_by_val[v] = nums[j]

        right_min_by_val = [INF] * 51
        for j in range(n - 1, -1, -1):
            v = nums[j]
            best = INF
            for x in range(1, v):
                if right_min_by_val[x] < best:
                    best = right_min_by_val[x]
            right_best[j] = best

            if nums[j] < right_min_by_val[v]:
                right_min_by_val[v] = nums[j]

        for j in range(1, n - 1):
            if left_best[j] != INF and right_best[j] != INF:
                ans = min(ans, left_best[j] + nums[j] + right_best[j])

        return -1 if ans == INF else ans
```

Attempt 6
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left_min[j] = minimum nums[i] with i<j and nums[i] < nums[j]
        left_min = [INF] * n
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if nums[i] < left_min[j]:
                        left_min[j] = nums[i]

        # right_min[j] = minimum nums[k] with k>j and nums[k] < nums[j]
        right_min = [INF] * n
        for j in range(n):
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    if nums[k] < right_min[j]:
                        right_min[j] = nums[k]

        ans = INF
        for j in range(n):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```

Attempt 7
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        # left_min[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        # right_min[j] = minimum nums[k] for k>j with nums[k] < nums[j]
        left_min = [INF] * n
        right_min = [INF] * n

        # Since nums[i] in [1..50], we can track minimum value seen for each number.
        left_best = [INF] * 51
        for j in range(n):
            x = nums[j]
            best = min(left_best[1:x]) if x > 1 else INF
            left_min[j] = best
            left_best[x] = min(left_best[x], x)

        right_best = [INF] * 51
        for j in range(n - 1, -1, -1):
            x = nums[j]
            best = min(right_best[1:x]) if x > 1 else INF
            right_min[j] = best
            right_best[x] = min(right_best[x], x)

        ans = INF
        for j in range(n):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```

Attempt 8
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        # Try each position j as the mountain peak.
        for j in range(1, n - 1):
            best_left = float('inf')   # min nums[i] with i < j and nums[i] < nums[j]
            best_right = float('inf')  # min nums[k] with k > j and nums[k] < nums[j]

            for i in range(j):
                if nums[i] < nums[j]:
                    best_left = min(best_left, nums[i])

            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    best_right = min(best_right, nums[k])

            if best_left != float('inf') and best_right != float('inf'):
                ans = min(ans, best_left + nums[j] + best_right)

        return -1 if ans == float('inf') else ans
```

Attempt 9
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left_min[j] = minimum value nums[i] for i<j with nums[i] < nums[j]
        # right_min[j] = minimum value nums[k] for k>j with nums[k] < nums[j]
        left_min = [INF] * n
        right_min = [INF] * n

        # Since nums[i] are in [1..50], we can use prefix/suffix minima by value.
        # Maintain best[v] = minimum nums[i] seen so far with value exactly v (or at least).
        # We'll query over values < nums[j].
        best_left = [INF] * 51
        for j in range(n):
            x = nums[j]
            left_best = INF
            for v in range(1, x):
                if best_left[v] < left_best:
                    left_best = best_left[v]
            left_min[j] = left_best
            best_left[x] = min(best_left[x], x)

        best_right = [INF] * 51
        for j in range(n - 1, -1, -1):
            x = nums[j]
            right_best = INF
            for v in range(1, x):
                if best_right[v] < right_best:
                    right_best = best_right[v]
            right_min[j] = right_best
            best_right[x] = min(best_right[x], x)

        ans = INF
        for j in range(1, n - 1):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```

#### Partially Correct
Attempt 1
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # best_left[v] = minimum value nums[i] with i < j and nums[i] == v
        best_left = [INF] * 51
        # We'll scan j from left to right, keeping best_left for nums[i] < nums[j].
        # For the right side, for each j we need min nums[k] for k > j with nums[k] < nums[j].
        # Precompute right_min_smaller[j][?] efficiently via suffix minima by value.
        # Since values are in [1,50], we can compute right_min[v] = minimum nums[k] to the right with nums[k] == v.
        right_min = [INF] * 51

        # Initialize suffix mins for k > j with j at 1 (we'll update as j moves).
        # Easier: maintain right_min for indices strictly greater than current j.
        # Start with last element as part of suffix, then adjust.
        right_min = [INF] * 51
        for idx in range(2, n):  # indices > 1
            right_min[nums[idx]] = min(right_min[nums[idx]], nums[idx])

        def min_suffix_smaller(val: int) -> int:
            # minimal value among right_min[x] for x < val
            m = INF
            # values range 1..50
            for x in range(1, val):
                if right_min[x] < m:
                    m = right_min[x]
            return m

        # Now iterate j from 1 to n-2
        for j in range(1, n - 1):
            vj = nums[j]

            left_smaller = INF
            for x in range(1, vj):
                left_smaller = min(left_smaller, best_left[x])

            right_smaller = min_suffix_smaller(vj)

            if left_smaller != INF and right_smaller != INF:
                ans = min(ans, left_smaller + vj + right_smaller)

            # Move j forward:
            # Current j becomes part of left for future iterations, and part of suffix for past ones.
            # Update best_left with nums[j]
            best_left[vj] = min(best_left[vj], vj)

            # Update suffix minima: remove index j+1? Our suffix currently represents indices > j.
            # We built initial suffix for j=1 as indices 2..n-1.
            # Before next iteration (j+1), suffix should represent indices > (j+1), i.e., indices j+2..n-1.
            # So we need to "remove" nums[j+1] from right_min, but we only stored minima by value,
            # which can't be removed easily.
            #
            # Instead, do a value-based DP without removals: precompute for each position j
            # the minimum value to the right that is < nums[j] using suffix arrays.
            #
            # Hence, break and switch to precomputed approach.

        # Recompute properly using precomputed suffix minima by value.
        # values are small (1..50), so do O(n*50) which is fine for n<=50.

        # left_best_min[v] while scanning
        ans = INF
        best_left = [INF] * 51

        # Precompute for each position j:
        # right_best_smaller[j] = min nums[k] for k>j with nums[k] < nums[j]
        right_best = [INF] * 51
        right_best_smaller = [INF] * n

        # Build suffix counts/minima
        for j in range(n - 2, -1, -1):
            v = nums[j + 1]
            right_best[v] = min(right_best[v], v)
            # query for position j
            cur = nums[j]
            m = INF
            for x in range(1, cur):
                m = min(m, right_best[x])
            right_best_smaller[j] = m

        for j in range(1, n - 1):
            vj = nums[j]
            left_min = INF
            for x in range(1, vj):
                left_min = min(left_min, best_left[x])
            right_min = right_best_smaller[j]
            if left_min != INF and right_min != INF:
                ans = min(ans, left_min + vj + right_min)
            best_left[vj] = min(best_left[vj], vj)

        return -1 if ans == INF else ans
```


## Response format
First write your analysis inside <reasoning> tags, then produce one or more memory items.
Each memory item must be a self-contained, generalizable insight that transfers to other problems.
A good memory reads like a reusable principle; a bad memory reads like a hint for one specific problem.
Each memory item must use this schema:
- "title": a short label for the memory item
- "description": one sentence summary of the memory item
- "content": 1-3 sentences describing the insight learned for successfully accomplishing similar tasks

<reasoning>Think about why certain attempts succeeded and others failed. What patterns distinguish them?</reasoning>

<memories>
<memory>
<title>The title of the memory item</title>
<description>One sentence summary of the memory item.</description>
<content>One to three sentences describing the reusable insight learned from the comparison.</content>
</memory>
<memory>
<title>Another distinct reusable principle</title>
<description>One sentence summary of the second memory item.</description>
<content>One to three sentences describing the second reusable insight.</content>
</memory>
</memories>
```

### Grouped Solutions

#### Tier: `full`

<details>
<summary>full attempt 1</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # min_left[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        # min_right[k] = minimum nums[k] for k>j with nums[k] < nums[j]
        min_left = [INF] * n
        min_seen = [INF] * 51  # values are in [1..50]
        
        for j in range(n):
            v = nums[j]
            if v > 1:
                min_left[j] = min(min_seen[1:v])  # min nums[i] < v
            min_seen[v] = min(min_seen[v], v)

        min_right = [INF] * n
        min_seen = [INF] * 51
        for j in range(n - 1, -1, -1):
            v = nums[j]
            if v > 1:
                min_right[j] = min(min_seen[1:v])  # min nums[k] < v to the right
            min_seen[v] = min(min_seen[v], v)

        for j in range(n):
            if min_left[j] != INF and min_right[j] != INF:
                total = min_left[j] + nums[j] + min_right[j]
                if total < ans:
                    ans = total

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left_min[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        left_min = [INF] * n
        best = INF

        # Precompute left_min
        for j in range(n):
            x = nums[j]
            mn = INF
            for i in range(j):
                if nums[i] < x:
                    mn = min(mn, nums[i])
            left_min[j] = mn

        # For each middle j, find minimum nums[k] for k>j with nums[k] < nums[j]
        for j in range(1, n - 1):
            if left_min[j] == INF:
                continue
            x = nums[j]
            mn_right = INF
            for k in range(j + 1, n):
                if nums[k] < x:
                    mn_right = min(mn_right, nums[k])
            if mn_right != INF:
                best = min(best, left_min[j] + x + mn_right)

        return -1 if best == INF else best
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # bestL[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        bestL = [INF] * n
        # bestR[j] = minimum nums[k] for k>j with nums[k] < nums[j]
        bestR = [INF] * n

        # nums[i] are in [1..50], so use Fenwick-like min prefix by value.
        # For each possible value v, store the minimum seen index/value that equals v.
        # We can just track minimum numbers by value; then query all < nums[j].
        maxv = 50
        min_by_val = [INF] * (maxv + 1)

        # Compute bestL
        for j in range(n):
            x = nums[j]
            # query min_by_val[1..x-1]
            mn = INF
            for v in range(1, x):
                if min_by_val[v] < mn:
                    mn = min_by_val[v]
            bestL[j] = mn
            if nums[j] < min_by_val[x]:
                min_by_val[x] = nums[j]

        # Compute bestR (from right)
        min_by_val = [INF] * (maxv + 1)
        for j in range(n - 1, -1, -1):
            x = nums[j]
            mn = INF
            for v in range(1, x):
                if min_by_val[v] < mn:
                    mn = min_by_val[v]
            bestR[j] = mn
            if nums[j] < min_by_val[x]:
                min_by_val[x] = nums[j]

        ans = INF
        for j in range(n):
            if bestL[j] < INF and bestR[j] < INF:
                ans = min(ans, bestL[j] + nums[j] + bestR[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9

        # min_left[j] = minimum nums[i] such that i < j and nums[i] < nums[j]
        min_left = [INF] * n
        for j in range(n):
            best = INF
            for i in range(j):
                if nums[i] < nums[j]:
                    best = min(best, nums[i])
            min_left[j] = best

        # min_right[j] = minimum nums[k] such that k > j and nums[k] < nums[j]
        min_right = [INF] * n
        for j in range(n - 1, -1, -1):
            best = INF
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    best = min(best, nums[k])
            min_right[j] = best

        ans = INF
        for j in range(n):
            if min_left[j] != INF and min_right[j] != INF:
                ans = min(ans, min_left[j] + nums[j] + min_right[j])

        return ans if ans != INF else -1
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF

        # left_best[j]: minimum possible nums[i] for i<j with nums[i] < nums[j]
        # right_best[j]: minimum possible nums[k] for k>j with nums[k] < nums[j]
        left_best = [INF] * n
        right_best = [INF] * n

        # Values are in [1..50], so we can use frequency-less min tracking.
        left_min_by_val = [INF] * 51  # left_min_by_val[v] = min nums[i] encountered with nums[i] == v

        for j in range(n):
            v = nums[j]
            # best among values < v
            best = INF
            for x in range(1, v):
                if left_min_by_val[x] < best:
                    best = left_min_by_val[x]
            left_best[j] = best

            # update encountered value v
            if nums[j] < left_min_by_val[v]:
                left_min_by_val[v] = nums[j]

        right_min_by_val = [INF] * 51
        for j in range(n - 1, -1, -1):
            v = nums[j]
            best = INF
            for x in range(1, v):
                if right_min_by_val[x] < best:
                    best = right_min_by_val[x]
            right_best[j] = best

            if nums[j] < right_min_by_val[v]:
                right_min_by_val[v] = nums[j]

        for j in range(1, n - 1):
            if left_best[j] != INF and right_best[j] != INF:
                ans = min(ans, left_best[j] + nums[j] + right_best[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left_min[j] = minimum nums[i] with i<j and nums[i] < nums[j]
        left_min = [INF] * n
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if nums[i] < left_min[j]:
                        left_min[j] = nums[i]

        # right_min[j] = minimum nums[k] with k>j and nums[k] < nums[j]
        right_min = [INF] * n
        for j in range(n):
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    if nums[k] < right_min[j]:
                        right_min[j] = nums[k]

        ans = INF
        for j in range(n):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        # left_min[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        # right_min[j] = minimum nums[k] for k>j with nums[k] < nums[j]
        left_min = [INF] * n
        right_min = [INF] * n

        # Since nums[i] in [1..50], we can track minimum value seen for each number.
        left_best = [INF] * 51
        for j in range(n):
            x = nums[j]
            best = min(left_best[1:x]) if x > 1 else INF
            left_min[j] = best
            left_best[x] = min(left_best[x], x)

        right_best = [INF] * 51
        for j in range(n - 1, -1, -1):
            x = nums[j]
            best = min(right_best[1:x]) if x > 1 else INF
            right_min[j] = best
            right_best[x] = min(right_best[x], x)

        ans = INF
        for j in range(n):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        # Try each position j as the mountain peak.
        for j in range(1, n - 1):
            best_left = float('inf')   # min nums[i] with i < j and nums[i] < nums[j]
            best_right = float('inf')  # min nums[k] with k > j and nums[k] < nums[j]

            for i in range(j):
                if nums[i] < nums[j]:
                    best_left = min(best_left, nums[i])

            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    best_right = min(best_right, nums[k])

            if best_left != float('inf') and best_right != float('inf'):
                ans = min(ans, best_left + nums[j] + best_right)

        return -1 if ans == float('inf') else ans
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left_min[j] = minimum value nums[i] for i<j with nums[i] < nums[j]
        # right_min[j] = minimum value nums[k] for k>j with nums[k] < nums[j]
        left_min = [INF] * n
        right_min = [INF] * n

        # Since nums[i] are in [1..50], we can use prefix/suffix minima by value.
        # Maintain best[v] = minimum nums[i] seen so far with value exactly v (or at least).
        # We'll query over values < nums[j].
        best_left = [INF] * 51
        for j in range(n):
            x = nums[j]
            left_best = INF
            for v in range(1, x):
                if best_left[v] < left_best:
                    left_best = best_left[v]
            left_min[j] = left_best
            best_left[x] = min(best_left[x], x)

        best_right = [INF] * 51
        for j in range(n - 1, -1, -1):
            x = nums[j]
            right_best = INF
            for v in range(1, x):
                if best_right[v] < right_best:
                    right_best = best_right[v]
            right_min[j] = right_best
            best_right[x] = min(best_right[x], x)

        ans = INF
        for j in range(1, n - 1):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

#### Tier: `partial`

<details>
<summary>partial attempt 1</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # best_left[v] = minimum value nums[i] with i < j and nums[i] == v
        best_left = [INF] * 51
        # We'll scan j from left to right, keeping best_left for nums[i] < nums[j].
        # For the right side, for each j we need min nums[k] for k > j with nums[k] < nums[j].
        # Precompute right_min_smaller[j][?] efficiently via suffix minima by value.
        # Since values are in [1,50], we can compute right_min[v] = minimum nums[k] to the right with nums[k] == v.
        right_min = [INF] * 51

        # Initialize suffix mins for k > j with j at 1 (we'll update as j moves).
        # Easier: maintain right_min for indices strictly greater than current j.
        # Start with last element as part of suffix, then adjust.
        right_min = [INF] * 51
        for idx in range(2, n):  # indices > 1
            right_min[nums[idx]] = min(right_min[nums[idx]], nums[idx])

        def min_suffix_smaller(val: int) -> int:
            # minimal value among right_min[x] for x < val
            m = INF
            # values range 1..50
            for x in range(1, val):
                if right_min[x] < m:
                    m = right_min[x]
            return m

        # Now iterate j from 1 to n-2
        for j in range(1, n - 1):
            vj = nums[j]

            left_smaller = INF
            for x in range(1, vj):
                left_smaller = min(left_smaller, best_left[x])

            right_smaller = min_suffix_smaller(vj)

            if left_smaller != INF and right_smaller != INF:
                ans = min(ans, left_smaller + vj + right_smaller)

            # Move j forward:
            # Current j becomes part of left for future iterations, and part of suffix for past ones.
            # Update best_left with nums[j]
            best_left[vj] = min(best_left[vj], vj)

            # Update suffix minima: remove index j+1? Our suffix currently represents indices > j.
            # We built initial suffix for j=1 as indices 2..n-1.
            # Before next iteration (j+1), suffix should represent indices > (j+1), i.e., indices j+2..n-1.
            # So we need to "remove" nums[j+1] from right_min, but we only stored minima by value,
            # which can't be removed easily.
            #
            # Instead, do a value-based DP without removals: precompute for each position j
            # the minimum value to the right that is < nums[j] using suffix arrays.
            #
            # Hence, break and switch to precomputed approach.

        # Recompute properly using precomputed suffix minima by value.
        # values are small (1..50), so do O(n*50) which is fine for n<=50.

        # left_best_min[v] while scanning
        ans = INF
        best_left = [INF] * 51

        # Precompute for each position j:
        # right_best_smaller[j] = min nums[k] for k>j with nums[k] < nums[j]
        right_best = [INF] * 51
        right_best_smaller = [INF] * n

        # Build suffix counts/minima
        for j in range(n - 2, -1, -1):
            v = nums[j + 1]
            right_best[v] = min(right_best[v], v)
            # query for position j
            cur = nums[j]
            m = INF
            for x in range(1, cur):
                m = min(m, right_best[x])
            right_best_smaller[j] = m

        for j in range(1, n - 1):
            vj = nums[j]
            left_min = INF
            for x in range(1, vj):
                left_min = min(left_min, best_left[x])
            right_min = right_best_smaller[j]
            if left_min != INF and right_min != INF:
                ans = min(ans, left_min + vj + right_min)
            best_left[vj] = min(best_left[vj], vj)

        return -1 if ans == INF else ans
```
```

</details>

### Parsed Memory Items

1. Peak-First Decomposition
Description: Reformulate a constrained triplet search by fixing the “peak” and solving left/right feasibility independently.
<details>
<summary>Content 1</summary>

```text
When a condition depends on a middle index with symmetric inequalities (e.g., both sides must be less than the peak), iterate over the middle position and compute the best possible left and right contributions separately. This converts a 3D search into repeated 1D subproblems and makes correctness easier to reason about.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
Successful attempts shared a clean decomposition: choose the peak position and then reduce the mountain condition to independently selecting the minimum feasible left value and minimum feasible right value that are strictly smaller than the peak. They also matched representation to constraints: because values are small and n is small, using value-indexed minima (or simple O(n·V) scans) is safe and avoids missing candidates. Unsuccessful/partially correct attempts typically failed due to an incorrect incremental-maintenance idea—especially around “removing” elements from a suffix structure when the split point moves—leading to stale data that no longer corresponds to the required index ranges. This highlights the importance of either precomputing per-split suffix information or using a data structure that correctly supports deletions (or monotone updates) before relying on it.
```

</details>

2. Use Value-Indexed Minima for Small Domains
Description: Match your algorithm’s state representation to small numeric bounds by storing minima by value.
<details>
<summary>Content 2</summary>

```text
If elements fall within a small range, maintain arrays keyed by value that store the minimum seen number for each value, and query over “all values less than v” to enforce strict inequalities. This avoids complex data structures and reduces the chance of missing candidates compared with ad-hoc bookkeeping.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
Successful attempts shared a clean decomposition: choose the peak position and then reduce the mountain condition to independently selecting the minimum feasible left value and minimum feasible right value that are strictly smaller than the peak. They also matched representation to constraints: because values are small and n is small, using value-indexed minima (or simple O(n·V) scans) is safe and avoids missing candidates. Unsuccessful/partially correct attempts typically failed due to an incorrect incremental-maintenance idea—especially around “removing” elements from a suffix structure when the split point moves—leading to stale data that no longer corresponds to the required index ranges. This highlights the importance of either precomputing per-split suffix information or using a data structure that correctly supports deletions (or monotone updates) before relying on it.
```

</details>

3. Beware of Sliding Split “Removal” Bugs
Description: Don’t incrementally reuse prefix/suffix aggregates if you can’t correctly “remove” items when the split point moves.
<details>
<summary>Content 3</summary>

```text
Partially correct attempts showed that maintaining a suffix structure while shifting the boundary can silently invalidate the index constraint unless deletions are handled exactly. Prefer recomputation/precomputation per boundary, or use a data structure that supports correct updates for the moving window/split.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
Successful attempts shared a clean decomposition: choose the peak position and then reduce the mountain condition to independently selecting the minimum feasible left value and minimum feasible right value that are strictly smaller than the peak. They also matched representation to constraints: because values are small and n is small, using value-indexed minima (or simple O(n·V) scans) is safe and avoids missing candidates. Unsuccessful/partially correct attempts typically failed due to an incorrect incremental-maintenance idea—especially around “removing” elements from a suffix structure when the split point moves—leading to stale data that no longer corresponds to the required index ranges. This highlights the importance of either precomputing per-split suffix information or using a data structure that correctly supports deletions (or monotone updates) before relying on it.
```

</details>

4. Validate Against Original Constraints After Optimizations
Description: After any optimization (e.g., compressing state or using minima over values), re-check that it still enforces both index-order and strict comparison constraints.
<details>
<summary>Content 4</summary>

```text
Even when the computed minima are correct by value, they may correspond to the wrong side of the split if the aggregate is stale. Add a verification mindset: ensure the left candidate index is strictly before the peak and the right candidate index is strictly after the peak, not just that values satisfy the inequality.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
Successful attempts shared a clean decomposition: choose the peak position and then reduce the mountain condition to independently selecting the minimum feasible left value and minimum feasible right value that are strictly smaller than the peak. They also matched representation to constraints: because values are small and n is small, using value-indexed minima (or simple O(n·V) scans) is safe and avoids missing candidates. Unsuccessful/partially correct attempts typically failed due to an incorrect incremental-maintenance idea—especially around “removing” elements from a suffix structure when the split point moves—leading to stale data that no longer corresponds to the required index ranges. This highlights the importance of either precomputing per-split suffix information or using a data structure that correctly supports deletions (or monotone updates) before relying on it.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
Successful attempts shared a clean decomposition: choose the peak position and then reduce the mountain condition to independently selecting the minimum feasible left value and minimum feasible right value that are strictly smaller than the peak. They also matched representation to constraints: because values are small and n is small, using value-indexed minima (or simple O(n·V) scans) is safe and avoids missing candidates. Unsuccessful/partially correct attempts typically failed due to an incorrect incremental-maintenance idea—especially around “removing” elements from a suffix structure when the split point moves—leading to stale data that no longer corresponds to the required index ranges. This highlights the importance of either precomputing per-split suffix information or using a data structure that correctly supports deletions (or monotone updates) before relying on it.
</reasoning>

<memories>
<memory>
<title>Peak-First Decomposition</title>
<description>Reformulate a constrained triplet search by fixing the “peak” and solving left/right feasibility independently.</description>
<content>When a condition depends on a middle index with symmetric inequalities (e.g., both sides must be less than the peak), iterate over the middle position and compute the best possible left and right contributions separately. This converts a 3D search into repeated 1D subproblems and makes correctness easier to reason about.</content>
</memory>

<memory>
<title>Use Value-Indexed Minima for Small Domains</title>
<description>Match your algorithm’s state representation to small numeric bounds by storing minima by value.</description>
<content>If elements fall within a small range, maintain arrays keyed by value that store the minimum seen number for each value, and query over “all values less than v” to enforce strict inequalities. This avoids complex data structures and reduces the chance of missing candidates compared with ad-hoc bookkeeping.</content>
</memory>

<memory>
<title>Beware of Sliding Split “Removal” Bugs</title>
<description>Don’t incrementally reuse prefix/suffix aggregates if you can’t correctly “remove” items when the split point moves.</description>
<content>Partially correct attempts showed that maintaining a suffix structure while shifting the boundary can silently invalidate the index constraint unless deletions are handled exactly. Prefer recomputation/precomputation per boundary, or use a data structure that supports correct updates for the moving window/split.</content>
</memory>

<memory>
<title>Validate Against Original Constraints After Optimizations</title>
<description>After any optimization (e.g., compressing state or using minima over values), re-check that it still enforces both index-order and strict comparison constraints.</description>
<content>Even when the computed minima are correct by value, they may correspond to the wrong side of the split if the aggregate is stale. Add a verification mindset: ensure the left candidate index is strictly before the peak and the right candidate index is strictly after the peak, not just that values satisfy the inequality.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `1.0000`
- Augmented pass@1: `1.0000`
- Improvement: `+0.0000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
You are given a 0-indexed array nums of integers.
A triplet of indices (i, j, k) is a mountain if:

i < j < k
nums[i] < nums[j] and nums[k] < nums[j]

Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.
 
Example 1:

Input: nums = [8,6,1,5,3]
Output: 9
Explanation: Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
- 2 < 3 < 4
- nums[2] < nums[3] and nums[4] < nums[3]
And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.

Example 2:

Input: nums = [5,4,8,7,10,2]
Output: 13
Explanation: Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
- 1 < 3 < 5
- nums[1] < nums[3] and nums[5] < nums[3]
And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.

Example 3:

Input: nums = [6,5,4,3,4,5]
Output: -1
Explanation: It can be shown that there are no mountain triplets in nums.

 
Constraints:

3 <= nums.length <= 50
1 <= nums[i] <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18

        # left_smaller[j] = min nums[i] with i<j and nums[i] < nums[j]
        left_smaller = [INF] * n
        best = [INF] * 51  # values are in [1..50]
        for j in range(n):
            v = nums[j]
            # smallest value among < v
            mn = INF
            for x in range(1, v):
                if best[x] < mn:
                    mn = best[x]
            left_smaller[j] = mn
            best[v] = min(best[v], nums[j])

        # right_smaller[j] = min nums[k] with k>j and nums[k] < nums[j]
        right_smaller = [INF] * n
        best = [INF] * 51
        for j in range(n - 1, -1, -1):
            v = nums[j]
            mn = INF
            for x in range(1, v):
                if best[x] < mn:
                    mn = best[x]
            right_smaller[j] = mn
            best[v] = min(best[v], nums[j])

        ans = INF
        for j in range(n):
            a = left_smaller[j]
            c = right_smaller[j]
            if a != INF and c != INF:
                s = a + nums[j] + c
                if s < ans:
                    ans = s

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # left[j][v] means minimum nums[i] with i<j and nums[i]=v, but since values are 1..50
        # We'll store minimum value strictly less than nums[j] directly.
        best_left = [INF] * n   # best_left[j] = min nums[i] for i<j and nums[i] < nums[j]
        best_right = [INF] * n # best_right[j] = min nums[k] for k>j and nums[k] < nums[j]

        # Values are small (<=50), so we can track minima by value.
        MAXV = 50
        min_by_val = [INF] * (MAXV + 1)

        for j in range(n):
            # compute best_left[j]
            mj = nums[j]
            mn = INF
            for v in range(1, mj):
                if min_by_val[v] < mn:
                    mn = min_by_val[v]
            best_left[j] = mn
            # update
            if nums[j] < min_by_val[nums[j]]:
                min_by_val[nums[j]] = nums[j]

        min_by_val = [INF] * (MAXV + 1)
        for j in range(n - 1, -1, -1):
            mj = nums[j]
            mn = INF
            for v in range(1, mj):
                if min_by_val[v] < mn:
                    mn = min_by_val[v]
            best_right[j] = mn
            if nums[j] < min_by_val[nums[j]]:
                min_by_val[nums[j]] = nums[j]

        ans = INF
        for j in range(1, n - 1):
            if best_left[j] != INF and best_right[j] != INF:
                s = best_left[j] + nums[j] + best_right[j]
                if s < ans:
                    ans = s

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # For each position j, we need:
        # left: max index i < j with nums[i] < nums[j] and minimal nums[i]
        # right: min index k > j with nums[k] < nums[j] and minimal nums[k]
        # But minimizing sum nums[i] + nums[j] + nums[k] for fixed j means:
        # - choose the smallest possible nums[i] (< nums[j]) among i<j
        # - choose the smallest possible nums[k] (< nums[j]) among k>j
        #
        # We compute minimal value on the left for each threshold, and similarly on the right.
        # Since nums[i] in [1..50], we can use frequency/min arrays.
        
        # left_min_less[v] = minimum nums[i] seen so far (i<current j) with nums[i] < v
        left_min_less = [INF] * 51

        # Initialize left info as we sweep j from left to right
        # We'll maintain counts/mins by value, then query min for < v.
        left_seen_min = [INF] * 51  # left_seen_min[val] = min of val seen

        # Precompute right similarly, then do one pass for j in the middle.
        right_seen_min = [INF] * 51
        # Build from right for k > j on demand by precomputing suffix minima by value.
        # We'll build suffix minima of values for each position:
        # suffix_min_value_at_pos[pos][val] is too heavy; instead we can maintain array
        # of minima by value and update as we move j.
        # We'll start with empty to the right, then update by adding nums[j+1] as j moves.

        # Setup: initially, right side includes indices > 1 (we'll update in loop)
        # We'll build a suffix structure: right_seen_min for values occurring in indices > current j
        for v in nums[2:]:
            if v < right_seen_min[v]:
                right_seen_min[v] = v

        def query_min_seen_less(seen_min, v):
            # minimum seen among values < v
            best = INF
            # values are small (<=50), so linear scan is fine
            for x in range(1, v):
                if seen_min[x] < best:
                    best = seen_min[x]
            return best

        # Sweep j from 1 to n-2 (mountain peak must be middle)
        # We need i<j and k>j
        for j in range(1, n - 1):
            # Ensure right structure represents indices k > j
            # Currently right includes nums[j+1..n-1] because we started with nums[2:]
            # For j=1 right should include 2..n-1 => correct.
            # After processing j, we remove nums[j+1] from right by rebuilding isn't easy.
            # So instead, do it with prefix/suffix preprocessing for simplicity.

            pass

        # The above approach got complicated; use DP-like prefix/suffix minima by value
        # Precompute for each position j:
        # left_best[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        # right_best[j] = minimum nums[k] for k>j with nums[k] < nums[j]
        # Answer is min over j of nums[j] + left_best[j] + right_best[j].
        
        left_best = [INF] * n
        right_best = [INF] * n

        # Compute left_best
        seen_min = [INF] * 51
        for j in range(n):
            # Query for nums[j]
            v = nums[j]
            best = INF
            for x in range(1, v):
                if seen_min[x] < best:
                    best = seen_min[x]
            if j > 0:
                left_best[j] = best
            # Update seen_min with nums[j]
            if nums[j] < seen_min[nums[j]]:
                seen_min[nums[j]] = nums[j]

        # Compute right_best
        seen_min = [INF] * 51
        for j in range(n - 1, -1, -1):
            v = nums[j]
            best = INF
            for x in range(1, v):
                if seen_min[x] < best:
                    best = seen_min[x]
            if j < n - 1:
                right_best[j] = best
            if nums[j] < seen_min[nums[j]]:
                seen_min[nums[j]] = nums[j]

        for j in range(1, n - 1):
            if left_best[j] != INF and right_best[j] != INF:
                s = left_best[j] + nums[j] + right_best[j]
                if s < ans:
                    ans = s

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF

        # left_min[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        # right_min[j] = minimum nums[k] for k>j with nums[k] < nums[j]
        left_min = [INF] * n
        right_min = [INF] * n

        # nums[i] values are in [1..50], so we can use arrays of size 51
        best_left = [INF] * 51
        for j in range(n):
            x = nums[j]
            # best_left[t] holds minimum value seen so far with value exactly t
            # we need minimum among t < x
            left_min[j] = min(best_left[:x]) if x > 1 else INF
            # update after computing for current j
            if nums[j] < best_left[x]:
                best_left[x] = nums[j]

        best_right = [INF] * 51
        for j in range(n - 1, -1, -1):
            x = nums[j]
            right_min[j] = min(best_right[:x]) if x > 1 else INF
            if nums[j] < best_right[x]:
                best_right[x] = nums[j]

        for j in range(n):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF

        # For each position j as the peak, we need:
        # - best left i (<j) with nums[i] < nums[j] having minimum nums[i]
        # - best right k (>j) with nums[k] < nums[j] having minimum nums[k]
        left_min = [INF] * n
        right_min = [INF] * n

        # Left: scan j from left to right, maintain minimum value seen for each value threshold.
        # Since nums[i] in [1..50], we can do O(50*n).
        best = [INF] * 51  # best[v] = min number seen with value == v
        for j in range(n):
            vj = nums[j]
            # min nums[i] < vj => min over values 1..vj-1
            if vj > 1:
                m = min(best[1:vj])
                left_min[j] = m
            # update best with nums[j]
            best[vj] = min(best[vj], nums[j])

        # Right: scan right to left
        best = [INF] * 51
        for j in range(n - 1, -1, -1):
            vj = nums[j]
            if vj > 1:
                m = min(best[1:vj])
                right_min[j] = m
            best[vj] = min(best[vj], nums[j])

        # Try each peak j that can have both sides
        for j in range(1, n - 1):
            if left_min[j] < INF and right_min[j] < INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF

        # bestL[j] = minimum nums[i] for i<j with nums[i] < nums[j]
        bestL = [INF] * n
        # For each value, keep the minimum index-value seen so far
        minValSeen = [INF] * 51  # nums[i] in [1..50]
        for j in range(n):
            x = nums[j]
            min_left = min(minValSeen[1:x]) if x > 1 else INF
            bestL[j] = min_left
            if nums[j] < minValSeen[x]:
                minValSeen[x] = nums[j]

        # bestR[j] = minimum nums[k] for k>j with nums[k] < nums[j]
        bestR = [INF] * n
        minValSeen = [INF] * 51
        for j in range(n - 1, -1, -1):
            x = nums[j]
            min_right = min(minValSeen[1:x]) if x > 1 else INF
            bestR[j] = min_right
            if nums[j] < minValSeen[x]:
                minValSeen[x] = nums[j]

        for j in range(n):
            if bestL[j] != INF and bestR[j] != INF:
                ans = min(ans, bestL[j] + nums[j] + bestR[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9

        # left_min[j] = minimum nums[i] for i<j with nums[i] < nums[j], else INF
        left_min = [INF] * n
        for j in range(n):
            best = INF
            for i in range(j):
                if nums[i] < nums[j]:
                    best = min(best, nums[i])
            left_min[j] = best

        # right_min[j] = minimum nums[k] for k>j with nums[k] < nums[j], else INF
        right_min = [INF] * n
        for j in range(n):
            best = INF
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    best = min(best, nums[k])
            right_min[j] = best

        ans = INF
        for j in range(1, n - 1):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF

        # best_left[j] = minimum possible nums[i] for i<j with nums[i] < nums[j]
        best_left = [INF] * n
        for j in range(n):
            bj = nums[j]
            for i in range(j):
                if nums[i] < bj:
                    best_left[j] = min(best_left[j], nums[i])

        # For each possible peak j, find minimum nums[k] for k>j with nums[k] < nums[j]
        for j in range(1, n - 1):
            bj = nums[j]
            left_min = best_left[j]
            if left_min == INF:
                continue
            right_min = INF
            for k in range(j + 1, n):
                if nums[k] < bj:
                    right_min = min(right_min, nums[k])
            if right_min != INF:
                ans = min(ans, left_min + bj + right_min)

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF

        # left_min[j] = minimum nums[i] with i<j and nums[i] < nums[j]
        # right_min[j] = minimum nums[k] with k>j and nums[k] < nums[j]
        left_min = [INF] * n
        right_min = [INF] * n

        # Since nums[i] in [1..50], we can keep minima per value for speed.
        # For left_min, we need min value among those < nums[j].
        left_best = [INF] * 51
        for j in range(n):
            val = nums[j]
            m = INF
            for x in range(1, val):
                if left_best[x] < m:
                    m = left_best[x]
            left_min[j] = m
            # Update best for this value
            if val < left_best[val]:
                left_best[val] = val

        right_best = [INF] * 51
        for j in range(n - 1, -1, -1):
            val = nums[j]
            m = INF
            for x in range(1, val):
                if right_best[x] < m:
                    m = right_best[x]
            right_min[j] = m
            if val < right_best[val]:
                right_best[val] = val

        # Choose middle j, sum of smallest possible left and right under nums[j]
        for j in range(1, n - 1):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        ans = INF

        # left_min[j] = minimum nums[i] with i < j and nums[i] < nums[j]
        left_min = [INF] * n
        best = [INF] * 51  # values are 1..50
        for j in range(n):
            left_min[j] = min(best[:nums[j]]) if nums[j] > 1 else INF
            best[nums[j]] = min(best[nums[j]], nums[j])

        # right_min[k] = minimum nums[k] with k > j and nums[k] < nums[j]
        right_min = [INF] * n
        best = [INF] * 51
        for j in range(n - 1, -1, -1):
            right_min[j] = min(best[:nums[j]]) if nums[j] > 1 else INF
            best[nums[j]] = min(best[nums[j]], nums[j])

        for j in range(n):
            if left_min[j] != INF and right_min[j] != INF:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])

        return -1 if ans == INF else ans
```
```

</details>

#### Baseline Scores

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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    }
  ]
}
```

</details>

### Augmented

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
Before solving, consider these reusable insights from prior analysis:

  1. Peak-First Decomposition: Reformulate a constrained triplet search by fixing the “peak” and solving left/right feasibility independently.
     When a condition depends on a middle index with symmetric inequalities (e.g., both sides must be less than the peak), iterate over the middle position and compute the best possible left and right contributions separately. This converts a 3D search into repeated 1D subproblems and makes correctness easier to reason about.
  2. Use Value-Indexed Minima for Small Domains: Match your algorithm’s state representation to small numeric bounds by storing minima by value.
     If elements fall within a small range, maintain arrays keyed by value that store the minimum seen number for each value, and query over “all values less than v” to enforce strict inequalities. This avoids complex data structures and reduces the chance of missing candidates compared with ad-hoc bookkeeping.
  3. Beware of Sliding Split “Removal” Bugs: Don’t incrementally reuse prefix/suffix aggregates if you can’t correctly “remove” items when the split point moves.
     Partially correct attempts showed that maintaining a suffix structure while shifting the boundary can silently invalidate the index constraint unless deletions are handled exactly. Prefer recomputation/precomputation per boundary, or use a data structure that supports correct updates for the moving window/split.
  4. Validate Against Original Constraints After Optimizations: After any optimization (e.g., compressing state or using minima over values), re-check that it still enforces both index-order and strict comparison constraints.
     Even when the computed minima are correct by value, they may correspond to the wrong side of the split if the aggregate is stale. Add a verification mindset: ensure the left candidate index is strictly before the peak and the right candidate index is strictly after the peak, not just that values satisfy the inequality.

Apply these insights to the problem below.

### Question:
You are given a 0-indexed array nums of integers.
A triplet of indices (i, j, k) is a mountain if:

i < j < k
nums[i] < nums[j] and nums[k] < nums[j]

Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.
 
Example 1:

Input: nums = [8,6,1,5,3]
Output: 9
Explanation: Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
- 2 < 3 < 4
- nums[2] < nums[3] and nums[4] < nums[3]
And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.

Example 2:

Input: nums = [5,4,8,7,10,2]
Output: 13
Explanation: Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
- 1 < 3 < 5
- nums[1] < nums[3] and nums[5] < nums[3]
And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.

Example 3:

Input: nums = [6,5,4,3,4,5]
Output: -1
Explanation: It can be shown that there are no mountain triplets in nums.

 
Constraints:

3 <= nums.length <= 50
1 <= nums[i] <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Augmented generation 1</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        # Peak-first decomposition:
        # Fix j as the mountain peak (the middle index).
        # Need i<j with nums[i] < nums[j] and k>j with nums[k] < nums[j].
        # Minimize nums[i] + nums[j] + nums[k] for each j.
        ans = INF

        for j in range(1, n - 1):
            peak = nums[j]

            # Left: best (minimum value) nums[i] where i<j and nums[i] < peak
            left_best = INF
            for i in range(j):
                if nums[i] < peak:
                    if nums[i] < left_best:
                        left_best = nums[i]

            if left_best == INF:
                continue

            # Right: best (minimum value) nums[k] where k>j and nums[k] < peak
            right_best = INF
            for k in range(j + 1, n):
                if nums[k] < peak:
                    if nums[k] < right_best:
                        right_best = nums[k]

            if right_best == INF:
                continue

            ans = min(ans, left_best + peak + right_best)

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        # Precompute for each possible peak position j:
        # bestLeft[j]  = minimal nums[i] with i<j and nums[i] < nums[j]
        # bestRight[j] = minimal nums[k] with k>j and nums[k] < nums[j]
        # If either doesn't exist, no mountain with peak j.
        
        # Since nums[i] in [1,50], we can store minima by value (insight #2).
        # For strict inequality nums[x] < peakVal, we need min over values < peakVal.
        MAXV = 50
        INF = 10**18

        bestLeft = [INF] * n
        bestRight = [INF] * n

        # Left side minima
        min_by_val = [INF] * (MAXV + 1)
        for j in range(n):
            peak = nums[j]
            # query min for values < peak
            if peak > 1:
                ml = INF
                for v in range(1, peak):
                    if min_by_val[v] < ml:
                        ml = min_by_val[v]
                bestLeft[j] = ml
            # update with current value for future peaks
            val = nums[j]
            if nums[j] < min_by_val[val]:
                min_by_val[val] = nums[j]

        # Right side minima
        min_by_val = [INF] * (MAXV + 1)
        for j in range(n - 1, -1, -1):
            peak = nums[j]
            if peak > 1:
                mr = INF
                for v in range(1, peak):
                    if min_by_val[v] < mr:
                        mr = min_by_val[v]
                bestRight[j] = mr
            val = nums[j]
            if nums[j] < min_by_val[val]:
                min_by_val[val] = nums[j]

        ans = INF
        # Peak-first decomposition (insight #1):
        # For each j as the middle index, combine best left and right.
        for j in range(1, n - 1):
            if bestLeft[j] != INF and bestRight[j] != INF:
                s = bestLeft[j] + nums[j] + bestRight[j]
                if s < ans:
                    ans = s

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # Values are in [1, 50]
        MAXV = 50

        # For each possible peak position j, find:
        # - best (minimum) nums[i] with i<j and nums[i] < nums[j]
        # - best (minimum) nums[k] with k>j and nums[k] < nums[j]
        # Then minimize nums[i] + nums[j] + nums[k].
        # We'll use value-indexed minima for strict inequality by value.
        for j in range(1, n - 1):
            peak = nums[j]

            # leftBest = min nums[i] for i<j with nums[i] < peak
            leftBest = INF
            leftMinByVal = [INF] * (MAXV + 1)
            for i in range(j):
                v = nums[i]
                if v < peak and v <= MAXV:
                    leftMinByVal[v] = min(leftMinByVal[v], v)

            # Query over all values < peak
            for v in range(1, min(peak, MAXV + 1)):
                leftBest = min(leftBest, leftMinByVal[v])

            if leftBest == INF:
                continue

            # rightBest = min nums[k] for k>j with nums[k] < peak
            rightBest = INF
            rightMinByVal = [INF] * (MAXV + 1)
            for k in range(j + 1, n):
                v = nums[k]
                if v < peak and v <= MAXV:
                    rightMinByVal[v] = min(rightMinByVal[v], v)

            for v in range(1, min(peak, MAXV + 1)):
                rightBest = min(rightBest, rightMinByVal[v])

            if rightBest == INF:
                continue

            ans = min(ans, leftBest + peak + rightBest)

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # For each possible peak j, compute the minimum left contribution (i<j, nums[i] < nums[j])
        # and right contribution (k>j, nums[k] < nums[j]) independently.
        for j in range(1, n - 1):
            peak = nums[j]

            best_left = INF
            best_right = INF

            # Left: i < j and nums[i] < peak
            for i in range(0, j):
                if nums[i] < peak:
                    best_left = min(best_left, nums[i])

            # Right: k > j and nums[k] < peak
            for k in range(j + 1, n):
                if nums[k] < peak:
                    best_right = min(best_right, nums[k])

            if best_left != INF and best_right != INF:
                ans = min(ans, best_left + peak + best_right)

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)

        # Precompute best left index value for each peak position:
        # For each j, we want minimum nums[i] such that i<j and nums[i] < nums[j]
        left_best = [10**9] * n
        for j in range(n):
            best = 10**9
            threshold = nums[j]
            for i in range(j):
                if nums[i] < threshold:
                    best = min(best, nums[i])
            left_best[j] = best

        # For each j, want minimum nums[k] such that k>j and nums[k] < nums[j]
        right_best = [10**9] * n
        for j in range(n):
            best = 10**9
            threshold = nums[j]
            for k in range(j + 1, n):
                if nums[k] < threshold:
                    best = min(best, nums[k])
            right_best[j] = best

        ans = 10**18
        for j in range(1, n - 1):
            if left_best[j] != 10**9 and right_best[j] != 10**9:
                total = left_best[j] + nums[j] + right_best[j]
                if total < ans:
                    ans = total

        return -1 if ans == 10**18 else ans
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # Precompute for each value v (1..50) the minimum pair (value, index)
        # left_min[val] = smallest nums[i] among i<j with nums[i] == val (track by value)
        # But since we only need minima by value and strict inequality:
        # for each j as peak, we need:
        #  left: smallest nums[i] where i<j and nums[i] < nums[j]
        #  right: smallest nums[k] where k>j and nums[k] < nums[j]
        # We'll compute these with suffix minima-by-value and scanning i for prefix.
        maxv = 50

        # suffix_best[val] = minimum nums[k] among k>j with nums[k] == val
        suffix_best = [INF] * (maxv + 1)

        # Initialize suffix for j = 0 (i.e., k>0): build from index 1..n-1
        for k in range(1, n):
            v = nums[k]
            suffix_best[v] = min(suffix_best[v], v)

        def best_less_from_suffix(limit: int) -> int:
            # minimum nums[k] for k>current j with nums[k] < limit
            best = INF
            for vv in range(1, limit):
                if suffix_best[vv] < best:
                    best = suffix_best[vv]
            return best

        # prefix_best[val] = whether we've seen value val in i<j; we need min value itself,
        # so if any exists, minimum candidate value for that val is vv.
        # Because nums[i] == vv, the min value is vv.
        prefix_seen = [False] * (maxv + 1)

        for j in range(1, n - 1):  # middle index
            peak = nums[j]

            # Update prefix structure with i=j-1 element before evaluating this j
            left_val = nums[j - 1]
            prefix_seen[left_val] = True

            # Ensure suffix corresponds to k>j.
            # Currently suffix_best was built for k>0; we must remove nums[j] from suffix as j increases.
            # Since we update j from left to right, we should "remove" nums[j]" from suffix_best before using it.
            # For j=1, suffix_best includes indices 1..n-1; we need k>1, so remove nums[1] before query.
            # We'll handle this by updating/removing at the start of each iteration.
            # So do removal now:
            v_to_remove = nums[j]
            # Remove only if this value contributed; since suffix_best stores just min for that value (=value),
            # and values are positive, we need to know if any occurrence remains after j.
            # Given duplicates, we require counts. We'll instead use counts by value.
            # To keep it simple and safe for small constraints (n<=50, values<=50), we'll rebuild suffix_best via counts once.
            # But we already started; let's correct with counts approach properly.
            # We'll implement a correct counts-based suffix in a separate loop below.
            pass

        # Correct implementation with counts + value-index minima for strict inequality.

        # Build counts for suffix by value for each potential j
        counts_suffix = [0] * (maxv + 1)
        for k in range(2, n):
            counts_suffix[nums[k]] += 1

        def best_less_from_counts(counts: List[int], limit: int) -> int:
            best = INF
            for vv in range(1, limit):
                if counts[vv] > 0:
                    best = vv  # since value itself is candidate
                    break
            return best

        counts_prefix = [0] * (maxv + 1)
        # j ranges from 1..n-2; prefix includes indices < j, suffix includes indices > j
        # We'll maintain counts_prefix for indices < j, and counts_suffix for indices > j.
        for j in range(1, n - 1):
            # Add index j-1 to prefix
            counts_prefix[nums[j - 1]] += 1
            # Remove index j+1 from suffix? We'll manage suffix to be >j:
            # Initialize suffix as >1 (indices 2..n-1) when j=1. For each step, remove nums[j+1] after it becomes <=j.
            # We already set suffix counts for indices 2..n-1, which is correct for j=1.
            # So at each j, suffix counts represent indices > j.
            peak = nums[j]

            left_best = INF
            for vv in range(1, peak):
                if counts_prefix[vv] > 0:
                    left_best = vv
                    break

            right_best = INF
            for vv in range(1, peak):
                if counts_suffix[vv] > 0:
                    right_best = vv
                    break

            if left_best < INF and right_best < INF:
                ans = min(ans, left_best + peak + right_best)

            # Move to next j: for j+1, suffix should represent indices > (j+1),
            # so remove nums[j+1+?]. Specifically, when incrementing j -> j+1,
            # the element at index (j+1) was previously in suffix (since it was > j),
            # but will no longer be > (j+1). That element is nums[j+1].
            if j + 1 < n:
                # currently at j, suffix includes indices > j => includes j+1
                if j + 1 <= n - 1:
                    counts_suffix[nums[j + 1]] -= 1

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # Since nums[i] in [1..50], we can keep value-indexed minima.
        # For each middle index j, we need:
        #   i < j, nums[i] < nums[j]   (min possible nums[i])
        #   k > j, nums[k] < nums[j]   (min possible nums[k])
        # Then candidate sum is nums[i] + nums[j] + nums[k].
        # Take minimum over all j.
        for j in range(1, n - 1):
            peak = nums[j]

            best_left = INF
            for i in range(0, j):
                if nums[i] < peak:
                    if nums[i] < best_left:
                        best_left = nums[i]

            best_right = INF
            for k in range(j + 1, n):
                if nums[k] < peak:
                    if nums[k] < best_right:
                        best_right = nums[k]

            if best_left != INF and best_right != INF:
                ans = min(ans, best_left + peak + best_right)

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF

        # For each possible middle index j, we need:
        # i < j with nums[i] < nums[j]
        # k > j with nums[k] < nums[j]
        # Minimize nums[i] + nums[j] + nums[k]
        for j in range(1, n - 1):
            peak = nums[j]

            # Left: minimum nums[i] among i<j with nums[i] < peak
            left_min = INF
            for i in range(j):
                if nums[i] < peak:
                    left_min = min(left_min, nums[i])

            # Right: minimum nums[k] among k>j with nums[k] < peak
            right_min = INF
            for k in range(j + 1, n):
                if nums[k] < peak:
                    right_min = min(right_min, nums[k])

            if left_min != INF and right_min != INF:
                ans = min(ans, left_min + peak + right_min)

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18
        # Since nums[i] in [1..50], we can store minima indexed by value.
        MAXV = 50

        ans = INF

        # Fix the peak index j, and compute best i<j with nums[i] < nums[j]
        # and best k>j with nums[k] < nums[j], then minimize sum.
        for j in range(1, n - 1):
            peak = nums[j]

            # min_left[v] = minimum nums[i] among i<j with nums[i]==v
            min_left = [INF] * (MAXV + 1)
            for i in range(0, j):
                v = nums[i]
                min_left[v] = min(min_left[v], v)

            # best left: minimum value strictly less than peak
            best_left = INF
            for v in range(1, peak):
                if min_left[v] < best_left:
                    best_left = min_left[v]

            # min_right[v] = minimum nums[k] among k>j with nums[k]==v
            min_right = [INF] * (MAXV + 1)
            for k in range(j + 1, n):
                v = nums[k]
                min_right[v] = min(min_right[v], v)

            best_right = INF
            for v in range(1, peak):
                if min_right[v] < best_right:
                    best_right = min_right[v]

            if best_left < INF and best_right < INF:
                ans = min(ans, best_left + peak + best_right)

        return -1 if ans == INF else ans
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        # values are small: 1..50
        V = 50
        INF = 10**9
        ans = INF

        # left_min[v] = smallest nums[i] seen so far with value == v
        # But we need strict nums[i] < nums[j], so we will precompute:
        # bestLeft[j] = min nums[i] for i<j with nums[i] < nums[j]
        # similarly for right.
        bestLeft = [INF] * n
        left_seen = [INF] * (V + 1)
        for j in range(n):
            x = nums[j]
            # compute min among values < x
            m = INF
            for val in range(1, x):
                if left_seen[val] < m:
                    m = left_seen[val]
            bestLeft[j] = m
            # update after querying so i < j
            if nums[j] < left_seen[nums[j]]:
                left_seen[nums[j]] = nums[j]

        bestRight = [INF] * n
        right_seen = [INF] * (V + 1)
        for j in range(n - 1, -1, -1):
            x = nums[j]
            m = INF
            for val in range(1, x):
                if right_seen[val] < m:
                    m = right_seen[val]
            bestRight[j] = m
            if nums[j] < right_seen[nums[j]]:
                right_seen[nums[j]] = nums[j]

        # peak-first: iterate peak position j
        for j in range(1, n - 1):
            left = bestLeft[j]
            right = bestRight[j]
            if left != INF and right != INF:
                ans = min(ans, left + nums[j] + right)

        return -1 if ans == INF else ans
```
```

</details>

#### Augmented Scores

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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "52",
      "actual": "52",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "57",
      "actual": "57",
      "error": ""
    },
    {
      "passed": true,
      "expected": "91",
      "actual": "91",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    }
  ]
}
```

</details>
