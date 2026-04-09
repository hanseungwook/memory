# Problem 2844

- Domain: `coding`

## Problem

```text
You are given a 1-indexed integer array nums of length n.
An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
Return the sum of the squares of all special elements of nums.
 
Example 1:

Input: nums = [1,2,3,4]
Output: 21
Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.  

Example 2:

Input: nums = [2,7,1,19,18,3]
Output: 63
Explanation: There are exactly 4 special elements in nums: nums[1] since 1 divides 6, nums[2] since 2 divides 6, nums[3] since 3 divides 6, and nums[6] since 6 divides 6. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] = 2 * 2 + 7 * 7 + 1 * 1 + 3 * 3 = 63. 

 
Constraints:

1 <= nums.length == n <= 50
1 <= nums[i] <= 50
```

### Starter Code

```python
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[1, 2, 3, 4]",
    "output": "21",
    "testtype": "functional"
  },
  {
    "input": "[2, 7, 1, 19, 18, 3]",
    "output": "63",
    "testtype": "functional"
  },
  {
    "input": "[4]",
    "output": "16",
    "testtype": "functional"
  },
  {
    "input": "[8]",
    "output": "64",
    "testtype": "functional"
  },
  {
    "input": "[14]",
    "output": "196",
    "testtype": "functional"
  },
  {
    "input": "[11]",
    "output": "121",
    "testtype": "functional"
  },
  {
    "input": "[9, 1]",
    "output": "82",
    "testtype": "functional"
  },
  {
    "input": "[43]",
    "output": "1849",
    "testtype": "functional"
  },
  {
    "input": "[7, 1]",
    "output": "50",
    "testtype": "functional"
  },
  {
    "input": "[8, 23]",
    "output": "593",
    "testtype": "functional"
  },
  {
    "input": "[36, 13, 50, 15, 34, 46, 4, 26, 16, 21, 4, 43, 50, 34, 46, 13, 36, 16, 42, 36, 45, 25, 48, 30, 48, 7, 34, 32, 30, 22, 8, 48, 31, 50, 50, 31, 30, 2, 30, 38, 28, 28, 44, 16, 24, 28, 5, 33, 27, 10]",
    "output": "5466",
    "testtype": "functional"
  },
  {
    "input": "[30, 14, 9, 12, 27, 25, 40, 12, 46, 21, 46, 36, 1, 37, 43, 38, 47, 7, 48, 10, 5, 20, 3, 21, 35, 32, 21, 17, 6, 26, 13, 12, 15, 11, 16, 13, 35, 23, 22, 28, 15, 11, 48, 13, 24, 21, 34, 24, 42, 34]",
    "output": "4647",
    "testtype": "functional"
  },
  {
    "input": "[3, 35, 18, 9, 27, 41, 11, 39, 41, 38, 32, 16, 23, 16, 11, 11, 42, 26, 21, 38, 45, 45, 28, 27, 29, 48, 3, 28, 50, 5, 21, 10, 47, 19, 16, 36, 4, 14, 30, 22, 37, 47, 17, 29, 4, 17, 47, 47, 17, 43]",
    "output": "6097",
    "testtype": "functional"
  },
  {
    "input": "[50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]",
    "output": "15000",
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
You are given a 1-indexed integer array nums of length n.
An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
Return the sum of the squares of all special elements of nums.
 
Example 1:

Input: nums = [1,2,3,4]
Output: 21
Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.  

Example 2:

Input: nums = [2,7,1,19,18,3]
Output: 63
Explanation: There are exactly 4 special elements in nums: nums[1] since 1 divides 6, nums[2] since 2 divides 6, nums[3] since 3 divides 6, and nums[6] since 6 divides 6. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] = 2 * 2 + 7 * 7 + 1 * 1 + 3 * 3 = 63. 

 
Constraints:

1 <= nums.length == n <= 50
1 <= nums[i] <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                v = nums[i - 1]
                ans += v * v
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
        return ans
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                v = nums[i - 1]
                ans += v * v
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
        return ans
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
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
You are given a 1-indexed integer array nums of length n.
An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
Return the sum of the squares of all special elements of nums.
 
Example 1:

Input: nums = [1,2,3,4]
Output: 21
Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.  

Example 2:

Input: nums = [2,7,1,19,18,3]
Output: 63
Explanation: There are exactly 4 special elements in nums: nums[1] since 1 divides 6, nums[2] since 2 divides 6, nums[3] since 3 divides 6, and nums[6] since 6 divides 6. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] = 2 * 2 + 7 * 7 + 1 * 1 + 3 * 3 = 63. 

 
Constraints:

1 <= nums.length == n <= 50
1 <= nums[i] <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] ** 2
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] ** 2
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):  # 1-indexed positions
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] ** 2
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] ** 2
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
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):  # 1-indexed
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
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
      "expected": "21",
      "actual": "21",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "64",
      "actual": "64",
      "error": ""
    },
    {
      "passed": true,
      "expected": "196",
      "actual": "196",
      "error": ""
    },
    {
      "passed": true,
      "expected": "121",
      "actual": "121",
      "error": ""
    },
    {
      "passed": true,
      "expected": "82",
      "actual": "82",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1849",
      "actual": "1849",
      "error": ""
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": true,
      "expected": "593",
      "actual": "593",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5466",
      "actual": "5466",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4647",
      "actual": "4647",
      "error": ""
    },
    {
      "passed": true,
      "expected": "6097",
      "actual": "6097",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15000",
      "actual": "15000",
      "error": ""
    }
  ]
}
```

</details>
