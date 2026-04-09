# Problem 2847

- Domain: `coding`

## Problem

```text
You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:

The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.

Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair.
 
Example 1:

Input: words = ["cd","ac","dc","ca","zz"]
Output: 2
Explanation: In this example, we can form 2 pair of strings in the following way:
- We pair the 0^th string with the 2^nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1^st string with the 3^rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.
Example 2:

Input: words = ["ab","ba","cc"]
Output: 1
Explanation: In this example, we can form 1 pair of strings in the following way:
- We pair the 0^th string with the 1^st string, as the reversed string of words[1] is "ab" and is equal to words[0].
It can be proven that 1 is the maximum number of pairs that can be formed.

Example 3:

Input: words = ["aa","ab"]
Output: 0
Explanation: In this example, we are unable to form any pair of strings.

 
Constraints:

1 <= words.length <= 50
words[i].length == 2
words consists of distinct strings.
words[i] contains only lowercase English letters.
```

### Starter Code

```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[\"cd\", \"ac\", \"dc\", \"ca\", \"zz\"]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[\"ab\", \"ba\", \"cc\"]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[\"aa\", \"ab\"]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[\"ga\"]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[\"uw\"]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[\"qg\"]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[\"zr\"]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[\"ku\"]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[\"fp\"]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[\"us\", \"su\"]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[\"gh\", \"hg\", \"kf\", \"fk\"]",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "[\"ei\", \"nq\", \"gw\", \"rt\", \"wb\", \"wg\", \"zr\", \"sn\", \"co\", \"oc\", \"qn\", \"uk\", \"ku\", \"tc\", \"ct\", \"df\", \"vb\", \"iy\", \"fd\", \"ns\", \"rz\", \"zv\", \"vz\", \"ip\", \"bw\", \"tr\", \"yi\", \"ie\", \"pi\", \"bv\"]",
    "output": "15",
    "testtype": "functional"
  },
  {
    "input": "[\"tv\", \"eu\", \"lg\", \"df\", \"pt\", \"cb\", \"ja\", \"by\", \"cw\", \"ut\", \"zt\", \"yn\", \"rh\", \"vs\", \"nj\", \"vn\", \"fl\", \"ln\", \"pe\", \"tk\", \"lq\", \"ug\", \"ab\", \"ex\", \"dt\", \"ee\", \"hm\", \"ce\", \"tm\", \"nu\", \"nr\", \"vc\", \"aw\", \"ti\", \"lk\", \"jc\", \"xi\", \"wm\", \"lt\", \"ih\", \"px\", \"uv\", \"hv\", \"sh\", \"qz\", \"ue\", \"sy\", \"qs\", \"ms\", \"po\"]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[\"qg\", \"vw\", \"lu\", \"xm\", \"yt\", \"am\", \"bs\", \"lp\", \"nt\", \"la\", \"rb\", \"tz\", \"bu\", \"op\", \"qt\", \"fi\", \"mj\", \"rw\", \"ud\", \"bb\", \"mh\", \"pq\", \"th\", \"zy\", \"ew\", \"so\", \"ig\", \"zb\", \"hc\", \"ax\", \"fy\", \"ov\", \"ka\", \"kv\", \"eo\", \"hj\", \"hk\", \"rv\", \"xb\", \"ny\", \"hn\", \"sw\", \"gh\", \"xf\", \"ec\", \"jj\", \"ix\", \"rg\", \"jo\", \"ho\"]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[\"vz\", \"zv\", \"fn\", \"nf\", \"ic\", \"ci\", \"tb\", \"bt\", \"mx\", \"xm\", \"uk\", \"ku\", \"gt\", \"tg\", \"mq\", \"qm\", \"iv\", \"vi\", \"gi\", \"ig\", \"lp\", \"pl\", \"sy\", \"ys\", \"hn\", \"nh\", \"vf\", \"fv\", \"vj\", \"jv\", \"xd\", \"dx\", \"hf\", \"fh\", \"tk\", \"kt\", \"qe\", \"eq\", \"fz\", \"zf\", \"zi\", \"iz\", \"pb\", \"bp\", \"uc\", \"cu\", \"rn\", \"nr\", \"vx\", \"xv\"]",
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
You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:

The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.

Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair.
 
Example 1:

Input: words = ["cd","ac","dc","ca","zz"]
Output: 2
Explanation: In this example, we can form 2 pair of strings in the following way:
- We pair the 0^th string with the 2^nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1^st string with the 3^rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.
Example 2:

Input: words = ["ab","ba","cc"]
Output: 1
Explanation: In this example, we can form 1 pair of strings in the following way:
- We pair the 0^th string with the 1^st string, as the reversed string of words[1] is "ab" and is equal to words[0].
It can be proven that 1 is the maximum number of pairs that can be formed.

Example 3:

Input: words = ["aa","ab"]
Output: 0
Explanation: In this example, we are unable to form any pair of strings.

 
Constraints:

1 <= words.length <= 50
words[i].length == 2
words consists of distinct strings.
words[i] contains only lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
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
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s:
                pairs += 1
                s.remove(w)      # prevent reuse
                s.remove(rev)    # also remove the pair partner
        return pairs
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            if w[::-1] in s:
                # Ensure each pair is counted once
                if w < w[::-1]:
                    pairs += 1
        return pairs
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rw = w[::-1]
            if rw in s:
                # ensure we count each pair once
                # (pair w with rw only when w is "lexicographically <=" its reverse)
                if w <= rw:
                    pairs += 1
                    # remove both to prevent reuse
                    s.remove(w)
                    s.remove(rw)
        return pairs
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()
        
        for w in words:
            if w in used:
                continue
            rev = w[::-1]
            if rev in s and rev not in used:
                # form a pair between w and rev
                used.add(w)
                used.add(rev)
                pairs += 1
        
        return pairs
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s and w < rev:  # count each pair once
                pairs += 1
        return pairs
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Count how many times each word appears (even though constraints say distinct,
        # this keeps the logic robust and simple).
        cnt = Counter(words)
        pairs = 0

        for w in words:
            if cnt[w] == 0:
                continue
            rw = w[::-1]
            # If reverse exists and we can consume both, form a pair.
            if cnt.get(rw, 0) > 0:
                # Consume one occurrence of each word.
                # This ensures each string is used at most once.
                cnt[w] -= 1
                cnt[rw] -= 1
                pairs += 1

        return pairs
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s:
                pairs += 1
                s.remove(w)
                s.remove(rev)
        return pairs
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            if w[0] != w[1]:  # only need to check non-palindromes
                rev = w[::-1]
                if rev in s:
                    pairs += 1
                    # Remove both so they can't be reused
                    s.remove(w)
                    s.remove(rev)
        return pairs
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()

        for w in words:
            if w in used:
                continue
            rev = w[::-1]
            if rev in s and rev not in used:
                pairs += 1
                used.add(w)
                used.add(rev)
        return pairs
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()

        for w in words:
            if w in used:
                continue
            rw = w[::-1]
            if rw in s and rw not in used:
                pairs += 1
                used.add(w)
                used.add(rw)

        return pairs
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.0000 | `fail` |
| 1 | 1.0000 | `full` |
| 2 | 0.0000 | `fail` |
| 3 | 0.6667 | `partial` |
| 4 | 1.0000 | `full` |
| 5 | 0.6667 | `partial` |
| 6 | 0.0000 | `fail` |
| 7 | 1.0000 | `full` |
| 8 | 0.6667 | `partial` |
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
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "2",
      "actual": "2",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
  "passed": 10,
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
      "passed": true,
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
      "expected": "15",
      "actual": "15",
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
      "expected": "0",
      "actual": "2",
      "error": "Wrong Answer"
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
      "expected": "2",
      "actual": "2",
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
      "expected": "25",
      "actual": "25",
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
      "passed": true,
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
      "expected": "15",
      "actual": "15",
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
      "expected": "0",
      "actual": "2",
      "error": "Wrong Answer"
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
<summary>Score details for generation 6</summary>

```json
{
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "2",
      "actual": "2",
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
  "passed": 10,
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
      "passed": true,
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
      "expected": "15",
      "actual": "15",
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
      "expected": "0",
      "actual": "2",
      "error": "Wrong Answer"
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
<summary>Score details for generation 9</summary>

```json
{
  "passed": 10,
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
      "passed": true,
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
      "expected": "15",
      "actual": "15",
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
      "expected": "0",
      "actual": "2",
      "error": "Wrong Answer"
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
You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:

The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.

Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair.
 
Example 1:

Input: words = ["cd","ac","dc","ca","zz"]
Output: 2
Explanation: In this example, we can form 2 pair of strings in the following way:
- We pair the 0^th string with the 2^nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1^st string with the 3^rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.
Example 2:

Input: words = ["ab","ba","cc"]
Output: 1
Explanation: In this example, we can form 1 pair of strings in the following way:
- We pair the 0^th string with the 1^st string, as the reversed string of words[1] is "ab" and is equal to words[0].
It can be proven that 1 is the maximum number of pairs that can be formed.

Example 3:

Input: words = ["aa","ab"]
Output: 0
Explanation: In this example, we are unable to form any pair of strings.

 
Constraints:

1 <= words.length <= 50
words[i].length == 2
words consists of distinct strings.
words[i] contains only lowercase English letters.

### Solutions
#### Correct
Attempt 1
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            if w[::-1] in s:
                # Ensure each pair is counted once
                if w < w[::-1]:
                    pairs += 1
        return pairs
```

Attempt 2
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s and w < rev:  # count each pair once
                pairs += 1
        return pairs
```

Attempt 3
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            if w[0] != w[1]:  # only need to check non-palindromes
                rev = w[::-1]
                if rev in s:
                    pairs += 1
                    # Remove both so they can't be reused
                    s.remove(w)
                    s.remove(rev)
        return pairs
```

#### Partially Correct
Attempt 1
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()
        
        for w in words:
            if w in used:
                continue
            rev = w[::-1]
            if rev in s and rev not in used:
                # form a pair between w and rev
                used.add(w)
                used.add(rev)
                pairs += 1
        
        return pairs
```

Attempt 2
```python
from typing import List
from collections import Counter

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Count how many times each word appears (even though constraints say distinct,
        # this keeps the logic robust and simple).
        cnt = Counter(words)
        pairs = 0

        for w in words:
            if cnt[w] == 0:
                continue
            rw = w[::-1]
            # If reverse exists and we can consume both, form a pair.
            if cnt.get(rw, 0) > 0:
                # Consume one occurrence of each word.
                # This ensures each string is used at most once.
                cnt[w] -= 1
                cnt[rw] -= 1
                pairs += 1

        return pairs
```

Attempt 3
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()

        for w in words:
            if w in used:
                continue
            rev = w[::-1]
            if rev in s and rev not in used:
                pairs += 1
                used.add(w)
                used.add(rev)
        return pairs
```

Attempt 4
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()

        for w in words:
            if w in used:
                continue
            rw = w[::-1]
            if rw in s and rw not in used:
                pairs += 1
                used.add(w)
                used.add(rw)

        return pairs
```

#### Incorrect
Attempt 1
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s:
                pairs += 1
                s.remove(w)      # prevent reuse
                s.remove(rev)    # also remove the pair partner
        return pairs
```

Attempt 2
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rw = w[::-1]
            if rw in s:
                # ensure we count each pair once
                # (pair w with rw only when w is "lexicographically <=" its reverse)
                if w <= rw:
                    pairs += 1
                    # remove both to prevent reuse
                    s.remove(w)
                    s.remove(rw)
        return pairs
```

Attempt 3
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s:
                pairs += 1
                s.remove(w)
                s.remove(rev)
        return pairs
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
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            if w[::-1] in s:
                # Ensure each pair is counted once
                if w < w[::-1]:
                    pairs += 1
        return pairs
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s and w < rev:  # count each pair once
                pairs += 1
        return pairs
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            if w[0] != w[1]:  # only need to check non-palindromes
                rev = w[::-1]
                if rev in s:
                    pairs += 1
                    # Remove both so they can't be reused
                    s.remove(w)
                    s.remove(rev)
        return pairs
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
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()
        
        for w in words:
            if w in used:
                continue
            rev = w[::-1]
            if rev in s and rev not in used:
                # form a pair between w and rev
                used.add(w)
                used.add(rev)
                pairs += 1
        
        return pairs
```
```

</details>

<details>
<summary>partial attempt 2</summary>

```text
```python
from typing import List
from collections import Counter

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Count how many times each word appears (even though constraints say distinct,
        # this keeps the logic robust and simple).
        cnt = Counter(words)
        pairs = 0

        for w in words:
            if cnt[w] == 0:
                continue
            rw = w[::-1]
            # If reverse exists and we can consume both, form a pair.
            if cnt.get(rw, 0) > 0:
                # Consume one occurrence of each word.
                # This ensures each string is used at most once.
                cnt[w] -= 1
                cnt[rw] -= 1
                pairs += 1

        return pairs
```
```

</details>

<details>
<summary>partial attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()

        for w in words:
            if w in used:
                continue
            rev = w[::-1]
            if rev in s and rev not in used:
                pairs += 1
                used.add(w)
                used.add(rev)
        return pairs
```
```

</details>

<details>
<summary>partial attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()

        for w in words:
            if w in used:
                continue
            rw = w[::-1]
            if rw in s and rw not in used:
                pairs += 1
                used.add(w)
                used.add(rw)

        return pairs
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
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s:
                pairs += 1
                s.remove(w)      # prevent reuse
                s.remove(rev)    # also remove the pair partner
        return pairs
```
```

</details>

<details>
<summary>fail attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rw = w[::-1]
            if rw in s:
                # ensure we count each pair once
                # (pair w with rw only when w is "lexicographically <=" its reverse)
                if w <= rw:
                    pairs += 1
                    # remove both to prevent reuse
                    s.remove(w)
                    s.remove(rw)
        return pairs
```
```

</details>

<details>
<summary>fail attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s:
                pairs += 1
                s.remove(w)
                s.remove(rev)
        return pairs
```
```

</details>

### Parsed Memory Items

1. Enforce “count once” with canonical pairing
Description: When pairs are symmetric, count each valid pair using a canonical rule so it can’t be discovered twice.
<details>
<summary>Content 1</summary>

```text
If objects pair by a reversible relation, define a deterministic way to select exactly one direction (e.g., based on ordering or a canonical representative). Then iterate through all objects and count only when the current object is the chosen representative, ensuring each pair contributes at most once.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
The successful approaches rely on a counting strategy that avoids double-counting and correctly enforces “each string used at most once.” They either (1) count only one representative per reversible pair using an ordering rule, or (2) explicitly track consumption via a “used” set or by removing elements from the remaining pool. The partially correct attempts that “almost” work fail when they don’t fully prevent double counting across the two directed scans of a reversible relationship, or when they rely on insufficiently strict consumption logic. The incorrect attempts show common pitfalls: removing from the pool without guarding against counting the same pair twice (due to encountering both members later), and using a too-permissive counting condition that doesn’t guarantee a pair is counted once.
```

</details>

2. Use state to prevent reuse (consumption or used-tracking)
Description: To satisfy “each item used at most once,” maintain explicit “available/used” state and update it when forming a pair.
<details>
<summary>Content 2</summary>

```text
Greedy pairing is safe when you consistently “consume” both elements of a chosen pair so they cannot be reused later. Implement this either by removing from a mutable pool (set/count map) or by maintaining a separate used set, and always check membership/availability before pairing.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
The successful approaches rely on a counting strategy that avoids double-counting and correctly enforces “each string used at most once.” They either (1) count only one representative per reversible pair using an ordering rule, or (2) explicitly track consumption via a “used” set or by removing elements from the remaining pool. The partially correct attempts that “almost” work fail when they don’t fully prevent double counting across the two directed scans of a reversible relationship, or when they rely on insufficiently strict consumption logic. The incorrect attempts show common pitfalls: removing from the pool without guarding against counting the same pair twice (due to encountering both members later), and using a too-permissive counting condition that doesn’t guarantee a pair is counted once.
```

</details>

3. Validate destructive operations against iteration order
Description: Any approach that deletes or marks items must be correct under the traversal order; otherwise it will still double-count.
<details>
<summary>Content 3</summary>

```text
When you remove elements from a set while iterating over an independent list, you must ensure later iterations won’t form the same logical pair again. Add a guard condition tied to pair uniqueness (canonical representative or used-check), not just existence at time of checking.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
The successful approaches rely on a counting strategy that avoids double-counting and correctly enforces “each string used at most once.” They either (1) count only one representative per reversible pair using an ordering rule, or (2) explicitly track consumption via a “used” set or by removing elements from the remaining pool. The partially correct attempts that “almost” work fail when they don’t fully prevent double counting across the two directed scans of a reversible relationship, or when they rely on insufficiently strict consumption logic. The incorrect attempts show common pitfalls: removing from the pool without guarding against counting the same pair twice (due to encountering both members later), and using a too-permissive counting condition that doesn’t guarantee a pair is counted once.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
The successful approaches rely on a counting strategy that avoids double-counting and correctly enforces “each string used at most once.” They either (1) count only one representative per reversible pair using an ordering rule, or (2) explicitly track consumption via a “used” set or by removing elements from the remaining pool. The partially correct attempts that “almost” work fail when they don’t fully prevent double counting across the two directed scans of a reversible relationship, or when they rely on insufficiently strict consumption logic. The incorrect attempts show common pitfalls: removing from the pool without guarding against counting the same pair twice (due to encountering both members later), and using a too-permissive counting condition that doesn’t guarantee a pair is counted once.
</reasoning>

<memories>
<memory>
<title>Enforce “count once” with canonical pairing</title>
<description>When pairs are symmetric, count each valid pair using a canonical rule so it can’t be discovered twice.</description>
<content>If objects pair by a reversible relation, define a deterministic way to select exactly one direction (e.g., based on ordering or a canonical representative). Then iterate through all objects and count only when the current object is the chosen representative, ensuring each pair contributes at most once.</content>
</memory>

<memory>
<title>Use state to prevent reuse (consumption or used-tracking)</title>
<description>To satisfy “each item used at most once,” maintain explicit “available/used” state and update it when forming a pair.</description>
<content>Greedy pairing is safe when you consistently “consume” both elements of a chosen pair so they cannot be reused later. Implement this either by removing from a mutable pool (set/count map) or by maintaining a separate used set, and always check membership/availability before pairing.</content>
</memory>

<memory>
<title>Validate destructive operations against iteration order</title>
<description>Any approach that deletes or marks items must be correct under the traversal order; otherwise it will still double-count.</description>
<content>When you remove elements from a set while iterating over an independent list, you must ensure later iterations won’t form the same logical pair again. Add a guard condition tied to pair uniqueness (canonical representative or used-check), not just existence at time of checking.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `0.2000`
- Augmented pass@1: `0.2000`
- Improvement: `+0.0000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:

The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.

Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair.
 
Example 1:

Input: words = ["cd","ac","dc","ca","zz"]
Output: 2
Explanation: In this example, we can form 2 pair of strings in the following way:
- We pair the 0^th string with the 2^nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1^st string with the 3^rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.
Example 2:

Input: words = ["ab","ba","cc"]
Output: 1
Explanation: In this example, we can form 1 pair of strings in the following way:
- We pair the 0^th string with the 1^st string, as the reversed string of words[1] is "ab" and is equal to words[0].
It can be proven that 1 is the maximum number of pairs that can be formed.

Example 3:

Input: words = ["aa","ab"]
Output: 0
Explanation: In this example, we are unable to form any pair of strings.

 
Constraints:

1 <= words.length <= 50
words[i].length == 2
words consists of distinct strings.
words[i] contains only lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
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
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Since words[i] are all length 2 and distinct,
        # we can greedily count how many word's reverse exists and hasn't been used.
        s = set(words)
        pairs = 0

        for w in words:
            if w in s:
                rev = w[::-1]
                if rev in s:
                    pairs += 1
                    # mark both as used by removing them from the set
                    s.remove(w)
                    s.remove(rev)

        return pairs
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rw = w[::-1]
            if rw in s:
                pairs += 1
                s.remove(w)
                s.remove(rw)
        return pairs
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()

        for w in words:
            if w in used:
                continue
            rev = w[::-1]
            if rev in s and rev not in used:
                pairs += 1
                used.add(w)
                used.add(rev)

        return pairs
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        used = set()

        for w in words:
            if w in used:
                continue
            rev = w[::-1]
            if rev in s and rev not in used:
                pairs += 1
                used.add(w)
                used.add(rev)

        return pairs
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set(words)
        pairs = 0
        used = set()

        for w in words:
            if w in used:
                continue
            rw = w[::-1]
            if rw in seen and rw not in used:
                pairs += 1
                used.add(w)
                used.add(rw)

        return pairs
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_set = set(words)
        pairs = 0
        for w in words:
            if w[0] == w[1]:  # "aa" type
                # Only pairable if its reverse exists (itself), but distinct strings imply impossible
                continue
            rev = w[1] + w[0]
            if rev in word_set:
                pairs += 1
                # Remove both so each string is used at most once
                word_set.remove(w)
                word_set.remove(rev)
        return pairs
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rw = w[::-1]
            if rw in s:
                pairs += 1
                s.remove(w)
                s.remove(rw)
        return pairs // 1
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_set = set(words)
        pairs = 0
        
        for w in words:
            rev = w[::-1]
            if rev in word_set:
                # Ensure each pair counted once by removing matched strings
                # (and also handle "w" with its reverse).
                if w < rev:
                    pairs += 1
                # If w == rev (e.g., "aa"), it can’t form a pair because all strings are distinct
                # and pairing requires i < j, but only one occurrence exists.
                # For distinct strings of length 2, such cases contribute 0.
        return pairs
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            # To avoid counting the same pair twice, only count when w <= reversed(w) lexicographically
            rw = w[::-1]
            if rw in s and w <= rw:
                pairs += 1
        return pairs // 2 if words else 0
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set(words)
        pairs = 0
        for w in words:
            rev = w[::-1]
            if rev in s:
                pairs += 1
                s.remove(w)      # each string used at most once
                s.remove(rev)
        return pairs
```
```

</details>

#### Baseline Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.0000 | `fail` |
| 1 | 0.0000 | `fail` |
| 2 | 0.6667 | `partial` |
| 3 | 0.6667 | `partial` |
| 4 | 0.6667 | `partial` |
| 5 | 1.0000 | `full` |
| 6 | 0.0000 | `fail` |
| 7 | 1.0000 | `full` |
| 8 | 0.6000 | `partial` |
| 9 | 0.0000 | `fail` |

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
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
  "passed": 10,
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
      "passed": true,
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
      "expected": "15",
      "actual": "15",
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
      "expected": "0",
      "actual": "2",
      "error": "Wrong Answer"
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
<summary>Score details for generation 3</summary>

```json
{
  "passed": 10,
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
      "passed": true,
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
      "expected": "15",
      "actual": "15",
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
      "expected": "0",
      "actual": "2",
      "error": "Wrong Answer"
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
<summary>Score details for generation 4</summary>

```json
{
  "passed": 10,
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
      "passed": true,
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
      "expected": "15",
      "actual": "15",
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
      "expected": "0",
      "actual": "2",
      "error": "Wrong Answer"
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
      "expected": "2",
      "actual": "2",
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
      "expected": "25",
      "actual": "25",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "2",
      "actual": "2",
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
  "passed": 9,
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
      "expected": "1",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "7",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "25",
      "actual": "12",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
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

  1. Enforce “count once” with canonical pairing: When pairs are symmetric, count each valid pair using a canonical rule so it can’t be discovered twice.
     If objects pair by a reversible relation, define a deterministic way to select exactly one direction (e.g., based on ordering or a canonical representative). Then iterate through all objects and count only when the current object is the chosen representative, ensuring each pair contributes at most once.
  2. Use state to prevent reuse (consumption or used-tracking): To satisfy “each item used at most once,” maintain explicit “available/used” state and update it when forming a pair.
     Greedy pairing is safe when you consistently “consume” both elements of a chosen pair so they cannot be reused later. Implement this either by removing from a mutable pool (set/count map) or by maintaining a separate used set, and always check membership/availability before pairing.
  3. Validate destructive operations against iteration order: Any approach that deletes or marks items must be correct under the traversal order; otherwise it will still double-count.
     When you remove elements from a set while iterating over an independent list, you must ensure later iterations won’t form the same logical pair again. Add a guard condition tied to pair uniqueness (canonical representative or used-check), not just existence at time of checking.

Apply these insights to the problem below.

### Question:
You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:

The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.

Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair.
 
Example 1:

Input: words = ["cd","ac","dc","ca","zz"]
Output: 2
Explanation: In this example, we can form 2 pair of strings in the following way:
- We pair the 0^th string with the 2^nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1^st string with the 3^rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.
Example 2:

Input: words = ["ab","ba","cc"]
Output: 1
Explanation: In this example, we can form 1 pair of strings in the following way:
- We pair the 0^th string with the 1^st string, as the reversed string of words[1] is "ab" and is equal to words[0].
It can be proven that 1 is the maximum number of pairs that can be formed.

Example 3:

Input: words = ["aa","ab"]
Output: 0
Explanation: In this example, we are unable to form any pair of strings.

 
Constraints:

1 <= words.length <= 50
words[i].length == 2
words consists of distinct strings.
words[i] contains only lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
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
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Count each word; words are distinct but we keep generic count logic.
        freq = {}
        for w in words:
            freq[w] = 1  # distinct

        pairs = 0
        used = set()  # words already paired/consumed

        for w in words:
            if w in used:
                continue
            rw = w[::-1]
            # Pair only in the forward direction to avoid double counting:
            # choose the canonical representative by lexicographic order.
            if rw in freq and rw not in used and w < rw:
                used.add(w)
                used.add(rw)
                pairs += 1

            # If w == reverse(w) (e.g., "aa"), can't form a pair because each string is distinct
            # and would require two copies of the same string.

        return pairs
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Use a set for O(1) membership checks.
        remaining = set(words)
        pairs = 0

        # Canonical “count once” rule:
        # Only form a pair when we can consume both sides from `remaining`,
        # and we always start from the element itself (deterministic loop
        # over the given array ensures no double counting).
        for w in words:
            if w not in remaining:
                continue  # already used in some previous pairing
            rw = w[::-1]
            if rw in remaining:
                pairs += 1
                remaining.remove(w)
                remaining.remove(rw)

        return pairs
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Count each unordered reversible match at most once by consuming both strings.
        remaining = set(words)
        pairs = 0
        for w in words:
            if w not in remaining:
                continue  # already used
            rev = w[::-1]
            if rev in remaining:
                remaining.remove(w)
                remaining.remove(rev)
                pairs += 1
        return pairs
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Count usable pairs by greedily consuming strings from a set
        # Reverse relation is symmetric; each pair is counted once by always
        # selecting the "current" string if its reverse is still available.
        remaining = set(words)
        pairs = 0

        for w in words:
            rw = w[::-1]
            if w in remaining and rw in remaining:
                pairs += 1
                remaining.remove(w)
                remaining.remove(rw)

        return pairs
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Count maximum pairs of (x, reverse(x)) with each word used at most once.
        remaining = set(words)
        ans = 0

        # Canonical "count once": only form pair when current word equals its own canonical representative.
        # We choose canonical by lexicographic order between the word and its reverse.
        for w in words:
            if w not in remaining:
                continue
            rw = w[::-1]
            if rw in remaining:
                # ensure each pair counted once
                if w < rw or w == rw:
                    remaining.remove(w)
                    remaining.remove(rw)
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
from collections import Counter

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Each word appears at most once (per problem statement).
        # Greedily consume a canonical direction to avoid double counting.
        remaining = set(words)
        pairs = 0

        for w in words:
            r = w[::-1]
            # Canonical rule: count only when w is the chosen representative
            # (here: w < reversed(w)), so each logical pair is considered once.
            if w < r and w in remaining and r in remaining:
                pairs += 1
                remaining.remove(w)
                remaining.remove(r)

        return pairs
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Count maximum number of disjoint pairs (word, reversed(word))
        # Each word is distinct, so we can greedily "consume" matches using a set.
        remaining = set(words)
        pairs = 0

        for w in words:
            if w not in remaining:
                continue  # already used in some previous pair

            rw = w[::-1]
            if rw in remaining:
                pairs += 1
                remaining.remove(w)
                remaining.remove(rw)

        return pairs
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Since words are length-2 and distinct, we can pair greedily using a set.
        # Ensure each word used at most once by consuming it from the set when paired.
        remaining = set(words)
        pairs = 0

        for w in words:
            if w not in remaining:
                continue
            rw = w[::-1]
            if rw in remaining:
                remaining.remove(w)
                remaining.remove(rw)
                pairs += 1

        return pairs
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Build set for O(1) availability checks
        remaining = set(words)
        pairs = 0

        # Canonical pairing: only attempt pairs where current word is
        # the lexicographically smaller between it and its reverse.
        for w in words:
            rw = w[::-1]
            if w in remaining and rw in remaining:
                if w <= rw:  # count each pair once
                    remaining.remove(w)
                    remaining.remove(rw)
                    pairs += 1

        return pairs
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Count maximum disjoint pairs (each word used at most once).
        # Since words are distinct, we can greedily form pairs by consuming from a set.
        s = set(words)
        pairs = 0
        for w in words:
            if w in s:
                rw = w[::-1]
                if rw in s:
                    pairs += 1
                    s.remove(w)
                    s.remove(rw)
        return pairs
```
```

</details>

#### Augmented Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 1.0000 | `full` |
| 1 | 0.0000 | `fail` |
| 2 | 0.0000 | `fail` |
| 3 | 0.0000 | `fail` |
| 4 | 0.0000 | `fail` |
| 5 | 1.0000 | `full` |
| 6 | 0.0000 | `fail` |
| 7 | 0.0000 | `fail` |
| 8 | 0.0000 | `fail` |
| 9 | 0.0000 | `fail` |

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
      "expected": "2",
      "actual": "2",
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
      "expected": "25",
      "actual": "25",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "25",
      "actual": "25",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: 'zz'"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
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
      "expected": "25",
      "actual": "",
      "error": "Skipped (earlier failure)"
    }
  ]
}
```

</details>
