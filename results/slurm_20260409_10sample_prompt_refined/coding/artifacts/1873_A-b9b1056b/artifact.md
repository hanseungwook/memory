# Problem 1873_A

- Domain: `coding`

## Problem

```text
There are three cards with letters $\texttt{a}$, $\texttt{b}$, $\texttt{c}$ placed in a row in some order. You can do the following operation at most once: 

 
-  Pick two cards, and swap them.  Is it possible that the row becomes $\texttt{abc}$ after the operation? Output "YES" if it is possible, and "NO" otherwise.

Input

The first line contains a single integer $t$ ($1 \leq t \leq 6$) — the number of test cases.

The only line of each test case contains a single string consisting of each of the three characters $\texttt{a}$, $\texttt{b}$, and $\texttt{c}$ exactly once, representing the cards.

Output

For each test case, output "YES" if you can make the row $\texttt{abc}$ with at most one operation, or "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).Sample Input 1:
6

abc

acb

bac

bca

cab

cba



Sample Output 1:

YES
YES
YES
NO
NO
YES


Note

In the first test case, we don't need to do any operations, since the row is already $\texttt{abc}$.

In the second test case, we can swap $\texttt{c}$ and $\texttt{b}$: $\texttt{acb} \to \texttt{abc}$.

In the third test case, we can swap $\texttt{b}$ and $\texttt{a}$: $\texttt{bac} \to \texttt{abc}$.

In the fourth test case, it is impossible to make $\texttt{abc}$ using at most one operation.
```

### Test Cases

```json
[
  {
    "input": "6\nabc\nacb\nbac\nbca\ncab\ncba\n",
    "output": "YES\nYES\nYES\nNO\nNO\nYES\n",
    "testtype": "stdin"
  },
  {
    "input": "1\nabc\n",
    "output": "YES\n",
    "testtype": "stdin"
  },
  {
    "input": "3\nabc\nabc\nabc\n",
    "output": "YES\nYES\nYES\n",
    "testtype": "stdin"
  },
  {
    "input": "5\ncab\nacb\ncba\nbac\nbca\n",
    "output": "NO\nYES\nYES\nYES\nNO\n",
    "testtype": "stdin"
  },
  {
    "input": "6\nabc\nabc\nabc\nabc\nabc\nabc\n",
    "output": "YES\nYES\nYES\nYES\nYES\nYES\n",
    "testtype": "stdin"
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
There are three cards with letters $\texttt{a}$, $\texttt{b}$, $\texttt{c}$ placed in a row in some order. You can do the following operation at most once: 

 
-  Pick two cards, and swap them.  Is it possible that the row becomes $\texttt{abc}$ after the operation? Output "YES" if it is possible, and "NO" otherwise.

Input

The first line contains a single integer $t$ ($1 \leq t \leq 6$) — the number of test cases.

The only line of each test case contains a single string consisting of each of the three characters $\texttt{a}$, $\texttt{b}$, and $\texttt{c}$ exactly once, representing the cards.

Output

For each test case, output "YES" if you can make the row $\texttt{abc}$ with at most one operation, or "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).Sample Input 1:
6

abc

acb

bac

bca

cab

cba



Sample Output 1:

YES
YES
YES
NO
NO
YES


Note

In the first test case, we don't need to do any operations, since the row is already $\texttt{abc}$.

In the second test case, we can swap $\texttt{c}$ and $\texttt{b}$: $\texttt{acb} \to \texttt{abc}$.

In the third test case, we can swap $\texttt{b}$ and $\texttt{a}$: $\texttt{bac} \to \texttt{abc}$.

In the fourth test case, it is impossible to make $\texttt{abc}$ using at most one operation.

### Format: Read the inputs from stdin solve the problem and write the answer to stdout (do not directly test on the sample inputs). Enclose your code within delimiters as follows. Ensure that when the python program runs, it reads the inputs, runs the algorithm and writes output to STDOUT.
```python
# YOUR CODE HERE
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            out.append("YES")
            continue
        # Check if target can be obtained by swapping exactly one pair
        pos = [(ch, idx) for idx, ch in enumerate(s) for ch2 in [ch] if True]  # not needed
        diff = [j for j in range(3) if s[j] != target[j]]
        # With 3 distinct letters, any one swap can only fix if mismatches are 2
        if len(diff) != 2:
            out.append("NO")
            continue
        a, b = diff
        s_list = list(s)
        s_list[a], s_list[b] = s_list[b], s_list[a]
        out.append("YES" if "".join(s_list) == target else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        arr = list(s)
        n = 3

        # Check if there exists at least one swap (i<j) that makes it "abc"
        ok = False
        for i in range(n):
            for j in range(i + 1, n):
                arr2 = arr[:]
                arr2[i], arr2[j] = arr2[j], arr2[i]
                if "".join(arr2) == target:
                    ok = True
                    break
            if ok:
                break

        out.append("YES" if ok else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    for i in range(1, t + 1):
        s = data[i]
        ans.append("YES" if s == "abc" or s in {"acb", "bac", "cba"} else "NO")
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    out = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            out.append("YES")
            continue

        # Count positions that differ from target
        diff = sum(1 for a, b in zip(s, target) if a != b)

        # A single swap can fix exactly:
        # - 0 mismatches (already handled)
        # - 2 mismatches (swap those two positions)
        # - 3 mismatches only if the permutation is a 3-cycle; but a single swap
        #   cannot transform one 3-cycle into identity (it would require 2 swaps).
        out.append("YES" if diff == 2 else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # Any swap is allowed at most once, so just check if s can become target by one swap
        # Compute mismatched indices
        mism = [i for i in range(3) if s[i] != target[i]]
        if len(mism) == 2:
            i, j = mism
            lst = list(s)
            lst[i], lst[j] = lst[j], lst[i]
            out.append("YES" if "".join(lst) == target else "NO")
        else:
            # If 0 -> already handled, if 3 -> would require more than one swap
            out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    ans = []
    for _ in range(t):
        s = next(it)
        if s == target:
            ans.append("YES")
            continue
        # Count mismatched positions relative to "abc"
        mismatches = [i for i in range(3) if s[i] != target[i]]
        # With one swap, we can fix at most 2 mismatched positions.
        # For 3 chars, the only solvable non-identity cases have exactly 2 mismatches.
        ans.append("YES" if len(mismatches) == 2 else "NO")
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    res = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            res.append("YES")
            continue
        # With one swap, positions that are already correct must remain correct.
        diff = [j for j in range(3) if s[j] != target[j]]
        if len(diff) == 2:
            a, b = diff
            lst = list(s)
            lst[a], lst[b] = lst[b], lst[a]
            res.append("YES" if "".join(lst) == target else "NO")
        else:
            res.append("NO")
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    target = "abc"

    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            ans.append("YES")
            continue
        # Check if s can be turned into target by swapping at most one pair
        mismatch = [j for j in range(3) if s[j] != target[j]]
        # If already different at exactly 2 positions, one swap may fix it
        if len(mismatch) == 2:
            a, b = mismatch
            s_list = list(s)
            s_list[a], s_list[b] = s_list[b], s_list[a]
            ans.append("YES" if ''.join(s_list) == target else "NO")
        else:
            ans.append("NO")

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # If it's exactly one swap away from "abc"
        # Since length is 3, we can just try all swaps (3C2 = 3).
        a = list(s)
        possible = False
        for i in range(3):
            for j in range(i+1, 3):
                b = a[:]
                b[i], b[j] = b[j], b[i]
                if ''.join(b) == target:
                    possible = True
                    break
            if possible:
                break
        out.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []

    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            out.append("YES")
            continue

        # Count positions that differ from target
        diff = sum(1 for a, b in zip(s, target) if a != b)

        # With one swap, the number of differing positions can be:
        # - 2 (swap the two misplaced cards to match)
        # - 0 (already handled)
        # If diff == 2, it's always fixable by swapping those two positions.
        out.append("YES" if diff == 2 else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            out.append("YES")
            continue
        # Check if target can be obtained by swapping exactly one pair
        pos = [(ch, idx) for idx, ch in enumerate(s) for ch2 in [ch] if True]  # not needed
        diff = [j for j in range(3) if s[j] != target[j]]
        # With 3 distinct letters, any one swap can only fix if mismatches are 2
        if len(diff) != 2:
            out.append("NO")
            continue
        a, b = diff
        s_list = list(s)
        s_list[a], s_list[b] = s_list[b], s_list[a]
        out.append("YES" if "".join(s_list) == target else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        arr = list(s)
        n = 3

        # Check if there exists at least one swap (i<j) that makes it "abc"
        ok = False
        for i in range(n):
            for j in range(i + 1, n):
                arr2 = arr[:]
                arr2[i], arr2[j] = arr2[j], arr2[i]
                if "".join(arr2) == target:
                    ok = True
                    break
            if ok:
                break

        out.append("YES" if ok else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    for i in range(1, t + 1):
        s = data[i]
        ans.append("YES" if s == "abc" or s in {"acb", "bac", "cba"} else "NO")
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    out = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            out.append("YES")
            continue

        # Count positions that differ from target
        diff = sum(1 for a, b in zip(s, target) if a != b)

        # A single swap can fix exactly:
        # - 0 mismatches (already handled)
        # - 2 mismatches (swap those two positions)
        # - 3 mismatches only if the permutation is a 3-cycle; but a single swap
        #   cannot transform one 3-cycle into identity (it would require 2 swaps).
        out.append("YES" if diff == 2 else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # Any swap is allowed at most once, so just check if s can become target by one swap
        # Compute mismatched indices
        mism = [i for i in range(3) if s[i] != target[i]]
        if len(mism) == 2:
            i, j = mism
            lst = list(s)
            lst[i], lst[j] = lst[j], lst[i]
            out.append("YES" if "".join(lst) == target else "NO")
        else:
            # If 0 -> already handled, if 3 -> would require more than one swap
            out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    ans = []
    for _ in range(t):
        s = next(it)
        if s == target:
            ans.append("YES")
            continue
        # Count mismatched positions relative to "abc"
        mismatches = [i for i in range(3) if s[i] != target[i]]
        # With one swap, we can fix at most 2 mismatched positions.
        # For 3 chars, the only solvable non-identity cases have exactly 2 mismatches.
        ans.append("YES" if len(mismatches) == 2 else "NO")
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    res = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            res.append("YES")
            continue
        # With one swap, positions that are already correct must remain correct.
        diff = [j for j in range(3) if s[j] != target[j]]
        if len(diff) == 2:
            a, b = diff
            lst = list(s)
            lst[a], lst[b] = lst[b], lst[a]
            res.append("YES" if "".join(lst) == target else "NO")
        else:
            res.append("NO")
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    target = "abc"

    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            ans.append("YES")
            continue
        # Check if s can be turned into target by swapping at most one pair
        mismatch = [j for j in range(3) if s[j] != target[j]]
        # If already different at exactly 2 positions, one swap may fix it
        if len(mismatch) == 2:
            a, b = mismatch
            s_list = list(s)
            s_list[a], s_list[b] = s_list[b], s_list[a]
            ans.append("YES" if ''.join(s_list) == target else "NO")
        else:
            ans.append("NO")

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # If it's exactly one swap away from "abc"
        # Since length is 3, we can just try all swaps (3C2 = 3).
        a = list(s)
        possible = False
        for i in range(3):
            for j in range(i+1, 3):
                b = a[:]
                b[i], b[j] = b[j], b[i]
                if ''.join(b) == target:
                    possible = True
                    break
            if possible:
                break
        out.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []

    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            out.append("YES")
            continue

        # Count positions that differ from target
        diff = sum(1 for a, b in zip(s, target) if a != b)

        # With one swap, the number of differing positions can be:
        # - 2 (swap the two misplaced cards to match)
        # - 0 (already handled)
        # If diff == 2, it's always fixable by swapping those two positions.
        out.append("YES" if diff == 2 else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
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
There are three cards with letters $\texttt{a}$, $\texttt{b}$, $\texttt{c}$ placed in a row in some order. You can do the following operation at most once: 

 
-  Pick two cards, and swap them.  Is it possible that the row becomes $\texttt{abc}$ after the operation? Output "YES" if it is possible, and "NO" otherwise.

Input

The first line contains a single integer $t$ ($1 \leq t \leq 6$) — the number of test cases.

The only line of each test case contains a single string consisting of each of the three characters $\texttt{a}$, $\texttt{b}$, and $\texttt{c}$ exactly once, representing the cards.

Output

For each test case, output "YES" if you can make the row $\texttt{abc}$ with at most one operation, or "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).Sample Input 1:
6

abc

acb

bac

bca

cab

cba



Sample Output 1:

YES
YES
YES
NO
NO
YES


Note

In the first test case, we don't need to do any operations, since the row is already $\texttt{abc}$.

In the second test case, we can swap $\texttt{c}$ and $\texttt{b}$: $\texttt{acb} \to \texttt{abc}$.

In the third test case, we can swap $\texttt{b}$ and $\texttt{a}$: $\texttt{bac} \to \texttt{abc}$.

In the fourth test case, it is impossible to make $\texttt{abc}$ using at most one operation.

### Format: Read the inputs from stdin solve the problem and write the answer to stdout (do not directly test on the sample inputs). Enclose your code within delimiters as follows. Ensure that when the python program runs, it reads the inputs, runs the algorithm and writes output to STDOUT.
```python
# YOUR CODE HERE
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # One swap can fix it iff we can obtain target by swapping exactly one pair
        # (or at most once, but swapping 0 is already handled above).
        chars = list(s)
        n = 3
        possible = False
        for i in range(n):
            for j in range(i + 1, n):
                chars[i], chars[j] = chars[j], chars[i]
                if "".join(chars) == target:
                    possible = True
                    chars[i], chars[j] = chars[j], chars[i]  # revert
                    break
                chars[i], chars[j] = chars[j], chars[i]  # revert
            if possible:
                break
        out.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # In a permutation of length 3, any single swap results from swapping
        # some pair positions. Check if any gives the target.
        s_list = list(s)
        possible = False
        for i in range(3):
            for j in range(i + 1, 3):
                b = s_list[:]          # copy
                b[i], b[j] = b[j], b[i]
                if "".join(b) == target:
                    possible = True
                    break
            if possible:
                break
        out.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    res = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            res.append("YES")
            continue
        # If we can reach target by at most one swap, then the strings must differ
        # only in positions involved by a single swap (i.e., exactly 2 mismatches)
        mism = [idx for idx, (x, y) in enumerate(zip(s, target)) if x != y]
        res.append("YES" if len(mism) == 2 else "NO")
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        # Try all swaps once and check if any gives "abc"
        chars = list(s)
        ok = False
        n = 3
        for i in range(n):
            for j in range(i + 1, n):
                tmp = chars[:]
                tmp[i], tmp[j] = tmp[j], tmp[i]
                if "".join(tmp) == target:
                    ok = True
                    break
            if ok:
                break
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    target = "abc"
    out = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        if s == target:
            out.append("YES")
            continue
        # Try all swaps of two positions once
        arr = list(s)
        possible = False
        for i in range(3):
            for j in range(i + 1, 3):
                arr2 = arr[:]
                arr2[i], arr2[j] = arr2[j], arr2[i]
                if "".join(arr2) == target:
                    possible = True
                    break
            if possible:
                break
        out.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        # If we can sort to "abc" with at most one swap,
        # then the number of mismatched positions between s and target
        # must be 0 or 2 (a single swap fixes two positions).
        mismatches = [i for i in range(3) if s[i] != target[i]]
        if len(mismatches) != 2:
            out.append("NO")
            continue

        i, j = mismatches
        # Check that swapping the mismatched positions makes it equal.
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        out.append("YES" if "".join(lst) == target else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    idx = 1
    out = []
    for _ in range(t):
        s = data[idx]
        idx += 1
        out.append("YES" if s == target else "YES" if sorted(s) == ['a','b','c'] and (s.index('a') != 0 or s.index('b') != 1 or s.index('c') != 2) and True else "NO")

    # The above logic is overly complicated; fix with correct approach below.

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    idx = 1
    out = []
    for _ in range(t):
        s = data[idx]; idx += 1
        if s == target:
            out.append("YES")
            continue
        # Determine if s can be turned into target by at most one swap
        pos = {ch: i for i, ch in enumerate(s)}
        # positions in target for each character
        # we can simulate all swaps that differ from target and see if any works in 1 swap
        found = False
        for i in range(3):
            for j in range(i+1, 3):
                lst = list(s)
                lst[i], lst[j] = lst[j], lst[i]
                if ''.join(lst) == target:
                    found = True
                    break
            if found:
                break
        out.append("YES" if found else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    ans = []
    target = "abc"
    for _ in range(t):
        s = next(it)
        if s == target:
            ans.append("YES")
        else:
            # Can we sort to "abc" in at most one swap?
            # Since only 3 chars, just check all single swaps.
            lst = list(s)
            ok = False
            for i in range(3):
                for j in range(i + 1, 3):
                    lst[i], lst[j] = lst[j], lst[i]
                    if "".join(lst) == target:
                        ok = True
                        break
                    lst[i], lst[j] = lst[j], lst[i]
                if ok:
                    break
            ans.append("YES" if ok else "NO")
    print("\n".join(ans))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        # If already target, YES; otherwise check if exactly one swap can make it.
        if s == target:
            out.append("YES")
            continue

        pos = {ch: i for i, ch in enumerate(s)}
        # Find swaps that could place 'a','b','c' into target positions
        # Since only 3 letters, at most 3 possible swaps.
        swapped = False
        arr = list(s)
        swaps = [(0,1), (0,2), (1,2)]
        for i, j in swaps:
            arr[i], arr[j] = arr[j], arr[i]
            if ''.join(arr) == target:
                swapped = True
                arr[i], arr[j] = arr[j], arr[i]  # restore
                break
            arr[i], arr[j] = arr[j], arr[i]  # restore
        out.append("YES" if swapped else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        # Count mismatched positions with target
        mismatches = sum(1 for i in range(3) if s[i] != target[i])
        # With at most one swap, we can fix the permutation if:
        # - already correct (0 mismatches), or
        # - exactly 2 positions differ (one swap can fix), or
        # - exactly 3 positions differ means it's a 3-cycle -> needs 2 swaps, not allowed
        out.append("YES" if mismatches in (0, 2) else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # One swap can fix it iff we can obtain target by swapping exactly one pair
        # (or at most once, but swapping 0 is already handled above).
        chars = list(s)
        n = 3
        possible = False
        for i in range(n):
            for j in range(i + 1, n):
                chars[i], chars[j] = chars[j], chars[i]
                if "".join(chars) == target:
                    possible = True
                    chars[i], chars[j] = chars[j], chars[i]  # revert
                    break
                chars[i], chars[j] = chars[j], chars[i]  # revert
            if possible:
                break
        out.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # In a permutation of length 3, any single swap results from swapping
        # some pair positions. Check if any gives the target.
        s_list = list(s)
        possible = False
        for i in range(3):
            for j in range(i + 1, 3):
                b = s_list[:]          # copy
                b[i], b[j] = b[j], b[i]
                if "".join(b) == target:
                    possible = True
                    break
            if possible:
                break
        out.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    res = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            res.append("YES")
            continue
        # If we can reach target by at most one swap, then the strings must differ
        # only in positions involved by a single swap (i.e., exactly 2 mismatches)
        mism = [idx for idx, (x, y) in enumerate(zip(s, target)) if x != y]
        res.append("YES" if len(mism) == 2 else "NO")
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        # Try all swaps once and check if any gives "abc"
        chars = list(s)
        ok = False
        n = 3
        for i in range(n):
            for j in range(i + 1, n):
                tmp = chars[:]
                tmp[i], tmp[j] = tmp[j], tmp[i]
                if "".join(tmp) == target:
                    ok = True
                    break
            if ok:
                break
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    target = "abc"
    out = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        if s == target:
            out.append("YES")
            continue
        # Try all swaps of two positions once
        arr = list(s)
        possible = False
        for i in range(3):
            for j in range(i + 1, 3):
                arr2 = arr[:]
                arr2[i], arr2[j] = arr2[j], arr2[i]
                if "".join(arr2) == target:
                    possible = True
                    break
            if possible:
                break
        out.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        # If we can sort to "abc" with at most one swap,
        # then the number of mismatched positions between s and target
        # must be 0 or 2 (a single swap fixes two positions).
        mismatches = [i for i in range(3) if s[i] != target[i]]
        if len(mismatches) != 2:
            out.append("NO")
            continue

        i, j = mismatches
        # Check that swapping the mismatched positions makes it equal.
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        out.append("YES" if "".join(lst) == target else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    idx = 1
    out = []
    for _ in range(t):
        s = data[idx]
        idx += 1
        out.append("YES" if s == target else "YES" if sorted(s) == ['a','b','c'] and (s.index('a') != 0 or s.index('b') != 1 or s.index('c') != 2) and True else "NO")

    # The above logic is overly complicated; fix with correct approach below.

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    idx = 1
    out = []
    for _ in range(t):
        s = data[idx]; idx += 1
        if s == target:
            out.append("YES")
            continue
        # Determine if s can be turned into target by at most one swap
        pos = {ch: i for i, ch in enumerate(s)}
        # positions in target for each character
        # we can simulate all swaps that differ from target and see if any works in 1 swap
        found = False
        for i in range(3):
            for j in range(i+1, 3):
                lst = list(s)
                lst[i], lst[j] = lst[j], lst[i]
                if ''.join(lst) == target:
                    found = True
                    break
            if found:
                break
        out.append("YES" if found else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    ans = []
    target = "abc"
    for _ in range(t):
        s = next(it)
        if s == target:
            ans.append("YES")
        else:
            # Can we sort to "abc" in at most one swap?
            # Since only 3 chars, just check all single swaps.
            lst = list(s)
            ok = False
            for i in range(3):
                for j in range(i + 1, 3):
                    lst[i], lst[j] = lst[j], lst[i]
                    if "".join(lst) == target:
                        ok = True
                        break
                    lst[i], lst[j] = lst[j], lst[i]
                if ok:
                    break
            ans.append("YES" if ok else "NO")
    print("\n".join(ans))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        # If already target, YES; otherwise check if exactly one swap can make it.
        if s == target:
            out.append("YES")
            continue

        pos = {ch: i for i, ch in enumerate(s)}
        # Find swaps that could place 'a','b','c' into target positions
        # Since only 3 letters, at most 3 possible swaps.
        swapped = False
        arr = list(s)
        swaps = [(0,1), (0,2), (1,2)]
        for i, j in swaps:
            arr[i], arr[j] = arr[j], arr[i]
            if ''.join(arr) == target:
                swapped = True
                arr[i], arr[j] = arr[j], arr[i]  # restore
                break
            arr[i], arr[j] = arr[j], arr[i]  # restore
        out.append("YES" if swapped else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        # Count mismatched positions with target
        mismatches = sum(1 for i in range(3) if s[i] != target[i])
        # With at most one swap, we can fix the permutation if:
        # - already correct (0 mismatches), or
        # - exactly 2 positions differ (one swap can fix), or
        # - exactly 3 positions differ means it's a 3-cycle -> needs 2 swaps, not allowed
        out.append("YES" if mismatches in (0, 2) else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
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
  "passed": 5,
  "total": 5,
  "cases": [
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nNO\nNO\nYES",
      "actual": "YES\nYES\nYES\nNO\nNO\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES",
      "actual": "YES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES",
      "actual": "YES\nYES\nYES",
      "error": ""
    },
    {
      "passed": true,
      "expected": "NO\nYES\nYES\nYES\nNO",
      "actual": "NO\nYES\nYES\nYES\nNO",
      "error": ""
    },
    {
      "passed": true,
      "expected": "YES\nYES\nYES\nYES\nYES\nYES",
      "actual": "YES\nYES\nYES\nYES\nYES\nYES",
      "error": ""
    }
  ]
}
```

</details>
