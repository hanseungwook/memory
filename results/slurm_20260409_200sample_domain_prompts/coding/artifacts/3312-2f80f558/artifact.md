# Problem 3312

- Domain: `coding`

## Problem

```text
You are given a 0-indexed string s typed by a user. Changing a key is defined as using a key different from the last used key. For example, s = "ab" has a change of a key while s = "bBBb" does not have any.
Return the number of times the user had to change the key. 
Note: Modifiers like shift or caps lock won't be counted in changing the key that is if a user typed the letter 'a' and then the letter 'A' then it will not be considered as a changing of key.
 
Example 1:

Input: s = "aAbBcC"
Output: 2
Explanation: 
From s[0] = 'a' to s[1] = 'A', there is no change of key as caps lock or shift is not counted.
From s[1] = 'A' to s[2] = 'b', there is a change of key.
From s[2] = 'b' to s[3] = 'B', there is no change of key as caps lock or shift is not counted.
From s[3] = 'B' to s[4] = 'c', there is a change of key.
From s[4] = 'c' to s[5] = 'C', there is no change of key as caps lock or shift is not counted.


Example 2:

Input: s = "AaAaAaaA"
Output: 0
Explanation: There is no change of key since only the letters 'a' and 'A' are pressed which does not require change of key.

 
Constraints:

1 <= s.length <= 100
s consists of only upper case and lower case English letters.
```

### Starter Code

```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
```

### Test Cases

```json
[
  {
    "input": "\"aAbBcC\"",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "\"AaAaAaaA\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"E\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"r\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"H\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"G\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"M\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"a\"",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"Qh\"",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"AIw\"",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "\"CRJEJYXHJAJUZQLSGDFCSMKSBAODDTATIFAOHBDSZIYUGVRBOEVCODFCLMUTTSBJZXAVBHIIPEIXYSXTXYNVCZZZOMSNHVHGZHKE\"",
    "output": "94",
    "testtype": "functional"
  },
  {
    "input": "\"RqZlRtJhLfPZXonaRNgfShpvIBrScljQGLtiySpeSwMQcQZPdxSgTBRiNWySVPweOAbrbRoywfWhcmrZgETIpDxmeXRMxQlznyxJ\"",
    "output": "99",
    "testtype": "functional"
  },
  {
    "input": "\"cjsiuzodienyfsyafmjkzrylsggairtvimbkkwtlgwprtauylqpazsbzfmizqctvibvxqnytextdmfuiwbovwbnqualasevmbjuc\"",
    "output": "97",
    "testtype": "functional"
  },
  {
    "input": "\"JkDvRICdDlDBvmMFXDybvyvJqCVmFhgkQQoSvnLFXKTLmGfcHVUgXRjuKjscOdkGxkYeeBagXJyJDyNvnPqULtGSabPEUROsMutw\"",
    "output": "95",
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
You are given a 0-indexed string s typed by a user. Changing a key is defined as using a key different from the last used key. For example, s = "ab" has a change of a key while s = "bBBb" does not have any.
Return the number of times the user had to change the key. 
Note: Modifiers like shift or caps lock won't be counted in changing the key that is if a user typed the letter 'a' and then the letter 'A' then it will not be considered as a changing of key.
 
Example 1:

Input: s = "aAbBcC"
Output: 2
Explanation: 
From s[0] = 'a' to s[1] = 'A', there is no change of key as caps lock or shift is not counted.
From s[1] = 'A' to s[2] = 'b', there is a change of key.
From s[2] = 'b' to s[3] = 'B', there is no change of key as caps lock or shift is not counted.
From s[3] = 'B' to s[4] = 'c', there is a change of key.
From s[4] = 'c' to s[5] = 'C', there is no change of key as caps lock or shift is not counted.


Example 2:

Input: s = "AaAaAaaA"
Output: 0
Explanation: There is no change of key since only the letters 'a' and 'A' are pressed which does not require change of key.

 
Constraints:

1 <= s.length <= 100
s consists of only upper case and lower case English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last = s[0].lower()
        for ch in s[1:]:
            cur = ch.lower()
            if cur != last:
                changes += 1
            last = cur
        return changes
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            # Count a key change only when the lowercase letters differ.
            # Upper/lower case (shift/caps) doesn't count as a change.
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Count changes when consecutive characters differ by case-insensitive letter.
        # Note: 'a' -> 'A' does NOT count as a key change (same underlying letter).
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last = s[0]
        for ch in s[1:]:
            if ch.lower() != last.lower():
                changes += 1
            last = ch
        return changes
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s:
            return 0
        
        changes = 0
        for i in range(1, len(s)):
            # Only case-insensitive comparison matters.
            # If the letter differs ignoring case, it's a key change.
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Count changes only when the letter case differs (i.e., different key)
        # Same letter differing only by shift/caps doesn't count.
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() == s[i - 1].lower() and s[i] != s[i - 1]:
                # Same key (same letter), just different case due to modifiers
                continue
            if s[i].lower() != s[i - 1].lower() and s[i] != s[i - 1]:
                # Different letters (keys), regardless of case
                changes += 1
            elif s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last = s[0]
        for ch in s[1:]:
            # Case-insensitive key; shift/caps don't count as key changes
            if ch.lower() != last.lower():
                changes += 1
            last = ch
        return changes
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last = s[0].lower()
        for ch in s[1:]:
            cur = ch.lower()
            if cur != last:
                changes += 1
            last = cur
        return changes
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            # Count a key change only when the lowercase letters differ.
            # Upper/lower case (shift/caps) doesn't count as a change.
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Count changes when consecutive characters differ by case-insensitive letter.
        # Note: 'a' -> 'A' does NOT count as a key change (same underlying letter).
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last = s[0]
        for ch in s[1:]:
            if ch.lower() != last.lower():
                changes += 1
            last = ch
        return changes
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s:
            return 0
        
        changes = 0
        for i in range(1, len(s)):
            # Only case-insensitive comparison matters.
            # If the letter differs ignoring case, it's a key change.
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Count changes only when the letter case differs (i.e., different key)
        # Same letter differing only by shift/caps doesn't count.
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() == s[i - 1].lower() and s[i] != s[i - 1]:
                # Same key (same letter), just different case due to modifiers
                continue
            if s[i].lower() != s[i - 1].lower() and s[i] != s[i - 1]:
                # Different letters (keys), regardless of case
                changes += 1
            elif s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last = s[0]
        for ch in s[1:]:
            # Case-insensitive key; shift/caps don't count as key changes
            if ch.lower() != last.lower():
                changes += 1
            last = ch
        return changes
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
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
You are given a 0-indexed string s typed by a user. Changing a key is defined as using a key different from the last used key. For example, s = "ab" has a change of a key while s = "bBBb" does not have any.
Return the number of times the user had to change the key. 
Note: Modifiers like shift or caps lock won't be counted in changing the key that is if a user typed the letter 'a' and then the letter 'A' then it will not be considered as a changing of key.
 
Example 1:

Input: s = "aAbBcC"
Output: 2
Explanation: 
From s[0] = 'a' to s[1] = 'A', there is no change of key as caps lock or shift is not counted.
From s[1] = 'A' to s[2] = 'b', there is a change of key.
From s[2] = 'b' to s[3] = 'B', there is no change of key as caps lock or shift is not counted.
From s[3] = 'B' to s[4] = 'c', there is a change of key.
From s[4] = 'c' to s[5] = 'C', there is no change of key as caps lock or shift is not counted.


Example 2:

Input: s = "AaAaAaaA"
Output: 0
Explanation: There is no change of key since only the letters 'a' and 'A' are pressed which does not require change of key.

 
Constraints:

1 <= s.length <= 100
s consists of only upper case and lower case English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            # Case-insensitive: shift/caps don't count as key change
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last = s[0]
        for ch in s[1:]:
            # Ignore case differences (shift/caps don't count)
            if ch.lower() != last.lower():
                changes += 1
            last = ch
        return changes
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            # Modifiers like shift/caps don't count, so compare case-insensitively
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Count transitions where adjacent characters differ by actual letter
        # (case matters only by character itself; shift/caps differences don't count)
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            # Ignore case: only actual key letter matters, not shift/caps.
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            # Case-insensitive: shift/caps don't count as key change
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last = s[0]
        for ch in s[1:]:
            # Ignore case differences (shift/caps don't count)
            if ch.lower() != last.lower():
                changes += 1
            last = ch
        return changes
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            # Modifiers like shift/caps don't count, so compare case-insensitively
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Count transitions where adjacent characters differ by actual letter
        # (case matters only by character itself; shift/caps differences don't count)
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            # Ignore case: only actual key letter matters, not shift/caps.
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
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
      "expected": "94",
      "actual": "94",
      "error": ""
    },
    {
      "passed": true,
      "expected": "99",
      "actual": "99",
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
      "expected": "95",
      "actual": "95",
      "error": ""
    }
  ]
}
```

</details>
