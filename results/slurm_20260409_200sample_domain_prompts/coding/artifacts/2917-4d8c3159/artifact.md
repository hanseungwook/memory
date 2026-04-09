# Problem 2917

- Domain: `coding`

## Problem

```text
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 
Example 1:

Input: nums = [-1,1,2,3,1], target = 2
Output: 3
Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
- (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
- (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.

Example 2:

Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
Output: 10
Explanation: There are 10 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = -4 < target
- (0, 3) since 0 < 3 and nums[0] + nums[3] = -8 < target
- (0, 4) since 0 < 4 and nums[0] + nums[4] = -13 < target
- (0, 5) since 0 < 5 and nums[0] + nums[5] = -7 < target
- (0, 6) since 0 < 6 and nums[0] + nums[6] = -3 < target
- (1, 4) since 1 < 4 and nums[1] + nums[4] = -5 < target
- (3, 4) since 3 < 4 and nums[3] + nums[4] = -9 < target
- (3, 5) since 3 < 5 and nums[3] + nums[5] = -3 < target
- (4, 5) since 4 < 5 and nums[4] + nums[5] = -8 < target
- (4, 6) since 4 < 6 and nums[4] + nums[6] = -4 < target

 
Constraints:

1 <= nums.length == n <= 50
-50 <= nums[i], target <= 50
```

### Starter Code

```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
```

### Test Cases

```json
[
  {
    "input": "[-1, 1, 2, 3, 1]\n2",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "[-6, 2, 5, -2, -7, -1, 3]\n-2",
    "output": "10",
    "testtype": "functional"
  },
  {
    "input": "[2, 4]\n1",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[-20]\n-35",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[27, 44]\n3",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[-5, -2]\n-1",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[-4, 9]\n-36",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[8, -4, -9, 5, 10]\n0",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "[-1, 3, -10, 3, -7]\n-3",
    "output": "7",
    "testtype": "functional"
  },
  {
    "input": "[-1, -8, -1, -10, -5, -10, 7]\n-19",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[-4, -1, 3, -2, -2, 5, -2, -5, -5, 1]\n6",
    "output": "43",
    "testtype": "functional"
  },
  {
    "input": "[-5, 1, -5, -10, 3, 3, 4, -7, -2, -8]\n-27",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[-15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15]\n-30",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[-50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50]\n-100",
    "output": "0",
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
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 
Example 1:

Input: nums = [-1,1,2,3,1], target = 2
Output: 3
Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
- (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
- (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.

Example 2:

Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
Output: 10
Explanation: There are 10 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = -4 < target
- (0, 3) since 0 < 3 and nums[0] + nums[3] = -8 < target
- (0, 4) since 0 < 4 and nums[0] + nums[4] = -13 < target
- (0, 5) since 0 < 5 and nums[0] + nums[5] = -7 < target
- (0, 6) since 0 < 6 and nums[0] + nums[6] = -3 < target
- (1, 4) since 1 < 4 and nums[1] + nums[4] = -5 < target
- (3, 4) since 3 < 4 and nums[3] + nums[4] = -9 < target
- (3, 5) since 3 < 5 and nums[3] + nums[5] = -3 < target
- (4, 5) since 4 < 5 and nums[4] + nums[5] = -8 < target
- (4, 6) since 4 < 6 and nums[4] + nums[6] = -4 < target

 
Constraints:

1 <= nums.length == n <= 50
-50 <= nums[i], target <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
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
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        # Brute force over all pairs (n <= 50)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Sort and use two pointers to count pairs with sum < target
        nums.sort()
        n = len(nums)
        ans = 0
        j = n - 1

        for i in range(n):
            # Move j left while sum >= target
            if j <= i:
                j = i  # keep invariant j > i when possible
            while j > i and nums[i] + nums[j] >= target:
                j -= 1
            # Now all indices k in (i, j] satisfy nums[i] + nums[k] < target
            ans += max(0, j - i)

        return ans
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Brute force with n <= 50 is sufficient
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        j = 1
        # For each i, find the largest r such that nums[i] + nums[r] < target,
        # with r < i is allowed only when counting pairs (l, r) with l < r.
        # Standard approach: for fixed j as right index, count valid i < j.
        # We'll use two-pointer with right pointer.
        j = 1
        for j in range(1, n):
            # Count how many i in [0, j-1] satisfy nums[i] < target - nums[j]
            # Since nums is sorted, use binary search via two pointers:
            # We'll maintain i pointer for first index not satisfying inequality.
            pass
        # Implement using binary search for clarity (n <= 50).
        import bisect
        for j in range(1, n):
            # need nums[i] + nums[j] < target  => nums[i] < target - nums[j]
            limit = target - nums[j]
            i_count = bisect.bisect_left(nums, limit, 0, j)  # indices < j and nums[i] < limit
            ans += i_count
        return ans
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Brute force with n <= 50 is sufficient: O(n^2)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # nums[i] + nums[j] < target for 0 <= i < j < n
        # Use sorting + two pointers: for each i as left pointer,
        # find how many right pointers j > i satisfy nums[i] + nums[j] < target.
        nums.sort()
        n = len(nums)
        ans = 0
        right = n - 1

        for i in range(n):
            # ensure j starts at least i+1; maintain right as the last index
            # such that nums[i] + nums[right] < target
            while right > i and nums[i] + nums[right] >= target:
                right -= 1
            if right <= i:
                break
            ans += (right - i)

        return ans
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Sort and use two pointers to count pairs with sum < target
        nums.sort()
        n = len(nums)
        res = 0

        # For each j as the right index, count i < j such that nums[i] < target - nums[j]
        # Because the array is sorted, we can binary-search the first index that fails.
        import bisect
        for j in range(n):
            limit = target - nums[j]
            # number of i in [0, j) with nums[i] < limit
            res += bisect.bisect_left(nums, limit, 0, j)

        return res
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Brute force is fine: n <= 50 => at most 1225 pairs
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    res += 1
        return res
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        # For each i, count j > i such that nums[i] + nums[j] < target
        j = n - 1
        for i in range(n):
            # Move j left while condition fails
            while i < j and nums[i] + nums[j] >= target:
                j -= 1
            if j <= i:
                break
            ans += (j - i)
        return ans
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        nums_sorted = sorted(nums)

        # For each i, find how many j > i satisfy nums[i] + nums[j] < target.
        for i in range(n):
            # Need nums[i] + nums[j] < target  => nums[j] < target - nums[i]
            limit = target - nums_sorted[i]
            # First index where nums_sorted[idx] >= limit
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums_sorted[mid] < limit:
                    lo = mid + 1
                else:
                    hi = mid
            # All indices in [i+1, lo) are valid
            ans += lo - (i + 1)

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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        # Brute force over all pairs (n <= 50)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Sort and use two pointers to count pairs with sum < target
        nums.sort()
        n = len(nums)
        ans = 0
        j = n - 1

        for i in range(n):
            # Move j left while sum >= target
            if j <= i:
                j = i  # keep invariant j > i when possible
            while j > i and nums[i] + nums[j] >= target:
                j -= 1
            # Now all indices k in (i, j] satisfy nums[i] + nums[k] < target
            ans += max(0, j - i)

        return ans
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Brute force with n <= 50 is sufficient
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        j = 1
        # For each i, find the largest r such that nums[i] + nums[r] < target,
        # with r < i is allowed only when counting pairs (l, r) with l < r.
        # Standard approach: for fixed j as right index, count valid i < j.
        # We'll use two-pointer with right pointer.
        j = 1
        for j in range(1, n):
            # Count how many i in [0, j-1] satisfy nums[i] < target - nums[j]
            # Since nums is sorted, use binary search via two pointers:
            # We'll maintain i pointer for first index not satisfying inequality.
            pass
        # Implement using binary search for clarity (n <= 50).
        import bisect
        for j in range(1, n):
            # need nums[i] + nums[j] < target  => nums[i] < target - nums[j]
            limit = target - nums[j]
            i_count = bisect.bisect_left(nums, limit, 0, j)  # indices < j and nums[i] < limit
            ans += i_count
        return ans
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Brute force with n <= 50 is sufficient: O(n^2)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # nums[i] + nums[j] < target for 0 <= i < j < n
        # Use sorting + two pointers: for each i as left pointer,
        # find how many right pointers j > i satisfy nums[i] + nums[j] < target.
        nums.sort()
        n = len(nums)
        ans = 0
        right = n - 1

        for i in range(n):
            # ensure j starts at least i+1; maintain right as the last index
            # such that nums[i] + nums[right] < target
            while right > i and nums[i] + nums[right] >= target:
                right -= 1
            if right <= i:
                break
            ans += (right - i)

        return ans
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Sort and use two pointers to count pairs with sum < target
        nums.sort()
        n = len(nums)
        res = 0

        # For each j as the right index, count i < j such that nums[i] < target - nums[j]
        # Because the array is sorted, we can binary-search the first index that fails.
        import bisect
        for j in range(n):
            limit = target - nums[j]
            # number of i in [0, j) with nums[i] < limit
            res += bisect.bisect_left(nums, limit, 0, j)

        return res
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Brute force is fine: n <= 50 => at most 1225 pairs
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    res += 1
        return res
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        # For each i, count j > i such that nums[i] + nums[j] < target
        j = n - 1
        for i in range(n):
            # Move j left while condition fails
            while i < j and nums[i] + nums[j] >= target:
                j -= 1
            if j <= i:
                break
            ans += (j - i)
        return ans
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        nums_sorted = sorted(nums)

        # For each i, find how many j > i satisfy nums[i] + nums[j] < target.
        for i in range(n):
            # Need nums[i] + nums[j] < target  => nums[j] < target - nums[i]
            limit = target - nums_sorted[i]
            # First index where nums_sorted[idx] >= limit
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums_sorted[mid] < limit:
                    lo = mid + 1
                else:
                    hi = mid
            # All indices in [i+1, lo) are valid
            ans += lo - (i + 1)

        return ans
```
```

</details>

## Evaluation

- Baseline pass@1: `1.0000`
- Augmented pass@1: `1.0000`
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
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 
Example 1:

Input: nums = [-1,1,2,3,1], target = 2
Output: 3
Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
- (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
- (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.

Example 2:

Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
Output: 10
Explanation: There are 10 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = -4 < target
- (0, 3) since 0 < 3 and nums[0] + nums[3] = -8 < target
- (0, 4) since 0 < 4 and nums[0] + nums[4] = -13 < target
- (0, 5) since 0 < 5 and nums[0] + nums[5] = -7 < target
- (0, 6) since 0 < 6 and nums[0] + nums[6] = -3 < target
- (1, 4) since 1 < 4 and nums[1] + nums[4] = -5 < target
- (3, 4) since 3 < 4 and nums[3] + nums[4] = -9 < target
- (3, 5) since 3 < 5 and nums[3] + nums[5] = -3 < target
- (4, 5) since 4 < 5 and nums[4] + nums[5] = -8 < target
- (4, 6) since 4 < 6 and nums[4] + nums[6] = -4 < target

 
Constraints:

1 <= nums.length == n <= 50
-50 <= nums[i], target <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
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
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums_sorted = sorted(nums)
        # For each i, find how many j>i satisfy nums[i] + nums[j] < target.
        # Since nums_sorted is ascending, for a fixed i we can binary search the
        # first index where the condition fails.
        import bisect
        for i in range(n):
            limit = target - nums_sorted[i]
            # We need nums_sorted[j] < limit, with j > i
            idx = bisect.bisect_left(nums_sorted, limit, i + 1, n)
            ans += idx - (i + 1)
        return ans
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        left = 0

        for i in range(n):
            # We want pairs (i, j) with i < j and nums[i] + nums[j] < target
            # For a fixed i, find the first index j where condition fails;
            # all j in [i+1, j-1] will satisfy.
            # Use binary search on range (i+1 .. n-1).
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[i] + nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            # lo is the first index where condition is false, so valid count:
            ans += lo - (i + 1)

        return ans
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Brute force is fine for n <= 50
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For each i, find number of j>i with nums[i] + nums[j] < target
        # Since array is sorted, for fixed i, the valid j form a prefix starting
        # from i+1 up to some boundary.
        j_start = 1
        for i in range(n):
            # Ensure j is at least i+1
            if j_start < i + 1:
                j_start = i + 1

            # Move j_end to the last valid index for this i:
            # nums[i] + nums[j_end] < target
            j_end = n
            # Binary search for first index where condition fails: nums[i] + nums[j] >= target
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[i] + nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            # 'lo' is the first failing index, so valid indices are [i+1, lo-1]
            ans += max(0, lo - (i + 1))

        return ans
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Since n <= 50, O(n^2) is sufficient.
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For each j, count i < j with nums[i] + nums[j] < target
        for j in range(n):
            need = target - nums[j]
            # number of i in [0..j-1] with nums[i] < need
            # since nums is sorted, lower_bound on need gives first index >= need
            lo, hi = 0, j
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < need:
                    lo = mid + 1
                else:
                    hi = mid
            ans += lo

        return ans
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        
        # For each i, count j > i such that nums[i] + nums[j] < target
        for i in range(n):
            # need nums[j] < target - nums[i]
            limit = target - nums[i]
            
            # first index j where nums[j] >= limit (in range [i+1, n))
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= limit:
                    hi = mid
                else:
                    lo = mid + 1
            
            # all indices in [i+1, lo) satisfy the condition
            ans += lo - (i + 1)
        
        return ans
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
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums_sorted = sorted(nums)
        # For each i, find how many j>i satisfy nums[i] + nums[j] < target.
        # Since nums_sorted is ascending, for a fixed i we can binary search the
        # first index where the condition fails.
        import bisect
        for i in range(n):
            limit = target - nums_sorted[i]
            # We need nums_sorted[j] < limit, with j > i
            idx = bisect.bisect_left(nums_sorted, limit, i + 1, n)
            ans += idx - (i + 1)
        return ans
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        left = 0

        for i in range(n):
            # We want pairs (i, j) with i < j and nums[i] + nums[j] < target
            # For a fixed i, find the first index j where condition fails;
            # all j in [i+1, j-1] will satisfy.
            # Use binary search on range (i+1 .. n-1).
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[i] + nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            # lo is the first index where condition is false, so valid count:
            ans += lo - (i + 1)

        return ans
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Brute force is fine for n <= 50
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For each i, find number of j>i with nums[i] + nums[j] < target
        # Since array is sorted, for fixed i, the valid j form a prefix starting
        # from i+1 up to some boundary.
        j_start = 1
        for i in range(n):
            # Ensure j is at least i+1
            if j_start < i + 1:
                j_start = i + 1

            # Move j_end to the last valid index for this i:
            # nums[i] + nums[j_end] < target
            j_end = n
            # Binary search for first index where condition fails: nums[i] + nums[j] >= target
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[i] + nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            # 'lo' is the first failing index, so valid indices are [i+1, lo-1]
            ans += max(0, lo - (i + 1))

        return ans
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Since n <= 50, O(n^2) is sufficient.
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For each j, count i < j with nums[i] + nums[j] < target
        for j in range(n):
            need = target - nums[j]
            # number of i in [0..j-1] with nums[i] < need
            # since nums is sorted, lower_bound on need gives first index >= need
            lo, hi = 0, j
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < need:
                    lo = mid + 1
                else:
                    hi = mid
            ans += lo

        return ans
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        
        # For each i, count j > i such that nums[i] + nums[j] < target
        for i in range(n):
            # need nums[j] < target - nums[i]
            limit = target - nums[i]
            
            # first index j where nums[j] >= limit (in range [i+1, n))
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= limit:
                    hi = mid
                else:
                    lo = mid + 1
            
            # all indices in [i+1, lo) satisfy the condition
            ans += lo - (i + 1)
        
        return ans
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
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "43",
      "actual": "43",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    }
  ]
}
```

</details>
