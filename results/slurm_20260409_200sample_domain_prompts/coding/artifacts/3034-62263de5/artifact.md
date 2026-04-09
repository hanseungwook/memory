# Problem 3034

- Domain: `coding`

## Problem

```text
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [start_i, end_i] where start_i is the starting point of the i^th car and end_i is the ending point of the i^th car.
Return the number of integer points on the line that are covered with any part of a car.
 
Example 1:

Input: nums = [[3,6],[1,5],[4,7]]
Output: 7
Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.

Example 2:

Input: nums = [[1,3],[5,8]]
Output: 7
Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.

 
Constraints:

1 <= nums.length <= 100
nums[i].length == 2
1 <= start_i <= end_i <= 100
```

### Starter Code

```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[[3, 6], [1, 5], [4, 7]]",
    "output": "7",
    "testtype": "functional"
  },
  {
    "input": "[[1, 3], [5, 8]]",
    "output": "7",
    "testtype": "functional"
  },
  {
    "input": "[[4, 6], [5, 9]]",
    "output": "6",
    "testtype": "functional"
  },
  {
    "input": "[[7, 10], [6, 7]]",
    "output": "5",
    "testtype": "functional"
  },
  {
    "input": "[[13, 20], [12, 13], [1, 8]]",
    "output": "17",
    "testtype": "functional"
  },
  {
    "input": "[[17, 20], [20, 22], [20, 24]]",
    "output": "8",
    "testtype": "functional"
  },
  {
    "input": "[[18, 22], [17, 21], [12, 15]]",
    "output": "10",
    "testtype": "functional"
  },
  {
    "input": "[[6, 19], [4, 8], [16, 18], [4, 5]]",
    "output": "16",
    "testtype": "functional"
  },
  {
    "input": "[[9, 10], [6, 7], [1, 10], [8, 9], [3, 8]]",
    "output": "10",
    "testtype": "functional"
  },
  {
    "input": "[[9, 10], [10, 13], [7, 10], [2, 2], [8, 12]]",
    "output": "8",
    "testtype": "functional"
  },
  {
    "input": "[[27, 29], [32, 33], [17, 21], [2, 9], [60, 66], [61, 67], [35, 36], [11, 18], [45, 47], [56, 56], [73, 80], [64, 69], [48, 50], [41, 41], [12, 13], [74, 78], [40, 47], [19, 20], [15, 25], [2, 7], [68, 72], [49, 57], [53, 53], [50, 55], [44, 49], [15, 17], [72, 80], [69, 78], [51, 56], [59, 65], [39, 46], [29, 33], [21, 28], [34, 39], [36, 44], [65, 73], [50, 56], [32, 40], [47, 57], [72, 74], [80, 88], [76, 84], [50, 56], [60, 65], [27, 27], [58, 61], [7, 13], [43, 46], [45, 54], [11, 20], [25, 33], [10, 14], [63, 72], [30, 34], [9, 15], [39, 49], [60, 60], [48, 55], [32, 38], [22, 32], [3, 5], [38, 42], [34, 38], [61, 63], [70, 78], [8, 15], [62, 72], [21, 27], [21, 30], [28, 38], [70, 75], [79, 83], [1, 1], [1, 11], [41, 49], [24, 30], [22, 25], [25, 32], [71, 79], [36, 38], [27, 30], [46, 47], [59, 67], [50, 53], [30, 31], [4, 8], [77, 87], [30, 40], [77, 82], [40, 41], [25, 26], [7, 8], [24, 32], [22, 26], [21, 24], [70, 75], [40, 43], [29, 32], [15, 18], [42, 50]]",
    "output": "88",
    "testtype": "functional"
  },
  {
    "input": "[[65, 65], [55, 55], [80, 81], [74, 75], [71, 72], [63, 63], [96, 96], [75, 76], [80, 81], [90, 91], [8, 9], [52, 53], [27, 28], [9, 9], [86, 87], [60, 60], [97, 97], [22, 23], [11, 12], [61, 61], [91, 92], [63, 64], [80, 81], [79, 80], [39, 39], [13, 14], [80, 81], [87, 88], [56, 56], [85, 86], [19, 19], [60, 60], [98, 99], [38, 39], [92, 93], [54, 54], [55, 56], [45, 45], [36, 37], [77, 77], [46, 46], [84, 85], [53, 53], [52, 52], [54, 54], [82, 82], [24, 24], [49, 50], [76, 77], [46, 47], [82, 83], [46, 47], [100, 100], [75, 76], [31, 32], [7, 7], [19, 19], [58, 59], [88, 88], [33, 33], [74, 74], [70, 71], [74, 74], [56, 56], [26, 26], [2, 3], [61, 61], [86, 87], [15, 15], [97, 98], [21, 22], [8, 9], [2, 3], [33, 33], [42, 43], [88, 88], [75, 75], [71, 72], [55, 55], [52, 53], [34, 34], [41, 42], [59, 60], [1, 1], [94, 95], [96, 96], [94, 94], [3, 4], [80, 80], [93, 93], [82, 82], [49, 50], [16, 17], [35, 35], [15, 16], [40, 40], [31, 31], [18, 18], [14, 14], [79, 79]]",
    "output": "81",
    "testtype": "functional"
  },
  {
    "input": "[[61, 62], [47, 50], [46, 47], [8, 9], [59, 62], [66, 67], [26, 29], [80, 81], [56, 56], [34, 35], [27, 29], [70, 75], [57, 61], [37, 39], [68, 68], [79, 80], [68, 69], [13, 15], [20, 21], [50, 50], [24, 26], [23, 23], [40, 44], [61, 65], [41, 43], [4, 9], [63, 67], [12, 13], [71, 76], [10, 11], [46, 46], [77, 79], [51, 55], [80, 84], [48, 50], [38, 42], [58, 58], [43, 44], [4, 6], [67, 70], [80, 81], [70, 70], [29, 30], [71, 75], [67, 69], [29, 32], [72, 74], [16, 16], [66, 67], [79, 79], [54, 59], [70, 70], [51, 51], [27, 29], [65, 69], [23, 27], [15, 15], [27, 28], [46, 49], [74, 79], [76, 77], [65, 66], [54, 55], [41, 43], [72, 74], [26, 27], [46, 46], [67, 70], [76, 76], [53, 56], [15, 15], [33, 36], [66, 67], [64, 66], [27, 29], [37, 37], [1, 2], [9, 13], [33, 34], [49, 50], [48, 48], [61, 65], [2, 5], [58, 61], [78, 81], [61, 65], [54, 58], [78, 78], [22, 27], [43, 45], [59, 62], [57, 58], [12, 14], [34, 35], [22, 26], [17, 22], [39, 39], [64, 67], [40, 41], [42, 46]]",
    "output": "84",
    "testtype": "functional"
  },
  {
    "input": "[[39, 40], [16, 83], [74, 95], [55, 65], [49, 100], [59, 98], [64, 98], [63, 93], [66, 74], [37, 47], [85, 100], [100, 100], [13, 80], [31, 61], [40, 75], [48, 52], [74, 85], [98, 100], [16, 47], [8, 30], [97, 99], [21, 34], [59, 71], [85, 94], [51, 100], [47, 55], [39, 86], [39, 80], [50, 54], [35, 98], [53, 72], [91, 98], [73, 82], [33, 86], [15, 82], [35, 58], [94, 96], [97, 100], [27, 50], [99, 99], [34, 52], [54, 69], [52, 76], [42, 46], [1, 37], [100, 100], [50, 92], [99, 100], [20, 28], [88, 91], [6, 36], [39, 76], [73, 93], [37, 56], [79, 87], [58, 66], [76, 82], [31, 71], [23, 54], [4, 29], [12, 51], [58, 92], [58, 70], [78, 96], [60, 83], [51, 72], [71, 81], [28, 78], [2, 67], [51, 61], [68, 74], [72, 72], [69, 86], [40, 58], [86, 97], [52, 55], [92, 98], [62, 83], [84, 99], [2, 42], [69, 86], [49, 60], [77, 95], [67, 80], [39, 83], [77, 90], [98, 100], [1, 52], [35, 41], [10, 91], [11, 67], [94, 99], [99, 99], [4, 84], [26, 56], [39, 82], [58, 97], [41, 50], [56, 93]]",
    "output": "100",
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
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [start_i, end_i] where start_i is the starting point of the i^th car and end_i is the ending point of the i^th car.
Return the number of integer points on the line that are covered with any part of a car.
 
Example 1:

Input: nums = [[3,6],[1,5],[4,7]]
Output: 7
Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.

Example 2:

Input: nums = [[1,3],[5,8]]
Output: 7
Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.

 
Constraints:

1 <= nums.length <= 100
nums[i].length == 2
1 <= start_i <= end_i <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
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
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = [False] * 101  # points from 1..100
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):  # inclusive integer points
                covered.add(x)
        return len(covered)
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = [False] * 101  # points from 1..100
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):  # inclusive integer points
                covered.add(x)
        return len(covered)
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
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [start_i, end_i] where start_i is the starting point of the i^th car and end_i is the ending point of the i^th car.
Return the number of integer points on the line that are covered with any part of a car.
 
Example 1:

Input: nums = [[3,6],[1,5],[4,7]]
Output: 7
Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.

Example 2:

Input: nums = [[1,3],[5,8]]
Output: 7
Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.

 
Constraints:

1 <= nums.length <= 100
nums[i].length == 2
1 <= start_i <= end_i <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
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
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = [False] * 101  # coordinates are within [1, 100]
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # Given constraints: start/end in [1, 100]
        covered = [False] * 101  # indices 0..100, we use 1..100
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = [False] * 101  # given 1 <= start_i, end_i <= 100
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # Car intervals have endpoints between 1 and 100 (inclusive).
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = [False] * 101  # points are within 1..100
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = [False] * 101  # coordinates are within [1, 100]
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # Given constraints: start/end in [1, 100]
        covered = [False] * 101  # indices 0..100, we use 1..100
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = [False] * 101  # given 1 <= start_i, end_i <= 100
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # Car intervals have endpoints between 1 and 100 (inclusive).
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = [False] * 101  # points are within 1..100
        for start, end in nums:
            for x in range(start, end + 1):
                covered[x] = True
        return sum(covered)
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range(start, end + 1):
                covered.add(x)
        return len(covered)
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "6",
      "actual": "6",
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
      "expected": "17",
      "actual": "17",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "10",
      "actual": "10",
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
      "expected": "88",
      "actual": "88",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "84",
      "actual": "84",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    }
  ]
}
```

</details>
