# Problem 3230

- Domain: `coding`

## Problem

```text
You are given a 0-indexed string word.
In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.
Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.
Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.
 
Example 1:

Input: word = "aaaaa"
Output: 2
Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.

Example 2:

Input: word = "abddez"
Output: 2
Explanation: We can change word into "ybdoez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
Example 3:

Input: word = "zyxyxyz"
Output: 3
Explanation: We can change word into "zaxaxaz" which does not have any adjacent almost-equal characters. 
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.

 
Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.
```

### Starter Code

```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
```

### Test Cases

```json
[
  {
    "input": "\"aaaaa\"",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "\"abddez\"",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "\"zyxyxyz\"",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "\"\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"x\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"k\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"e\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"a\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"i\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"d\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"s\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"b\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"tuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmno\"",
    "output": "49",
    "testtype": "functional"
  },
  {
    "input": "\"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\"",
    "output": "50",
    "testtype": "functional"
  },
  {
    "input": "\"cxyayzaxybxzbyxcyybyycyzczzayxazyaxxczybxzczxbyxcyybxxaxzbzyczzayybyyayybxzczzbxxbyyaxzcxzczxcyyczzb\"",
    "output": "25",
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
You are given a 0-indexed string word.
In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.
Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.
Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.
 
Example 1:

Input: word = "aaaaa"
Output: 2
Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.

Example 2:

Input: word = "abddez"
Output: 2
Explanation: We can change word into "ybdoez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
Example 3:

Input: word = "zyxyxyz"
Output: 3
Explanation: We can change word into "zaxaxaz" which does not have any adjacent almost-equal characters. 
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.

 
Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        # minimal operations using DP with last chosen character category:
        # Track last letter as one of 27 categories:
        # 0..25 actual letters (kept as-is in transitions via "best choose"),
        # 26 = "we don't care" (not used; kept for clarity)
        #
        # More direct approach: For each position i, choose a letter c.
        # Cost at i is 0 if c == word[i] else 1.
        # Constraint: for adjacent positions, chosen letters x,y must NOT be almost-equal
        # i.e., |x-y| == 0 or 1 in alphabet index difference. So need |x-y| >= 2.
        #
        # DP over alphabet letters (26) is small: n<=100 => 2600 states, fine.

        INF = 10**9
        dp_prev = [INF] * 26
        # initialize with choosing letter at position 0
        for c in range(26):
            dp_prev[c] = 0 if c == (ord(word[0]) - 97) else 1

        for i in range(1, n):
            dp_cur = [INF] * 26
            orig = ord(word[i]) - 97
            for c in range(26):  # chosen letter at i
                cost = 0 if c == orig else 1
                best_prev = INF
                # previous chosen letter p must satisfy |c-p| >= 2
                for p in range(26):
                    if abs(c - p) >= 2:
                        if dp_prev[p] < best_prev:
                            best_prev = dp_prev[p]
                dp_cur[c] = best_prev + cost
            dp_prev = dp_cur

        return min(dp_prev)
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # DP with 27 states: previous chosen character (0..25) or 26 for "none"
        n = len(word)
        INF = 10**9
        dp = [[INF] * 27 for _ in range(n + 1)]
        dp[0][26] = 0

        def ok(a, b):
            # a and b are almost-equal if a==b or adjacent in alphabet
            return abs(a - b) <= 1

        for i in range(n):
            for prev in range(27):
                cur_cost = dp[i][prev]
                if cur_cost >= INF:
                    continue
                prev_char = None if prev == 26 else prev

                for x in range(26):
                    if prev_char is not None and ok(prev_char, x):
                        continue
                    add = 0 if ord(word[i]) - 97 == x else 1
                    dp[i + 1][x] = min(dp[i + 1][x], cur_cost + add)

        return min(dp[n])
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        # dp[i][c]: min ops up to position i with resulting word[i] = c
        # c is 0..25
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        
        # Initialize for i = 0
        for c in range(26):
            dp[0][c] = 0 if (ord(word[0]) - 97) == c else 1
        
        def almost_equal(a, b):
            # a and b are almost-equal iff a==b or adjacent in alphabet
            return a == b or abs(a - b) == 1
        
        for i in range(1, n):
            orig = ord(word[i]) - 97
            for c in range(26):  # chosen char at i
                cost = 0 if c == orig else 1
                best = INF
                for p in range(26):  # chosen char at i-1
                    if not almost_equal(p, c):
                        if dp[i - 1][p] < best:
                            best = dp[i - 1][p]
                dp[i][c] = best + cost
        
        return min(dp[n - 1])
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)

        # Adjacent almost-equal means: same letter or consecutive letters in alphabet.
        # We need minimal changes so that for all i:
        #   |new[i] - new[i-1]| >= 2  (in alphabet distance)
        #
        # With operations allowed independently per position, we can do DP:
        # dp[i][c] = min ops up to i if word[i] becomes letter c (0..25)
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        for c in range(26):
            dp[0][c] = 0 if ord(word[0]) - 97 == c else 1

        for i in range(1, n):
            prev_word_val = ord(word[i]) - 97
            for c in range(26):
                cost = 0 if c == prev_word_val else 1
                best = INF
                # Allowed predecessors p satisfy abs(c - p) >= 2
                for p in range(26):
                    if abs(c - p) >= 2:
                        if dp[i - 1][p] < best:
                            best = dp[i - 1][p]
                dp[i][c] = best + cost

        return min(dp[n - 1])
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # We need the minimum operations so that after changes
        # no adjacent pair (word[i], word[i+1]) is almost-equal:
        # almost-equal means equal or consecutive in alphabet.
        #
        # DP over positions with last chosen character.
        # dp[i][c] = min ops up to position i if we set word[i] to char c.
        n = len(word)
        INF = 10**9

        # Map letters 'a'..'z' to 0..25
        orig = [ord(ch) - 97 for ch in word]

        # Initialize for i=0
        dp_prev = [INF] * 26
        for c in range(26):
            dp_prev[c] = 0 if c == orig[0] else 1

        for i in range(1, n):
            dp_cur = [INF] * 26
            oi = orig[i]
            for c in range(26):  # chosen for position i
                add = 0 if c == oi else 1
                best = INF
                # previous char p cannot be almost-equal with c:
                # disallow p==c, p==c-1, p==c+1
                for p in range(26):
                    if p == c or p + 1 == c or p - 1 == c:
                        continue
                    if dp_prev[p] < best:
                        best = dp_prev[p]
                dp_cur[c] = best + add
            dp_prev = dp_cur

        return min(dp_prev)
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # If we look at the final string after operations, each kept position
        # only needs to avoid "almost-equal" adjacency with its neighbors.
        #
        # It turns out that to minimize operations, for each i we keep the
        # original character if possible, otherwise we change it.
        #
        # Greedy works with the observation that "almost-equal" depends only on
        # equality or +/- 1 in alphabet. While scanning left to right, we choose
        # the smallest number of changes by keeping word[i] whenever it doesn't
        # violate the constraint with the previous chosen character; otherwise
        # we change word[i] to the smallest feasible letter.
        #
        # Because alphabet size is 26 and constraint is local, this greedy
        # yields optimal minimum changes.
        
        def ok(a: str, b: str) -> bool:
            da = ord(a) - ord('a')
            db = ord(b) - ord('a')
            return da == db or abs(da - db) == 1  # "almost-equal"

        n = len(word)
        if n <= 1:
            return 0

        # chosen is the character we decide to have at each position
        # (we don't need full string, just the previous char).
        prev = word[0]
        changes = 0

        for i in range(1, n):
            cur_orig = word[i]
            # If original doesn't create an almost-equal pair with prev, keep it.
            if not ok(prev, cur_orig):
                prev = cur_orig
            else:
                changes += 1
                # Pick any letter that is not almost-equal to prev.
                # Choose lexicographically smallest feasible.
                prev_ord = ord(prev) - ord('a')
                forbidden = {prev_ord, prev_ord - 1, prev_ord + 1}
                chosen_ord = 0
                while chosen_ord in forbidden:
                    chosen_ord += 1
                prev = chr(chosen_ord + ord('a'))

        return changes
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # After operations, we need a final string s such that for all i:
        # |ord(s[i]) - ord(s[i-1])| != 0 and != 1 (mod alphabet adjacency)
        # i.e., adjacent letters must differ by at least 2.
        #
        # We minimize number of positions changed from original word.

        n = len(word)
        w = [ord(c) - 97 for c in word]  # 0..25

        # dp[i][c] = min ops for prefix ending at position i with s[i] = c
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        dp[0] = [0 if c == w[0] else 1 for c in range(26)]

        def ok(prev, cur):
            return abs(prev - cur) >= 2  # different and not adjacent in alphabet

        for i in range(1, n):
            cost = [0 if c == w[i] else 1 for c in range(26)]
            for cur in range(26):
                best = INF
                # Try all prev; n<=100 so 26*26 per step is fine.
                for prev in range(26):
                    if ok(prev, cur):
                        val = dp[i - 1][prev]
                        if val < best:
                            best = val
                dp[i][cur] = best + cost[cur]

        return min(dp[n - 1])
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # DP over the processed prefix.
        # Let dp[c] = minimum operations so far where the last kept character is c (0..25).
        # We rebuild the string by deciding each position's final character.
        n = len(word)
        INF = 10**9
        dp = [INF] * 26

        # Initialize with first character
        for c in range(26):
            dp[c] = 0 if ord(word[0]) - 97 == c else 1

        for i in range(1, n):
            ndp = [INF] * 26
            orig = ord(word[i]) - 97
            for prev in range(26):
                if dp[prev] == INF:
                    continue
                # Choose current character cur such that it is NOT almost-equal to prev
                # almost-equal means cur == prev or |cur-prev| == 1
                for cur in range(26):
                    if cur == prev or abs(cur - prev) == 1:
                        continue
                    cost = 0 if cur == orig else 1
                    if dp[prev] + cost < ndp[cur]:
                        ndp[cur] = dp[prev] + cost
            dp = ndp

        return min(dp)
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)

        # almost-equal means: equal OR adjacent in alphabet
        # We'll greedily fix any "bad" adjacent pair (i-1, i)
        # by changing word[i] to the smallest possible letter that breaks
        # the relation with both neighbors (i-1 and i+1 not yet fixed,
        # but we only need to ensure current pair (i-1,i) is fixed).
        #
        # Greedy works because the condition is local (adjacent pairs only):
        # once we fix a[i] to be safe w.r.t. a[i-1], the earlier part
        # never changes again.
        #
        # For the best minimum, we should avoid changing when already safe.

        def is_bad(a: str, b: str) -> bool:
            if a == b:
                return True
            return abs(ord(a) - ord(b)) == 1

        # Use a mutable list for the working string
        s = list(word)
        ops = 0

        for i in range(1, n):
            if is_bad(s[i - 1], s[i]):
                # Need to change s[i]
                # Choose a letter c such that:
                # 1) not almost-equal with s[i-1]
                prev = s[i - 1]
                for code in range(26):
                    c = chr(ord('a') + code)
                    if not is_bad(prev, c):
                        s[i] = c
                        ops += 1
                        break

        # Note: With this greedy, it suffices because only adjacent pairs matter.
        # Changing s[i] might create a bad pair with s[i+1], but that will be handled
        # when we reach i+1.
        return ops
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        arr = [ord(c) - 97 for c in word]  # 0..25

        # dp[i][c] = min operations after fixing position i to letter c,
        # while ensuring no adjacent almost-equal characters.
        INF = 10**9
        dp = [ [INF]*26 for _ in range(n) ]

        # allowed transitions:
        # adjacent letters must NOT be equal and NOT consecutive in alphabet.
        def ok(prev, cur):
            return prev != cur and abs(prev - cur) != 1

        for c in range(26):
            dp[0][c] = (0 if c == arr[0] else 1)

        for i in range(1, n):
            for cur in range(26):
                cost = 0 if cur == arr[i] else 1
                best = INF
                # prev can be any except {cur-1, cur, cur+1}
                for prev in range(26):
                    if ok(prev, cur):
                        val = dp[i-1][prev]
                        if val < best:
                            best = val
                dp[i][cur] = best + cost

        return min(dp[n-1])
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.2000 | `partial` |
| 1 | 1.0000 | `full` |
| 2 | 0.2000 | `partial` |
| 3 | 0.2000 | `partial` |
| 4 | 0.2000 | `partial` |
| 5 | 0.8000 | `partial` |
| 6 | 0.2000 | `partial` |
| 7 | 0.2000 | `partial` |
| 8 | 0.8000 | `partial` |
| 9 | 0.2000 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
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
      "expected": "49",
      "actual": "49",
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
      "expected": "25",
      "actual": "25",
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
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 3</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 4</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: list index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 5</summary>

```json
{
  "passed": 12,
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
      "passed": false,
      "expected": "49",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "43",
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
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: list index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 8</summary>

```json
{
  "passed": 12,
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
      "passed": false,
      "expected": "49",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "43",
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
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: list index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
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
You are given a 0-indexed string word.
In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.
Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.
Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.
 
Example 1:

Input: word = "aaaaa"
Output: 2
Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.

Example 2:

Input: word = "abddez"
Output: 2
Explanation: We can change word into "ybdoez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
Example 3:

Input: word = "zyxyxyz"
Output: 3
Explanation: We can change word into "zaxaxaz" which does not have any adjacent almost-equal characters. 
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.

 
Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.

### Solutions
#### Correct
Attempt 1
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # DP with 27 states: previous chosen character (0..25) or 26 for "none"
        n = len(word)
        INF = 10**9
        dp = [[INF] * 27 for _ in range(n + 1)]
        dp[0][26] = 0

        def ok(a, b):
            # a and b are almost-equal if a==b or adjacent in alphabet
            return abs(a - b) <= 1

        for i in range(n):
            for prev in range(27):
                cur_cost = dp[i][prev]
                if cur_cost >= INF:
                    continue
                prev_char = None if prev == 26 else prev

                for x in range(26):
                    if prev_char is not None and ok(prev_char, x):
                        continue
                    add = 0 if ord(word[i]) - 97 == x else 1
                    dp[i + 1][x] = min(dp[i + 1][x], cur_cost + add)

        return min(dp[n])
```

#### Partially Correct
Attempt 1
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        # minimal operations using DP with last chosen character category:
        # Track last letter as one of 27 categories:
        # 0..25 actual letters (kept as-is in transitions via "best choose"),
        # 26 = "we don't care" (not used; kept for clarity)
        #
        # More direct approach: For each position i, choose a letter c.
        # Cost at i is 0 if c == word[i] else 1.
        # Constraint: for adjacent positions, chosen letters x,y must NOT be almost-equal
        # i.e., |x-y| == 0 or 1 in alphabet index difference. So need |x-y| >= 2.
        #
        # DP over alphabet letters (26) is small: n<=100 => 2600 states, fine.

        INF = 10**9
        dp_prev = [INF] * 26
        # initialize with choosing letter at position 0
        for c in range(26):
            dp_prev[c] = 0 if c == (ord(word[0]) - 97) else 1

        for i in range(1, n):
            dp_cur = [INF] * 26
            orig = ord(word[i]) - 97
            for c in range(26):  # chosen letter at i
                cost = 0 if c == orig else 1
                best_prev = INF
                # previous chosen letter p must satisfy |c-p| >= 2
                for p in range(26):
                    if abs(c - p) >= 2:
                        if dp_prev[p] < best_prev:
                            best_prev = dp_prev[p]
                dp_cur[c] = best_prev + cost
            dp_prev = dp_cur

        return min(dp_prev)
```

Attempt 2
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        # dp[i][c]: min ops up to position i with resulting word[i] = c
        # c is 0..25
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        
        # Initialize for i = 0
        for c in range(26):
            dp[0][c] = 0 if (ord(word[0]) - 97) == c else 1
        
        def almost_equal(a, b):
            # a and b are almost-equal iff a==b or adjacent in alphabet
            return a == b or abs(a - b) == 1
        
        for i in range(1, n):
            orig = ord(word[i]) - 97
            for c in range(26):  # chosen char at i
                cost = 0 if c == orig else 1
                best = INF
                for p in range(26):  # chosen char at i-1
                    if not almost_equal(p, c):
                        if dp[i - 1][p] < best:
                            best = dp[i - 1][p]
                dp[i][c] = best + cost
        
        return min(dp[n - 1])
```

Attempt 3
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)

        # Adjacent almost-equal means: same letter or consecutive letters in alphabet.
        # We need minimal changes so that for all i:
        #   |new[i] - new[i-1]| >= 2  (in alphabet distance)
        #
        # With operations allowed independently per position, we can do DP:
        # dp[i][c] = min ops up to i if word[i] becomes letter c (0..25)
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        for c in range(26):
            dp[0][c] = 0 if ord(word[0]) - 97 == c else 1

        for i in range(1, n):
            prev_word_val = ord(word[i]) - 97
            for c in range(26):
                cost = 0 if c == prev_word_val else 1
                best = INF
                # Allowed predecessors p satisfy abs(c - p) >= 2
                for p in range(26):
                    if abs(c - p) >= 2:
                        if dp[i - 1][p] < best:
                            best = dp[i - 1][p]
                dp[i][c] = best + cost

        return min(dp[n - 1])
```

Attempt 4
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # We need the minimum operations so that after changes
        # no adjacent pair (word[i], word[i+1]) is almost-equal:
        # almost-equal means equal or consecutive in alphabet.
        #
        # DP over positions with last chosen character.
        # dp[i][c] = min ops up to position i if we set word[i] to char c.
        n = len(word)
        INF = 10**9

        # Map letters 'a'..'z' to 0..25
        orig = [ord(ch) - 97 for ch in word]

        # Initialize for i=0
        dp_prev = [INF] * 26
        for c in range(26):
            dp_prev[c] = 0 if c == orig[0] else 1

        for i in range(1, n):
            dp_cur = [INF] * 26
            oi = orig[i]
            for c in range(26):  # chosen for position i
                add = 0 if c == oi else 1
                best = INF
                # previous char p cannot be almost-equal with c:
                # disallow p==c, p==c-1, p==c+1
                for p in range(26):
                    if p == c or p + 1 == c or p - 1 == c:
                        continue
                    if dp_prev[p] < best:
                        best = dp_prev[p]
                dp_cur[c] = best + add
            dp_prev = dp_cur

        return min(dp_prev)
```

Attempt 5
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # If we look at the final string after operations, each kept position
        # only needs to avoid "almost-equal" adjacency with its neighbors.
        #
        # It turns out that to minimize operations, for each i we keep the
        # original character if possible, otherwise we change it.
        #
        # Greedy works with the observation that "almost-equal" depends only on
        # equality or +/- 1 in alphabet. While scanning left to right, we choose
        # the smallest number of changes by keeping word[i] whenever it doesn't
        # violate the constraint with the previous chosen character; otherwise
        # we change word[i] to the smallest feasible letter.
        #
        # Because alphabet size is 26 and constraint is local, this greedy
        # yields optimal minimum changes.
        
        def ok(a: str, b: str) -> bool:
            da = ord(a) - ord('a')
            db = ord(b) - ord('a')
            return da == db or abs(da - db) == 1  # "almost-equal"

        n = len(word)
        if n <= 1:
            return 0

        # chosen is the character we decide to have at each position
        # (we don't need full string, just the previous char).
        prev = word[0]
        changes = 0

        for i in range(1, n):
            cur_orig = word[i]
            # If original doesn't create an almost-equal pair with prev, keep it.
            if not ok(prev, cur_orig):
                prev = cur_orig
            else:
                changes += 1
                # Pick any letter that is not almost-equal to prev.
                # Choose lexicographically smallest feasible.
                prev_ord = ord(prev) - ord('a')
                forbidden = {prev_ord, prev_ord - 1, prev_ord + 1}
                chosen_ord = 0
                while chosen_ord in forbidden:
                    chosen_ord += 1
                prev = chr(chosen_ord + ord('a'))

        return changes
```

Attempt 6
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # After operations, we need a final string s such that for all i:
        # |ord(s[i]) - ord(s[i-1])| != 0 and != 1 (mod alphabet adjacency)
        # i.e., adjacent letters must differ by at least 2.
        #
        # We minimize number of positions changed from original word.

        n = len(word)
        w = [ord(c) - 97 for c in word]  # 0..25

        # dp[i][c] = min ops for prefix ending at position i with s[i] = c
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        dp[0] = [0 if c == w[0] else 1 for c in range(26)]

        def ok(prev, cur):
            return abs(prev - cur) >= 2  # different and not adjacent in alphabet

        for i in range(1, n):
            cost = [0 if c == w[i] else 1 for c in range(26)]
            for cur in range(26):
                best = INF
                # Try all prev; n<=100 so 26*26 per step is fine.
                for prev in range(26):
                    if ok(prev, cur):
                        val = dp[i - 1][prev]
                        if val < best:
                            best = val
                dp[i][cur] = best + cost[cur]

        return min(dp[n - 1])
```

Attempt 7
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # DP over the processed prefix.
        # Let dp[c] = minimum operations so far where the last kept character is c (0..25).
        # We rebuild the string by deciding each position's final character.
        n = len(word)
        INF = 10**9
        dp = [INF] * 26

        # Initialize with first character
        for c in range(26):
            dp[c] = 0 if ord(word[0]) - 97 == c else 1

        for i in range(1, n):
            ndp = [INF] * 26
            orig = ord(word[i]) - 97
            for prev in range(26):
                if dp[prev] == INF:
                    continue
                # Choose current character cur such that it is NOT almost-equal to prev
                # almost-equal means cur == prev or |cur-prev| == 1
                for cur in range(26):
                    if cur == prev or abs(cur - prev) == 1:
                        continue
                    cost = 0 if cur == orig else 1
                    if dp[prev] + cost < ndp[cur]:
                        ndp[cur] = dp[prev] + cost
            dp = ndp

        return min(dp)
```

Attempt 8
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)

        # almost-equal means: equal OR adjacent in alphabet
        # We'll greedily fix any "bad" adjacent pair (i-1, i)
        # by changing word[i] to the smallest possible letter that breaks
        # the relation with both neighbors (i-1 and i+1 not yet fixed,
        # but we only need to ensure current pair (i-1,i) is fixed).
        #
        # Greedy works because the condition is local (adjacent pairs only):
        # once we fix a[i] to be safe w.r.t. a[i-1], the earlier part
        # never changes again.
        #
        # For the best minimum, we should avoid changing when already safe.

        def is_bad(a: str, b: str) -> bool:
            if a == b:
                return True
            return abs(ord(a) - ord(b)) == 1

        # Use a mutable list for the working string
        s = list(word)
        ops = 0

        for i in range(1, n):
            if is_bad(s[i - 1], s[i]):
                # Need to change s[i]
                # Choose a letter c such that:
                # 1) not almost-equal with s[i-1]
                prev = s[i - 1]
                for code in range(26):
                    c = chr(ord('a') + code)
                    if not is_bad(prev, c):
                        s[i] = c
                        ops += 1
                        break

        # Note: With this greedy, it suffices because only adjacent pairs matter.
        # Changing s[i] might create a bad pair with s[i+1], but that will be handled
        # when we reach i+1.
        return ops
```

Attempt 9
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        arr = [ord(c) - 97 for c in word]  # 0..25

        # dp[i][c] = min operations after fixing position i to letter c,
        # while ensuring no adjacent almost-equal characters.
        INF = 10**9
        dp = [ [INF]*26 for _ in range(n) ]

        # allowed transitions:
        # adjacent letters must NOT be equal and NOT consecutive in alphabet.
        def ok(prev, cur):
            return prev != cur and abs(prev - cur) != 1

        for c in range(26):
            dp[0][c] = (0 if c == arr[0] else 1)

        for i in range(1, n):
            for cur in range(26):
                cost = 0 if cur == arr[i] else 1
                best = INF
                # prev can be any except {cur-1, cur, cur+1}
                for prev in range(26):
                    if ok(prev, cur):
                        val = dp[i-1][prev]
                        if val < best:
                            best = val
                dp[i][cur] = best + cost

        return min(dp[n-1])
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
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # DP with 27 states: previous chosen character (0..25) or 26 for "none"
        n = len(word)
        INF = 10**9
        dp = [[INF] * 27 for _ in range(n + 1)]
        dp[0][26] = 0

        def ok(a, b):
            # a and b are almost-equal if a==b or adjacent in alphabet
            return abs(a - b) <= 1

        for i in range(n):
            for prev in range(27):
                cur_cost = dp[i][prev]
                if cur_cost >= INF:
                    continue
                prev_char = None if prev == 26 else prev

                for x in range(26):
                    if prev_char is not None and ok(prev_char, x):
                        continue
                    add = 0 if ord(word[i]) - 97 == x else 1
                    dp[i + 1][x] = min(dp[i + 1][x], cur_cost + add)

        return min(dp[n])
```
```

</details>

#### Tier: `partial`

<details>
<summary>partial attempt 1</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        # minimal operations using DP with last chosen character category:
        # Track last letter as one of 27 categories:
        # 0..25 actual letters (kept as-is in transitions via "best choose"),
        # 26 = "we don't care" (not used; kept for clarity)
        #
        # More direct approach: For each position i, choose a letter c.
        # Cost at i is 0 if c == word[i] else 1.
        # Constraint: for adjacent positions, chosen letters x,y must NOT be almost-equal
        # i.e., |x-y| == 0 or 1 in alphabet index difference. So need |x-y| >= 2.
        #
        # DP over alphabet letters (26) is small: n<=100 => 2600 states, fine.

        INF = 10**9
        dp_prev = [INF] * 26
        # initialize with choosing letter at position 0
        for c in range(26):
            dp_prev[c] = 0 if c == (ord(word[0]) - 97) else 1

        for i in range(1, n):
            dp_cur = [INF] * 26
            orig = ord(word[i]) - 97
            for c in range(26):  # chosen letter at i
                cost = 0 if c == orig else 1
                best_prev = INF
                # previous chosen letter p must satisfy |c-p| >= 2
                for p in range(26):
                    if abs(c - p) >= 2:
                        if dp_prev[p] < best_prev:
                            best_prev = dp_prev[p]
                dp_cur[c] = best_prev + cost
            dp_prev = dp_cur

        return min(dp_prev)
```
```

</details>

<details>
<summary>partial attempt 2</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        # dp[i][c]: min ops up to position i with resulting word[i] = c
        # c is 0..25
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        
        # Initialize for i = 0
        for c in range(26):
            dp[0][c] = 0 if (ord(word[0]) - 97) == c else 1
        
        def almost_equal(a, b):
            # a and b are almost-equal iff a==b or adjacent in alphabet
            return a == b or abs(a - b) == 1
        
        for i in range(1, n):
            orig = ord(word[i]) - 97
            for c in range(26):  # chosen char at i
                cost = 0 if c == orig else 1
                best = INF
                for p in range(26):  # chosen char at i-1
                    if not almost_equal(p, c):
                        if dp[i - 1][p] < best:
                            best = dp[i - 1][p]
                dp[i][c] = best + cost
        
        return min(dp[n - 1])
```
```

</details>

<details>
<summary>partial attempt 3</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)

        # Adjacent almost-equal means: same letter or consecutive letters in alphabet.
        # We need minimal changes so that for all i:
        #   |new[i] - new[i-1]| >= 2  (in alphabet distance)
        #
        # With operations allowed independently per position, we can do DP:
        # dp[i][c] = min ops up to i if word[i] becomes letter c (0..25)
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        for c in range(26):
            dp[0][c] = 0 if ord(word[0]) - 97 == c else 1

        for i in range(1, n):
            prev_word_val = ord(word[i]) - 97
            for c in range(26):
                cost = 0 if c == prev_word_val else 1
                best = INF
                # Allowed predecessors p satisfy abs(c - p) >= 2
                for p in range(26):
                    if abs(c - p) >= 2:
                        if dp[i - 1][p] < best:
                            best = dp[i - 1][p]
                dp[i][c] = best + cost

        return min(dp[n - 1])
```
```

</details>

<details>
<summary>partial attempt 4</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # We need the minimum operations so that after changes
        # no adjacent pair (word[i], word[i+1]) is almost-equal:
        # almost-equal means equal or consecutive in alphabet.
        #
        # DP over positions with last chosen character.
        # dp[i][c] = min ops up to position i if we set word[i] to char c.
        n = len(word)
        INF = 10**9

        # Map letters 'a'..'z' to 0..25
        orig = [ord(ch) - 97 for ch in word]

        # Initialize for i=0
        dp_prev = [INF] * 26
        for c in range(26):
            dp_prev[c] = 0 if c == orig[0] else 1

        for i in range(1, n):
            dp_cur = [INF] * 26
            oi = orig[i]
            for c in range(26):  # chosen for position i
                add = 0 if c == oi else 1
                best = INF
                # previous char p cannot be almost-equal with c:
                # disallow p==c, p==c-1, p==c+1
                for p in range(26):
                    if p == c or p + 1 == c or p - 1 == c:
                        continue
                    if dp_prev[p] < best:
                        best = dp_prev[p]
                dp_cur[c] = best + add
            dp_prev = dp_cur

        return min(dp_prev)
```
```

</details>

<details>
<summary>partial attempt 5</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # If we look at the final string after operations, each kept position
        # only needs to avoid "almost-equal" adjacency with its neighbors.
        #
        # It turns out that to minimize operations, for each i we keep the
        # original character if possible, otherwise we change it.
        #
        # Greedy works with the observation that "almost-equal" depends only on
        # equality or +/- 1 in alphabet. While scanning left to right, we choose
        # the smallest number of changes by keeping word[i] whenever it doesn't
        # violate the constraint with the previous chosen character; otherwise
        # we change word[i] to the smallest feasible letter.
        #
        # Because alphabet size is 26 and constraint is local, this greedy
        # yields optimal minimum changes.
        
        def ok(a: str, b: str) -> bool:
            da = ord(a) - ord('a')
            db = ord(b) - ord('a')
            return da == db or abs(da - db) == 1  # "almost-equal"

        n = len(word)
        if n <= 1:
            return 0

        # chosen is the character we decide to have at each position
        # (we don't need full string, just the previous char).
        prev = word[0]
        changes = 0

        for i in range(1, n):
            cur_orig = word[i]
            # If original doesn't create an almost-equal pair with prev, keep it.
            if not ok(prev, cur_orig):
                prev = cur_orig
            else:
                changes += 1
                # Pick any letter that is not almost-equal to prev.
                # Choose lexicographically smallest feasible.
                prev_ord = ord(prev) - ord('a')
                forbidden = {prev_ord, prev_ord - 1, prev_ord + 1}
                chosen_ord = 0
                while chosen_ord in forbidden:
                    chosen_ord += 1
                prev = chr(chosen_ord + ord('a'))

        return changes
```
```

</details>

<details>
<summary>partial attempt 6</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # After operations, we need a final string s such that for all i:
        # |ord(s[i]) - ord(s[i-1])| != 0 and != 1 (mod alphabet adjacency)
        # i.e., adjacent letters must differ by at least 2.
        #
        # We minimize number of positions changed from original word.

        n = len(word)
        w = [ord(c) - 97 for c in word]  # 0..25

        # dp[i][c] = min ops for prefix ending at position i with s[i] = c
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        dp[0] = [0 if c == w[0] else 1 for c in range(26)]

        def ok(prev, cur):
            return abs(prev - cur) >= 2  # different and not adjacent in alphabet

        for i in range(1, n):
            cost = [0 if c == w[i] else 1 for c in range(26)]
            for cur in range(26):
                best = INF
                # Try all prev; n<=100 so 26*26 per step is fine.
                for prev in range(26):
                    if ok(prev, cur):
                        val = dp[i - 1][prev]
                        if val < best:
                            best = val
                dp[i][cur] = best + cost[cur]

        return min(dp[n - 1])
```
```

</details>

<details>
<summary>partial attempt 7</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # DP over the processed prefix.
        # Let dp[c] = minimum operations so far where the last kept character is c (0..25).
        # We rebuild the string by deciding each position's final character.
        n = len(word)
        INF = 10**9
        dp = [INF] * 26

        # Initialize with first character
        for c in range(26):
            dp[c] = 0 if ord(word[0]) - 97 == c else 1

        for i in range(1, n):
            ndp = [INF] * 26
            orig = ord(word[i]) - 97
            for prev in range(26):
                if dp[prev] == INF:
                    continue
                # Choose current character cur such that it is NOT almost-equal to prev
                # almost-equal means cur == prev or |cur-prev| == 1
                for cur in range(26):
                    if cur == prev or abs(cur - prev) == 1:
                        continue
                    cost = 0 if cur == orig else 1
                    if dp[prev] + cost < ndp[cur]:
                        ndp[cur] = dp[prev] + cost
            dp = ndp

        return min(dp)
```
```

</details>

<details>
<summary>partial attempt 8</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)

        # almost-equal means: equal OR adjacent in alphabet
        # We'll greedily fix any "bad" adjacent pair (i-1, i)
        # by changing word[i] to the smallest possible letter that breaks
        # the relation with both neighbors (i-1 and i+1 not yet fixed,
        # but we only need to ensure current pair (i-1,i) is fixed).
        #
        # Greedy works because the condition is local (adjacent pairs only):
        # once we fix a[i] to be safe w.r.t. a[i-1], the earlier part
        # never changes again.
        #
        # For the best minimum, we should avoid changing when already safe.

        def is_bad(a: str, b: str) -> bool:
            if a == b:
                return True
            return abs(ord(a) - ord(b)) == 1

        # Use a mutable list for the working string
        s = list(word)
        ops = 0

        for i in range(1, n):
            if is_bad(s[i - 1], s[i]):
                # Need to change s[i]
                # Choose a letter c such that:
                # 1) not almost-equal with s[i-1]
                prev = s[i - 1]
                for code in range(26):
                    c = chr(ord('a') + code)
                    if not is_bad(prev, c):
                        s[i] = c
                        ops += 1
                        break

        # Note: With this greedy, it suffices because only adjacent pairs matter.
        # Changing s[i] might create a bad pair with s[i+1], but that will be handled
        # when we reach i+1.
        return ops
```
```

</details>

<details>
<summary>partial attempt 9</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        arr = [ord(c) - 97 for c in word]  # 0..25

        # dp[i][c] = min operations after fixing position i to letter c,
        # while ensuring no adjacent almost-equal characters.
        INF = 10**9
        dp = [ [INF]*26 for _ in range(n) ]

        # allowed transitions:
        # adjacent letters must NOT be equal and NOT consecutive in alphabet.
        def ok(prev, cur):
            return prev != cur and abs(prev - cur) != 1

        for c in range(26):
            dp[0][c] = (0 if c == arr[0] else 1)

        for i in range(1, n):
            for cur in range(26):
                cost = 0 if cur == arr[i] else 1
                best = INF
                # prev can be any except {cur-1, cur, cur+1}
                for prev in range(26):
                    if ok(prev, cur):
                        val = dp[i-1][prev]
                        if val < best:
                            best = val
                dp[i][cur] = best + cost

        return min(dp[n-1])
```
```

</details>

### Parsed Memory Items

1. Constraint-Driven DP with Minimal State
Description: When forbidden relationships are local (e.g., only between adjacent items), build a DP whose state stores just enough history to enforce that locality.
<details>
<summary>Content 1</summary>

```text
Represent the processed prefix by the last chosen character (or another minimal boundary variable). For each new position, iterate candidates for the current choice and allow transitions only if they don’t violate the local constraint with the previous state. Add the per-position cost (keep vs change) and take minima over all states to ensure global optimality.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
The correct solutions use a DP formulation where the local constraint (adjacent characters being forbidden when “almost-equal”) is enforced via the last chosen character/state. Failures in the “partially correct” and “unsuccessful-looking” attempts stem from common issues: (1) incorrect re-encoding of the constraint using the wrong inequality (e.g., mixing “not almost-equal” with “distance >= 2” but then accidentally using “not almost-equal” incorrectly, or computing transitions with equality/adjacency conditions mis-specified), (2) greedy choices that ignore future interactions—since changing a character can create new violations with its right neighbor, greedy “fix-now” strategies are not provably optimal without full optimal substructure, and (3) DP indexing/initialization errors that make the state represent the wrong position (some attempts use different dimensions or base cases inconsistently, which can silently break correctness even if transitions seem plausible). The successful approach is consistent: represent the minimal future-relevant information as the last chosen character, then minimize edit cost with transitions filtered by the constraint, finishing with min over terminal states.
```

</details>

2. Reformulate “Almost-Equal” Precisely into a Transition Predicate
Description: Convert informal relation definitions into an explicit, reusable predicate function before implementing transitions.
<details>
<summary>Content 2</summary>

```text
Define almost-equal using an exact algebraic condition (e.g., equality OR alphabet adjacency) and then derive the allowed transition as its negation. This avoids subtle sign mistakes like using the wrong distance threshold or using an inequality that includes/excludes the wrong cases. After coding, mentally verify the predicate on boundary scenarios (same letter, neighboring letters, far letters).
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
The correct solutions use a DP formulation where the local constraint (adjacent characters being forbidden when “almost-equal”) is enforced via the last chosen character/state. Failures in the “partially correct” and “unsuccessful-looking” attempts stem from common issues: (1) incorrect re-encoding of the constraint using the wrong inequality (e.g., mixing “not almost-equal” with “distance >= 2” but then accidentally using “not almost-equal” incorrectly, or computing transitions with equality/adjacency conditions mis-specified), (2) greedy choices that ignore future interactions—since changing a character can create new violations with its right neighbor, greedy “fix-now” strategies are not provably optimal without full optimal substructure, and (3) DP indexing/initialization errors that make the state represent the wrong position (some attempts use different dimensions or base cases inconsistently, which can silently break correctness even if transitions seem plausible). The successful approach is consistent: represent the minimal future-relevant information as the last chosen character, then minimize edit cost with transitions filtered by the constraint, finishing with min over terminal states.
```

</details>

3. Greedy Fix-Local Strategy Requires Proof; DP Usually Wins
Description: Local greedy repairs can fail when changing an element affects constraints at the next boundary, so prefer DP unless optimality is proven.
<details>
<summary>Content 3</summary>

```text
If an operation at position i can create or remove violations with position i+1, a strategy that only ensures the current pair is valid may block better global solutions later. Unless you can prove that the greedy choice never reduces future options (a strong exchange argument), use DP with optimal substructure to guarantee correctness.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
The correct solutions use a DP formulation where the local constraint (adjacent characters being forbidden when “almost-equal”) is enforced via the last chosen character/state. Failures in the “partially correct” and “unsuccessful-looking” attempts stem from common issues: (1) incorrect re-encoding of the constraint using the wrong inequality (e.g., mixing “not almost-equal” with “distance >= 2” but then accidentally using “not almost-equal” incorrectly, or computing transitions with equality/adjacency conditions mis-specified), (2) greedy choices that ignore future interactions—since changing a character can create new violations with its right neighbor, greedy “fix-now” strategies are not provably optimal without full optimal substructure, and (3) DP indexing/initialization errors that make the state represent the wrong position (some attempts use different dimensions or base cases inconsistently, which can silently break correctness even if transitions seem plausible). The successful approach is consistent: represent the minimal future-relevant information as the last chosen character, then minimize edit cost with transitions filtered by the constraint, finishing with min over terminal states.
```

</details>

4. Cost Modeling Must Match the State’s Meaning
Description: Ensure the DP’s transition cost (keep/change) is computed against the same “current choice” the state represents.
<details>
<summary>Content 4</summary>

```text
A common source of bugs is computing the edit cost for the wrong index/variable (e.g., comparing against the previous state instead of the candidate current character). Tie the cost directly to the candidate letter chosen for that position and accumulate it in dp[i][state] so the final minimization over terminal states is meaningful.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
The correct solutions use a DP formulation where the local constraint (adjacent characters being forbidden when “almost-equal”) is enforced via the last chosen character/state. Failures in the “partially correct” and “unsuccessful-looking” attempts stem from common issues: (1) incorrect re-encoding of the constraint using the wrong inequality (e.g., mixing “not almost-equal” with “distance >= 2” but then accidentally using “not almost-equal” incorrectly, or computing transitions with equality/adjacency conditions mis-specified), (2) greedy choices that ignore future interactions—since changing a character can create new violations with its right neighbor, greedy “fix-now” strategies are not provably optimal without full optimal substructure, and (3) DP indexing/initialization errors that make the state represent the wrong position (some attempts use different dimensions or base cases inconsistently, which can silently break correctness even if transitions seem plausible). The successful approach is consistent: represent the minimal future-relevant information as the last chosen character, then minimize edit cost with transitions filtered by the constraint, finishing with min over terminal states.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
The correct solutions use a DP formulation where the local constraint (adjacent characters being forbidden when “almost-equal”) is enforced via the last chosen character/state. Failures in the “partially correct” and “unsuccessful-looking” attempts stem from common issues: (1) incorrect re-encoding of the constraint using the wrong inequality (e.g., mixing “not almost-equal” with “distance >= 2” but then accidentally using “not almost-equal” incorrectly, or computing transitions with equality/adjacency conditions mis-specified), (2) greedy choices that ignore future interactions—since changing a character can create new violations with its right neighbor, greedy “fix-now” strategies are not provably optimal without full optimal substructure, and (3) DP indexing/initialization errors that make the state represent the wrong position (some attempts use different dimensions or base cases inconsistently, which can silently break correctness even if transitions seem plausible). The successful approach is consistent: represent the minimal future-relevant information as the last chosen character, then minimize edit cost with transitions filtered by the constraint, finishing with min over terminal states.
</reasoning>
<memories>
<memory>
<title>Constraint-Driven DP with Minimal State</title>
<description>When forbidden relationships are local (e.g., only between adjacent items), build a DP whose state stores just enough history to enforce that locality.</description>
<content>Represent the processed prefix by the last chosen character (or another minimal boundary variable). For each new position, iterate candidates for the current choice and allow transitions only if they don’t violate the local constraint with the previous state. Add the per-position cost (keep vs change) and take minima over all states to ensure global optimality.</content>
</memory>
<memory>
<title>Reformulate “Almost-Equal” Precisely into a Transition Predicate</title>
<description>Convert informal relation definitions into an explicit, reusable predicate function before implementing transitions.</description>
<content>Define almost-equal using an exact algebraic condition (e.g., equality OR alphabet adjacency) and then derive the allowed transition as its negation. This avoids subtle sign mistakes like using the wrong distance threshold or using an inequality that includes/excludes the wrong cases. After coding, mentally verify the predicate on boundary scenarios (same letter, neighboring letters, far letters).</content>
<memory>
<title>Greedy Fix-Local Strategy Requires Proof; DP Usually Wins</title>
<description>Local greedy repairs can fail when changing an element affects constraints at the next boundary, so prefer DP unless optimality is proven.</description>
<content>If an operation at position i can create or remove violations with position i+1, a strategy that only ensures the current pair is valid may block better global solutions later. Unless you can prove that the greedy choice never reduces future options (a strong exchange argument), use DP with optimal substructure to guarantee correctness.</content>
</memory>
<memory>
<title>Cost Modeling Must Match the State’s Meaning</title>
<description>Ensure the DP’s transition cost (keep/change) is computed against the same “current choice” the state represents.</description>
<content>A common source of bugs is computing the edit cost for the wrong index/variable (e.g., comparing against the previous state instead of the candidate current character). Tie the cost directly to the candidate letter chosen for that position and accumulate it in dp[i][state] so the final minimization over terminal states is meaningful.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `0.1000`
- Augmented pass@1: `0.0000`
- Improvement: `-0.1000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
You are given a 0-indexed string word.
In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.
Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.
Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.
 
Example 1:

Input: word = "aaaaa"
Output: 2
Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.

Example 2:

Input: word = "abddez"
Output: 2
Explanation: We can change word into "ybdoez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
Example 3:

Input: word = "zyxyxyz"
Output: 3
Explanation: We can change word into "zaxaxaz" which does not have any adjacent almost-equal characters. 
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.

 
Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # DP over positions with the last chosen character (0..25)
        n = len(word)
        INF = 10**9
        # dp_prev[c] = min operations up to i with chosen last char = c
        dp_prev = [INF] * 26

        # Initialize for i = 0
        w0 = ord(word[0]) - 97
        for c in range(26):
            dp_prev[c] = 0 if c == w0 else 1

        for i in range(1, n):
            w = ord(word[i]) - 97
            dp_cur = [INF] * 26
            for c in range(26):  # chosen current char
                cost = 0 if c == w else 1
                # previous char p allowed if not almost-equal with c:
                # disallowed: p == c or abs(p-c) == 1
                best = INF
                for p in range(26):
                    if p == c or abs(p - c) == 1:
                        continue
                    if dp_prev[p] < best:
                        best = dp_prev[p]
                dp_cur[c] = best + cost
            dp_prev = dp_cur

        return min(dp_prev)
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        INF = 10**9

        # almost-equal means |a-b| <= 1 in alphabet order
        def ok(prev, cur):
            if prev is None:
                return True
            d = abs(ord(prev) - ord(cur))
            return d > 1

        # dp[i][c] = min operations for prefix ending at position i with letter c at i,
        # where c is a lowercase letter (0..25).
        dp = [INF] * 26
        for c in range(26):
            dp[c] = 0 if ord(word[0]) - 97 == c else 1

        for i in range(1, n):
            ndp = [INF] * 26
            for pc in range(26):
                if dp[pc] >= INF:
                    continue
                for c in range(26):
                    # must not be almost-equal with previous character
                    if abs(pc - c) <= 1:
                        continue
                    cost = 0 if ord(word[i]) - 97 == c else 1
                    val = dp[pc] + cost
                    if val < ndp[c]:
                        ndp[c] = val
            dp = ndp

        return min(dp)
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        def almost_equal(a: str, b: str) -> bool:
            return abs(ord(a) - ord(b)) <= 1  # adjacent in alphabet or equal

        n = len(word)
        # dp[i][c] = min ops to make prefix up to i (inclusive) valid
        # and set word[i] to letter c, where c is 0..25
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n)]
        for c in range(26):
            dp[0][c] = 0 if word[0] == chr(ord('a') + c) else 1

        for i in range(1, n):
            for c in range(26):
                cur = dp[i][c]
                if cur >= INF:
                    pass
                add = 0 if word[i] == chr(ord('a') + c) else 1
                cur_best = INF
                # transition from previous letter p that is NOT almost-equal to c
                for p in range(26):
                    if dp[i - 1][p] >= INF:
                        continue
                    # p and c must NOT be almost-equal
                    if abs(p - c) <= 1:
                        continue
                    cur_best = min(cur_best, dp[i - 1][p] + add)
                dp[i][c] = cur_best

        return min(dp[n - 1])
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # adjacent characters can only be "equal" or "alphabet-adjacent"
        # We need min operations to make every adjacent pair not almost-equal.
        # Greedy: keep a character if possible; otherwise change it.
        def ok(a: str, b: str) -> bool:
            return not (a == b or abs(ord(a) - ord(b)) == 1)

        n = len(word)
        # dp[i][c] = min ops up to position i with kept final letter c at i
        # We'll only ever need consider 26 letters.
        INF = 10**9
        prev = [INF] * 26

        # initialize for i=0
        for c in range(26):
            letter = chr(ord('a') + c)
            prev[c] = 0 if word[0] == letter else 1

        for i in range(1, n):
            cur = [INF] * 26
            for c in range(26):
                letter_c = chr(ord('a') + c)
                add = 0 if word[i] == letter_c else 1
                # choose previous kept letter p such that (p, c) is not almost-equal
                # scan all 26 previous letters (n<=100 so 26^2*100 is fine)
                best = INF
                for p in range(26):
                    if prev[p] == INF:
                        continue
                    letter_p = chr(ord('a') + p)
                    if ok(letter_p, letter_c):
                        best = min(best, prev[p])
                cur[c] = best + add
            prev = cur

        return min(prev)
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        # Minimum operations via DP over positions and chosen resulting last character.
        # We build a final string with no adjacent almost-equal characters:
        # forbidden if abs(a-b) <= 1 in alphabet (including equal).
        # i.e., for letters x, next letter y must satisfy |x-y| >= 2.
        INF = 10**9
        dp = [INF] * 26  # dp[c] = min ops up to current index with last chosen char = c
        for c in range(26):
            dp[c] = 0 if ord(word[0]) - 97 == c else 1

        for i in range(1, n):
            newdp = [INF] * 26
            for prev in range(26):
                if dp[prev] >= INF:
                    continue
                # next must have |prev-next| >= 2
                for nxt in range(26):
                    if abs(prev - nxt) >= 2:
                        cost = 0 if (ord(word[i]) - 97) == nxt else 1
                        v = dp[prev] + cost
                        if v < newdp[nxt]:
                            newdp[nxt] = v
            dp = newdp

        return min(dp)
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)

        # Two adjacent chars are "almost-equal" if they are equal or adjacent in alphabet.
        # If we scan left to right, keeping a chosen character for position i-1,
        # we can determine the minimum replacements for i.
        #
        # Since we can change each position independently, the optimal strategy is:
        # choose for each position either keep the original char or replace it with
        # some char that avoids being almost-equal with previous kept/replaced char.
        #
        # We can do DP where state is the previous character choice.
        # However alphabet size is 26, word length <= 100 -> 2600 states is fine.
        ALPH = 26
        INF = 10**9

        # dp[c] = min operations up to current index-1 with previous char = c (0..25)
        dp = [INF] * ALPH

        # initialize for index 0
        first = ord(word[0]) - 97
        for c in range(ALPH):
            dp[c] = 0 if c == first else 1

        def almost_equal(x, y):
            return x == y or abs(x - y) == 1

        for i in range(1, n):
            ndp = [INF] * ALPH
            orig = ord(word[i]) - 97
            for prev_c in range(ALPH):
                if dp[prev_c] >= INF:
                    continue
                # choose current character cur_c
                for cur_c in range(ALPH):
                    if almost_equal(prev_c, cur_c):
                        continue
                    cost = 0 if cur_c == orig else 1
                    if dp[prev_c] + cost < ndp[cur_c]:
                        ndp[cur_c] = dp[prev_c] + cost
            dp = ndp

        return min(dp)
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        # Allowed: for every adjacent pair (i-1, i), final chars must NOT be:
        # equal, or consecutive in alphabet (diff == 1).
        # We choose target letters to minimize number of positions changed.
        #
        # DP over positions with state being chosen letter at current position.
        # alphabet size = 26, n <= 100 => O(n*26*26) is fine.
        A = 26
        INF = 10**9

        def ok(prev_c: int, cur_c: int) -> bool:
            # prev and cur are "almost-equal" iff same or adjacent in alphabet
            diff = abs(prev_c - cur_c)
            return not (diff == 0 or diff == 1)

        # dp[i][c] = min changes up to i with word[i] set to letter c
        # Use rolling arrays.
        dp = [INF] * A
        for c in range(A):
            dp[c] = 0 if ord(word[0]) - 97 == c else 1

        for i in range(1, n):
            ndp = [INF] * A
            orig = ord(word[i]) - 97
            for c in range(A):
                change_cost = 0 if c == orig else 1
                best = INF
                # transition from prev letter p where ok(p,c)
                for p in range(A):
                    if dp[p] < INF and ok(p, c):
                        v = dp[p] + change_cost
                        if v < best:
                            best = v
                ndp[c] = best
            dp = ndp

        return min(dp)
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ans = 0

        def almost_equal(a: str, b: str) -> bool:
            return a == b or abs(ord(a) - ord(b)) == 1

        for i in range(n - 1):
            if i > 0 and almost_equal(word[i], word[i - 1]):
                # The previous position is already in a bad relation with current,
                # but only the current index can be changed to fix adjacency with i-1.
                # We'll still handle the i-1,i adjacency below.
                pass

            if almost_equal(word[i], word[i + 1]):
                # Change word[i+1] to something that is NOT almost-equal to word[i]
                # and also attempt to be safe w.r.t word[i+2] when possible.
                x = word[i]
                # Prefer a letter far from x to avoid creating new almost-equal issues.
                # If possible, choose one with minimal conflict with x.
                best = None
                for c in range(26):
                    ch = chr(ord('a') + c)
                    if not almost_equal(x, ch):
                        if i + 2 < n and almost_equal(ch, word[i + 2]):
                            # avoid if it would also conflict with next original char
                            continue
                        best = ch
                        break
                if best is None:
                    # fallback: just pick any letter not almost-equal to x
                    for c in range(26):
                        ch = chr(ord('a') + c)
                        if not almost_equal(x, ch):
                            best = ch
                            break

                # apply the change logically by updating word[i+1]
                word = word[:i + 1] + best + word[i + 2:]
                ans += 1

        return ans
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        # dp[i][c] = min ops to process prefix up to i (0..i-1),
        # with resulting word[i-1] == chr(c)
        # c in 0..25 for 'a'..'z'
        INF = 10**9
        dp = [[INF] * 26 for _ in range(n + 1)]
        # No previous character for i=0; start by setting cost at position 0 freely.
        for c in range(26):
            orig = ord(word[0]) - 97
            dp[1][c] = 0 if c == orig else 1

        # Adjacent almost-equal constraint:
        # prev char x and curr char y are forbidden if y == x or abs(y-x) == 1
        for i in range(1, n):
            orig_i = ord(word[i]) - 97
            for prev in range(26):
                best = dp[i][prev]
                if best >= INF:
                    continue
                # curr can be any letter not almost-equal to prev
                for curr in range(26):
                    if curr == prev or abs(curr - prev) == 1:
                        continue
                    cost = best + (0 if curr == orig_i else 1)
                    if cost < dp[i + 1][curr]:
                        dp[i + 1][curr] = cost

        return min(dp[n])
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # We greedily build a final string by choosing, for each position i,
        # the smallest possible letter that is NOT almost-equal to the previous letter.
        # If the original character already works, we keep it (0 cost),
        # otherwise we change it (1 cost). This greedy is optimal because
        # costs are independent per position except for the constraint with
        # the immediate previous character.
        #
        # Almost-equal means letters differ by at most 1 in alphabet,
        # i.e., abs(a-b) <= 1.
        
        prev = None
        ops = 0

        for ch in word:
            cur = ord(ch) - 97
            if prev is None:
                prev = cur
                continue

            # Check if keeping cur violates adjacency almost-equal with prev.
            if abs(cur - prev) <= 1:
                # Need to pick some letter x such that abs(x - prev) > 1.
                # To minimize future issues, pick the closest valid letter.
                # If prev is p, valid x are [0..p-2] U [p+2..25].
                # Choose smallest valid.
                p = prev
                if p >= 2:
                    x = 0  # smallest in [0..p-2]
                else:
                    x = 3  # since p in {0,1}, smallest in [p+2..] is 3 or 2
                    # More precisely:
                    # if p==0 => p+2=2 => smallest is 2
                    # if p==1 => p+2=3 => smallest is 3
                    x = 2 if p == 0 else 3
                ops += 1
                prev = x
            else:
                prev = cur

        return ops
```
```

</details>

#### Baseline Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.2000 | `partial` |
| 1 | 0.2000 | `partial` |
| 2 | 0.2000 | `partial` |
| 3 | 0.2000 | `partial` |
| 4 | 0.2000 | `partial` |
| 5 | 0.2000 | `partial` |
| 6 | 0.2000 | `partial` |
| 7 | 1.0000 | `full` |
| 8 | 0.2000 | `partial` |
| 9 | 0.8000 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 1</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 2</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 3</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 4</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 5</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 6</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
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
      "expected": "49",
      "actual": "49",
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
      "expected": "25",
      "actual": "25",
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
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 9</summary>

```json
{
  "passed": 12,
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
      "passed": false,
      "expected": "49",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "50",
      "actual": "50",
      "error": ""
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "43",
      "error": "Wrong Answer"
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

  1. Constraint-Driven DP with Minimal State: When forbidden relationships are local (e.g., only between adjacent items), build a DP whose state stores just enough history to enforce that locality.
     Represent the processed prefix by the last chosen character (or another minimal boundary variable). For each new position, iterate candidates for the current choice and allow transitions only if they don’t violate the local constraint with the previous state. Add the per-position cost (keep vs change) and take minima over all states to ensure global optimality.
  2. Reformulate “Almost-Equal” Precisely into a Transition Predicate: Convert informal relation definitions into an explicit, reusable predicate function before implementing transitions.
     Define almost-equal using an exact algebraic condition (e.g., equality OR alphabet adjacency) and then derive the allowed transition as its negation. This avoids subtle sign mistakes like using the wrong distance threshold or using an inequality that includes/excludes the wrong cases. After coding, mentally verify the predicate on boundary scenarios (same letter, neighboring letters, far letters).
  3. Greedy Fix-Local Strategy Requires Proof; DP Usually Wins: Local greedy repairs can fail when changing an element affects constraints at the next boundary, so prefer DP unless optimality is proven.
     If an operation at position i can create or remove violations with position i+1, a strategy that only ensures the current pair is valid may block better global solutions later. Unless you can prove that the greedy choice never reduces future options (a strong exchange argument), use DP with optimal substructure to guarantee correctness.
  4. Cost Modeling Must Match the State’s Meaning: Ensure the DP’s transition cost (keep/change) is computed against the same “current choice” the state represents.
     A common source of bugs is computing the edit cost for the wrong index/variable (e.g., comparing against the previous state instead of the candidate current character). Tie the cost directly to the candidate letter chosen for that position and accumulate it in dp[i][state] so the final minimization over terminal states is meaningful.

Apply these insights to the problem below.

### Question:
You are given a 0-indexed string word.
In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.
Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.
Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.
 
Example 1:

Input: word = "aaaaa"
Output: 2
Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.

Example 2:

Input: word = "abddez"
Output: 2
Explanation: We can change word into "ybdoez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
Example 3:

Input: word = "zyxyxyz"
Output: 3
Explanation: We can change word into "zaxaxaz" which does not have any adjacent almost-equal characters. 
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.

 
Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Augmented generation 1</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        INF = 10**9
        letters = [chr(ord('a') + i) for i in range(26)]

        # almost-equal: same OR adjacent in alphabet (distance 1)
        def almost_equal(a: str, b: str) -> bool:
            ia, ib = ord(a) - 97, ord(b) - 97
            return ia == ib or abs(ia - ib) == 1

        # DP: dp[i][c] = min operations for prefix up to i with word[i] == c
        # Transition enforces that word[i-1] and word[i] are NOT almost-equal.
        dp = [INF] * 26
        for c in range(26):
            dp[c] = 0 if word[0] == letters[c] else 1

        for i in range(1, n):
            ndp = [INF] * 26
            for cur in range(26):
                cost = 0 if word[i] == letters[cur] else 1
                best_prev = INF
                for prev in range(26):
                    if not (prev == cur or abs(prev - cur) == 1):
                        if dp[prev] < best_prev:
                            best_prev = dp[prev]
                ndp[cur] = best_prev + cost
            dp = ndp

        return min(dp)
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ALPHA = 26
        INF = 10**9

        # almost_equal: a==b or |a-b|==1 in alphabet (adjacent letters)
        def almost_equal(c1: int, c2: int) -> bool:
            return c1 == c2 or abs(c1 - c2) == 1

        # dp_prev[prev_char] = min operations up to i-1 ending with prev_char at position i-1
        # We'll build dp_curr for position i choosing curr_char.
        dp_prev = [INF] * ALPHA
        for ch in range(ALPHA):
            dp_prev[ch] = 0 if ch == (ord(word[0]) - 97) else 1

        for i in range(1, n):
            dp_curr = [INF] * ALPHA
            orig = ord(word[i]) - 97
            for prev_ch in range(ALPHA):
                best = dp_prev[prev_ch]
                if best >= INF:
                    continue
                # choose current char curr_ch
                for curr_ch in range(ALPHA):
                    # Allowed iff not almost-equal with previous chosen character
                    if almost_equal(prev_ch, curr_ch):
                        continue
                    cost = 0 if curr_ch == orig else 1
                    val = best + cost
                    if val < dp_curr[curr_ch]:
                        dp_curr[curr_ch] = val
            dp_prev = dp_curr

        return min(dp_prev)
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        INF = 10**9

        def almost_equal(a: int, b: int) -> bool:
            # a and b are almost-equal if same or adjacent in alphabet
            return a == b or abs(a - b) == 1

        # dp[i][c] = min ops for prefix up to i (inclusive),
        # with word[i] set to character c (0..25),
        # and no adjacent almost-equal characters within the prefix.
        dp = [[INF] * 26 for _ in range(n)]
        for c in range(26):
            dp[0][c] = 0 if c == ord(word[0]) - 97 else 1

        for i in range(1, n):
            orig = ord(word[i]) - 97
            for c in range(26):
                cost = 0 if c == orig else 1
                best_prev = INF
                for p in range(26):
                    if not almost_equal(p, c):
                        if dp[i - 1][p] < best_prev:
                            best_prev = dp[i - 1][p]
                dp[i][c] = best_prev + cost

        return min(dp[n - 1])
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        INF = 10**9

        # almost-equal: same or adjacent in alphabet
        def almost_equal(a: str, b: str) -> bool:
            ia, ib = ord(a) - 97, ord(b) - 97
            return ia == ib or abs(ia - ib) == 1

        # dp[i][c] = min operations for prefix word[:i+1] if we set word[i] to char with index c
        # c in [0..25]
        dp = [INF] * 26

        # initialize i=0
        w0 = word[0]
        for c in range(26):
            dp[c] = 0 if c == ord(w0) - 97 else 1

        for i in range(1, n):
            ndp = [INF] * 26
            wi = ord(word[i]) - 97
            for prev_c in range(26):
                if dp[prev_c] >= INF:
                    continue
                prev_ch = chr(prev_c + 97)
                # choose current character cur_c
                for cur_c in range(26):
                    cur_ch = chr(cur_c + 97)
                    if almost_equal(prev_ch, cur_ch):
                        continue
                    cost = 0 if cur_c == wi else 1
                    val = dp[prev_c] + cost
                    if val < ndp[cur_c]:
                        ndp[cur_c] = val
            dp = ndp

        return min(dp)
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        """
        DP over minimal state: only need the last chosen character to enforce that
        no adjacent pair is almost-equal.
        Cost model: cost is 1 if we change word[i] to candidate char, else 0.
        """
        n = len(word)
        alphabet = [chr(ord('a') + i) for i in range(26)]

        # predicate: almost-equal => equal OR adjacent in alphabet
        def almost_equal(a: str, b: str) -> bool:
            if a == b:
                return True
            return abs(ord(a) - ord(b)) == 1

        INF = 10**9
        # dp_prev[last_char_index] = min operations up to position i-1 ending with that last char
        dp_prev = [INF] * 26

        # Initialize for i = 0
        w0 = word[0]
        for c_idx, c in enumerate(alphabet):
            dp_prev[c_idx] = 0 if c == w0 else 1

        # Transition for i >= 1
        for i in range(1, n):
            wi = word[i]
            dp_cur = [INF] * 26
            for prev_idx in range(26):
                prev_cost = dp_prev[prev_idx]
                if prev_cost >= INF:
                    continue
                prev_c = alphabet[prev_idx]
                for cur_idx in range(26):
                    cur_c = alphabet[cur_idx]
                    if almost_equal(prev_c, cur_c):
                        continue
                    add_cost = 0 if cur_c == wi else 1
                    new_cost = prev_cost + add_cost
                    if new_cost < dp_cur[cur_idx]:
                        dp_cur[cur_idx] = new_cost
            dp_prev = dp_cur

        return min(dp_prev)
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ALPH = [chr(ord('a') + i) for i in range(26)]

        # almost-equal: same or adjacent in alphabet
        def almost_equal(a: str, b: str) -> bool:
            ia = ord(a) - 97
            ib = ord(b) - 97
            return ia == ib or abs(ia - ib) == 1

        INF = 10**9
        # dp_prev[j] = min ops up to position i-1 if word[i-1] becomes ALPH[j]
        dp_prev = [0] * 26

        # Initialize for i = 0
        for j in range(26):
            dp_prev[j] = 0 if word[0] == ALPH[j] else 1

        for i in range(1, n):
            dp_cur = [INF] * 26
            for prev_j in range(26):
                prev_char = ALPH[prev_j]
                base = dp_prev[prev_j]
                # Try choose current char
                for cur_j in range(26):
                    cur_char = ALPH[cur_j]
                    if not almost_equal(prev_char, cur_char):
                        cost = 0 if word[i] == cur_char else 1
                        val = base + cost
                        if val < dp_cur[cur_j]:
                            dp_cur[cur_j] = val
            dp_prev = dp_cur

        return min(dp_prev)
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        INF = 10**9

        # almost_equal(a,b) <=> a==b or adjacent in alphabet (|pos diff|==1)
        # Allowed transition requires NOT almost_equal with previous chosen char.
        def bad(prev_c: str, cur_c: str) -> bool:
            pa = ord(prev_c) - 97
            pc = ord(cur_c) - 97
            return abs(pa - pc) <= 1  # includes equality and adjacent alphabet letters

        # dp_prev[prev_letter_index] = min operations up to i with last chosen letter = prev_letter
        dp_prev = [INF] * 26

        # Initialize for i=0
        first = word[0]
        for cur in range(26):
            ch = chr(cur + 97)
            dp_prev[cur] = 0 if ch == first else 1

        for i in range(1, n):
            dp_cur = [INF] * 26
            orig = word[i]
            for prev in range(26):
                base = dp_prev[prev]
                if base >= INF:
                    continue
                prev_c = chr(prev + 97)
                for cur in range(26):
                    cur_c = chr(cur + 97)
                    if bad(prev_c, cur_c):
                        continue
                    cost = 0 if cur_c == orig else 1
                    val = base + cost
                    if val < dp_cur[cur]:
                        dp_cur[cur] = val
            dp_prev = dp_cur

        return min(dp_prev)
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        INF = 10**9

        # almost-equal: same letter OR alphabet-adjacent (diff == 1)
        def almost_eq(a: int, b: int) -> bool:
            return a == b or abs(a - b) == 1

        # dp[c] = min operations for processed prefix where last chosen char is c
        dp = [INF] * 26
        # initialize with first character choice
        orig0 = ord(word[0]) - 97
        for c in range(26):
            dp[c] = 0 if c == orig0 else 1

        for i in range(1, n):
            orig = ord(word[i]) - 97
            newdp = [INF] * 26
            for prev in range(26):
                best_prev = dp[prev]
                if best_prev >= INF:
                    continue
                for cur in range(26):
                    # Need to avoid adjacent almost-equal => NOT almost_eq(prev, cur)
                    if not almost_eq(prev, cur):
                        cost = 0 if cur == orig else 1
                        val = best_prev + cost
                        if val < newdp[cur]:
                            newdp[cur] = val
            dp = newdp

        return min(dp)
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        INF = 10**9

        # almost_equal(a, b) <=> a == b or adjacent in alphabet
        # Allowed adjacent pair iff NOT almost_equal.
        def allowed(prev_c: int, cur_c: int) -> bool:
            return abs(prev_c - cur_c) > 1

        # DP over positions with minimal state: last chosen character.
        # dp[c] = min ops to make processed prefix end with character c (0..25)
        dp = [INF] * 26
        for c in range(26):
            dp[c] = 0 if word[0] == chr(ord('a') + c) else 1

        for i in range(1, n):
            ndp = [INF] * 26
            orig = ord(word[i]) - ord('a')
            for cur in range(26):
                cost = 0 if cur == orig else 1
                best = INF
                for prev in range(26):
                    if allowed(prev, cur):
                        if dp[prev] < best:
                            best = dp[prev]
                ndp[cur] = best + cost
            dp = ndp

        return min(dp)
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ALPH = 26
        INF = 10**9

        def almost_equal(a_idx: int, b_idx: int) -> bool:
            # almost-equal iff same or alphabet-adjacent
            return a_idx == b_idx or abs(a_idx - b_idx) == 1

        # dp[c] = min ops for processed prefix where last chosen char is c
        dp = [INF] * ALPH
        first = ord(word[0]) - ord('a')
        for c in range(ALPH):
            dp[c] = 0 if c == first else 1

        for i in range(1, n):
            ndp = [INF] * ALPH
            cur_orig = ord(word[i]) - ord('a')
            for prev in range(ALPH):
                if dp[prev] == INF:
                    continue
                # current candidate c must not be almost-equal with prev
                for c in range(ALPH):
                    if almost_equal(prev, c):
                        continue
                    cost = 0 if c == cur_orig else 1
                    val = dp[prev] + cost
                    if val < ndp[c]:
                        ndp[c] = val
            dp = ndp

        return min(dp)
```
```

</details>

#### Augmented Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.2000 | `partial` |
| 1 | 0.2000 | `partial` |
| 2 | 0.2000 | `partial` |
| 3 | 0.2000 | `partial` |
| 4 | 0.2000 | `partial` |
| 5 | 0.2000 | `partial` |
| 6 | 0.2000 | `partial` |
| 7 | 0.2000 | `partial` |
| 8 | 0.2000 | `partial` |
| 9 | 0.2000 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 1</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 2</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 3</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 4</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 5</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 6</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 8</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 9</summary>

```json
{
  "passed": 3,
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
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Runtime Error: string index out of range"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "49",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "50",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>
