# Problem 3193

- Domain: `coding`

## Problem

```text
You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

|x - y| <= min(x, y)

You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
Return the maximum XOR value out of all possible strong pairs in the array nums.
Note that you can pick the same integer twice to form a pair.
 
Example 1:

Input: nums = [1,2,3,4,5]
Output: 7
Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.

Example 2:

Input: nums = [10,100]
Output: 0
Explanation: There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.

Example 3:

Input: nums = [5,6,25,30]
Output: 7
Explanation: There are 6 strong pairs in the array nums: (5, 5), (5, 6), (6, 6), (25, 25), (25, 30) and (30, 30).
The maximum XOR possible from these pairs is 25 XOR 30 = 7 since the only other non-zero XOR value is 5 XOR 6 = 3.

 
Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 100
```

### Starter Code

```python
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[1, 2, 3, 4, 5]",
    "output": "7",
    "testtype": "functional"
  },
  {
    "input": "[10, 100]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[5, 6, 25, 30]",
    "output": "7",
    "testtype": "functional"
  },
  {
    "input": "[4]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[7]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[30]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[41]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[84]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[17]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[45]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[2, 1]",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "[41, 57, 83, 41, 80, 43, 37, 73, 80, 8, 35, 66, 28, 29, 46, 10, 13, 96, 82, 5, 69, 60, 92, 3, 35, 60, 68, 15, 40, 24, 73, 19, 31, 30, 83, 21, 22, 95, 16, 35, 88, 18, 22, 41, 21, 47, 32, 63, 22]",
    "output": "127",
    "testtype": "functional"
  },
  {
    "input": "[48, 74, 57, 13, 20, 81, 81, 47, 20, 69, 8, 17, 54, 59, 57, 87, 80, 48, 9, 23, 1, 51, 75, 26, 100, 64, 34, 32, 21, 4, 18, 36, 8, 49, 58, 50, 45, 12, 15, 77, 49, 77, 28, 29, 47, 93, 30, 69, 17, 92]",
    "output": "127",
    "testtype": "functional"
  },
  {
    "input": "[74, 45, 35, 24, 49, 47, 30, 16, 16, 21, 95, 44, 36, 100, 38, 90, 17, 24, 40, 4, 69, 77, 54, 11, 58, 80, 78, 40, 38, 58, 47, 71, 23, 90, 61, 26, 25, 72, 97, 83, 53, 70, 44, 68, 91, 65, 83, 30, 82, 43]",
    "output": "127",
    "testtype": "functional"
  },
  {
    "input": "[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]",
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
You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

|x - y| <= min(x, y)

You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
Return the maximum XOR value out of all possible strong pairs in the array nums.
Note that you can pick the same integer twice to form a pair.
 
Example 1:

Input: nums = [1,2,3,4,5]
Output: 7
Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.

Example 2:

Input: nums = [10,100]
Output: 0
Explanation: There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.

Example 3:

Input: nums = [5,6,25,30]
Output: 7
Explanation: There are 6 strong pairs in the array nums: (5, 5), (5, 6), (6, 6), (25, 25), (25, 30) and (30, 30).
The maximum XOR possible from these pairs is 25 XOR 30 = 7 since the only other non-zero XOR value is 5 XOR 6 = 3.

 
Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        best = 0

        # Strong pair condition:
        # |x - y| <= min(x, y)  <=>  max(x,y) <= 2*min(x,y)
        # With sorted array, for any x = nums[i] (as the smaller),
        # valid y are nums[j] where nums[j] <= 2*x.
        for i in range(n):
            x = nums[i]
            limit = 2 * x
            j = i
            while j < n and nums[j] <= limit:
                best = max(best, x ^ nums[j])
                j += 1

        return best
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # For strong pair condition:
        # |x - y| <= min(x, y)  (x, y >= 1)
        # Let wlog x >= y => x - y <= y => x <= 2y.
        # So (a, b) is strong iff max(a, b) <= 2 * min(a, b).

        nums = sorted(nums)
        ans = 0
        n = len(nums)

        # If we fix the larger element as nums[j], valid smaller elements nums[i] satisfy:
        # nums[i] >= ceil(nums[j] / 2). We'll check only those within this bound.
        for j in range(n):
            lo = (nums[j] + 1) // 2  # ceil(nums[j]/2)
            i = self._lower_bound(nums, lo, 0, j + 1)
            # Now nums[k] for k in [i, j] are all valid with nums[j]
            # Compute maximum XOR among this small range.
            # n<=50 so O(n^2) is fine.
            best = 0
            for k in range(i, j + 1):
                best = max(best, nums[k] ^ nums[j])
            ans = max(ans, best)

        return ans

    def _lower_bound(self, a: List[int], x: int, lo: int, hi: int) -> int:
        # first index in a[lo:hi] with a[idx] >= x
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Build list of candidate values for XOR:
        # For a strong pair (x,y) with x<=y: y-x <= x  => x <= y <= 2x
        # So for each x, y must lie in [x, 2x]. We'll only need to consider
        # the numbers within that window to get the maximum XOR.
        candidates = []
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j < n and nums[j] <= 2 * nums[i]:
                j += 1
            # all nums[i..j-1] can pair with nums[i]
            # collect boundary-ish values (all are fine due to small constraints)
            candidates.extend(nums[i:j])

        # Brute force over candidates (constraints are small, candidates are limited)
        # but still safe because nums[i] <= 100 and n<=50.
        best = 0
        # remove duplicates for speed
        cand = list(set(candidates))
        m = len(cand)
        for a in cand:
            for b in cand:
                if abs(a - b) <= min(a, b):
                    best = max(best, a ^ b)
        return best
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Strong pair condition: |x - y| <= min(x, y)
        # For x,y > 0, with x <= y: y-x <= x  -> y <= 2x
        # So for each smaller value a, valid b must satisfy a <= b <= 2a.

        nums.sort()
        best = 0

        # Only values in range [a, 2a] can pair with a as the smaller element.
        # nums[i] <= 100, so we can afford checking per i.
        for i in range(len(nums)):
            a = nums[i]
            j = i
            while j < len(nums) and nums[j] <= 2 * a:
                # (nums[i], nums[j]) is strong because nums[i] <= nums[j] <= 2*nums[i]
                # Also if nums[j] < nums[i], it will be covered when i is the smaller one.
                best = max(best, a ^ nums[j])
                j += 1

        return best
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        # For each possible larger value b = nums[j], allowed a must satisfy:
        # |a - b| <= min(a, b). With a <= b, this becomes b - a <= a -> a >= ceil(b/2).
        # So for b at index j, we only need consider i in [lower_bound(ceil(b/2)), j].
        # Track maximum XOR among strong pairs using incremental bitwise trie.
        class TrieNode:
            __slots__ = ("nxt",)
            def __init__(self):
                self.nxt = [None, None]

        def insert(root, x):
            node = root
            for k in range(7, -1, -1):  # nums[i] <= 100 < 2^7; keep 0..7 to be safe
                b = (x >> k) & 1
                if node.nxt[b] is None:
                    node.nxt[b] = TrieNode()
                node = node.nxt[b]

        def max_xor_with(root, x):
            node = root
            best = 0
            for k in range(7, -1, -1):
                b = (x >> k) & 1
                want = 1 - b
                if node.nxt[want] is not None:
                    best |= 1 << k
                    node = node.nxt[want]
                else:
                    node = node.nxt[b]
            return best

        # Simple trie without deletion: we sweep increasing b and rebuild for each j window size
        # but that would be O(n^2 * bits). Instead, since n<=50 it's fine and simpler:
        # n^2 is 2500, bits ~ 8 => very fast. We'll brute strong pairs directly.
        for i in range(n):
            for j in range(i, n):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    ans = max(ans, x ^ y)
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Strong pair condition: for integers x,y with a = min(x,y), b = max(x,y),
        # we need |x-y| = b-a <= a  <=>  b <= 2a.
        #
        # Sort and use the fact nums[i] can only pair with nums[j] where nums[j] <= 2*nums[i]
        # for i <= j.
        nums.sort()
        n = len(nums)

        ans = 0
        left = 0

        # Build a binary trie for numbers in current eligible window [left..i]
        class Trie:
            __slots__ = ("child", "cnt")
            def __init__(self):
                self.child = [[-1, -1]]
                self.cnt = [0]

            def add(self, x: int):
                node = 0
                self.cnt[node] += 1
                for b in range(6, -1, -1):  # nums[i] <= 100 < 2^7
                    bit = (x >> b) & 1
                    nxt = self.child[node][bit]
                    if nxt == -1:
                        nxt = len(self.child)
                        self.child[node][bit] = nxt
                        self.child.append([-1, -1])
                        self.cnt.append(0)
                    node = nxt
                    self.cnt[node] += 1

            def remove(self, x: int):
                node = 0
                self.cnt[node] -= 1
                for b in range(6, -1, -1):
                    bit = (x >> b) & 1
                    node = self.child[node][bit]
                    self.cnt[node] -= 1

            def max_xor(self, x: int) -> int:
                # assumes trie is non-empty
                node = 0
                res = 0
                for b in range(6, -1, -1):
                    bit = (x >> b) & 1
                    want = 1 - bit
                    nxt = self.child[node][want]
                    if nxt != -1 and self.cnt[nxt] > 0:
                        res |= (1 << b)
                        node = nxt
                    else:
                        node = self.child[node][bit]
                return res

            def __len__(self):
                return self.cnt[0]

        trie = Trie()

        for i in range(n):
            # Move left until nums[i] <= 2*nums[left]
            while nums[i] > 2 * nums[left]:
                trie.remove(nums[left])
                left += 1

            # Now all nums[k] in [left..i] satisfy nums[i] <= 2*nums[k] for k>=left? Actually
            # because nums is sorted and k <= i, we have min(nums[k], nums[i]) = nums[k] and
            # condition requires nums[i] <= 2*nums[k]. With left chosen as above, this holds.
            if len(trie) > 0:
                ans = max(ans, trie.max_xor(nums[i]))

            trie.add(nums[i])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Strong pair condition: |x-y| <= min(x,y)
        # For x<=y, this is y-x <= x  <=> y <= 2x.
        # So for each x, it can pair only with values in [x, 2x].
        #
        # Given nums[i] up to 100 and n up to 50, we can safely do:
        # - For each value as the smaller element, restrict j indices.
        # - Compute XOR max among those pairs (including same element).
        #
        # Complexity: O(n^2) worst-case (still tiny for constraints).
        ans = 0
        for i in range(n):
            x = nums[i]
            # Find the last index j such that nums[j] <= 2*x
            # Since sorted, just advance pointer or binary search.
            lo, hi = i, n - 1
            best_j = i
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= 2 * x:
                    best_j = mid
                    lo = mid + 1
                else:
                    hi = mid - 1

            for j in range(i, best_j + 1):
                ans = max(ans, x ^ nums[j])

        return ans
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        best = 0

        # Strong pair condition:
        # |x - y| <= min(x, y)
        # Let a <= b => b - a <= a  <=>  b <= 2a
        # Therefore strong pairs are exactly those with
        # for each a, partner b must satisfy b <= 2a.
        for i in range(n):
            a = nums[i]
            j = i
            while j < n and nums[j] <= 2 * a:
                # compute xor with all valid b in [i..j)
                best = max(best, a ^ nums[j])
                j += 1

        return best
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Sort and keep only distinct values (duplicates don't change achievable XOR
        # because we can always pick the same value twice).
        nums = sorted(set(nums))
        m = len(nums)
        ans = 0

        # Two-pointer window based on the strong-pair condition:
        # Need |x-y| <= min(x,y). If we consider x <= y, condition becomes y-x <= x => y <= 2x.
        # For each smaller value x at index i, all larger values y with y <= 2x are strong with x.
        j = 0
        for i in range(m):
            if j < i:
                j = i
            while j < m and nums[j] <= 2 * nums[i]:
                j += 1

            # Now nums[i..j-1] all satisfy strong-pair with nums[i] (since nums[i] <= nums[k] <= 2*nums[i])
            # Compute best XOR between nums[i] and those candidates.
            # Brute-force is fine: m <= 50.
            for k in range(i, j):
                ans = max(ans, nums[i] ^ nums[k])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # For strong pair (x,y): |x-y| <= min(x,y).
        # This is always true when x and y are sorted: for x <= y -> y-x <= x -> y <= 2x.
        nums = sorted(nums)
        n = len(nums)

        # Build candidate set: for each nums[i] as the smaller value,
        # any nums[j] with j <= upper_bound(2*nums[i]) can pair strongly with nums[i].
        # The optimal XOR will be achieved among these limited candidates.
        candidates = set()
        for i in range(n):
            x = nums[i]
            limit = 2 * x
            # find first index > limit
            lo, hi = i, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= limit:
                    lo = mid + 1
                else:
                    hi = mid
            # nums[i..lo-1] are within limit
            for k in range(i, lo):
                candidates.add(nums[k])

        cand = list(candidates)

        # Compute max XOR over all pairs in candidates (including same element twice).
        ans = 0
        m = len(cand)
        for i in range(m):
            for j in range(i, m):
                ans = max(ans, cand[i] ^ cand[j])
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
| 9 | 0.8667 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 13,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "110",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "7",
      "actual": "31",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

|x - y| <= min(x, y)

You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
Return the maximum XOR value out of all possible strong pairs in the array nums.
Note that you can pick the same integer twice to form a pair.
 
Example 1:

Input: nums = [1,2,3,4,5]
Output: 7
Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.

Example 2:

Input: nums = [10,100]
Output: 0
Explanation: There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.

Example 3:

Input: nums = [5,6,25,30]
Output: 7
Explanation: There are 6 strong pairs in the array nums: (5, 5), (5, 6), (6, 6), (25, 25), (25, 30) and (30, 30).
The maximum XOR possible from these pairs is 25 XOR 30 = 7 since the only other non-zero XOR value is 5 XOR 6 = 3.

 
Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 100

### Solutions
#### Correct
Attempt 1
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        best = 0

        # Strong pair condition:
        # |x - y| <= min(x, y)  <=>  max(x,y) <= 2*min(x,y)
        # With sorted array, for any x = nums[i] (as the smaller),
        # valid y are nums[j] where nums[j] <= 2*x.
        for i in range(n):
            x = nums[i]
            limit = 2 * x
            j = i
            while j < n and nums[j] <= limit:
                best = max(best, x ^ nums[j])
                j += 1

        return best
```

Attempt 2
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # For strong pair condition:
        # |x - y| <= min(x, y)  (x, y >= 1)
        # Let wlog x >= y => x - y <= y => x <= 2y.
        # So (a, b) is strong iff max(a, b) <= 2 * min(a, b).

        nums = sorted(nums)
        ans = 0
        n = len(nums)

        # If we fix the larger element as nums[j], valid smaller elements nums[i] satisfy:
        # nums[i] >= ceil(nums[j] / 2). We'll check only those within this bound.
        for j in range(n):
            lo = (nums[j] + 1) // 2  # ceil(nums[j]/2)
            i = self._lower_bound(nums, lo, 0, j + 1)
            # Now nums[k] for k in [i, j] are all valid with nums[j]
            # Compute maximum XOR among this small range.
            # n<=50 so O(n^2) is fine.
            best = 0
            for k in range(i, j + 1):
                best = max(best, nums[k] ^ nums[j])
            ans = max(ans, best)

        return ans

    def _lower_bound(self, a: List[int], x: int, lo: int, hi: int) -> int:
        # first index in a[lo:hi] with a[idx] >= x
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
```

Attempt 3
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Build list of candidate values for XOR:
        # For a strong pair (x,y) with x<=y: y-x <= x  => x <= y <= 2x
        # So for each x, y must lie in [x, 2x]. We'll only need to consider
        # the numbers within that window to get the maximum XOR.
        candidates = []
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j < n and nums[j] <= 2 * nums[i]:
                j += 1
            # all nums[i..j-1] can pair with nums[i]
            # collect boundary-ish values (all are fine due to small constraints)
            candidates.extend(nums[i:j])

        # Brute force over candidates (constraints are small, candidates are limited)
        # but still safe because nums[i] <= 100 and n<=50.
        best = 0
        # remove duplicates for speed
        cand = list(set(candidates))
        m = len(cand)
        for a in cand:
            for b in cand:
                if abs(a - b) <= min(a, b):
                    best = max(best, a ^ b)
        return best
```

Attempt 4
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Strong pair condition: |x - y| <= min(x, y)
        # For x,y > 0, with x <= y: y-x <= x  -> y <= 2x
        # So for each smaller value a, valid b must satisfy a <= b <= 2a.

        nums.sort()
        best = 0

        # Only values in range [a, 2a] can pair with a as the smaller element.
        # nums[i] <= 100, so we can afford checking per i.
        for i in range(len(nums)):
            a = nums[i]
            j = i
            while j < len(nums) and nums[j] <= 2 * a:
                # (nums[i], nums[j]) is strong because nums[i] <= nums[j] <= 2*nums[i]
                # Also if nums[j] < nums[i], it will be covered when i is the smaller one.
                best = max(best, a ^ nums[j])
                j += 1

        return best
```

Attempt 5
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        # For each possible larger value b = nums[j], allowed a must satisfy:
        # |a - b| <= min(a, b). With a <= b, this becomes b - a <= a -> a >= ceil(b/2).
        # So for b at index j, we only need consider i in [lower_bound(ceil(b/2)), j].
        # Track maximum XOR among strong pairs using incremental bitwise trie.
        class TrieNode:
            __slots__ = ("nxt",)
            def __init__(self):
                self.nxt = [None, None]

        def insert(root, x):
            node = root
            for k in range(7, -1, -1):  # nums[i] <= 100 < 2^7; keep 0..7 to be safe
                b = (x >> k) & 1
                if node.nxt[b] is None:
                    node.nxt[b] = TrieNode()
                node = node.nxt[b]

        def max_xor_with(root, x):
            node = root
            best = 0
            for k in range(7, -1, -1):
                b = (x >> k) & 1
                want = 1 - b
                if node.nxt[want] is not None:
                    best |= 1 << k
                    node = node.nxt[want]
                else:
                    node = node.nxt[b]
            return best

        # Simple trie without deletion: we sweep increasing b and rebuild for each j window size
        # but that would be O(n^2 * bits). Instead, since n<=50 it's fine and simpler:
        # n^2 is 2500, bits ~ 8 => very fast. We'll brute strong pairs directly.
        for i in range(n):
            for j in range(i, n):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    ans = max(ans, x ^ y)
        return ans
```

Attempt 6
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Strong pair condition: for integers x,y with a = min(x,y), b = max(x,y),
        # we need |x-y| = b-a <= a  <=>  b <= 2a.
        #
        # Sort and use the fact nums[i] can only pair with nums[j] where nums[j] <= 2*nums[i]
        # for i <= j.
        nums.sort()
        n = len(nums)

        ans = 0
        left = 0

        # Build a binary trie for numbers in current eligible window [left..i]
        class Trie:
            __slots__ = ("child", "cnt")
            def __init__(self):
                self.child = [[-1, -1]]
                self.cnt = [0]

            def add(self, x: int):
                node = 0
                self.cnt[node] += 1
                for b in range(6, -1, -1):  # nums[i] <= 100 < 2^7
                    bit = (x >> b) & 1
                    nxt = self.child[node][bit]
                    if nxt == -1:
                        nxt = len(self.child)
                        self.child[node][bit] = nxt
                        self.child.append([-1, -1])
                        self.cnt.append(0)
                    node = nxt
                    self.cnt[node] += 1

            def remove(self, x: int):
                node = 0
                self.cnt[node] -= 1
                for b in range(6, -1, -1):
                    bit = (x >> b) & 1
                    node = self.child[node][bit]
                    self.cnt[node] -= 1

            def max_xor(self, x: int) -> int:
                # assumes trie is non-empty
                node = 0
                res = 0
                for b in range(6, -1, -1):
                    bit = (x >> b) & 1
                    want = 1 - bit
                    nxt = self.child[node][want]
                    if nxt != -1 and self.cnt[nxt] > 0:
                        res |= (1 << b)
                        node = nxt
                    else:
                        node = self.child[node][bit]
                return res

            def __len__(self):
                return self.cnt[0]

        trie = Trie()

        for i in range(n):
            # Move left until nums[i] <= 2*nums[left]
            while nums[i] > 2 * nums[left]:
                trie.remove(nums[left])
                left += 1

            # Now all nums[k] in [left..i] satisfy nums[i] <= 2*nums[k] for k>=left? Actually
            # because nums is sorted and k <= i, we have min(nums[k], nums[i]) = nums[k] and
            # condition requires nums[i] <= 2*nums[k]. With left chosen as above, this holds.
            if len(trie) > 0:
                ans = max(ans, trie.max_xor(nums[i]))

            trie.add(nums[i])

        return ans
```

Attempt 7
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Strong pair condition: |x-y| <= min(x,y)
        # For x<=y, this is y-x <= x  <=> y <= 2x.
        # So for each x, it can pair only with values in [x, 2x].
        #
        # Given nums[i] up to 100 and n up to 50, we can safely do:
        # - For each value as the smaller element, restrict j indices.
        # - Compute XOR max among those pairs (including same element).
        #
        # Complexity: O(n^2) worst-case (still tiny for constraints).
        ans = 0
        for i in range(n):
            x = nums[i]
            # Find the last index j such that nums[j] <= 2*x
            # Since sorted, just advance pointer or binary search.
            lo, hi = i, n - 1
            best_j = i
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= 2 * x:
                    best_j = mid
                    lo = mid + 1
                else:
                    hi = mid - 1

            for j in range(i, best_j + 1):
                ans = max(ans, x ^ nums[j])

        return ans
```

Attempt 8
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        best = 0

        # Strong pair condition:
        # |x - y| <= min(x, y)
        # Let a <= b => b - a <= a  <=>  b <= 2a
        # Therefore strong pairs are exactly those with
        # for each a, partner b must satisfy b <= 2a.
        for i in range(n):
            a = nums[i]
            j = i
            while j < n and nums[j] <= 2 * a:
                # compute xor with all valid b in [i..j)
                best = max(best, a ^ nums[j])
                j += 1

        return best
```

Attempt 9
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Sort and keep only distinct values (duplicates don't change achievable XOR
        # because we can always pick the same value twice).
        nums = sorted(set(nums))
        m = len(nums)
        ans = 0

        # Two-pointer window based on the strong-pair condition:
        # Need |x-y| <= min(x,y). If we consider x <= y, condition becomes y-x <= x => y <= 2x.
        # For each smaller value x at index i, all larger values y with y <= 2x are strong with x.
        j = 0
        for i in range(m):
            if j < i:
                j = i
            while j < m and nums[j] <= 2 * nums[i]:
                j += 1

            # Now nums[i..j-1] all satisfy strong-pair with nums[i] (since nums[i] <= nums[k] <= 2*nums[i])
            # Compute best XOR between nums[i] and those candidates.
            # Brute-force is fine: m <= 50.
            for k in range(i, j):
                ans = max(ans, nums[i] ^ nums[k])

        return ans
```

#### Partially Correct
Attempt 1
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # For strong pair (x,y): |x-y| <= min(x,y).
        # This is always true when x and y are sorted: for x <= y -> y-x <= x -> y <= 2x.
        nums = sorted(nums)
        n = len(nums)

        # Build candidate set: for each nums[i] as the smaller value,
        # any nums[j] with j <= upper_bound(2*nums[i]) can pair strongly with nums[i].
        # The optimal XOR will be achieved among these limited candidates.
        candidates = set()
        for i in range(n):
            x = nums[i]
            limit = 2 * x
            # find first index > limit
            lo, hi = i, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= limit:
                    lo = mid + 1
                else:
                    hi = mid
            # nums[i..lo-1] are within limit
            for k in range(i, lo):
                candidates.add(nums[k])

        cand = list(candidates)

        # Compute max XOR over all pairs in candidates (including same element twice).
        ans = 0
        m = len(cand)
        for i in range(m):
            for j in range(i, m):
                ans = max(ans, cand[i] ^ cand[j])
        return ans
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        best = 0

        # Strong pair condition:
        # |x - y| <= min(x, y)  <=>  max(x,y) <= 2*min(x,y)
        # With sorted array, for any x = nums[i] (as the smaller),
        # valid y are nums[j] where nums[j] <= 2*x.
        for i in range(n):
            x = nums[i]
            limit = 2 * x
            j = i
            while j < n and nums[j] <= limit:
                best = max(best, x ^ nums[j])
                j += 1

        return best
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # For strong pair condition:
        # |x - y| <= min(x, y)  (x, y >= 1)
        # Let wlog x >= y => x - y <= y => x <= 2y.
        # So (a, b) is strong iff max(a, b) <= 2 * min(a, b).

        nums = sorted(nums)
        ans = 0
        n = len(nums)

        # If we fix the larger element as nums[j], valid smaller elements nums[i] satisfy:
        # nums[i] >= ceil(nums[j] / 2). We'll check only those within this bound.
        for j in range(n):
            lo = (nums[j] + 1) // 2  # ceil(nums[j]/2)
            i = self._lower_bound(nums, lo, 0, j + 1)
            # Now nums[k] for k in [i, j] are all valid with nums[j]
            # Compute maximum XOR among this small range.
            # n<=50 so O(n^2) is fine.
            best = 0
            for k in range(i, j + 1):
                best = max(best, nums[k] ^ nums[j])
            ans = max(ans, best)

        return ans

    def _lower_bound(self, a: List[int], x: int, lo: int, hi: int) -> int:
        # first index in a[lo:hi] with a[idx] >= x
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Build list of candidate values for XOR:
        # For a strong pair (x,y) with x<=y: y-x <= x  => x <= y <= 2x
        # So for each x, y must lie in [x, 2x]. We'll only need to consider
        # the numbers within that window to get the maximum XOR.
        candidates = []
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j < n and nums[j] <= 2 * nums[i]:
                j += 1
            # all nums[i..j-1] can pair with nums[i]
            # collect boundary-ish values (all are fine due to small constraints)
            candidates.extend(nums[i:j])

        # Brute force over candidates (constraints are small, candidates are limited)
        # but still safe because nums[i] <= 100 and n<=50.
        best = 0
        # remove duplicates for speed
        cand = list(set(candidates))
        m = len(cand)
        for a in cand:
            for b in cand:
                if abs(a - b) <= min(a, b):
                    best = max(best, a ^ b)
        return best
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Strong pair condition: |x - y| <= min(x, y)
        # For x,y > 0, with x <= y: y-x <= x  -> y <= 2x
        # So for each smaller value a, valid b must satisfy a <= b <= 2a.

        nums.sort()
        best = 0

        # Only values in range [a, 2a] can pair with a as the smaller element.
        # nums[i] <= 100, so we can afford checking per i.
        for i in range(len(nums)):
            a = nums[i]
            j = i
            while j < len(nums) and nums[j] <= 2 * a:
                # (nums[i], nums[j]) is strong because nums[i] <= nums[j] <= 2*nums[i]
                # Also if nums[j] < nums[i], it will be covered when i is the smaller one.
                best = max(best, a ^ nums[j])
                j += 1

        return best
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        # For each possible larger value b = nums[j], allowed a must satisfy:
        # |a - b| <= min(a, b). With a <= b, this becomes b - a <= a -> a >= ceil(b/2).
        # So for b at index j, we only need consider i in [lower_bound(ceil(b/2)), j].
        # Track maximum XOR among strong pairs using incremental bitwise trie.
        class TrieNode:
            __slots__ = ("nxt",)
            def __init__(self):
                self.nxt = [None, None]

        def insert(root, x):
            node = root
            for k in range(7, -1, -1):  # nums[i] <= 100 < 2^7; keep 0..7 to be safe
                b = (x >> k) & 1
                if node.nxt[b] is None:
                    node.nxt[b] = TrieNode()
                node = node.nxt[b]

        def max_xor_with(root, x):
            node = root
            best = 0
            for k in range(7, -1, -1):
                b = (x >> k) & 1
                want = 1 - b
                if node.nxt[want] is not None:
                    best |= 1 << k
                    node = node.nxt[want]
                else:
                    node = node.nxt[b]
            return best

        # Simple trie without deletion: we sweep increasing b and rebuild for each j window size
        # but that would be O(n^2 * bits). Instead, since n<=50 it's fine and simpler:
        # n^2 is 2500, bits ~ 8 => very fast. We'll brute strong pairs directly.
        for i in range(n):
            for j in range(i, n):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    ans = max(ans, x ^ y)
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Strong pair condition: for integers x,y with a = min(x,y), b = max(x,y),
        # we need |x-y| = b-a <= a  <=>  b <= 2a.
        #
        # Sort and use the fact nums[i] can only pair with nums[j] where nums[j] <= 2*nums[i]
        # for i <= j.
        nums.sort()
        n = len(nums)

        ans = 0
        left = 0

        # Build a binary trie for numbers in current eligible window [left..i]
        class Trie:
            __slots__ = ("child", "cnt")
            def __init__(self):
                self.child = [[-1, -1]]
                self.cnt = [0]

            def add(self, x: int):
                node = 0
                self.cnt[node] += 1
                for b in range(6, -1, -1):  # nums[i] <= 100 < 2^7
                    bit = (x >> b) & 1
                    nxt = self.child[node][bit]
                    if nxt == -1:
                        nxt = len(self.child)
                        self.child[node][bit] = nxt
                        self.child.append([-1, -1])
                        self.cnt.append(0)
                    node = nxt
                    self.cnt[node] += 1

            def remove(self, x: int):
                node = 0
                self.cnt[node] -= 1
                for b in range(6, -1, -1):
                    bit = (x >> b) & 1
                    node = self.child[node][bit]
                    self.cnt[node] -= 1

            def max_xor(self, x: int) -> int:
                # assumes trie is non-empty
                node = 0
                res = 0
                for b in range(6, -1, -1):
                    bit = (x >> b) & 1
                    want = 1 - bit
                    nxt = self.child[node][want]
                    if nxt != -1 and self.cnt[nxt] > 0:
                        res |= (1 << b)
                        node = nxt
                    else:
                        node = self.child[node][bit]
                return res

            def __len__(self):
                return self.cnt[0]

        trie = Trie()

        for i in range(n):
            # Move left until nums[i] <= 2*nums[left]
            while nums[i] > 2 * nums[left]:
                trie.remove(nums[left])
                left += 1

            # Now all nums[k] in [left..i] satisfy nums[i] <= 2*nums[k] for k>=left? Actually
            # because nums is sorted and k <= i, we have min(nums[k], nums[i]) = nums[k] and
            # condition requires nums[i] <= 2*nums[k]. With left chosen as above, this holds.
            if len(trie) > 0:
                ans = max(ans, trie.max_xor(nums[i]))

            trie.add(nums[i])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Strong pair condition: |x-y| <= min(x,y)
        # For x<=y, this is y-x <= x  <=> y <= 2x.
        # So for each x, it can pair only with values in [x, 2x].
        #
        # Given nums[i] up to 100 and n up to 50, we can safely do:
        # - For each value as the smaller element, restrict j indices.
        # - Compute XOR max among those pairs (including same element).
        #
        # Complexity: O(n^2) worst-case (still tiny for constraints).
        ans = 0
        for i in range(n):
            x = nums[i]
            # Find the last index j such that nums[j] <= 2*x
            # Since sorted, just advance pointer or binary search.
            lo, hi = i, n - 1
            best_j = i
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= 2 * x:
                    best_j = mid
                    lo = mid + 1
                else:
                    hi = mid - 1

            for j in range(i, best_j + 1):
                ans = max(ans, x ^ nums[j])

        return ans
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        best = 0

        # Strong pair condition:
        # |x - y| <= min(x, y)
        # Let a <= b => b - a <= a  <=>  b <= 2a
        # Therefore strong pairs are exactly those with
        # for each a, partner b must satisfy b <= 2a.
        for i in range(n):
            a = nums[i]
            j = i
            while j < n and nums[j] <= 2 * a:
                # compute xor with all valid b in [i..j)
                best = max(best, a ^ nums[j])
                j += 1

        return best
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Sort and keep only distinct values (duplicates don't change achievable XOR
        # because we can always pick the same value twice).
        nums = sorted(set(nums))
        m = len(nums)
        ans = 0

        # Two-pointer window based on the strong-pair condition:
        # Need |x-y| <= min(x,y). If we consider x <= y, condition becomes y-x <= x => y <= 2x.
        # For each smaller value x at index i, all larger values y with y <= 2x are strong with x.
        j = 0
        for i in range(m):
            if j < i:
                j = i
            while j < m and nums[j] <= 2 * nums[i]:
                j += 1

            # Now nums[i..j-1] all satisfy strong-pair with nums[i] (since nums[i] <= nums[k] <= 2*nums[i])
            # Compute best XOR between nums[i] and those candidates.
            # Brute-force is fine: m <= 50.
            for k in range(i, j):
                ans = max(ans, nums[i] ^ nums[k])

        return ans
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # For strong pair (x,y): |x-y| <= min(x,y).
        # This is always true when x and y are sorted: for x <= y -> y-x <= x -> y <= 2x.
        nums = sorted(nums)
        n = len(nums)

        # Build candidate set: for each nums[i] as the smaller value,
        # any nums[j] with j <= upper_bound(2*nums[i]) can pair strongly with nums[i].
        # The optimal XOR will be achieved among these limited candidates.
        candidates = set()
        for i in range(n):
            x = nums[i]
            limit = 2 * x
            # find first index > limit
            lo, hi = i, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= limit:
                    lo = mid + 1
                else:
                    hi = mid
            # nums[i..lo-1] are within limit
            for k in range(i, lo):
                candidates.add(nums[k])

        cand = list(candidates)

        # Compute max XOR over all pairs in candidates (including same element twice).
        ans = 0
        m = len(cand)
        for i in range(m):
            for j in range(i, m):
                ans = max(ans, cand[i] ^ cand[j])
        return ans
```
```

</details>

### Parsed Memory Items

1. Constraint Rewriting with Min/Max Ordering
Description: Reformulate a symmetric inequality into a one-sided bound by assuming an order (min/max), which makes valid pairs correspond to a simple range relation.
<details>
<summary>Content 1</summary>

```text
When a condition involves |x−y| and min(x,y), pick a wlog order (e.g., treat one value as the smaller) to transform it into a monotone inequality like “larger ≤ constant × smaller.” This turns checking pair validity into checking membership in a numeric interval, enabling efficient enumeration strategies.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
The successful attempts consistently start by correctly rewriting the strong-pair condition into a simple inequality using an ordering assumption (min/max), then exploit sorted order to limit which elements can pair. They mostly use a “for each element, only consider partners within a bounded window” strategy, implemented either with two-pointers or binary-search for the window endpoints, and then brute-force within that small candidate set. Failures/partial solutions typically came from either (a) collecting candidates without preserving which pairings are actually valid with the chosen “smaller” element, (b) including unnecessary or incorrect candidates leading to invalid strong pairs during the final XOR maximization, or (c) overly complex approaches (e.g., trie sliding window) where maintaining correctness of the eligible window and pair condition is harder; the simpler window+brute-force versions avoid those pitfalls under small constraints.
```

</details>

2. Use Sorted Order to Restrict Search to Partner Windows
Description: After sorting, valid partners for a fixed element form a contiguous index range, so you only need to scan within that window to find optimal objective values.
<details>
<summary>Content 2</summary>

```text
Once the strong-pair condition becomes a bound of the form partner ≤ f(fixed), sorting guarantees all valid partners are clustered in one prefix of the suffix. Implement the window endpoints with two-pointers (incremental) or binary search (direct), then compute the objective (e.g., maximum XOR) only over pairs inside the window.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
The successful attempts consistently start by correctly rewriting the strong-pair condition into a simple inequality using an ordering assumption (min/max), then exploit sorted order to limit which elements can pair. They mostly use a “for each element, only consider partners within a bounded window” strategy, implemented either with two-pointers or binary-search for the window endpoints, and then brute-force within that small candidate set. Failures/partial solutions typically came from either (a) collecting candidates without preserving which pairings are actually valid with the chosen “smaller” element, (b) including unnecessary or incorrect candidates leading to invalid strong pairs during the final XOR maximization, or (c) overly complex approaches (e.g., trie sliding window) where maintaining correctness of the eligible window and pair condition is harder; the simpler window+brute-force versions avoid those pitfalls under small constraints.
```

</details>

3. Validate Candidate-Set Construction Against Pair-Specific Validity
Description: A candidate set used for the final maximization must preserve the property that every chosen pair is truly valid, not just that each element appears in some valid pairing.
<details>
<summary>Content 3</summary>

```text
If you aggregate elements that can pair with something (e.g., “belongs to a window for some smaller element”) but later take arbitrary pairs among them, you may create invalid pairs that were never jointly feasible under the original condition. Prefer computing the objective while iterating the same loop structure that enforces the pair-specific constraint, or explicitly ensure candidate pairing respects the interval bound for the chosen smaller element.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
The successful attempts consistently start by correctly rewriting the strong-pair condition into a simple inequality using an ordering assumption (min/max), then exploit sorted order to limit which elements can pair. They mostly use a “for each element, only consider partners within a bounded window” strategy, implemented either with two-pointers or binary-search for the window endpoints, and then brute-force within that small candidate set. Failures/partial solutions typically came from either (a) collecting candidates without preserving which pairings are actually valid with the chosen “smaller” element, (b) including unnecessary or incorrect candidates leading to invalid strong pairs during the final XOR maximization, or (c) overly complex approaches (e.g., trie sliding window) where maintaining correctness of the eligible window and pair condition is harder; the simpler window+brute-force versions avoid those pitfalls under small constraints.
```

</details>

4. Exploit Small Constraints with Correct Brute Force Inside Pruned Ranges
Description: When constraints are small, correctness can be prioritized by pruning candidates with the derived bound and then brute-forcing within the remaining limited set.
<details>
<summary>Content 4</summary>

```text
Instead of reaching for complex data structures, use the derived monotone validity condition to shrink the pair search from O(n²) to O(n·window) (often still small). Then brute-force all pairs inside each valid window to compute the maximum XOR, reducing the risk of subtle implementation errors.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
The successful attempts consistently start by correctly rewriting the strong-pair condition into a simple inequality using an ordering assumption (min/max), then exploit sorted order to limit which elements can pair. They mostly use a “for each element, only consider partners within a bounded window” strategy, implemented either with two-pointers or binary-search for the window endpoints, and then brute-force within that small candidate set. Failures/partial solutions typically came from either (a) collecting candidates without preserving which pairings are actually valid with the chosen “smaller” element, (b) including unnecessary or incorrect candidates leading to invalid strong pairs during the final XOR maximization, or (c) overly complex approaches (e.g., trie sliding window) where maintaining correctness of the eligible window and pair condition is harder; the simpler window+brute-force versions avoid those pitfalls under small constraints.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
The successful attempts consistently start by correctly rewriting the strong-pair condition into a simple inequality using an ordering assumption (min/max), then exploit sorted order to limit which elements can pair. They mostly use a “for each element, only consider partners within a bounded window” strategy, implemented either with two-pointers or binary-search for the window endpoints, and then brute-force within that small candidate set. Failures/partial solutions typically came from either (a) collecting candidates without preserving which pairings are actually valid with the chosen “smaller” element, (b) including unnecessary or incorrect candidates leading to invalid strong pairs during the final XOR maximization, or (c) overly complex approaches (e.g., trie sliding window) where maintaining correctness of the eligible window and pair condition is harder; the simpler window+brute-force versions avoid those pitfalls under small constraints.
</reasoning>

<memories>
<memory>
<title>Constraint Rewriting with Min/Max Ordering</title>
<description>Reformulate a symmetric inequality into a one-sided bound by assuming an order (min/max), which makes valid pairs correspond to a simple range relation.</description>
<content>When a condition involves |x−y| and min(x,y), pick a wlog order (e.g., treat one value as the smaller) to transform it into a monotone inequality like “larger ≤ constant × smaller.” This turns checking pair validity into checking membership in a numeric interval, enabling efficient enumeration strategies.</content>
</memory>

<memory>
<title>Use Sorted Order to Restrict Search to Partner Windows</title>
<description>After sorting, valid partners for a fixed element form a contiguous index range, so you only need to scan within that window to find optimal objective values.</description>
<content>Once the strong-pair condition becomes a bound of the form partner ≤ f(fixed), sorting guarantees all valid partners are clustered in one prefix of the suffix. Implement the window endpoints with two-pointers (incremental) or binary search (direct), then compute the objective (e.g., maximum XOR) only over pairs inside the window.</content>
</memory>

<memory>
<title>Validate Candidate-Set Construction Against Pair-Specific Validity</title>
<description>A candidate set used for the final maximization must preserve the property that every chosen pair is truly valid, not just that each element appears in some valid pairing.</description>
<content>If you aggregate elements that can pair with something (e.g., “belongs to a window for some smaller element”) but later take arbitrary pairs among them, you may create invalid pairs that were never jointly feasible under the original condition. Prefer computing the objective while iterating the same loop structure that enforces the pair-specific constraint, or explicitly ensure candidate pairing respects the interval bound for the chosen smaller element.</content>
</memory>

<memory>
<title>Exploit Small Constraints with Correct Brute Force Inside Pruned Ranges</title>
<description>When constraints are small, correctness can be prioritized by pruning candidates with the derived bound and then brute-forcing within the remaining limited set.</description>
<content>Instead of reaching for complex data structures, use the derived monotone validity condition to shrink the pair search from O(n²) to O(n·window) (often still small). Then brute-force all pairs inside each valid window to compute the maximum XOR, reducing the risk of subtle implementation errors.</content>
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
You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

|x - y| <= min(x, y)

You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
Return the maximum XOR value out of all possible strong pairs in the array nums.
Note that you can pick the same integer twice to form a pair.
 
Example 1:

Input: nums = [1,2,3,4,5]
Output: 7
Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.

Example 2:

Input: nums = [10,100]
Output: 0
Explanation: There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.

Example 3:

Input: nums = [5,6,25,30]
Output: 7
Explanation: There are 6 strong pairs in the array nums: (5, 5), (5, 6), (6, 6), (25, 25), (25, 30) and (30, 30).
The maximum XOR possible from these pairs is 25 XOR 30 = 7 since the only other non-zero XOR value is 5 XOR 6 = 3.

 
Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Condition |x - y| <= min(x, y) implies that if we let a <= b,
        # then b - a <= a  => b <= 2a.
        # So strong pairs are exactly pairs where max <= 2*min (with min chosen as smaller/equal).
        nums.sort()
        n = len(nums)

        # For each index i as the smaller number, consider candidates j where nums[j] <= 2*nums[i].
        # Any such (i, j) is strong.
        ans = 0
        # XOR candidates; array values are <= 100 so we can keep a small linear-time basis.
        # But easiest: the stronger property + small constraints allow O(n^2) enumeration.
        for i in range(n):
            limit = 2 * nums[i]
            j = i
            while j < n and nums[j] <= limit:
                ans = max(ans, nums[i] ^ nums[j])
                j += 1

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        
        # Strong pair condition: |x - y| <= min(x, y)
        # For sorted x<=y: y-x <= x  => y <= 2x
        # So for each x=nums[i], its valid partner values are <= 2*x.
        ans = 0
        
        for i in range(n):
            lo = nums[i]
            # Consider all nums[j] with nums[j] <= 2*lo (including itself).
            # This is O(n^2) but n<=50 so it's fine.
            limit = 2 * lo
            for j in range(i, n):
                if nums[j] > limit:
                    break
                ans = max(ans, lo ^ nums[j])
        
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Strong pair condition for x <= y:
        # y - x <= x  => y <= 2*x
        # So for each i (as the smaller element), j must satisfy nums[j] <= 2*nums[i].
        # Thus strong pairs only occur within this sliding window.
        best = 0
        for i in range(n):
            limit = 2 * nums[i]
            j = i
            while j < n and nums[j] <= limit:
                j += 1
            # Now nums[k] for k in [i, j-1] can pair strongly with nums[i]
            # Include xor with the same index i (also strong).
            for k in range(i, j):
                best = max(best, nums[i] ^ nums[k])
        return best
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Sort to use the strong-pair condition efficiently.
        nums.sort()
        n = len(nums)

        # Find the minimum x that can pair with each y: for strong pair (x,y),
        # with x <= y: |x-y| = y-x <= min(x,y)=x => y <= 2x => x >= ceil(y/2).
        # So for each y=nums[j], any x in nums[i..j] with nums[i] >= (y+1)//2 are valid.
        best = 0

        # Precompute prefixes for the sliding window [l..j] of valid candidates.
        # We'll just maintain a binary trie over the current window.
        # Window invariant: nums[l] >= ceil(nums[j]/2). (Also nums[l] <= nums[j].)
        l = 0

        class Trie:
            __slots__ = ("child",)
            def __init__(self):
                # child[node][0 or 1]
                self.child = [[-1, -1]]

            def insert(self, val: int):
                node = 0
                for b in range(7, -1, -1):  # nums[i] <= 100 < 2^7, but use 8 bits safely
                    bit = (val >> b) & 1
                    nxt = self.child[node][bit]
                    if nxt == -1:
                        nxt = len(self.child)
                        self.child[node][bit] = nxt
                        self.child.append([-1, -1])
                    node = nxt

            def max_xor(self, val: int) -> int:
                node = 0
                res = 0
                for b in range(7, -1, -1):
                    bit = (val >> b) & 1
                    # Prefer opposite bit
                    want = 1 - bit
                    nxt = self.child[node][want]
                    if nxt != -1:
                        res |= (1 << b)
                        node = nxt
                    else:
                        node = self.child[node][bit]
                        if node == -1:
                            break
                return res

        # Since deletions are needed for sliding window, use rebuild strategy:
        # n<=50, we can afford O(n^3) with trie rebuilds per j.
        # We'll rebuild trie for window [l..j] each time j advances.
        # Complexity: O(n^2 * bits + n^2) <= ~50^2*8 = 20k inserts, fine.
        for j in range(n):
            while nums[l] < (nums[j] + 1) // 2:
                l += 1

            # Build trie for current window nums[l..j]
            trie = Trie()
            for i in range(l, j + 1):
                trie.insert(nums[i])

            best = max(best, trie.max_xor(nums[j]))

        return best
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        # For a strong pair (x, y) with x <= y:
        # y - x <= x  => y <= 2x
        # so for each x, we only need y in [x, 2x].
        for i in range(n):
            x = nums[i]
            lo = i
            hi = 2 * x
            # find first index > hi
            r = lo
            while r < n and nums[r] <= hi:
                r += 1

            # compute max xor between nums[i] and nums[j] for j in [i, r)
            # (including i itself)
            for j in range(lo, r):
                ans = max(ans, x ^ nums[j])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Condition: |x - y| <= min(x, y)
        # For x <= y, this becomes y - x <= x  ->  y <= 2x
        # So for each x, y can be any number in [x, 2x] (including x itself).
        # Hence, for each i as the smaller element, we only need to consider j where nums[j] <= 2*nums[i].
        # Then compute maximum XOR among those strong pairs.
        #
        # Standard approach for constraints here: for each i in increasing order,
        # compute max XOR between nums[i] and all nums[j] in [i..r] using a bitwise trie.
        # We maintain a growing trie as r increases, but we must ensure only elements
        # <= 2*nums[i] are considered for each i, and elements < nums[i] are naturally excluded
        # since j >= i for x<=y after sorting.

        # We'll do two-pointer sweep with a trie over a moving window [i..r].
        # For each i, we want all y in [i..r(i)] where r(i) is max index with nums[r] <= 2*nums[i].
        # As i increments, r does not decrease; we remove elements that fall out of range on left.
        # Since trie doesn't support deletions easily, we'll instead just rebuild per i.
        # With nums[i] <= 100 and n<=50, rebuilding is still cheap:
        # O(n^2 * bits) with bits<=7 is fine.

        # Max value is <=100, so XOR fits within 0..127 (7 bits).
        MAX_BIT = 6  # since 2^6=64, 2^7=128

        class Trie:
            __slots__ = ("nxt", "cnt")
            def __init__(self):
                self.nxt = [[-1, -1]]
                self.cnt = [0]

            def add(self, val: int):
                node = 0
                self.cnt[node] += 1
                for b in range(MAX_BIT, -1, -1):
                    bit = (val >> b) & 1
                    if self.nxt[node][bit] == -1:
                        self.nxt[node][bit] = len(self.nxt)
                        self.nxt.append([-1, -1])
                        self.cnt.append(0)
                    node = self.nxt[node][bit]
                    self.cnt[node] += 1

            def best_xor(self, x: int) -> int:
                node = 0
                ans = 0
                for b in range(MAX_BIT, -1, -1):
                    bit = (x >> b) & 1
                    want = 1 - bit  # to maximize XOR
                    if self.nxt[node][want] != -1 and self.cnt[self.nxt[node][want]] > 0:
                        ans |= (1 << b)
                        node = self.nxt[node][want]
                    else:
                        node = self.nxt[node][bit]
                return ans

        res = 0
        for i in range(n):
            t = Trie()
            # j ranges over indices >= i where nums[j] <= 2*nums[i]
            # since nums is sorted, stop when condition fails.
            limit = 2 * nums[i]
            for j in range(i, n):
                if nums[j] > limit:
                    break
                t.add(nums[j])
            # maximum XOR with nums[i] against all valid nums[j]
            res = max(res, t.best_xor(nums[i]))
        return res
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Strong pair condition: |x-y| <= min(x,y).
        # For positive integers, this is equivalent to:
        # let m = min(x,y), M = max(x,y) => M - m <= m => M <= 2m.
        # So we need max XOR among pairs (a,b) such that max(a,b) <= 2*min(a,b).
        nums = sorted(nums)
        n = len(nums)
        ans = 0

        # For each i as the smaller element nums[i], only candidates j with nums[j] <= 2*nums[i]
        # can form a strong pair with it. We'll restrict to nearby values (range is small).
        # Since nums[i] <= 100, this is small; but we implement generically.
        for i in range(n):
            lo = nums[i]
            limit = 2 * lo
            j = i
            while j < n and nums[j] <= limit:
                j += 1
            # Candidates are nums[i..j-1] with nums[i] as min, plus we can allow equal indices
            # We'll compute best XOR between nums[i] and each candidate in the window.
            # Additionally, other pairs where the min is > nums[i] will be covered when that min is processed.
            for k in range(i, j):
                ans = max(ans, nums[i] ^ nums[k])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[-1]
        # For x <= y, condition |x-y| <= min(x,y) becomes y - x <= x  => y <= 2x
        # Thus strong pairs correspond to choosing indices i<=j with nums[j] <= 2*nums[i].

        # Greedy/bitwise filtering:
        # We only need to consider candidates within the bound for each element.
        # But constraints are small; we can instead enumerate all strong pairs with
        # a two-pointer and compute max XOR directly (O(n^2) with n<=50).
        n = len(nums)
        best = 0
        for i in range(n):
            for j in range(i, n):
                if nums[j] <= 2 * nums[i]:
                    best = max(best, nums[i] ^ nums[j])
                else:
                    break
        return best
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # If we pick x <= y, strong condition becomes:
        # y - x <= x  =>  y <= 2x
        # So for any x, we only need to consider y in [x, 2x].
        nums.sort()
        n = len(nums)

        # Build a binary trie over the subset of values that are <= current_limit (<= 2*nums[i])
        class TrieNode:
            __slots__ = ("nxt",)
            def __init__(self):
                self.nxt = [None, None]

        MAX_BIT = 7  # since nums[i] <= 100 < 128

        root = TrieNode()

        # Use a multiset-like trie by counting occurrences at nodes (via leaf counts),
        # to support adding/removing if needed. Here we only add as i increases,
        # so we can do without removals by constructing sets differently.
        #
        # However, we need, for each x=nums[i], the y to be within [x, 2x] and also >= x.
        # We'll instead do this by maintaining a trie of candidates y in [nums[i], 2*nums[i]]
        # using two pointers with add/remove.
        counts = {}  # not used

        # Trie with counts on each node
        class CountTrieNode:
            __slots__ = ("nxt", "cnt")
            def __init__(self):
                self.nxt = [None, None]
                self.cnt = 0

        root = CountTrieNode()

        def add(val: int, delta: int) -> None:
            node = root
            node.cnt += delta
            for b in range(MAX_BIT, -1, -1):
                bit = (val >> b) & 1
                if node.nxt[bit] is None:
                    node.nxt[bit] = CountTrieNode()
                node = node.nxt[bit]
                node.cnt += delta

        def max_xor_with(val: int) -> int:
            # Assumes trie not empty
            node = root
            ans = 0
            for b in range(MAX_BIT, -1, -1):
                bit = (val >> b) & 1
                want = 1 - bit
                if node.nxt[want] is not None and node.nxt[want].cnt > 0:
                    ans |= (1 << b)
                    node = node.nxt[want]
                else:
                    node = node.nxt[bit]
            return ans

        ans = 0
        j = 0  # will expand right pointer
        # Two pointers: i is left endpoint x, maintain candidates in trie for y in [nums[i], 2*nums[i]]
        # Start by adding nothing; then for each i add until <= 2*nums[i], and remove nums < nums[i].
        for i in range(n):
            x = nums[i]
            right_limit = 2 * x

            # Add all nums[j] <= right_limit
            while j < n and nums[j] <= right_limit:
                add(nums[j], +1)
                j += 1

            # Remove nums that are < x from trie (i.e., ensure minimum is nums[i])
            # Because we move i forward, we need to remove nums[i-1] each iteration.
            # We'll do it lazily: when i > 0, remove nums[i-1].
            if i > 0:
                add(nums[i - 1], -1)

            # Now trie contains exactly nums[k] for k in [i, j-1] (all y candidates >= x and <= 2x)
            if root.cnt > 0:
                ans = max(ans, max_xor_with(x))

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Strong condition: |x-y| <= min(x,y) for nonnegative integers.
        # This is equivalent to max(x,y) <= 2*min(x,y).
        # Hence only values in [v/2, 2v] around v can pair with v.
        nums_sorted = sorted(nums)
        n = len(nums_sorted)
        ans = 0

        # Trie for maximum XOR queries among values within current sliding window.
        class TrieNode:
            __slots__ = ("ch",)
            def __init__(self):
                self.ch = [None, None]

        def insert(root, val):
            node = root
            for b in range(7, -1, -1):  # nums[i] <= 100 < 2^7, but keep 8 bits for safety
                bit = (val >> b) & 1
                if node.ch[bit] is None:
                    node.ch[bit] = TrieNode()
                node = node.ch[bit]

        # For removal, we use a count-augmented trie
        class CTrieNode:
            __slots__ = ("ch", "cnt")
            def __init__(self):
                self.ch = [None, None]
                self.cnt = 0

        def insert_ct(root, val):
            node = root
            node.cnt += 1
            for b in range(7, -1, -1):
                bit = (val >> b) & 1
                if node.ch[bit] is None:
                    node.ch[bit] = CTrieNode()
                node = node.ch[bit]
                node.cnt += 1

        def remove_ct(root, val):
            node = root
            node.cnt -= 1
            for b in range(7, -1, -1):
                bit = (val >> b) & 1
                nxt = node.ch[bit]
                nxt.cnt -= 1
                node = nxt

        def query_max_xor(root, val):
            node = root
            res = 0
            for b in range(7, -1, -1):
                bit = (val >> b) & 1
                want = 1 - bit
                if node.ch[want] is not None and node.ch[want].cnt > 0:
                    res |= (1 << b)
                    node = node.ch[want]
                else:
                    node = node.ch[bit]
            return res

        root = CTrieNode()

        # Sliding window: for each right index j, maintain i..j-1 such that
        # nums_sorted[i] >= ceil(nums_sorted[j]/2) and nums_sorted[j] <= 2*nums_sorted[i].
        i = 0
        for j in range(n):
            v = nums_sorted[j]
            # Ensure window left bound: nums[i] >= ceil(v/2)
            while i < j and nums_sorted[i] * 2 < v:
                # remove nums_sorted[i] from trie
                remove_ct(root, nums_sorted[i])
                i += 1

            # Now all nums[k] in [i, j-1] satisfy v <= 2*nums[k] (equivalently nums[k]*2 >= v)
            # Also need |v - nums[k]| <= nums[k] => v - nums[k] <= nums[k] => v <= 2*nums[k],
            # and since nums[k] <= v (window is earlier), other side holds automatically.

            # Query against current window plus also allow pairing with itself:
            # To allow (v, v), we insert v first and query, or query with existing window and then insert.
            # We'll insert v temporarily via query after insertion.
            insert_ct(root, v)
            ans = max(ans, query_max_xor(root, v))

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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
Before solving, consider these reusable insights from prior analysis:

  1. Constraint Rewriting with Min/Max Ordering: Reformulate a symmetric inequality into a one-sided bound by assuming an order (min/max), which makes valid pairs correspond to a simple range relation.
     When a condition involves |x−y| and min(x,y), pick a wlog order (e.g., treat one value as the smaller) to transform it into a monotone inequality like “larger ≤ constant × smaller.” This turns checking pair validity into checking membership in a numeric interval, enabling efficient enumeration strategies.
  2. Use Sorted Order to Restrict Search to Partner Windows: After sorting, valid partners for a fixed element form a contiguous index range, so you only need to scan within that window to find optimal objective values.
     Once the strong-pair condition becomes a bound of the form partner ≤ f(fixed), sorting guarantees all valid partners are clustered in one prefix of the suffix. Implement the window endpoints with two-pointers (incremental) or binary search (direct), then compute the objective (e.g., maximum XOR) only over pairs inside the window.
  3. Validate Candidate-Set Construction Against Pair-Specific Validity: A candidate set used for the final maximization must preserve the property that every chosen pair is truly valid, not just that each element appears in some valid pairing.
     If you aggregate elements that can pair with something (e.g., “belongs to a window for some smaller element”) but later take arbitrary pairs among them, you may create invalid pairs that were never jointly feasible under the original condition. Prefer computing the objective while iterating the same loop structure that enforces the pair-specific constraint, or explicitly ensure candidate pairing respects the interval bound for the chosen smaller element.
  4. Exploit Small Constraints with Correct Brute Force Inside Pruned Ranges: When constraints are small, correctness can be prioritized by pruning candidates with the derived bound and then brute-forcing within the remaining limited set.
     Instead of reaching for complex data structures, use the derived monotone validity condition to shrink the pair search from O(n²) to O(n·window) (often still small). Then brute-force all pairs inside each valid window to compute the maximum XOR, reducing the risk of subtle implementation errors.

Apply these insights to the problem below.

### Question:
You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

|x - y| <= min(x, y)

You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
Return the maximum XOR value out of all possible strong pairs in the array nums.
Note that you can pick the same integer twice to form a pair.
 
Example 1:

Input: nums = [1,2,3,4,5]
Output: 7
Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.

Example 2:

Input: nums = [10,100]
Output: 0
Explanation: There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.

Example 3:

Input: nums = [5,6,25,30]
Output: 7
Explanation: There are 6 strong pairs in the array nums: (5, 5), (5, 6), (6, 6), (25, 25), (25, 30) and (30, 30).
The maximum XOR possible from these pairs is 25 XOR 30 = 7 since the only other non-zero XOR value is 5 XOR 6 = 3.

 
Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        ans = 0
        # For each x = nums[i] as the larger element, strong pair condition:
        # |x-y| <= min(x,y). With y <= x => x - y <= y => x <= 2y => y >= ceil(x/2)
        # So for fixed i, valid j are contiguous indices in [lower_bound(x/2), i].
        for i in range(n):
            x = nums[i]
            lo_val = (x + 1) // 2  # ceil(x/2)
            # lower_bound of lo_val in nums[0..i]
            lo, hi = 0, i
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= lo_val:
                    hi = mid
                else:
                    lo = mid + 1
            start = lo

            # brute force all valid partners for this i
            for j in range(start, i + 1):
                ans = max(ans, nums[i] ^ nums[j])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For x <= y: |y-x| <= min(x,y) = x  => y - x <= x  => y <= 2x
        # So for a fixed smaller value x = nums[i], valid partners are nums[j] in [i..hi]
        # where nums[j] <= 2*nums[i].
        for i in range(n):
            hi_val = 2 * nums[i]
            # find the last index j such that nums[j] <= 2*nums[i]
            lo, hi = i, n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= hi_val:
                    lo = mid + 1
                else:
                    hi = mid - 1
            last = hi  # last valid partner index

            for j in range(i, last + 1):
                ans = max(ans, nums[i] ^ nums[j])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # If x <= y then |x-y| <= x  <=>  y - x <= x  <=>  y <= 2x
        # So for each x=nums[i], all strong partners are in nums[j] where i <= j and nums[j] <= 2*nums[i].
        for i in range(n):
            limit = 2 * nums[i]

            # find rightmost j such that nums[j] <= limit
            lo, hi = i, n - 1
            r = i - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= limit:
                    r = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            if r < i:
                continue

            # brute-force XOR within the valid window [i, r]
            for j in range(i, r + 1):
                ans = max(ans, nums[i] ^ nums[j])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Since |x-y| <= min(x,y):
        # WLOG let x <= y (so min = x). Then y - x <= x => y <= 2x.
        # For each i as the smaller element, valid partners j satisfy i <= j <= upper_bound(2*nums[i]).
        ans = 0

        for i in range(n):
            lo = i  # j must be >= i because nums[i] is the smaller (or equal)
            hi_val = 2 * nums[i]

            # binary search for first index > hi_val, then valid j are [i, idx-1]
            l, r = i, n
            while l < r:
                m = (l + r) // 2
                if nums[m] <= hi_val:
                    l = m + 1
                else:
                    r = m
            hi = l  # exclusive upper index

            # brute force all pairs within this valid window
            for j in range(lo, hi):
                ans = max(ans, nums[i] ^ nums[j])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For a strong pair (x, y), wlog let y <= x.
        # Condition: x - y <= y  =>  x <= 2y
        # After sorting, for each index i (as the larger element nums[i]),
        # valid partners j are those with nums[j] >= ceil(nums[i]/2) and nums[j] <= nums[i].
        for i in range(n):
            lo_val = (nums[i] + 1) // 2  # ceil(nums[i]/2)
            # binary search first index j in [0..i] such that nums[j] >= lo_val
            l, r = 0, i
            while l < r:
                m = (l + r) // 2
                if nums[m] >= lo_val:
                    r = m
                else:
                    l = m + 1
            start = l
            # brute-force all j in the valid window [start..i]
            for j in range(start, i + 1):
                ans = max(ans, nums[i] ^ nums[j])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For fixed y as the larger element, condition becomes:
        # let x = smaller (or equal). Then y - x <= x  => y <= 2x  => x >= ceil(y/2)
        for j in range(n):
            y = nums[j]
            left_val = (y + 1) // 2  # ceil(y/2)
            # find smallest i such that nums[i] >= left_val
            lo, hi = 0, j
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= left_val:
                    hi = mid
                else:
                    lo = mid + 1
            i0 = lo

            # brute force all valid i in [i0, j] for max xor with nums[j]
            for i in range(i0, j + 1):
                ans = max(ans, nums[i] ^ y)

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For x <= y, condition |x-y| <= min(x,y) becomes y - x <= x  =>  y <= 2x
        # So for a fixed smaller value x = nums[i], valid partners are nums[j] with i <= j <= hi,
        # where nums[j] <= 2*nums[i].
        for i in range(n):
            hi_val = 2 * nums[i]
            # binary search for upper bound of hi_val in nums
            l, r = i, n  # [l, r)
            while l < r:
                m = (l + r) // 2
                if nums[m] <= hi_val:
                    l = m + 1
                else:
                    r = m
            hi = l - 1
            for j in range(i, hi + 1):
                ans = max(ans, nums[i] ^ nums[j])
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For strong pair (x, y) with x >= y:
        # |x-y| <= min(x,y)  =>  x - y <= y  =>  x <= 2y
        # We'll iterate y as the smaller element and consider x in (y .. 2y].
        for i in range(n):
            y = nums[i]
            # Find largest index j such that nums[j] <= 2*y, and j >= i
            hi_val = 2 * y
            j = i
            while j + 1 < n and nums[j + 1] <= hi_val:
                j += 1

            # brute force all x candidates in window [i..j]
            for k in range(i, j + 1):
                ans = max(ans, nums[i] ^ nums[k])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        # For x <= y: |x-y| <= min(x,y)  =>  y - x <= x  =>  y <= 2x
        # So for each nums[i] as the smaller one, valid partners are nums[j] with:
        # i <= j < upper such that nums[j] <= 2*nums[i]
        for i in range(n):
            upper_val = 2 * nums[i]
            # binary search for first index > upper_val
            lo, hi = i, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= upper_val:
                    lo = mid + 1
                else:
                    hi = mid
            upper = lo  # valid j are in [i, upper)

            # brute force within the valid window
            for j in range(i, upper):
                ans = max(ans, nums[i] ^ nums[j])

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Condition: |x-y| <= min(x,y)
        # Assume wlog y >= x > 0. Then y - x <= x  => y <= 2x.
        # Also if x == y, always strong.
        #
        # We'll sort nums, and for each index i as the smaller value nums[i],
        # valid partners are indices j where nums[j] <= 2*nums[i] (and j >= i
        # to respect y >= x). Then brute-force XOR inside this window.
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n):
            limit = 2 * nums[i]
            # Find last index j with nums[j] <= limit
            # Since n<=50, simple linear scan is fine and safe.
            j = i
            while j < n and nums[j] <= limit:
                ans = max(ans, nums[i] ^ nums[j])
                j += 1

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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
      "error": ""
    },
    {
      "passed": true,
      "expected": "127",
      "actual": "127",
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
