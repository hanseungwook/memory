# Problem abc302_a

- Domain: `coding`

## Problem

```text
There is an enemy with stamina A.  Every time you attack the enemy, its stamina reduces by B.
At least how many times do you need to attack the enemy to make its stamina 0 or less?

Input

The input is given from Standard Input in the following format:
A B

Output

Print the answer.

Constraints


- 1 \le A,B \le 10^{18}
- A and B are integers.

Sample Input 1

7 3

Sample Output 1

3

Attacking three times make the enemy's stamina -2.
Attacking only twice makes the stamina 1, so you need to attack it three times.

Sample Input 2

123456789123456789 987654321

Sample Output 2

124999999

Sample Input 3

999999999999999998 2

Sample Output 3

499999999999999999
```

### Test Cases

```json
[
  {
    "input": "7 3\n",
    "output": "3\n",
    "testtype": "stdin"
  },
  {
    "input": "123456789123456789 987654321\n",
    "output": "124999999\n",
    "testtype": "stdin"
  },
  {
    "input": "999999999999999998 2\n",
    "output": "499999999999999999\n",
    "testtype": "stdin"
  },
  {
    "input": "7270 116\n",
    "output": "63\n",
    "testtype": "stdin"
  },
  {
    "input": "59977464294637 1862647\n",
    "output": "32200124\n",
    "testtype": "stdin"
  },
  {
    "input": "11533765830482604 817419533590\n",
    "output": "14110\n",
    "testtype": "stdin"
  },
  {
    "input": "103838087894477201 4\n",
    "output": "25959521973619301\n",
    "testtype": "stdin"
  },
  {
    "input": "324013942553097064 767290441\n",
    "output": "422283304\n",
    "testtype": "stdin"
  },
  {
    "input": "159058673781516990 835315590\n",
    "output": "190417461\n",
    "testtype": "stdin"
  },
  {
    "input": "238734688664061268 297816499\n",
    "output": "801616732\n",
    "testtype": "stdin"
  },
  {
    "input": "406777939015149177 2\n",
    "output": "203388969507574589\n",
    "testtype": "stdin"
  },
  {
    "input": "623064468778408115 5\n",
    "output": "124612893755681623\n",
    "testtype": "stdin"
  },
  {
    "input": "802035354240686040 925744958032207328\n",
    "output": "1\n",
    "testtype": "stdin"
  },
  {
    "input": "390896634924972442 366843596946451619\n",
    "output": "2\n",
    "testtype": "stdin"
  },
  {
    "input": "883473210852275310 58937130685266794\n",
    "output": "15\n",
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
There is an enemy with stamina A.  Every time you attack the enemy, its stamina reduces by B.
At least how many times do you need to attack the enemy to make its stamina 0 or less?

Input

The input is given from Standard Input in the following format:
A B

Output

Print the answer.

Constraints


- 1 \le A,B \le 10^{18}
- A and B are integers.

Sample Input 1

7 3

Sample Output 1

3

Attacking three times make the enemy's stamina -2.
Attacking only twice makes the stamina 1, so you need to attack it three times.

Sample Input 2

123456789123456789 987654321

Sample Output 2

124999999

Sample Input 3

999999999999999998 2

Sample Output 3

499999999999999999

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Minimum x such that A - x*B <= 0  => x >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    ans = (A + B - 1) // B  # ceiling of A/B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n >= A/B
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n*B >= A
    n = (A + B - 1) // B
    print(n)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  -> n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    ans = (A + B - 1) // B  # ceil(A / B)
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Minimum n such that A - n*B <= 0  =>  n >= A/B
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Minimum x such that A - x*B <= 0  => x >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    ans = (A + B - 1) // B  # ceiling of A/B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n >= A/B
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n*B >= A
    n = (A + B - 1) // B
    print(n)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  -> n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    ans = (A + B - 1) // B  # ceil(A / B)
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Minimum n such that A - n*B <= 0  =>  n >= A/B
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
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
There is an enemy with stamina A.  Every time you attack the enemy, its stamina reduces by B.
At least how many times do you need to attack the enemy to make its stamina 0 or less?

Input

The input is given from Standard Input in the following format:
A B

Output

Print the answer.

Constraints


- 1 \le A,B \le 10^{18}
- A and B are integers.

Sample Input 1

7 3

Sample Output 1

3

Attacking three times make the enemy's stamina -2.
Attacking only twice makes the stamina 1, so you need to attack it three times.

Sample Input 2

123456789123456789 987654321

Sample Output 2

124999999

Sample Input 3

999999999999999998 2

Sample Output 3

499999999999999999

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
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n*B >= A  => n = ceil(A/B)
    ans = (A + B - 1) // B
    print(ans)

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
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n*B >= A
    # n = ceil(A / B)
    n = (A + B - 1) // B
    print(n)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  <=>  n >= A/B
    ans = (A + B - 1) // B  # ceil(A/B)
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n >= A/B
    # So n = ceil(A/B)
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need the smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  <=>  n*B >= A
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n*B >= A  =>  n = ceil(A/B)
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # minimal n such that A - n*B <= 0  <=>  n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n*B >= A  => n = ceil(A/B)
    ans = (A + B - 1) // B
    print(ans)

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
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n*B >= A
    # n = ceil(A / B)
    n = (A + B - 1) // B
    print(n)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  <=>  n >= A/B
    ans = (A + B - 1) // B  # ceil(A/B)
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n >= A/B
    # So n = ceil(A/B)
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need the smallest n such that A - n*B <= 0  => n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
import sys

def solve():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  <=>  n*B >= A
    ans = (A + B - 1) // B
    print(ans)

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

def main():
    A, B = map(int, sys.stdin.readline().split())
    # Need smallest n such that A - n*B <= 0  =>  n*B >= A  =>  n = ceil(A/B)
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    # minimal n such that A - n*B <= 0  <=>  n >= A/B
    ans = (A + B - 1) // B
    print(ans)

if __name__ == "__main__":
    main()
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124999999",
      "actual": "124999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "499999999999999999",
      "actual": "499999999999999999",
      "error": ""
    },
    {
      "passed": true,
      "expected": "63",
      "actual": "63",
      "error": ""
    },
    {
      "passed": true,
      "expected": "32200124",
      "actual": "32200124",
      "error": ""
    },
    {
      "passed": true,
      "expected": "14110",
      "actual": "14110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "25959521973619301",
      "actual": "25959521973619301",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422283304",
      "actual": "422283304",
      "error": ""
    },
    {
      "passed": true,
      "expected": "190417461",
      "actual": "190417461",
      "error": ""
    },
    {
      "passed": true,
      "expected": "801616732",
      "actual": "801616732",
      "error": ""
    },
    {
      "passed": true,
      "expected": "203388969507574589",
      "actual": "203388969507574589",
      "error": ""
    },
    {
      "passed": true,
      "expected": "124612893755681623",
      "actual": "124612893755681623",
      "error": ""
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
    }
  ]
}
```

</details>
