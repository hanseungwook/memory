# Problem 3320

- Domain: `coding`

## Problem

```text
Given an array of integers called nums, you can perform the following operation while nums contains at least 2 elements:

Choose the first two elements of nums and delete them.

The score of the operation is the sum of the deleted elements.
Your task is to find the maximum number of operations that can be performed, such that all operations have the same score.
Return the maximum number of operations possible that satisfy the condition mentioned above.
 
Example 1:

Input: nums = [3,2,1,4,5]
Output: 2
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [1,4,5].
- Delete the first two elements, with score 1 + 4 = 5, nums = [5].
We are unable to perform any more operations as nums contain only 1 element.
Example 2:

Input: nums = [3,2,6,1,4]
Output: 1
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
We are unable to perform any more operations as the score of the next operation isn't the same as the previous one.

 
Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 1000
```

### Starter Code

```python
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[3, 2, 1, 4, 5]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[3, 2, 6, 1, 4]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[1, 1]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[2, 1]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[5, 5]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[50, 50]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[65, 65]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[42, 488]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[500, 500]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[250, 250]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[199, 301]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]",
    "output": "50",
    "testtype": "functional"
  },
  {
    "input": "[500, 500, 501, 499, 502, 498, 503, 497, 504, 496, 505, 495, 506, 494, 507, 493, 508, 492, 509, 491, 510, 490, 511, 489, 512, 488, 513, 487, 514, 486, 515, 485, 516, 484, 517, 483, 518, 482, 519, 481, 520, 480, 521, 479, 522, 478, 523, 477, 524, 476, 525, 475, 526, 474, 527, 473, 528, 472, 529, 471, 530, 470, 531, 469, 532, 468, 533, 467, 534, 466, 535, 465, 536, 464, 537, 463, 538, 462, 539, 461, 540, 460, 541, 459, 542, 458, 543, 457, 544, 456, 545, 455, 546, 454, 547, 453, 548, 452, 549, 451]",
    "output": "50",
    "testtype": "functional"
  },
  {
    "input": "[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 499]",
    "output": "49",
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
Given an array of integers called nums, you can perform the following operation while nums contains at least 2 elements:

Choose the first two elements of nums and delete them.

The score of the operation is the sum of the deleted elements.
Your task is to find the maximum number of operations that can be performed, such that all operations have the same score.
Return the maximum number of operations possible that satisfy the condition mentioned above.
 
Example 1:

Input: nums = [3,2,1,4,5]
Output: 2
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [1,4,5].
- Delete the first two elements, with score 1 + 4 = 5, nums = [5].
We are unable to perform any more operations as nums contain only 1 element.
Example 2:

Input: nums = [3,2,6,1,4]
Output: 1
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
We are unable to perform any more operations as the score of the next operation isn't the same as the previous one.

 
Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 1000

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
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
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try each possible score determined by the first operation:
        # score = nums[0] + nums[1] (must be the first pair's sum)
        target = nums[0] + nums[1]

        # Count how many consecutive "front-pair" deletions can be made
        # while each pair sums to the same target.
        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2
        return ops
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # Try each possible target score derived from the first operation:
        # score = nums[0] + nums[1], but after deleting first two,
        # the next required score is determined by the same target.
        target = nums[0] + nums[1]
        i = 2  # next element index after removing first two
        ops = 1

        # Greedily remove pairs from the front as long as their sum matches target.
        while i + 1 < len(nums) and nums[i] + nums[i + 1] == target:
            ops += 1
            i += 2

        return ops
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        # Try all possible first-operation sums: first element + nums[1]
        # The score must equal the sum of each removed pair, so once the target
        # is fixed, the process is deterministic.
        target = nums[0] + nums[1]

        i = 2
        cnt = 1
        curr_sum = nums[0] + nums[1]

        if curr_sum != target:
            return 0  # not possible, but kept for completeness

        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            cnt += 1
            i += 2

        best = cnt
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
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def can_make(target: int) -> int:
            # Greedily consume pairs from the front while their sum == target
            i = 0
            ops = 0
            while i + 1 < n and nums[i] + nums[i + 1] == target:
                ops += 1
                i += 2
            return ops

        # The score must be the sum of the first two elements in the chosen scheme.
        # Therefore we only need to try two possible starting sums:
        # - using initial pair (0,1) => target1
        # - if you remove none? not allowed; operations begin with first two.
        # In this problem, target can only be nums[0]+nums[1].
        # However, we can also consider the first operation score as nums[0]+nums[1] only.
        # We'll compute directly.
        target = nums[0] + nums[1]
        return can_make(target)
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # Try possible target scores derived from the first operation.
        # Each operation removes the first two elements, so the score is fixed
        # once we choose the target sum for the first pair.
        n = len(nums)
        if n < 2:
            return 0

        target1 = nums[0] + nums[1]
        target2 = nums[0] + nums[2] if n >= 3 else None

        def simulate(target: int) -> int:
            ops = 0
            i = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] != target:
                    break
                ops += 1
                i += 2
            return ops

        best = simulate(target1)
        if target2 is not None:
            best = max(best, simulate(target2))
        return best
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        # Try every possible target score formed by the first two elements removed
        # i.e., target = nums[0] + nums[1], then simulate greedily.
        for i in range(n - 1):
            target = nums[i] + nums[0]  # not used directly; we instead simulate after fixing initial pair
            # We actually need to fix the initial pair to be the first two elements at start.
            # So only one choice exists: the target score must be nums[0] + nums[1].
            break

        target = nums[0] + nums[1]
        score = target
        ops = 0
        # Since the operation always deletes the first two elements, the sequence is deterministic.
        j = 0
        while j + 1 < n:
            if nums[j] + nums[j + 1] == score:
                ops += 1
                j += 2
            else:
                break
        return ops
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def can_make(k: int) -> int:
            # Simulate deletions while every operation sum == k
            i = 0
            ops = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] != k:
                    break
                ops += 1
                i += 2
            return ops

        # First operation sum determines the required k, so only need to try candidates.
        # Try k as sum of first two elements, and also possible if we want
        # to allow skipping? Actually we cannot reorder and we always delete first two,
        # so k must be nums[0] + nums[1] for any operation count >= 1.
        k = nums[0] + nums[1]  # only possible score for the first operation
        return can_make(k)
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def can_make(target: int) -> int:
            i = 0
            ops = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] == target:
                    ops += 1
                    i += 2
                else:
                    return ops
            return ops

        # Try score candidates derived from the first operation.
        # If the first operation is valid, its score must be nums[0]+nums[1].
        # There are no other possibilities because operations always remove the first two.
        target = nums[0] + nums[1]
        return can_make(target)
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try every possible target score derived from the first operation:
        # score = nums[0] + nums[1], and we simulate consuming the array greedily.
        best = 0
        for start in (0,):
            target = nums[start] + nums[start + 1]
            ops = 0
            i = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] != target:
                    break
                ops += 1
                i += 2
            best = max(best, ops)

        return best
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try each possible first-pair sum as the target score.
        # At most n-1 operations, but we can just check i from 0..n-2.
        best = 0
        for target in (nums[0] + nums[1],):
            # Since the first operation must use the first two elements,
            # the target is forced to nums[0] + nums[1] (LC problem statement).
            # Build iteratively: each operation consumes next two elements.
            ops = 0
            i = 0
            while i + 1 < n and ops >= 0:
                if nums[i] + nums[i + 1] != target:
                    break
                ops += 1
                i += 2
            best = ops

        return best
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try each possible score determined by the first operation:
        # score = nums[0] + nums[1] (must be the first pair's sum)
        target = nums[0] + nums[1]

        # Count how many consecutive "front-pair" deletions can be made
        # while each pair sums to the same target.
        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2
        return ops
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # Try each possible target score derived from the first operation:
        # score = nums[0] + nums[1], but after deleting first two,
        # the next required score is determined by the same target.
        target = nums[0] + nums[1]
        i = 2  # next element index after removing first two
        ops = 1

        # Greedily remove pairs from the front as long as their sum matches target.
        while i + 1 < len(nums) and nums[i] + nums[i + 1] == target:
            ops += 1
            i += 2

        return ops
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        # Try all possible first-operation sums: first element + nums[1]
        # The score must equal the sum of each removed pair, so once the target
        # is fixed, the process is deterministic.
        target = nums[0] + nums[1]

        i = 2
        cnt = 1
        curr_sum = nums[0] + nums[1]

        if curr_sum != target:
            return 0  # not possible, but kept for completeness

        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            cnt += 1
            i += 2

        best = cnt
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
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def can_make(target: int) -> int:
            # Greedily consume pairs from the front while their sum == target
            i = 0
            ops = 0
            while i + 1 < n and nums[i] + nums[i + 1] == target:
                ops += 1
                i += 2
            return ops

        # The score must be the sum of the first two elements in the chosen scheme.
        # Therefore we only need to try two possible starting sums:
        # - using initial pair (0,1) => target1
        # - if you remove none? not allowed; operations begin with first two.
        # In this problem, target can only be nums[0]+nums[1].
        # However, we can also consider the first operation score as nums[0]+nums[1] only.
        # We'll compute directly.
        target = nums[0] + nums[1]
        return can_make(target)
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # Try possible target scores derived from the first operation.
        # Each operation removes the first two elements, so the score is fixed
        # once we choose the target sum for the first pair.
        n = len(nums)
        if n < 2:
            return 0

        target1 = nums[0] + nums[1]
        target2 = nums[0] + nums[2] if n >= 3 else None

        def simulate(target: int) -> int:
            ops = 0
            i = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] != target:
                    break
                ops += 1
                i += 2
            return ops

        best = simulate(target1)
        if target2 is not None:
            best = max(best, simulate(target2))
        return best
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        # Try every possible target score formed by the first two elements removed
        # i.e., target = nums[0] + nums[1], then simulate greedily.
        for i in range(n - 1):
            target = nums[i] + nums[0]  # not used directly; we instead simulate after fixing initial pair
            # We actually need to fix the initial pair to be the first two elements at start.
            # So only one choice exists: the target score must be nums[0] + nums[1].
            break

        target = nums[0] + nums[1]
        score = target
        ops = 0
        # Since the operation always deletes the first two elements, the sequence is deterministic.
        j = 0
        while j + 1 < n:
            if nums[j] + nums[j + 1] == score:
                ops += 1
                j += 2
            else:
                break
        return ops
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def can_make(k: int) -> int:
            # Simulate deletions while every operation sum == k
            i = 0
            ops = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] != k:
                    break
                ops += 1
                i += 2
            return ops

        # First operation sum determines the required k, so only need to try candidates.
        # Try k as sum of first two elements, and also possible if we want
        # to allow skipping? Actually we cannot reorder and we always delete first two,
        # so k must be nums[0] + nums[1] for any operation count >= 1.
        k = nums[0] + nums[1]  # only possible score for the first operation
        return can_make(k)
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def can_make(target: int) -> int:
            i = 0
            ops = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] == target:
                    ops += 1
                    i += 2
                else:
                    return ops
            return ops

        # Try score candidates derived from the first operation.
        # If the first operation is valid, its score must be nums[0]+nums[1].
        # There are no other possibilities because operations always remove the first two.
        target = nums[0] + nums[1]
        return can_make(target)
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try every possible target score derived from the first operation:
        # score = nums[0] + nums[1], and we simulate consuming the array greedily.
        best = 0
        for start in (0,):
            target = nums[start] + nums[start + 1]
            ops = 0
            i = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] != target:
                    break
                ops += 1
                i += 2
            best = max(best, ops)

        return best
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try each possible first-pair sum as the target score.
        # At most n-1 operations, but we can just check i from 0..n-2.
        best = 0
        for target in (nums[0] + nums[1],):
            # Since the first operation must use the first two elements,
            # the target is forced to nums[0] + nums[1] (LC problem statement).
            # Build iteratively: each operation consumes next two elements.
            ops = 0
            i = 0
            while i + 1 < n and ops >= 0:
                if nums[i] + nums[i + 1] != target:
                    break
                ops += 1
                i += 2
            best = ops

        return best
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
Given an array of integers called nums, you can perform the following operation while nums contains at least 2 elements:

Choose the first two elements of nums and delete them.

The score of the operation is the sum of the deleted elements.
Your task is to find the maximum number of operations that can be performed, such that all operations have the same score.
Return the maximum number of operations possible that satisfy the condition mentioned above.
 
Example 1:

Input: nums = [3,2,1,4,5]
Output: 2
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [1,4,5].
- Delete the first two elements, with score 1 + 4 = 5, nums = [5].
We are unable to perform any more operations as nums contain only 1 element.
Example 2:

Input: nums = [3,2,6,1,4]
Output: 1
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
We are unable to perform any more operations as the score of the next operation isn't the same as the previous one.

 
Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 1000

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
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
    def maxOperations(self, nums: List[int]) -> int:
        # Try all possible target sums: only sums of the first two elements
        # and one-step ahead (because each operation removes from the front).
        n = len(nums)

        def can_do(target: int) -> int:
            ops = 0
            i = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] != target:
                    break
                ops += 1
                i += 2
            return ops

        # The target sum must be nums[0] + nums[1] if at least one operation is done.
        return can_do(nums[0] + nums[1])
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # All valid solutions are determined by the score of the first operation:
        # If we take x = nums[0] + nums[1], then every later operation must also
        # remove the next two elements summing to x.
        target = nums[0] + nums[1]
        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2
        return ops
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def can_make(target: int) -> bool:
            i = 0
            ops = 0
            n = len(nums)
            while i + 1 < n:
                if nums[i] + nums[i + 1] != target:
                    return False
                ops += 1
                i += 2
            return ops > 0  # at least one operation fits this target

        # Try all possible targets derived from the first operation.
        # Each operation always deletes the first two elements, so targets
        # can only come from nums[0] + nums[1] or nums[0] + nums[2] (if used after one deletion),
        # but actually the second operation's first element depends on first split,
        # and in the greedy structure after choosing a target, the process is determined.
        # We'll just enumerate targets that can appear for the first operation:
        # First operation must be nums[0] + nums[1].
        targets = {nums[0] + nums[1]}
        
        # Note: In this specific process, the first deletion is fixed, so only that target is possible.
        # However, some similar tasks allow choosing target from different indices.
        # Here the operation always deletes first two elements, so only one target is feasible.
        # Still, implement in a general safe way: include only feasible target(s).
        best = 0
        for t in targets:
            i = 0
            ops = 0
            n = len(nums)
            while i + 1 < n and nums[i] + nums[i + 1] == t:
                ops += 1
                i += 2
            best = max(best, ops)
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
    def maxOperations(self, nums: List[int]) -> int:
        def can_make(target: int) -> int:
            i = 0
            ops = 0
            while i + 1 < len(nums):
                if nums[i] + nums[i + 1] == target:
                    ops += 1
                    i += 2
                else:
                    break
            return ops

        best = 0
        # First operation determines the fixed score, so try possible targets
        # based on the first pair (only one possible for each target).
        for target in (nums[0] + nums[1],):
            best = max(best, can_make(target))

        # More generally, consider targets created by choosing the first two elements
        # (but since the operation always uses the first two, only nums[0]+nums[1] matters).
        # The loop above is kept for clarity/minimal extensibility.
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
    def maxOperations(self, nums: List[int]) -> int:
        # Since each operation always removes the first two elements,
        # any valid solution is determined by the target score s,
        # which must equal nums[0] + nums[1] for the first operation.
        s = nums[0] + nums[1]
        ops = 0
        i = 0
        n = len(nums)
        while i + 1 < n and nums[i] + nums[i + 1] == s:
            ops += 1
            i += 2
        return ops
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def can(score: int) -> int:
            ops = 0
            i = 0
            n = len(nums)
            while i + 1 < n:
                if nums[i] + nums[i + 1] != score:
                    break
                ops += 1
                i += 2
            return ops

        n = len(nums)
        if n < 2:
            return 0

        # Possible scores are sums of the first two elements after choosing
        # which first pair score to match: only possible candidate is nums[0]+nums[1].
        # But after deletions, the first pair is always from the current prefix,
        # so score must be nums[0]+nums[1].
        score = nums[0] + nums[1]
        return can(score)
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        # Try all possible first operation scores derived from deleting
        # the first two elements repeatedly (only possible score is fixed
        # once we take the first two elements).
        # But still, since score must be equal for all operations and
        # operations are forced to always delete the first two elements,
        # the score is determined by the first pair: nums[0] + nums[1].
        target = nums[0] + nums[1]

        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2

        return ops
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try all possible target sums using the first operation.
        # Two pointers for a fixed target:
        # - We always delete from the front, so next operation starts at some index i.
        best = 0
        for j in range(1, n, 1):
            # Fix the target as sum of first two elements (always indices 0 and 1)
            # This operation model implies target must equal nums[0] + nums[1].
            # But to align with possible interpretations, keep logic general:
            # In reality, since deletions always remove the first two elements,
            # the score is fixed to nums[0] + nums[1] for any feasible solution.
            pass

        target = nums[0] + nums[1]
        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2
        return ops
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try all possible target scores derived from deleting the first two elements.
        # For each target score, greedily delete as long as possible.
        best = 0
        for i in range(2, n + 1):
            target = nums[0] + nums[1]  # initial candidate score
            # Check target validity against current prefix (only depends on first pair)
            # Greedy simulation with this fixed target.
            ops = 0
            j = 0
            k = 1
            while k + 1 < n - (2 * ops - 1):  # not robust, avoid this approach

                break

        # The above attempt is incorrect; implement correct O(n) greedy per target.
        # Only scores possible come from first two elements since every operation
        # begins with the current first two elements. Therefore there is only one possible target:
        # nums[0] + nums[1]. However, deletions happen, so after deletions the next first two
        # elements must also sum to the same target; that's it.
        target = nums[0] + nums[1]
        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] == target:
                ops += 1
                i += 2
            else:
                break
        return ops
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Choose target score as sum of the first pair.
        target = nums[0] + nums[1]

        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2
        return ops
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
    def maxOperations(self, nums: List[int]) -> int:
        # Try all possible target sums: only sums of the first two elements
        # and one-step ahead (because each operation removes from the front).
        n = len(nums)

        def can_do(target: int) -> int:
            ops = 0
            i = 0
            while i + 1 < n:
                if nums[i] + nums[i + 1] != target:
                    break
                ops += 1
                i += 2
            return ops

        # The target sum must be nums[0] + nums[1] if at least one operation is done.
        return can_do(nums[0] + nums[1])
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # All valid solutions are determined by the score of the first operation:
        # If we take x = nums[0] + nums[1], then every later operation must also
        # remove the next two elements summing to x.
        target = nums[0] + nums[1]
        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2
        return ops
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def can_make(target: int) -> bool:
            i = 0
            ops = 0
            n = len(nums)
            while i + 1 < n:
                if nums[i] + nums[i + 1] != target:
                    return False
                ops += 1
                i += 2
            return ops > 0  # at least one operation fits this target

        # Try all possible targets derived from the first operation.
        # Each operation always deletes the first two elements, so targets
        # can only come from nums[0] + nums[1] or nums[0] + nums[2] (if used after one deletion),
        # but actually the second operation's first element depends on first split,
        # and in the greedy structure after choosing a target, the process is determined.
        # We'll just enumerate targets that can appear for the first operation:
        # First operation must be nums[0] + nums[1].
        targets = {nums[0] + nums[1]}
        
        # Note: In this specific process, the first deletion is fixed, so only that target is possible.
        # However, some similar tasks allow choosing target from different indices.
        # Here the operation always deletes first two elements, so only one target is feasible.
        # Still, implement in a general safe way: include only feasible target(s).
        best = 0
        for t in targets:
            i = 0
            ops = 0
            n = len(nums)
            while i + 1 < n and nums[i] + nums[i + 1] == t:
                ops += 1
                i += 2
            best = max(best, ops)
        return best
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def can_make(target: int) -> int:
            i = 0
            ops = 0
            while i + 1 < len(nums):
                if nums[i] + nums[i + 1] == target:
                    ops += 1
                    i += 2
                else:
                    break
            return ops

        best = 0
        # First operation determines the fixed score, so try possible targets
        # based on the first pair (only one possible for each target).
        for target in (nums[0] + nums[1],):
            best = max(best, can_make(target))

        # More generally, consider targets created by choosing the first two elements
        # (but since the operation always uses the first two, only nums[0]+nums[1] matters).
        # The loop above is kept for clarity/minimal extensibility.
        return best
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # Since each operation always removes the first two elements,
        # any valid solution is determined by the target score s,
        # which must equal nums[0] + nums[1] for the first operation.
        s = nums[0] + nums[1]
        ops = 0
        i = 0
        n = len(nums)
        while i + 1 < n and nums[i] + nums[i + 1] == s:
            ops += 1
            i += 2
        return ops
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def can(score: int) -> int:
            ops = 0
            i = 0
            n = len(nums)
            while i + 1 < n:
                if nums[i] + nums[i + 1] != score:
                    break
                ops += 1
                i += 2
            return ops

        n = len(nums)
        if n < 2:
            return 0

        # Possible scores are sums of the first two elements after choosing
        # which first pair score to match: only possible candidate is nums[0]+nums[1].
        # But after deletions, the first pair is always from the current prefix,
        # so score must be nums[0]+nums[1].
        score = nums[0] + nums[1]
        return can(score)
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        # Try all possible first operation scores derived from deleting
        # the first two elements repeatedly (only possible score is fixed
        # once we take the first two elements).
        # But still, since score must be equal for all operations and
        # operations are forced to always delete the first two elements,
        # the score is determined by the first pair: nums[0] + nums[1].
        target = nums[0] + nums[1]

        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2

        return ops
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try all possible target sums using the first operation.
        # Two pointers for a fixed target:
        # - We always delete from the front, so next operation starts at some index i.
        best = 0
        for j in range(1, n, 1):
            # Fix the target as sum of first two elements (always indices 0 and 1)
            # This operation model implies target must equal nums[0] + nums[1].
            # But to align with possible interpretations, keep logic general:
            # In reality, since deletions always remove the first two elements,
            # the score is fixed to nums[0] + nums[1] for any feasible solution.
            pass

        target = nums[0] + nums[1]
        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2
        return ops
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try all possible target scores derived from deleting the first two elements.
        # For each target score, greedily delete as long as possible.
        best = 0
        for i in range(2, n + 1):
            target = nums[0] + nums[1]  # initial candidate score
            # Check target validity against current prefix (only depends on first pair)
            # Greedy simulation with this fixed target.
            ops = 0
            j = 0
            k = 1
            while k + 1 < n - (2 * ops - 1):  # not robust, avoid this approach

                break

        # The above attempt is incorrect; implement correct O(n) greedy per target.
        # Only scores possible come from first two elements since every operation
        # begins with the current first two elements. Therefore there is only one possible target:
        # nums[0] + nums[1]. However, deletions happen, so after deletions the next first two
        # elements must also sum to the same target; that's it.
        target = nums[0] + nums[1]
        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] == target:
                ops += 1
                i += 2
            else:
                break
        return ops
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Choose target score as sum of the first pair.
        target = nums[0] + nums[1]

        ops = 0
        i = 0
        while i + 1 < n:
            if nums[i] + nums[i + 1] != target:
                break
            ops += 1
            i += 2
        return ops
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "1",
      "actual": "1",
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
      "expected": "50",
      "actual": "50",
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
      "expected": "49",
      "actual": "49",
      "error": ""
    }
  ]
}
```

</details>
