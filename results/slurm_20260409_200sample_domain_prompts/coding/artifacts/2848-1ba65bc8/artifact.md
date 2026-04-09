# Problem 2848

- Domain: `coding`

## Problem

```text
You are given a 0-indexed integer array nums containing n distinct positive integers. A permutation of nums is called special if:

For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] % nums[i] == 0.

Return the total number of special permutations. As the answer could be large, return it modulo 10^9 + 7.
 
Example 1:

Input: nums = [2,3,6]
Output: 2
Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.

Example 2:

Input: nums = [1,4,3]
Output: 2
Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.

 
Constraints:

2 <= nums.length <= 14
1 <= nums[i] <= 10^9
```

### Starter Code

```python
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[2, 3, 6]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[1, 4, 3]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[3, 6]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[2, 9]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[9, 3]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[8, 2]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[1, 2]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[1, 4]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[3, 19]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[10, 4, 3]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[14, 7, 8]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[296573006, 843224034, 611728152, 710630427, 167640710, 512370634, 670120901, 726495939, 771393204, 404562485, 406564308, 199755311, 985371443, 874785529]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[862055003, 862055004, 862055005, 862055006, 862055007, 862055008, 862055009, 862055010, 862055011, 862055012, 862055013, 862055014, 862055015, 862055016]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[100000007, 200000014, 300000021, 400000028, 500000035, 600000042, 700000049, 800000056, 900000063, 1000000070, 1100000077, 1200000084, 1300000091, 1400000098]",
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
You are given a 0-indexed integer array nums containing n distinct positive integers. A permutation of nums is called special if:

For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] % nums[i] == 0.

Return the total number of special permutations. As the answer could be large, return it modulo 10^9 + 7.
 
Example 1:

Input: nums = [2,3,6]
Output: 2
Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.

Example 2:

Input: nums = [1,4,3]
Output: 2
Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.

 
Constraints:

2 <= nums.length <= 14
1 <= nums[i] <= 10^9

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Build adjacency: i -> j if nums[i] can be next to nums[j] in either direction condition
        # Condition: nums[i] % nums[j] == 0 OR nums[j] % nums[i] == 0
        adj = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i][j] = True
        
        # dp[mask][last] = number of ways to build permutation using indices in mask ending at last
        # We'll compute via memoized recursion to keep code compact.
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            res = 0
            for nxt in range(n):
                if (mask >> nxt) & 1 == 0 and adj[last][nxt]:
                    res = (res + dp(mask | (1 << nxt), nxt)) % MOD
            return res
        
        # Start from each index as the first element
        ans = 0
        for i in range(n):
            ans = (ans + dp(1 << i, i)) % MOD
        return ans
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute adjacency: i -> j allowed if nums[i] divides nums[j] or vice versa
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i].append(j)

        size = 1 << n

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # number of ways to build a valid special permutation using exactly
            # elements in mask, ending with index last
            if mask == (1 << last):
                return 1
            prev_mask = mask ^ (1 << last)
            total = 0
            # previous element must be prev with edge prev -> last
            for prev in range(n):
                if (prev_mask >> prev) & 1:
                    # check compatibility between prev and last
                    a, b = nums[prev], nums[last]
                    if a % b == 0 or b % a == 0:
                        total += dp(prev_mask, prev)
            return total % MOD

        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp(full, last)) % MOD
        return ans
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        # Precompute adjacency: can go i -> j if divisible either way
        adj = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i][j] = True

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # number of special permutations that use exactly elements in mask,
            # ending at index last
            if mask == (1 << last):
                return 1
            total = 0
            prev_mask = mask ^ (1 << last)
            for prev in range(n):
                if prev_mask & (1 << prev) and adj[prev][last]:
                    total = (total + dp(prev_mask, prev)) % MOD
            return total

        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp(full, last)) % MOD
        return ans
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute compatibility: edge i -> j if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = nums[i], nums[j]
                ok[i][j] = (a % b == 0) or (b % a == 0)

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            """Number of ways to form permutation of elements in 'mask'
               ending with index 'last'."""
            if mask == (1 << last):
                return 1
            prev_mask = mask ^ (1 << last)
            ans = 0
            # try all possible previous indices k
            for k in range(n):
                if (prev_mask >> k) & 1 and ok[k][last]:
                    ans += dp(prev_mask, k)
            return ans % MOD

        full = (1 << n) - 1
        res = 0
        for last in range(n):
            res += dp(full, last)
        return res % MOD
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Build adjacency: i -> j if nums[i] divides nums[j] or nums[j] divides nums[i]
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = nums[i], nums[j]
                if a % b == 0 or b % a == 0:
                    adj[i].append(j)
        
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            """
            Number of ways to build a special permutation using exactly the elements in `mask`,
            ending at index `last`.
            """
            if mask & (mask - 1) == 0:  # only one bit set
                return 1
            prev_mask = mask ^ (1 << last)
            res = 0
            # previous index must connect to `last`
            for p in adj[last]:
                if prev_mask & (1 << p):
                    res += dp(prev_mask, p)
            return res % MOD
        
        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp(full, last)) % MOD
        return ans
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute valid adjacency: i -> j if nums[i] divides nums[j] or vice versa
        adj = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i][j] = True

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # Number of ways to build a special permutation using elements in mask
            # and ending with index 'last'
            if mask == (1 << n) - 1:
                return 1
            ans = 0
            for nxt in range(n):
                if not (mask & (1 << nxt)) and adj[last][nxt]:
                    ans += dp(mask | (1 << nxt), nxt)
                    if ans >= MOD:
                        ans %= MOD
            return ans % MOD

        total = 0
        for start in range(n):
            total += dp(1 << start, start)
            total %= MOD
        return total
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute compatibility: i -> j allowed if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        ok[i][j] = True
        
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == (1 << n) - 1:
                return 1
            ans = 0
            for nxt in range(n):
                if (mask >> nxt) & 1 == 0 and ok[last][nxt]:
                    ans = (ans + dp(mask | (1 << nxt), nxt)) % MOD
            return ans
        
        total = 0
        for start in range(n):
            total = (total + dp(1 << start, start)) % MOD
        return total
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        # adj[i] contains all j != i such that nums[i] can be adjacent to nums[j]
        # (i.e., either nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0).
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i].append(j)

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            """Number of ways to build a special permutation using exactly indices in mask,
            ending at position 'last' (where last is one of the chosen indices)."""
            if mask == (1 << n) - 1:
                return 1
            total = 0
            for nxt in adj[last]:
                if not (mask & (1 << nxt)):
                    total = (total + dp(mask | (1 << nxt), nxt)) % MOD
            return total

        ans = 0
        for i in range(n):
            ans = (ans + dp(1 << i, i)) % MOD
        return ans
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        a = nums

        # adjacency: can i be followed by j?
        can = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    x, y = a[i], a[j]
                    can[i][j] = (x % y == 0) or (y % x == 0)

        # dp[mask][last] = ways to build permutation using indices in mask ending at last
        # Use top-down memoization for efficiency.
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << last):
                return 1
            prev_mask = mask ^ (1 << last)
            total = 0
            # try all prev indices
            m = prev_mask
            while m:
                i = (m & -m).bit_length() - 1
                if can[i][last]:
                    total += dp(prev_mask, i)
                total %= MOD
                m &= m - 1
            return total

        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp(full, last)) % MOD
        return ans
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute adjacency: ok[i][j] means nums[i] can be followed by nums[j]
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        full = (1 << n) - 1

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == full:
                return 1
            ans = 0
            for nxt in range(n):
                if (mask >> nxt) & 1:
                    continue
                if ok[last][nxt]:
                    ans = (ans + dp(mask | (1 << nxt), nxt)) % MOD
            return ans

        res = 0
        for i in range(n):
            res = (res + dp(1 << i, i)) % MOD
        return res
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Build adjacency: i -> j if nums[i] can be next to nums[j] in either direction condition
        # Condition: nums[i] % nums[j] == 0 OR nums[j] % nums[i] == 0
        adj = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i][j] = True
        
        # dp[mask][last] = number of ways to build permutation using indices in mask ending at last
        # We'll compute via memoized recursion to keep code compact.
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            res = 0
            for nxt in range(n):
                if (mask >> nxt) & 1 == 0 and adj[last][nxt]:
                    res = (res + dp(mask | (1 << nxt), nxt)) % MOD
            return res
        
        # Start from each index as the first element
        ans = 0
        for i in range(n):
            ans = (ans + dp(1 << i, i)) % MOD
        return ans
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute adjacency: i -> j allowed if nums[i] divides nums[j] or vice versa
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i].append(j)

        size = 1 << n

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # number of ways to build a valid special permutation using exactly
            # elements in mask, ending with index last
            if mask == (1 << last):
                return 1
            prev_mask = mask ^ (1 << last)
            total = 0
            # previous element must be prev with edge prev -> last
            for prev in range(n):
                if (prev_mask >> prev) & 1:
                    # check compatibility between prev and last
                    a, b = nums[prev], nums[last]
                    if a % b == 0 or b % a == 0:
                        total += dp(prev_mask, prev)
            return total % MOD

        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp(full, last)) % MOD
        return ans
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        # Precompute adjacency: can go i -> j if divisible either way
        adj = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i][j] = True

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # number of special permutations that use exactly elements in mask,
            # ending at index last
            if mask == (1 << last):
                return 1
            total = 0
            prev_mask = mask ^ (1 << last)
            for prev in range(n):
                if prev_mask & (1 << prev) and adj[prev][last]:
                    total = (total + dp(prev_mask, prev)) % MOD
            return total

        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp(full, last)) % MOD
        return ans
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute compatibility: edge i -> j if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = nums[i], nums[j]
                ok[i][j] = (a % b == 0) or (b % a == 0)

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            """Number of ways to form permutation of elements in 'mask'
               ending with index 'last'."""
            if mask == (1 << last):
                return 1
            prev_mask = mask ^ (1 << last)
            ans = 0
            # try all possible previous indices k
            for k in range(n):
                if (prev_mask >> k) & 1 and ok[k][last]:
                    ans += dp(prev_mask, k)
            return ans % MOD

        full = (1 << n) - 1
        res = 0
        for last in range(n):
            res += dp(full, last)
        return res % MOD
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Build adjacency: i -> j if nums[i] divides nums[j] or nums[j] divides nums[i]
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = nums[i], nums[j]
                if a % b == 0 or b % a == 0:
                    adj[i].append(j)
        
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            """
            Number of ways to build a special permutation using exactly the elements in `mask`,
            ending at index `last`.
            """
            if mask & (mask - 1) == 0:  # only one bit set
                return 1
            prev_mask = mask ^ (1 << last)
            res = 0
            # previous index must connect to `last`
            for p in adj[last]:
                if prev_mask & (1 << p):
                    res += dp(prev_mask, p)
            return res % MOD
        
        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp(full, last)) % MOD
        return ans
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute valid adjacency: i -> j if nums[i] divides nums[j] or vice versa
        adj = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i][j] = True

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # Number of ways to build a special permutation using elements in mask
            # and ending with index 'last'
            if mask == (1 << n) - 1:
                return 1
            ans = 0
            for nxt in range(n):
                if not (mask & (1 << nxt)) and adj[last][nxt]:
                    ans += dp(mask | (1 << nxt), nxt)
                    if ans >= MOD:
                        ans %= MOD
            return ans % MOD

        total = 0
        for start in range(n):
            total += dp(1 << start, start)
            total %= MOD
        return total
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute compatibility: i -> j allowed if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        ok[i][j] = True
        
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == (1 << n) - 1:
                return 1
            ans = 0
            for nxt in range(n):
                if (mask >> nxt) & 1 == 0 and ok[last][nxt]:
                    ans = (ans + dp(mask | (1 << nxt), nxt)) % MOD
            return ans
        
        total = 0
        for start in range(n):
            total = (total + dp(1 << start, start)) % MOD
        return total
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        # adj[i] contains all j != i such that nums[i] can be adjacent to nums[j]
        # (i.e., either nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0).
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        adj[i].append(j)

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            """Number of ways to build a special permutation using exactly indices in mask,
            ending at position 'last' (where last is one of the chosen indices)."""
            if mask == (1 << n) - 1:
                return 1
            total = 0
            for nxt in adj[last]:
                if not (mask & (1 << nxt)):
                    total = (total + dp(mask | (1 << nxt), nxt)) % MOD
            return total

        ans = 0
        for i in range(n):
            ans = (ans + dp(1 << i, i)) % MOD
        return ans
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        a = nums

        # adjacency: can i be followed by j?
        can = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    x, y = a[i], a[j]
                    can[i][j] = (x % y == 0) or (y % x == 0)

        # dp[mask][last] = ways to build permutation using indices in mask ending at last
        # Use top-down memoization for efficiency.
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << last):
                return 1
            prev_mask = mask ^ (1 << last)
            total = 0
            # try all prev indices
            m = prev_mask
            while m:
                i = (m & -m).bit_length() - 1
                if can[i][last]:
                    total += dp(prev_mask, i)
                total %= MOD
                m &= m - 1
            return total

        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp(full, last)) % MOD
        return ans
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute adjacency: ok[i][j] means nums[i] can be followed by nums[j]
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        full = (1 << n) - 1

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == full:
                return 1
            ans = 0
            for nxt in range(n):
                if (mask >> nxt) & 1:
                    continue
                if ok[last][nxt]:
                    ans = (ans + dp(mask | (1 << nxt), nxt)) % MOD
            return ans

        res = 0
        for i in range(n):
            res = (res + dp(1 << i, i)) % MOD
        return res
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
You are given a 0-indexed integer array nums containing n distinct positive integers. A permutation of nums is called special if:

For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] % nums[i] == 0.

Return the total number of special permutations. As the answer could be large, return it modulo 10^9 + 7.
 
Example 1:

Input: nums = [2,3,6]
Output: 2
Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.

Example 2:

Input: nums = [1,4,3]
Output: 2
Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.

 
Constraints:

2 <= nums.length <= 14
1 <= nums[i] <= 10^9

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums = list(nums)

        # Precompute adjacency: can go from i to j if divisible either way
        can = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    can[i][j] = True

        # DP over subsets, last element index
        # dp[mask][last] = number of ways to build permutation using elements in mask ending at last
        # We'll implement via recursion + memoization for efficiency/clarity.
        full_mask = (1 << n) - 1

        @lru_cache(None)
        def dfs(mask: int, last: int) -> int:
            if mask == full_mask:
                return 1
            total = 0
            for nxt in range(n):
                if (mask >> nxt) & 1:
                    continue
                if can[last][nxt]:
                    total += dfs(mask | (1 << nxt), nxt)
            return total % MOD

        ans = 0
        for start in range(n):
            ans += dfs(1 << start, start)
        return ans % MOD
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # adjacency mask: i -> j allowed if divisible either way
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        # dp[mask][last] = number of ways to build a special permutation
        # using exactly elements in mask, ending with index last.
        # We'll implement with memoization over (mask,last).
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            ans = 0
            for nxt in range(n):
                if (mask >> nxt) & 1:
                    continue
                if ok[last][nxt]:
                    ans += dp(mask | (1 << nxt), nxt)
            return ans % MOD

        res = 0
        for start in range(n):
            res = (res + dp(1 << start, start)) % MOD
        return res
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Build adjacency: i -> j if nums[i] and nums[j] are compatible by divisibility
        ok = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        # DP over subsets:
        # dp[mask][last] = number of ways to build a special permutation using elements in mask,
        # ending at index last.
        # Use memoized recursion to keep code compact.
        @lru_cache(None)
        def dfs(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            total = 0
            for nxt in range(n):
                if not (mask >> nxt) & 1 and ok[last][nxt]:
                    total += dfs(mask | (1 << nxt), nxt)
                    if total >= MOD:
                        total %= MOD
            return total % MOD

        ans = 0
        for start in range(n):
            ans += dfs(1 << start, start)
            ans %= MOD
        return ans
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # Build adjacency: edge i->j if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    ok[i][j] = (a % b == 0) or (b % a == 0)

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # number of ways to build a special permutation using indices in mask
            # ending with 'last' (where last is included in mask)
            if mask == (1 << n) - 1:
                return 1
            res = 0
            for nxt in range(n):
                if (mask >> nxt) & 1 == 0 and ok[last][nxt]:
                    res = (res + dp(mask | (1 << nxt), nxt)) % MOD
            return res

        ans = 0
        for start in range(n):
            ans = (ans + dp(1 << start, start)) % MOD
        return ans
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute adjacency: can i be followed by j?
        can = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        can[i][j] = True

        full_mask = (1 << n) - 1

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == full_mask:
                return 1
            res = 0
            # try next
            for nxt in range(n):
                if (mask >> nxt) & 1:
                    continue
                if can[last][nxt]:
                    res = (res + dp(mask | (1 << nxt), nxt)) % MOD
            return res

        ans = 0
        for start in range(n):
            ans = (ans + dp(1 << start, start)) % MOD
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
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Edge i->j if nums[i] divides nums[j] or nums[j] divides nums[i]
        ok = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        # dp[mask][last] = ways to build a special permutation using elements in mask,
        # ending with index last.
        size = 1 << n
        dp = [ [0]*n for _ in range(size) ]
        
        for i in range(n):
            dp[1 << i][i] = 1
        
        for mask in range(size):
            for last in range(n):
                ways = dp[mask][last]
                if ways == 0:
                    continue
                for nxt in range(n):
                    if (mask >> nxt) & 1:
                        continue
                    if ok[last][nxt]:
                        dp[mask | (1 << nxt)][nxt] = (dp[mask | (1 << nxt)][nxt] + ways) % MOD

        full = size - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp[full][last]) % MOD
        return ans
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        # Precompute divisibility compatibility
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == (1 << n) - 1:
                return 1
            ans = 0
            for nxt in range(n):
                if not (mask & (1 << nxt)) and ok[last][nxt]:
                    ans = (ans + dp(mask | (1 << nxt), nxt)) % MOD
            return ans

        res = 0
        for i in range(n):
            res = (res + dp(1 << i, i)) % MOD
        return res
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sorted_idx = list(range(n))  # just to be explicit

        # Build compatibility: i -> j if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        ok[i][j] = True

        full_mask = (1 << n) - 1

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            """
            Number of ways to build a special permutation of the subset 'mask'
            that ends with index 'last'.
            """
            if mask == (1 << last):
                return 1
            ans = 0
            prev_mask = mask ^ (1 << last)
            # Try all possible previous indices
            for prev in range(n):
                if (prev_mask >> prev) & 1 and ok[prev][last]:
                    ans = (ans + dp(prev_mask, prev)) % MOD
            return ans

        res = 0
        for last in range(n):
            res = (res + dp(full_mask, last)) % MOD
        return res
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        # Precompute adjacency: i -> j if nums[i] and nums[j] are compatible
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        ok[i][j] = True

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == (1 << n) - 1:
                return 1
            res = 0
            for nxt in range(n):
                if (mask >> nxt) & 1 == 0 and ok[last][nxt]:
                    res = (res + dp(mask | (1 << nxt), nxt)) % MOD
            return res

        ans = 0
        for i in range(n):
            ans = (ans + dp(1 << i, i)) % MOD
        return ans
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute adjacency: edge i->j if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        ok[i][j] = True

        # DP over subsets:
        # dp[mask][last] = number of ways to form permutation using indices in mask ending at last
        size = 1 << n

        # Using memoized recursion
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << last):
                return 1
            res = 0
            prev_mask = mask ^ (1 << last)
            # try previous index k
            m = prev_mask
            while m:
                k_bit = m & -m
                k = (k_bit.bit_length() - 1)
                if ok[k][last]:
                    res += dp(prev_mask, k)
                res %= MOD
                m -= k_bit
            return res

        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans += dp(full, last)
            ans %= MOD
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums = list(nums)

        # Precompute adjacency: can go from i to j if divisible either way
        can = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    can[i][j] = True

        # DP over subsets, last element index
        # dp[mask][last] = number of ways to build permutation using elements in mask ending at last
        # We'll implement via recursion + memoization for efficiency/clarity.
        full_mask = (1 << n) - 1

        @lru_cache(None)
        def dfs(mask: int, last: int) -> int:
            if mask == full_mask:
                return 1
            total = 0
            for nxt in range(n):
                if (mask >> nxt) & 1:
                    continue
                if can[last][nxt]:
                    total += dfs(mask | (1 << nxt), nxt)
            return total % MOD

        ans = 0
        for start in range(n):
            ans += dfs(1 << start, start)
        return ans % MOD
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # adjacency mask: i -> j allowed if divisible either way
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        # dp[mask][last] = number of ways to build a special permutation
        # using exactly elements in mask, ending with index last.
        # We'll implement with memoization over (mask,last).
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            ans = 0
            for nxt in range(n):
                if (mask >> nxt) & 1:
                    continue
                if ok[last][nxt]:
                    ans += dp(mask | (1 << nxt), nxt)
            return ans % MOD

        res = 0
        for start in range(n):
            res = (res + dp(1 << start, start)) % MOD
        return res
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Build adjacency: i -> j if nums[i] and nums[j] are compatible by divisibility
        ok = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        # DP over subsets:
        # dp[mask][last] = number of ways to build a special permutation using elements in mask,
        # ending at index last.
        # Use memoized recursion to keep code compact.
        @lru_cache(None)
        def dfs(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            total = 0
            for nxt in range(n):
                if not (mask >> nxt) & 1 and ok[last][nxt]:
                    total += dfs(mask | (1 << nxt), nxt)
                    if total >= MOD:
                        total %= MOD
            return total % MOD

        ans = 0
        for start in range(n):
            ans += dfs(1 << start, start)
            ans %= MOD
        return ans
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # Build adjacency: edge i->j if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    ok[i][j] = (a % b == 0) or (b % a == 0)

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # number of ways to build a special permutation using indices in mask
            # ending with 'last' (where last is included in mask)
            if mask == (1 << n) - 1:
                return 1
            res = 0
            for nxt in range(n):
                if (mask >> nxt) & 1 == 0 and ok[last][nxt]:
                    res = (res + dp(mask | (1 << nxt), nxt)) % MOD
            return res

        ans = 0
        for start in range(n):
            ans = (ans + dp(1 << start, start)) % MOD
        return ans
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute adjacency: can i be followed by j?
        can = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        can[i][j] = True

        full_mask = (1 << n) - 1

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == full_mask:
                return 1
            res = 0
            # try next
            for nxt in range(n):
                if (mask >> nxt) & 1:
                    continue
                if can[last][nxt]:
                    res = (res + dp(mask | (1 << nxt), nxt)) % MOD
            return res

        ans = 0
        for start in range(n):
            ans = (ans + dp(1 << start, start)) % MOD
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
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Edge i->j if nums[i] divides nums[j] or nums[j] divides nums[i]
        ok = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        # dp[mask][last] = ways to build a special permutation using elements in mask,
        # ending with index last.
        size = 1 << n
        dp = [ [0]*n for _ in range(size) ]
        
        for i in range(n):
            dp[1 << i][i] = 1
        
        for mask in range(size):
            for last in range(n):
                ways = dp[mask][last]
                if ways == 0:
                    continue
                for nxt in range(n):
                    if (mask >> nxt) & 1:
                        continue
                    if ok[last][nxt]:
                        dp[mask | (1 << nxt)][nxt] = (dp[mask | (1 << nxt)][nxt] + ways) % MOD

        full = size - 1
        ans = 0
        for last in range(n):
            ans = (ans + dp[full][last]) % MOD
        return ans
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        # Precompute divisibility compatibility
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    ok[i][j] = True

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == (1 << n) - 1:
                return 1
            ans = 0
            for nxt in range(n):
                if not (mask & (1 << nxt)) and ok[last][nxt]:
                    ans = (ans + dp(mask | (1 << nxt), nxt)) % MOD
            return ans

        res = 0
        for i in range(n):
            res = (res + dp(1 << i, i)) % MOD
        return res
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sorted_idx = list(range(n))  # just to be explicit

        # Build compatibility: i -> j if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        ok[i][j] = True

        full_mask = (1 << n) - 1

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            """
            Number of ways to build a special permutation of the subset 'mask'
            that ends with index 'last'.
            """
            if mask == (1 << last):
                return 1
            ans = 0
            prev_mask = mask ^ (1 << last)
            # Try all possible previous indices
            for prev in range(n):
                if (prev_mask >> prev) & 1 and ok[prev][last]:
                    ans = (ans + dp(prev_mask, prev)) % MOD
            return ans

        res = 0
        for last in range(n):
            res = (res + dp(full_mask, last)) % MOD
        return res
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        # Precompute adjacency: i -> j if nums[i] and nums[j] are compatible
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        ok[i][j] = True

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            # mask includes 'last'
            if mask == (1 << n) - 1:
                return 1
            res = 0
            for nxt in range(n):
                if (mask >> nxt) & 1 == 0 and ok[last][nxt]:
                    res = (res + dp(mask | (1 << nxt), nxt)) % MOD
            return res

        ans = 0
        for i in range(n):
            ans = (ans + dp(1 << i, i)) % MOD
        return ans
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute adjacency: edge i->j if nums[i] divides nums[j] or vice versa
        ok = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        ok[i][j] = True

        # DP over subsets:
        # dp[mask][last] = number of ways to form permutation using indices in mask ending at last
        size = 1 << n

        # Using memoized recursion
        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << last):
                return 1
            res = 0
            prev_mask = mask ^ (1 << last)
            # try previous index k
            m = prev_mask
            while m:
                k_bit = m & -m
                k = (k_bit.bit_length() - 1)
                if ok[k][last]:
                    res += dp(prev_mask, k)
                res %= MOD
                m -= k_bit
            return res

        full = (1 << n) - 1
        ans = 0
        for last in range(n):
            ans += dp(full, last)
            ans %= MOD
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
