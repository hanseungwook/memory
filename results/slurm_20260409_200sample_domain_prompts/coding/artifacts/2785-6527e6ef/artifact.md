# Problem 2785

- Domain: `coding`

## Problem

```text
You are given a 0-indexed permutation of n integers nums.
A permutation is called semi-ordered if the first number equals 1 and the last number equals n. You can perform the below operation as many times as you want until you make nums a semi-ordered permutation:

Pick two adjacent elements in nums, then swap them.

Return the minimum number of operations to make nums a semi-ordered permutation.
A permutation is a sequence of integers from 1 to n of length n containing each number exactly once.
 
Example 1:

Input: nums = [2,1,4,3]
Output: 2
Explanation: We can make the permutation semi-ordered using these sequence of operations: 
1 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
2 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than two operations that make nums a semi-ordered permutation. 

Example 2:

Input: nums = [2,4,1,3]
Output: 3
Explanation: We can make the permutation semi-ordered using these sequence of operations:
1 - swap i = 1 and j = 2. The permutation becomes [2,1,4,3].
2 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
3 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than three operations that make nums a semi-ordered permutation.

Example 3:

Input: nums = [1,3,4,2,5]
Output: 0
Explanation: The permutation is already a semi-ordered permutation.

 
Constraints:

2 <= nums.length == n <= 50
1 <= nums[i] <= 50
nums is a permutation.
```

### Starter Code

```python
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[2, 1, 4, 3]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[2, 4, 1, 3]",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "[1, 3, 4, 2, 5]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[1, 3, 2]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[3, 1, 2]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[2, 1, 3]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[1, 2, 3]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[2, 4, 1, 3]",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "[1, 3, 2, 4]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[1, 5, 3, 2, 4]",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "[1, 2, 3, 4, 5]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[5, 1, 6, 3, 4, 2]",
    "output": "4",
    "testtype": "functional"
  },
  {
    "input": "[1, 28, 39, 12, 14, 6, 15, 27, 17, 38, 45, 16, 25, 37, 26, 44, 46, 10, 33, 40, 35, 4, 32, 34, 11, 9, 21, 43, 41, 48, 22, 30, 42, 50, 8, 29, 23, 5, 49, 13, 7, 3, 24, 20, 2, 31, 19, 36, 18, 47]",
    "output": "16",
    "testtype": "functional"
  },
  {
    "input": "[50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]",
    "output": "97",
    "testtype": "functional"
  },
  {
    "input": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1]",
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
You are given a 0-indexed permutation of n integers nums.
A permutation is called semi-ordered if the first number equals 1 and the last number equals n. You can perform the below operation as many times as you want until you make nums a semi-ordered permutation:

Pick two adjacent elements in nums, then swap them.

Return the minimum number of operations to make nums a semi-ordered permutation.
A permutation is a sequence of integers from 1 to n of length n containing each number exactly once.
 
Example 1:

Input: nums = [2,1,4,3]
Output: 2
Explanation: We can make the permutation semi-ordered using these sequence of operations: 
1 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
2 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than two operations that make nums a semi-ordered permutation. 

Example 2:

Input: nums = [2,4,1,3]
Output: 3
Explanation: We can make the permutation semi-ordered using these sequence of operations:
1 - swap i = 1 and j = 2. The permutation becomes [2,1,4,3].
2 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
3 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than three operations that make nums a semi-ordered permutation.

Example 3:

Input: nums = [1,3,4,2,5]
Output: 0
Explanation: The permutation is already a semi-ordered permutation.

 
Constraints:

2 <= nums.length == n <= 50
1 <= nums[i] <= 50
nums is a permutation.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # Minimum adjacent swaps to bring 1 to index 0
        pos1 = nums.index(1)
        swaps_left = pos1  # moving left by pos1 swaps

        # Minimum adjacent swaps to bring n to index n-1 after moving 1
        # If 1 is originally to the left of n's position, its movement left shifts n left by 1,
        # otherwise n's index is unchanged.
        posn = nums.index(n)
        if pos1 < posn:
            posn -= 1
        swaps_right = (n - 1) - posn

        return swaps_left + swaps_right
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If 1 and n are on the "correct sides" already, they can be fixed
        # without interfering too much; otherwise, operations must include
        # moving them across each other when necessary.
        # Since swaps are adjacent, minimum swaps to move an element to a target
        # position is its distance, but moving one element shifts positions
        # of others.
        #
        # We can reason in terms of relative order:
        # - We need 1 at index 0 and n at index n-1.
        # Let i = pos1, j = posn.
        # If i < j:
        #   Move 1 left by i swaps -> n stays at index j-i.
        #   Then move n right to n-1 by (n-1 - (j-i)) swaps.
        # Else (i > j):
        #   Move n left by (j to 0?) can't; n needs to go right to n-1.
        #   But moving 1 left by i swaps will shift n one step left each time
        #   1 crosses it. Total adjustments lead to:
        #   First move 1 left by i swaps: n shifts to index j (since 1 crosses it,
        #   their relative order flips). Equivalent closed-form:
        #   swaps = i + (n-1 - j) + extra where necessary.
        #
        # Known correct simplification for this problem:
        # Let i = pos1, j = posn.
        # If i < j:
        #   answer = i + (n - 1 - j)
        # Else:
        #   answer = i + (n - 1 - j) - 1 + 1? (handle crossing)
        #
        # More robust approach: simulate with counting swaps required by
        # greedy fixed-point method without actually building array:
        # We place 1 to front by swapping adjacent until it reaches index 0.
        # After that, we place n to end by swapping adjacent until it reaches index n-1.
        # This counts minimum because swapping adjacent to move an element to target
        # while fixing others is optimal.
        arr = nums[:]  # only positions are needed, but n<=50 so fine

        ops = 0
        # Move 1 to index 0
        while arr[0] != 1:
            k = arr.index(1)
            # swap positions k-1 and k until index 0
            # Since k is where 1 currently is:
            # each adjacent swap reduces k by 1
            while k > 0:
                arr[k-1], arr[k] = arr[k], arr[k-1]
                ops += 1
                k -= 1

        # Move n to index n-1
        target = n - 1
        while arr[target] != n:
            k = arr.index(n)
            while k < target:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                ops += 1
                k += 1

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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Minimum swaps to bring 1 to index 0:
        i1 = nums.index(1)
        ops = i1  # swapping 1 left one step at a time

        # Minimum swaps to bring n to index n-1.
        # After moving 1 to the front, the position of n may shift only if n lies left of i1.
        in_pos = nums.index(n)
        if in_pos < i1:
            in_pos += 1  # it shifts right by one when 1 passes it

        ops += (n - 1 - in_pos)  # swapping n right one step at a time
        return ops
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos = [0] * (n + 1)
        for i, v in enumerate(nums):
            pos[v] = i

        # Fix 1 to position 0
        # Using adjacent swaps, moving element from index a to b costs abs(a-b)
        ops = abs(pos[1] - 0)

        # After bringing 1 to the front, the relative indices of other elements may shift.
        # If 1 was to the right, moving it left shifts elements between [0, pos[1]-1] right by 1.
        # If 1 was to the left, moving it right shifts elements between [pos[1]+1, n-1] left by 1.
        if pos[1] > 0:
            # 1 moves left by pos[1]
            # Only elements originally in [0, pos[1)-1] shift right by 1
            if pos[n] < pos[1]:
                ops += 1  # because n's position increases by 1
        else:
            # already at front; no shift
            pass

        # Fix n to position n-1 (count adjacent swaps given updated position)
        # Updated position of n is pos[n] plus 1 if pos[n] < pos[1] (when pos[1] > 0)
        new_pos_n = pos[n]
        if pos[1] > 0 and new_pos_n < pos[1]:
            new_pos_n += 1

        ops += abs(new_pos_n - (n - 1))
        return ops
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Minimum adjacent swaps to bring 1 to index 0
        # and n to index n-1. Moves are independent because we
        # can always perform swaps in an order that doesn't interfere
        # with the minimality of each target.
        ans = 0
        ans += pos1  # swaps moving 1 left to index 0

        # When moving n to the end, if n is currently left of position of 1,
        # then after moving 1 left, n's index decreases by 1 (because 1 crosses it).
        # We account for the effect on the number of swaps needed.
        if posn < pos1:
            ans += (n - 1 - (posn)) - 1
        else:
            ans += (n - 1 - posn)

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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Find current positions of 1 and n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # We need to bring 1 to index 0 and n to index n-1 using adjacent swaps.
        # Adjacent swaps distance:
        moves1 = pos1                          # swaps to move 1 left to index 0
        movesn = (n - 1) - posn               # swaps to move n right to index n-1

        # If paths overlap (pos1 > posn), moving 1 left crosses n, which forces extra swap.
        # The overlap distance effectively becomes moves1 + movesn + 1.
        # This happens when 1 starts to the right of n.
        if pos1 > posn:
            return moves1 + movesn + 1
        return moves1 + movesn
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # positions of value 1 and value n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Bring 1 to index 0 by adjacent swaps
        # Bringing n to index n-1 by adjacent swaps
        # Since swaps only move elements within array, we must handle overlap:
        # If pos1 < posn, moving 1 left shifts indices of elements between,
        # but n's relative movement count depends on the order.
        ans = 0
        if pos1 < posn:
            # Move 1 to front: pos1 swaps
            ans += pos1
            # After moving 1 left by pos1 steps, n shifts left by 1*?:
            # elements between 0..pos1-1 removed; effectively n index decreases by pos1.
            ans += (posn - 1) - pos1  # equivalent to (posn - pos1 - 1) + (n-1 - (posn - pos1))
            # Let's compute directly for clarity:
            # After moving 1 to 0, n is at index posn - pos1.
            # Needed swaps to reach n-1 is (n-1) - (posn - pos1)
            ans = pos1 + ((n - 1) - (posn - pos1))
        else:
            # Move n to end first: (n-1 - posn)
            ans += (n - 1 - posn)
            # After moving n right by that many steps, 1 index unchanged if 1 is left of n
            # because 1 lies before posn and n moves right across elements after it.
            ans += pos1  # bring 1 to front by pos1 swaps

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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Find current positions of 1 and n
        pos1 = 0
        posn = 0
        for i, v in enumerate(nums):
            if v == 1:
                pos1 = i
            elif v == n:
                posn = i

        # Minimum adjacent swaps to move 1 to index 0 and n to index n-1.
        # Moving one may shift the other depending on whether it lies in the moved interval.
        if pos1 < posn:
            # Move 1 left to 0: distance pos1
            # After moving 1 left, n's position decreases by pos1 (it gets shifted left)
            # Then move n to n-1: remaining distance (n-1 - (posn - pos1))
            return pos1 + (n - 1 - (posn - pos1))
        else:
            # posn < pos1
            # Move n right to n-1: distance (n-1 - posn)
            # After moving n right, 1's position increases by (n-1 - posn)
            # Then move 1 to 0: remaining distance (pos1 + (n-1 - posn))
            return (n - 1 - posn) + (pos1 + (n - 1 - posn))
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # Find positions of 1 and n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If we swap adjacent elements, the number of swaps needed
        # to move an element from i to j is |i-j|.
        # But moves may overlap; when pos1 < posn, moving 1 right and n left
        # compete for the same swaps in the interval between them.
        if pos1 < posn:
            # Move 1 to the front: pos1 swaps leftwards
            # Move n to the end: (n-1 - posn) swaps rightwards
            # Total for disjoint parts minus overlap: when 1 and n cross,
            # their relative order changes; minimal swaps equals the size
            # of interval between them.
            return pos1 + (n - 1 - posn) + (posn - pos1 - 1)
            # Simplifies to n-2 if already correct order? but keep correct formula.
        else:
            # When pos1 > posn, 1 is to the right of n; to get 1 to front and n to end,
            # they must cross at some point.
            # Minimal swaps equals number of elements to move for 1 plus for n.
            return (pos1) + (n - 1 - posn)

        # Note: The above conditional is incorrect due to the overlap logic.
        # We'll provide the correct implementation below.

    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Move 1 to index 0, and n to index n-1.
        # We only need count swaps; with adjacent swaps:
        # - Swapping 1 left by pos1 steps costs pos1.
        # - Swapping n right by (n-1-posn) steps costs that.
        # However, if 1 starts to the left of n, moving them toward their targets
        # does not require extra beyond these two independent moves.
        # If 1 is to the right of n, their paths overlap by 1 swap each time they cross,
        # which is automatically captured by independent counts except for overlap:
        # the true minimal is:
        #   if pos1 < posn: (pos1) + (n-1-posn)
        #   else:          (pos1) + (n-1-posn) - 1
        # Reason: when pos1 > posn, one swap will move both toward targets while crossing,
        # reducing total by 1 compared to naive sum.
        ans = pos1 + (n - 1 - posn)
        if pos1 > posn:
            ans -= 1
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Minimum swaps to bring 1 to index 0 equals its current index,
        # since adjacent swaps move it one step per operation.
        pos1 = nums.index(1)
        ops_left = pos1

        # Minimum swaps to bring n to index n-1.
        # After moving 1 to the front, relative positions to the right of index 0
        # are affected only if n lies to the right of 1's original position.
        posn = nums.index(n)
        ops_right = (n - 1 - posn)
        if pos1 < posn:
            # When 1 moves left, elements between indices [0, pos1-1] are shifted right by 1,
            # which decreases posn by 1.
            ops_right = (n - 2 - (posn - 1))  # equivalent to n-1-(posn-1)
        else:
            # pos1 > posn: n is left of 1, its index unchanged by moving 1 to the front
            ops_right = (n - 1 - posn)

        return ops_left + ops_right
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.0000 | `fail` |
| 1 | 1.0000 | `full` |
| 2 | 1.0000 | `full` |
| 3 | 0.6667 | `partial` |
| 4 | 1.0000 | `full` |
| 5 | 0.6667 | `partial` |
| 6 | 0.4667 | `partial` |
| 7 | 0.4667 | `partial` |
| 8 | 1.0000 | `full` |
| 9 | 0.6667 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "4",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "4",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "4",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "4",
      "actual": "5",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "16",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "98",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "50",
      "error": "Wrong Answer"
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 10,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "4",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
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
      "passed": false,
      "expected": "3",
      "actual": "4",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "98",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "50",
      "error": "Wrong Answer"
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 10,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "4",
      "error": "Wrong Answer"
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
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "99",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "51",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 6</summary>

```json
{
  "passed": 7,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "4",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "4",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "4",
      "actual": "5",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "98",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "50",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "passed": 7,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "6",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "5",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "6",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "4",
      "actual": "5",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "147",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "51",
      "error": "Wrong Answer"
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 10,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "4",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
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
      "passed": false,
      "expected": "3",
      "actual": "4",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "98",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "50",
      "error": "Wrong Answer"
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
You are given a 0-indexed permutation of n integers nums.
A permutation is called semi-ordered if the first number equals 1 and the last number equals n. You can perform the below operation as many times as you want until you make nums a semi-ordered permutation:

Pick two adjacent elements in nums, then swap them.

Return the minimum number of operations to make nums a semi-ordered permutation.
A permutation is a sequence of integers from 1 to n of length n containing each number exactly once.
 
Example 1:

Input: nums = [2,1,4,3]
Output: 2
Explanation: We can make the permutation semi-ordered using these sequence of operations: 
1 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
2 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than two operations that make nums a semi-ordered permutation. 

Example 2:

Input: nums = [2,4,1,3]
Output: 3
Explanation: We can make the permutation semi-ordered using these sequence of operations:
1 - swap i = 1 and j = 2. The permutation becomes [2,1,4,3].
2 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
3 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than three operations that make nums a semi-ordered permutation.

Example 3:

Input: nums = [1,3,4,2,5]
Output: 0
Explanation: The permutation is already a semi-ordered permutation.

 
Constraints:

2 <= nums.length == n <= 50
1 <= nums[i] <= 50
nums is a permutation.

### Solutions
#### Correct
Attempt 1
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If 1 and n are on the "correct sides" already, they can be fixed
        # without interfering too much; otherwise, operations must include
        # moving them across each other when necessary.
        # Since swaps are adjacent, minimum swaps to move an element to a target
        # position is its distance, but moving one element shifts positions
        # of others.
        #
        # We can reason in terms of relative order:
        # - We need 1 at index 0 and n at index n-1.
        # Let i = pos1, j = posn.
        # If i < j:
        #   Move 1 left by i swaps -> n stays at index j-i.
        #   Then move n right to n-1 by (n-1 - (j-i)) swaps.
        # Else (i > j):
        #   Move n left by (j to 0?) can't; n needs to go right to n-1.
        #   But moving 1 left by i swaps will shift n one step left each time
        #   1 crosses it. Total adjustments lead to:
        #   First move 1 left by i swaps: n shifts to index j (since 1 crosses it,
        #   their relative order flips). Equivalent closed-form:
        #   swaps = i + (n-1 - j) + extra where necessary.
        #
        # Known correct simplification for this problem:
        # Let i = pos1, j = posn.
        # If i < j:
        #   answer = i + (n - 1 - j)
        # Else:
        #   answer = i + (n - 1 - j) - 1 + 1? (handle crossing)
        #
        # More robust approach: simulate with counting swaps required by
        # greedy fixed-point method without actually building array:
        # We place 1 to front by swapping adjacent until it reaches index 0.
        # After that, we place n to end by swapping adjacent until it reaches index n-1.
        # This counts minimum because swapping adjacent to move an element to target
        # while fixing others is optimal.
        arr = nums[:]  # only positions are needed, but n<=50 so fine

        ops = 0
        # Move 1 to index 0
        while arr[0] != 1:
            k = arr.index(1)
            # swap positions k-1 and k until index 0
            # Since k is where 1 currently is:
            # each adjacent swap reduces k by 1
            while k > 0:
                arr[k-1], arr[k] = arr[k], arr[k-1]
                ops += 1
                k -= 1

        # Move n to index n-1
        target = n - 1
        while arr[target] != n:
            k = arr.index(n)
            while k < target:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                ops += 1
                k += 1

        return ops
```

Attempt 2
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Minimum swaps to bring 1 to index 0:
        i1 = nums.index(1)
        ops = i1  # swapping 1 left one step at a time

        # Minimum swaps to bring n to index n-1.
        # After moving 1 to the front, the position of n may shift only if n lies left of i1.
        in_pos = nums.index(n)
        if in_pos < i1:
            in_pos += 1  # it shifts right by one when 1 passes it

        ops += (n - 1 - in_pos)  # swapping n right one step at a time
        return ops
```

Attempt 3
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Minimum adjacent swaps to bring 1 to index 0
        # and n to index n-1. Moves are independent because we
        # can always perform swaps in an order that doesn't interfere
        # with the minimality of each target.
        ans = 0
        ans += pos1  # swaps moving 1 left to index 0

        # When moving n to the end, if n is currently left of position of 1,
        # then after moving 1 left, n's index decreases by 1 (because 1 crosses it).
        # We account for the effect on the number of swaps needed.
        if posn < pos1:
            ans += (n - 1 - (posn)) - 1
        else:
            ans += (n - 1 - posn)

        return ans
```

Attempt 4
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # Find positions of 1 and n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If we swap adjacent elements, the number of swaps needed
        # to move an element from i to j is |i-j|.
        # But moves may overlap; when pos1 < posn, moving 1 right and n left
        # compete for the same swaps in the interval between them.
        if pos1 < posn:
            # Move 1 to the front: pos1 swaps leftwards
            # Move n to the end: (n-1 - posn) swaps rightwards
            # Total for disjoint parts minus overlap: when 1 and n cross,
            # their relative order changes; minimal swaps equals the size
            # of interval between them.
            return pos1 + (n - 1 - posn) + (posn - pos1 - 1)
            # Simplifies to n-2 if already correct order? but keep correct formula.
        else:
            # When pos1 > posn, 1 is to the right of n; to get 1 to front and n to end,
            # they must cross at some point.
            # Minimal swaps equals number of elements to move for 1 plus for n.
            return (pos1) + (n - 1 - posn)

        # Note: The above conditional is incorrect due to the overlap logic.
        # We'll provide the correct implementation below.

    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Move 1 to index 0, and n to index n-1.
        # We only need count swaps; with adjacent swaps:
        # - Swapping 1 left by pos1 steps costs pos1.
        # - Swapping n right by (n-1-posn) steps costs that.
        # However, if 1 starts to the left of n, moving them toward their targets
        # does not require extra beyond these two independent moves.
        # If 1 is to the right of n, their paths overlap by 1 swap each time they cross,
        # which is automatically captured by independent counts except for overlap:
        # the true minimal is:
        #   if pos1 < posn: (pos1) + (n-1-posn)
        #   else:          (pos1) + (n-1-posn) - 1
        # Reason: when pos1 > posn, one swap will move both toward targets while crossing,
        # reducing total by 1 compared to naive sum.
        ans = pos1 + (n - 1 - posn)
        if pos1 > posn:
            ans -= 1
        return ans
```

#### Partially Correct
Attempt 1
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos = [0] * (n + 1)
        for i, v in enumerate(nums):
            pos[v] = i

        # Fix 1 to position 0
        # Using adjacent swaps, moving element from index a to b costs abs(a-b)
        ops = abs(pos[1] - 0)

        # After bringing 1 to the front, the relative indices of other elements may shift.
        # If 1 was to the right, moving it left shifts elements between [0, pos[1]-1] right by 1.
        # If 1 was to the left, moving it right shifts elements between [pos[1]+1, n-1] left by 1.
        if pos[1] > 0:
            # 1 moves left by pos[1]
            # Only elements originally in [0, pos[1)-1] shift right by 1
            if pos[n] < pos[1]:
                ops += 1  # because n's position increases by 1
        else:
            # already at front; no shift
            pass

        # Fix n to position n-1 (count adjacent swaps given updated position)
        # Updated position of n is pos[n] plus 1 if pos[n] < pos[1] (when pos[1] > 0)
        new_pos_n = pos[n]
        if pos[1] > 0 and new_pos_n < pos[1]:
            new_pos_n += 1

        ops += abs(new_pos_n - (n - 1))
        return ops
```

Attempt 2
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Find current positions of 1 and n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # We need to bring 1 to index 0 and n to index n-1 using adjacent swaps.
        # Adjacent swaps distance:
        moves1 = pos1                          # swaps to move 1 left to index 0
        movesn = (n - 1) - posn               # swaps to move n right to index n-1

        # If paths overlap (pos1 > posn), moving 1 left crosses n, which forces extra swap.
        # The overlap distance effectively becomes moves1 + movesn + 1.
        # This happens when 1 starts to the right of n.
        if pos1 > posn:
            return moves1 + movesn + 1
        return moves1 + movesn
```

Attempt 3
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # positions of value 1 and value n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Bring 1 to index 0 by adjacent swaps
        # Bringing n to index n-1 by adjacent swaps
        # Since swaps only move elements within array, we must handle overlap:
        # If pos1 < posn, moving 1 left shifts indices of elements between,
        # but n's relative movement count depends on the order.
        ans = 0
        if pos1 < posn:
            # Move 1 to front: pos1 swaps
            ans += pos1
            # After moving 1 left by pos1 steps, n shifts left by 1*?:
            # elements between 0..pos1-1 removed; effectively n index decreases by pos1.
            ans += (posn - 1) - pos1  # equivalent to (posn - pos1 - 1) + (n-1 - (posn - pos1))
            # Let's compute directly for clarity:
            # After moving 1 to 0, n is at index posn - pos1.
            # Needed swaps to reach n-1 is (n-1) - (posn - pos1)
            ans = pos1 + ((n - 1) - (posn - pos1))
        else:
            # Move n to end first: (n-1 - posn)
            ans += (n - 1 - posn)
            # After moving n right by that many steps, 1 index unchanged if 1 is left of n
            # because 1 lies before posn and n moves right across elements after it.
            ans += pos1  # bring 1 to front by pos1 swaps

        return ans
```

Attempt 4
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Find current positions of 1 and n
        pos1 = 0
        posn = 0
        for i, v in enumerate(nums):
            if v == 1:
                pos1 = i
            elif v == n:
                posn = i

        # Minimum adjacent swaps to move 1 to index 0 and n to index n-1.
        # Moving one may shift the other depending on whether it lies in the moved interval.
        if pos1 < posn:
            # Move 1 left to 0: distance pos1
            # After moving 1 left, n's position decreases by pos1 (it gets shifted left)
            # Then move n to n-1: remaining distance (n-1 - (posn - pos1))
            return pos1 + (n - 1 - (posn - pos1))
        else:
            # posn < pos1
            # Move n right to n-1: distance (n-1 - posn)
            # After moving n right, 1's position increases by (n-1 - posn)
            # Then move 1 to 0: remaining distance (pos1 + (n-1 - posn))
            return (n - 1 - posn) + (pos1 + (n - 1 - posn))
```

Attempt 5
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Minimum swaps to bring 1 to index 0 equals its current index,
        # since adjacent swaps move it one step per operation.
        pos1 = nums.index(1)
        ops_left = pos1

        # Minimum swaps to bring n to index n-1.
        # After moving 1 to the front, relative positions to the right of index 0
        # are affected only if n lies to the right of 1's original position.
        posn = nums.index(n)
        ops_right = (n - 1 - posn)
        if pos1 < posn:
            # When 1 moves left, elements between indices [0, pos1-1] are shifted right by 1,
            # which decreases posn by 1.
            ops_right = (n - 2 - (posn - 1))  # equivalent to n-1-(posn-1)
        else:
            # pos1 > posn: n is left of 1, its index unchanged by moving 1 to the front
            ops_right = (n - 1 - posn)

        return ops_left + ops_right
```

#### Incorrect
Attempt 1
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # Minimum adjacent swaps to bring 1 to index 0
        pos1 = nums.index(1)
        swaps_left = pos1  # moving left by pos1 swaps

        # Minimum adjacent swaps to bring n to index n-1 after moving 1
        # If 1 is originally to the left of n's position, its movement left shifts n left by 1,
        # otherwise n's index is unchanged.
        posn = nums.index(n)
        if pos1 < posn:
            posn -= 1
        swaps_right = (n - 1) - posn

        return swaps_left + swaps_right
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If 1 and n are on the "correct sides" already, they can be fixed
        # without interfering too much; otherwise, operations must include
        # moving them across each other when necessary.
        # Since swaps are adjacent, minimum swaps to move an element to a target
        # position is its distance, but moving one element shifts positions
        # of others.
        #
        # We can reason in terms of relative order:
        # - We need 1 at index 0 and n at index n-1.
        # Let i = pos1, j = posn.
        # If i < j:
        #   Move 1 left by i swaps -> n stays at index j-i.
        #   Then move n right to n-1 by (n-1 - (j-i)) swaps.
        # Else (i > j):
        #   Move n left by (j to 0?) can't; n needs to go right to n-1.
        #   But moving 1 left by i swaps will shift n one step left each time
        #   1 crosses it. Total adjustments lead to:
        #   First move 1 left by i swaps: n shifts to index j (since 1 crosses it,
        #   their relative order flips). Equivalent closed-form:
        #   swaps = i + (n-1 - j) + extra where necessary.
        #
        # Known correct simplification for this problem:
        # Let i = pos1, j = posn.
        # If i < j:
        #   answer = i + (n - 1 - j)
        # Else:
        #   answer = i + (n - 1 - j) - 1 + 1? (handle crossing)
        #
        # More robust approach: simulate with counting swaps required by
        # greedy fixed-point method without actually building array:
        # We place 1 to front by swapping adjacent until it reaches index 0.
        # After that, we place n to end by swapping adjacent until it reaches index n-1.
        # This counts minimum because swapping adjacent to move an element to target
        # while fixing others is optimal.
        arr = nums[:]  # only positions are needed, but n<=50 so fine

        ops = 0
        # Move 1 to index 0
        while arr[0] != 1:
            k = arr.index(1)
            # swap positions k-1 and k until index 0
            # Since k is where 1 currently is:
            # each adjacent swap reduces k by 1
            while k > 0:
                arr[k-1], arr[k] = arr[k], arr[k-1]
                ops += 1
                k -= 1

        # Move n to index n-1
        target = n - 1
        while arr[target] != n:
            k = arr.index(n)
            while k < target:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                ops += 1
                k += 1

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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Minimum swaps to bring 1 to index 0:
        i1 = nums.index(1)
        ops = i1  # swapping 1 left one step at a time

        # Minimum swaps to bring n to index n-1.
        # After moving 1 to the front, the position of n may shift only if n lies left of i1.
        in_pos = nums.index(n)
        if in_pos < i1:
            in_pos += 1  # it shifts right by one when 1 passes it

        ops += (n - 1 - in_pos)  # swapping n right one step at a time
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Minimum adjacent swaps to bring 1 to index 0
        # and n to index n-1. Moves are independent because we
        # can always perform swaps in an order that doesn't interfere
        # with the minimality of each target.
        ans = 0
        ans += pos1  # swaps moving 1 left to index 0

        # When moving n to the end, if n is currently left of position of 1,
        # then after moving 1 left, n's index decreases by 1 (because 1 crosses it).
        # We account for the effect on the number of swaps needed.
        if posn < pos1:
            ans += (n - 1 - (posn)) - 1
        else:
            ans += (n - 1 - posn)

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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # Find positions of 1 and n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If we swap adjacent elements, the number of swaps needed
        # to move an element from i to j is |i-j|.
        # But moves may overlap; when pos1 < posn, moving 1 right and n left
        # compete for the same swaps in the interval between them.
        if pos1 < posn:
            # Move 1 to the front: pos1 swaps leftwards
            # Move n to the end: (n-1 - posn) swaps rightwards
            # Total for disjoint parts minus overlap: when 1 and n cross,
            # their relative order changes; minimal swaps equals the size
            # of interval between them.
            return pos1 + (n - 1 - posn) + (posn - pos1 - 1)
            # Simplifies to n-2 if already correct order? but keep correct formula.
        else:
            # When pos1 > posn, 1 is to the right of n; to get 1 to front and n to end,
            # they must cross at some point.
            # Minimal swaps equals number of elements to move for 1 plus for n.
            return (pos1) + (n - 1 - posn)

        # Note: The above conditional is incorrect due to the overlap logic.
        # We'll provide the correct implementation below.

    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Move 1 to index 0, and n to index n-1.
        # We only need count swaps; with adjacent swaps:
        # - Swapping 1 left by pos1 steps costs pos1.
        # - Swapping n right by (n-1-posn) steps costs that.
        # However, if 1 starts to the left of n, moving them toward their targets
        # does not require extra beyond these two independent moves.
        # If 1 is to the right of n, their paths overlap by 1 swap each time they cross,
        # which is automatically captured by independent counts except for overlap:
        # the true minimal is:
        #   if pos1 < posn: (pos1) + (n-1-posn)
        #   else:          (pos1) + (n-1-posn) - 1
        # Reason: when pos1 > posn, one swap will move both toward targets while crossing,
        # reducing total by 1 compared to naive sum.
        ans = pos1 + (n - 1 - posn)
        if pos1 > posn:
            ans -= 1
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos = [0] * (n + 1)
        for i, v in enumerate(nums):
            pos[v] = i

        # Fix 1 to position 0
        # Using adjacent swaps, moving element from index a to b costs abs(a-b)
        ops = abs(pos[1] - 0)

        # After bringing 1 to the front, the relative indices of other elements may shift.
        # If 1 was to the right, moving it left shifts elements between [0, pos[1]-1] right by 1.
        # If 1 was to the left, moving it right shifts elements between [pos[1]+1, n-1] left by 1.
        if pos[1] > 0:
            # 1 moves left by pos[1]
            # Only elements originally in [0, pos[1)-1] shift right by 1
            if pos[n] < pos[1]:
                ops += 1  # because n's position increases by 1
        else:
            # already at front; no shift
            pass

        # Fix n to position n-1 (count adjacent swaps given updated position)
        # Updated position of n is pos[n] plus 1 if pos[n] < pos[1] (when pos[1] > 0)
        new_pos_n = pos[n]
        if pos[1] > 0 and new_pos_n < pos[1]:
            new_pos_n += 1

        ops += abs(new_pos_n - (n - 1))
        return ops
```
```

</details>

<details>
<summary>partial attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Find current positions of 1 and n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # We need to bring 1 to index 0 and n to index n-1 using adjacent swaps.
        # Adjacent swaps distance:
        moves1 = pos1                          # swaps to move 1 left to index 0
        movesn = (n - 1) - posn               # swaps to move n right to index n-1

        # If paths overlap (pos1 > posn), moving 1 left crosses n, which forces extra swap.
        # The overlap distance effectively becomes moves1 + movesn + 1.
        # This happens when 1 starts to the right of n.
        if pos1 > posn:
            return moves1 + movesn + 1
        return moves1 + movesn
```
```

</details>

<details>
<summary>partial attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # positions of value 1 and value n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Bring 1 to index 0 by adjacent swaps
        # Bringing n to index n-1 by adjacent swaps
        # Since swaps only move elements within array, we must handle overlap:
        # If pos1 < posn, moving 1 left shifts indices of elements between,
        # but n's relative movement count depends on the order.
        ans = 0
        if pos1 < posn:
            # Move 1 to front: pos1 swaps
            ans += pos1
            # After moving 1 left by pos1 steps, n shifts left by 1*?:
            # elements between 0..pos1-1 removed; effectively n index decreases by pos1.
            ans += (posn - 1) - pos1  # equivalent to (posn - pos1 - 1) + (n-1 - (posn - pos1))
            # Let's compute directly for clarity:
            # After moving 1 to 0, n is at index posn - pos1.
            # Needed swaps to reach n-1 is (n-1) - (posn - pos1)
            ans = pos1 + ((n - 1) - (posn - pos1))
        else:
            # Move n to end first: (n-1 - posn)
            ans += (n - 1 - posn)
            # After moving n right by that many steps, 1 index unchanged if 1 is left of n
            # because 1 lies before posn and n moves right across elements after it.
            ans += pos1  # bring 1 to front by pos1 swaps

        return ans
```
```

</details>

<details>
<summary>partial attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Find current positions of 1 and n
        pos1 = 0
        posn = 0
        for i, v in enumerate(nums):
            if v == 1:
                pos1 = i
            elif v == n:
                posn = i

        # Minimum adjacent swaps to move 1 to index 0 and n to index n-1.
        # Moving one may shift the other depending on whether it lies in the moved interval.
        if pos1 < posn:
            # Move 1 left to 0: distance pos1
            # After moving 1 left, n's position decreases by pos1 (it gets shifted left)
            # Then move n to n-1: remaining distance (n-1 - (posn - pos1))
            return pos1 + (n - 1 - (posn - pos1))
        else:
            # posn < pos1
            # Move n right to n-1: distance (n-1 - posn)
            # After moving n right, 1's position increases by (n-1 - posn)
            # Then move 1 to 0: remaining distance (pos1 + (n-1 - posn))
            return (n - 1 - posn) + (pos1 + (n - 1 - posn))
```
```

</details>

<details>
<summary>partial attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Minimum swaps to bring 1 to index 0 equals its current index,
        # since adjacent swaps move it one step per operation.
        pos1 = nums.index(1)
        ops_left = pos1

        # Minimum swaps to bring n to index n-1.
        # After moving 1 to the front, relative positions to the right of index 0
        # are affected only if n lies to the right of 1's original position.
        posn = nums.index(n)
        ops_right = (n - 1 - posn)
        if pos1 < posn:
            # When 1 moves left, elements between indices [0, pos1-1] are shifted right by 1,
            # which decreases posn by 1.
            ops_right = (n - 2 - (posn - 1))  # equivalent to n-1-(posn-1)
        else:
            # pos1 > posn: n is left of 1, its index unchanged by moving 1 to the front
            ops_right = (n - 1 - posn)

        return ops_left + ops_right
```
```

</details>

#### Tier: `fail`

<details>
<summary>fail attempt 1</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # Minimum adjacent swaps to bring 1 to index 0
        pos1 = nums.index(1)
        swaps_left = pos1  # moving left by pos1 swaps

        # Minimum adjacent swaps to bring n to index n-1 after moving 1
        # If 1 is originally to the left of n's position, its movement left shifts n left by 1,
        # otherwise n's index is unchanged.
        posn = nums.index(n)
        if pos1 < posn:
            posn -= 1
        swaps_right = (n - 1) - posn

        return swaps_left + swaps_right
```
```

</details>

### Parsed Memory Items

1. Count Adjacent-Swap Distance, Then Fix Overlap via Crossing
Description: Minimum adjacent swaps to move elements into target positions can be computed by distance, but must be corrected when their movement paths overlap.
<details>
<summary>Content 1</summary>

```text
When using adjacent swaps, moving an element to a target index costs the number of positions it passes. If two elements are both being moved, verify whether one move causes the other to shift or whether they must “cross” during the process; this is the only interaction you need to correct, rather than re-deriving from scratch.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
Successful attempts converged on a robust way to count the minimum adjacent swaps needed to place two special elements into fixed target positions, while carefully accounting for how moving one element shifts the other when their movement intervals overlap. The incorrect/partially correct attempts typically failed by (a) assuming the two repositioning steps are always independent, or (b) updating the other element’s position with an incorrect shift amount/sign, or (c) adding an “overlap penalty” without a validated invariant that ties it to the actual crossing behavior. The key distinction is whether the method explicitly models the interaction as “crossing events” under adjacent swaps, then derives the final count from distances plus the single necessary correction.
```

</details>

2. Choose a Composable Strategy: Fix One Element Then the Other
Description: A correct minimum can often be obtained by fixing one constraint first and then recomputing the second under the resulting state change.
<details>
<summary>Content 2</summary>

```text
A reliable pattern is: (1) move the first special element to its required position using adjacent swaps, (2) update the effective position of the second element due to elements shifting in the affected interval, (3) add the adjacent-swaps needed to bring the second to its target. This prevents “double counting” or missing shifts that independent formulas can cause.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
Successful attempts converged on a robust way to count the minimum adjacent swaps needed to place two special elements into fixed target positions, while carefully accounting for how moving one element shifts the other when their movement intervals overlap. The incorrect/partially correct attempts typically failed by (a) assuming the two repositioning steps are always independent, or (b) updating the other element’s position with an incorrect shift amount/sign, or (c) adding an “overlap penalty” without a validated invariant that ties it to the actual crossing behavior. The key distinction is whether the method explicitly models the interaction as “crossing events” under adjacent swaps, then derives the final count from distances plus the single necessary correction.
```

</details>

3. Validate Index-Update Logic with Interval Reasoning
Description: When one element is moved, the other element’s index changes only if it lies inside the moved segment.
<details>
<summary>Content 3</summary>

```text
For any operation that shifts positions (like moving an element left/right via adjacent swaps), the other element’s index changes by a predictable amount only when it is within the indices crossed. If your update rules depend on ordering, express them as “was the other element inside the swap interval?” rather than guessing the sign/magnitude.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
Successful attempts converged on a robust way to count the minimum adjacent swaps needed to place two special elements into fixed target positions, while carefully accounting for how moving one element shifts the other when their movement intervals overlap. The incorrect/partially correct attempts typically failed by (a) assuming the two repositioning steps are always independent, or (b) updating the other element’s position with an incorrect shift amount/sign, or (c) adding an “overlap penalty” without a validated invariant that ties it to the actual crossing behavior. The key distinction is whether the method explicitly models the interaction as “crossing events” under adjacent swaps, then derives the final count from distances plus the single necessary correction.
```

</details>

4. Beware Unjustified “Overlap Penalties”
Description: If you add a constant or ad-hoc penalty for overlap without proving it matches the actual number of crossings, the result will likely be wrong.
<details>
<summary>Content 4</summary>

```text
Overlap between two adjacent-swap sequences matters only through how many times the two tracked elements cross (or equivalently, how their relative order changes). Before applying a correction term, ground it in a precise invariant (relative order/crossings) or simulate the crossing count on the conceptual interval.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
Successful attempts converged on a robust way to count the minimum adjacent swaps needed to place two special elements into fixed target positions, while carefully accounting for how moving one element shifts the other when their movement intervals overlap. The incorrect/partially correct attempts typically failed by (a) assuming the two repositioning steps are always independent, or (b) updating the other element’s position with an incorrect shift amount/sign, or (c) adding an “overlap penalty” without a validated invariant that ties it to the actual crossing behavior. The key distinction is whether the method explicitly models the interaction as “crossing events” under adjacent swaps, then derives the final count from distances plus the single necessary correction.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
Successful attempts converged on a robust way to count the minimum adjacent swaps needed to place two special elements into fixed target positions, while carefully accounting for how moving one element shifts the other when their movement intervals overlap. The incorrect/partially correct attempts typically failed by (a) assuming the two repositioning steps are always independent, or (b) updating the other element’s position with an incorrect shift amount/sign, or (c) adding an “overlap penalty” without a validated invariant that ties it to the actual crossing behavior. The key distinction is whether the method explicitly models the interaction as “crossing events” under adjacent swaps, then derives the final count from distances plus the single necessary correction.
</reasoning>

<memories>
<memory>
<title>Count Adjacent-Swap Distance, Then Fix Overlap via Crossing</title>
<description>Minimum adjacent swaps to move elements into target positions can be computed by distance, but must be corrected when their movement paths overlap.</description>
<content>When using adjacent swaps, moving an element to a target index costs the number of positions it passes. If two elements are both being moved, verify whether one move causes the other to shift or whether they must “cross” during the process; this is the only interaction you need to correct, rather than re-deriving from scratch.</content>
</memory>

<memory>
<title>Choose a Composable Strategy: Fix One Element Then the Other</title>
<description>A correct minimum can often be obtained by fixing one constraint first and then recomputing the second under the resulting state change.</description>
<content>A reliable pattern is: (1) move the first special element to its required position using adjacent swaps, (2) update the effective position of the second element due to elements shifting in the affected interval, (3) add the adjacent-swaps needed to bring the second to its target. This prevents “double counting” or missing shifts that independent formulas can cause.</content>
</memory>

<memory>
<title>Validate Index-Update Logic with Interval Reasoning</title>
<description>When one element is moved, the other element’s index changes only if it lies inside the moved segment.</description>
<content>For any operation that shifts positions (like moving an element left/right via adjacent swaps), the other element’s index changes by a predictable amount only when it is within the indices crossed. If your update rules depend on ordering, express them as “was the other element inside the swap interval?” rather than guessing the sign/magnitude.</content>
</memory>

<memory>
<title>Beware Unjustified “Overlap Penalties”</title>
<description>If you add a constant or ad-hoc penalty for overlap without proving it matches the actual number of crossings, the result will likely be wrong.</description>
<content>Overlap between two adjacent-swap sequences matters only through how many times the two tracked elements cross (or equivalently, how their relative order changes). Before applying a correction term, ground it in a precise invariant (relative order/crossings) or simulate the crossing count on the conceptual interval.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `0.4000`
- Augmented pass@1: `0.9000`
- Improvement: `+0.5000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
You are given a 0-indexed permutation of n integers nums.
A permutation is called semi-ordered if the first number equals 1 and the last number equals n. You can perform the below operation as many times as you want until you make nums a semi-ordered permutation:

Pick two adjacent elements in nums, then swap them.

Return the minimum number of operations to make nums a semi-ordered permutation.
A permutation is a sequence of integers from 1 to n of length n containing each number exactly once.
 
Example 1:

Input: nums = [2,1,4,3]
Output: 2
Explanation: We can make the permutation semi-ordered using these sequence of operations: 
1 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
2 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than two operations that make nums a semi-ordered permutation. 

Example 2:

Input: nums = [2,4,1,3]
Output: 3
Explanation: We can make the permutation semi-ordered using these sequence of operations:
1 - swap i = 1 and j = 2. The permutation becomes [2,1,4,3].
2 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
3 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than three operations that make nums a semi-ordered permutation.

Example 3:

Input: nums = [1,3,4,2,5]
Output: 0
Explanation: The permutation is already a semi-ordered permutation.

 
Constraints:

2 <= nums.length == n <= 50
1 <= nums[i] <= 50
nums is a permutation.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Find positions of 1 and n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If 1 is left of n, they can be moved inward independently:
        # distance to move 1 to index 0 plus distance to move n to index n-1.
        # Each adjacent swap decreases that distance by exactly 1.
        # Since swaps are within fixed segment ordering, they don't interfere
        # when doing the minimal strategy.
        if pos1 < posn:
            return pos1 + (n - 1 - posn)
        
        # If 1 is to the right of n, moving both to the ends requires them
        # to "cross" each other. The crossing adds 1 extra operation.
        return pos1 + (n - 1 - posn) + 1
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Number of adjacent swaps to bring 1 to index 0:
        # moving element left by pos1 positions
        # Similarly, bring n to index n-1: moving it right by (n-1 - posn)
        swaps1 = pos1
        swapsn = (n - 1) - posn

        # But if the paths cross (1 is to the right of n),
        # the second target position shifts by 1 after moving one element.
        # Specifically, if pos1 > posn then moving 1 left by swaps1
        # effectively shifts n one step right relative to the array indices.
        if pos1 > posn:
            swapsn += 1

        return swaps1 + swapsn
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Locate 1 and n
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If we treat adjacent swaps as "bubble" moves:
        # - Move 1 to index 0: needs pos1 swaps.
        # - Move n to index n-1: needs (n-1 - posn) swaps.
        #
        # But if pos1 > posn, then moving 1 left will shift the position of n
        # by 1 for each swap that occurs before n moves. In that case,
        # total becomes pos1 + (n-1 - posn) + 1? Let's compute precisely.
        #
        # Let i=pos1, j=posn.
        # Final indices must be 0 for 1 and n-1 for n.
        # Using adjacent swaps, the number of swaps equals:
        # (i - 0) + ((n-1) - j) + adjustment if the swaps overlap.
        #
        # When i < j: moving 1 left doesn't affect n's path -> no adjustment.
        # When i > j: moving 1 left crosses over n at some point -> n is shifted
        # by one additional position relative to naive count -> +1 adjustment.
        #
        # Thus: base = i + (n-1-j) + (1 if i > j else 0)
        ans = pos1 + (n - 1 - posn)
        if pos1 > posn:
            ans += 1
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Bring 1 to index 0
        pos1 = nums.index(1)
        ops = pos1
        nums = nums[:]  # not strictly needed, but keeps logic clear
        while pos1 > 0:
            nums[pos1], nums[pos1 - 1] = nums[pos1 - 1], nums[pos1]
            pos1 -= 1

        # Bring n to index n-1 (note: after moving 1, position of n may shift)
        posn = nums.index(n)
        ops += (n - 1 - posn)
        while posn < n - 1:
            nums[posn], nums[posn + 1] = nums[posn + 1], nums[posn]
            posn += 1

        return ops
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] == 1 and nums[-1] == n:
            return 0

        # Positions (0-indexed) of 1 and n
        i1 = nums.index(1)
        in_ = nums.index(n)

        # If we bring 1 to the front by adjacent swaps, it takes i1 swaps.
        # If we bring n to the end by adjacent swaps, it takes (n-1 - in_) swaps.
        # When their movement ranges overlap, swaps can be shared.
        # Let the array indices where 1 moves: [0..i1]
        # and where n moves: [in_..n-1]
        # Overlap exists when in_ < i1 (i.e., n is left of 1).
        # Total minimal swaps becomes sum of distances minus 1 share per crossing block.
        if i1 < in_:
            # 1 is left of n; their paths don't conflict
            return i1 + (n - 1 - in_)
        else:
            # n is left of 1; they cross during sorting
            # One swap can contribute to both movements at the crossing
            return i1 + (n - 1 - in_) - 1
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # Positions of 1 and n in the current permutation
        pos1 = nums.index(1)
        posn = nums.index(n)

        # We need minimal adjacent swaps to move 1 to index 0 and n to index n-1.
        # Swaps are independent except when their paths cross (affects count by 1).
        # This is the standard result for two items moving towards their targets
        # with adjacent swaps.
        left_steps = pos1  # swaps to bring 1 from pos1 -> 0
        right_steps = (n - 1) - posn  # swaps to bring n from posn -> n-1

        # If 1 is to the right of n, or equivalently pos1 > posn,
        # their swap paths cross once; that reduces the total by 1.
        # (We won't double-count the meeting swap.)
        cross = 1 if pos1 > posn else 0

        return left_steps + right_steps - cross
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # positions where each value currently is
        pos = [0] * (n + 1)
        for i, v in enumerate(nums):
            pos[v] = i

        i1 = pos[1]       # current index of 1 (0-based)
        in_ = pos[n]     # current index of n

        # If 1 is to the right of n, they must cross if both are moved to ends,
        # costing one extra swap compared to the non-crossing case.
        if i1 < in_:
            # Move 1 left to index 0: i1 swaps
            # Move n right to index n-1: (n-1 - in_) swaps
            return i1 + (n - 1 - in_)
        else:
            # Move 1 left to index 0: i1 swaps
            # Move n right to index n-1: (n-1 - in_) swaps
            # Crossing adds 1 swap.
            return i1 + (n - 1 - in_) + 1
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        ans = 0
        # Bring 1 to index 0
        if pos1 > 0:
            ans += pos1
        # Bring n to index n-1.
        # After moving 1 to the front, indices shift if 1 was left of n.
        if posn < n - 1:
            # If pos1 < posn, then n's index decreases by pos1 during the swaps of 1 left.
            posn_after = posn - 1 if pos1 < posn else posn
            # However, the number of swaps needed depends on the exact final position.
            # A correct direct formula is:
            # swaps to move n right by (n-1 - final_index_of_n).
            final_index_of_n = posn_after  # after the effect of moving 1 to front
            ans += (n - 1 - final_index_of_n)
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos = [0] * (n + 1)
        for i, v in enumerate(nums):
            pos[v] = i

        # min adjacent swaps to move value x to index target
        def swaps_to_move(x: int, target: int) -> int:
            return abs(pos[x] - target)

        ops_first = swaps_to_move(1, 0)          # bring 1 to index 0
        # After moving 1, its position changes. If  n is fixed, we track overlap cases.
        # Adjacent swaps preserve relative order of other elements except for the shifted window.
        # For minimal moves, we can simulate the effect on the position of n.
        i1 = pos[1]
        in_ = pos[n]
        ops_last = None

        if n == 1:
            ops_last = 0
        else:
            # If moving 1 crosses the position of n, n's index shifts by +/-1 accordingly.
            # When 1 moves from i1 to 0:
            # - if in_ < i1, then all swaps happen to the left of n => n index unchanged
            # - if in_ > i1, then swaps cross over positions up to i1 only => n index unchanged
            # Actually when moving 1 leftwards, it only swaps with elements between target(0) and i1-1,
            # so it does NOT interact with elements right of i1. Thus n index changes only if n is in that interval.
            # n index changes if in_ < i1? Wait: moving left crosses indices [0..i1-1]. If n is in there,
            # its index increases by 1 each time 1 swaps past it (effectively, n shifts right).
            # So:
            if in_ < i1:
                # 1 passes over n, shifting n right by ops_first
                new_in = in_ + ops_first
            else:
                # 1 does not pass over n
                new_in = in_
            ops_last = abs(new_in - (n - 1))

        return ops_first + ops_last
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos = [0] * (n + 1)
        for i, x in enumerate(nums):
            pos[x] = i

        # If 1 is at index p, moving it to index 0 needs p adjacent swaps.
        # If n is at index q, moving it to index n-1 needs (n-1 - q) adjacent swaps.
        #
        # But if the swap operations overlap (i.e., paths cross), we must avoid double counting.
        # The overlap happens exactly when 1 starts to the right of n in the array (pos[1] > pos[n]).
        p, q = pos[1], pos[n]

        ans = p + (n - 1 - q)
        if p > q:
            ans -= 1
        return ans
```
```

</details>

#### Baseline Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.6667 | `partial` |
| 1 | 0.6667 | `partial` |
| 2 | 0.6667 | `partial` |
| 3 | 1.0000 | `full` |
| 4 | 1.0000 | `full` |
| 5 | 1.0000 | `full` |
| 6 | 0.6667 | `partial` |
| 7 | 0.3333 | `partial` |
| 8 | 0.7333 | `partial` |
| 9 | 1.0000 | `full` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 10,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "4",
      "error": "Wrong Answer"
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
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "99",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "51",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 1</summary>

```json
{
  "passed": 10,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "4",
      "error": "Wrong Answer"
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
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "99",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "51",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 2</summary>

```json
{
  "passed": 10,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "4",
      "error": "Wrong Answer"
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
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "99",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "51",
      "error": "Wrong Answer"
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 10,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "4",
      "error": "Wrong Answer"
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
      "passed": false,
      "expected": "3",
      "actual": "5",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "99",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "51",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "passed": 5,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "4",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
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
      "passed": false,
      "expected": "3",
      "actual": "4",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "4",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "4",
      "actual": "5",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "16",
      "actual": "17",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "98",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "50",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 8</summary>

```json
{
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "2",
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
      "expected": "1",
      "actual": "1",
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
      "passed": false,
      "expected": "3",
      "actual": "2",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
      "error": ""
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": false,
      "expected": "97",
      "actual": "49",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "97",
      "error": "Wrong Answer"
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
Before solving, consider these reusable insights from prior analysis:

  1. Count Adjacent-Swap Distance, Then Fix Overlap via Crossing: Minimum adjacent swaps to move elements into target positions can be computed by distance, but must be corrected when their movement paths overlap.
     When using adjacent swaps, moving an element to a target index costs the number of positions it passes. If two elements are both being moved, verify whether one move causes the other to shift or whether they must “cross” during the process; this is the only interaction you need to correct, rather than re-deriving from scratch.
  2. Choose a Composable Strategy: Fix One Element Then the Other: A correct minimum can often be obtained by fixing one constraint first and then recomputing the second under the resulting state change.
     A reliable pattern is: (1) move the first special element to its required position using adjacent swaps, (2) update the effective position of the second element due to elements shifting in the affected interval, (3) add the adjacent-swaps needed to bring the second to its target. This prevents “double counting” or missing shifts that independent formulas can cause.
  3. Validate Index-Update Logic with Interval Reasoning: When one element is moved, the other element’s index changes only if it lies inside the moved segment.
     For any operation that shifts positions (like moving an element left/right via adjacent swaps), the other element’s index changes by a predictable amount only when it is within the indices crossed. If your update rules depend on ordering, express them as “was the other element inside the swap interval?” rather than guessing the sign/magnitude.
  4. Beware Unjustified “Overlap Penalties”: If you add a constant or ad-hoc penalty for overlap without proving it matches the actual number of crossings, the result will likely be wrong.
     Overlap between two adjacent-swap sequences matters only through how many times the two tracked elements cross (or equivalently, how their relative order changes). Before applying a correction term, ground it in a precise invariant (relative order/crossings) or simulate the crossing count on the conceptual interval.

Apply these insights to the problem below.

### Question:
You are given a 0-indexed permutation of n integers nums.
A permutation is called semi-ordered if the first number equals 1 and the last number equals n. You can perform the below operation as many times as you want until you make nums a semi-ordered permutation:

Pick two adjacent elements in nums, then swap them.

Return the minimum number of operations to make nums a semi-ordered permutation.
A permutation is a sequence of integers from 1 to n of length n containing each number exactly once.
 
Example 1:

Input: nums = [2,1,4,3]
Output: 2
Explanation: We can make the permutation semi-ordered using these sequence of operations: 
1 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
2 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than two operations that make nums a semi-ordered permutation. 

Example 2:

Input: nums = [2,4,1,3]
Output: 3
Explanation: We can make the permutation semi-ordered using these sequence of operations:
1 - swap i = 1 and j = 2. The permutation becomes [2,1,4,3].
2 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
3 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than three operations that make nums a semi-ordered permutation.

Example 3:

Input: nums = [1,3,4,2,5]
Output: 0
Explanation: The permutation is already a semi-ordered permutation.

 
Constraints:

2 <= nums.length == n <= 50
1 <= nums[i] <= 50
nums is a permutation.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Move 1 to index 0 via adjacent swaps: costs pos1
        # After moving 1 left, elements originally in [0..pos1-1] shift right by 1,
        # so if n was among them (i.e., posn < pos1), n's position increases by 1.
        swaps1 = pos1
        posn_after = posn + (1 if posn < pos1 else 0)

        # Move n to index n-1 via adjacent swaps: costs (n-1 - posn_after)
        swapsn = (n - 1) - posn_after

        return swaps1 + swapsn
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Case A: 1 is left of n
        # Move 1 left to index 0: pos1 swaps.
        # Then move n right to index n-1. After moving 1, n shifts left by pos1
        # only if n was to the right of 1 (which it is in this case).
        if pos1 < posn:
            # after bringing 1 to front, n's new index becomes posn - pos1
            return pos1 + (n - 1 - (posn - pos1))

        # Case B: 1 is right of n
        # Move n right to index n-1: (n-1 - posn) swaps.
        # Then move 1 left to index 0. After moving n, 1 shifts right by
        # (n-1-posn) only if 1 was left of n (which it is not; it's right of n),
        # but since pos1 > posn, 1 is indeed to the right of the moved segment
        # and will shift right by 0; instead, 1 is within the interval that is
        # affected by moving n? Let's compute by order/crossing:
        #
        # A robust way: adjacent swaps cost equals number of inversions added
        # required to fix relative order of items. The total minimal operations
        # equals distance of 1 to front plus distance of n to back minus the
        # number of times their moves would "overlap" (cross) which is exactly
        # 1 if pos1 > posn (they must cross), else 0.
        #
        # But overlap correction for boundary-fixing ends up being:
        # if pos1 > posn: total = pos1 + (n-1 - posn) - 1
        # if pos1 < posn: total = pos1 + (n-1 - posn)  (no correction)
        total = pos1 + (n - 1 - posn)
        if pos1 > posn:
            return total - 1
        else:
            return total
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If we move 1 to index 0, elements between 0..pos1-1 shift right by 1.
        # If n lies in that shifted interval, its position increases by 1.
        left_needed = pos1  # adjacent swaps to bring 1 from pos1 -> 0

        # After moving 1 left to index 0:
        posn_after = posn + (1 if posn < pos1 else 0)

        # Then move n to index n-1
        right_needed = (n - 1) - posn_after

        return left_needed + right_needed
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If 1 needs to move left, it takes pos1 swaps.
        # If n needs to move right, it takes (n-1 - posn) swaps.
        # If their movements overlap in the sense that 1 must pass over n,
        # then the swap needed for their relative order is counted twice by the sum,
        # so we correct by subtracting 1.
        ans = 0
        if pos1 != 0:
            ans += pos1
        if posn != n - 1:
            ans += (n - 1 - posn)

        # overlap/crossing correction:
        # 1 moves left to index 0; it crosses every element originally in [0, pos1-1].
        # n moves right to index n-1; it crosses every element originally in [posn+1, n-1].
        # The only potential double-count is when 1 needs to cross n:
        # that happens exactly when pos1 > posn (since 1 is to the right of n initially).
        if pos1 > posn:
            ans -= 1

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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Move 1 to index 0 using adjacent swaps.
        # Cost is exactly how many positions it moves left.
        ans = pos1

        # After moving 1 to front, elements between [0..pos1-1] shift right by 1.
        # If n was in that interval, its index increases by 1.
        if posn < pos1:
            posn += 1

        # Now move n to index n-1 (rightmost) using adjacent swaps.
        # Cost is how many positions it moves right.
        ans += (n - 1 - posn)
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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)
        
        # To minimize operations (adjacent swaps):
        # Move 1 to index 0: cost = pos1
        # After that, if n is to the left of 1's original position, its index shifts right by 1.
        cost = pos1
        if posn < pos1:
            posn += 1  # n gets shifted right by 1 due to moving 1 left past it

        # Now move n to index n-1 from its updated position.
        cost += (n - 1 - posn)
        return cost
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # If 1 is after n, moving 1 left and n right can cross; account naturally.
        # Minimum operations to bring element x from index i to target t equals |i - t|,
        # but with adjacent swaps we must consider crossings between the two tracked elements.
        # For two elements, the number of adjacent swaps needed to reach both target indices
        # equals:
        #   |pos1 - 0| + |posn - (n-1)|  - 1  if their relative order flips during the process.
        #
        # The relative order flips iff initially pos1 > posn (1 is to the right of n),
        # because in the final configuration 1 must be before n.
        # Then the two elements must cross exactly once, reducing the naive sum by 1.
        base = abs(pos1 - 0) + abs(posn - (n - 1))
        if pos1 > posn:
            base -= 1
        return base
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Minimum adjacent swaps to place 1 at index 0 and n at index n-1
        # depends on their relative order; after placing one, the other's
        # position shifts only if it lies in the moved interval.
        #
        # Compute both possible orders (move 1 first or move n first) and take min.
        def move_first(first_val: int, first_target: int, other_val: int, other_pos: int) -> int:
            """Move first_val from its current position to first_target using adjacent swaps,
            and compute added cost plus the cost to move other_val to its target after shift."""
            first_pos = nums.index(first_val)

            # Cost to move first to target (adjacent swaps)
            cost1 = abs(first_pos - first_target)

            # After moving first between min..max (inclusive range swept),
            # update other's position if it lies inside that interval.
            l = min(first_pos, first_target)
            r = max(first_pos, first_target)

            other_pos_after = other_pos
            if l <= other_pos <= r:
                # If moving left (first_target < first_pos), elements in [first_target..first_pos-1]
                # shift right by 1, so other's position increases by 1.
                # If moving right, elements in [first_pos+1..first_target] shift left by 1,
                # so other's position decreases by 1.
                if first_target < first_pos:
                    other_pos_after = other_pos + 1
                else:
                    other_pos_after = other_pos - 1

            # Cost to move other to its target
            other_target = n - 1 if other_val == n else 0
            cost2 = abs(other_pos_after - other_target)
            return cost1 + cost2

        ans = 10**9

        # Order A: move 1 to front first, then move n to end
        pos_n = posn
        # If 1 already at front, pos doesn't change; move_first still works.
        ans = min(ans, move_first(1, 0, n, pos_n))

        # Order B: move n to end first, then move 1 to front
        pos_1 = pos1
        ans = min(ans, move_first(n, n - 1, 1, pos_1))

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
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Minimum adjacent swaps to bring 1 to index 0
        # (each swap moves 1 left by 1)
        cost = pos1

        # After moving 1 left across indices [0 .. pos1-1], the element at index n_pos
        # shifts only if n is in that crossed interval.
        if posn < pos1:
            # n is to the left of where 1 starts, so when 1 moves left it doesn't cross n,
            # but indices of elements to the right of the swapped pair change; net effect:
            # n's index increases by 1 for each swap where 1 passes indices <= posn-1,
            # equivalently n index shifts by +1 because 1's path pushes it right when
            # n lies inside the interval [0 .. pos1-1].
            posn += 1
        # If posn > pos1, moving 1 left happens entirely left of n, so n's index is unchanged.
        # If posn == pos1 can't happen since 1 and n are distinct (n>=2).

        # Now we need to move n to index n-1 via adjacent swaps.
        # Since adjacent swaps cost = distance to target, and we only care about n's
        # effective position after the first phase.
        cost += (n - 1 - posn)

        return cost
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)

        # Move 1 to index 0 by adjacent swaps:
        # cost = pos1
        # This shifts elements between [0..pos1] one step right, so n's position changes
        # iff n was inside that interval.
        cost1 = pos1
        new_posn = posn + 1 if posn <= pos1 else posn

        # Now move n to index n-1 (right end) by adjacent swaps:
        # cost = (n-1) - new_posn
        costn = (n - 1) - new_posn

        return cost1 + costn
```
```

</details>

#### Augmented Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 1.0000 | `full` |
| 1 | 0.8000 | `partial` |
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 12,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "3",
      "actual": "3",
      "error": ""
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "2",
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
      "expected": "3",
      "actual": "3",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "4",
      "actual": "5",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "16",
      "actual": "16",
      "error": ""
    },
    {
      "passed": true,
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "97",
      "actual": "97",
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
