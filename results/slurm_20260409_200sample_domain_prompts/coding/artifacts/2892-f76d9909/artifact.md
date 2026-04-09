# Problem 2892

- Domain: `coding`

## Problem

```text
You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
Return true if the given array is good, otherwise return false.
Note: A permutation of integers represents an arrangement of these numbers.
 
Example 1:

Input: nums = [2, 1, 3]
Output: false
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

Example 2:

Input: nums = [1, 3, 3, 2]
Output: true
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.
Example 3:

Input: nums = [1, 1]
Output: true
Explanation: Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.
Example 4:

Input: nums = [3, 4, 4, 1, 2, 1]
Output: false
Explanation: Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.

 
Constraints:

1 <= nums.length <= 100
1 <= num[i] <= 200
```

### Starter Code

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
```

### Test Cases

```json
[
  {
    "input": "[2, 1, 3]",
    "output": "false",
    "testtype": "functional"
  },
  {
    "input": "[1, 3, 3, 2]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[1, 1]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[3, 4, 4, 1, 2, 1]",
    "output": "false",
    "testtype": "functional"
  },
  {
    "input": "[1, 1]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[1, 2, 2]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[1, 4, 2, 3]",
    "output": "false",
    "testtype": "functional"
  },
  {
    "input": "[1, 3, 4, 4, 2]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[3, 2, 5, 5, 1, 4]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[4, 1, 2, 6, 6, 5, 3]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[3, 7, 7, 6, 5, 4, 1, 2]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[10, 9, 2, 7, 1, 4, 8, 5, 11, 3, 6, 11]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[18, 14, 16, 20, 33, 3, 24, 11, 22, 2, 46, 17, 29, 28, 38, 40, 48, 21, 19, 4, 15, 8, 39, 27, 51, 12, 44, 7, 30, 23, 26, 13, 32, 42, 52, 9, 47, 6, 34, 10, 50, 45, 36, 31, 49, 35, 1, 5, 37, 25, 41, 52, 43]",
    "output": "true",
    "testtype": "functional"
  },
  {
    "input": "[83, 132, 194, 188, 59, 167, 116, 199, 164, 94, 12, 163, 128, 30, 92, 9, 151, 169, 121, 58, 170, 62, 186, 29, 189, 75, 100, 74, 89, 173, 162, 126, 2, 108, 86, 182, 122, 64, 43, 47, 37, 49, 197, 21, 144, 18, 112, 150, 40, 157, 97, 20, 129, 95, 68, 66, 142, 76, 48, 172, 84, 139, 99, 25, 1, 119, 41, 143, 180, 90, 24, 161, 73, 196, 82, 35, 135, 153, 8, 134, 13, 146, 5, 39, 133, 55, 198, 178, 171, 53, 137]",
    "output": "false",
    "testtype": "functional"
  },
  {
    "input": "[106, 78, 121, 76, 160, 104, 82, 47, 158, 151, 62, 134, 113, 74, 51, 121, 67, 87, 37, 199, 41, 90, 58, 48, 198, 101, 44, 177, 107, 112, 167, 20, 66, 35, 131, 102, 181, 191, 73, 83, 88, 135, 183, 50, 30, 186, 40, 38, 60, 17, 57, 133, 153, 174, 122, 86, 196, 95, 103, 69, 64, 123, 111, 89, 147, 19, 56, 164, 16, 184, 189, 25, 125, 129, 195, 139, 68, 55, 45, 99, 23, 180, 77, 144, 32, 152, 27, 175, 81, 193, 143, 182]",
    "output": "false",
    "testtype": "functional"
  },
  {
    "input": "[95, 53, 23, 8, 119, 1, 148, 179, 70, 185, 132, 161, 87, 80, 99, 60, 10, 115, 124, 73, 79, 71, 89, 58, 77, 111, 50, 167, 141, 189, 74, 82, 40, 22, 68, 13, 190, 30, 52, 45, 103, 177, 25, 158, 153, 15, 186, 3, 118, 105, 32, 91, 137, 108, 90, 112, 168, 156, 46, 191, 93, 139, 195, 135, 28, 155, 131, 17, 67, 169, 138, 144, 110, 78, 150, 154, 38, 64, 163, 55, 25, 48, 147, 11, 81, 33, 128, 198, 26, 140, 188, 182, 199, 171, 62, 6, 146, 37]",
    "output": "false",
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
You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
Return true if the given array is good, otherwise return false.
Note: A permutation of integers represents an arrangement of these numbers.
 
Example 1:

Input: nums = [2, 1, 3]
Output: false
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

Example 2:

Input: nums = [1, 3, 3, 2]
Output: true
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.
Example 3:

Input: nums = [1, 1]
Output: true
Explanation: Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.
Example 4:

Input: nums = [3, 4, 4, 1, 2, 1]
Output: false
Explanation: Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.

 
Constraints:

1 <= nums.length <= 100
1 <= num[i] <= 200

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
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
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False

        # base[n] contains 1..n-1 exactly once and n exactly twice
        freq = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            freq[x] += 1

        # Check counts for 1..n-1 and n
        for v in range(1, n):
            if freq[v] != 1:
                return False
        return freq[n] == 2
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1 (contains 1..n-1 once, and n twice)
        if len(nums) != n + 1:
            return False

        cnt = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            cnt[x] += 1

        # Check: 1..n-1 exactly once, and n exactly twice
        for i in range(1, n):
            if cnt[i] != 1:
                return False
        return cnt[n] == 2
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False

        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1

        # nums must contain 1..n-1 exactly once, and n exactly twice
        for i in range(1, n):
            if cnt.get(i, 0) != 1:
                return False
        return cnt.get(n, 0) == 2
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1, so nums must match
        if len(nums) != n + 1:
            return False

        # All values 1..n-1 must appear exactly once, and n must appear exactly twice
        cnt = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            cnt[x] += 1

        for i in range(1, n):
            if cnt[i] != 1:
                return False
        return cnt[n] == 2
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1 with 1..n-1 each exactly once and n exactly twice
        if len(nums) != n + 1:
            return False
        
        cnt = Counter(nums)
        # n must appear exactly twice
        if cnt[n] != 2:
            return False
        
        # all numbers 1..n-1 must appear exactly once
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False
        
        # no other values can exist (shouldn't, given the checks, but keep it safe)
        for x in cnt:
            if x < 1 or x > n:
                return False
        
        return True
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False
        
        c = Counter(nums)
        # Must contain 1..n-1 exactly once, and n exactly twice
        for x in range(1, n):
            if c.get(x, 0) != 1:
                return False
        if c.get(n, 0) != 2:
            return False
        
        return True
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1, and contains 1..n-1 exactly once, and n twice
        if len(nums) != n + 1:
            return False

        cnt = Counter(nums)
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False
        if cnt.get(n, 0) != 2:
            return False

        return True
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)
        n = mx
        # base[n] has length n + 1, but nums must match length exactly
        if len(nums) != n + 1:
            return False

        # nums should contain 1..n-1 exactly once, and n exactly twice
        # Build frequency and validate.
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # n must appear exactly twice
        if freq.get(n, 0) != 2:
            return False

        # each 1..n-1 must appear exactly once
        for v in range(1, n):
            if freq.get(v, 0) != 1:
                return False

        return True
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False

        cnt = Counter(nums)
        # Must contain 1..n-1 exactly once each
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False
        # Must contain n exactly twice
        return cnt.get(n, 0) == 2
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # Let n be the maximum value. Then any candidate base[n] must match:
        # - length of nums must be n+1
        # - all numbers 1..n-1 appear exactly once
        # - n appears exactly twice
        n = max(nums)
        if len(nums) != n + 1:
            return False

        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1

        # n must appear exactly twice
        if cnt.get(n, 0) != 2:
            return False

        # numbers 1..n-1 must each appear exactly once
        for v in range(1, n):
            if cnt.get(v, 0) != 1:
                return False

        # no other values can appear (though constraints + max check generally prevent it)
        # ensure all keys are within 1..n
        for x in cnt:
            if x < 1 or x > n:
                return False

        return True
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False

        # base[n] contains 1..n-1 exactly once and n exactly twice
        freq = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            freq[x] += 1

        # Check counts for 1..n-1 and n
        for v in range(1, n):
            if freq[v] != 1:
                return False
        return freq[n] == 2
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1 (contains 1..n-1 once, and n twice)
        if len(nums) != n + 1:
            return False

        cnt = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            cnt[x] += 1

        # Check: 1..n-1 exactly once, and n exactly twice
        for i in range(1, n):
            if cnt[i] != 1:
                return False
        return cnt[n] == 2
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False

        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1

        # nums must contain 1..n-1 exactly once, and n exactly twice
        for i in range(1, n):
            if cnt.get(i, 0) != 1:
                return False
        return cnt.get(n, 0) == 2
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1, so nums must match
        if len(nums) != n + 1:
            return False

        # All values 1..n-1 must appear exactly once, and n must appear exactly twice
        cnt = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            cnt[x] += 1

        for i in range(1, n):
            if cnt[i] != 1:
                return False
        return cnt[n] == 2
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1 with 1..n-1 each exactly once and n exactly twice
        if len(nums) != n + 1:
            return False
        
        cnt = Counter(nums)
        # n must appear exactly twice
        if cnt[n] != 2:
            return False
        
        # all numbers 1..n-1 must appear exactly once
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False
        
        # no other values can exist (shouldn't, given the checks, but keep it safe)
        for x in cnt:
            if x < 1 or x > n:
                return False
        
        return True
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False
        
        c = Counter(nums)
        # Must contain 1..n-1 exactly once, and n exactly twice
        for x in range(1, n):
            if c.get(x, 0) != 1:
                return False
        if c.get(n, 0) != 2:
            return False
        
        return True
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1, and contains 1..n-1 exactly once, and n twice
        if len(nums) != n + 1:
            return False

        cnt = Counter(nums)
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False
        if cnt.get(n, 0) != 2:
            return False

        return True
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)
        n = mx
        # base[n] has length n + 1, but nums must match length exactly
        if len(nums) != n + 1:
            return False

        # nums should contain 1..n-1 exactly once, and n exactly twice
        # Build frequency and validate.
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # n must appear exactly twice
        if freq.get(n, 0) != 2:
            return False

        # each 1..n-1 must appear exactly once
        for v in range(1, n):
            if freq.get(v, 0) != 1:
                return False

        return True
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False

        cnt = Counter(nums)
        # Must contain 1..n-1 exactly once each
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False
        # Must contain n exactly twice
        return cnt.get(n, 0) == 2
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # Let n be the maximum value. Then any candidate base[n] must match:
        # - length of nums must be n+1
        # - all numbers 1..n-1 appear exactly once
        # - n appears exactly twice
        n = max(nums)
        if len(nums) != n + 1:
            return False

        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1

        # n must appear exactly twice
        if cnt.get(n, 0) != 2:
            return False

        # numbers 1..n-1 must each appear exactly once
        for v in range(1, n):
            if cnt.get(v, 0) != 1:
                return False

        # no other values can appear (though constraints + max check generally prevent it)
        # ensure all keys are within 1..n
        for x in cnt:
            if x < 1 or x > n:
                return False

        return True
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
You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
Return true if the given array is good, otherwise return false.
Note: A permutation of integers represents an arrangement of these numbers.
 
Example 1:

Input: nums = [2, 1, 3]
Output: false
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

Example 2:

Input: nums = [1, 3, 3, 2]
Output: true
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.
Example 3:

Input: nums = [1, 1]
Output: true
Explanation: Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.
Example 4:

Input: nums = [3, 4, 4, 1, 2, 1]
Output: false
Explanation: Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.

 
Constraints:

1 <= nums.length <= 100
1 <= num[i] <= 200

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
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
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1, and contains 1..n-1 exactly once and n twice.
        if len(nums) != n + 1:
            return False

        count = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            count[x] += 1

        # Numbers 1..n-1 must appear exactly once
        for i in range(1, n):
            if count[i] != 1:
                return False

        # n must appear exactly twice
        return count[n] == 2
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)

        # base[n] has length n+1
        if len(nums) != n + 1:
            return False

        cnt = Counter(nums)

        # Numbers 1..n-1 appear exactly once, and n appears exactly twice
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False
        return cnt.get(n, 0) == 2
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        expected_len = n + 1
        if len(nums) != expected_len:
            return False
        
        freq = Counter(nums)
        for x in range(1, n):
            if freq.get(x, 0) != 1:
                return False
        return freq.get(n, 0) == 2
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1 and consists of 1..n-1 once, and n twice
        if len(nums) != n + 1:
            return False

        cnt = Counter(nums)
        # n must appear exactly twice
        if cnt.get(n, 0) != 2:
            return False

        # all numbers 1..n-1 must appear exactly once
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False

        # no other numbers can appear (covered by length check + above constraints)
        return True
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1, consisting of 1..n-1 each once and n twice
        if len(nums) != n + 1:
            return False

        cnt = [0] * (n + 1)
        for x in nums:
            if x > n:  # can't happen since n is max, but keeps logic safe
                return False
            cnt[x] += 1

        # Must contain 1..n-1 exactly once
        for i in range(1, n):
            if cnt[i] != 1:
                return False
        # n must appear exactly twice
        return cnt[n] == 2
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        base_len = n + 1
        if len(nums) != base_len:
            return False

        cnt = Counter(nums)

        # n must appear exactly twice
        if cnt[n] != 2:
            return False

        # numbers 1..n-1 must each appear exactly once
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False

        # no other values (though constraints imply positive integers only)
        # This check is cheap and safe.
        for x in cnt:
            if x < 1 or x > n:
                return False

        return True
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False
        # Must contain 1..n-1 exactly once and n exactly twice
        cnt = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            cnt[x] += 1
        for i in range(1, n):
            if cnt[i] != 1:
                return False
        return cnt[n] == 2
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False
        
        # Count occurrences: 1..n-1 exactly once, and n exactly twice
        cnt = [0] * (n + 1)
        for x in nums:
            if x > n:  # safety (shouldn't happen since n = max(nums))
                return False
            cnt[x] += 1
        
        for v in range(1, n):
            if cnt[v] != 1:
                return False
        return cnt[n] == 2
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        # base[m] has length m+1
        return len(nums) == m + 1 and nums.count(m) == 2 and len(set(nums)) == m
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1
        if len(nums) != n + 1:
            return False

        # base[n] should contain 1..n-1 exactly once, and n exactly twice
        cnt = [0] * (n + 1)
        for x in nums:
            if x > n or x < 1:
                return False
            cnt[x] += 1

        for v in range(1, n):
            if cnt[v] != 1:
                return False
        return cnt[n] == 2
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1, and contains 1..n-1 exactly once and n twice.
        if len(nums) != n + 1:
            return False

        count = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            count[x] += 1

        # Numbers 1..n-1 must appear exactly once
        for i in range(1, n):
            if count[i] != 1:
                return False

        # n must appear exactly twice
        return count[n] == 2
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)

        # base[n] has length n+1
        if len(nums) != n + 1:
            return False

        cnt = Counter(nums)

        # Numbers 1..n-1 appear exactly once, and n appears exactly twice
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False
        return cnt.get(n, 0) == 2
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        expected_len = n + 1
        if len(nums) != expected_len:
            return False
        
        freq = Counter(nums)
        for x in range(1, n):
            if freq.get(x, 0) != 1:
                return False
        return freq.get(n, 0) == 2
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1 and consists of 1..n-1 once, and n twice
        if len(nums) != n + 1:
            return False

        cnt = Counter(nums)
        # n must appear exactly twice
        if cnt.get(n, 0) != 2:
            return False

        # all numbers 1..n-1 must appear exactly once
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False

        # no other numbers can appear (covered by length check + above constraints)
        return True
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1, consisting of 1..n-1 each once and n twice
        if len(nums) != n + 1:
            return False

        cnt = [0] * (n + 1)
        for x in nums:
            if x > n:  # can't happen since n is max, but keeps logic safe
                return False
            cnt[x] += 1

        # Must contain 1..n-1 exactly once
        for i in range(1, n):
            if cnt[i] != 1:
                return False
        # n must appear exactly twice
        return cnt[n] == 2
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        base_len = n + 1
        if len(nums) != base_len:
            return False

        cnt = Counter(nums)

        # n must appear exactly twice
        if cnt[n] != 2:
            return False

        # numbers 1..n-1 must each appear exactly once
        for x in range(1, n):
            if cnt.get(x, 0) != 1:
                return False

        # no other values (though constraints imply positive integers only)
        # This check is cheap and safe.
        for x in cnt:
            if x < 1 or x > n:
                return False

        return True
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False
        # Must contain 1..n-1 exactly once and n exactly twice
        cnt = [0] * (n + 1)
        for x in nums:
            if x < 1 or x > n:
                return False
            cnt[x] += 1
        for i in range(1, n):
            if cnt[i] != 1:
                return False
        return cnt[n] == 2
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n + 1
        if len(nums) != n + 1:
            return False
        
        # Count occurrences: 1..n-1 exactly once, and n exactly twice
        cnt = [0] * (n + 1)
        for x in nums:
            if x > n:  # safety (shouldn't happen since n = max(nums))
                return False
            cnt[x] += 1
        
        for v in range(1, n):
            if cnt[v] != 1:
                return False
        return cnt[n] == 2
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        # base[m] has length m+1
        return len(nums) == m + 1 and nums.count(m) == 2 and len(set(nums)) == m
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        # base[n] has length n+1
        if len(nums) != n + 1:
            return False

        # base[n] should contain 1..n-1 exactly once, and n exactly twice
        cnt = [0] * (n + 1)
        for x in nums:
            if x > n or x < 1:
                return False
            cnt[x] += 1

        for v in range(1, n):
            if cnt[v] != 1:
                return False
        return cnt[n] == 2
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
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
  "passed": 16,
  "total": 16,
  "cases": [
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "true",
      "actual": "True",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    },
    {
      "passed": true,
      "expected": "false",
      "actual": "False",
      "error": ""
    }
  ]
}
```

</details>
