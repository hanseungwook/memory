# Problem 3236

- Domain: `coding`

## Problem

```text
You are given a 0-indexed array of integers nums.
A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.
Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.
 
Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

Example 2:

Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

 
Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
```

### Starter Code

```python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[1, 2, 3, 2, 5]",
    "output": "6",
    "testtype": "functional"
  },
  {
    "input": "[3, 4, 5, 1, 12, 14, 13]",
    "output": "15",
    "testtype": "functional"
  },
  {
    "input": "[7]",
    "output": "8",
    "testtype": "functional"
  },
  {
    "input": "[44]",
    "output": "45",
    "testtype": "functional"
  },
  {
    "input": "[32]",
    "output": "33",
    "testtype": "functional"
  },
  {
    "input": "[23, 43]",
    "output": "24",
    "testtype": "functional"
  },
  {
    "input": "[1, 4, 6]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[2, 3, 6, 9]",
    "output": "5",
    "testtype": "functional"
  },
  {
    "input": "[8, 19, 21, 45]",
    "output": "9",
    "testtype": "functional"
  },
  {
    "input": "[1, 1, 2, 3, 4, 6, 8, 9]",
    "output": "5",
    "testtype": "functional"
  },
  {
    "input": "[39, 19, 38, 36, 4, 47, 37, 40]",
    "output": "41",
    "testtype": "functional"
  },
  {
    "input": "[50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]",
    "output": "51",
    "testtype": "functional"
  },
  {
    "input": "[28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28]",
    "output": "29",
    "testtype": "functional"
  },
  {
    "input": "[13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]",
    "output": "14",
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
You are given a 0-indexed array of integers nums.
A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.
Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.
 
Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

Example 2:

Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

 
Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
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
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        i = 0
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1

        # Sum of that prefix
        s = sum(nums[:i + 1])

        # Find smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        # Find the longest sequential prefix
        i = 0
        while i + 1 < n and nums[i + 1] == nums[i] + 1:
            i += 1

        # Compute sum of that prefix
        target_sum = sum(nums[: i + 1])

        # Find smallest missing integer >= target_sum
        s = set(nums)
        x = target_sum
        while x in s:
            x += 1
        return x
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find length of the longest sequential prefix
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Smallest missing integer >= sum_of_longest_sequential_prefix
        s = total
        present = set(nums)
        while s in present:
            s += 1
        return s
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find longest sequential prefix
        s = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == cur + 1:
                cur = nums[i]
                s += cur
            else:
                break

        # Smallest integer >= sum s that is missing from nums
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find length of the longest sequential prefix
        # where nums[j] = nums[j-1] + 1 for all j in the prefix.
        pref_sum = 0
        i = 0
        n = len(nums)

        # Build sequential prefix
        pref_sum += nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                pref_sum += nums[i]
            else:
                break

        # pref_sum is sum of longest sequential prefix
        s = pref_sum

        # Return smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)

        # Find the longest sequential prefix where nums[j] = nums[j-1] + 1
        prefix_sum = nums[0]
        for j in range(1, n):
            if nums[j] == nums[j - 1] + 1:
                prefix_sum += nums[j]
            else:
                break

        # Smallest missing integer >= prefix_sum
        s = set(nums)
        x = prefix_sum
        while x in s:
            x += 1
        return x
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix (nums[j] == nums[j-1] + 1).
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        target = total

        # Smallest missing integer >= target
        s = set(nums)
        while target in s:
            target += 1
        return target
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix: nums[k] = nums[k-1] + 1
        s = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1

        # Smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        # sequential means nums[j] = nums[j-1] + 1 for all j in [1..i]
        s = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1

        # Need the smallest missing integer >= sum of the longest sequential prefix
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find the smallest missing integer >= total
        present = set(nums)
        x = total
        while x in present:
            x += 1
        return x
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        i = 0
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1

        # Sum of that prefix
        s = sum(nums[:i + 1])

        # Find smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        # Find the longest sequential prefix
        i = 0
        while i + 1 < n and nums[i + 1] == nums[i] + 1:
            i += 1

        # Compute sum of that prefix
        target_sum = sum(nums[: i + 1])

        # Find smallest missing integer >= target_sum
        s = set(nums)
        x = target_sum
        while x in s:
            x += 1
        return x
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find length of the longest sequential prefix
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Smallest missing integer >= sum_of_longest_sequential_prefix
        s = total
        present = set(nums)
        while s in present:
            s += 1
        return s
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find longest sequential prefix
        s = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == cur + 1:
                cur = nums[i]
                s += cur
            else:
                break

        # Smallest integer >= sum s that is missing from nums
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find length of the longest sequential prefix
        # where nums[j] = nums[j-1] + 1 for all j in the prefix.
        pref_sum = 0
        i = 0
        n = len(nums)

        # Build sequential prefix
        pref_sum += nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                pref_sum += nums[i]
            else:
                break

        # pref_sum is sum of longest sequential prefix
        s = pref_sum

        # Return smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)

        # Find the longest sequential prefix where nums[j] = nums[j-1] + 1
        prefix_sum = nums[0]
        for j in range(1, n):
            if nums[j] == nums[j - 1] + 1:
                prefix_sum += nums[j]
            else:
                break

        # Smallest missing integer >= prefix_sum
        s = set(nums)
        x = prefix_sum
        while x in s:
            x += 1
        return x
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix (nums[j] == nums[j-1] + 1).
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        target = total

        # Smallest missing integer >= target
        s = set(nums)
        while target in s:
            target += 1
        return target
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix: nums[k] = nums[k-1] + 1
        s = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1

        # Smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        # sequential means nums[j] = nums[j-1] + 1 for all j in [1..i]
        s = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1

        # Need the smallest missing integer >= sum of the longest sequential prefix
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find the smallest missing integer >= total
        present = set(nums)
        x = total
        while x in present:
            x += 1
        return x
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
You are given a 0-indexed array of integers nums.
A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.
Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.
 
Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

Example 2:

Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

 
Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
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
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix starting at nums[0]
        prefix_sum = nums[0]
        cur = nums[0]
        best_sum = prefix_sum

        for i in range(1, len(nums)):
            if nums[i] == cur + 1:
                cur = nums[i]
                prefix_sum += nums[i]
                best_sum = prefix_sum
            else:
                break

        # Find the smallest missing integer >= best_sum
        s = best_sum
        present = set(nums)
        while s in present:
            s += 1
        return s
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            i += 1
        # Longest sequential prefix is nums[0 : i]
        s = sum(nums[:i])

        # Find smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur_sum += nums[i]
            else:
                break
        # Smallest missing integer >= sum of that longest sequential prefix
        x = cur_sum
        s = set(nums)
        while x in s:
            x += 1
        return x
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Find the smallest missing integer >= sum of that prefix
        s = total
        present = set(nums)
        while s in present:
            s += 1
        return s
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        # Find the longest sequential prefix starting at nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            i += 1

        # Sum of nums[0..i-1]
        s = sum(nums[:i])

        nums_set = set(nums)
        x = s
        while x in nums_set:
            x += 1
        return x
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find longest sequential prefix: nums[j] == nums[j-1] + 1
        n = len(nums)
        s = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1

        # Now s is the sum of the longest sequential prefix.
        # Return the smallest missing integer >= s.
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        s = nums[0]
        total = nums[0]
        best_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
                best_sum = total
            else:
                break

        target = best_sum

        # Find the smallest missing integer >= target
        present = set(nums)
        x = target
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix and its sum
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        s = total  # sum of the longest sequential prefix

        # Find smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break

        target_sum = s
        present = set(nums)

        # Smallest missing integer >= target_sum
        x = target_sum
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        target = total
        s = set(nums)
        while target in s:
            target += 1
        return target
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix starting at nums[0]
        prefix_sum = nums[0]
        cur = nums[0]
        best_sum = prefix_sum

        for i in range(1, len(nums)):
            if nums[i] == cur + 1:
                cur = nums[i]
                prefix_sum += nums[i]
                best_sum = prefix_sum
            else:
                break

        # Find the smallest missing integer >= best_sum
        s = best_sum
        present = set(nums)
        while s in present:
            s += 1
        return s
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            i += 1
        # Longest sequential prefix is nums[0 : i]
        s = sum(nums[:i])

        # Find smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur_sum += nums[i]
            else:
                break
        # Smallest missing integer >= sum of that longest sequential prefix
        x = cur_sum
        s = set(nums)
        while x in s:
            x += 1
        return x
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Find the smallest missing integer >= sum of that prefix
        s = total
        present = set(nums)
        while s in present:
            s += 1
        return s
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        # Find the longest sequential prefix starting at nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            i += 1

        # Sum of nums[0..i-1]
        s = sum(nums[:i])

        nums_set = set(nums)
        x = s
        while x in nums_set:
            x += 1
        return x
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find longest sequential prefix: nums[j] == nums[j-1] + 1
        n = len(nums)
        s = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1

        # Now s is the sum of the longest sequential prefix.
        # Return the smallest missing integer >= s.
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        s = nums[0]
        total = nums[0]
        best_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
                best_sum = total
            else:
                break

        target = best_sum

        # Find the smallest missing integer >= target
        present = set(nums)
        x = target
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix and its sum
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        s = total  # sum of the longest sequential prefix

        # Find smallest missing integer >= s
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break

        target_sum = s
        present = set(nums)

        # Smallest missing integer >= target_sum
        x = target_sum
        while x in present:
            x += 1
        return x
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        target = total
        s = set(nums)
        while target in s:
            target += 1
        return target
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "15",
      "actual": "15",
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
      "expected": "45",
      "actual": "45",
      "error": ""
    },
    {
      "passed": true,
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24",
      "actual": "24",
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
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "41",
      "actual": "41",
      "error": ""
    },
    {
      "passed": true,
      "expected": "51",
      "actual": "51",
      "error": ""
    },
    {
      "passed": true,
      "expected": "29",
      "actual": "29",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14",
      "actual": "14",
      "error": ""
    }
  ]
}
```

</details>
