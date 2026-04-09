# Problem abc301_a

- Domain: `coding`

## Problem

```text
Takahashi and Aoki played N games.
You are given a string S of length N, representing the results of these games.
Takahashi won the i-th game if the i-th character of S is T, and Aoki won that game if it is A.
The overall winner between Takahashi and Aoki is the one who won more games than the other.
If they had the same number of wins, the overall winner is the one who reached that number of wins first.
Find the overall winner: Takahashi or Aoki.

Input

The input is given from Standard Input in the following format:
N
S

Output

If the overall winner is Takahashi, print T; if it is Aoki, print A.

Constraints


- 1\leq N \leq 100
- N is an integer.
- S is a string of length N consisting of T and A.

Sample Input 1

5
TTAAT

Sample Output 1

T

Takahashi won three games, and Aoki won two.
Thus, the overall winner is Takahashi, who won more games.

Sample Input 2

6
ATTATA

Sample Output 2

T

Both Takahashi and Aoki won three games.
Takahashi reached three wins in the fifth game, and Aoki in the sixth game.
Thus, the overall winner is Takahashi, who reached three wins first.

Sample Input 3

1
A

Sample Output 3

A
```

### Test Cases

```json
[
  {
    "input": "5\nTTAAT\n",
    "output": "T\n",
    "testtype": "stdin"
  },
  {
    "input": "6\nATTATA\n",
    "output": "T\n",
    "testtype": "stdin"
  },
  {
    "input": "1\nA\n",
    "output": "A\n",
    "testtype": "stdin"
  },
  {
    "input": "90\nATTTTATATATTATTAATATATTAATTATTAAATTAAATTATTTATTAATAAAAATATTATTTTAATAAAAATTAAAAAAAATATTTTTT\n",
    "output": "A\n",
    "testtype": "stdin"
  },
  {
    "input": "91\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n",
    "output": "A\n",
    "testtype": "stdin"
  },
  {
    "input": "92\nAATAAAAAAATATAAAAAAAAATAAAAAAATAAATAAAAAAAAAAAAAAAAATAAAAAAAAAATAAAAAATAAAATAAAATAAAAAATATAA\n",
    "output": "A\n",
    "testtype": "stdin"
  },
  {
    "input": "92\nATTTAAATTTTAAAAATAAATTTAAAATTAAAATTAAAAATAATTTTAATTTATATTTATTTAATTTTATAAATAATTTTTATATAATATTA\n",
    "output": "T\n",
    "testtype": "stdin"
  },
  {
    "input": "92\nATTTTTATTTTTATTATTTTAATATTTAAATTAATTTATTAAATTTTATTTTAAATATATTTAAATAATATTATTAAATTAATATTTAAATA\n",
    "output": "T\n",
    "testtype": "stdin"
  },
  {
    "input": "92\nATATTTAAATAATTTTATTAATTATTTAATATTTTTATTATTTAATTTAATTTAAATATATAATATAAAAAATTATAAATTATAAAATAAAT\n",
    "output": "A\n",
    "testtype": "stdin"
  },
  {
    "input": "93\nTTAAAATTTTATAATAAAAAAAATAATAAATTTTATTTAATAATAAATAAAAAAAAAAAATTTTTATTATATTTATATTTTTAAAAATTATAA\n",
    "output": "A\n",
    "testtype": "stdin"
  },
  {
    "input": "93\nTTTATTATTATATTTTTATATTTTATTTTTTAAATTTTATAATTTTTATTTTTTATTTATATTTATTTAAATTTTATATTTATTATATTTTTA\n",
    "output": "T\n",
    "testtype": "stdin"
  },
  {
    "input": "96\nTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT\n",
    "output": "T\n",
    "testtype": "stdin"
  },
  {
    "input": "97\nTTTTTTTTTATTTATTTTTTTATTTTTTTTTATTAAATTTATTTTTTTTTTTTTATTTTTTTATTTTTAATTTTTTTTTATTTTTTATTTTTTTTTT\n",
    "output": "T\n",
    "testtype": "stdin"
  },
  {
    "input": "98\nTTAATATTATATAATTAAAATAATTTATATAAATTAATAATTATTTATAATATATAATAAATAATAATTTATAATAATTTTTATATTTATTATAATTA\n",
    "output": "T\n",
    "testtype": "stdin"
  },
  {
    "input": "100\nAAAAAAAAAAAAAAAAAAAAAAAATTTAAAAATATTATAAAATATAATAATTAAAAAAAAATATTTATTTATAAAATATAAAATAATTAAATATATAATA\n",
    "output": "A\n",
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
Takahashi and Aoki played N games.
You are given a string S of length N, representing the results of these games.
Takahashi won the i-th game if the i-th character of S is T, and Aoki won that game if it is A.
The overall winner between Takahashi and Aoki is the one who won more games than the other.
If they had the same number of wins, the overall winner is the one who reached that number of wins first.
Find the overall winner: Takahashi or Aoki.

Input

The input is given from Standard Input in the following format:
N
S

Output

If the overall winner is Takahashi, print T; if it is Aoki, print A.

Constraints


- 1\leq N \leq 100
- N is an integer.
- S is a string of length N consisting of T and A.

Sample Input 1

5
TTAAT

Sample Output 1

T

Takahashi won three games, and Aoki won two.
Thus, the overall winner is Takahashi, who won more games.

Sample Input 2

6
ATTATA

Sample Output 2

T

Both Takahashi and Aoki won three games.
Takahashi reached three wins in the fifth game, and Aoki in the sixth game.
Thus, the overall winner is Takahashi, who reached three wins first.

Sample Input 3

1
A

Sample Output 3

A

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
    n = int(data[0])
    s = data[1].strip()

    t = 0  # Takahashi wins
    a = 0  # Aoki wins

    for i, ch in enumerate(s, start=1):
        if ch == 'T':
            t += 1
        else:
            a += 1

        # If someone is ahead, they are the overall winner.
        # If tied, keep going; the rules say the one who reaches the target first wins.
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

    # If never differs (shouldn't happen given N>=1), decide by who reached first.
    # But as written above, difference will occur at some point for any non-empty string.
    # Fallback:
    print('T' if t >= a else 'A')

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

def main():
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    S = input_data[1]

    t_wins = 0
    a_wins = 0
    target_t = None
    target_a = None

    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            t_wins += 1
            if t_wins > a_wins:
                print('T')
                return
            if t_wins == a_wins:
                # If equal now, winner depends on who reached the higher wins first.
                # That happens only when one surpasses the other, so continue.
                pass
        else:  # 'A'
            a_wins += 1
            if a_wins > t_wins:
                print('A')
                return

    # If reached here, neither ever surpassed the other -> must be ties, so
    # by rule the one who reached that number of wins first wins.
    # We'll compute with a second pass for first reaching the max wins.
    max_wins = max(t_wins, a_wins)
    t_first = None
    a_first = None
    tw = aw = 0
    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            tw += 1
            if tw == max_wins:
                t_first = i
                break
        else:
            aw += 1
            if aw == max_wins:
                a_first = i
                break

    # If t_wins == a_wins, only one of the first indices will have occurred first
    # based on loop order; compute properly:
    # Actually loop above stops at first max_wins reached by either; so decide by ch.
    # Simpler: redo properly.
    tw = aw = 0
    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            tw += 1
            if tw == max_wins:
                print('T')
                return
        else:
            aw += 1
            if aw == max_wins:
                print('A')
                return

if __name__ == "__main__":
    main()
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
    N = int(data[0])
    S = data[1].strip()

    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t == a:
            continue
        # someone has more wins; determine which reached first to this higher count
        # But the problem's rule about "same number of wins reached first" means:
        # As we iterate, the first time someone becomes strictly greater than the other,
        # their current win count is the winner's final tie/break condition.
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

    # For completeness (should always return within loop)
    print('T' if t > a else 'A')

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
    N = int(data[0])
    S = data[1].strip()

    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t > a:
            # first to make t strictly greater than a wins overall
            # but per problem: if same wins, whoever reached that count first
            # We can handle directly by checking when someone reaches final count.
            pass

    # Better approach: track first time reaching the final win count.
    total_t = S.count('T')
    total_a = N - total_t

    if total_t > total_a:
        target = total_t
        count = 0
        for ch in S:
            if ch == 'T':
                count += 1
                if count == target:
                    print('T')
                    return
    elif total_a > total_t:
        target = total_a
        count = 0
        for ch in S:
            if ch == 'A':
                count += 1
                if count == target:
                    print('A')
                    return
    else:
        # same wins: whoever reaches that number first
        target = total_t
        t = a = 0
        for ch in S:
            if ch == 'T':
                t += 1
                if t == target:
                    print('T')
                    return
            else:
                a += 1
                if a == target:
                    print('A')
                    return

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
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1].strip()

    t_cnt = 0
    a_cnt = 0

    for ch in s:
        if ch == 'T':
            t_cnt += 1
            if t_cnt > a_cnt:
                print('T')
                return
        else:  # 'A'
            a_cnt += 1
            if a_cnt > t_cnt:
                print('A')
                return

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
    n = int(data[0])
    s = data[1].strip()

    t_wins = 0
    a_wins = 0

    for ch in s:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

        if t_wins > a_wins:
            print('T')
            return
        if a_wins > t_wins:
            print('A')
            return

    # If counts are equal after N games, the one who first reached the final max
    # wins is the one whose winning count reached max earlier.
    # But with the above loop, one side would have exceeded the other unless equal.
    # Therefore, determine by first occurrence of max wins.
    max_w = max(t_wins, a_wins)
    t_idx = next((i for i, ch in enumerate(s, 1) if ch == 'T'), None)

    # Recompute first time each reaches max_w
    t_first = None
    a_first = None
    t = a = 0
    for i, ch in enumerate(s, 1):
        if ch == 'T':
            t += 1
            if t == max_w and t_first is None:
                t_first = i
        else:
            a += 1
            if a == max_w and a_first is None:
                a_first = i
        if t_first is not None and a_first is not None:
            break

    print('T' if t_first < a_first else 'A')

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
    N = int(data[0])
    S = data[1].strip()

    t = 0  # Takahashi wins
    a = 0  # Aoki wins

    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        # When someone reaches more wins than the other, they are the overall winner
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

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
    if not data:
        return
    N = int(data[0])
    S = data[1].strip()

    t_wins = 0
    a_wins = 0
    for ch in S:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

        if t_wins != a_wins:
            continue

        # If currently tied, keep going until one reaches the other's final win count.
        # But the problem wants: who wins more; if equal, who reached that number first.
        # So we can finish by tracking max wins and earliest reach.
        # We'll handle this by continuing and computing final result after loop.
    # Compute final winner
    if t_wins > a_wins:
        sys.stdout.write('T')
    elif a_wins > t_wins:
        sys.stdout.write('A')
    else:
        target = t_wins  # same as a_wins
        t = 0
        a = 0
        for ch in S:
            if ch == 'T':
                t += 1
            else:
                a += 1
            if t == target:
                sys.stdout.write('T')
                return
            if a == target:
                sys.stdout.write('A')
                return

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
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    S = input_data[1].strip()

    t_wins = 0
    a_wins = 0

    for c in S:
        if c == 'T':
            t_wins += 1
        else:
            a_wins += 1

    if t_wins > a_wins:
        print('T')
        return
    if a_wins > t_wins:
        print('A')
        return

    # Same number of wins: whoever reaches that number first
    target = t_wins
    t = 0
    a = 0
    for c in S:
        if c == 'T':
            t += 1
            if t == target:
                print('T')
                return
        else:
            a += 1
            if a == target:
                print('A')
                return

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
    N = int(data[0])
    S = data[1].strip()

    t = 0  # wins for Takahashi
    a = 0  # wins for Aoki
    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

if __name__ == "__main__":
    solve()
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.7333 | `partial` |
| 1 | 0.7333 | `partial` |
| 2 | 0.7333 | `partial` |
| 3 | 1.0000 | `full` |
| 4 | 0.7333 | `partial` |
| 5 | 0.7333 | `partial` |
| 6 | 0.7333 | `partial` |
| 7 | 1.0000 | `full` |
| 8 | 1.0000 | `full` |
| 9 | 0.7333 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
Takahashi and Aoki played N games.
You are given a string S of length N, representing the results of these games.
Takahashi won the i-th game if the i-th character of S is T, and Aoki won that game if it is A.
The overall winner between Takahashi and Aoki is the one who won more games than the other.
If they had the same number of wins, the overall winner is the one who reached that number of wins first.
Find the overall winner: Takahashi or Aoki.

Input

The input is given from Standard Input in the following format:
N
S

Output

If the overall winner is Takahashi, print T; if it is Aoki, print A.

Constraints


- 1\leq N \leq 100
- N is an integer.
- S is a string of length N consisting of T and A.

Sample Input 1

5
TTAAT

Sample Output 1

T

Takahashi won three games, and Aoki won two.
Thus, the overall winner is Takahashi, who won more games.

Sample Input 2

6
ATTATA

Sample Output 2

T

Both Takahashi and Aoki won three games.
Takahashi reached three wins in the fifth game, and Aoki in the sixth game.
Thus, the overall winner is Takahashi, who reached three wins first.

Sample Input 3

1
A

Sample Output 3

A

### Solutions
#### Correct
Attempt 1
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t > a:
            # first to make t strictly greater than a wins overall
            # but per problem: if same wins, whoever reached that count first
            # We can handle directly by checking when someone reaches final count.
            pass

    # Better approach: track first time reaching the final win count.
    total_t = S.count('T')
    total_a = N - total_t

    if total_t > total_a:
        target = total_t
        count = 0
        for ch in S:
            if ch == 'T':
                count += 1
                if count == target:
                    print('T')
                    return
    elif total_a > total_t:
        target = total_a
        count = 0
        for ch in S:
            if ch == 'A':
                count += 1
                if count == target:
                    print('A')
                    return
    else:
        # same wins: whoever reaches that number first
        target = total_t
        t = a = 0
        for ch in S:
            if ch == 'T':
                t += 1
                if t == target:
                    print('T')
                    return
            else:
                a += 1
                if a == target:
                    print('A')
                    return

if __name__ == "__main__":
    solve()
```

Attempt 2
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    S = data[1].strip()

    t_wins = 0
    a_wins = 0
    for ch in S:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

        if t_wins != a_wins:
            continue

        # If currently tied, keep going until one reaches the other's final win count.
        # But the problem wants: who wins more; if equal, who reached that number first.
        # So we can finish by tracking max wins and earliest reach.
        # We'll handle this by continuing and computing final result after loop.
    # Compute final winner
    if t_wins > a_wins:
        sys.stdout.write('T')
    elif a_wins > t_wins:
        sys.stdout.write('A')
    else:
        target = t_wins  # same as a_wins
        t = 0
        a = 0
        for ch in S:
            if ch == 'T':
                t += 1
            else:
                a += 1
            if t == target:
                sys.stdout.write('T')
                return
            if a == target:
                sys.stdout.write('A')
                return

if __name__ == "__main__":
    solve()
```

Attempt 3
```python
import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    S = input_data[1].strip()

    t_wins = 0
    a_wins = 0

    for c in S:
        if c == 'T':
            t_wins += 1
        else:
            a_wins += 1

    if t_wins > a_wins:
        print('T')
        return
    if a_wins > t_wins:
        print('A')
        return

    # Same number of wins: whoever reaches that number first
    target = t_wins
    t = 0
    a = 0
    for c in S:
        if c == 'T':
            t += 1
            if t == target:
                print('T')
                return
        else:
            a += 1
            if a == target:
                print('A')
                return

if __name__ == "__main__":
    solve()
```

#### Partially Correct
Attempt 1
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1].strip()

    t = 0  # Takahashi wins
    a = 0  # Aoki wins

    for i, ch in enumerate(s, start=1):
        if ch == 'T':
            t += 1
        else:
            a += 1

        # If someone is ahead, they are the overall winner.
        # If tied, keep going; the rules say the one who reaches the target first wins.
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

    # If never differs (shouldn't happen given N>=1), decide by who reached first.
    # But as written above, difference will occur at some point for any non-empty string.
    # Fallback:
    print('T' if t >= a else 'A')

if __name__ == "__main__":
    solve()
```

Attempt 2
```python
import sys

def main():
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    S = input_data[1]

    t_wins = 0
    a_wins = 0
    target_t = None
    target_a = None

    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            t_wins += 1
            if t_wins > a_wins:
                print('T')
                return
            if t_wins == a_wins:
                # If equal now, winner depends on who reached the higher wins first.
                # That happens only when one surpasses the other, so continue.
                pass
        else:  # 'A'
            a_wins += 1
            if a_wins > t_wins:
                print('A')
                return

    # If reached here, neither ever surpassed the other -> must be ties, so
    # by rule the one who reached that number of wins first wins.
    # We'll compute with a second pass for first reaching the max wins.
    max_wins = max(t_wins, a_wins)
    t_first = None
    a_first = None
    tw = aw = 0
    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            tw += 1
            if tw == max_wins:
                t_first = i
                break
        else:
            aw += 1
            if aw == max_wins:
                a_first = i
                break

    # If t_wins == a_wins, only one of the first indices will have occurred first
    # based on loop order; compute properly:
    # Actually loop above stops at first max_wins reached by either; so decide by ch.
    # Simpler: redo properly.
    tw = aw = 0
    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            tw += 1
            if tw == max_wins:
                print('T')
                return
        else:
            aw += 1
            if aw == max_wins:
                print('A')
                return

if __name__ == "__main__":
    main()
```

Attempt 3
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t == a:
            continue
        # someone has more wins; determine which reached first to this higher count
        # But the problem's rule about "same number of wins reached first" means:
        # As we iterate, the first time someone becomes strictly greater than the other,
        # their current win count is the winner's final tie/break condition.
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

    # For completeness (should always return within loop)
    print('T' if t > a else 'A')

if __name__ == "__main__":
    solve()
```

Attempt 4
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1].strip()

    t_cnt = 0
    a_cnt = 0

    for ch in s:
        if ch == 'T':
            t_cnt += 1
            if t_cnt > a_cnt:
                print('T')
                return
        else:  # 'A'
            a_cnt += 1
            if a_cnt > t_cnt:
                print('A')
                return

if __name__ == "__main__":
    solve()
```

Attempt 5
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1].strip()

    t_wins = 0
    a_wins = 0

    for ch in s:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

        if t_wins > a_wins:
            print('T')
            return
        if a_wins > t_wins:
            print('A')
            return

    # If counts are equal after N games, the one who first reached the final max
    # wins is the one whose winning count reached max earlier.
    # But with the above loop, one side would have exceeded the other unless equal.
    # Therefore, determine by first occurrence of max wins.
    max_w = max(t_wins, a_wins)
    t_idx = next((i for i, ch in enumerate(s, 1) if ch == 'T'), None)

    # Recompute first time each reaches max_w
    t_first = None
    a_first = None
    t = a = 0
    for i, ch in enumerate(s, 1):
        if ch == 'T':
            t += 1
            if t == max_w and t_first is None:
                t_first = i
        else:
            a += 1
            if a == max_w and a_first is None:
                a_first = i
        if t_first is not None and a_first is not None:
            break

    print('T' if t_first < a_first else 'A')

if __name__ == "__main__":
    solve()
```

Attempt 6
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t = 0  # Takahashi wins
    a = 0  # Aoki wins

    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        # When someone reaches more wins than the other, they are the overall winner
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

solve()
```

Attempt 7
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t = 0  # wins for Takahashi
    a = 0  # wins for Aoki
    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

if __name__ == "__main__":
    solve()
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
import sys

def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t > a:
            # first to make t strictly greater than a wins overall
            # but per problem: if same wins, whoever reached that count first
            # We can handle directly by checking when someone reaches final count.
            pass

    # Better approach: track first time reaching the final win count.
    total_t = S.count('T')
    total_a = N - total_t

    if total_t > total_a:
        target = total_t
        count = 0
        for ch in S:
            if ch == 'T':
                count += 1
                if count == target:
                    print('T')
                    return
    elif total_a > total_t:
        target = total_a
        count = 0
        for ch in S:
            if ch == 'A':
                count += 1
                if count == target:
                    print('A')
                    return
    else:
        # same wins: whoever reaches that number first
        target = total_t
        t = a = 0
        for ch in S:
            if ch == 'T':
                t += 1
                if t == target:
                    print('T')
                    return
            else:
                a += 1
                if a == target:
                    print('A')
                    return

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
    if not data:
        return
    N = int(data[0])
    S = data[1].strip()

    t_wins = 0
    a_wins = 0
    for ch in S:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

        if t_wins != a_wins:
            continue

        # If currently tied, keep going until one reaches the other's final win count.
        # But the problem wants: who wins more; if equal, who reached that number first.
        # So we can finish by tracking max wins and earliest reach.
        # We'll handle this by continuing and computing final result after loop.
    # Compute final winner
    if t_wins > a_wins:
        sys.stdout.write('T')
    elif a_wins > t_wins:
        sys.stdout.write('A')
    else:
        target = t_wins  # same as a_wins
        t = 0
        a = 0
        for ch in S:
            if ch == 'T':
                t += 1
            else:
                a += 1
            if t == target:
                sys.stdout.write('T')
                return
            if a == target:
                sys.stdout.write('A')
                return

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
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    S = input_data[1].strip()

    t_wins = 0
    a_wins = 0

    for c in S:
        if c == 'T':
            t_wins += 1
        else:
            a_wins += 1

    if t_wins > a_wins:
        print('T')
        return
    if a_wins > t_wins:
        print('A')
        return

    # Same number of wins: whoever reaches that number first
    target = t_wins
    t = 0
    a = 0
    for c in S:
        if c == 'T':
            t += 1
            if t == target:
                print('T')
                return
        else:
            a += 1
            if a == target:
                print('A')
                return

if __name__ == "__main__":
    solve()
```
```

</details>

#### Tier: `partial`

<details>
<summary>partial attempt 1</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1].strip()

    t = 0  # Takahashi wins
    a = 0  # Aoki wins

    for i, ch in enumerate(s, start=1):
        if ch == 'T':
            t += 1
        else:
            a += 1

        # If someone is ahead, they are the overall winner.
        # If tied, keep going; the rules say the one who reaches the target first wins.
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

    # If never differs (shouldn't happen given N>=1), decide by who reached first.
    # But as written above, difference will occur at some point for any non-empty string.
    # Fallback:
    print('T' if t >= a else 'A')

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>partial attempt 2</summary>

```text
```python
import sys

def main():
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    S = input_data[1]

    t_wins = 0
    a_wins = 0
    target_t = None
    target_a = None

    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            t_wins += 1
            if t_wins > a_wins:
                print('T')
                return
            if t_wins == a_wins:
                # If equal now, winner depends on who reached the higher wins first.
                # That happens only when one surpasses the other, so continue.
                pass
        else:  # 'A'
            a_wins += 1
            if a_wins > t_wins:
                print('A')
                return

    # If reached here, neither ever surpassed the other -> must be ties, so
    # by rule the one who reached that number of wins first wins.
    # We'll compute with a second pass for first reaching the max wins.
    max_wins = max(t_wins, a_wins)
    t_first = None
    a_first = None
    tw = aw = 0
    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            tw += 1
            if tw == max_wins:
                t_first = i
                break
        else:
            aw += 1
            if aw == max_wins:
                a_first = i
                break

    # If t_wins == a_wins, only one of the first indices will have occurred first
    # based on loop order; compute properly:
    # Actually loop above stops at first max_wins reached by either; so decide by ch.
    # Simpler: redo properly.
    tw = aw = 0
    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            tw += 1
            if tw == max_wins:
                print('T')
                return
        else:
            aw += 1
            if aw == max_wins:
                print('A')
                return

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>partial attempt 3</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t == a:
            continue
        # someone has more wins; determine which reached first to this higher count
        # But the problem's rule about "same number of wins reached first" means:
        # As we iterate, the first time someone becomes strictly greater than the other,
        # their current win count is the winner's final tie/break condition.
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

    # For completeness (should always return within loop)
    print('T' if t > a else 'A')

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>partial attempt 4</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1].strip()

    t_cnt = 0
    a_cnt = 0

    for ch in s:
        if ch == 'T':
            t_cnt += 1
            if t_cnt > a_cnt:
                print('T')
                return
        else:  # 'A'
            a_cnt += 1
            if a_cnt > t_cnt:
                print('A')
                return

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>partial attempt 5</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1].strip()

    t_wins = 0
    a_wins = 0

    for ch in s:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

        if t_wins > a_wins:
            print('T')
            return
        if a_wins > t_wins:
            print('A')
            return

    # If counts are equal after N games, the one who first reached the final max
    # wins is the one whose winning count reached max earlier.
    # But with the above loop, one side would have exceeded the other unless equal.
    # Therefore, determine by first occurrence of max wins.
    max_w = max(t_wins, a_wins)
    t_idx = next((i for i, ch in enumerate(s, 1) if ch == 'T'), None)

    # Recompute first time each reaches max_w
    t_first = None
    a_first = None
    t = a = 0
    for i, ch in enumerate(s, 1):
        if ch == 'T':
            t += 1
            if t == max_w and t_first is None:
                t_first = i
        else:
            a += 1
            if a == max_w and a_first is None:
                a_first = i
        if t_first is not None and a_first is not None:
            break

    print('T' if t_first < a_first else 'A')

if __name__ == "__main__":
    solve()
```
```

</details>

<details>
<summary>partial attempt 6</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t = 0  # Takahashi wins
    a = 0  # Aoki wins

    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        # When someone reaches more wins than the other, they are the overall winner
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

solve()
```
```

</details>

<details>
<summary>partial attempt 7</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t = 0  # wins for Takahashi
    a = 0  # wins for Aoki
    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t > a:
            print('T')
            return
        if a > t:
            print('A')
            return

if __name__ == "__main__":
    solve()
```
```

</details>

### Parsed Memory Items

1. Constraint-First Decision Logic
Description: Derive the algorithm directly from the problem’s formal win/tie-breaking rules instead of using intuitive ordering assumptions.
<details>
<summary>Content 1</summary>

```text
When a problem has a primary criterion (e.g., “more wins”) plus a tie-break (e.g., “reached that number first”), implement them as separate, explicit branches. This prevents subtle logical mismatches where a natural “first time one leads” notion does not equal the specified tie-break.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
The correct attempts converge on a robust strategy: explicitly handle the two-phase rule implied by the statement—(1) compare total wins, and (2) if tied, resolve by the earliest time a player reaches that tied win count. The partially correct attempts fail mainly by making an incorrect assumption that the “first to exceed” the other always matches the tie-break rule, or by using an inconsistent/overcomplicated method to infer “who reached the max first,” which can break when the logic about reaching and timing is misapplied. Overall, success comes from aligning the algorithm directly with the problem’s decision rule rather than relying on intuitive shortcuts, and from doing a clean tie-break computation with an unambiguous condition.
```

</details>

2. Two-Pass Tie-Break Computation
Description: In tie situations, compute the target milestone from final totals, then rescan to find the first time each side reaches it.
<details>
<summary>Content 2</summary>

```text
A reliable pattern is: first compute final aggregates; if equal, define a “target count” and scan in order to detect the earliest position where each side reaches that count. This makes the timing rule unambiguous and avoids complex reasoning about intermediate comparisons.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
The correct attempts converge on a robust strategy: explicitly handle the two-phase rule implied by the statement—(1) compare total wins, and (2) if tied, resolve by the earliest time a player reaches that tied win count. The partially correct attempts fail mainly by making an incorrect assumption that the “first to exceed” the other always matches the tie-break rule, or by using an inconsistent/overcomplicated method to infer “who reached the max first,” which can break when the logic about reaching and timing is misapplied. Overall, success comes from aligning the algorithm directly with the problem’s decision rule rather than relying on intuitive shortcuts, and from doing a clean tie-break computation with an unambiguous condition.
```

</details>

3. Validate “First Exceeds” Reasoning
Description: Any transformation that replaces the required tie-break with “who first becomes strictly ahead” must be checked for equivalence.
<details>
<summary>Content 3</summary>

```text
It’s tempting to decide during the scan when one side becomes greater, but that can fail when the problem’s tie-break is about reaching a shared target count, not about first exceeding. Add an equivalence check (or follow the statement’s rule literally) before adopting such a shortcut.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
The correct attempts converge on a robust strategy: explicitly handle the two-phase rule implied by the statement—(1) compare total wins, and (2) if tied, resolve by the earliest time a player reaches that tied win count. The partially correct attempts fail mainly by making an incorrect assumption that the “first to exceed” the other always matches the tie-break rule, or by using an inconsistent/overcomplicated method to infer “who reached the max first,” which can break when the logic about reaching and timing is misapplied. Overall, success comes from aligning the algorithm directly with the problem’s decision rule rather than relying on intuitive shortcuts, and from doing a clean tie-break computation with an unambiguous condition.
```

</details>

4. Avoid Overcomplicated Index Inference
Description: Don’t infer first-reaching order indirectly; track it with a direct condition during a controlled scan.
<details>
<summary>Content 4</summary>

```text
Partially correct attempts that try to deduce timing using partial information or placeholder variables often end up inconsistent. Prefer a straightforward loop that stops when the precise event (“reaches the target count”) occurs.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
The correct attempts converge on a robust strategy: explicitly handle the two-phase rule implied by the statement—(1) compare total wins, and (2) if tied, resolve by the earliest time a player reaches that tied win count. The partially correct attempts fail mainly by making an incorrect assumption that the “first to exceed” the other always matches the tie-break rule, or by using an inconsistent/overcomplicated method to infer “who reached the max first,” which can break when the logic about reaching and timing is misapplied. Overall, success comes from aligning the algorithm directly with the problem’s decision rule rather than relying on intuitive shortcuts, and from doing a clean tie-break computation with an unambiguous condition.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
The correct attempts converge on a robust strategy: explicitly handle the two-phase rule implied by the statement—(1) compare total wins, and (2) if tied, resolve by the earliest time a player reaches that tied win count. The partially correct attempts fail mainly by making an incorrect assumption that the “first to exceed” the other always matches the tie-break rule, or by using an inconsistent/overcomplicated method to infer “who reached the max first,” which can break when the logic about reaching and timing is misapplied. Overall, success comes from aligning the algorithm directly with the problem’s decision rule rather than relying on intuitive shortcuts, and from doing a clean tie-break computation with an unambiguous condition.
</reasoning>

<memories>
<memory>
<title>Constraint-First Decision Logic</title>
<description>Derive the algorithm directly from the problem’s formal win/tie-breaking rules instead of using intuitive ordering assumptions.</description>
<content>When a problem has a primary criterion (e.g., “more wins”) plus a tie-break (e.g., “reached that number first”), implement them as separate, explicit branches. This prevents subtle logical mismatches where a natural “first time one leads” notion does not equal the specified tie-break.</content>
</memory>

<memory>
<title>Two-Pass Tie-Break Computation</title>
<description>In tie situations, compute the target milestone from final totals, then rescan to find the first time each side reaches it.</description>
<content>A reliable pattern is: first compute final aggregates; if equal, define a “target count” and scan in order to detect the earliest position where each side reaches that count. This makes the timing rule unambiguous and avoids complex reasoning about intermediate comparisons.</content>
</memory>

<memory>
<title>Validate “First Exceeds” Reasoning</title>
<description>Any transformation that replaces the required tie-break with “who first becomes strictly ahead” must be checked for equivalence.</description>
<content>It’s tempting to decide during the scan when one side becomes greater, but that can fail when the problem’s tie-break is about reaching a shared target count, not about first exceeding. Add an equivalence check (or follow the statement’s rule literally) before adopting such a shortcut.</content>
</memory>

<memory>
<title>Avoid Overcomplicated Index Inference</title>
<description>Don’t infer first-reaching order indirectly; track it with a direct condition during a controlled scan.</description>
<content>Partially correct attempts that try to deduce timing using partial information or placeholder variables often end up inconsistent. Prefer a straightforward loop that stops when the precise event (“reaches the target count”) occurs.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `0.4000`
- Augmented pass@1: `1.0000`
- Improvement: `+0.6000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
Takahashi and Aoki played N games.
You are given a string S of length N, representing the results of these games.
Takahashi won the i-th game if the i-th character of S is T, and Aoki won that game if it is A.
The overall winner between Takahashi and Aoki is the one who won more games than the other.
If they had the same number of wins, the overall winner is the one who reached that number of wins first.
Find the overall winner: Takahashi or Aoki.

Input

The input is given from Standard Input in the following format:
N
S

Output

If the overall winner is Takahashi, print T; if it is Aoki, print A.

Constraints


- 1\leq N \leq 100
- N is an integer.
- S is a string of length N consisting of T and A.

Sample Input 1

5
TTAAT

Sample Output 1

T

Takahashi won three games, and Aoki won two.
Thus, the overall winner is Takahashi, who won more games.

Sample Input 2

6
ATTATA

Sample Output 2

T

Both Takahashi and Aoki won three games.
Takahashi reached three wins in the fifth game, and Aoki in the sixth game.
Thus, the overall winner is Takahashi, who reached three wins first.

Sample Input 3

1
A

Sample Output 3

A

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
    n = int(data[0])
    s = data[1].strip()

    t = 0
    a = 0
    first_target = None  # first player to reach final max wins

    for i, ch in enumerate(s):
        if ch == 'T':
            t += 1
        else:
            a += 1

        # Once someone reaches the other player's final win count, determine winner
        # But final win count isn't known until the end, so we instead compute at end
        # We'll just track wins at each step and decide after counting totals.
        # (Simpler: compute totals first, then scan for first reach.)
    t_total = s.count('T')
    a_total = n - t_total

    target = max(t_total, a_total)
    for ch in s:
        if ch == 'T':
            t += 1
            if t == target:
                print('T')
                return
        else:
            a += 1
            if a == target:
                print('A')
                return

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
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t = 0
    a = 0
    for i, ch in enumerate(S):
        if ch == 'T':
            t += 1
            if t > a:
                print('T')
                return
            if t == a:
                # tie case: decide only when one side catches up to the final winner,
                # but we can still continue until someone exceeds or finishes.
                pass
        else:
            a += 1
            if a > t:
                print('A')
                return
            if t == a:
                pass

    # If we reach here, then final counts are equal.
    # The winner is the one who reached that number of wins first.
    target = t  # == a
    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
            if t == target:
                print('T')
                return
        else:
            a += 1
            if a == target:
                print('A')
                return

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
    n = int(data[0])
    s = data[1].strip()

    t_wins = 0
    a_wins = 0

    for ch in s:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

        # If someone has more wins than the other, they are the overall winner.
        if t_wins > a_wins:
            print('T')
            return
        if a_wins > t_wins:
            print('A')
            return

    # If equal after all games, it means N==0 (not possible by constraints),
    # but we'll keep a safe fallback.
    print('T' if t_wins > a_wins else 'A')

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
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    s = input_data[1].strip()

    t_wins = 0
    a_wins = 0
    target_t = target_a = None

    # Track first time either reaches its final max (i.e., the other can't catch up)
    # Equivalent simpler approach:
    # - compute final counts
    # - if unequal: winner is one with more
    # - if equal: winner is who reaches that count first in the sequence
    for ch in s:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

    if t_wins > a_wins:
        print('T')
        return
    if a_wins > t_wins:
        print('A')
        return

    # tie: find first index where one reaches the tied count
    target = t_wins
    t_wins = a_wins = 0
    for ch in s:
        if ch == 'T':
            t_wins += 1
            if t_wins == target:
                print('T')
                return
        else:
            a_wins += 1
            if a_wins == target:
                print('A')
                return

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
    n = int(data[0])
    s = data[1]

    t_wins = 0
    a_wins = 0

    for ch in s:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

        if t_wins != a_wins:
            # The one who eventually wins more is determined by counts;
            # but the "first to reach the final tie-break number" happens exactly
            # when one side crosses the other's current count.
            pass

        # If one side has more wins than the other, it is already the overall winner
        if t_wins > a_wins:
            print('T')
            return
        if a_wins > t_wins:
            print('A')
            return

    # If we get here, counts are equal (only possible when n is even and all processed),
    # tie-breaker is who reached that number first; can be found by scanning again.
    target = n // 2
    t_reach = None
    a_reach = None
    t_count = 0
    a_count = 0
    for i, ch in enumerate(s):
        if ch == 'T':
            t_count += 1
            if t_reach is None and t_count == target:
                t_reach = i
        else:
            a_count += 1
            if a_reach is None and a_count == target:
                a_reach = i
        if t_reach is not None and a_reach is not None:
            break
    print('T' if t_reach < a_reach else 'A')

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
    N = int(data[0])
    S = data[1].strip()

    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t > N//2 and t != a and t > a:
            # Not needed; we handle by first reaching max
            pass

    # Determine overall winner using "more wins, else who reached that count first"
    if t > a:
        target = t
    elif a > t:
        target = a
    else:
        target = t  # same

    # Who reached target first?
    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
            if t == target:
                print('T')
                return
        else:
            a += 1
            if a == target:
                print('A')
                return

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
    n = int(data[0])
    s = data[1]

    t_count = 0
    a_count = 0

    for ch in s:
        if ch == 'T':
            t_count += 1
            if t_count > a_count:
                print('T')
                return
        else:
            a_count += 1
            if a_count > t_count:
                print('A')
                return

    # The loop should always decide before end, but for completeness:
    # If equal overall (not possible here because n finite and winner defined by first reach),
    # decide by first reaching max; simulate after loop.
    if t_count > a_count:
        print('T')
    elif a_count > t_count:
        print('A')
    else:
        # If somehow equal, determine who reached it first by scanning again
        target = t_count
        t_first = a_first = None
        for i, ch in enumerate(s):
            if ch == 'T' and t_first is None:
                # count T's
                pass
        # fallback: compute first index where each reaches target
        t = a = 0
        for i, ch in enumerate(s):
            if ch == 'T':
                t += 1
                if t == target:
                    t_first = i
                    break
            else:
                a += 1
                if a == target:
                    a_first = i
                    break
        # scan for other if needed
        t = a = 0
        for i, ch in enumerate(s):
            if ch == 'T':
                t += 1
                if t == target:
                    t_first = i
                    break
            else:
                a += 1
                if a == target:
                    a_first = i
                    break
        print('T' if t_first is not None and a_first is not None and t_first < a_first else 'A')

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
    N = int(data[0])
    S = data[1].strip()

    t = 0
    a = 0
    for i, ch in enumerate(S):
        if ch == 'T':
            t += 1
        else:
            a += 1

        # When one leads by more than the other, winner is determined.
        # Equivalent to: if current winner's wins > opponent's wins, that current player is overall winner.
        if t > a:
            # This happens exactly when T first becomes overall winner.
            # But A could also become overall winner later; we need first time max comparison.
            # With this rule we must ensure the other can't have become overall earlier.
            # It's safe to return here because t>a occurs at the earliest point T can lead.
            pass
        if a > t:
            pass

        # Determine overall winner condition:
        if t >= a:
            # If t > a, or t == a (can't happen as it would mean no one has strictly more yet),
            # we only finalize when someone has strictly more OR when equal threshold reached first.
            # The problem defines "same wins -> who reached that number first".
            # So we can track first time each reaches its final winning count.
            pass

    # Simpler correct approach:
    # Let final counts be t_total and a_total. If one is larger, print that.
    # If equal, find first index where cumulative wins reach that count.

    # Recompute totals and if equal, determine by first reach.
    t_total = S.count('T')
    a_total = N - t_total

    if t_total > a_total:
        print('T')
        return
    if a_total > t_total:
        print('A')
        return

    target = t_total  # equal to a_total
    t = 0
    a = 0
    for ch in S:
        if ch == 'T':
            t += 1
            if t == target:
                print('T')
                return
        else:
            a += 1
            if a == target:
                print('A')
                return

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
    n = int(data[0])
    s = data[1].strip()

    t_count = 0
    a_count = 0

    for ch in s:
        if ch == 'T':
            t_count += 1
        else:
            a_count += 1

        if t_count == a_count + 1:
            # Takahashi just got the lead by 1
            # but we still should confirm overall winner via first reaching max
            pass

    # Determine overall winner:
    # One with more wins, or if tie, who reached that count first.
    if t_count > a_count:
        target = t_count
        running = 0
        for i, ch in enumerate(s):
            if ch == 'T':
                running += 1
            if running == target:
                print('T')
                return
    elif a_count > t_count:
        target = a_count
        running = 0
        for i, ch in enumerate(s):
            if ch == 'A':
                running += 1
            if running == target:
                print('A')
                return
    else:
        # Same number of wins: whoever reached that number first
        target = t_count
        t_reached = a_reached = None
        t_running = a_running = 0
        for i, ch in enumerate(s):
            if ch == 'T':
                t_running += 1
                if t_running == target and t_reached is None:
                    t_reached = i
            else:
                a_running += 1
                if a_running == target and a_reached is None:
                    a_reached = i
            if t_reached is not None and a_reached is not None:
                break
        print('T' if t_reached < a_reached else 'A')

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
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    s = input_data[1]

    t_count = 0
    a_count = 0

    for i, ch in enumerate(s, start=1):
        if ch == 'T':
            t_count += 1
            if t_count > a_count:
                print('T')
                return
            if t_count == a_count:
                # continue; first to reach the tied maximum will be decided later
                continue
        else:
            a_count += 1
            if a_count > t_count:
                print('A')
                return
            if a_count == t_count:
                continue

    # Determine by rule: more wins wins; if equal, who reached that number first.
    # We already printed when someone reached a strictly larger count.
    # If equal overall, find earliest index where the winning count was achieved.
    # Compute final counts
    t_total = s.count('T')
    a_total = n - t_total

    if t_total > a_total:
        print('T')
        return
    if a_total > t_total:
        print('A')
        return

    # Equal wins: find first index where cumulative matches that win count
    t_needed = t_total
    a_needed = a_total
    cum_t = cum_a = 0
    for ch in s:
        if ch == 'T':
            cum_t += 1
        else:
            cum_a += 1
        if cum_t == t_needed:
            print('T')
            return
        if cum_a == a_needed:
            print('A')
            return

if __name__ == "__main__":
    solve()
```
```

</details>

#### Baseline Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.0000 | `fail` |
| 1 | 0.7333 | `partial` |
| 2 | 0.7333 | `partial` |
| 3 | 1.0000 | `full` |
| 4 | 0.7333 | `partial` |
| 5 | 1.0000 | `full` |
| 6 | 0.7333 | `partial` |
| 7 | 1.0000 | `full` |
| 8 | 1.0000 | `full` |
| 9 | 0.7333 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 0,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
  "passed": 11,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "T",
      "actual": "A",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": false,
      "expected": "A",
      "actual": "T",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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

  1. Constraint-First Decision Logic: Derive the algorithm directly from the problem’s formal win/tie-breaking rules instead of using intuitive ordering assumptions.
     When a problem has a primary criterion (e.g., “more wins”) plus a tie-break (e.g., “reached that number first”), implement them as separate, explicit branches. This prevents subtle logical mismatches where a natural “first time one leads” notion does not equal the specified tie-break.
  2. Two-Pass Tie-Break Computation: In tie situations, compute the target milestone from final totals, then rescan to find the first time each side reaches it.
     A reliable pattern is: first compute final aggregates; if equal, define a “target count” and scan in order to detect the earliest position where each side reaches that count. This makes the timing rule unambiguous and avoids complex reasoning about intermediate comparisons.
  3. Validate “First Exceeds” Reasoning: Any transformation that replaces the required tie-break with “who first becomes strictly ahead” must be checked for equivalence.
     It’s tempting to decide during the scan when one side becomes greater, but that can fail when the problem’s tie-break is about reaching a shared target count, not about first exceeding. Add an equivalence check (or follow the statement’s rule literally) before adopting such a shortcut.
  4. Avoid Overcomplicated Index Inference: Don’t infer first-reaching order indirectly; track it with a direct condition during a controlled scan.
     Partially correct attempts that try to deduce timing using partial information or placeholder variables often end up inconsistent. Prefer a straightforward loop that stops when the precise event (“reaches the target count”) occurs.

Apply these insights to the problem below.

### Question:
Takahashi and Aoki played N games.
You are given a string S of length N, representing the results of these games.
Takahashi won the i-th game if the i-th character of S is T, and Aoki won that game if it is A.
The overall winner between Takahashi and Aoki is the one who won more games than the other.
If they had the same number of wins, the overall winner is the one who reached that number of wins first.
Find the overall winner: Takahashi or Aoki.

Input

The input is given from Standard Input in the following format:
N
S

Output

If the overall winner is Takahashi, print T; if it is Aoki, print A.

Constraints


- 1\leq N \leq 100
- N is an integer.
- S is a string of length N consisting of T and A.

Sample Input 1

5
TTAAT

Sample Output 1

T

Takahashi won three games, and Aoki won two.
Thus, the overall winner is Takahashi, who won more games.

Sample Input 2

6
ATTATA

Sample Output 2

T

Both Takahashi and Aoki won three games.
Takahashi reached three wins in the fifth game, and Aoki in the sixth game.
Thus, the overall winner is Takahashi, who reached three wins first.

Sample Input 3

1
A

Sample Output 3

A

### Format: Read the inputs from stdin solve the problem and write the answer to stdout (do not directly test on the sample inputs). Enclose your code within delimiters as follows. Ensure that when the python program runs, it reads the inputs, runs the algorithm and writes output to STDOUT.
```python
# YOUR CODE HERE
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Augmented generation 1</summary>

```text
```python
import sys

def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t_total = S.count('T')
    a_total = N - t_total

    if t_total > a_total:
        print('T')
        return
    if a_total > t_total:
        print('A')
        return

    # Tie: determine who reached the final equal number of wins first
    target = t_total  # == a_total
    t = a = 0
    for ch in S:
        if ch == 'T':
            t += 1
        else:
            a += 1
        if t == target:
            print('T')
            return
        if a == target:
            print('A')
            return

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
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1].strip()

    t_total = s.count('T')
    a_total = n - t_total

    if t_total > a_total:
        print('T')
        return
    if a_total > t_total:
        print('A')
        return

    # Tie-break: the one who reached that number of wins first
    target = t_total  # == a_total
    t_count = 0
    a_count = 0
    for ch in s:
        if ch == 'T':
            t_count += 1
        else:
            a_count += 1
        if t_count == target and a_count == target:
            # This can only happen if both reach target in same game,
            # but since a game can't be won by both, it won't occur.
            break
        if t_count == target:
            print('T')
            return
        if a_count == target:
            print('A')
            return

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
    N = int(data[0])
    S = data[1].strip()

    t = S.count('T')
    a = N - t

    if t > a:
        print('T')
        return
    if a > t:
        print('A')
        return

    # Tie: reached the final win count first
    target = t  # == a
    t_reached = None
    a_reached = None
    t_count = 0
    a_count = 0

    for i, ch in enumerate(S, start=1):
        if ch == 'T':
            t_count += 1
            if t_reached is None and t_count == target:
                t_reached = i
        else:
            a_count += 1
            if a_reached is None and a_count == target:
                a_reached = i
        if t_reached is not None and a_reached is not None:
            break

    print('T' if t_reached < a_reached else 'A')

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
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    S = data[1].strip()

    t_total = S.count('T')
    a_total = N - t_total

    if t_total > a_total:
        print('T')
        return
    if a_total > t_total:
        print('A')
        return

    # Tie: both reached the same number of wins. Winner is who reached it first.
    target = t_total
    t_reached = None
    a_reached = None
    t_cnt = a_cnt = 0

    for i, ch in enumerate(S):
        if ch == 'T':
            t_cnt += 1
            if t_reached is None and t_cnt == target:
                t_reached = i
        else:
            a_cnt += 1
            if a_reached is None and a_cnt == target:
                a_reached = i

        if t_reached is not None and a_reached is not None:
            break

    print('T' if t_reached < a_reached else 'A')

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
    n = int(data[0])
    s = data[1].strip()

    t_total = s.count('T')
    a_total = n - t_total

    if t_total > a_total:
        print("T")
        return
    if a_total > t_total:
        print("A")
        return

    # Tie: determine who reached the final win count first
    target = t_total  # == a_total
    t_reached = a_reached = None
    t = a = 0
    for i, ch in enumerate(s, start=1):
        if ch == 'T':
            t += 1
            if t_reached is None and t == target:
                t_reached = i
        else:
            a += 1
            if a_reached is None and a == target:
                a_reached = i
        if t_reached is not None and a_reached is not None:
            break

    print("T" if t_reached < a_reached else "A")

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
    if not data:
        return
    N = int(data[0])
    S = data[1].strip()

    t_total = S.count('T')
    a_total = N - t_total

    if t_total > a_total:
        print('T')
        return
    if a_total > t_total:
        print('A')
        return

    # Tie-break: who reaches the final win count first
    target = t_total  # == a_total
    t_reached = None
    a_reached = None
    t_cnt = 0
    a_cnt = 0
    for i, ch in enumerate(S):
        if ch == 'T':
            t_cnt += 1
            if t_reached is None and t_cnt == target:
                t_reached = i
        else:  # 'A'
            a_cnt += 1
            if a_reached is None and a_cnt == target:
                a_reached = i

    print('T' if t_reached < a_reached else 'A')

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
    n = int(data[0])
    s = data[1]

    t_wins = s.count('T')
    a_wins = n - t_wins

    if t_wins > a_wins:
        print('T')
        return
    if a_wins > t_wins:
        print('A')
        return

    # Tie-break: who reached that number of wins first
    target = t_wins
    t = a = 0
    for ch in s:
        if ch == 'T':
            t += 1
            if t == target:
                print('T')
                return
        else:
            a += 1
            if a == target:
                print('A')
                return

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
    n = int(data[0])
    s = data[1].strip()

    t_wins = s.count('T')
    a_wins = n - t_wins

    if t_wins > a_wins:
        print('T')
        return
    if a_wins > t_wins:
        print('A')
        return

    # Tie: both have same wins; decide by who reached that count first.
    target = t_wins  # == a_wins
    t_reached = a_reached = None
    tc = ac = 0
    for i, ch in enumerate(s, start=1):
        if ch == 'T':
            tc += 1
            if t_reached is None and tc == target:
                t_reached = i
        else:
            ac += 1
            if a_reached is None and ac == target:
                a_reached = i
        if t_reached is not None and a_reached is not None:
            break

    print('T' if t_reached < a_reached else 'A')

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
    n = int(data[0])
    s = data[1].strip()

    t_wins = 0
    a_wins = 0
    for ch in s:
        if ch == 'T':
            t_wins += 1
        else:
            a_wins += 1

    if t_wins > a_wins:
        print("T")
        return
    if a_wins > t_wins:
        print("A")
        return

    # Tie: both have same wins; whoever reached that win count first wins.
    target = t_wins
    t_reached = a_reached = None
    for i, ch in enumerate(s):
        if ch == 'T':
            t_wins_so_far = s[:i+1].count('T')
            if t_reached is None and t_wins_so_far == target:
                t_reached = i
        else:
            a_wins_so_far = s[:i+1].count('A')
            if a_reached is None and a_wins_so_far == target:
                a_reached = i
        if t_reached is not None and a_reached is not None:
            break

    # Compare first reach times
    print("T" if t_reached < a_reached else "A")

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
    n = int(data[0])
    s = data[1].strip()

    t_wins = s.count('T')
    a_wins = n - t_wins

    if t_wins > a_wins:
        print('T')
        return
    if a_wins > t_wins:
        print('A')
        return

    # Tie: reached that number of wins first.
    target = t_wins  # == a_wins
    t_reach = None
    a_reach = None
    t_cnt = a_cnt = 0

    for i, ch in enumerate(s, start=1):
        if ch == 'T':
            t_cnt += 1
            if t_reach is None and t_cnt == target:
                t_reach = i
        else:
            a_cnt += 1
            if a_reach is None and a_cnt == target:
                a_reach = i

        if t_reach is not None and a_reach is not None:
            break

    print('T' if t_reach < a_reach else 'A')

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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
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
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "T",
      "actual": "T",
      "error": ""
    },
    {
      "passed": true,
      "expected": "A",
      "actual": "A",
      "error": ""
    }
  ]
}
```

</details>
