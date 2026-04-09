# Problem 2786

- Domain: `coding`

## Problem

```text
You are given a 0-indexed string s that consists of digits from 0 to 9.
A string t is called a semi-repetitive if there is at most one consecutive pair of the same digits inside t. For example, 0010, 002020, 0123, 2002, and 54944 are semi-repetitive while 00101022, and 1101234883 are not.
Return the length of the longest semi-repetitive substring inside s.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "52233"
Output: 4
Explanation: The longest semi-repetitive substring is "5223", which starts at i = 0 and ends at j = 3. 

Example 2:

Input: s = "5494"
Output: 4
Explanation: s is a semi-reptitive string, so the answer is 4.

Example 3:

Input: s = "1111111"
Output: 2
Explanation: The longest semi-repetitive substring is "11", which starts at i = 0 and ends at j = 1.

 
Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '9'
```

### Starter Code

```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
```

### Test Cases

```json
[
  {
    "input": "\"52233\"",
    "output": "4",
    "testtype": "functional"
  },
  {
    "input": "\"5494\"",
    "output": "4",
    "testtype": "functional"
  },
  {
    "input": "\"1111111\"",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "\"4\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"1\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"9\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"0\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"6\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"5\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"7\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"97\"",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "\"32\"",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "\"58957479549437162345618928832412218355982224525842\"",
    "output": "32",
    "testtype": "functional"
  },
  {
    "input": "\"19431832444439006895006189596466887181869887222990\"",
    "output": "16",
    "testtype": "functional"
  },
  {
    "input": "\"44934647782254142104037419772854740202657048962190\"",
    "output": "39",
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
You are given a 0-indexed string s that consists of digits from 0 to 9.
A string t is called a semi-repetitive if there is at most one consecutive pair of the same digits inside t. For example, 0010, 002020, 0123, 2002, and 54944 are semi-repetitive while 00101022, and 1101234883 are not.
Return the length of the longest semi-repetitive substring inside s.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "52233"
Output: 4
Explanation: The longest semi-repetitive substring is "5223", which starts at i = 0 and ends at j = 3. 

Example 2:

Input: s = "5494"
Output: 4
Explanation: s is a semi-reptitive string, so the answer is 4.

Example 3:

Input: s = "1111111"
Output: 2
Explanation: The longest semi-repetitive substring is "11", which starts at i = 0 and ends at j = 1.

 
Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '9'

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # At most one place where s[i] == s[i-1] occurs inside the substring
        bad_pairs = 0
        left = 0
        ans = 1

        for right in range(1, n):
            if s[right] == s[right - 1]:
                bad_pairs += 1

            while bad_pairs > 1:
                if left + 1 <= right and s[left + 1] == s[left]:
                    bad_pairs -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n
        
        left = 0
        pairs = 0  # number of indices i where s[i] == s[i+1] within current window

        best = 1
        for right in range(n):
            # If adding s[right] creates a new equal adjacent pair at (right-1, right)
            if right - 1 >= left and s[right] == s[right - 1]:
                pairs += 1

            # Shrink until window has at most one adjacent equal pair
            while pairs > 1:
                # If removing s[left] affects the adjacent pair at (left, left+1),
                # update pairs accordingly.
                if left + 1 <= right and s[left] == s[left + 1]:
                    pairs -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        ans = 1
        l = 0
        # count of "bad" adjacent pairs (i-1 == i) inside current window
        bad = 0

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad += 1

            # Keep at most one consecutive pair of same digits
            while bad > 1:
                # when moving l forward, check if the removed boundary was bad
                if l + 1 <= r and s[l + 1] == s[l]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # Count how many "bad" adjacent equal pairs exist inside current window.
        # Semi-repetitive => at most one such pair.
        left = 0
        bad = 0
        ans = 1

        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                bad += 1

            while bad > 1:
                # If the removed char was part of an equal adjacent pair, update bad.
                if left + 1 <= right and s[left + 1] == s[left]:
                    bad -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        l = 0
        bad_used = False  # whether we've already used the one allowed "aa" pair

        for r in range(1, n):
            if s[r] == s[r - 1]:
                if not bad_used:
                    bad_used = True
                else:
                    # We have a second consecutive equal pair: move l to remove the earliest pair
                    # l should advance until just after the previous equal pair start.
                    # The previous equal pair is at (r-1, r), and the first allowed pair must be the one ending at r-1.
                    # Move l to r-1 to ensure only one equal pair remains (at r-1, r).
                    l = r - 1

            # Update answer if current window [l..r] is valid (it always is with above logic)
            ans = max(ans, r - l + 1)

            # If current window starts after the first "aa" pair, we might no longer have it;
            # but with the logic above, ans correctness holds without extra bookkeeping.

        return ans
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # We maintain a sliding window [l..r] such that
        # inside it there is at most one index i with s[i] == s[i+1] (a "double").
        l = 0
        doubles = 0
        best = 1

        for r in range(1, n):
            # If the new pair (r-1, r) is a double, count it
            if s[r - 1] == s[r]:
                doubles += 1

            # Shrink until at most one double remains
            while doubles > 1:
                # If the removed boundary pair (l, l+1) was a double, decrement
                if l + 1 < n and s[l] == s[l + 1]:
                    doubles -= 1
                l += 1

            best = max(best, r - l + 1)

        return best
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        l = 0
        
        # countBad: number of indices i in current window such that s[i] == s[i-1]
        # (these are "bad consecutive pairs"; semi-repetitive allows at most one)
        countBad = 0
        
        for r in range(1, n):
            if s[r] == s[r - 1]:
                countBad += 1

            # shrink until the window becomes semi-repetitive
            while countBad > 1:
                if l + 1 <= n - 1 and s[l + 1] == s[l]:
                    countBad -= 1
                l += 1

            ans = max(ans, r - l + 1)
        
        return ans
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # sliding window [l..r] that contains at most one "bad" adjacent equal pair
        l = 0
        bad = 0  # number of indices i in [l..r-1] where s[i] == s[i+1]
        ans = 1

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad += 1

            # shrink until window has at most one bad pair
            while bad > 1:
                if l + 1 <= r - 0 and s[l] == s[l + 1]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # Count consecutive equal digit pairs in current window
        # A window is semi-repetitive if it contains at most one such pair.
        def is_pair(i):
            return s[i] == s[i + 1]

        left = 0
        pairs = 0  # number of consecutive equal pairs within [left, right]

        ans = 1
        for right in range(n):
            # When extending to right, we may add a new pair ending at right (i.e., right-1, right)
            if right - 1 >= 0 and is_pair(right - 1):
                pairs += 1

            # If more than one pair, move left until valid
            while pairs > 1:
                if left + 1 < n and is_pair(left):
                    pairs -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # Sliding window [L..R] with at most one "bad" consecutive pair
        # where s[i] == s[i-1] counts as a violation beyond the first.
        L = 0
        bad = 0
        ans = 1

        for R in range(1, n):
            if s[R] == s[R - 1]:
                bad += 1

            # Maintain at most one consecutive equal pair in the window
            while bad > 1:
                if L + 1 <= R and s[L + 1] == s[L]:
                    bad -= 1
                L += 1

            ans = max(ans, R - L + 1)

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
| 4 | 0.8667 | `partial` |
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
  "passed": 13,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
      "error": ""
    },
    {
      "passed": false,
      "expected": "16",
      "actual": "11",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "39",
      "actual": "24",
      "error": "Wrong Answer"
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
You are given a 0-indexed string s that consists of digits from 0 to 9.
A string t is called a semi-repetitive if there is at most one consecutive pair of the same digits inside t. For example, 0010, 002020, 0123, 2002, and 54944 are semi-repetitive while 00101022, and 1101234883 are not.
Return the length of the longest semi-repetitive substring inside s.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "52233"
Output: 4
Explanation: The longest semi-repetitive substring is "5223", which starts at i = 0 and ends at j = 3. 

Example 2:

Input: s = "5494"
Output: 4
Explanation: s is a semi-reptitive string, so the answer is 4.

Example 3:

Input: s = "1111111"
Output: 2
Explanation: The longest semi-repetitive substring is "11", which starts at i = 0 and ends at j = 1.

 
Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '9'

### Solutions
#### Correct
Attempt 1
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # At most one place where s[i] == s[i-1] occurs inside the substring
        bad_pairs = 0
        left = 0
        ans = 1

        for right in range(1, n):
            if s[right] == s[right - 1]:
                bad_pairs += 1

            while bad_pairs > 1:
                if left + 1 <= right and s[left + 1] == s[left]:
                    bad_pairs -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

Attempt 2
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n
        
        left = 0
        pairs = 0  # number of indices i where s[i] == s[i+1] within current window

        best = 1
        for right in range(n):
            # If adding s[right] creates a new equal adjacent pair at (right-1, right)
            if right - 1 >= left and s[right] == s[right - 1]:
                pairs += 1

            # Shrink until window has at most one adjacent equal pair
            while pairs > 1:
                # If removing s[left] affects the adjacent pair at (left, left+1),
                # update pairs accordingly.
                if left + 1 <= right and s[left] == s[left + 1]:
                    pairs -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
```

Attempt 3
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        ans = 1
        l = 0
        # count of "bad" adjacent pairs (i-1 == i) inside current window
        bad = 0

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad += 1

            # Keep at most one consecutive pair of same digits
            while bad > 1:
                # when moving l forward, check if the removed boundary was bad
                if l + 1 <= r and s[l + 1] == s[l]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```

Attempt 4
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # Count how many "bad" adjacent equal pairs exist inside current window.
        # Semi-repetitive => at most one such pair.
        left = 0
        bad = 0
        ans = 1

        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                bad += 1

            while bad > 1:
                # If the removed char was part of an equal adjacent pair, update bad.
                if left + 1 <= right and s[left + 1] == s[left]:
                    bad -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

Attempt 5
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # We maintain a sliding window [l..r] such that
        # inside it there is at most one index i with s[i] == s[i+1] (a "double").
        l = 0
        doubles = 0
        best = 1

        for r in range(1, n):
            # If the new pair (r-1, r) is a double, count it
            if s[r - 1] == s[r]:
                doubles += 1

            # Shrink until at most one double remains
            while doubles > 1:
                # If the removed boundary pair (l, l+1) was a double, decrement
                if l + 1 < n and s[l] == s[l + 1]:
                    doubles -= 1
                l += 1

            best = max(best, r - l + 1)

        return best
```

Attempt 6
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        l = 0
        
        # countBad: number of indices i in current window such that s[i] == s[i-1]
        # (these are "bad consecutive pairs"; semi-repetitive allows at most one)
        countBad = 0
        
        for r in range(1, n):
            if s[r] == s[r - 1]:
                countBad += 1

            # shrink until the window becomes semi-repetitive
            while countBad > 1:
                if l + 1 <= n - 1 and s[l + 1] == s[l]:
                    countBad -= 1
                l += 1

            ans = max(ans, r - l + 1)
        
        return ans
```

Attempt 7
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # sliding window [l..r] that contains at most one "bad" adjacent equal pair
        l = 0
        bad = 0  # number of indices i in [l..r-1] where s[i] == s[i+1]
        ans = 1

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad += 1

            # shrink until window has at most one bad pair
            while bad > 1:
                if l + 1 <= r - 0 and s[l] == s[l + 1]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```

Attempt 8
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # Count consecutive equal digit pairs in current window
        # A window is semi-repetitive if it contains at most one such pair.
        def is_pair(i):
            return s[i] == s[i + 1]

        left = 0
        pairs = 0  # number of consecutive equal pairs within [left, right]

        ans = 1
        for right in range(n):
            # When extending to right, we may add a new pair ending at right (i.e., right-1, right)
            if right - 1 >= 0 and is_pair(right - 1):
                pairs += 1

            # If more than one pair, move left until valid
            while pairs > 1:
                if left + 1 < n and is_pair(left):
                    pairs -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

Attempt 9
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # Sliding window [L..R] with at most one "bad" consecutive pair
        # where s[i] == s[i-1] counts as a violation beyond the first.
        L = 0
        bad = 0
        ans = 1

        for R in range(1, n):
            if s[R] == s[R - 1]:
                bad += 1

            # Maintain at most one consecutive equal pair in the window
            while bad > 1:
                if L + 1 <= R and s[L + 1] == s[L]:
                    bad -= 1
                L += 1

            ans = max(ans, R - L + 1)

        return ans
```

#### Partially Correct
Attempt 1
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        l = 0
        bad_used = False  # whether we've already used the one allowed "aa" pair

        for r in range(1, n):
            if s[r] == s[r - 1]:
                if not bad_used:
                    bad_used = True
                else:
                    # We have a second consecutive equal pair: move l to remove the earliest pair
                    # l should advance until just after the previous equal pair start.
                    # The previous equal pair is at (r-1, r), and the first allowed pair must be the one ending at r-1.
                    # Move l to r-1 to ensure only one equal pair remains (at r-1, r).
                    l = r - 1

            # Update answer if current window [l..r] is valid (it always is with above logic)
            ans = max(ans, r - l + 1)

            # If current window starts after the first "aa" pair, we might no longer have it;
            # but with the logic above, ans correctness holds without extra bookkeeping.

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
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # At most one place where s[i] == s[i-1] occurs inside the substring
        bad_pairs = 0
        left = 0
        ans = 1

        for right in range(1, n):
            if s[right] == s[right - 1]:
                bad_pairs += 1

            while bad_pairs > 1:
                if left + 1 <= right and s[left + 1] == s[left]:
                    bad_pairs -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n
        
        left = 0
        pairs = 0  # number of indices i where s[i] == s[i+1] within current window

        best = 1
        for right in range(n):
            # If adding s[right] creates a new equal adjacent pair at (right-1, right)
            if right - 1 >= left and s[right] == s[right - 1]:
                pairs += 1

            # Shrink until window has at most one adjacent equal pair
            while pairs > 1:
                # If removing s[left] affects the adjacent pair at (left, left+1),
                # update pairs accordingly.
                if left + 1 <= right and s[left] == s[left + 1]:
                    pairs -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        ans = 1
        l = 0
        # count of "bad" adjacent pairs (i-1 == i) inside current window
        bad = 0

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad += 1

            # Keep at most one consecutive pair of same digits
            while bad > 1:
                # when moving l forward, check if the removed boundary was bad
                if l + 1 <= r and s[l + 1] == s[l]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # Count how many "bad" adjacent equal pairs exist inside current window.
        # Semi-repetitive => at most one such pair.
        left = 0
        bad = 0
        ans = 1

        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                bad += 1

            while bad > 1:
                # If the removed char was part of an equal adjacent pair, update bad.
                if left + 1 <= right and s[left + 1] == s[left]:
                    bad -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # We maintain a sliding window [l..r] such that
        # inside it there is at most one index i with s[i] == s[i+1] (a "double").
        l = 0
        doubles = 0
        best = 1

        for r in range(1, n):
            # If the new pair (r-1, r) is a double, count it
            if s[r - 1] == s[r]:
                doubles += 1

            # Shrink until at most one double remains
            while doubles > 1:
                # If the removed boundary pair (l, l+1) was a double, decrement
                if l + 1 < n and s[l] == s[l + 1]:
                    doubles -= 1
                l += 1

            best = max(best, r - l + 1)

        return best
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        l = 0
        
        # countBad: number of indices i in current window such that s[i] == s[i-1]
        # (these are "bad consecutive pairs"; semi-repetitive allows at most one)
        countBad = 0
        
        for r in range(1, n):
            if s[r] == s[r - 1]:
                countBad += 1

            # shrink until the window becomes semi-repetitive
            while countBad > 1:
                if l + 1 <= n - 1 and s[l + 1] == s[l]:
                    countBad -= 1
                l += 1

            ans = max(ans, r - l + 1)
        
        return ans
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # sliding window [l..r] that contains at most one "bad" adjacent equal pair
        l = 0
        bad = 0  # number of indices i in [l..r-1] where s[i] == s[i+1]
        ans = 1

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad += 1

            # shrink until window has at most one bad pair
            while bad > 1:
                if l + 1 <= r - 0 and s[l] == s[l + 1]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # Count consecutive equal digit pairs in current window
        # A window is semi-repetitive if it contains at most one such pair.
        def is_pair(i):
            return s[i] == s[i + 1]

        left = 0
        pairs = 0  # number of consecutive equal pairs within [left, right]

        ans = 1
        for right in range(n):
            # When extending to right, we may add a new pair ending at right (i.e., right-1, right)
            if right - 1 >= 0 and is_pair(right - 1):
                pairs += 1

            # If more than one pair, move left until valid
            while pairs > 1:
                if left + 1 < n and is_pair(left):
                    pairs -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # Sliding window [L..R] with at most one "bad" consecutive pair
        # where s[i] == s[i-1] counts as a violation beyond the first.
        L = 0
        bad = 0
        ans = 1

        for R in range(1, n):
            if s[R] == s[R - 1]:
                bad += 1

            # Maintain at most one consecutive equal pair in the window
            while bad > 1:
                if L + 1 <= R and s[L + 1] == s[L]:
                    bad -= 1
                L += 1

            ans = max(ans, R - L + 1)

        return ans
```
```

</details>

#### Tier: `partial`

<details>
<summary>partial attempt 1</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        l = 0
        bad_used = False  # whether we've already used the one allowed "aa" pair

        for r in range(1, n):
            if s[r] == s[r - 1]:
                if not bad_used:
                    bad_used = True
                else:
                    # We have a second consecutive equal pair: move l to remove the earliest pair
                    # l should advance until just after the previous equal pair start.
                    # The previous equal pair is at (r-1, r), and the first allowed pair must be the one ending at r-1.
                    # Move l to r-1 to ensure only one equal pair remains (at r-1, r).
                    l = r - 1

            # Update answer if current window [l..r] is valid (it always is with above logic)
            ans = max(ans, r - l + 1)

            # If current window starts after the first "aa" pair, we might no longer have it;
            # but with the logic above, ans correctness holds without extra bookkeeping.

        return ans
```
```

</details>

### Parsed Memory Items

1. Constraint-Driven Sliding Window Invariant
Description: Convert “at most one consecutive equal pair” into an explicit, countable window invariant.
<details>
<summary>Content 1</summary>

```text
Represent the constraint using a simple metric (e.g., the number of adjacent-equal “bad pairs” inside the current window). Maintain an invariant like “bad_pairs ≤ 1” at every step, so the window is always valid while you search for the maximum length.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
Successful attempts consistently used a correct sliding-window invariant: the current substring/window always contains at most a fixed number (one) of “violations” defined via adjacent equal pairs. They maintained this invariant with a monotone two-pointer approach by incrementing a violation counter when the window expands and decrementing it appropriately as the left boundary moves. Partially correct attempts tried to special-case the “second violation” without fully maintaining the general invariant through pointer movement, which can break when the window contains overlapping/shifted adjacency patterns. Several failed/partial approaches also show the risk of incorrect boundary updates—confusing which adjacent pair gets removed or relying on assumptions about where the remaining “allowed” pair must be located.
```

</details>

2. Two-Pointer with Violation Counter
Description: Update a violation counter when the right pointer expands, and shrink with the same counter when it exceeds the limit.
<details>
<summary>Content 2</summary>

```text
When extending the window by one character, only a small local change can affect validity (typically the new boundary adjacency). While the counter exceeds the allowed maximum, move the left pointer forward and decrement the counter only if the removed boundary adjacency was part of a violation.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
Successful attempts consistently used a correct sliding-window invariant: the current substring/window always contains at most a fixed number (one) of “violations” defined via adjacent equal pairs. They maintained this invariant with a monotone two-pointer approach by incrementing a violation counter when the window expands and decrementing it appropriately as the left boundary moves. Partially correct attempts tried to special-case the “second violation” without fully maintaining the general invariant through pointer movement, which can break when the window contains overlapping/shifted adjacency patterns. Several failed/partial approaches also show the risk of incorrect boundary updates—confusing which adjacent pair gets removed or relying on assumptions about where the remaining “allowed” pair must be located.
```

</details>

3. Boundary-Removal Accounting
Description: When shrinking a window, recompute the effect only for adjacencies that actually change at the boundary.
<details>
<summary>Content 3</summary>

```text
As the left boundary moves, the only adjacent-equal pair status that can change is the one involving the new left boundary neighbor. Correct solutions check that specific pair before decrementing the violation counter, avoiding off-by-one logic that assumes where the “remaining allowed violation” must be.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
Successful attempts consistently used a correct sliding-window invariant: the current substring/window always contains at most a fixed number (one) of “violations” defined via adjacent equal pairs. They maintained this invariant with a monotone two-pointer approach by incrementing a violation counter when the window expands and decrementing it appropriately as the left boundary moves. Partially correct attempts tried to special-case the “second violation” without fully maintaining the general invariant through pointer movement, which can break when the window contains overlapping/shifted adjacency patterns. Several failed/partial approaches also show the risk of incorrect boundary updates—confusing which adjacent pair gets removed or relying on assumptions about where the remaining “allowed” pair must be located.
```

</details>

4. Avoid Brittle Special-Case Logic
Description: Don’t replace invariant maintenance with ad hoc pointer jumps unless you can prove correctness for all overlap patterns.
<details>
<summary>Content 4</summary>

```text
Partially correct attempts often tried to directly jump the left pointer to a guessed index when a second violation appears, but overlapping adjacent pairs can make the guessed adjustment incorrect. The robust approach is to shrink incrementally under the same invariant (counter-based) rather than relying on a one-off structural assumption.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
Successful attempts consistently used a correct sliding-window invariant: the current substring/window always contains at most a fixed number (one) of “violations” defined via adjacent equal pairs. They maintained this invariant with a monotone two-pointer approach by incrementing a violation counter when the window expands and decrementing it appropriately as the left boundary moves. Partially correct attempts tried to special-case the “second violation” without fully maintaining the general invariant through pointer movement, which can break when the window contains overlapping/shifted adjacency patterns. Several failed/partial approaches also show the risk of incorrect boundary updates—confusing which adjacent pair gets removed or relying on assumptions about where the remaining “allowed” pair must be located.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
Successful attempts consistently used a correct sliding-window invariant: the current substring/window always contains at most a fixed number (one) of “violations” defined via adjacent equal pairs. They maintained this invariant with a monotone two-pointer approach by incrementing a violation counter when the window expands and decrementing it appropriately as the left boundary moves. Partially correct attempts tried to special-case the “second violation” without fully maintaining the general invariant through pointer movement, which can break when the window contains overlapping/shifted adjacency patterns. Several failed/partial approaches also show the risk of incorrect boundary updates—confusing which adjacent pair gets removed or relying on assumptions about where the remaining “allowed” pair must be located.
</reasoning>

<memories>
  <memory>
    <title>Constraint-Driven Sliding Window Invariant</title>
    <description>Convert “at most one consecutive equal pair” into an explicit, countable window invariant.</description>
    <content>Represent the constraint using a simple metric (e.g., the number of adjacent-equal “bad pairs” inside the current window). Maintain an invariant like “bad_pairs ≤ 1” at every step, so the window is always valid while you search for the maximum length.</content>
  </memory>

  <memory>
    <title>Two-Pointer with Violation Counter</title>
    <description>Update a violation counter when the right pointer expands, and shrink with the same counter when it exceeds the limit.</description>
    <content>When extending the window by one character, only a small local change can affect validity (typically the new boundary adjacency). While the counter exceeds the allowed maximum, move the left pointer forward and decrement the counter only if the removed boundary adjacency was part of a violation.</content>
  </memory>

  <memory>
    <title>Boundary-Removal Accounting</title>
    <description>When shrinking a window, recompute the effect only for adjacencies that actually change at the boundary.</description>
    <content>As the left boundary moves, the only adjacent-equal pair status that can change is the one involving the new left boundary neighbor. Correct solutions check that specific pair before decrementing the violation counter, avoiding off-by-one logic that assumes where the “remaining allowed violation” must be.</content>
  </memory>

  <memory>
    <title>Avoid Brittle Special-Case Logic</title>
    <description>Don’t replace invariant maintenance with ad hoc pointer jumps unless you can prove correctness for all overlap patterns.</description>
    <content>Partially correct attempts often tried to directly jump the left pointer to a guessed index when a second violation appears, but overlapping adjacent pairs can make the guessed adjustment incorrect. The robust approach is to shrink incrementally under the same invariant (counter-based) rather than relying on a one-off structural assumption.</content>
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
You are given a 0-indexed string s that consists of digits from 0 to 9.
A string t is called a semi-repetitive if there is at most one consecutive pair of the same digits inside t. For example, 0010, 002020, 0123, 2002, and 54944 are semi-repetitive while 00101022, and 1101234883 are not.
Return the length of the longest semi-repetitive substring inside s.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "52233"
Output: 4
Explanation: The longest semi-repetitive substring is "5223", which starts at i = 0 and ends at j = 3. 

Example 2:

Input: s = "5494"
Output: 4
Explanation: s is a semi-reptitive string, so the answer is 4.

Example 3:

Input: s = "1111111"
Output: 2
Explanation: The longest semi-repetitive substring is "11", which starts at i = 0 and ends at j = 1.

 
Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '9'

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        l = 0

        # window [l..r] should contain at most one "bad" consecutive pair
        bad = 0  # number of indices i in window where s[i]==s[i-1]

        for r in range(1, n):
            if s[r] == s[r - 1]:
                bad += 1

            while bad > 1:
                # if the pair ending at current l exists, remove it when moving l
                if l + 1 <= r and s[l + 1] == s[l]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        left = 0
        bad_pairs = 0  # number of indices i where s[i] == s[i-1] in current window

        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                bad_pairs += 1

            # maintain at most one consecutive equal pair inside the window
            while bad_pairs > 1:
                if left + 1 <= right and s[left + 1] == s[left]:
                    bad_pairs -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # Sliding window [l, r] that contains at most one place where s[i]==s[i-1]
        l = 0
        bad = 0  # number of consecutive-equal pairs within the window

        best = 1
        for r in range(n):
            # When extending to r, check if (r-1, r) is a consecutive equal pair
            if r > 0 and s[r] == s[r - 1]:
                bad += 1

            # If we have more than one consecutive equal pair, move l forward
            while bad > 1:
                # If removing s[l] affects the pair (l, l+1), then adjust.
                if l + 1 <= r and s[l + 1] == s[l]:
                    bad -= 1
                l += 1

            best = max(best, r - l + 1)

        return best
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        l = 0
        pairs = 0  # number of indices k with s[k] == s[k+1] within current window

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                pairs += 1

            while pairs > 1:
                # Moving l to the right may remove a pair that starts at l
                if l + 1 < n and s[l] == s[l + 1]:
                    pairs -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        l = 0
        bad = 0  # number of consecutive equal pairs in current window

        for r in range(n - 1):
            if s[r] == s[r + 1]:
                bad += 1

            # ensure at most one consecutive equal pair
            while bad > 1:
                if s[l] == s[l + 1]:
                    bad -= 1
                l += 1

            # window [l, r+1] length
            ans = max(ans, (r + 1) - l + 1)

        # if string length is 1, or no pairs considered, ans may remain 0
        return max(ans, 1)
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        l = 0
        bad = 0  # number of consecutive equal pairs in current window

        for r in range(1, n):
            if s[r] == s[r - 1]:
                bad += 1

            while bad > 1:
                if l + 1 <= r and s[l + 1] == s[l]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n
        
        ans = 1
        left = 0
        bad = 0  # count of indices i in [left, current-1] where s[i]==s[i+1]
        
        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                bad += 1
            
            while bad > 1:
                if left + 1 <= right and s[left] == s[left + 1]:
                    bad -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        l = 0
        # count how many adjacent equal pairs exist in current window
        bad = 0  # number of i in [l+1..r] with s[i]==s[i-1]

        for r in range(1, n):
            if s[r] == s[r - 1]:
                bad += 1

            # shrink until at most one adjacent equal pair
            while bad > 1:
                # when moving l forward, we may remove the pair (l, l+1)
                if l + 1 <= r and s[l + 1] == s[l]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        bad_pairs = 0  # number of indices i in [left, right-1] where s[i]==s[i+1]
        
        ans = 1
        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                bad_pairs += 1
            
            while bad_pairs > 1:
                # Move left forward, updating bad_pairs if we discard a consecutive pair
                if left + 1 <= right and s[left] == s[left + 1]:
                    bad_pairs -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        # count positions i where s[i] == s[i-1]
        # then a substring is semi-repetitive iff it contains at most one such position.
        bad = [-1] * n
        cnt = 0
        # We'll use two pointers with count of consecutive-equal pairs inside window.
        ans = 1
        left = 0
        pairs_in_window = 0  # number of indices k in (left+1..right) with s[k]==s[k-1]

        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                pairs_in_window += 1

            # shrink until at most one consecutive pair remains
            while pairs_in_window > 1:
                if left + 1 <= right and s[left + 1] == s[left]:
                    pairs_in_window -= 1
                left += 1

            ans = max(ans, right - left + 1)

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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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

  1. Constraint-Driven Sliding Window Invariant: Convert “at most one consecutive equal pair” into an explicit, countable window invariant.
     Represent the constraint using a simple metric (e.g., the number of adjacent-equal “bad pairs” inside the current window). Maintain an invariant like “bad_pairs ≤ 1” at every step, so the window is always valid while you search for the maximum length.
  2. Two-Pointer with Violation Counter: Update a violation counter when the right pointer expands, and shrink with the same counter when it exceeds the limit.
     When extending the window by one character, only a small local change can affect validity (typically the new boundary adjacency). While the counter exceeds the allowed maximum, move the left pointer forward and decrement the counter only if the removed boundary adjacency was part of a violation.
  3. Boundary-Removal Accounting: When shrinking a window, recompute the effect only for adjacencies that actually change at the boundary.
     As the left boundary moves, the only adjacent-equal pair status that can change is the one involving the new left boundary neighbor. Correct solutions check that specific pair before decrementing the violation counter, avoiding off-by-one logic that assumes where the “remaining allowed violation” must be.
  4. Avoid Brittle Special-Case Logic: Don’t replace invariant maintenance with ad hoc pointer jumps unless you can prove correctness for all overlap patterns.
     Partially correct attempts often tried to directly jump the left pointer to a guessed index when a second violation appears, but overlapping adjacent pairs can make the guessed adjustment incorrect. The robust approach is to shrink incrementally under the same invariant (counter-based) rather than relying on a one-off structural assumption.

Apply these insights to the problem below.

### Question:
You are given a 0-indexed string s that consists of digits from 0 to 9.
A string t is called a semi-repetitive if there is at most one consecutive pair of the same digits inside t. For example, 0010, 002020, 0123, 2002, and 54944 are semi-repetitive while 00101022, and 1101234883 are not.
Return the length of the longest semi-repetitive substring inside s.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "52233"
Output: 4
Explanation: The longest semi-repetitive substring is "5223", which starts at i = 0 and ends at j = 3. 

Example 2:

Input: s = "5494"
Output: 4
Explanation: s is a semi-reptitive string, so the answer is 4.

Example 3:

Input: s = "1111111"
Output: 2
Explanation: The longest semi-repetitive substring is "11", which starts at i = 0 and ends at j = 1.

 
Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '9'

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Augmented generation 1</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        # Two pointers with a "violation counter":
        # let bad be the number of indices k in [l+1..r] such that s[k] == s[k-1].
        # A substring is valid iff bad <= 1.
        n = len(s)
        l = 0
        bad = 0
        ans = 1  # s is non-empty

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad += 1

            while bad > 1:
                # Removing s[l] affects only the adjacency between s[l] and s[l+1]
                # (i.e., whether s[l+1] == s[l]).
                if l + 1 <= r and s[l + 1] == s[l]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # bad pairs = number of i where s[i] == s[i-1] inside current window [l..r]
        bad = 0
        ans = 0
        l = 0

        for r in range(n):
            # Adding s[r] creates a new adjacent-equal pair with s[r-1] (if any)
            if r > 0 and s[r] == s[r - 1]:
                bad += 1

            # Maintain invariant: bad <= 1
            while bad > 1:
                # When removing s[l], only adjacency that can change is between s[l] and s[l+1]
                if l + 1 <= r and s[l] == s[l + 1]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        bad_pairs = 0  # number of indices i in [left, right-1] with s[i]==s[i+1]
        ans = 1

        for right in range(n):
            # When we extend to right, we may create a new bad pair at (right-1, right)
            if right > 0 and s[right] == s[right - 1]:
                bad_pairs += 1

            # Maintain invariant: bad_pairs <= 1
            while bad_pairs > 1:
                # We are moving left forward; only adjacency that can change is (left, left+1)
                if left + 1 <= right and s[left] == s[left + 1]:
                    bad_pairs -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        # Maintain a sliding window [l..r] such that it contains at most one
        # adjacent-equal pair, i.e., pairs where s[i] == s[i+1].
        n = len(s)
        l = 0
        bad_pairs = 0  # number of indices i in [l..r-1] with s[i]==s[i+1]
        ans = 1

        for r in range(n):
            # Add new character s[r]; only adjacency that can newly contribute
            # to bad_pairs is between r-1 and r.
            if r > 0 and s[r] == s[r - 1]:
                bad_pairs += 1

            # If constraint violated, move left boundary until valid again.
            while bad_pairs > 1:
                # Removing s[l] affects only the adjacency between l and l+1
                # (if it exists in the current window).
                if l + 1 <= r and s[l] == s[l + 1]:
                    bad_pairs -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        # Count "bad pairs" = number of indices i in window where s[i] == s[i+1].
        # We maintain invariant: bad_pairs <= 1 for the current window [l, r].
        n = len(s)
        l = 0
        bad_pairs = 0
        ans = 1

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad_pairs += 1

            while bad_pairs > 1:
                # When removing s[l] from the left, only adjacency that can change is (l, l+1),
                # i.e., between s[l] and s[l+1], provided l+1 is within the window.
                if l + 1 <= r and s[l] == s[l + 1]:
                    bad_pairs -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # bad_pairs = number of i such that s[i] == s[i+1] within current window [l..r]
        bad_pairs = 0
        l = 0
        best = 1

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad_pairs += 1

            while bad_pairs > 1:
                # If the pair (l, l+1) is bad, removing s[l] reduces bad_pairs by 1.
                if l + 1 <= r and s[l] == s[l + 1]:
                    bad_pairs -= 1
                l += 1

            best = max(best, r - l + 1)

        return best
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        bad = 0  # number of indices i in [left, right-1] such that s[i] == s[i+1]
        ans = 0

        for right in range(n):
            # New pair formed with the previous char
            if right - 1 >= left and s[right] == s[right - 1]:
                bad += 1

            # Keep window valid: at most one consecutive equal pair
            while bad > 1:
                # When moving left forward, only pair (left, left+1) might be removed
                if left + 1 <= right and s[left] == s[left + 1]:
                    bad -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # bad pairs = number of indices i in current window [l, r]
        # such that s[i] == s[i+1]. For a substring to be semi-repetitive: bad_pairs <= 1.
        l = 0
        bad_pairs = 0
        ans = 1

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad_pairs += 1

            while bad_pairs > 1:
                # Removing s[l] affects adjacency only between l and l+1 (old boundary).
                if l + 1 <= r and s[l] == s[l + 1]:
                    bad_pairs -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # bad_pairs = number of indices i in [l, r-1] such that s[i] == s[i+1]
        l = 0
        bad_pairs = 0
        ans = 1

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad_pairs += 1

            while bad_pairs > 1:
                # Removing s[l] changes only the adjacency between s[l] and s[l+1],
                # i.e., whether s[l] == s[l+1]. That adjacency corresponds to index l.
                if l + 1 <= r and s[l] == s[l + 1]:
                    bad_pairs -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        # bad_pairs = number of indices i in [l, r-1] such that s[i] == s[i+1]
        bad_pairs = 0
        ans = 0
        l = 0

        for r in range(n):
            if r > 0 and s[r] == s[r - 1]:
                bad_pairs += 1

            while bad_pairs > 1:
                # removing s[l], only adjacency that changes is between (l, l+1)
                if l + 1 <= r and s[l] == s[l + 1]:
                    bad_pairs -= 1
                l += 1

            ans = max(ans, r - l + 1)

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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
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
      "expected": "4",
      "actual": "4",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "32",
      "actual": "32",
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
      "expected": "39",
      "actual": "39",
      "error": ""
    }
  ]
}
```

</details>
