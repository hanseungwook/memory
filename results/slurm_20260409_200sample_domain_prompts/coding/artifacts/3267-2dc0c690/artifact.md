# Problem 3267

- Domain: `coding`

## Problem

```text
You are given a string s that consists of lowercase English letters.
A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.

Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.

Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.

 
Constraints:

3 <= s.length <= 50
s consists of only lowercase English letters.
```

### Starter Code

```python
class Solution:
    def maximumLength(self, s: str) -> int:
```

### Test Cases

```json
[
  {
    "input": "\"aaaa\"",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "\"abcdef\"",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "\"abcaba\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"vvv\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"ttt\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"yww\"",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "\"azd\"",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "\"tbr\"",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "\"ltac\"",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "\"fxdz\"",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "\"tgvjv\"",
    "output": "-1",
    "testtype": "functional"
  },
  {
    "input": "\"wqtaxohmdjrcykeeaxpbtavzjdpe\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"grnnnnnnnnnnnnnnnnnnndywsdesevvtmjhmrnnnnnnnnnnapz\"",
    "output": "17",
    "testtype": "functional"
  },
  {
    "input": "\"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedxdyvleqlmialrknr\"",
    "output": "31",
    "testtype": "functional"
  },
  {
    "input": "\"dzllllllllllllllllllllqordklowgscjqzjuoecfgrruwecw\"",
    "output": "18",
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
You are given a string s that consists of lowercase English letters.
A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.

Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.

Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.

 
Constraints:

3 <= s.length <= 50
s consists of only lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count maximum occurrences for each character length.
        # Since s length <= 50 and special substrings are just repeated single characters,
        # we can brute over possible lengths for each char.
        n = len(s)
        best = -1

        for ch in set(s):
            # Gather run lengths of this character in s
            run_lengths = []
            i = 0
            while i < n:
                if s[i] == ch:
                    j = i
                    while j < n and s[j] == ch:
                        j += 1
                    run_lengths.append(j - i)
                    i = j
                else:
                    i += 1

            # For a given length L, total number of occurrences of ch repeated L times
            # is sum over runs of max(0, run_len - L + 1). Need >= 3.
            # L cannot exceed max run length.
            max_run = max(run_lengths) if run_lengths else 0

            for L in range(1, max_run + 1):
                cnt = 0
                for r in run_lengths:
                    if r >= L:
                        cnt += r - L + 1
                    if cnt >= 3:
                        break
                if cnt >= 3:
                    best = max(best, L)

        return best
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Binary-search on length L; check if any single-character substring of length L
        # occurs at least 3 times (as contiguous blocks).
        n = len(s)

        # Precompute runs: (char, start, end_inclusive)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        # For a run of length len_run, how many substrings of length L consisting of the run's char?
        # For L <= len_run: occurrences = len_run - L + 1, else 0.
        def can(L: int) -> bool:
            if L <= 0:
                return True
            cnt = [0] * 26
            for ch, length in runs:
                if length >= L:
                    occurrences = length - L + 1
                    cnt[ord(ch) - 97] += occurrences
                    if cnt[ord(ch) - 97] >= 3:
                        return True
            return False

        # Maximum possible L is n, but practically <= n//? still safe to bound by n.
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans if ans != 0 else -1
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of each character at each possible run length.
        # A special substring is just one character repeated k times: "c"*k.
        # It occurs (as a substring) as many times as there are positions where a run of c's
        # has length >= k. For a run of length L, number of substrings "c"*k inside it is (L-k+1).
        n = len(s)
        best = -1

        for ch in set(s):
            runs = []
            i = 0
            while i < n:
                if s[i] != ch:
                    i += 1
                    continue
                j = i
                while j < n and s[j] == ch:
                    j += 1
                runs.append(j - i)
                i = j

            # For each k, total occurrences is sum over runs of max(0, L-k+1).
            # We need the maximum k such that total >= 3.
            maxL = max(runs) if runs else 0
            # Small constraints (n<=50) -> brute force k is fine.
            for k in range(1, maxL + 1):
                total = 0
                for L in runs:
                    if L >= k:
                        total += (L - k + 1)
                    if total >= 3:  # early stop
                        break
                if total >= 3:
                    if k > best:
                        best = k

        return best
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of runs of each character
        # For a special substring of length L consisting of char c to occur >= 3 times,
        # we need at least three positions of length-L windows inside occurrences.
        # In a run of length r, number of substrings of length L for that char is:
        #   max(0, r - L + 1)
        # We can binary search L and check feasibility.
        
        n = len(s)
        runs = {}
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ch = s[i]
            runs[ch] = runs.get(ch, []) + [j - i]
            i = j

        def can(L: int) -> bool:
            if L == 0:
                return True
            for ch_runs in runs.values():
                total = 0
                for r in ch_runs:
                    if r >= L:
                        total += r - L + 1
                        if total >= 3:
                            return True
            return False

        # Max possible L is n
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # For any special substring, it is just one character repeated.
        # If a character c appears in maximal consecutive block length L,
        # then it contributes substrings of length k (1<=k<=L).
        # Count how many times each length k appears for that character across all blocks:
        # occurrences for length k is sum over blocks of max(0, block_len - k + 1).
        # We need the maximum k such that some character has occurrences >= 3.
        
        n = len(s)
        blocks = []  # list of (char, block_length)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks.append((s[i], j - i))
            i = j

        # Maximum possible length is max block length, <= n.
        best = -1
        # We can compute for each character separately, since only 26 letters.
        for ch in range(26):
            c = chr(ord('a') + ch)
            lens = [L for (cc, L) in blocks if cc == c]
            if not lens:
                continue

            # For k from 1..maxLen, count occurrences:
            # occ(k) = sum(max(0, L - k + 1))
            maxLen = max(lens)
            # We can cap early: if total occurrences for k=1 < 3 => answer can't be >1.
            for k in range(1, maxLen + 1):
                occ = 0
                for L in lens:
                    if L >= k:
                        occ += L - k + 1
                        if occ >= 3:
                            best = max(best, k)
                            break

        return best
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # For a special substring, it is some character c repeated L times: c^L.
        # Any occurrence is fully contained within a maximal run of c's.
        # If the maximum run lengths for c are r1 >= r2 >= r3 ...
        # then the count of occurrences of c^L is:
        # sum over runs max(0, run_len - L + 1) >= 3
        # We can binary search the answer length for each L, but since |s|<=50,
        # brute over L and counts is simplest.

        n = len(s)
        # Collect run lengths for each character
        run_lens = [[] for _ in range(26)]
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            run_lens[ord(s[i]) - 97].append(j - i)
            i = j

        def exists(L: int) -> bool:
            if L <= 0:
                return True
            total_needed = 3
            for ch in range(26):
                cnt = 0
                for r in run_lens[ch]:
                    if r >= L:
                        cnt += r - L + 1
                        if cnt >= total_needed:
                            return True
            return False

        # Maximum possible length is at most max run length
        max_run = max((max(lst) for lst in run_lens if lst), default=0)
        ans = -1
        # L from high to low; small constraints allow O(26 * runs * n)
        for L in range(max_run, 0, -1):
            if exists(L):
                ans = L
                break
        return ans
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count consecutive occurrences for each character
        n = len(s)
        runs = [0] * 26
        # We need lengths of substrings made of a single repeated char.
        # For each char, collect all run lengths where it appears contiguously.
        char_runs = [[] for _ in range(26)]
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            k = ord(s[i]) - 97
            char_runs[k].append(j - i)
            i = j

        def can(L: int) -> bool:
            # Check if there exists a special substring of length L
            # that appears at least 3 times in total (across all positions).
            if L <= 0:
                return True
            for c in range(26):
                total = 0
                for r in char_runs[c]:
                    if r >= L:
                        # In a run of length r, number of occurrences of length-L
                        # special substring = r-L+1
                        total += (r - L + 1)
                    if total >= 3:
                        return True
            return False

        # Binary search maximum L
        lo, hi = 1, n // 3 + 1  # upper bound small enough; safe for this problem
        # Actually maximum special substring length can't exceed n//3? Not necessarily
        # if overlaps allowed, but since we need 3 occurrences of length L,
        # in same run length r gives (r-L+1) >= 3 => L <= r-2 <= n-2.
        # Still, we'll just binary search up to n.
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count maximum length L such that some character c has at least
        # three substrings of length L all equal to c repeated L times.
        #
        # For each character with total run length = len_run, number of
        # substrings of length L within that run is max(0, len_run - L + 1).
        # If there are multiple runs, we sum counts across runs (since
        # identical single-character substrings from different positions
        # still count as occurrences).
        #
        # Then check if any character reaches >= 3 occurrences.
        def feasible(L: int) -> bool:
            if L == 0:
                return True
            # For each char, total occurrences of substring of length L
            # consisting only of that char.
            occ = [0] * 26
            n = len(s)

            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                run_len = j - i
                if run_len >= L:
                    occ[ord(s[i]) - 97] += run_len - L + 1
                    if occ[ord(s[i]) - 97] >= 3:
                        return True
                i = j
            return False

        lo, hi = 1, len(s)  # search length
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # count total length of each run of identical chars
        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append(j - i)
            i = j

        # For any special substring consisting of char c and length L:
        # it occurs as many times as sum over runs of c of max(0, run_len - L + 1).
        # Since s length <= 50, we can brute L from 1..n/?? and check counts.
        # The alphabet size is small; but easiest is enumerate L descending and check.
        best = -1
        for L in range(n, 0, -1):
            # compute occurrences for each character for this L
            occ = [0] * 26
            idx = 0
            while idx < n:
                ch = s[idx]
                j = idx
                while j < n and s[j] == ch:
                    j += 1
                run_len = j - idx
                if run_len >= L:
                    occ[ord(ch) - 97] += run_len - L + 1
                idx = j

            if any(x >= 3 for x in occ):
                best = L
                break

        return best
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of each character as a "special substring"
        # i.e., any substring consisting of only that one character.
        # A character run of length L contributes:
        # lengths 1..L each occur (L - len + 1) times, all within the run.
        # If total across all runs for a given length is >= 3, it's valid.
        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        best = -1
        for ch in set(s):
            # collect run lengths for this character
            Ls = [L for c, L in runs if c == ch]
            if not Ls:
                continue

            # We only need lengths up to max run length (<= 50)
            maxL = max(Ls)
            cnt = [0] * (maxL + 1)  # cnt[len] = total occurrences of special substrings of that length
            for L in Ls:
                for length in range(1, L + 1):
                    cnt[length] += (L - length + 1)

            # find largest length with cnt[len] >= 3
            for length in range(maxL, 0, -1):
                if cnt[length] >= 3:
                    if length > best:
                        best = length
                    break

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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count maximum occurrences for each character length.
        # Since s length <= 50 and special substrings are just repeated single characters,
        # we can brute over possible lengths for each char.
        n = len(s)
        best = -1

        for ch in set(s):
            # Gather run lengths of this character in s
            run_lengths = []
            i = 0
            while i < n:
                if s[i] == ch:
                    j = i
                    while j < n and s[j] == ch:
                        j += 1
                    run_lengths.append(j - i)
                    i = j
                else:
                    i += 1

            # For a given length L, total number of occurrences of ch repeated L times
            # is sum over runs of max(0, run_len - L + 1). Need >= 3.
            # L cannot exceed max run length.
            max_run = max(run_lengths) if run_lengths else 0

            for L in range(1, max_run + 1):
                cnt = 0
                for r in run_lengths:
                    if r >= L:
                        cnt += r - L + 1
                    if cnt >= 3:
                        break
                if cnt >= 3:
                    best = max(best, L)

        return best
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Binary-search on length L; check if any single-character substring of length L
        # occurs at least 3 times (as contiguous blocks).
        n = len(s)

        # Precompute runs: (char, start, end_inclusive)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        # For a run of length len_run, how many substrings of length L consisting of the run's char?
        # For L <= len_run: occurrences = len_run - L + 1, else 0.
        def can(L: int) -> bool:
            if L <= 0:
                return True
            cnt = [0] * 26
            for ch, length in runs:
                if length >= L:
                    occurrences = length - L + 1
                    cnt[ord(ch) - 97] += occurrences
                    if cnt[ord(ch) - 97] >= 3:
                        return True
            return False

        # Maximum possible L is n, but practically <= n//? still safe to bound by n.
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans if ans != 0 else -1
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of each character at each possible run length.
        # A special substring is just one character repeated k times: "c"*k.
        # It occurs (as a substring) as many times as there are positions where a run of c's
        # has length >= k. For a run of length L, number of substrings "c"*k inside it is (L-k+1).
        n = len(s)
        best = -1

        for ch in set(s):
            runs = []
            i = 0
            while i < n:
                if s[i] != ch:
                    i += 1
                    continue
                j = i
                while j < n and s[j] == ch:
                    j += 1
                runs.append(j - i)
                i = j

            # For each k, total occurrences is sum over runs of max(0, L-k+1).
            # We need the maximum k such that total >= 3.
            maxL = max(runs) if runs else 0
            # Small constraints (n<=50) -> brute force k is fine.
            for k in range(1, maxL + 1):
                total = 0
                for L in runs:
                    if L >= k:
                        total += (L - k + 1)
                    if total >= 3:  # early stop
                        break
                if total >= 3:
                    if k > best:
                        best = k

        return best
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of runs of each character
        # For a special substring of length L consisting of char c to occur >= 3 times,
        # we need at least three positions of length-L windows inside occurrences.
        # In a run of length r, number of substrings of length L for that char is:
        #   max(0, r - L + 1)
        # We can binary search L and check feasibility.
        
        n = len(s)
        runs = {}
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ch = s[i]
            runs[ch] = runs.get(ch, []) + [j - i]
            i = j

        def can(L: int) -> bool:
            if L == 0:
                return True
            for ch_runs in runs.values():
                total = 0
                for r in ch_runs:
                    if r >= L:
                        total += r - L + 1
                        if total >= 3:
                            return True
            return False

        # Max possible L is n
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # For any special substring, it is just one character repeated.
        # If a character c appears in maximal consecutive block length L,
        # then it contributes substrings of length k (1<=k<=L).
        # Count how many times each length k appears for that character across all blocks:
        # occurrences for length k is sum over blocks of max(0, block_len - k + 1).
        # We need the maximum k such that some character has occurrences >= 3.
        
        n = len(s)
        blocks = []  # list of (char, block_length)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks.append((s[i], j - i))
            i = j

        # Maximum possible length is max block length, <= n.
        best = -1
        # We can compute for each character separately, since only 26 letters.
        for ch in range(26):
            c = chr(ord('a') + ch)
            lens = [L for (cc, L) in blocks if cc == c]
            if not lens:
                continue

            # For k from 1..maxLen, count occurrences:
            # occ(k) = sum(max(0, L - k + 1))
            maxLen = max(lens)
            # We can cap early: if total occurrences for k=1 < 3 => answer can't be >1.
            for k in range(1, maxLen + 1):
                occ = 0
                for L in lens:
                    if L >= k:
                        occ += L - k + 1
                        if occ >= 3:
                            best = max(best, k)
                            break

        return best
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # For a special substring, it is some character c repeated L times: c^L.
        # Any occurrence is fully contained within a maximal run of c's.
        # If the maximum run lengths for c are r1 >= r2 >= r3 ...
        # then the count of occurrences of c^L is:
        # sum over runs max(0, run_len - L + 1) >= 3
        # We can binary search the answer length for each L, but since |s|<=50,
        # brute over L and counts is simplest.

        n = len(s)
        # Collect run lengths for each character
        run_lens = [[] for _ in range(26)]
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            run_lens[ord(s[i]) - 97].append(j - i)
            i = j

        def exists(L: int) -> bool:
            if L <= 0:
                return True
            total_needed = 3
            for ch in range(26):
                cnt = 0
                for r in run_lens[ch]:
                    if r >= L:
                        cnt += r - L + 1
                        if cnt >= total_needed:
                            return True
            return False

        # Maximum possible length is at most max run length
        max_run = max((max(lst) for lst in run_lens if lst), default=0)
        ans = -1
        # L from high to low; small constraints allow O(26 * runs * n)
        for L in range(max_run, 0, -1):
            if exists(L):
                ans = L
                break
        return ans
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count consecutive occurrences for each character
        n = len(s)
        runs = [0] * 26
        # We need lengths of substrings made of a single repeated char.
        # For each char, collect all run lengths where it appears contiguously.
        char_runs = [[] for _ in range(26)]
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            k = ord(s[i]) - 97
            char_runs[k].append(j - i)
            i = j

        def can(L: int) -> bool:
            # Check if there exists a special substring of length L
            # that appears at least 3 times in total (across all positions).
            if L <= 0:
                return True
            for c in range(26):
                total = 0
                for r in char_runs[c]:
                    if r >= L:
                        # In a run of length r, number of occurrences of length-L
                        # special substring = r-L+1
                        total += (r - L + 1)
                    if total >= 3:
                        return True
            return False

        # Binary search maximum L
        lo, hi = 1, n // 3 + 1  # upper bound small enough; safe for this problem
        # Actually maximum special substring length can't exceed n//3? Not necessarily
        # if overlaps allowed, but since we need 3 occurrences of length L,
        # in same run length r gives (r-L+1) >= 3 => L <= r-2 <= n-2.
        # Still, we'll just binary search up to n.
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count maximum length L such that some character c has at least
        # three substrings of length L all equal to c repeated L times.
        #
        # For each character with total run length = len_run, number of
        # substrings of length L within that run is max(0, len_run - L + 1).
        # If there are multiple runs, we sum counts across runs (since
        # identical single-character substrings from different positions
        # still count as occurrences).
        #
        # Then check if any character reaches >= 3 occurrences.
        def feasible(L: int) -> bool:
            if L == 0:
                return True
            # For each char, total occurrences of substring of length L
            # consisting only of that char.
            occ = [0] * 26
            n = len(s)

            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                run_len = j - i
                if run_len >= L:
                    occ[ord(s[i]) - 97] += run_len - L + 1
                    if occ[ord(s[i]) - 97] >= 3:
                        return True
                i = j
            return False

        lo, hi = 1, len(s)  # search length
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # count total length of each run of identical chars
        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append(j - i)
            i = j

        # For any special substring consisting of char c and length L:
        # it occurs as many times as sum over runs of c of max(0, run_len - L + 1).
        # Since s length <= 50, we can brute L from 1..n/?? and check counts.
        # The alphabet size is small; but easiest is enumerate L descending and check.
        best = -1
        for L in range(n, 0, -1):
            # compute occurrences for each character for this L
            occ = [0] * 26
            idx = 0
            while idx < n:
                ch = s[idx]
                j = idx
                while j < n and s[j] == ch:
                    j += 1
                run_len = j - idx
                if run_len >= L:
                    occ[ord(ch) - 97] += run_len - L + 1
                idx = j

            if any(x >= 3 for x in occ):
                best = L
                break

        return best
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of each character as a "special substring"
        # i.e., any substring consisting of only that one character.
        # A character run of length L contributes:
        # lengths 1..L each occur (L - len + 1) times, all within the run.
        # If total across all runs for a given length is >= 3, it's valid.
        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        best = -1
        for ch in set(s):
            # collect run lengths for this character
            Ls = [L for c, L in runs if c == ch]
            if not Ls:
                continue

            # We only need lengths up to max run length (<= 50)
            maxL = max(Ls)
            cnt = [0] * (maxL + 1)  # cnt[len] = total occurrences of special substrings of that length
            for L in Ls:
                for length in range(1, L + 1):
                    cnt[length] += (L - length + 1)

            # find largest length with cnt[len] >= 3
            for length in range(maxL, 0, -1):
                if cnt[length] >= 3:
                    if length > best:
                        best = length
                    break

        return best
```
```

</details>

## Evaluation

- Baseline pass@1: `0.9000`
- Augmented pass@1: `0.9000`
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
You are given a string s that consists of lowercase English letters.
A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.

Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.

Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.

 
Constraints:

3 <= s.length <= 50
s consists of only lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        # Binary search on length L: check if some special substring of length L
        # (i.e., all same char) appears at least 3 times.
        def can(L: int) -> bool:
            if L == 0:
                return True
            cnt = [0] * 26  # total number of occurrences (with overlap) of runs' length-L substrings per char
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                run_len = j - i
                if run_len >= L:
                    # In a run of length run_len, number of length-L substrings all equal to that char:
                    # (run_len - L + 1)
                    cnt[ord(s[i]) - 97] += run_len - L + 1
                i = j

            # Need any char whose special substring count >= 3
            return any(x >= 3 for x in cnt)

        lo, hi = 1, n // 3 * 3  # upper bound can be n//3 in general, but n<=50 so safe
        # More precise hi: maximum run length, but not necessary.
        hi = n  # we'll binary search up to n; can() will handle too-large L

        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Collect lengths of each maximal run of identical characters.
        # Any special substring is just c repeated k times; it can occur
        # within runs of c. For a run length L, the substring length k
        # appears (L - k + 1) times within that run.
        from collections import Counter

        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        # For each character, gather run lengths.
        by_char = {}
        for ch, L in runs:
            by_char.setdefault(ch, []).append(L)

        def feasible(k: int) -> bool:
            # Check if there exists any character c such that its special substring
            # of length k appears at least 3 times in the whole string.
            for ch, lens in by_char.items():
                total = 0
                for L in lens:
                    if L >= k:
                        total += L - k + 1
                    if total >= 3:
                        return True
            return False

        # Maximum possible k is bounded by n//3? Not strictly, but n <= 50.
        # We can safely binary search from 1..n.
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import Counter

        # Count frequency of each character
        n = len(s)
        cnt = Counter(s)

        # For a special substring of length L using character c:
        # we need at least 3 occurrences (i.e., L is contained in at least 3 windows
        # of consecutive c's). If a block has length b, it contributes
        # (b - L + 1) occurrences of length-L all-c substrings when b >= L.
        #
        # Since s.length <= 50 and alphabet size small, we can brute L from high to low,
        # and check feasibility.
        max_possible = 0
        for b in cnt.values():
            max_possible = max(max_possible, b)

        # Collect lengths of consecutive character blocks for each character
        blocks = {ch: [] for ch in cnt}
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks[s[i]].append(j - i)
            i = j

        def feasible(L: int) -> bool:
            if L == 0:
                return True
            for ch, blist in blocks.items():
                occ = 0
                for b in blist:
                    if b >= L:
                        occ += b - L + 1
                        if occ >= 3:
                            return True
            return False

        for L in range(max_possible, 0, -1):
            if feasible(L):
                return L
        return -1
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Need longest special substring (single char repeated) that occurs at least 3 times.
        # For each character c with run lengths L1, L2, ..., occurrences of substring c^k is:
        # sum over runs of max(0, Li - k + 1). We need max k such that this >= 3.
        n = len(s)

        # Collect run lengths for each character
        run_lengths = {chr(ord('a') + i): [] for i in range(26)}
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            run_lengths[s[i]].append(j - i)
            i = j

        def can(k: int) -> bool:
            if k <= 0:
                return True
            total_needed = 3
            for c in range(26):
                ch = chr(ord('a') + c)
                cnt = 0
                for L in run_lengths[ch]:
                    if L >= k:
                        cnt += L - k + 1
                        if cnt >= total_needed:
                            return True
            return False

        # Binary search maximum k in [1, n] (actually <= n//1 but safe)
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Find, for each character, the maximum number of occurrences possible for
        # any special substring of that character with a given length.
        # A special substring is just repeated same character, so special substrings
        # are "c"*k for some k and some character c.
        n = len(s)
        best = -1

        # Gather lengths of maximal runs for each character.
        runs = {}
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ch = s[i]
            run_len = j - i
            runs.setdefault(ch, []).append(run_len)
            i = j

        # For each possible k, check if any character has at least three substrings of
        # "ch"*k across all runs. In a run of length L, it contributes:
        # count = max(0, L - k + 1) occurrences of "ch"*k.
        for ch, lens in runs.items():
            # Upper bound for k is the max run length.
            maxL = max(lens)
            for k in range(1, maxL + 1):
                total = 0
                for L in lens:
                    if L >= k:
                        total += L - k + 1
                    if total >= 3:
                        break
                if total >= 3:
                    best = max(best, k)

        return best
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of each "special substring" = a run of one character.
        n = len(s)
        best = -1
        freq = {chr(ord('a') + i): [0] * (n + 1) for i in range(26)}

        # For each character, we only need to consider lengths of substrings within runs.
        i = 0
        while i < n:
            ch = s[i]
            j = i
            while j < n and s[j] == ch:
                j += 1
            run_len = j - i

            # For every length L <= run_len, this run contributes (run_len - L + 1) substrings of length L.
            # We'll update freq[ch][L] by that amount.
            # Complexity: sum of run_len over all runs = n, but updating all L per run costs O(n^2) worst-case,
            # still fine for n <= 50.
            for L in range(1, run_len + 1):
                freq[ch][L] += run_len - L + 1

            i = j

        # Find the largest L such that some character has at least 3 occurrences.
        for ch_i in range(26):
            ch = chr(ord('a') + ch_i)
            for L in range(n, 0, -1):
                if freq[ch][L] >= 3:
                    best = max(best, L)
                    break  # since L decreases, first hit is the largest for this ch

        return best
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # For a special substring (single repeated char) of length L to occur
        # at least three times in s, it's enough to consider the runs of each char.
        # If a run has length len_run, then it contains (len_run - L + 1) occurrences
        # of that special substring, for L <= len_run.
        #
        # We need the maximum L such that total occurrences across runs >= 3.
        n = len(s)
        best = -1

        # Group by character runs
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        # Maximum possible L is at most n, but with n <= 50 it's fine.
        # We'll binary search L and check each char? Actually we can just check
        # L from high to low and compute occurrences.
        for L in range(n, 0, -1):
            total = 0
            for ch, run_len in runs:
                if run_len >= L:
                    total += (run_len - L + 1)
                    if total >= 3:
                        # But that counts occurrences of potentially different chars.
                        # We must ensure they come from the same single-character substring.
                        # So we need per-character totals.
                        pass
            # Rework properly below (per character totals).
            # We'll break from the loop only when correct.
            totals = [0] * 26
            for ch, run_len in runs:
                if run_len >= L:
                    totals[ord(ch) - 97] += (run_len - L + 1)
            if max(totals) >= 3:
                best = L
                break

        return best
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of each character as a contiguous "special substring"
        # i.e., for a character c, any special substring is "c"*k for some k<=maxRunLen(c).
        # Such a substring occurs at least thrice iff total number of length-k substrings
        # from all runs is >= 3.
        from collections import defaultdict

        runs = defaultdict(list)  # char -> list of run lengths
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs[s[i]].append(j - i)
            i = j

        def can(L: int) -> bool:
            if L <= 0:
                return True
            for ch, lens in runs.items():
                total = 0
                for rl in lens:
                    if rl >= L:
                        # In a run of length rl, number of substrings "ch"*L is rl-L+1
                        total += rl - L + 1
                    if total >= 3:
                        return True
            return False

        # Binary search the maximum L
        lo, hi = 1, max((max(v) for v in runs.values()), default=0)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of every special substring (i.e., a character repeated k times).
        # A special substring is fully defined by (char, length k).
        n = len(s)
        runs = []
        # Compute run lengths for each maximal block of identical chars
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        # For each block length L, it contributes (L - k + 1) occurrences of char^k for k<=L.
        # We only care whether total occurrences >= 3.
        max_run = max(L for _, L in runs)
        total = [[0] * (max_run + 1) for _ in range(26)]  # total[c][k]

        for ch, L in runs:
            idx = ord(ch) - ord('a')
            for k in range(1, L + 1):
                total[idx][k] += L - k + 1

        # Find maximum k such that any char has occurrences >=3
        ans = -1
        for k in range(max_run, 0, -1):
            for c in range(26):
                if total[c][k] >= 3:
                    return k
        return ans
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        # Count occurrences of each character's consecutive run lengths
        # For a given length L of a special substring "c"*L, it occurs at least:
        # sum over runs of floor(run_len / L).
        # We want the maximum L such that for some c, that sum >= 3.
        #
        # Since n <= 50, we can brute L from n down to 1 and check efficiently.
        for L in range(n, 0, -1):
            possible = False
            for ch in range(26):
                c = chr(ord('a') + ch)
                cnt = 0
                i = 0
                while i < n:
                    if s[i] != c:
                        i += 1
                        continue
                    j = i
                    while j < n and s[j] == c:
                        j += 1
                    run_len = j - i
                    cnt += run_len // L
                    if cnt >= 3:
                        possible = True
                        break
                    i = j
                if possible:
                    return L
        return -1
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
| 9 | 0.7333 | `partial` |

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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "17",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "31",
      "actual": "11",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "6",
      "error": "Wrong Answer"
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
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        # Binary search on length L: check if some special substring of length L
        # (i.e., all same char) appears at least 3 times.
        def can(L: int) -> bool:
            if L == 0:
                return True
            cnt = [0] * 26  # total number of occurrences (with overlap) of runs' length-L substrings per char
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                run_len = j - i
                if run_len >= L:
                    # In a run of length run_len, number of length-L substrings all equal to that char:
                    # (run_len - L + 1)
                    cnt[ord(s[i]) - 97] += run_len - L + 1
                i = j

            # Need any char whose special substring count >= 3
            return any(x >= 3 for x in cnt)

        lo, hi = 1, n // 3 * 3  # upper bound can be n//3 in general, but n<=50 so safe
        # More precise hi: maximum run length, but not necessary.
        hi = n  # we'll binary search up to n; can() will handle too-large L

        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Collect lengths of each maximal run of identical characters.
        # Any special substring is just c repeated k times; it can occur
        # within runs of c. For a run length L, the substring length k
        # appears (L - k + 1) times within that run.
        from collections import Counter

        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        # For each character, gather run lengths.
        by_char = {}
        for ch, L in runs:
            by_char.setdefault(ch, []).append(L)

        def feasible(k: int) -> bool:
            # Check if there exists any character c such that its special substring
            # of length k appears at least 3 times in the whole string.
            for ch, lens in by_char.items():
                total = 0
                for L in lens:
                    if L >= k:
                        total += L - k + 1
                    if total >= 3:
                        return True
            return False

        # Maximum possible k is bounded by n//3? Not strictly, but n <= 50.
        # We can safely binary search from 1..n.
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import Counter

        # Count frequency of each character
        n = len(s)
        cnt = Counter(s)

        # For a special substring of length L using character c:
        # we need at least 3 occurrences (i.e., L is contained in at least 3 windows
        # of consecutive c's). If a block has length b, it contributes
        # (b - L + 1) occurrences of length-L all-c substrings when b >= L.
        #
        # Since s.length <= 50 and alphabet size small, we can brute L from high to low,
        # and check feasibility.
        max_possible = 0
        for b in cnt.values():
            max_possible = max(max_possible, b)

        # Collect lengths of consecutive character blocks for each character
        blocks = {ch: [] for ch in cnt}
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks[s[i]].append(j - i)
            i = j

        def feasible(L: int) -> bool:
            if L == 0:
                return True
            for ch, blist in blocks.items():
                occ = 0
                for b in blist:
                    if b >= L:
                        occ += b - L + 1
                        if occ >= 3:
                            return True
            return False

        for L in range(max_possible, 0, -1):
            if feasible(L):
                return L
        return -1
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Need longest special substring (single char repeated) that occurs at least 3 times.
        # For each character c with run lengths L1, L2, ..., occurrences of substring c^k is:
        # sum over runs of max(0, Li - k + 1). We need max k such that this >= 3.
        n = len(s)

        # Collect run lengths for each character
        run_lengths = {chr(ord('a') + i): [] for i in range(26)}
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            run_lengths[s[i]].append(j - i)
            i = j

        def can(k: int) -> bool:
            if k <= 0:
                return True
            total_needed = 3
            for c in range(26):
                ch = chr(ord('a') + c)
                cnt = 0
                for L in run_lengths[ch]:
                    if L >= k:
                        cnt += L - k + 1
                        if cnt >= total_needed:
                            return True
            return False

        # Binary search maximum k in [1, n] (actually <= n//1 but safe)
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Find, for each character, the maximum number of occurrences possible for
        # any special substring of that character with a given length.
        # A special substring is just repeated same character, so special substrings
        # are "c"*k for some k and some character c.
        n = len(s)
        best = -1

        # Gather lengths of maximal runs for each character.
        runs = {}
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ch = s[i]
            run_len = j - i
            runs.setdefault(ch, []).append(run_len)
            i = j

        # For each possible k, check if any character has at least three substrings of
        # "ch"*k across all runs. In a run of length L, it contributes:
        # count = max(0, L - k + 1) occurrences of "ch"*k.
        for ch, lens in runs.items():
            # Upper bound for k is the max run length.
            maxL = max(lens)
            for k in range(1, maxL + 1):
                total = 0
                for L in lens:
                    if L >= k:
                        total += L - k + 1
                    if total >= 3:
                        break
                if total >= 3:
                    best = max(best, k)

        return best
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of each "special substring" = a run of one character.
        n = len(s)
        best = -1
        freq = {chr(ord('a') + i): [0] * (n + 1) for i in range(26)}

        # For each character, we only need to consider lengths of substrings within runs.
        i = 0
        while i < n:
            ch = s[i]
            j = i
            while j < n and s[j] == ch:
                j += 1
            run_len = j - i

            # For every length L <= run_len, this run contributes (run_len - L + 1) substrings of length L.
            # We'll update freq[ch][L] by that amount.
            # Complexity: sum of run_len over all runs = n, but updating all L per run costs O(n^2) worst-case,
            # still fine for n <= 50.
            for L in range(1, run_len + 1):
                freq[ch][L] += run_len - L + 1

            i = j

        # Find the largest L such that some character has at least 3 occurrences.
        for ch_i in range(26):
            ch = chr(ord('a') + ch_i)
            for L in range(n, 0, -1):
                if freq[ch][L] >= 3:
                    best = max(best, L)
                    break  # since L decreases, first hit is the largest for this ch

        return best
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # For a special substring (single repeated char) of length L to occur
        # at least three times in s, it's enough to consider the runs of each char.
        # If a run has length len_run, then it contains (len_run - L + 1) occurrences
        # of that special substring, for L <= len_run.
        #
        # We need the maximum L such that total occurrences across runs >= 3.
        n = len(s)
        best = -1

        # Group by character runs
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        # Maximum possible L is at most n, but with n <= 50 it's fine.
        # We'll binary search L and check each char? Actually we can just check
        # L from high to low and compute occurrences.
        for L in range(n, 0, -1):
            total = 0
            for ch, run_len in runs:
                if run_len >= L:
                    total += (run_len - L + 1)
                    if total >= 3:
                        # But that counts occurrences of potentially different chars.
                        # We must ensure they come from the same single-character substring.
                        # So we need per-character totals.
                        pass
            # Rework properly below (per character totals).
            # We'll break from the loop only when correct.
            totals = [0] * 26
            for ch, run_len in runs:
                if run_len >= L:
                    totals[ord(ch) - 97] += (run_len - L + 1)
            if max(totals) >= 3:
                best = L
                break

        return best
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of each character as a contiguous "special substring"
        # i.e., for a character c, any special substring is "c"*k for some k<=maxRunLen(c).
        # Such a substring occurs at least thrice iff total number of length-k substrings
        # from all runs is >= 3.
        from collections import defaultdict

        runs = defaultdict(list)  # char -> list of run lengths
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs[s[i]].append(j - i)
            i = j

        def can(L: int) -> bool:
            if L <= 0:
                return True
            for ch, lens in runs.items():
                total = 0
                for rl in lens:
                    if rl >= L:
                        # In a run of length rl, number of substrings "ch"*L is rl-L+1
                        total += rl - L + 1
                    if total >= 3:
                        return True
            return False

        # Binary search the maximum L
        lo, hi = 1, max((max(v) for v in runs.values()), default=0)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        # Count occurrences of every special substring (i.e., a character repeated k times).
        # A special substring is fully defined by (char, length k).
        n = len(s)
        runs = []
        # Compute run lengths for each maximal block of identical chars
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        # For each block length L, it contributes (L - k + 1) occurrences of char^k for k<=L.
        # We only care whether total occurrences >= 3.
        max_run = max(L for _, L in runs)
        total = [[0] * (max_run + 1) for _ in range(26)]  # total[c][k]

        for ch, L in runs:
            idx = ord(ch) - ord('a')
            for k in range(1, L + 1):
                total[idx][k] += L - k + 1

        # Find maximum k such that any char has occurrences >=3
        ans = -1
        for k in range(max_run, 0, -1):
            for c in range(26):
                if total[c][k] >= 3:
                    return k
        return ans
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        # Count occurrences of each character's consecutive run lengths
        # For a given length L of a special substring "c"*L, it occurs at least:
        # sum over runs of floor(run_len / L).
        # We want the maximum L such that for some c, that sum >= 3.
        #
        # Since n <= 50, we can brute L from n down to 1 and check efficiently.
        for L in range(n, 0, -1):
            possible = False
            for ch in range(26):
                c = chr(ord('a') + ch)
                cnt = 0
                i = 0
                while i < n:
                    if s[i] != c:
                        i += 1
                        continue
                    j = i
                    while j < n and s[j] == c:
                        j += 1
                    run_len = j - i
                    cnt += run_len // L
                    if cnt >= 3:
                        possible = True
                        break
                    i = j
                if possible:
                    return L
        return -1
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
| 9 | 0.7333 | `partial` |

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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "2",
      "actual": "2",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
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
      "expected": "31",
      "actual": "31",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18",
      "actual": "18",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-1",
      "actual": "-1",
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
      "expected": "17",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "31",
      "actual": "11",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18",
      "actual": "6",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>
