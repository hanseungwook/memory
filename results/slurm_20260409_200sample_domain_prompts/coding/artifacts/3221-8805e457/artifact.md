# Problem 3221

- Domain: `coding`

## Problem

```text
You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.
Return an array that consists of indices of peaks in the given array in any order.
Notes:

A peak is defined as an element that is strictly greater than its neighboring elements.
The first and last elements of the array are not a peak.

 
Example 1:

Input: mountain = [2,4,4]
Output: []
Explanation: mountain[0] and mountain[2] can not be a peak because they are first and last elements of the array.
mountain[1] also can not be a peak because it is not strictly greater than mountain[2].
So the answer is [].

Example 2:

Input: mountain = [1,4,3,8,5]
Output: [1,3]
Explanation: mountain[0] and mountain[4] can not be a peak because they are first and last elements of the array.
mountain[2] also can not be a peak because it is not strictly greater than mountain[3] and mountain[1].
But mountain [1] and mountain[3] are strictly greater than their neighboring elements.
So the answer is [1,3].

 
Constraints:

3 <= mountain.length <= 100
1 <= mountain[i] <= 100
```

### Starter Code

```python
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
```

### Test Cases

```json
[
  {
    "input": "[2, 4, 4]",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[1, 4, 3, 8, 5]",
    "output": "[1, 3]",
    "testtype": "functional"
  },
  {
    "input": "[2, 10, 1]",
    "output": "[1]",
    "testtype": "functional"
  },
  {
    "input": "[1, 100, 1]",
    "output": "[1]",
    "testtype": "functional"
  },
  {
    "input": "[33, 65, 58]",
    "output": "[1]",
    "testtype": "functional"
  },
  {
    "input": "[67, 92, 60]",
    "output": "[1]",
    "testtype": "functional"
  },
  {
    "input": "[85, 88, 13]",
    "output": "[1]",
    "testtype": "functional"
  },
  {
    "input": "[12, 13, 82, 60]",
    "output": "[2]",
    "testtype": "functional"
  },
  {
    "input": "[33, 4, 42, 68, 53, 40, 53, 13, 93, 54, 58, 26, 5, 2, 86, 23, 30, 43, 8, 81, 67, 32, 8, 31, 64, 68, 51, 2, 37, 8, 74, 21, 43, 69, 7, 79, 90]",
    "output": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
    "testtype": "functional"
  },
  {
    "input": "[62, 85, 10, 28, 89, 6, 13, 73, 92, 24, 17, 47, 50, 86, 85, 63, 74, 62, 31, 47, 11, 80, 6, 77, 12, 47, 88, 36, 45, 89, 3, 36, 98, 52, 10, 45]",
    "output": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
    "testtype": "functional"
  },
  {
    "input": "[1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 1]",
    "output": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
    "testtype": "functional"
  },
  {
    "input": "[22, 80, 9, 80, 79, 81, 77, 15, 61, 39, 31, 5, 31, 98, 30, 38, 13, 12, 46, 15, 5, 7, 58, 95, 60, 1, 89, 56, 69, 82, 51, 68, 28, 75, 48, 52, 79, 19, 52, 25, 94, 17, 48, 62, 50, 52, 64, 47, 50, 34, 56, 69, 61, 43, 63, 37, 58, 68, 92, 77, 44, 93, 12, 91, 77, 44, 12, 34, 62, 88, 5, 43, 65, 87, 89, 55, 96, 8, 98, 32, 98, 3, 13, 3, 29, 79, 61, 62, 34, 21, 48, 17, 54, 87, 73, 54, 64, 59, 100, 90]",
    "output": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
    "testtype": "functional"
  },
  {
    "input": "[32, 69, 48, 34, 56, 37, 15, 89, 45, 83, 19, 77, 27, 4, 49, 26, 5, 93, 34, 81, 75, 26, 47, 70, 46, 60, 27, 61, 44, 14, 72, 78, 99, 99, 3, 51, 51, 73, 99, 19, 91, 11, 45, 2, 89, 50, 82, 72, 38, 95, 44, 21, 75, 39, 48, 51, 19, 64, 51, 55, 33, 25, 37, 11, 39, 84, 90, 66, 98, 82, 57, 79, 61, 11, 99, 51, 47, 96, 69, 100, 47, 45, 14, 71, 51, 69, 25, 50, 36, 12, 41, 46, 97, 45, 71, 19, 62, 10, 25, 25]",
    "output": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
    "testtype": "functional"
  },
  {
    "input": "[1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 1]",
    "output": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.
Return an array that consists of indices of peaks in the given array in any order.
Notes:

A peak is defined as an element that is strictly greater than its neighboring elements.
The first and last elements of the array are not a peak.

 
Example 1:

Input: mountain = [2,4,4]
Output: []
Explanation: mountain[0] and mountain[2] can not be a peak because they are first and last elements of the array.
mountain[1] also can not be a peak because it is not strictly greater than mountain[2].
So the answer is [].

Example 2:

Input: mountain = [1,4,3,8,5]
Output: [1,3]
Explanation: mountain[0] and mountain[4] can not be a peak because they are first and last elements of the array.
mountain[2] also can not be a peak because it is not strictly greater than mountain[3] and mountain[1].
But mountain [1] and mountain[3] are strictly greater than their neighboring elements.
So the answer is [1,3].

 
Constraints:

3 <= mountain.length <= 100
1 <= mountain[i] <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        
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
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last cannot be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peaks = []
        for i in range(1, n - 1):  # first and last can't be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        # First and last indices cannot be peaks
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peaks = []
        # First and last are not peaks, so check 1..n-2
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peaks = []
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        # first and last can't be peaks
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last can't be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last cannot be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peaks = []
        for i in range(1, n - 1):  # first and last can't be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        # First and last indices cannot be peaks
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peaks = []
        # First and last are not peaks, so check 1..n-2
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peaks = []
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        # first and last can't be peaks
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last can't be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
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
You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.
Return an array that consists of indices of peaks in the given array in any order.
Notes:

A peak is defined as an element that is strictly greater than its neighboring elements.
The first and last elements of the array are not a peak.

 
Example 1:

Input: mountain = [2,4,4]
Output: []
Explanation: mountain[0] and mountain[2] can not be a peak because they are first and last elements of the array.
mountain[1] also can not be a peak because it is not strictly greater than mountain[2].
So the answer is [].

Example 2:

Input: mountain = [1,4,3,8,5]
Output: [1,3]
Explanation: mountain[0] and mountain[4] can not be a peak because they are first and last elements of the array.
mountain[2] also can not be a peak because it is not strictly greater than mountain[3] and mountain[1].
But mountain [1] and mountain[3] are strictly greater than their neighboring elements.
So the answer is [1,3].

 
Constraints:

3 <= mountain.length <= 100
1 <= mountain[i] <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        
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
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last can't be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last cannot be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peaks = []
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last can't be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last can't be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last cannot be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peaks = []
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # exclude first and last
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):  # first and last can't be peaks
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3]",
      "actual": "[1, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1]",
      "actual": "[1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "actual": "[3, 6, 8, 10, 14, 17, 19, 25, 28, 30, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "actual": "[1, 4, 8, 13, 16, 19, 21, 23, 26, 29, 32]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "actual": "[1, 3, 5, 8, 13, 15, 18, 23, 26, 29, 31, 33, 36, 38, 40, 43, 46, 48, 51, 54, 58, 61, 63, 69, 74, 76, 78, 80, 82, 85, 87, 90, 93, 96, 98]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "actual": "[1, 4, 7, 9, 11, 14, 17, 19, 23, 25, 27, 38, 40, 42, 44, 46, 49, 52, 55, 57, 59, 62, 66, 68, 71, 74, 77, 79, 83, 85, 87, 92, 94, 96]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "actual": "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]",
      "error": ""
    }
  ]
}
```

</details>
