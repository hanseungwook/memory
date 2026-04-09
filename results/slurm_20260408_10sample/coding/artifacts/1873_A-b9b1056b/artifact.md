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

        # One swap allowed. Check all swaps.
        lst = list(s)
        ok = False
        n = 3
        for a in range(n):
            for b in range(a + 1, n):
                lst[a], lst[b] = lst[b], lst[a]
                if "".join(lst) == target:
                    ok = True
                    lst[a], lst[b] = lst[b], lst[a]
                    break
                lst[a], lst[b] = lst[b], lst[a]
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
<summary>Generation 2</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    ans = []
    for i in range(1, t + 1):
        s = data[i]
        # If already correct, or one swap away to reach "abc"
        if s == target:
            ans.append("YES")
            continue

        # For 3 chars, there are exactly 3 possible swaps: (0,1), (0,2), (1,2)
        possible = False
        a = list(s)
        pairs = [(0, 1), (0, 2), (1, 2)]
        for x, y in pairs:
            a[x], a[y] = a[y], a[x]
            if ''.join(a) == target:
                possible = True
                break
            a[x], a[y] = a[y], a[x]  # swap back
        ans.append("YES" if possible else "NO")

    sys.stdout.write("\n".join(ans))

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
    target = "abc"
    out = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        if s == target:
            out.append("YES")
        else:
            # Check if s can become target with at most one swap.
            # With 3 elements, "at most one swap" <=> either 0 mismatches or exactly 2 mismatches.
            mism = [i for i in range(3) if s[i] != target[i]]
            if len(mism) == 2:
                i, j = mism
                lst = list(s)
                lst[i], lst[j] = lst[j], lst[i]
                out.append("YES" if ''.join(lst) == target else "NO")
            else:
                out.append("NO")
    sys.stdout.write("\n".join(out))

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
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        a, b, c = s[0], s[1], s[2]
        ok = False

        # Try swapping every pair (at most once)
        arr = list(s)
        pairs = [(0, 1), (0, 2), (1, 2)]
        for i, j in pairs:
            arr[i], arr[j] = arr[j], arr[i]
            if "".join(arr) == target:
                ok = True
            arr[i], arr[j] = arr[j], arr[i]  # swap back
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
<summary>Generation 5</summary>

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
        # If already target, YES
        if s == target:
            ans.append("YES")
            continue

        # Generate all strings reachable by at most one swap (including zero swap already handled)
        arr = list(s)
        possible = False
        n = 3
        for i in range(n):
            for j in range(i + 1, n):
                arr[i], arr[j] = arr[j], arr[i]
                if "".join(arr) == target:
                    possible = True
                    break
                arr[i], arr[j] = arr[j], arr[i]
            if possible:
                break
        ans.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(ans))

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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            ans.append("YES")
            continue
        # one swap allowed => check if target can be obtained by swapping two positions
        # Since only 3 chars, brute force all swaps (including 0 swaps already handled)
        ok = False
        s_list = list(s)
        n = 3
        for a in range(n):
            for b in range(a + 1, n):
                s2 = s_list[:]
                s2[a], s2[b] = s2[b], s2[a]
                if "".join(s2) == target:
                    ok = True
                    break
            if ok:
                break
        ans.append("YES" if ok else "NO")
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
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        # In 3 elements, any single swap can only create strings that differ by swapping
        # two positions. Check all swaps.
        chars = list(s)
        possible = False
        for i in range(3):
            for j in range(i + 1, 3):
                chars[i], chars[j] = chars[j], chars[i]
                if "".join(chars) == target:
                    possible = True
                    break
                chars[i], chars[j] = chars[j], chars[i]
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
<summary>Generation 8</summary>

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
        # With at most one swap, we can always reach abc iff s differs from abc
        # by 0 or exactly 2 positions (any valid swap between those mismatched positions fixes it).
        mismatches = [j for j in range(3) if s[j] != target[j]]
        out.append("YES" if len(mismatches) in (0, 2) else "NO")
    sys.stdout.write("\n".join(out))

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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    for i in range(1, t + 1):
        s = data[i]
        out.append("YES" if s == target or (s != target and True) and (tuple(s) in [
            tuple("abc"), tuple("acb"), tuple("bac"), tuple("bca"), tuple("cab"), tuple("cba")
        ]) else "NO")
    # The above logic is wrong; fix with correct direct check.

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    for i in range(1, t + 1):
        s = data[i]
        pos = {ch: idx for idx, ch in enumerate(s)}
        # Because only permutations of 3 letters exist, we can just compute
        # whether target can be obtained by 0 or 1 swap.
        # Try all swaps including the identity (0 swaps).
        arr = list(s)
        ok = False
        # 0 swaps
        if s == target:
            ok = True
        else:
            # 1 swap
            n = 3
            for a in range(n):
                for b in range(a + 1, n):
                    arr2 = arr[:]
                    arr2[a], arr2[b] = arr2[b], arr2[a]
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
<summary>Generation 10</summary>

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

        # Check if s can become target after exactly one swap.
        # Find first two positions that differ; if swapping them fixes all, it's YES.
        diffs = [i for i in range(3) if s[i] != target[i]]
        if len(diffs) != 2:
            out.append("NO")
            continue
        i, j = diffs
        s_list = list(s)
        s_list[i], s_list[j] = s_list[j], s_list[i]
        out.append("YES" if "".join(s_list) == target else "NO")
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

        # One swap allowed. Check all swaps.
        lst = list(s)
        ok = False
        n = 3
        for a in range(n):
            for b in range(a + 1, n):
                lst[a], lst[b] = lst[b], lst[a]
                if "".join(lst) == target:
                    ok = True
                    lst[a], lst[b] = lst[b], lst[a]
                    break
                lst[a], lst[b] = lst[b], lst[a]
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
<summary>full attempt 2</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    ans = []
    for i in range(1, t + 1):
        s = data[i]
        # If already correct, or one swap away to reach "abc"
        if s == target:
            ans.append("YES")
            continue

        # For 3 chars, there are exactly 3 possible swaps: (0,1), (0,2), (1,2)
        possible = False
        a = list(s)
        pairs = [(0, 1), (0, 2), (1, 2)]
        for x, y in pairs:
            a[x], a[y] = a[y], a[x]
            if ''.join(a) == target:
                possible = True
                break
            a[x], a[y] = a[y], a[x]  # swap back
        ans.append("YES" if possible else "NO")

    sys.stdout.write("\n".join(ans))

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
    target = "abc"
    out = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        if s == target:
            out.append("YES")
        else:
            # Check if s can become target with at most one swap.
            # With 3 elements, "at most one swap" <=> either 0 mismatches or exactly 2 mismatches.
            mism = [i for i in range(3) if s[i] != target[i]]
            if len(mism) == 2:
                i, j = mism
                lst = list(s)
                lst[i], lst[j] = lst[j], lst[i]
                out.append("YES" if ''.join(lst) == target else "NO")
            else:
                out.append("NO")
    sys.stdout.write("\n".join(out))

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
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        a, b, c = s[0], s[1], s[2]
        ok = False

        # Try swapping every pair (at most once)
        arr = list(s)
        pairs = [(0, 1), (0, 2), (1, 2)]
        for i, j in pairs:
            arr[i], arr[j] = arr[j], arr[i]
            if "".join(arr) == target:
                ok = True
            arr[i], arr[j] = arr[j], arr[i]  # swap back
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
<summary>full attempt 5</summary>

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
        # If already target, YES
        if s == target:
            ans.append("YES")
            continue

        # Generate all strings reachable by at most one swap (including zero swap already handled)
        arr = list(s)
        possible = False
        n = 3
        for i in range(n):
            for j in range(i + 1, n):
                arr[i], arr[j] = arr[j], arr[i]
                if "".join(arr) == target:
                    possible = True
                    break
                arr[i], arr[j] = arr[j], arr[i]
            if possible:
                break
        ans.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(ans))

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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            ans.append("YES")
            continue
        # one swap allowed => check if target can be obtained by swapping two positions
        # Since only 3 chars, brute force all swaps (including 0 swaps already handled)
        ok = False
        s_list = list(s)
        n = 3
        for a in range(n):
            for b in range(a + 1, n):
                s2 = s_list[:]
                s2[a], s2[b] = s2[b], s2[a]
                if "".join(s2) == target:
                    ok = True
                    break
            if ok:
                break
        ans.append("YES" if ok else "NO")
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
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue

        # In 3 elements, any single swap can only create strings that differ by swapping
        # two positions. Check all swaps.
        chars = list(s)
        possible = False
        for i in range(3):
            for j in range(i + 1, 3):
                chars[i], chars[j] = chars[j], chars[i]
                if "".join(chars) == target:
                    possible = True
                    break
                chars[i], chars[j] = chars[j], chars[i]
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
<summary>full attempt 8</summary>

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
        # With at most one swap, we can always reach abc iff s differs from abc
        # by 0 or exactly 2 positions (any valid swap between those mismatched positions fixes it).
        mismatches = [j for j in range(3) if s[j] != target[j]]
        out.append("YES" if len(mismatches) in (0, 2) else "NO")
    sys.stdout.write("\n".join(out))

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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    for i in range(1, t + 1):
        s = data[i]
        out.append("YES" if s == target or (s != target and True) and (tuple(s) in [
            tuple("abc"), tuple("acb"), tuple("bac"), tuple("bca"), tuple("cab"), tuple("cba")
        ]) else "NO")
    # The above logic is wrong; fix with correct direct check.

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    for i in range(1, t + 1):
        s = data[i]
        pos = {ch: idx for idx, ch in enumerate(s)}
        # Because only permutations of 3 letters exist, we can just compute
        # whether target can be obtained by 0 or 1 swap.
        # Try all swaps including the identity (0 swaps).
        arr = list(s)
        ok = False
        # 0 swaps
        if s == target:
            ok = True
        else:
            # 1 swap
            n = 3
            for a in range(n):
                for b in range(a + 1, n):
                    arr2 = arr[:]
                    arr2[a], arr2[b] = arr2[b], arr2[a]
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
<summary>full attempt 10</summary>

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

        # Check if s can become target after exactly one swap.
        # Find first two positions that differ; if swapping them fixes all, it's YES.
        diffs = [i for i in range(3) if s[i] != target[i]]
        if len(diffs) != 2:
            out.append("NO")
            continue
        i, j = diffs
        s_list = list(s)
        s_list[i], s_list[j] = s_list[j], s_list[i]
        out.append("YES" if "".join(s_list) == target else "NO")
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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            out.append("YES")
            continue
        # At most one swap: check if s can become target by swapping two positions.
        pos = {}
        for idx, ch in enumerate(s):
            pos[ch] = idx

        # Find the positions where s differs from target
        diffs = [j for j in range(3) if s[j] != target[j]]
        # If already not equal, target can be reached in <=1 swap iff:
        # - they differ in exactly 2 positions and those two chars are the needed ones.
        # (For 3 chars, any other case requires >=2 swaps.)
        if len(diffs) == 2:
            j1, j2 = diffs
            chars = list(s)
            chars[j1], chars[j2] = chars[j2], chars[j1]
            out.append("YES" if "".join(chars) == target else "NO")
        else:
            out.append("NO")
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
    ans = []
    for _ in range(t):
        s = next(it)
        if s == target:
            ans.append("YES")
            continue

        # Try swapping any two positions once
        possible = False
        s_list = list(s)
        for i in range(3):
            for j in range(i + 1, 3):
                b = s_list[:]
                b[i], b[j] = b[j], b[i]
                if "".join(b) == target:
                    possible = True
                    break
            if possible:
                break
        ans.append("YES" if possible else "NO")

    print("\n".join(ans))

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
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # Check whether s can become target by at most one swap
        # (For 3 chars, either already matches or swap the two mismatched positions.)
        idx_mis = [i for i in range(3) if s[i] != target[i]]
        if len(idx_mis) != 2:
            out.append("NO")
            continue
        i, j = idx_mis
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

        # Check if s can become target by swapping at most one pair
        # by comparing mismatch positions.
        mism = [i for i in range(3) if s[i] != target[i]]
        if len(mism) != 2:
            out.append("NO")
        else:
            i, j = mism
            swapped = list(s)
            swapped[i], swapped[j] = swapped[j], swapped[i]
            out.append("YES" if "".join(swapped) == target else "NO")

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
    t = int(data[0])
    ans = []
    target = "abc"

    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            ans.append("YES")
            continue

        # Try at most one swap: generate all swaps of positions (0,1,2)
        chars = list(s)
        possible = False
        for x in range(3):
            for y in range(x + 1, 3):
                chars[x], chars[y] = chars[y], chars[x]
                if ''.join(chars) == target:
                    possible = True
                    chars[x], chars[y] = chars[y], chars[x]
                    break
                chars[x], chars[y] = chars[y], chars[x]
            if possible:
                break

        ans.append("YES" if possible else "NO")

    sys.stdout.write("\n".join(ans))

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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    res = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            res.append("YES")
            continue
        # Check if we can reach target with exactly one swap (or fewer, but s != target already)
        # For any permutation of 3, at most one swap distance can be verified by:
        mismatches = [idx for idx, (x, y) in enumerate(zip(s, target)) if x != y]
        if len(mismatches) != 2:
            res.append("NO")
            continue
        a, b = mismatches
        lst = list(s)
        lst[a], lst[b] = lst[b], lst[a]
        res.append("YES" if "".join(lst) == target else "NO")
    sys.stdout.write("\n".join(res))

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
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # Check if s can reach target by exactly one swap
        lst = list(s)
        # find positions where s differs from target
        diff = [i for i in range(3) if lst[i] != target[i]]
        # If more than 2 positions differ, one swap can't fix it.
        if len(diff) != 2:
            out.append("NO")
            continue
        i, j = diff
        lst[i], lst[j] = lst[j], lst[i]
        out.append("YES" if "".join(lst) == target else "NO")
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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    idx = 1
    out_lines = []
    for _ in range(t):
        s = data[idx]
        idx += 1
        if s == target:
            out_lines.append("YES")
            continue
        if sorted(s) != sorted(target):
            out_lines.append("NO")
            continue

        # Check if s can reach target by at most one swap
        pos = {ch: i for i, ch in enumerate(s)}
        # target positions of each character
        mismatched = [i for i in range(3) if s[i] != target[i]]
        if len(mismatched) == 2:
            i, j = mismatched
            a, b = s[i], s[j]
            # swapping s[i] and s[j] should match target at both positions
            if target[i] == b and target[j] == a:
                out_lines.append("YES")
            else:
                out_lines.append("NO")
        elif len(mismatched) == 0:
            out_lines.append("YES")
        else:
            # 3 mismatched implies need at least 2 swaps
            out_lines.append("NO")

    sys.stdout.write("\n".join(out_lines))

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
    idx = 1
    out = []
    for _ in range(t):
        s = data[idx]
        idx += 1
        if s == target:
            out.append("YES")
            continue
        # Try swapping any one pair and check if it becomes "abc"
        possible = False
        s_list = list(s)
        n = 3
        for i in range(n):
            for j in range(i + 1, n):
                s_list[i], s_list[j] = s_list[j], s_list[i]
                if "".join(s_list) == target:
                    possible = True
                    s_list[i], s_list[j] = s_list[j], s_list[i]
                    break
                s_list[i], s_list[j] = s_list[j], s_list[i]
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
<summary>Baseline generation 10</summary>

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
        # At most one swap: check all strings obtainable by one swap (including none)
        if s == target:
            out.append("YES")
            continue

        chars = list(s)
        ok = False
        n = 3
        for i in range(n):
            for j in range(i + 1, n):
                # swap i, j
                chars[i], chars[j] = chars[j], chars[i]
                if "".join(chars) == target:
                    ok = True
                    break
                # swap back
                chars[i], chars[j] = chars[j], chars[i]
            if ok:
                break
        out.append("YES" if ok else "NO")

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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    out = []
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            out.append("YES")
            continue
        # At most one swap: check if s can become target by swapping two positions.
        pos = {}
        for idx, ch in enumerate(s):
            pos[ch] = idx

        # Find the positions where s differs from target
        diffs = [j for j in range(3) if s[j] != target[j]]
        # If already not equal, target can be reached in <=1 swap iff:
        # - they differ in exactly 2 positions and those two chars are the needed ones.
        # (For 3 chars, any other case requires >=2 swaps.)
        if len(diffs) == 2:
            j1, j2 = diffs
            chars = list(s)
            chars[j1], chars[j2] = chars[j2], chars[j1]
            out.append("YES" if "".join(chars) == target else "NO")
        else:
            out.append("NO")
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
    ans = []
    for _ in range(t):
        s = next(it)
        if s == target:
            ans.append("YES")
            continue

        # Try swapping any two positions once
        possible = False
        s_list = list(s)
        for i in range(3):
            for j in range(i + 1, 3):
                b = s_list[:]
                b[i], b[j] = b[j], b[i]
                if "".join(b) == target:
                    possible = True
                    break
            if possible:
                break
        ans.append("YES" if possible else "NO")

    print("\n".join(ans))

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
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # Check whether s can become target by at most one swap
        # (For 3 chars, either already matches or swap the two mismatched positions.)
        idx_mis = [i for i in range(3) if s[i] != target[i]]
        if len(idx_mis) != 2:
            out.append("NO")
            continue
        i, j = idx_mis
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

        # Check if s can become target by swapping at most one pair
        # by comparing mismatch positions.
        mism = [i for i in range(3) if s[i] != target[i]]
        if len(mism) != 2:
            out.append("NO")
        else:
            i, j = mism
            swapped = list(s)
            swapped[i], swapped[j] = swapped[j], swapped[i]
            out.append("YES" if "".join(swapped) == target else "NO")

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
    t = int(data[0])
    ans = []
    target = "abc"

    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            ans.append("YES")
            continue

        # Try at most one swap: generate all swaps of positions (0,1,2)
        chars = list(s)
        possible = False
        for x in range(3):
            for y in range(x + 1, 3):
                chars[x], chars[y] = chars[y], chars[x]
                if ''.join(chars) == target:
                    possible = True
                    chars[x], chars[y] = chars[y], chars[x]
                    break
                chars[x], chars[y] = chars[y], chars[x]
            if possible:
                break

        ans.append("YES" if possible else "NO")

    sys.stdout.write("\n".join(ans))

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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    res = []
    target = "abc"
    for i in range(1, t + 1):
        s = data[i]
        if s == target:
            res.append("YES")
            continue
        # Check if we can reach target with exactly one swap (or fewer, but s != target already)
        # For any permutation of 3, at most one swap distance can be verified by:
        mismatches = [idx for idx, (x, y) in enumerate(zip(s, target)) if x != y]
        if len(mismatches) != 2:
            res.append("NO")
            continue
        a, b = mismatches
        lst = list(s)
        lst[a], lst[b] = lst[b], lst[a]
        res.append("YES" if "".join(lst) == target else "NO")
    sys.stdout.write("\n".join(res))

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
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    target = "abc"
    out = []
    for _ in range(t):
        s = next(it)
        if s == target:
            out.append("YES")
            continue
        # Check if s can reach target by exactly one swap
        lst = list(s)
        # find positions where s differs from target
        diff = [i for i in range(3) if lst[i] != target[i]]
        # If more than 2 positions differ, one swap can't fix it.
        if len(diff) != 2:
            out.append("NO")
            continue
        i, j = diff
        lst[i], lst[j] = lst[j], lst[i]
        out.append("YES" if "".join(lst) == target else "NO")
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
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    target = "abc"
    idx = 1
    out_lines = []
    for _ in range(t):
        s = data[idx]
        idx += 1
        if s == target:
            out_lines.append("YES")
            continue
        if sorted(s) != sorted(target):
            out_lines.append("NO")
            continue

        # Check if s can reach target by at most one swap
        pos = {ch: i for i, ch in enumerate(s)}
        # target positions of each character
        mismatched = [i for i in range(3) if s[i] != target[i]]
        if len(mismatched) == 2:
            i, j = mismatched
            a, b = s[i], s[j]
            # swapping s[i] and s[j] should match target at both positions
            if target[i] == b and target[j] == a:
                out_lines.append("YES")
            else:
                out_lines.append("NO")
        elif len(mismatched) == 0:
            out_lines.append("YES")
        else:
            # 3 mismatched implies need at least 2 swaps
            out_lines.append("NO")

    sys.stdout.write("\n".join(out_lines))

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
    idx = 1
    out = []
    for _ in range(t):
        s = data[idx]
        idx += 1
        if s == target:
            out.append("YES")
            continue
        # Try swapping any one pair and check if it becomes "abc"
        possible = False
        s_list = list(s)
        n = 3
        for i in range(n):
            for j in range(i + 1, n):
                s_list[i], s_list[j] = s_list[j], s_list[i]
                if "".join(s_list) == target:
                    possible = True
                    s_list[i], s_list[j] = s_list[j], s_list[i]
                    break
                s_list[i], s_list[j] = s_list[j], s_list[i]
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
<summary>Augmented generation 10</summary>

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
        # At most one swap: check all strings obtainable by one swap (including none)
        if s == target:
            out.append("YES")
            continue

        chars = list(s)
        ok = False
        n = 3
        for i in range(n):
            for j in range(i + 1, n):
                # swap i, j
                chars[i], chars[j] = chars[j], chars[i]
                if "".join(chars) == target:
                    ok = True
                    break
                # swap back
                chars[i], chars[j] = chars[j], chars[i]
            if ok:
                break
        out.append("YES" if ok else "NO")

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
