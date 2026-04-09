# Problem 3347

- Domain: `coding`

## Problem

```text
You are given a 1-indexed array of distinct integers nums of length n.
You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the i^th operation:

If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1. Otherwise, append nums[i] to arr2.

The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].
Return the array result.
 
Example 1:

Input: nums = [2,1,3]
Output: [2,3,1]
Explanation: After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (2 > 1), append nums[3] to arr1.
After 3 operations, arr1 = [2,3] and arr2 = [1].
Hence, the array result formed by concatenation is [2,3,1].

Example 2:

Input: nums = [5,4,3,8]
Output: [5,3,4,8]
Explanation: After the first 2 operations, arr1 = [5] and arr2 = [4].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (5 > 4), append nums[3] to arr1, hence arr1 becomes [5,3].
In the 4^th operation, as the last element of arr2 is greater than the last element of arr1 (4 > 3), append nums[4] to arr2, hence arr2 becomes [4,8].
After 4 operations, arr1 = [5,3] and arr2 = [4,8].
Hence, the array result formed by concatenation is [5,3,4,8].

 
Constraints:

3 <= n <= 50
1 <= nums[i] <= 100
All elements in nums are distinct.
```

### Starter Code

```python
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
```

### Test Cases

```json
[
  {
    "input": "[2, 1, 3]",
    "output": "[2, 3, 1]",
    "testtype": "functional"
  },
  {
    "input": "[5, 4, 3, 8]",
    "output": "[5, 3, 4, 8]",
    "testtype": "functional"
  },
  {
    "input": "[45, 40, 1]",
    "output": "[45, 1, 40]",
    "testtype": "functional"
  },
  {
    "input": "[41, 35, 24, 9]",
    "output": "[41, 24, 35, 9]",
    "testtype": "functional"
  },
  {
    "input": "[29, 33, 45, 43]",
    "output": "[29, 33, 45, 43]",
    "testtype": "functional"
  },
  {
    "input": "[4, 83, 73, 96, 22]",
    "output": "[4, 83, 73, 96, 22]",
    "testtype": "functional"
  },
  {
    "input": "[9, 38, 42, 18, 27]",
    "output": "[9, 38, 42, 18, 27]",
    "testtype": "functional"
  },
  {
    "input": "[50, 44, 5, 20, 34]",
    "output": "[50, 5, 44, 20, 34]",
    "testtype": "functional"
  },
  {
    "input": "[48, 28, 26, 45, 19]",
    "output": "[48, 26, 28, 45, 19]",
    "testtype": "functional"
  },
  {
    "input": "[12, 78, 53, 40, 59]",
    "output": "[12, 78, 53, 40, 59]",
    "testtype": "functional"
  },
  {
    "input": "[16, 46, 15, 11, 4, 7]",
    "output": "[16, 11, 7, 46, 15, 4]",
    "testtype": "functional"
  },
  {
    "input": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
    "output": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
    "testtype": "functional"
  },
  {
    "input": "[75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]",
    "output": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
    "testtype": "functional"
  },
  {
    "input": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
    "output": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
You are given a 1-indexed array of distinct integers nums of length n.
You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the i^th operation:

If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1. Otherwise, append nums[i] to arr2.

The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].
Return the array result.
 
Example 1:

Input: nums = [2,1,3]
Output: [2,3,1]
Explanation: After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (2 > 1), append nums[3] to arr1.
After 3 operations, arr1 = [2,3] and arr2 = [1].
Hence, the array result formed by concatenation is [2,3,1].

Example 2:

Input: nums = [5,4,3,8]
Output: [5,3,4,8]
Explanation: After the first 2 operations, arr1 = [5] and arr2 = [4].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (5 > 4), append nums[3] to arr1, hence arr1 becomes [5,3].
In the 4^th operation, as the last element of arr2 is greater than the last element of arr1 (4 > 3), append nums[4] to arr2, hence arr2 becomes [4,8].
After 4 operations, arr1 = [5,3] and arr2 = [4,8].
Hence, the array result formed by concatenation is [5,3,4,8].

 
Constraints:

3 <= n <= 50
1 <= nums[i] <= 100
All elements in nums are distinct.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
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
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
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
You are given a 1-indexed array of distinct integers nums of length n.
You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the i^th operation:

If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1. Otherwise, append nums[i] to arr2.

The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].
Return the array result.
 
Example 1:

Input: nums = [2,1,3]
Output: [2,3,1]
Explanation: After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (2 > 1), append nums[3] to arr1.
After 3 operations, arr1 = [2,3] and arr2 = [1].
Hence, the array result formed by concatenation is [2,3,1].

Example 2:

Input: nums = [5,4,3,8]
Output: [5,3,4,8]
Explanation: After the first 2 operations, arr1 = [5] and arr2 = [4].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (5 > 4), append nums[3] to arr1, hence arr1 becomes [5,3].
In the 4^th operation, as the last element of arr2 is greater than the last element of arr1 (4 > 3), append nums[4] to arr2, hence arr2 becomes [4,8].
After 4 operations, arr1 = [5,3] and arr2 = [4,8].
Hence, the array result formed by concatenation is [5,3,4,8].

 
Constraints:

3 <= n <= 50
1 <= nums[i] <= 100
All elements in nums are distinct.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
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
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)
        
        return arr1 + arr2
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)

        return arr1 + arr2
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        for x in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(x)
            else:
                arr2.append(x)
        
        return arr1 + arr2
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
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
      "expected": "[2, 3, 1]",
      "actual": "[2, 3, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[5, 3, 4, 8]",
      "actual": "[5, 3, 4, 8]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[45, 1, 40]",
      "actual": "[45, 1, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[41, 24, 35, 9]",
      "actual": "[41, 24, 35, 9]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[29, 33, 45, 43]",
      "actual": "[29, 33, 45, 43]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[4, 83, 73, 96, 22]",
      "actual": "[4, 83, 73, 96, 22]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[9, 38, 42, 18, 27]",
      "actual": "[9, 38, 42, 18, 27]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[50, 5, 44, 20, 34]",
      "actual": "[50, 5, 44, 20, 34]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[48, 26, 28, 45, 19]",
      "actual": "[48, 26, 28, 45, 19]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[12, 78, 53, 40, 59]",
      "actual": "[12, 78, 53, 40, 59]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[16, 11, 7, 46, 15, 4]",
      "actual": "[16, 11, 7, 46, 15, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "actual": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "actual": "[75, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "actual": "[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]",
      "error": ""
    }
  ]
}
```

</details>
