# Problem 2791

- Domain: `coding`

## Problem

```text
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the i^th friend brings you to the (i+1)^th friend for 1 <= i < n, and moving clockwise from the n^th friend brings you to the 1^st friend.
The rules of the game are as follows:
1^st friend receives the ball.

After that, 1^st friend passes it to the friend who is k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 2 * k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 3 * k steps away from them in the clockwise direction, and so on and so forth.

In other words, on the i^th turn, the friend holding the ball should pass it to the friend who is i * k steps away from them in the clockwise direction.
The game is finished when some friend receives the ball for the second time.
The losers of the game are friends who did not receive the ball in the entire game.
Given the number of friends, n, and an integer k, return the array answer, which contains the losers of the game in the ascending order.
 
Example 1:

Input: n = 5, k = 2
Output: [4,5]
Explanation: The game goes as follows:
1) Start at 1^st friend and pass the ball to the friend who is 2 steps away from them - 3^rd friend.
2) 3^rd friend passes the ball to the friend who is 4 steps away from them - 2^nd friend.
3) 2^nd friend passes the ball to the friend who is 6 steps away from them  - 3^rd friend.
4) The game ends as 3^rd friend receives the ball for the second time.

Example 2:

Input: n = 4, k = 4
Output: [2,3,4]
Explanation: The game goes as follows:
1) Start at the 1^st friend and pass the ball to the friend who is 4 steps away from them - 1^st friend.
2) The game ends as 1^st friend receives the ball for the second time.

 
Constraints:

1 <= k <= n <= 50
```

### Starter Code

```python
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
```

### Test Cases

```json
[
  {
    "input": "5\n2",
    "output": "[4, 5]",
    "testtype": "functional"
  },
  {
    "input": "4\n4",
    "output": "[2, 3, 4]",
    "testtype": "functional"
  },
  {
    "input": "4\n3",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "2\n1",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "1\n1",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "4\n1",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "3\n1",
    "output": "[3]",
    "testtype": "functional"
  },
  {
    "input": "3\n3",
    "output": "[2, 3]",
    "testtype": "functional"
  },
  {
    "input": "6\n4",
    "output": "[2, 3, 4, 6]",
    "testtype": "functional"
  },
  {
    "input": "33\n9",
    "output": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
    "testtype": "functional"
  },
  {
    "input": "50\n1",
    "output": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
    "testtype": "functional"
  },
  {
    "input": "49\n35",
    "output": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
    "testtype": "functional"
  },
  {
    "input": "50\n25",
    "output": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
    "testtype": "functional"
  },
  {
    "input": "50\n50",
    "output": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the i^th friend brings you to the (i+1)^th friend for 1 <= i < n, and moving clockwise from the n^th friend brings you to the 1^st friend.
The rules of the game are as follows:
1^st friend receives the ball.

After that, 1^st friend passes it to the friend who is k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 2 * k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 3 * k steps away from them in the clockwise direction, and so on and so forth.

In other words, on the i^th turn, the friend holding the ball should pass it to the friend who is i * k steps away from them in the clockwise direction.
The game is finished when some friend receives the ball for the second time.
The losers of the game are friends who did not receive the ball in the entire game.
Given the number of friends, n, and an integer k, return the array answer, which contains the losers of the game in the ascending order.
 
Example 1:

Input: n = 5, k = 2
Output: [4,5]
Explanation: The game goes as follows:
1) Start at 1^st friend and pass the ball to the friend who is 2 steps away from them - 3^rd friend.
2) 3^rd friend passes the ball to the friend who is 4 steps away from them - 2^nd friend.
3) 2^nd friend passes the ball to the friend who is 6 steps away from them  - 3^rd friend.
4) The game ends as 3^rd friend receives the ball for the second time.

Example 2:

Input: n = 4, k = 4
Output: [2,3,4]
Explanation: The game goes as follows:
1) Start at the 1^st friend and pass the ball to the friend who is 4 steps away from them - 1^st friend.
2) The game ends as 1^st friend receives the ball for the second time.

 
Constraints:

1 <= k <= n <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        
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
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Use modular arithmetic to simulate visited holders.
        # But we can do it efficiently by finding the cycle in positions.
        visited = set()
        order_seen = set()

        cur = 0  # 0-based index for friend 1
        step = k
        t = 1
        while cur not in visited:
            visited.add(cur)
            order_seen.add(cur)
            # Next position: add (t*k) steps from current (t starts at 1)
            cur = (cur + t * step) % n
            t += 1

        # Players who never received the ball are the losers.
        # Since the first repeat indicates we've looped over all "winners"
        # (the game stops at the second time someone receives the ball),
        # the repeated position is in visited already; thus winners are visited.
        losers = [i + 1 for i in range(n) if i not in visited]
        return losers
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Each move from i to i + t*k (mod n), where t increases each turn.
        # The ball revisits a position when cumulative steps match modulo n.
        # This results in a cycle length equal to n / gcd(n, k).
        # Only friends in the cycle ever receive the ball; others are losers.
        import math

        g = math.gcd(n, k)
        winners = set()
        # Starting from friend 1, the set of receivers corresponds to:
        # positions after t steps: 1 + (t(t+1)/2)*k (mod n)
        # But winners are exactly those reachable before repetition, which count is n/g.
        # Those reachable correspond to indices 1, 1+g, 1+2g, ... in 1-based numbering.
        for i in range(n // g):
            winners.add(1 + i * g)

        losers = [i for i in range(1, n + 1) if i not in winners]
        return losers
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List
import math

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The ball visits friends according to step sizes:
        # positions: 1, 1+k, 1+3k, 1+6k, ... (mod n)
        # This results in visiting exactly the subgroup generated by k (mod n).
        # Hence the game ends when a visited position repeats; losers are those
        # not in the visited set. Count of visited friends is n / gcd(n, k).
        g = math.gcd(n, k)
        m = n // g  # number of friends who receive the ball at least once

        # Visited friends are: 1, 1+g, 1+2g, ..., 1+(m-1)g (mod n)
        visited = set(((1 + i * g - 1) % n) + 1 for i in range(m))

        return [i for i in range(1, n + 1) if i not in visited]
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List
import math

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Let step = k mod n. After t moves, position = 1 + sum_{i=1..t} (i*k)
        # = 1 + k * t(t+1)/2 (mod n). The ball repeats when this sequence cycles.
        # The set of friends who ever receive the ball has size equal to the
        # length of the cycle in this modular progression, which is n / gcd(n, k)
        # (equivalently, some standard derivation for this problem variant).
        step_gcd = math.gcd(n, k)
        m = n // step_gcd  # number of distinct receivers (including initial)
        
        # The receivers are every (k mod n)th friend starting from 1 in a cycle;
        # losers are the rest.
        # Since n <= 50, simplest: simulate using visited until repeat.
        visited = [False] * n
        pos = 0  # 0-based, start at friend 1
        t = 1
        while not visited[pos]:
            visited[pos] = True
            pos = (pos + t * k) % n
            t += 1
        
        # Losers are those who never received the ball
        return [i + 1 for i, v in enumerate(visited) if not v]
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Simulation is fine for n <= 50, but we can do it deterministically:
        # The ball holder sequence is periodic; we track visited holders.
        visited = [False] * (n + 1)  # 1..n
        pos = 1
        step = 1
        visited[pos] = True

        while True:
            # Move i*k steps clockwise each turn, where current turn is step (1-based).
            pos = (pos + (step * k)) % n
            if pos == 0:
                pos = n

            if visited[pos]:
                break
            visited[pos] = True
            step += 1

        # Losers are those who never received the ball
        return [i for i in range(1, n + 1) if not visited[i]]
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List
from math import gcd

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        step = k
        # Let g be gcd(n, k). The ball visits exactly n/g distinct friends.
        g = gcd(n, step)
        visited = set()
        for i in range(n // g):
            # Position after i turns starting from friend 1:
            # 1 -> 1 + (1*k + 2*k + ... + i*k) = 1 + k * i*(i+1)/2
            pos = (1 + (step * i * (i + 1) // 2)) % n
            if pos == 0:
                pos = n
            visited.add(pos)

        losers = [i for i in range(1, n + 1) if i not in visited]
        return losers
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # When holding the ball at step i (0-indexed), the position advances by (i+1)*k.
        # Mod n, the sequence is: pos_j = 1 + k * (1+2+...+j) = 1 + k * T_j  (mod n).
        # The game ends when a position repeats, i.e., when the sequence has a cycle.
        #
        # A known result for this problem: the set of losers are exactly those positions
        # not reachable from 1 under steps of size k in terms of gcd.
        # Equivalent characterization: winners form a single arithmetic progression
        # modulo n with step size k; the number of winners is n / gcd(n, k).
        #
        # Losers are all friends not in winners set, in ascending order.
        import math

        g = math.gcd(n, k)
        winners = set()
        step = k % n
        pos = 0  # 0-based, starting at friend 1
        for _ in range(n // g):
            winners.add(pos)
            pos = (pos + step) % n

        # losers are those indices (0-based) not in winners
        losers = [i + 1 for i in range(n) if i not in winners]
        return losers
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The ball moves by i*k (mod n) at the i-th step.
        # Positions that ever receive the ball are exactly multiples of gcd(n, k) away from 0.
        # The game repeats when a position is reached twice; those are exactly the visited positions.
        d = __import__("math").gcd(n, k)
        losers = []
        # Convert to 1-based indexing:
        # visited positions are: 1, 1+d, 1+2d, ... (mod n). Others are losers.
        for person in range(1, n + 1):
            if (person - 1) % d != 0:
                losers.append(person)
        return losers
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Starting at friend 1, on turn i we move i*k steps clockwise.
        # Total positions visited are: 1 + k * (1 + 2 + ... + t) = 1 + k*t*(t+1)/2 (mod n)
        # The game ends when a position repeats. The visited set corresponds to residues of
        # k * triangular numbers; equivalently the process cycles with step based on gcd.
        #
        # It can be shown that the set of friends who ever receive the ball are exactly the
        # positions congruent to 1 modulo gcd(n, k). Thus losers are the rest.
        g = __import__("math").gcd(n, k)
        step = g
        losers = [i for i in range(1, n + 1) if (i - 1) % step != 0]
        return losers
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # simulate in terms of visited receivers
        visited = [False] * n
        cur = 0  # 0-based index for friend 1
        step = k % n

        # mark the starting friend as having received once
        visited[cur] = True

        # on turn i, move i*k steps; equivalently total movement after t turns:
        # cur = sum_{i=1..t} (i*k) mod n = t*(t+1)/2 * k mod n
        # We'll just simulate receivers until a repeat occurs.
        while True:
            # Next receiver index after i turns depends on i; easiest is iterative:
            # maintain increment multiplier using turn count.
            # We'll keep a running total of movement.
            break

        # Proper simulation with running total movement
        visited = [False] * n
        cur = 0
        visited[cur] = True
        total_move = 0
        i = 1  # turn count

        while True:
            total_move = (total_move + i * step) % n
            cur = total_move
            if visited[cur]:
                break
            visited[cur] = True
            i += 1

        losers = [idx + 1 for idx, ok in enumerate(visited) if not ok]
        return losers
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 1.0000 | `full` |
| 1 | 0.5714 | `partial` |
| 2 | 0.5714 | `partial` |
| 3 | 1.0000 | `full` |
| 4 | 1.0000 | `full` |
| 5 | 0.9286 | `partial` |
| 6 | 0.5714 | `partial` |
| 7 | 0.5714 | `partial` |
| 8 | 0.5714 | `partial` |
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 13,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 13, 14, 15, 18, 19, 20, 23, 24, 25, 28, 30, 33, 34, 35, 38, 39, 40, 43, 44, 45, 48, 49, 50]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the i^th friend brings you to the (i+1)^th friend for 1 <= i < n, and moving clockwise from the n^th friend brings you to the 1^st friend.
The rules of the game are as follows:
1^st friend receives the ball.

After that, 1^st friend passes it to the friend who is k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 2 * k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 3 * k steps away from them in the clockwise direction, and so on and so forth.

In other words, on the i^th turn, the friend holding the ball should pass it to the friend who is i * k steps away from them in the clockwise direction.
The game is finished when some friend receives the ball for the second time.
The losers of the game are friends who did not receive the ball in the entire game.
Given the number of friends, n, and an integer k, return the array answer, which contains the losers of the game in the ascending order.
 
Example 1:

Input: n = 5, k = 2
Output: [4,5]
Explanation: The game goes as follows:
1) Start at 1^st friend and pass the ball to the friend who is 2 steps away from them - 3^rd friend.
2) 3^rd friend passes the ball to the friend who is 4 steps away from them - 2^nd friend.
3) 2^nd friend passes the ball to the friend who is 6 steps away from them  - 3^rd friend.
4) The game ends as 3^rd friend receives the ball for the second time.

Example 2:

Input: n = 4, k = 4
Output: [2,3,4]
Explanation: The game goes as follows:
1) Start at the 1^st friend and pass the ball to the friend who is 4 steps away from them - 1^st friend.
2) The game ends as 1^st friend receives the ball for the second time.

 
Constraints:

1 <= k <= n <= 50

### Solutions
#### Correct
Attempt 1
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Use modular arithmetic to simulate visited holders.
        # But we can do it efficiently by finding the cycle in positions.
        visited = set()
        order_seen = set()

        cur = 0  # 0-based index for friend 1
        step = k
        t = 1
        while cur not in visited:
            visited.add(cur)
            order_seen.add(cur)
            # Next position: add (t*k) steps from current (t starts at 1)
            cur = (cur + t * step) % n
            t += 1

        # Players who never received the ball are the losers.
        # Since the first repeat indicates we've looped over all "winners"
        # (the game stops at the second time someone receives the ball),
        # the repeated position is in visited already; thus winners are visited.
        losers = [i + 1 for i in range(n) if i not in visited]
        return losers
```

Attempt 2
```python
from typing import List
import math

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Let step = k mod n. After t moves, position = 1 + sum_{i=1..t} (i*k)
        # = 1 + k * t(t+1)/2 (mod n). The ball repeats when this sequence cycles.
        # The set of friends who ever receive the ball has size equal to the
        # length of the cycle in this modular progression, which is n / gcd(n, k)
        # (equivalently, some standard derivation for this problem variant).
        step_gcd = math.gcd(n, k)
        m = n // step_gcd  # number of distinct receivers (including initial)
        
        # The receivers are every (k mod n)th friend starting from 1 in a cycle;
        # losers are the rest.
        # Since n <= 50, simplest: simulate using visited until repeat.
        visited = [False] * n
        pos = 0  # 0-based, start at friend 1
        t = 1
        while not visited[pos]:
            visited[pos] = True
            pos = (pos + t * k) % n
            t += 1
        
        # Losers are those who never received the ball
        return [i + 1 for i, v in enumerate(visited) if not v]
```

Attempt 3
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Simulation is fine for n <= 50, but we can do it deterministically:
        # The ball holder sequence is periodic; we track visited holders.
        visited = [False] * (n + 1)  # 1..n
        pos = 1
        step = 1
        visited[pos] = True

        while True:
            # Move i*k steps clockwise each turn, where current turn is step (1-based).
            pos = (pos + (step * k)) % n
            if pos == 0:
                pos = n

            if visited[pos]:
                break
            visited[pos] = True
            step += 1

        # Losers are those who never received the ball
        return [i for i in range(1, n + 1) if not visited[i]]
```

Attempt 4
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # simulate in terms of visited receivers
        visited = [False] * n
        cur = 0  # 0-based index for friend 1
        step = k % n

        # mark the starting friend as having received once
        visited[cur] = True

        # on turn i, move i*k steps; equivalently total movement after t turns:
        # cur = sum_{i=1..t} (i*k) mod n = t*(t+1)/2 * k mod n
        # We'll just simulate receivers until a repeat occurs.
        while True:
            # Next receiver index after i turns depends on i; easiest is iterative:
            # maintain increment multiplier using turn count.
            # We'll keep a running total of movement.
            break

        # Proper simulation with running total movement
        visited = [False] * n
        cur = 0
        visited[cur] = True
        total_move = 0
        i = 1  # turn count

        while True:
            total_move = (total_move + i * step) % n
            cur = total_move
            if visited[cur]:
                break
            visited[cur] = True
            i += 1

        losers = [idx + 1 for idx, ok in enumerate(visited) if not ok]
        return losers
```

#### Partially Correct
Attempt 1
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Each move from i to i + t*k (mod n), where t increases each turn.
        # The ball revisits a position when cumulative steps match modulo n.
        # This results in a cycle length equal to n / gcd(n, k).
        # Only friends in the cycle ever receive the ball; others are losers.
        import math

        g = math.gcd(n, k)
        winners = set()
        # Starting from friend 1, the set of receivers corresponds to:
        # positions after t steps: 1 + (t(t+1)/2)*k (mod n)
        # But winners are exactly those reachable before repetition, which count is n/g.
        # Those reachable correspond to indices 1, 1+g, 1+2g, ... in 1-based numbering.
        for i in range(n // g):
            winners.add(1 + i * g)

        losers = [i for i in range(1, n + 1) if i not in winners]
        return losers
```

Attempt 2
```python
from typing import List
import math

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The ball visits friends according to step sizes:
        # positions: 1, 1+k, 1+3k, 1+6k, ... (mod n)
        # This results in visiting exactly the subgroup generated by k (mod n).
        # Hence the game ends when a visited position repeats; losers are those
        # not in the visited set. Count of visited friends is n / gcd(n, k).
        g = math.gcd(n, k)
        m = n // g  # number of friends who receive the ball at least once

        # Visited friends are: 1, 1+g, 1+2g, ..., 1+(m-1)g (mod n)
        visited = set(((1 + i * g - 1) % n) + 1 for i in range(m))

        return [i for i in range(1, n + 1) if i not in visited]
```

Attempt 3
```python
from typing import List
from math import gcd

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        step = k
        # Let g be gcd(n, k). The ball visits exactly n/g distinct friends.
        g = gcd(n, step)
        visited = set()
        for i in range(n // g):
            # Position after i turns starting from friend 1:
            # 1 -> 1 + (1*k + 2*k + ... + i*k) = 1 + k * i*(i+1)/2
            pos = (1 + (step * i * (i + 1) // 2)) % n
            if pos == 0:
                pos = n
            visited.add(pos)

        losers = [i for i in range(1, n + 1) if i not in visited]
        return losers
```

Attempt 4
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # When holding the ball at step i (0-indexed), the position advances by (i+1)*k.
        # Mod n, the sequence is: pos_j = 1 + k * (1+2+...+j) = 1 + k * T_j  (mod n).
        # The game ends when a position repeats, i.e., when the sequence has a cycle.
        #
        # A known result for this problem: the set of losers are exactly those positions
        # not reachable from 1 under steps of size k in terms of gcd.
        # Equivalent characterization: winners form a single arithmetic progression
        # modulo n with step size k; the number of winners is n / gcd(n, k).
        #
        # Losers are all friends not in winners set, in ascending order.
        import math

        g = math.gcd(n, k)
        winners = set()
        step = k % n
        pos = 0  # 0-based, starting at friend 1
        for _ in range(n // g):
            winners.add(pos)
            pos = (pos + step) % n

        # losers are those indices (0-based) not in winners
        losers = [i + 1 for i in range(n) if i not in winners]
        return losers
```

Attempt 5
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The ball moves by i*k (mod n) at the i-th step.
        # Positions that ever receive the ball are exactly multiples of gcd(n, k) away from 0.
        # The game repeats when a position is reached twice; those are exactly the visited positions.
        d = __import__("math").gcd(n, k)
        losers = []
        # Convert to 1-based indexing:
        # visited positions are: 1, 1+d, 1+2d, ... (mod n). Others are losers.
        for person in range(1, n + 1):
            if (person - 1) % d != 0:
                losers.append(person)
        return losers
```

Attempt 6
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Starting at friend 1, on turn i we move i*k steps clockwise.
        # Total positions visited are: 1 + k * (1 + 2 + ... + t) = 1 + k*t*(t+1)/2 (mod n)
        # The game ends when a position repeats. The visited set corresponds to residues of
        # k * triangular numbers; equivalently the process cycles with step based on gcd.
        #
        # It can be shown that the set of friends who ever receive the ball are exactly the
        # positions congruent to 1 modulo gcd(n, k). Thus losers are the rest.
        g = __import__("math").gcd(n, k)
        step = g
        losers = [i for i in range(1, n + 1) if (i - 1) % step != 0]
        return losers
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
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Use modular arithmetic to simulate visited holders.
        # But we can do it efficiently by finding the cycle in positions.
        visited = set()
        order_seen = set()

        cur = 0  # 0-based index for friend 1
        step = k
        t = 1
        while cur not in visited:
            visited.add(cur)
            order_seen.add(cur)
            # Next position: add (t*k) steps from current (t starts at 1)
            cur = (cur + t * step) % n
            t += 1

        # Players who never received the ball are the losers.
        # Since the first repeat indicates we've looped over all "winners"
        # (the game stops at the second time someone receives the ball),
        # the repeated position is in visited already; thus winners are visited.
        losers = [i + 1 for i in range(n) if i not in visited]
        return losers
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List
import math

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Let step = k mod n. After t moves, position = 1 + sum_{i=1..t} (i*k)
        # = 1 + k * t(t+1)/2 (mod n). The ball repeats when this sequence cycles.
        # The set of friends who ever receive the ball has size equal to the
        # length of the cycle in this modular progression, which is n / gcd(n, k)
        # (equivalently, some standard derivation for this problem variant).
        step_gcd = math.gcd(n, k)
        m = n // step_gcd  # number of distinct receivers (including initial)
        
        # The receivers are every (k mod n)th friend starting from 1 in a cycle;
        # losers are the rest.
        # Since n <= 50, simplest: simulate using visited until repeat.
        visited = [False] * n
        pos = 0  # 0-based, start at friend 1
        t = 1
        while not visited[pos]:
            visited[pos] = True
            pos = (pos + t * k) % n
            t += 1
        
        # Losers are those who never received the ball
        return [i + 1 for i, v in enumerate(visited) if not v]
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Simulation is fine for n <= 50, but we can do it deterministically:
        # The ball holder sequence is periodic; we track visited holders.
        visited = [False] * (n + 1)  # 1..n
        pos = 1
        step = 1
        visited[pos] = True

        while True:
            # Move i*k steps clockwise each turn, where current turn is step (1-based).
            pos = (pos + (step * k)) % n
            if pos == 0:
                pos = n

            if visited[pos]:
                break
            visited[pos] = True
            step += 1

        # Losers are those who never received the ball
        return [i for i in range(1, n + 1) if not visited[i]]
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # simulate in terms of visited receivers
        visited = [False] * n
        cur = 0  # 0-based index for friend 1
        step = k % n

        # mark the starting friend as having received once
        visited[cur] = True

        # on turn i, move i*k steps; equivalently total movement after t turns:
        # cur = sum_{i=1..t} (i*k) mod n = t*(t+1)/2 * k mod n
        # We'll just simulate receivers until a repeat occurs.
        while True:
            # Next receiver index after i turns depends on i; easiest is iterative:
            # maintain increment multiplier using turn count.
            # We'll keep a running total of movement.
            break

        # Proper simulation with running total movement
        visited = [False] * n
        cur = 0
        visited[cur] = True
        total_move = 0
        i = 1  # turn count

        while True:
            total_move = (total_move + i * step) % n
            cur = total_move
            if visited[cur]:
                break
            visited[cur] = True
            i += 1

        losers = [idx + 1 for idx, ok in enumerate(visited) if not ok]
        return losers
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
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Each move from i to i + t*k (mod n), where t increases each turn.
        # The ball revisits a position when cumulative steps match modulo n.
        # This results in a cycle length equal to n / gcd(n, k).
        # Only friends in the cycle ever receive the ball; others are losers.
        import math

        g = math.gcd(n, k)
        winners = set()
        # Starting from friend 1, the set of receivers corresponds to:
        # positions after t steps: 1 + (t(t+1)/2)*k (mod n)
        # But winners are exactly those reachable before repetition, which count is n/g.
        # Those reachable correspond to indices 1, 1+g, 1+2g, ... in 1-based numbering.
        for i in range(n // g):
            winners.add(1 + i * g)

        losers = [i for i in range(1, n + 1) if i not in winners]
        return losers
```
```

</details>

<details>
<summary>partial attempt 2</summary>

```text
```python
from typing import List
import math

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The ball visits friends according to step sizes:
        # positions: 1, 1+k, 1+3k, 1+6k, ... (mod n)
        # This results in visiting exactly the subgroup generated by k (mod n).
        # Hence the game ends when a visited position repeats; losers are those
        # not in the visited set. Count of visited friends is n / gcd(n, k).
        g = math.gcd(n, k)
        m = n // g  # number of friends who receive the ball at least once

        # Visited friends are: 1, 1+g, 1+2g, ..., 1+(m-1)g (mod n)
        visited = set(((1 + i * g - 1) % n) + 1 for i in range(m))

        return [i for i in range(1, n + 1) if i not in visited]
```
```

</details>

<details>
<summary>partial attempt 3</summary>

```text
```python
from typing import List
from math import gcd

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        step = k
        # Let g be gcd(n, k). The ball visits exactly n/g distinct friends.
        g = gcd(n, step)
        visited = set()
        for i in range(n // g):
            # Position after i turns starting from friend 1:
            # 1 -> 1 + (1*k + 2*k + ... + i*k) = 1 + k * i*(i+1)/2
            pos = (1 + (step * i * (i + 1) // 2)) % n
            if pos == 0:
                pos = n
            visited.add(pos)

        losers = [i for i in range(1, n + 1) if i not in visited]
        return losers
```
```

</details>

<details>
<summary>partial attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # When holding the ball at step i (0-indexed), the position advances by (i+1)*k.
        # Mod n, the sequence is: pos_j = 1 + k * (1+2+...+j) = 1 + k * T_j  (mod n).
        # The game ends when a position repeats, i.e., when the sequence has a cycle.
        #
        # A known result for this problem: the set of losers are exactly those positions
        # not reachable from 1 under steps of size k in terms of gcd.
        # Equivalent characterization: winners form a single arithmetic progression
        # modulo n with step size k; the number of winners is n / gcd(n, k).
        #
        # Losers are all friends not in winners set, in ascending order.
        import math

        g = math.gcd(n, k)
        winners = set()
        step = k % n
        pos = 0  # 0-based, starting at friend 1
        for _ in range(n // g):
            winners.add(pos)
            pos = (pos + step) % n

        # losers are those indices (0-based) not in winners
        losers = [i + 1 for i in range(n) if i not in winners]
        return losers
```
```

</details>

<details>
<summary>partial attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The ball moves by i*k (mod n) at the i-th step.
        # Positions that ever receive the ball are exactly multiples of gcd(n, k) away from 0.
        # The game repeats when a position is reached twice; those are exactly the visited positions.
        d = __import__("math").gcd(n, k)
        losers = []
        # Convert to 1-based indexing:
        # visited positions are: 1, 1+d, 1+2d, ... (mod n). Others are losers.
        for person in range(1, n + 1):
            if (person - 1) % d != 0:
                losers.append(person)
        return losers
```
```

</details>

<details>
<summary>partial attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Starting at friend 1, on turn i we move i*k steps clockwise.
        # Total positions visited are: 1 + k * (1 + 2 + ... + t) = 1 + k*t*(t+1)/2 (mod n)
        # The game ends when a position repeats. The visited set corresponds to residues of
        # k * triangular numbers; equivalently the process cycles with step based on gcd.
        #
        # It can be shown that the set of friends who ever receive the ball are exactly the
        # positions congruent to 1 modulo gcd(n, k). Thus losers are the rest.
        g = __import__("math").gcd(n, k)
        step = g
        losers = [i for i in range(1, n + 1) if (i - 1) % step != 0]
        return losers
```
```

</details>

### Parsed Memory Items

1. Invariant-First Simulation for Repeat-Stopping Processes
Description: When the game ends at the first repeat of a state (e.g., ball holder), track visited states directly to guarantee correctness.
<details>
<summary>Content 1</summary>

```text
Reformulate the process as a deterministic state transition (current holder → next holder) and maintain a visited set/array. Terminate immediately upon encountering a previously visited holder, since the problem’s stopping condition is exactly that repeat.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
The successful attempts mostly used direct simulation with a “visited positions” invariant, correctly matching the rule that the stopping condition is a repeat (second time someone receives). They avoided relying on an unverified number-theory characterization for the winner set. In contrast, several partially-correct attempts jumped to a gcd/arithmetic-progression characterization without fully validating it against the actual “increasing step size by turn” dynamics (triangular-number/accumulated movement), leading to incorrect winner sets for some cases. The key distinction is whether the method maintains a correct invariant tied to the game’s stopping condition (repeat of holders) rather than an overgeneralized closed form.
```

</details>

2. Validate Any Closed-Form Claim Against the Actual Transition Rule
Description: If you derive winners/losers via gcd or group structure, explicitly verify the derivation against the true transition (including changing step sizes).
<details>
<summary>Content 2</summary>

```text
It’s easy to guess a gcd-based orbit for problems with constant step size, but here the step depends on the turn, so the closed form must incorporate accumulated movement (often leading to triangular-number effects modulo n). Before trusting a formula, test it by reasoning from the exact recurrence or running a small verification simulation.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
The successful attempts mostly used direct simulation with a “visited positions” invariant, correctly matching the rule that the stopping condition is a repeat (second time someone receives). They avoided relying on an unverified number-theory characterization for the winner set. In contrast, several partially-correct attempts jumped to a gcd/arithmetic-progression characterization without fully validating it against the actual “increasing step size by turn” dynamics (triangular-number/accumulated movement), leading to incorrect winner sets for some cases. The key distinction is whether the method maintains a correct invariant tied to the game’s stopping condition (repeat of holders) rather than an overgeneralized closed form.
```

</details>

3. Choose a Representation That Matches What You Need to Output
Description: Maintain the set of receivers/holders rather than indirectly reasoning about counts, so you can output losers in sorted order reliably.
<details>
<summary>Content 3</summary>

```text
Instead of inferring which participants are winners, record which indices are ever reached. This directly yields the losers as the complement and naturally supports returning the answer in ascending order.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
The successful attempts mostly used direct simulation with a “visited positions” invariant, correctly matching the rule that the stopping condition is a repeat (second time someone receives). They avoided relying on an unverified number-theory characterization for the winner set. In contrast, several partially-correct attempts jumped to a gcd/arithmetic-progression characterization without fully validating it against the actual “increasing step size by turn” dynamics (triangular-number/accumulated movement), leading to incorrect winner sets for some cases. The key distinction is whether the method maintains a correct invariant tied to the game’s stopping condition (repeat of holders) rather than an overgeneralized closed form.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
The successful attempts mostly used direct simulation with a “visited positions” invariant, correctly matching the rule that the stopping condition is a repeat (second time someone receives). They avoided relying on an unverified number-theory characterization for the winner set. In contrast, several partially-correct attempts jumped to a gcd/arithmetic-progression characterization without fully validating it against the actual “increasing step size by turn” dynamics (triangular-number/accumulated movement), leading to incorrect winner sets for some cases. The key distinction is whether the method maintains a correct invariant tied to the game’s stopping condition (repeat of holders) rather than an overgeneralized closed form.
</reasoning>

<memories>
  <memory>
    <title>Invariant-First Simulation for Repeat-Stopping Processes</title>
    <description>When the game ends at the first repeat of a state (e.g., ball holder), track visited states directly to guarantee correctness.</description>
    <content>Reformulate the process as a deterministic state transition (current holder → next holder) and maintain a visited set/array. Terminate immediately upon encountering a previously visited holder, since the problem’s stopping condition is exactly that repeat.</content>
  </memory>

  <memory>
    <title>Validate Any Closed-Form Claim Against the Actual Transition Rule</title>
    <description>If you derive winners/losers via gcd or group structure, explicitly verify the derivation against the true transition (including changing step sizes).</description>
    <content>It’s easy to guess a gcd-based orbit for problems with constant step size, but here the step depends on the turn, so the closed form must incorporate accumulated movement (often leading to triangular-number effects modulo n). Before trusting a formula, test it by reasoning from the exact recurrence or running a small verification simulation.</content>
  </memory>

  <memory>
    <title>Choose a Representation That Matches What You Need to Output</title>
    <description>Maintain the set of receivers/holders rather than indirectly reasoning about counts, so you can output losers in sorted order reliably.</description>
    <content>Instead of inferring which participants are winners, record which indices are ever reached. This directly yields the losers as the complement and naturally supports returning the answer in ascending order.</content>
  </memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `0.3000`
- Augmented pass@1: `1.0000`
- Improvement: `+0.7000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the i^th friend brings you to the (i+1)^th friend for 1 <= i < n, and moving clockwise from the n^th friend brings you to the 1^st friend.
The rules of the game are as follows:
1^st friend receives the ball.

After that, 1^st friend passes it to the friend who is k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 2 * k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 3 * k steps away from them in the clockwise direction, and so on and so forth.

In other words, on the i^th turn, the friend holding the ball should pass it to the friend who is i * k steps away from them in the clockwise direction.
The game is finished when some friend receives the ball for the second time.
The losers of the game are friends who did not receive the ball in the entire game.
Given the number of friends, n, and an integer k, return the array answer, which contains the losers of the game in the ascending order.
 
Example 1:

Input: n = 5, k = 2
Output: [4,5]
Explanation: The game goes as follows:
1) Start at 1^st friend and pass the ball to the friend who is 2 steps away from them - 3^rd friend.
2) 3^rd friend passes the ball to the friend who is 4 steps away from them - 2^nd friend.
3) 2^nd friend passes the ball to the friend who is 6 steps away from them  - 3^rd friend.
4) The game ends as 3^rd friend receives the ball for the second time.

Example 2:

Input: n = 4, k = 4
Output: [2,3,4]
Explanation: The game goes as follows:
1) Start at the 1^st friend and pass the ball to the friend who is 4 steps away from them - 1^st friend.
2) The game ends as 1^st friend receives the ball for the second time.

 
Constraints:

1 <= k <= n <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
from typing import List
import math

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # On turn i, the ball moves by i*k steps.
        # After t steps, total move is k*(1+2+...+t) = k*t*(t+1)/2.
        # Game ends when some friend receives the ball the second time.
        # The set of visited friends forms a cycle whose size is n / gcd(n, k).
        # Losers are the unvisited friends => count is n - cycle_size.
        g = math.gcd(n, k)
        step = n // g  # visited friends are 1, 1+step, 1+2*step, ...

        losers = []
        for friend in range(1, n + 1):
            # visited iff (friend - 1) is divisible by step
            if (friend - 1) % step != 0:
                losers.append(friend)
        return losers
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The sequence of ball holders advances by k, then 2k, ... modulo n.
        # Net position after i-th move (from start at 1) is:
        # 1 + k*(1 + 2 + ... + i) = 1 + k*i*(i+1)/2 (mod n).
        # The game ends when a friend repeats (i.e., sequence in mod n cycles).
        # It can be shown the set of visited friends has size n / gcd(n, k),
        # and the number of "losers" equals n - n/gcd(n, k).
        g = __import__("math").gcd(n, k)
        visited = n // g

        # The starting friend is 1 (index 0 internally). The visited friends are:
        # positions 0, step, 2*step, ... where step = g (in 0-based indexing)
        # because the move pattern ultimately hits exactly those residues.
        step = g
        is_winner = [False] * n
        for t in range(visited):
            is_winner[(t * step) % n] = True

        # Losers: those who never received the ball
        losers = [i + 1 for i in range(n) if not is_winner[i]]
        return losers
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # After each step i, position advances by i*k (mod n).
        # The sequence of positions returns to a previous player at the smallest i
        # such that i(i+1)/2 * k is 0 (mod n).
        # The number of distinct players visited equals n / gcd(n, k).
        # Losers are the unvisited players.
        g = 1
        # compute gcd(n, k) without importing math for simplicity
        a, b = n, k
        while b:
            a, b = b, a % b
        g = a  # gcd(n, k)
        visited_count = n // g

        # The starting player is 1. The visited players are multiples of g in the
        # modular step pattern; easiest: simulate indices visited by following
        # the actual rule until repeat.
        seen = set()
        pos = 1  # player labels are 1..n
        i = 1
        step = 1
        while pos not in seen:
            seen.add(pos)
            step = (step + k * i) % n  # but this would be cumulative; instead do simulation below
            i += 1
            # We'll redo simulation properly:
            break

        # Correct simulation of the game:
        seen = set()
        pos = 1
        i = 1
        while pos not in seen:
            seen.add(pos)
            pos = ((pos - 1 + i * k) % n) + 1
            i += 1

        losers = [p for p in range(1, n + 1) if p not in seen]
        return losers
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The ball moves from start to positions:
        # 1 -> 1+k -> 1+3k -> 1+6k -> ... (increments are 1*k, 2*k, 3*k, ...)
        # The sequence of positions modulo n repeats when a position is visited twice.
        # This happens when we reach a position whose index is congruent to 1 modulo
        # the group size defined by gcd(n, k).
        #
        # Known result: all winners are exactly the first "m" positions in the same cycle,
        # where m = n / gcd(n, k). Losers are the remaining numbers (1-indexed).
        g = __import__("math").gcd(n, k)
        cycle_len = n // g

        winners = set()
        for i in range(cycle_len):
            winners.add(1 + i * g)

        losers = [x for x in range(1, n + 1) if x not in winners]
        return losers
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The ball is passed with step sizes k, 2k, 3k, ...
        # This sequence of positions forms a cycle in terms of modulo n.
        # Winners are exactly the positions visited before repeating, which count is:
        # cycle_length = n / gcd(n, k)
        # All other friends are losers.
        
        import math
        g = math.gcd(n, k)
        cycle_len = n // g

        winners = set()
        pos = 0  # 0-based position of the ball holder (starts at friend 1)
        for _ in range(cycle_len):
            winners.add(pos)
            # next position: move (current_turn * k) steps, where turn starts at 1
            # If we are at turn t holder, next move is t*k, so position update:
            # pos = (pos + t*k) % n
            # Here iteration index i represents turn = i+1
            # Since this loop already runs cycle_len times, we update at end.
            # We'll compute increment using (i+1) each time by tracking via loop index.
            # To keep it simple, we re-implement with an index.
        
        winners.clear()
        pos = 0
        for t in range(1, cycle_len + 1):
            winners.add(pos)
            pos = (pos + t * k) % n

        losers = [i + 1 for i in range(n) if i not in winners]
        return losers
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # The ball's holder after t steps forms a sequence modulo n.
        # It repeats when t*k ≡ 0 (mod n), so the cycle length is n / gcd(n, k).
        # Losers are those not in that cycle.
        import math

        g = math.gcd(n, k)
        cycle_len = n // g

        # Positions visited starting from 1:
        # holder at step t is (1 + t*k) mod n, using 1-based friend numbers.
        visited = set()
        cur = 0  # 0-based index for friend 1
        visited.add(cur)
        for _ in range(1, cycle_len):
            cur = (cur + k) % n
            visited.add(cur)

        # Losers are 1-based indices not visited
        losers = [i + 1 for i in range(n) if i not in visited]
        return losers
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # After t moves, the ball is at position: t*(t+1)/2 * k (mod n) relative to friend 1.
        # The game ends when a position repeats. In this process, the set of visited
        # friends corresponds to multiples of gcd(n, k) (in a suitable step size graph).
        # The standard result: the losers are those not in the cycle reachable from 1,
        # which are all friends except {1 + i*(g) mod n}, where g = gcd(n, k).
        import math

        g = math.gcd(n, k)

        losers = []
        for friend in range(1, n + 1):
            # Winner set size is n/g; winners are congruent to 1 modulo g (1-indexed circle)
            if (friend - 1) % g != 0:
                losers.append(friend)
        return losers
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Positions visited by the ball starting from friend 1:
        # after t turns, friend index advances by (1+2+...+t)*k = t(t+1)/2 * k (mod n)
        # The game ends when a position repeats; all others are losers.
        visited = [False] * (n + 1)  # 1..n
        cur = 1
        step = k % n
        visited[cur] = True

        turn = 1
        while True:
            # Move i*k steps on i-th turn
            # current move uses multiplier = turn
            # cur = (cur + turn*k) mod n
            cur = ((cur - 1 + turn * step) % n) + 1
            if visited[cur]:
                break
            visited[cur] = True
            turn += 1

        losers = [i for i in range(1, n + 1) if not visited[i]]
        return losers
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Track which friends ever receive the ball.
        # The ball moves by i*k steps on the i-th pass:
        # receiver after t moves is 1 + k * (1 + 2 + ... + t) = 1 + k * t(t+1)/2 (mod n)
        # This induces a cycle whose set of reachable nodes has size n / gcd(n, k).
        # Those reachable are the winners; losers are the rest.
        g = __import__("math").gcd(n, k)
        winners = set()
        # Winners are exactly positions reachable by repeatedly adding k mod n
        # (equivalently those whose index i satisfies (i-1) * inv? but easier by simulation of cycle length n/g)
        # We can generate winners by starting at 1 and adding k each time:
        # In this game, the set of recipients equals {1 + m*k (mod n)} for m=0..n/g-1.
        cur = 0  # 0-based index for friend 1
        for _ in range(n // g):
            winners.add(cur)
            cur = (cur + k) % n

        losers = [i + 1 for i in range(n) if i not in winners]
        return losers
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = [False] * n          # visited[i] == has friend (i+1) received the ball?
        second_time = [False] * n      # optional: not needed, but keeps clarity

        pos = 0  # 0-based index for friend 1
        visited_count = 0
        step = 1
        while not second_time[pos]:
            if visited[pos]:
                second_time[pos] = True
                break
            visited[pos] = True
            visited_count += 1
            pos = (pos + step * k) % n
            step += 1

        losers = [i + 1 for i in range(n) if not visited[i]]
        return losers
```
```

</details>

#### Baseline Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.0714 | `partial` |
| 1 | 0.5714 | `partial` |
| 2 | 1.0000 | `full` |
| 3 | 0.5714 | `partial` |
| 4 | 0.9286 | `partial` |
| 5 | 0.5714 | `partial` |
| 6 | 0.5714 | `partial` |
| 7 | 1.0000 | `full` |
| 8 | 0.5714 | `partial` |
| 9 | 1.0000 | `full` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 1,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[2, 3, 4, 5]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[]",
      "actual": "[2, 3, 4]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[]",
      "actual": "[2]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[]",
      "actual": "[2, 3, 4]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[2, 3]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 5, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 13, 14, 15, 18, 19, 20, 23, 24, 25, 28, 30, 33, 34, 35, 38, 39, 40, 43, 44, 45, 48, 49, 50]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
  "passed": 8,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "[4, 5]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[3]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 4, 6]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[]",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49]",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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

  1. Invariant-First Simulation for Repeat-Stopping Processes: When the game ends at the first repeat of a state (e.g., ball holder), track visited states directly to guarantee correctness.
     Reformulate the process as a deterministic state transition (current holder → next holder) and maintain a visited set/array. Terminate immediately upon encountering a previously visited holder, since the problem’s stopping condition is exactly that repeat.
  2. Validate Any Closed-Form Claim Against the Actual Transition Rule: If you derive winners/losers via gcd or group structure, explicitly verify the derivation against the true transition (including changing step sizes).
     It’s easy to guess a gcd-based orbit for problems with constant step size, but here the step depends on the turn, so the closed form must incorporate accumulated movement (often leading to triangular-number effects modulo n). Before trusting a formula, test it by reasoning from the exact recurrence or running a small verification simulation.
  3. Choose a Representation That Matches What You Need to Output: Maintain the set of receivers/holders rather than indirectly reasoning about counts, so you can output losers in sorted order reliably.
     Instead of inferring which participants are winners, record which indices are ever reached. This directly yields the losers as the complement and naturally supports returning the answer in ascending order.

Apply these insights to the problem below.

### Question:
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the i^th friend brings you to the (i+1)^th friend for 1 <= i < n, and moving clockwise from the n^th friend brings you to the 1^st friend.
The rules of the game are as follows:
1^st friend receives the ball.

After that, 1^st friend passes it to the friend who is k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 2 * k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 3 * k steps away from them in the clockwise direction, and so on and so forth.

In other words, on the i^th turn, the friend holding the ball should pass it to the friend who is i * k steps away from them in the clockwise direction.
The game is finished when some friend receives the ball for the second time.
The losers of the game are friends who did not receive the ball in the entire game.
Given the number of friends, n, and an integer k, return the array answer, which contains the losers of the game in the ascending order.
 
Example 1:

Input: n = 5, k = 2
Output: [4,5]
Explanation: The game goes as follows:
1) Start at 1^st friend and pass the ball to the friend who is 2 steps away from them - 3^rd friend.
2) 3^rd friend passes the ball to the friend who is 4 steps away from them - 2^nd friend.
3) 2^nd friend passes the ball to the friend who is 6 steps away from them  - 3^rd friend.
4) The game ends as 3^rd friend receives the ball for the second time.

Example 2:

Input: n = 4, k = 4
Output: [2,3,4]
Explanation: The game goes as follows:
1) Start at the 1^st friend and pass the ball to the friend who is 4 steps away from them - 1^st friend.
2) The game ends as 1^st friend receives the ball for the second time.

 
Constraints:

1 <= k <= n <= 50

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        
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
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # holders/receivers are deterministic: current holder -> next holder
        # step size on i-th turn is i*k, so we can simulate by turn count.
        visited = [False] * n  # visited[friend_index]
        
        current = 0  # friend 1 in 0-based indexing
        turn = 1
        visited[current] = True
        
        while True:
            # pass i*k steps clockwise
            current = (current + (turn * k)) % n
            if visited[current]:  # second time received => stop
                break
            visited[current] = True
            turn += 1

        losers = [i + 1 for i, v in enumerate(visited) if not v]
        return losers
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Deterministic state transition: holder -> next holder
        # Stop when a holder repeats.
        visited = [False] * n  # visited[i] => friend (i+1) has received ball
        cur = 0  # friend 1 in 0-based
        step_mult = 1

        while not visited[cur]:
            visited[cur] = True
            cur = (cur + step_mult * k) % n
            step_mult += 1

        # Losers are those never visited.
        return [i + 1 for i in range(n) if not visited[i]]
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Deterministic transition: holder t passes to holder (t + i*k) mod n (0-indexed),
        # where i is the 1-based turn count after the start.
        # Stop when a holder repeats.
        seen = [False] * n

        cur = 0  # 0 represents friend 1
        seen[cur] = True

        step_mult = 1  # i in the statement
        i = 1
        while True:
            cur = (cur + i * k) % n
            if seen[cur]:
                break
            seen[cur] = True
            i += 1

        losers = [idx + 1 for idx in range(n) if not seen[idx]]
        return losers
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = [False] * n
        cur = 0  # 0-based index for friend 1
        visited[cur] = True

        step = 1
        while True:
            cur = (cur + step * k) % n
            if visited[cur]:
                break
            visited[cur] = True
            step += 1

        losers = [i + 1 for i in range(n) if not visited[i]]
        return losers
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # visited[i] indicates whether friend (i+1) has received the ball
        visited = [False] * n
        cur = 0  # 0-based index for friend 1
        step_mult = 1  # i * k where i starts at 1 on the first move

        while not visited[cur]:
            visited[cur] = True
            cur = (cur + step_mult * k) % n
            step_mult += 1

        # Losers are those never visited
        return [i + 1 for i in range(n) if not visited[i]]
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Track states by current holder (ball position). The game stops
        # at the first repeat of a holder.
        visited = [False] * (n + 1)  # 1..n
        order_seen = [0] * (n + 1)

        cur = 1
        visited[cur] = True
        step = 1

        while True:
            # move i*k steps clockwise where i is the current turn index (step)
            cur = (cur - 1 + (step * k) % n) % n + 1
            if visited[cur]:
                break
            visited[cur] = True
            step += 1

        losers = [i for i in range(1, n + 1) if not visited[i]]
        return losers
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Deterministic state transition: holder -> next holder.
        # Stop exactly when a holder is seen for the 2nd time.
        visited = [False] * n
        holder = 0  # 1st friend (0-indexed)
        turn = 1

        while not visited[holder]:
            visited[holder] = True
            # On turn t, pass i*k steps; here i == turn.
            holder = (holder + (turn * k) % n) % n
            turn += 1

        # Losers are those never visited.
        return [i + 1 for i in range(n) if not visited[i]]
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = [False] * n  # visited[i] => friend (i+1) has received the ball
        cur = 0  # 0-based index for friend 1
        visited[cur] = True

        step_mul = 1
        while True:
            nxt = (cur + step_mul * k) % n
            if visited[nxt]:  # game ends when someone receives the ball second time
                break
            visited[nxt] = True
            cur = nxt
            step_mul += 1

        losers = [i + 1 for i in range(n) if not visited[i]]
        return losers
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Deterministic transition: on i-th move (1-indexed), holder x passes to
        # x + i*k (clockwise), modulo n.
        #
        # Game stops when a holder repeats (i.e., receives the ball for the 2nd time).
        visited = [False] * n  # visited[i] means friend (i+1) has received the ball
        cur = 0  # friend 1 (0-based)
        visited[cur] = True

        step_mul = 1
        while True:
            cur = (cur + step_mul * k) % n
            if visited[cur]:
                break
            visited[cur] = True
            step_mul += 1

        losers = [i + 1 for i in range(n) if not visited[i]]
        return losers
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Deterministic simulation: state is "current holder".
        # Stop exactly when a holder repeats.
        visited = [False] * (n + 1)  # 1..n
        order = []  # holders in the order we visit (optional, but clarifies intent)

        cur = 1
        step_mult = 1

        while not visited[cur]:
            visited[cur] = True
            order.append(cur)

            # next holder after i-th turn: move i*k steps clockwise
            # Using 0-based arithmetic then back to 1-based.
            cur0 = cur - 1
            nxt0 = (cur0 + (step_mult * k)) % n
            cur = nxt0 + 1
            step_mult += 1

        # losers are those never visited
        losers = [i for i in range(1, n + 1) if not visited[i]]
        return losers
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
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
      "expected": "[4, 5]",
      "actual": "[4, 5]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4]",
      "actual": "[2, 3, 4]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3]",
      "actual": "[3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3]",
      "actual": "[2, 3]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 6]",
      "actual": "[2, 3, 4, 6]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "actual": "[2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "actual": "[3, 5, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "actual": "[2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "actual": "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]",
      "error": ""
    }
  ]
}
```

</details>
