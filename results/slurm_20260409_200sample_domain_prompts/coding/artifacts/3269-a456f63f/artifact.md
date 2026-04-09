# Problem 3269

- Domain: `coding`

## Problem

```text
You are given a 0-indexed integer array nums of size n, and a 0-indexed integer array pattern of size m consisting of integers -1, 0, and 1.
A subarray nums[i..j] of size m + 1 is said to match the pattern if the following conditions hold for each element pattern[k]:

nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
nums[i + k + 1] < nums[i + k] if pattern[k] == -1.

Return the count of subarrays in nums that match the pattern.
 
Example 1:

Input: nums = [1,2,3,4,5,6], pattern = [1,1]
Output: 4
Explanation: The pattern [1,1] indicates that we are looking for strictly increasing subarrays of size 3. In the array nums, the subarrays [1,2,3], [2,3,4], [3,4,5], and [4,5,6] match this pattern.
Hence, there are 4 subarrays in nums that match the pattern.

Example 2:

Input: nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]
Output: 2
Explanation: Here, the pattern [1,0,-1] indicates that we are looking for a sequence where the first number is smaller than the second, the second is equal to the third, and the third is greater than the fourth. In the array nums, the subarrays [1,4,4,1], and [3,5,5,3] match this pattern.
Hence, there are 2 subarrays in nums that match the pattern.

 
Constraints:

2 <= n == nums.length <= 100
1 <= nums[i] <= 10^9
1 <= m == pattern.length < n
-1 <= pattern[i] <= 1
```

### Starter Code

```python
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[1, 2, 3, 4, 5, 6]\n[1, 1]",
    "output": "4",
    "testtype": "functional"
  },
  {
    "input": "[1, 4, 4, 1, 3, 5, 5, 3]\n[1, 0, -1]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[81, 50]\n[-1]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[7, 57, 88]\n[-1]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[28, 53, 21]\n[0]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[5, 47, 63, 48]\n[-1, 0]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[46, 60, 80, 98, 90]\n[0, 1]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[9, 83, 77, 75, 39, 32, 68, 60]\n[0]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[73, 26, 7, 20, 30, 48, 97]\n[-1, 1]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[17, 19, 71, 21, 2, 24, 29]\n[0, -1, 0]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[88, 35, 41, 84, 38, 30, 87, 7]\n[0, 1, 0, 1, -1, 1]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[73, 34, 14, 60, 77, 97, 54, 63]\n[-1, 1, 0, -1, -1, 0]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[501399232, 959315981, 630569939, 369992778, 762747706, 678500115, 290334310, 666493456, 207228447, 367090709, 710041308, 135377803, 814213426, 969179920, 869845371, 276379138, 120760857, 852013521, 967284240, 76906837, 464555393, 865016650, 788827506, 750075661, 847293256, 74072686, 273445644, 611123245, 679977255, 717345474, 672117374, 280314168, 18176283, 651591389, 946339492, 884013286, 863214339, 121877045, 936428905, 749504839, 49112178, 961728742, 118501222, 442201631, 950793264, 180831825, 51869751, 502194993, 826181405, 198659336, 587636696, 222864939, 623098844, 210888296, 398223150, 59909422, 352052866, 429669422, 64797567, 780553664, 286945028, 289350308, 607115484, 416826628, 227986024, 665979338, 938728931, 385600482, 799076139, 408699336, 456756072, 482748621, 879865330, 493872639, 393551506, 925116932, 981007406, 454780366, 652424028, 991421291, 166830803, 484315076, 907419950, 875405057, 939199322, 153628762, 967592872, 419748504, 797841033, 533613156, 763571640, 462980381, 865162358, 906034855, 973792201, 150079861, 982936258, 499336540, 384170831, 15599924]\n[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[131844005, 503539488, 895277194, 759135098, 222859496, 417206297, 93592988, 652746849, 668575746, 426968159, 90365765, 524804995, 424162038, 852071046, 595357210, 495180102, 671676834, 876299439, 994737405, 627163327, 244830313, 602073054, 300741633, 718338014, 289606104, 39647787, 321603458, 111918550, 601078319, 225088907, 103288961, 512810211, 257054465, 258736734, 792225867, 940177318, 176181969, 463804773, 936882278, 82890317, 212577344, 883127335, 158830242, 839256780, 413346255, 235128553, 309360347, 183335816, 935094040, 716290736, 242939618, 768597219, 867126752, 588146428, 708144623, 744416831, 646490848, 591132747, 896874946, 708473731, 653644741, 988864797, 684605163, 632823994, 860471013, 156163540, 457954345, 621980039, 553883429, 973856399, 847853262, 301416141, 67641836, 343357596, 428499293, 259578322, 344728849, 561456318, 273243699, 788203584, 350552917, 808682861, 788006599, 961916298, 480628920, 117333757, 572805397, 941296324, 914575507, 789429393, 373909251, 1504179, 335023081, 404799938, 519327858, 749008948, 355046964, 375123262, 858160530, 666369522]\n[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]",
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
You are given a 0-indexed integer array nums of size n, and a 0-indexed integer array pattern of size m consisting of integers -1, 0, and 1.
A subarray nums[i..j] of size m + 1 is said to match the pattern if the following conditions hold for each element pattern[k]:

nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
nums[i + k + 1] < nums[i + k] if pattern[k] == -1.

Return the count of subarrays in nums that match the pattern.
 
Example 1:

Input: nums = [1,2,3,4,5,6], pattern = [1,1]
Output: 4
Explanation: The pattern [1,1] indicates that we are looking for strictly increasing subarrays of size 3. In the array nums, the subarrays [1,2,3], [2,3,4], [3,4,5], and [4,5,6] match this pattern.
Hence, there are 4 subarrays in nums that match the pattern.

Example 2:

Input: nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]
Output: 2
Explanation: Here, the pattern [1,0,-1] indicates that we are looking for a sequence where the first number is smaller than the second, the second is equal to the third, and the third is greater than the fourth. In the array nums, the subarrays [1,4,4,1], and [3,5,5,3] match this pattern.
Hence, there are 2 subarrays in nums that match the pattern.

 
Constraints:

2 <= n == nums.length <= 100
1 <= nums[i] <= 10^9
1 <= m == pattern.length < n
-1 <= pattern[i] <= 1

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        # Compare consecutive elements once: diff_sign[i] describes nums[i] -> nums[i+1]
        diff_sign = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff_sign[i] = 1
            elif nums[i + 1] == nums[i]:
                diff_sign[i] = 0
            else:
                diff_sign[i] = -1

        # A subarray nums[i..i+m] matches iff diff_sign[i..i+m-1] == pattern
        ans = 0
        for i in range(n - m):
            if diff_sign[i:i + m] == pattern:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        cnt = 0
        # start index i for subarray nums[i .. i+m]
        for i in range(n - m):
            ok = True
            for k in range(m):
                a = nums[i + k]
                b = nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                cnt += 1
        return cnt
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        count = 0

        # For subarray nums[i..i+m], compare consecutive pairs
        # nums[i+k+1] vs nums[i+k] must satisfy pattern[k]
        for i in range(n - m):
            ok = True
            for k in range(m):
                a, b = nums[i + k], nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                count += 1

        return count
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        # Build comparison array between consecutive elements:
        # diff[i] describes relation between nums[i] and nums[i+1]
        # diff[i] = 1  if nums[i+1] > nums[i]
        # diff[i] = 0  if nums[i+1] == nums[i]
        # diff[i] = -1 if nums[i+1] < nums[i]
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] < nums[i]:
                diff[i] = -1
            else:
                diff[i] = 0

        # We need diff[i .. i+m-1] to equal pattern[0..m-1]
        ans = 0
        for i in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if diff[i + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        # diff[i] represents relation between nums[i] and nums[i+1]
        # diff[i] = 1 if increasing, 0 if equal, -1 if decreasing
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] < nums[i]:
                diff[i] = -1
            else:
                diff[i] = 0

        # A subarray nums[i..i+m] matches pattern iff diff[i..i+m-1] == pattern
        ans = 0
        for start in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if diff[start + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        # Compare each adjacent pair to determine trend in nums
        # trend[i] describes comparison between nums[i] and nums[i+1]
        trend = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                trend[i] = 1
            elif nums[i + 1] < nums[i]:
                trend[i] = -1
            else:
                trend[i] = 0

        # Count subarrays where the sequence of trends matches pattern
        # pattern length m corresponds to nums subarray length m+1,
        # and therefore to trend segment length m.
        ans = 0
        for start in range(0, (n - 1) - m + 1):
            if trend[start:start + m] == pattern:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        ans = 0

        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                if pattern[k] == 1:
                    if not (nums[i + k + 1] > nums[i + k]):
                        ok = False
                        break
                elif pattern[k] == 0:
                    if not (nums[i + k + 1] == nums[i + k]):
                        ok = False
                        break
                else:  # pattern[k] == -1
                    if not (nums[i + k + 1] < nums[i + k]):
                        ok = False
                        break
            if ok:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        # Convert nums into comparisons between consecutive elements:
        # rel[i] corresponds to nums[i] ? nums[i+1] where i ranges 0..n-2.
        rel = []
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                rel.append(1)
            elif nums[i + 1] == nums[i]:
                rel.append(0)
            else:
                rel.append(-1)

        # Now a subarray nums[i..i+m] matches pattern iff
        # rel[i..i+m-1] == pattern.
        cnt = 0
        for start in range(0, (n - 1) - m + 1):
            if rel[start:start + m] == pattern:
                cnt += 1
        return cnt
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        # We need to compare nums[i+1]..nums[i+m] with nums[i]..nums[i+m-1]
        # For each k in [0..m-1], define relation between consecutive elements.
        # relation = 1 if inc, 0 if equal, -1 if dec.
        if n < m + 1:
            return 0

        rel = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                rel[i] = 1
            elif nums[i + 1] == nums[i]:
                rel[i] = 0
            else:
                rel[i] = -1

        ans = 0
        # We need rel[i + k] == pattern[k] for k in [0..m-1]
        # Subarrays start at i, length m+1, so rel window length is m.
        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                if rel[i + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        # diff[i] represents comparison between nums[i] and nums[i+1]
        # diff[i] = 1 if nums[i+1] > nums[i], 0 if equal, -1 if smaller
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] == nums[i]:
                diff[i] = 0
            else:
                diff[i] = -1

        ans = 0
        # Need m diffs to match pattern -> start at diff index i corresponds to nums[i..i+m]
        for i in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if diff[i + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        # Compare consecutive elements once: diff_sign[i] describes nums[i] -> nums[i+1]
        diff_sign = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff_sign[i] = 1
            elif nums[i + 1] == nums[i]:
                diff_sign[i] = 0
            else:
                diff_sign[i] = -1

        # A subarray nums[i..i+m] matches iff diff_sign[i..i+m-1] == pattern
        ans = 0
        for i in range(n - m):
            if diff_sign[i:i + m] == pattern:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        cnt = 0
        # start index i for subarray nums[i .. i+m]
        for i in range(n - m):
            ok = True
            for k in range(m):
                a = nums[i + k]
                b = nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                cnt += 1
        return cnt
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        count = 0

        # For subarray nums[i..i+m], compare consecutive pairs
        # nums[i+k+1] vs nums[i+k] must satisfy pattern[k]
        for i in range(n - m):
            ok = True
            for k in range(m):
                a, b = nums[i + k], nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                count += 1

        return count
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        # Build comparison array between consecutive elements:
        # diff[i] describes relation between nums[i] and nums[i+1]
        # diff[i] = 1  if nums[i+1] > nums[i]
        # diff[i] = 0  if nums[i+1] == nums[i]
        # diff[i] = -1 if nums[i+1] < nums[i]
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] < nums[i]:
                diff[i] = -1
            else:
                diff[i] = 0

        # We need diff[i .. i+m-1] to equal pattern[0..m-1]
        ans = 0
        for i in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if diff[i + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        # diff[i] represents relation between nums[i] and nums[i+1]
        # diff[i] = 1 if increasing, 0 if equal, -1 if decreasing
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] < nums[i]:
                diff[i] = -1
            else:
                diff[i] = 0

        # A subarray nums[i..i+m] matches pattern iff diff[i..i+m-1] == pattern
        ans = 0
        for start in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if diff[start + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        # Compare each adjacent pair to determine trend in nums
        # trend[i] describes comparison between nums[i] and nums[i+1]
        trend = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                trend[i] = 1
            elif nums[i + 1] < nums[i]:
                trend[i] = -1
            else:
                trend[i] = 0

        # Count subarrays where the sequence of trends matches pattern
        # pattern length m corresponds to nums subarray length m+1,
        # and therefore to trend segment length m.
        ans = 0
        for start in range(0, (n - 1) - m + 1):
            if trend[start:start + m] == pattern:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        ans = 0

        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                if pattern[k] == 1:
                    if not (nums[i + k + 1] > nums[i + k]):
                        ok = False
                        break
                elif pattern[k] == 0:
                    if not (nums[i + k + 1] == nums[i + k]):
                        ok = False
                        break
                else:  # pattern[k] == -1
                    if not (nums[i + k + 1] < nums[i + k]):
                        ok = False
                        break
            if ok:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        # Convert nums into comparisons between consecutive elements:
        # rel[i] corresponds to nums[i] ? nums[i+1] where i ranges 0..n-2.
        rel = []
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                rel.append(1)
            elif nums[i + 1] == nums[i]:
                rel.append(0)
            else:
                rel.append(-1)

        # Now a subarray nums[i..i+m] matches pattern iff
        # rel[i..i+m-1] == pattern.
        cnt = 0
        for start in range(0, (n - 1) - m + 1):
            if rel[start:start + m] == pattern:
                cnt += 1
        return cnt
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        # We need to compare nums[i+1]..nums[i+m] with nums[i]..nums[i+m-1]
        # For each k in [0..m-1], define relation between consecutive elements.
        # relation = 1 if inc, 0 if equal, -1 if dec.
        if n < m + 1:
            return 0

        rel = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                rel[i] = 1
            elif nums[i + 1] == nums[i]:
                rel[i] = 0
            else:
                rel[i] = -1

        ans = 0
        # We need rel[i + k] == pattern[k] for k in [0..m-1]
        # Subarrays start at i, length m+1, so rel window length is m.
        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                if rel[i + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
        return ans
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        # diff[i] represents comparison between nums[i] and nums[i+1]
        # diff[i] = 1 if nums[i+1] > nums[i], 0 if equal, -1 if smaller
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] == nums[i]:
                diff[i] = 0
            else:
                diff[i] = -1

        ans = 0
        # Need m diffs to match pattern -> start at diff index i corresponds to nums[i..i+m]
        for i in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if diff[i + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
        return ans
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
You are given a 0-indexed integer array nums of size n, and a 0-indexed integer array pattern of size m consisting of integers -1, 0, and 1.
A subarray nums[i..j] of size m + 1 is said to match the pattern if the following conditions hold for each element pattern[k]:

nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
nums[i + k + 1] < nums[i + k] if pattern[k] == -1.

Return the count of subarrays in nums that match the pattern.
 
Example 1:

Input: nums = [1,2,3,4,5,6], pattern = [1,1]
Output: 4
Explanation: The pattern [1,1] indicates that we are looking for strictly increasing subarrays of size 3. In the array nums, the subarrays [1,2,3], [2,3,4], [3,4,5], and [4,5,6] match this pattern.
Hence, there are 4 subarrays in nums that match the pattern.

Example 2:

Input: nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]
Output: 2
Explanation: Here, the pattern [1,0,-1] indicates that we are looking for a sequence where the first number is smaller than the second, the second is equal to the third, and the third is greater than the fourth. In the array nums, the subarrays [1,4,4,1], and [3,5,5,3] match this pattern.
Hence, there are 2 subarrays in nums that match the pattern.

 
Constraints:

2 <= n == nums.length <= 100
1 <= nums[i] <= 10^9
1 <= m == pattern.length < n
-1 <= pattern[i] <= 1

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        ans = 0

        # For a subarray nums[i..i+m], we compare consecutive pairs nums[i+k] and nums[i+k+1]
        # to pattern[k].
        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                a, b = nums[i + k], nums[i + k + 1]
                if pattern[k] == 1:
                    if not (b > a):
                        ok = False
                        break
                elif pattern[k] == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # pattern[k] == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        if m + 1 > n:
            return 0

        # diff[i] describes relation between nums[i] and nums[i+1]
        # diff[i] in {-1, 0, 1}
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] < nums[i]:
                diff[i] = -1
            else:
                diff[i] = 0

        # Count windows of length m in diff that equal pattern
        ans = 0
        for start in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if diff[start + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        # Convert nums into comparisons between consecutive elements
        # cmp[i] corresponds to relationship between nums[i] and nums[i+1]
        # cmp[i] in {-1,0,1}
        cmp = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                cmp[i] = 1
            elif nums[i + 1] < nums[i]:
                cmp[i] = -1
            else:
                cmp[i] = 0

        # Subarray nums[i..i+m] matches pattern iff
        # cmp[i..i+m-1] equals pattern[0..m-1]
        ans = 0
        for i in range(n - m):
            ok = True
            for k in range(m):
                if cmp[i + k] != pattern[k]:
                    ok = False
                    break
            if ok:
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        ans = 0

        # Check each subarray of length m+1 starting at i
        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                a = nums[i + k]
                b = nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

        return ans
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        ans = 0

        # Check each subarray nums[i .. i+m]
        for i in range(n - m):
            ok = True
            for k in range(m):
                a = nums[i + k]
                b = nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)

        # Convert nums adjacent comparisons into -1/0/1
        diffs = []
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diffs.append(1)
            elif nums[i + 1] == nums[i]:
                diffs.append(0)
            else:
                diffs.append(-1)

        # Count matches of pattern in diffs; subarray length m+1 corresponds to m diffs
        ans = 0
        for start in range(0, len(diffs) - m + 1):
            ok = True
            for k in range(m):
                if diffs[start + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)

        # Build comparison array between adjacent elements:
        # diff[i] corresponds to nums[i] -> nums[i+1]
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] < nums[i]:
                diff[i] = -1
            # else diff[i] stays 0

        ans = 0
        target_len = m  # because we need m comparisons for a subarray of size m+1

        for start in range(n - (m + 1) + 1):
            # subarray nums[start .. start+m] => comparisons diff[start .. start+m-1]
            if diff[start:start + target_len] == pattern:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        # Build comparison array cmp where cmp[i] represents relation between nums[i] and nums[i+1]
        # cmp[i] = 1  if nums[i+1] > nums[i]
        #          0  if nums[i+1] == nums[i]
        #         -1  if nums[i+1] < nums[i]
        cmp = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                cmp[i] = 1
            elif nums[i + 1] < nums[i]:
                cmp[i] = -1
            # else remains 0

        # Match pattern against cmp using a direct sliding window (n <= 100, so O(n*m) is fine)
        ans = 0
        for start in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if cmp[start + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        # Need subarrays of length m+1 => starting indices i in [0 .. n-(m+1)]
        limit = n - (m + 1)
        ans = 0

        for i in range(limit + 1):
            ok = True
            for k, p in enumerate(pattern):
                a = nums[i + k]
                b = nums[i + k + 1]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        ans = 0

        # For a subarray nums[i..i+m], compare nums[i+k] -> nums[i+k+1] for k=0..m-1
        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                a = nums[i + k]
                b = nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        ans = 0

        # For a subarray nums[i..i+m], we compare consecutive pairs nums[i+k] and nums[i+k+1]
        # to pattern[k].
        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                a, b = nums[i + k], nums[i + k + 1]
                if pattern[k] == 1:
                    if not (b > a):
                        ok = False
                        break
                elif pattern[k] == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # pattern[k] == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        if m + 1 > n:
            return 0

        # diff[i] describes relation between nums[i] and nums[i+1]
        # diff[i] in {-1, 0, 1}
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] < nums[i]:
                diff[i] = -1
            else:
                diff[i] = 0

        # Count windows of length m in diff that equal pattern
        ans = 0
        for start in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if diff[start + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        # Convert nums into comparisons between consecutive elements
        # cmp[i] corresponds to relationship between nums[i] and nums[i+1]
        # cmp[i] in {-1,0,1}
        cmp = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                cmp[i] = 1
            elif nums[i + 1] < nums[i]:
                cmp[i] = -1
            else:
                cmp[i] = 0

        # Subarray nums[i..i+m] matches pattern iff
        # cmp[i..i+m-1] equals pattern[0..m-1]
        ans = 0
        for i in range(n - m):
            ok = True
            for k in range(m):
                if cmp[i + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        ans = 0

        # Check each subarray of length m+1 starting at i
        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                a = nums[i + k]
                b = nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        ans = 0

        # Check each subarray nums[i .. i+m]
        for i in range(n - m):
            ok = True
            for k in range(m):
                a = nums[i + k]
                b = nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)

        # Convert nums adjacent comparisons into -1/0/1
        diffs = []
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diffs.append(1)
            elif nums[i + 1] == nums[i]:
                diffs.append(0)
            else:
                diffs.append(-1)

        # Count matches of pattern in diffs; subarray length m+1 corresponds to m diffs
        ans = 0
        for start in range(0, len(diffs) - m + 1):
            ok = True
            for k in range(m):
                if diffs[start + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)

        # Build comparison array between adjacent elements:
        # diff[i] corresponds to nums[i] -> nums[i+1]
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] < nums[i]:
                diff[i] = -1
            # else diff[i] stays 0

        ans = 0
        target_len = m  # because we need m comparisons for a subarray of size m+1

        for start in range(n - (m + 1) + 1):
            # subarray nums[start .. start+m] => comparisons diff[start .. start+m-1]
            if diff[start:start + target_len] == pattern:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        # Build comparison array cmp where cmp[i] represents relation between nums[i] and nums[i+1]
        # cmp[i] = 1  if nums[i+1] > nums[i]
        #          0  if nums[i+1] == nums[i]
        #         -1  if nums[i+1] < nums[i]
        cmp = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                cmp[i] = 1
            elif nums[i + 1] < nums[i]:
                cmp[i] = -1
            # else remains 0

        # Match pattern against cmp using a direct sliding window (n <= 100, so O(n*m) is fine)
        ans = 0
        for start in range(0, (n - 1) - m + 1):
            ok = True
            for k in range(m):
                if cmp[start + k] != pattern[k]:
                    ok = False
                    break
            if ok:
                ans += 1
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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        # Need subarrays of length m+1 => starting indices i in [0 .. n-(m+1)]
        limit = n - (m + 1)
        ans = 0

        for i in range(limit + 1):
            ok = True
            for k, p in enumerate(pattern):
                a = nums[i + k]
                b = nums[i + k + 1]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        ans = 0

        # For a subarray nums[i..i+m], compare nums[i+k] -> nums[i+k+1] for k=0..m-1
        for i in range(n - (m + 1) + 1):
            ok = True
            for k in range(m):
                a = nums[i + k]
                b = nums[i + k + 1]
                p = pattern[k]
                if p == 1:
                    if not (b > a):
                        ok = False
                        break
                elif p == 0:
                    if not (b == a):
                        ok = False
                        break
                else:  # p == -1
                    if not (b < a):
                        ok = False
                        break
            if ok:
                ans += 1

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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
      "expected": "4",
      "actual": "4",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
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
