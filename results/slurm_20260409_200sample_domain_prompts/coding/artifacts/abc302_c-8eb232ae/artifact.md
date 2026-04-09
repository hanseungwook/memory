# Problem abc302_c

- Domain: `coding`

## Problem

```text
You are given N strings S_1,S_2,\dots,S_N, each of length M, consisting of lowercase English letter.  Here, S_i are pairwise distinct.
Determine if one can rearrange these strings to obtain a new sequence of strings T_1,T_2,\dots,T_N such that:

- for all integers i such that 1 \le i \le N-1, one can alter exactly one character of T_i to another lowercase English letter to make it equal to T_{i+1}.

Input

The input is given from Standard Input in the following format:
N M
S_1
S_2
\vdots
S_N

Output

Print Yes if one can obtain a conforming sequence; print No otherwise.

Constraints


- 2 \le N \le 8
- 1 \le M \le 5
- S_i is a string of length M consisting of lowercase English letters.  (1 \le i \le N)
- S_i are pairwise distinct.

Sample Input 1

4 4
bbed
abcd
abed
fbed

Sample Output 1

Yes

One can rearrange them in this order: abcd, abed, bbed, fbed.  This sequence satisfies the condition.

Sample Input 2

2 5
abcde
abced

Sample Output 2

No

No matter how the strings are rearranged, the condition is never satisfied.

Sample Input 3

8 4
fast
face
cast
race
fact
rice
nice
case

Sample Output 3

Yes
```

### Test Cases

```json
[
  {
    "input": "4 4\nbbed\nabcd\nabed\nfbed\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "2 5\nabcde\nabced\n",
    "output": "No\n",
    "testtype": "stdin"
  },
  {
    "input": "8 4\nfast\nface\ncast\nrace\nfact\nrice\nnice\ncase\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "2 2\nuw\nun\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "3 1\nj\nw\na\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "4 1\nz\ni\nj\nb\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "2 5\nwdqms\nppqfo\n",
    "output": "No\n",
    "testtype": "stdin"
  },
  {
    "input": "3 4\nyzuz\nezuz\nuzuz\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "5 3\nbag\nbad\nbat\nbed\ndad\n",
    "output": "No\n",
    "testtype": "stdin"
  },
  {
    "input": "6 4\neeee\neeeg\ngeeg\nkeeg\nweee\nxeee\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "6 4\ncccc\ncccd\ndccd\njccd\noccc\nwccc\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "6 4\ncccc\ncccg\ngccg\nhccg\niccc\nuccc\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "8 5\nlvntx\nlvytx\nlvynx\nmvfox\nmvyox\novfox\nlvnwx\nmvynx\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "8 5\naoymb\nfoymb\npocmb\npvcdb\npicdb\npocdb\nfocmb\npicgb\n",
    "output": "Yes\n",
    "testtype": "stdin"
  },
  {
    "input": "8 5\nbtacv\nbgacv\nbtlcv\nbwoyv\nbgucv\nbtoyv\nbguyv\nbwuyv\n",
    "output": "Yes\n",
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
You are given N strings S_1,S_2,\dots,S_N, each of length M, consisting of lowercase English letter.  Here, S_i are pairwise distinct.
Determine if one can rearrange these strings to obtain a new sequence of strings T_1,T_2,\dots,T_N such that:

- for all integers i such that 1 \le i \le N-1, one can alter exactly one character of T_i to another lowercase English letter to make it equal to T_{i+1}.

Input

The input is given from Standard Input in the following format:
N M
S_1
S_2
\vdots
S_N

Output

Print Yes if one can obtain a conforming sequence; print No otherwise.

Constraints


- 2 \le N \le 8
- 1 \le M \le 5
- S_i is a string of length M consisting of lowercase English letters.  (1 \le i \le N)
- S_i are pairwise distinct.

Sample Input 1

4 4
bbed
abcd
abed
fbed

Sample Output 1

Yes

One can rearrange them in this order: abcd, abed, bbed, fbed.  This sequence satisfies the condition.

Sample Input 2

2 5
abcde
abced

Sample Output 2

No

No matter how the strings are rearranged, the condition is never satisfied.

Sample Input 3

8 4
fast
face
cast
race
fact
rice
nice
case

Sample Output 3

Yes

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
from itertools import permutations

def differs_by_one(a: str, b: str) -> bool:
    # True iff exactly one character differs
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    N = int(next(it))
    M = int(next(it))
    S = [next(it) for _ in range(N)]

    # Build adjacency based on "exactly one character differs"
    adj = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                adj[i][j] = differs_by_one(S[i], S[j])

    # Backtracking / DP over subsets to find Hamiltonian path in this directed graph
    # N <= 8 so bitmask DP is easy.
    FULL = (1 << N) - 1
    dp = [ [False]*N for _ in range(1 << N) ]
    # Start at any node
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(1 << N):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in range(N):
                if mask & (1 << nxt):
                    continue
                if adj[last][nxt]:
                    dp[mask | (1 << nxt)][nxt] = True

    ok = any(dp[FULL][last] for last in range(N))
    print("Yes" if ok else "No")

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
from functools import lru_cache

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # adjacency: i -> j if S_i can go to S_j by changing exactly one character
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            diff = 0
            for k in range(M):
                if S[i][k] != S[j][k]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                adj[i].append(j)

    full_mask = (1 << N) - 1

    @lru_cache(None)
    def dp(mask, last):
        # can we arrange strings in 'mask' ending at 'last' in a valid chain?
        if mask == (1 << last):
            return True
        pmask = mask ^ (1 << last)
        # try predecessor p such that p -> last and p in pmask
        for p in range(N):
            if (pmask >> p) & 1:
                # p must connect to last
                # check quickly by membership
                if last in adj[p]:
                    if dp(pmask, p):
                        return True
        return False

    for start in range(N):
        if dp(1 << start, start) and N == 1:
            print("Yes")
            return

    for last in range(N):
        if dp(full_mask, last):
            print("Yes")
            return
    print("No")

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
from collections import defaultdict

def diff1(a, b):
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if can go from S[i] to S[j] by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets, path uses all N nodes exactly once
    # dp[mask][last] = True if there exists a permutation of strings in 'mask' ending at 'last'
    # Start with any single node.
    size = 1 << N
    dp = [set() for _ in range(size)]
    for i in range(N):
        dp[1 << i].add(i)

    full = size - 1
    for mask in range(size):
        if not dp[mask]:
            continue
        for last in list(dp[mask]):
            # try to append a new node nxt not in mask
            for nxt in adj[last]:
                if (mask >> nxt) & 1:
                    continue
                nm = mask | (1 << nxt)
                dp[nm].add(nxt)

    if dp[full]:
        print("Yes")
    else:
        print("No")

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
from itertools import permutations

def differ_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: edge i->j if S[i] can reach S[j] by changing exactly one char.
    adj = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if differ_one(S[i], S[j]):
                    adj[i][j] = True

    # Since N <= 8, brute force permutations is feasible.
    for perm in permutations(range(N)):
        ok = True
        for k in range(N - 1):
            if not adj[perm[k]][perm[k+1]]:
                ok = False
                break
        if ok:
            print("Yes")
            return
    print("No")

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
from itertools import permutations

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Precompute adjacency: edge i->j if strings differ by exactly one character
    diff1 = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            cnt = 0
            a, b = S[i], S[j]
            for k in range(M):
                if a[k] != b[k]:
                    cnt += 1
                    if cnt > 1:
                        break
            if cnt == 1:
                diff1[i][j] = True

    # Try to find a Hamiltonian path in this directed graph
    # N <= 8, so bitmask DP is feasible.
    FULL = (1 << N) - 1
    dp = [[False]*N for _ in range(1 << N)]
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(1 << N):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in range(N):
                if (mask >> nxt) & 1:
                    continue
                if diff1[last][nxt]:
                    dp[mask | (1 << nxt)][nxt] = True

    for last in range(N):
        if dp[FULL][last]:
            print("Yes")
            return
    print("No")

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

def differ_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: edge i->j if S_i can become S_j by changing exactly one character
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differ_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = reachable
    # Use bitmask because N <= 8
    size = 1 << N
    dp = [0] * size  # dp[mask] is bitset of possible 'last' nodes
    for i in range(N):
        dp[1 << i] |= 1 << i

    for mask in range(size):
        if dp[mask] == 0:
            continue
        last_bits = dp[mask]
        # iterate last nodes in this mask
        lb = last_bits
        while lb:
            lsb = lb & -lb
            last = (lsb.bit_length() - 1)
            lb -= lsb
            # try extend
            for nxt in adj[last]:
                if not (mask & (1 << nxt)):
                    dp[mask | (1 << nxt)] |= 1 << nxt

    full = (1 << N) - 1
    print("Yes" if dp[full] != 0 else "No")

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
from itertools import permutations

def differs_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if Si can become Sj by changing exactly one char
    adj = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differs_by_one(S[i], S[j]):
                adj[i][j] = True

    # Try to find a Hamiltonian path in this directed graph
    # Since N<=8, use DP over subsets.
    # dp[mask][last] = True if we can form a path using strings in 'mask' ending at 'last'
    dp = [ [False]*N for _ in range(1<<N) ]
    for i in range(N):
        dp[1<<i][i] = True

    for mask in range(1<<N):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in range(N):
                if (mask >> nxt) & 1:
                    continue
                if adj[last][nxt]:
                    dp[mask | (1<<nxt)][nxt] = True

    full = (1<<N) - 1
    ok = any(dp[full][last] for last in range(N))
    print("Yes" if ok else "No")

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
from itertools import permutations

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    def diff1(a, b):
        # exactly one character differs
        d = 0
        for x, y in zip(a, b):
            if x != y:
                d += 1
                if d > 1:
                    return False
        return d == 1

    # Build adjacency graph
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = reachable
    # N <= 8, so this is small
    size = 1 << N
    dp = [set() for _ in range(size)]
    for i in range(N):
        dp[1 << i].add(i)

    for mask in range(size):
        if not dp[mask]:
            continue
        for last in list(dp[mask]):
            for nxt in adj[last]:
                nmask = mask | (1 << nxt)
                dp[nmask].add(nxt)

    full = size - 1
    print("Yes" if dp[full] else "No")

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
from itertools import permutations

def solve():
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Precompute adjacency: i -> j if by changing exactly one char of S[i] we can get S[j]
    def diff1(a, b):
        d = 0
        for x, y in zip(a, b):
            if x != y:
                d += 1
                if d > 1:
                    return False
        return d == 1

    adj = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i][j] = True

    # Hamiltonian path existence in directed graph of size <= 8
    # dp[mask][last] = True if there is a path visiting exactly mask ending at last
    size = 1 << N
    dp = [[False] * N for _ in range(size)]
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(size):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in range(N):
                if mask & (1 << nxt):
                    continue
                if adj[last][nxt]:
                    dp[mask | (1 << nxt)][nxt] = True

    full = size - 1
    ok = any(dp[full][last] for last in range(N))
    print("Yes" if ok else "No")

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
from functools import lru_cache

def differ_by_one(a: str, b: str) -> bool:
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build directed edges: i -> j if S_i can become S_j by changing exactly one character
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differ_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] means possible to form a path using exactly mask
    # (mask includes last), ending at last.
    size = 1 << N
    dp = [None] * size
    for mask in range(size):
        dp[mask] = [False] * N

    # Initialize singletons
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(size):
        for last in range(N):
            if not dp[mask][last]:
                continue
            # extend
            for nxt in adj[last]:
                if (mask >> nxt) & 1:
                    continue
                dp[mask | (1 << nxt)][nxt] = True

    full = size - 1
    ok = any(dp[full][last] for last in range(N))
    print("Yes" if ok else "No")

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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
from itertools import permutations

def differs_by_one(a: str, b: str) -> bool:
    # True iff exactly one character differs
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    N = int(next(it))
    M = int(next(it))
    S = [next(it) for _ in range(N)]

    # Build adjacency based on "exactly one character differs"
    adj = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                adj[i][j] = differs_by_one(S[i], S[j])

    # Backtracking / DP over subsets to find Hamiltonian path in this directed graph
    # N <= 8 so bitmask DP is easy.
    FULL = (1 << N) - 1
    dp = [ [False]*N for _ in range(1 << N) ]
    # Start at any node
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(1 << N):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in range(N):
                if mask & (1 << nxt):
                    continue
                if adj[last][nxt]:
                    dp[mask | (1 << nxt)][nxt] = True

    ok = any(dp[FULL][last] for last in range(N))
    print("Yes" if ok else "No")

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
from functools import lru_cache

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # adjacency: i -> j if S_i can go to S_j by changing exactly one character
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            diff = 0
            for k in range(M):
                if S[i][k] != S[j][k]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                adj[i].append(j)

    full_mask = (1 << N) - 1

    @lru_cache(None)
    def dp(mask, last):
        # can we arrange strings in 'mask' ending at 'last' in a valid chain?
        if mask == (1 << last):
            return True
        pmask = mask ^ (1 << last)
        # try predecessor p such that p -> last and p in pmask
        for p in range(N):
            if (pmask >> p) & 1:
                # p must connect to last
                # check quickly by membership
                if last in adj[p]:
                    if dp(pmask, p):
                        return True
        return False

    for start in range(N):
        if dp(1 << start, start) and N == 1:
            print("Yes")
            return

    for last in range(N):
        if dp(full_mask, last):
            print("Yes")
            return
    print("No")

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
from collections import defaultdict

def diff1(a, b):
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if can go from S[i] to S[j] by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets, path uses all N nodes exactly once
    # dp[mask][last] = True if there exists a permutation of strings in 'mask' ending at 'last'
    # Start with any single node.
    size = 1 << N
    dp = [set() for _ in range(size)]
    for i in range(N):
        dp[1 << i].add(i)

    full = size - 1
    for mask in range(size):
        if not dp[mask]:
            continue
        for last in list(dp[mask]):
            # try to append a new node nxt not in mask
            for nxt in adj[last]:
                if (mask >> nxt) & 1:
                    continue
                nm = mask | (1 << nxt)
                dp[nm].add(nxt)

    if dp[full]:
        print("Yes")
    else:
        print("No")

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
from itertools import permutations

def differ_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: edge i->j if S[i] can reach S[j] by changing exactly one char.
    adj = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if differ_one(S[i], S[j]):
                    adj[i][j] = True

    # Since N <= 8, brute force permutations is feasible.
    for perm in permutations(range(N)):
        ok = True
        for k in range(N - 1):
            if not adj[perm[k]][perm[k+1]]:
                ok = False
                break
        if ok:
            print("Yes")
            return
    print("No")

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
from itertools import permutations

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Precompute adjacency: edge i->j if strings differ by exactly one character
    diff1 = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            cnt = 0
            a, b = S[i], S[j]
            for k in range(M):
                if a[k] != b[k]:
                    cnt += 1
                    if cnt > 1:
                        break
            if cnt == 1:
                diff1[i][j] = True

    # Try to find a Hamiltonian path in this directed graph
    # N <= 8, so bitmask DP is feasible.
    FULL = (1 << N) - 1
    dp = [[False]*N for _ in range(1 << N)]
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(1 << N):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in range(N):
                if (mask >> nxt) & 1:
                    continue
                if diff1[last][nxt]:
                    dp[mask | (1 << nxt)][nxt] = True

    for last in range(N):
        if dp[FULL][last]:
            print("Yes")
            return
    print("No")

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

def differ_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: edge i->j if S_i can become S_j by changing exactly one character
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differ_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = reachable
    # Use bitmask because N <= 8
    size = 1 << N
    dp = [0] * size  # dp[mask] is bitset of possible 'last' nodes
    for i in range(N):
        dp[1 << i] |= 1 << i

    for mask in range(size):
        if dp[mask] == 0:
            continue
        last_bits = dp[mask]
        # iterate last nodes in this mask
        lb = last_bits
        while lb:
            lsb = lb & -lb
            last = (lsb.bit_length() - 1)
            lb -= lsb
            # try extend
            for nxt in adj[last]:
                if not (mask & (1 << nxt)):
                    dp[mask | (1 << nxt)] |= 1 << nxt

    full = (1 << N) - 1
    print("Yes" if dp[full] != 0 else "No")

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
from itertools import permutations

def differs_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if Si can become Sj by changing exactly one char
    adj = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differs_by_one(S[i], S[j]):
                adj[i][j] = True

    # Try to find a Hamiltonian path in this directed graph
    # Since N<=8, use DP over subsets.
    # dp[mask][last] = True if we can form a path using strings in 'mask' ending at 'last'
    dp = [ [False]*N for _ in range(1<<N) ]
    for i in range(N):
        dp[1<<i][i] = True

    for mask in range(1<<N):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in range(N):
                if (mask >> nxt) & 1:
                    continue
                if adj[last][nxt]:
                    dp[mask | (1<<nxt)][nxt] = True

    full = (1<<N) - 1
    ok = any(dp[full][last] for last in range(N))
    print("Yes" if ok else "No")

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
from itertools import permutations

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    def diff1(a, b):
        # exactly one character differs
        d = 0
        for x, y in zip(a, b):
            if x != y:
                d += 1
                if d > 1:
                    return False
        return d == 1

    # Build adjacency graph
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = reachable
    # N <= 8, so this is small
    size = 1 << N
    dp = [set() for _ in range(size)]
    for i in range(N):
        dp[1 << i].add(i)

    for mask in range(size):
        if not dp[mask]:
            continue
        for last in list(dp[mask]):
            for nxt in adj[last]:
                nmask = mask | (1 << nxt)
                dp[nmask].add(nxt)

    full = size - 1
    print("Yes" if dp[full] else "No")

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
from itertools import permutations

def solve():
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Precompute adjacency: i -> j if by changing exactly one char of S[i] we can get S[j]
    def diff1(a, b):
        d = 0
        for x, y in zip(a, b):
            if x != y:
                d += 1
                if d > 1:
                    return False
        return d == 1

    adj = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i][j] = True

    # Hamiltonian path existence in directed graph of size <= 8
    # dp[mask][last] = True if there is a path visiting exactly mask ending at last
    size = 1 << N
    dp = [[False] * N for _ in range(size)]
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(size):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in range(N):
                if mask & (1 << nxt):
                    continue
                if adj[last][nxt]:
                    dp[mask | (1 << nxt)][nxt] = True

    full = size - 1
    ok = any(dp[full][last] for last in range(N))
    print("Yes" if ok else "No")

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
from functools import lru_cache

def differ_by_one(a: str, b: str) -> bool:
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build directed edges: i -> j if S_i can become S_j by changing exactly one character
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differ_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] means possible to form a path using exactly mask
    # (mask includes last), ending at last.
    size = 1 << N
    dp = [None] * size
    for mask in range(size):
        dp[mask] = [False] * N

    # Initialize singletons
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(size):
        for last in range(N):
            if not dp[mask][last]:
                continue
            # extend
            for nxt in adj[last]:
                if (mask >> nxt) & 1:
                    continue
                dp[mask | (1 << nxt)][nxt] = True

    full = size - 1
    ok = any(dp[full][last] for last in range(N))
    print("Yes" if ok else "No")

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
You are given N strings S_1,S_2,\dots,S_N, each of length M, consisting of lowercase English letter.  Here, S_i are pairwise distinct.
Determine if one can rearrange these strings to obtain a new sequence of strings T_1,T_2,\dots,T_N such that:

- for all integers i such that 1 \le i \le N-1, one can alter exactly one character of T_i to another lowercase English letter to make it equal to T_{i+1}.

Input

The input is given from Standard Input in the following format:
N M
S_1
S_2
\vdots
S_N

Output

Print Yes if one can obtain a conforming sequence; print No otherwise.

Constraints


- 2 \le N \le 8
- 1 \le M \le 5
- S_i is a string of length M consisting of lowercase English letters.  (1 \le i \le N)
- S_i are pairwise distinct.

Sample Input 1

4 4
bbed
abcd
abed
fbed

Sample Output 1

Yes

One can rearrange them in this order: abcd, abed, bbed, fbed.  This sequence satisfies the condition.

Sample Input 2

2 5
abcde
abced

Sample Output 2

No

No matter how the strings are rearranged, the condition is never satisfied.

Sample Input 3

8 4
fast
face
cast
race
fact
rice
nice
case

Sample Output 3

Yes

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
from collections import defaultdict

def main():
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Precompute edges: i -> j if S_i can reach S_j by changing exactly one character
    idx = list(range(N))
    edges = [[] for _ in range(N)]

    def one_change(a, b):
        diff = 0
        for x, y in zip(a, b):
            if x != y:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    for i in idx:
        for j in idx:
            if i != j and one_change(S[i], S[j]):
                edges[i].append(j)

    # DP over subsets (Hamiltonian path in this directed graph)
    # N <= 8 so this is easy.
    full = (1 << N) - 1
    dp = [None] * (1 << N)  # dp[mask] is a bitset of possible ending nodes
    # Use bitmask to represent set of ends.
    for i in idx:
        dp[1 << i] = (1 << i)

    for mask in range(1 << N):
        if dp[mask] is None:
            continue
        ends_bitset = dp[mask]
        # iterate bits
        e = ends_bitset
        while e:
            lsb = e & -e
            u = (lsb.bit_length() - 1)
            e -= lsb
            for v in edges[u]:
                nmask = mask | (1 << v)
                if dp[nmask] is None:
                    dp[nmask] = (1 << v)
                else:
                    dp[nmask] |= (1 << v)

    # Check any end node for full mask
    if dp[full] is not None:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
import sys
from functools import lru_cache

def differ_by_one(a: str, b: str) -> bool:
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if S_i can become S_j by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differ_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets to find Hamiltonian path in directed graph
    # dp[mask][last] = True if there's a path using exactly strings in mask ending at last
    size = 1 << N
    dp = [0] * size  # bitset of last nodes
    for i in range(N):
        dp[1 << i] |= 1 << i

    for mask in range(size):
        lasts = dp[mask]
        if lasts == 0:
            continue
        for last in range(N):
            if (lasts >> last) & 1 == 0:
                continue
            # try extending to nxt not in mask
            for nxt in adj[last]:
                if (mask >> nxt) & 1 == 0:
                    dp[mask | (1 << nxt)] |= 1 << nxt

    full = size - 1
    print("Yes" if dp[full] != 0 else "No")

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
from functools import lru_cache

def diff_one(a: str, b: str) -> bool:
    # True iff a and b differ in exactly one position
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build directed edges: i -> j if S[i] can become S[j] by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: does there exist a Hamiltonian path following edges?
    # dp[mask][last] = True if mask includes 'last' and there is a valid path using exactly those nodes.
    # N <= 8 so bitmask is fine.
    size = 1 << N
    dp = [0] * size
    # dp[mask] bitset of possible 'last' vertices
    for i in range(N):
        dp[1 << i] |= 1 << i

    for mask in range(size):
        last_bits = dp[mask]
        if last_bits == 0:
            continue
        # try to extend to any next vertex not in mask
        # Iterate possible last vertices
        for last in range(N):
            if (last_bits >> last) & 1 == 0:
                continue
            for nxt in adj[last]:
                if (mask >> nxt) & 1 == 0:
                    dp[mask | (1 << nxt)] |= 1 << nxt

    full = (1 << N) - 1
    print("Yes" if dp[full] != 0 else "No")

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
from functools import lru_cache

def differs_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if S_i can go to S_j by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differs_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = possible
    # Use bitmask with N <= 8
    full = (1 << N) - 1
    dp = [0] * (1 << N)
    # We'll store reachable last nodes as bitsets
    for i in range(N):
        dp[1 << i] |= (1 << i)

    for mask in range(1 << N):
        last_bits = dp[mask]
        if last_bits == 0:
            continue
        for last in range(N):
            if not (last_bits >> last) & 1:
                continue
            for nxt in adj[last]:
                nmask = mask | (1 << nxt)
                dp[nmask] |= (1 << nxt)

    ok = dp[full] != 0
    print("Yes" if ok else "No")

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
from itertools import permutations

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    def diff1(a, b):
        # True iff a and b differ at exactly one position
        cnt = 0
        for x, y in zip(a, b):
            if x != y:
                cnt += 1
                if cnt > 1:
                    return False
        return cnt == 1

    # Build adjacency graph where an edge means can go in one step
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i].append(j)

    # Since N <= 8, do DP over subsets for Hamiltonian path existence.
    # dp[mask][last] = reachable
    size = 1 << N
    dp = [0] * size
    # Use bitset per mask? simpler: dp[mask][last] as boolean in sets
    # We'll store dp_mask_last as list of bitsets.
    reach = [0] * size  # bitset of possible last indices
    for i in range(N):
        reach[1 << i] |= 1 << i

    for mask in range(size):
        lasts = reach[mask]
        if lasts == 0:
            continue
        for last in range(N):
            if (lasts >> last) & 1 == 0:
                continue
            # try to extend
            for nxt in adj[last]:
                if (mask >> nxt) & 1:
                    continue
                newmask = mask | (1 << nxt)
                reach[newmask] |= 1 << nxt

    full = (1 << N) - 1
    print("Yes" if reach[full] != 0 else "No")

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
from itertools import permutations

def diff1(a: str, b: str) -> bool:
    d = 0
    for x, y in zip(a, b):
        if x != y:
            d += 1
            if d > 1:
                return False
    return d == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency graph: edge i->j if S[i] can go to S[j] with exactly one char change
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = possible
    size = 1 << N
    dp = [[False] * N for _ in range(size)]
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(size):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in adj[last]:
                if not (mask >> nxt) & 1:
                    dp[mask | (1 << nxt)][nxt] = True

    full = size - 1
    ans = any(dp[full][last] for last in range(N))
    print("Yes" if ans else "No")

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
from itertools import permutations

def differs_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if S[i] can go to S[j] by changing exactly one character
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differs_by_one(S[i], S[j]):
                adj[i].append(j)

    # Since N <= 8, use DFS with pruning over subsets (Hamiltonian path in this directed graph)
    # DP over subsets: dp[mask][last] = reachable
    size = 1 << N
    dp = [[False] * N for _ in range(size)]

    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(size):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in adj[last]:
                if mask & (1 << nxt):
                    continue
                dp[mask | (1 << nxt)][nxt] = True

    full = (1 << N) - 1
    ok = any(dp[full][last] for last in range(N))
    print("Yes" if ok else "No")

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

def one_edit_away(a: str, b: str) -> bool:
    # Check if Hamming distance is exactly 1 (same length guaranteed)
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency graph: edge i->j if S_i can become S_j by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and one_edit_away(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = True if we can form a valid sequence
    # using exactly strings in mask and ending at 'last'.
    size = 1 << N
    dp = [0] * size
    # dp_mask_last encoded as bitset in dp[mask], where bit 'k' means dp[mask][k]=True
    # Initialize: sequences of length 1
    for i in range(N):
        dp[1 << i] |= 1 << i

    for mask in range(size):
        if dp[mask] == 0:
            continue
        cur_bits = dp[mask]
        # try extending to any j not in mask
        for last in range(N):
            if (cur_bits >> last) & 1 == 0:
                continue
            for nxt in adj[last]:
                if (mask >> nxt) & 1:
                    continue
                nmask = mask | (1 << nxt)
                dp[nmask] |= 1 << nxt

    full = (1 << N) - 1
    print("Yes" if dp[full] != 0 else "No")

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
from collections import defaultdict

def differs_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if can change exactly one character of S[i] to get S[j]
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differs_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = reachable
    # N <= 8 so we can do bitmask DP
    FULL = (1 << N) - 1
    dp = [0] * (1 << N)  # dp[mask] bitset of possible last indices
    for i in range(N):
        dp[1 << i] |= (1 << i)

    for mask in range(1 << N):
        if dp[mask] == 0:
            continue
        last_bits = dp[mask]
        for last in range(N):
            if not (last_bits >> last) & 1:
                continue
            for nxt in adj[last]:
                nmask = mask | (1 << nxt)
                dp[nmask] |= (1 << nxt)

    # If any last is reachable with all used, answer Yes
    print("Yes" if dp[FULL] != 0 else "No")

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
from functools import lru_cache

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Precompute adjacency: i -> j if S_i can become S_j by changing exactly one character
    adj = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            diff = 0
            a, b = S[i], S[j]
            for k in range(M):
                if a[k] != b[k]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                adj[i][j] = True

    full_mask = (1 << N) - 1

    # DP over subsets: dp[mask][last] = possible
    # N <= 8, so use bitmask DP with memoization.
    @lru_cache(None)
    def dfs(mask, last):
        if mask == full_mask:
            return True
        # try append next string not used yet
        for nxt in range(N):
            if (mask >> nxt) & 1:
                continue
            if adj[last][nxt] and dfs(mask | (1 << nxt), nxt):
                return True
        return False

    for start in range(N):
        if dfs(1 << start, start):
            print("Yes")
            return
    print("No")

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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
from collections import defaultdict

def main():
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Precompute edges: i -> j if S_i can reach S_j by changing exactly one character
    idx = list(range(N))
    edges = [[] for _ in range(N)]

    def one_change(a, b):
        diff = 0
        for x, y in zip(a, b):
            if x != y:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    for i in idx:
        for j in idx:
            if i != j and one_change(S[i], S[j]):
                edges[i].append(j)

    # DP over subsets (Hamiltonian path in this directed graph)
    # N <= 8 so this is easy.
    full = (1 << N) - 1
    dp = [None] * (1 << N)  # dp[mask] is a bitset of possible ending nodes
    # Use bitmask to represent set of ends.
    for i in idx:
        dp[1 << i] = (1 << i)

    for mask in range(1 << N):
        if dp[mask] is None:
            continue
        ends_bitset = dp[mask]
        # iterate bits
        e = ends_bitset
        while e:
            lsb = e & -e
            u = (lsb.bit_length() - 1)
            e -= lsb
            for v in edges[u]:
                nmask = mask | (1 << v)
                if dp[nmask] is None:
                    dp[nmask] = (1 << v)
                else:
                    dp[nmask] |= (1 << v)

    # Check any end node for full mask
    if dp[full] is not None:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
import sys
from functools import lru_cache

def differ_by_one(a: str, b: str) -> bool:
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if S_i can become S_j by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differ_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets to find Hamiltonian path in directed graph
    # dp[mask][last] = True if there's a path using exactly strings in mask ending at last
    size = 1 << N
    dp = [0] * size  # bitset of last nodes
    for i in range(N):
        dp[1 << i] |= 1 << i

    for mask in range(size):
        lasts = dp[mask]
        if lasts == 0:
            continue
        for last in range(N):
            if (lasts >> last) & 1 == 0:
                continue
            # try extending to nxt not in mask
            for nxt in adj[last]:
                if (mask >> nxt) & 1 == 0:
                    dp[mask | (1 << nxt)] |= 1 << nxt

    full = size - 1
    print("Yes" if dp[full] != 0 else "No")

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
from functools import lru_cache

def diff_one(a: str, b: str) -> bool:
    # True iff a and b differ in exactly one position
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build directed edges: i -> j if S[i] can become S[j] by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: does there exist a Hamiltonian path following edges?
    # dp[mask][last] = True if mask includes 'last' and there is a valid path using exactly those nodes.
    # N <= 8 so bitmask is fine.
    size = 1 << N
    dp = [0] * size
    # dp[mask] bitset of possible 'last' vertices
    for i in range(N):
        dp[1 << i] |= 1 << i

    for mask in range(size):
        last_bits = dp[mask]
        if last_bits == 0:
            continue
        # try to extend to any next vertex not in mask
        # Iterate possible last vertices
        for last in range(N):
            if (last_bits >> last) & 1 == 0:
                continue
            for nxt in adj[last]:
                if (mask >> nxt) & 1 == 0:
                    dp[mask | (1 << nxt)] |= 1 << nxt

    full = (1 << N) - 1
    print("Yes" if dp[full] != 0 else "No")

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
from functools import lru_cache

def differs_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if S_i can go to S_j by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differs_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = possible
    # Use bitmask with N <= 8
    full = (1 << N) - 1
    dp = [0] * (1 << N)
    # We'll store reachable last nodes as bitsets
    for i in range(N):
        dp[1 << i] |= (1 << i)

    for mask in range(1 << N):
        last_bits = dp[mask]
        if last_bits == 0:
            continue
        for last in range(N):
            if not (last_bits >> last) & 1:
                continue
            for nxt in adj[last]:
                nmask = mask | (1 << nxt)
                dp[nmask] |= (1 << nxt)

    ok = dp[full] != 0
    print("Yes" if ok else "No")

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
from itertools import permutations

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    def diff1(a, b):
        # True iff a and b differ at exactly one position
        cnt = 0
        for x, y in zip(a, b):
            if x != y:
                cnt += 1
                if cnt > 1:
                    return False
        return cnt == 1

    # Build adjacency graph where an edge means can go in one step
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i].append(j)

    # Since N <= 8, do DP over subsets for Hamiltonian path existence.
    # dp[mask][last] = reachable
    size = 1 << N
    dp = [0] * size
    # Use bitset per mask? simpler: dp[mask][last] as boolean in sets
    # We'll store dp_mask_last as list of bitsets.
    reach = [0] * size  # bitset of possible last indices
    for i in range(N):
        reach[1 << i] |= 1 << i

    for mask in range(size):
        lasts = reach[mask]
        if lasts == 0:
            continue
        for last in range(N):
            if (lasts >> last) & 1 == 0:
                continue
            # try to extend
            for nxt in adj[last]:
                if (mask >> nxt) & 1:
                    continue
                newmask = mask | (1 << nxt)
                reach[newmask] |= 1 << nxt

    full = (1 << N) - 1
    print("Yes" if reach[full] != 0 else "No")

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
from itertools import permutations

def diff1(a: str, b: str) -> bool:
    d = 0
    for x, y in zip(a, b):
        if x != y:
            d += 1
            if d > 1:
                return False
    return d == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency graph: edge i->j if S[i] can go to S[j] with exactly one char change
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and diff1(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = possible
    size = 1 << N
    dp = [[False] * N for _ in range(size)]
    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(size):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in adj[last]:
                if not (mask >> nxt) & 1:
                    dp[mask | (1 << nxt)][nxt] = True

    full = size - 1
    ans = any(dp[full][last] for last in range(N))
    print("Yes" if ans else "No")

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
from itertools import permutations

def differs_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if S[i] can go to S[j] by changing exactly one character
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differs_by_one(S[i], S[j]):
                adj[i].append(j)

    # Since N <= 8, use DFS with pruning over subsets (Hamiltonian path in this directed graph)
    # DP over subsets: dp[mask][last] = reachable
    size = 1 << N
    dp = [[False] * N for _ in range(size)]

    for i in range(N):
        dp[1 << i][i] = True

    for mask in range(size):
        for last in range(N):
            if not dp[mask][last]:
                continue
            for nxt in adj[last]:
                if mask & (1 << nxt):
                    continue
                dp[mask | (1 << nxt)][nxt] = True

    full = (1 << N) - 1
    ok = any(dp[full][last] for last in range(N))
    print("Yes" if ok else "No")

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

def one_edit_away(a: str, b: str) -> bool:
    # Check if Hamming distance is exactly 1 (same length guaranteed)
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency graph: edge i->j if S_i can become S_j by changing exactly one char
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and one_edit_away(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = True if we can form a valid sequence
    # using exactly strings in mask and ending at 'last'.
    size = 1 << N
    dp = [0] * size
    # dp_mask_last encoded as bitset in dp[mask], where bit 'k' means dp[mask][k]=True
    # Initialize: sequences of length 1
    for i in range(N):
        dp[1 << i] |= 1 << i

    for mask in range(size):
        if dp[mask] == 0:
            continue
        cur_bits = dp[mask]
        # try extending to any j not in mask
        for last in range(N):
            if (cur_bits >> last) & 1 == 0:
                continue
            for nxt in adj[last]:
                if (mask >> nxt) & 1:
                    continue
                nmask = mask | (1 << nxt)
                dp[nmask] |= 1 << nxt

    full = (1 << N) - 1
    print("Yes" if dp[full] != 0 else "No")

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
from collections import defaultdict

def differs_by_one(a: str, b: str) -> bool:
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Build adjacency: i -> j if can change exactly one character of S[i] to get S[j]
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and differs_by_one(S[i], S[j]):
                adj[i].append(j)

    # DP over subsets: dp[mask][last] = reachable
    # N <= 8 so we can do bitmask DP
    FULL = (1 << N) - 1
    dp = [0] * (1 << N)  # dp[mask] bitset of possible last indices
    for i in range(N):
        dp[1 << i] |= (1 << i)

    for mask in range(1 << N):
        if dp[mask] == 0:
            continue
        last_bits = dp[mask]
        for last in range(N):
            if not (last_bits >> last) & 1:
                continue
            for nxt in adj[last]:
                nmask = mask | (1 << nxt)
                dp[nmask] |= (1 << nxt)

    # If any last is reachable with all used, answer Yes
    print("Yes" if dp[FULL] != 0 else "No")

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
from functools import lru_cache

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # Precompute adjacency: i -> j if S_i can become S_j by changing exactly one character
    adj = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            diff = 0
            a, b = S[i], S[j]
            for k in range(M):
                if a[k] != b[k]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                adj[i][j] = True

    full_mask = (1 << N) - 1

    # DP over subsets: dp[mask][last] = possible
    # N <= 8, so use bitmask DP with memoization.
    @lru_cache(None)
    def dfs(mask, last):
        if mask == full_mask:
            return True
        # try append next string not used yet
        for nxt in range(N):
            if (mask >> nxt) & 1:
                continue
            if adj[last][nxt] and dfs(mask | (1 << nxt), nxt):
                return True
        return False

    for start in range(N):
        if dfs(1 << start, start):
            print("Yes")
            return
    print("No")

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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
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
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "No",
      "actual": "No",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    },
    {
      "passed": true,
      "expected": "Yes",
      "actual": "Yes",
      "error": ""
    }
  ]
}
```

</details>
