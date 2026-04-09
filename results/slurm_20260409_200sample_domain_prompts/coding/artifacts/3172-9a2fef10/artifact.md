# Problem 3172

- Domain: `coding`

## Problem

```text
You are given positive integers n and m.
Define two integers, num1 and num2, as follows:

num1: The sum of all integers in the range [1, n] that are not divisible by m.
num2: The sum of all integers in the range [1, n] that are divisible by m.

Return the integer num1 - num2.
 
Example 1:

Input: n = 10, m = 3
Output: 19
Explanation: In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.

Example 2:

Input: n = 5, m = 6
Output: 15
Explanation: In the given example:
- Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], num1 is the sum of those integers = 15.
- Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.
We return 15 - 0 = 15 as the answer.

Example 3:

Input: n = 5, m = 1
Output: -15
Explanation: In the given example:
- Integers in the range [1, 5] that are not divisible by 1 are [], num1 is the sum of those integers = 0.
- Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], num2 is the sum of those integers = 15.
We return 0 - 15 = -15 as the answer.

 
Constraints:

1 <= n, m <= 1000
```

### Starter Code

```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
```

### Test Cases

```json
[
  {
    "input": "10\n3",
    "output": "19",
    "testtype": "functional"
  },
  {
    "input": "5\n6",
    "output": "15",
    "testtype": "functional"
  },
  {
    "input": "5\n1",
    "output": "-15",
    "testtype": "functional"
  },
  {
    "input": "1\n8",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "1\n2",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "5\n2",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "6\n5",
    "output": "11",
    "testtype": "functional"
  },
  {
    "input": "5\n7",
    "output": "15",
    "testtype": "functional"
  },
  {
    "input": "9\n6",
    "output": "33",
    "testtype": "functional"
  },
  {
    "input": "8\n10",
    "output": "36",
    "testtype": "functional"
  },
  {
    "input": "7\n10",
    "output": "28",
    "testtype": "functional"
  },
  {
    "input": "10\n1",
    "output": "-55",
    "testtype": "functional"
  },
  {
    "input": "55\n6",
    "output": "1000",
    "testtype": "functional"
  },
  {
    "input": "921\n387",
    "output": "422259",
    "testtype": "functional"
  },
  {
    "input": "1000\n1000",
    "output": "498500",
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
You are given positive integers n and m.
Define two integers, num1 and num2, as follows:

num1: The sum of all integers in the range [1, n] that are not divisible by m.
num2: The sum of all integers in the range [1, n] that are divisible by m.

Return the integer num1 - num2.
 
Example 1:

Input: n = 10, m = 3
Output: 19
Explanation: In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.

Example 2:

Input: n = 5, m = 6
Output: 15
Explanation: In the given example:
- Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], num1 is the sum of those integers = 15.
- Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.
We return 15 - 0 = 15 as the answer.

Example 3:

Input: n = 5, m = 1
Output: -15
Explanation: In the given example:
- Integers in the range [1, 5] that are not divisible by 1 are [], num1 is the sum of those integers = 0.
- Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], num2 is the sum of those integers = 15.
We return 0 - 15 = -15 as the answer.

 
Constraints:

1 <= n, m <= 1000

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        if m == 0:
            return 0  # not needed given constraints
        k = n // m  # count of multiples of m in [1..n]

        # sum of all numbers in [1..n]
        total = n * (n + 1) // 2

        # sum of multiples of m: m * (1 + 2 + ... + k)
        sum_mult = m * k * (k + 1) // 2

        # numbers not divisible by m: total - sum_mult
        num1 = total - sum_mult
        num2 = sum_mult

        return num1 - num2
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all integers from 1..n
        total = n * (n + 1) // 2
        
        # If m divides x, then x = m*k for k = 1..n//m
        k = n // m
        divisible_sum = m * k * (k + 1) // 2  # m * sum_{i=1..k} i
        
        # num1 - num2 = (total - divisible_sum) - divisible_sum
        return total - 2 * divisible_sum
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of 1..n
        total = n * (n + 1) // 2

        # Sum of multiples of m up to n: m + 2m + ... + km where k = n//m
        k = n // m
        mult_sum = m * k * (k + 1) // 2

        # num1 - num2 = (total - mult_sum) - mult_sum = total - 2*mult_sum
        return total - 2 * mult_sum
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all numbers from 1 to n
        total = n * (n + 1) // 2
        
        # If m == 1, then all numbers are divisible by m
        if m == 1:
            return 0 - total
        
        # Sum of numbers divisible by m: m + 2m + ... + km where km <= n
        k = n // m
        sum_divisible = m * k * (k + 1) // 2
        
        # num1 - num2 = (total - sum_divisible) - sum_divisible
        return total - 2 * sum_divisible
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2  # sum of 1..n
        if m == 0:  # not needed due to constraints, but safe
            return total_sum

        k = n // m  # count of multiples of m
        multiples_sum = m * k * (k + 1) // 2  # m*(1+2+...+k)
        # num1 - num2 = (total_sum - multiples_sum) - multiples_sum
        return total_sum - 2 * multiples_sum
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        if m == 0:
            return total
        k = n // m  # count of multiples of m
        sum_multiples = m * k * (k + 1) // 2
        # num1 - num2 where num1 = total - sum_multiples, num2 = sum_multiples
        return total - 2 * sum_multiples
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        if m == 1:
            # all numbers are divisible by m
            return 0 - sum(range(1, n + 1))

        # Sum of numbers not divisible by m = total sum - sum divisible by m
        total = n * (n + 1) // 2
        k = n // m  # count of divisible numbers
        divisible_sum = m * k * (k + 1) // 2  # m*(1+2+...+k)

        # num1 - num2 = (total - divisible_sum) - divisible_sum = total - 2*divisible_sum
        return total - 2 * divisible_sum
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        if m == 0:  # not needed due to constraints, but keeps it robust
            return 0

        k = n // m  # count of multiples of m
        sum_multiples = m * k * (k + 1) // 2
        # num1 - num2 = (total - sum_multiples) - sum_multiples
        return total - 2 * sum_multiples
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of 1..n
        total = n * (n + 1) // 2
        
        # Sum of multiples of m up to n
        k = n // m
        sum_multiples = m * k * (k + 1) // 2
        
        # num1 - num2 = (total - sum_multiples) - sum_multiples
        return total - 2 * sum_multiples
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of 1..n minus twice the sum of numbers divisible by m
        total = n * (n + 1) // 2
        k = n // m  # count of multiples of m
        mult_sum = m * k * (k + 1) // 2  # m * (1+2+...+k)
        return total - 2 * mult_sum
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
    def differenceOfSums(self, n: int, m: int) -> int:
        if m == 0:
            return 0  # not needed given constraints
        k = n // m  # count of multiples of m in [1..n]

        # sum of all numbers in [1..n]
        total = n * (n + 1) // 2

        # sum of multiples of m: m * (1 + 2 + ... + k)
        sum_mult = m * k * (k + 1) // 2

        # numbers not divisible by m: total - sum_mult
        num1 = total - sum_mult
        num2 = sum_mult

        return num1 - num2
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all integers from 1..n
        total = n * (n + 1) // 2
        
        # If m divides x, then x = m*k for k = 1..n//m
        k = n // m
        divisible_sum = m * k * (k + 1) // 2  # m * sum_{i=1..k} i
        
        # num1 - num2 = (total - divisible_sum) - divisible_sum
        return total - 2 * divisible_sum
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of 1..n
        total = n * (n + 1) // 2

        # Sum of multiples of m up to n: m + 2m + ... + km where k = n//m
        k = n // m
        mult_sum = m * k * (k + 1) // 2

        # num1 - num2 = (total - mult_sum) - mult_sum = total - 2*mult_sum
        return total - 2 * mult_sum
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all numbers from 1 to n
        total = n * (n + 1) // 2
        
        # If m == 1, then all numbers are divisible by m
        if m == 1:
            return 0 - total
        
        # Sum of numbers divisible by m: m + 2m + ... + km where km <= n
        k = n // m
        sum_divisible = m * k * (k + 1) // 2
        
        # num1 - num2 = (total - sum_divisible) - sum_divisible
        return total - 2 * sum_divisible
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2  # sum of 1..n
        if m == 0:  # not needed due to constraints, but safe
            return total_sum

        k = n // m  # count of multiples of m
        multiples_sum = m * k * (k + 1) // 2  # m*(1+2+...+k)
        # num1 - num2 = (total_sum - multiples_sum) - multiples_sum
        return total_sum - 2 * multiples_sum
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        if m == 0:
            return total
        k = n // m  # count of multiples of m
        sum_multiples = m * k * (k + 1) // 2
        # num1 - num2 where num1 = total - sum_multiples, num2 = sum_multiples
        return total - 2 * sum_multiples
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        if m == 1:
            # all numbers are divisible by m
            return 0 - sum(range(1, n + 1))

        # Sum of numbers not divisible by m = total sum - sum divisible by m
        total = n * (n + 1) // 2
        k = n // m  # count of divisible numbers
        divisible_sum = m * k * (k + 1) // 2  # m*(1+2+...+k)

        # num1 - num2 = (total - divisible_sum) - divisible_sum = total - 2*divisible_sum
        return total - 2 * divisible_sum
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        if m == 0:  # not needed due to constraints, but keeps it robust
            return 0

        k = n // m  # count of multiples of m
        sum_multiples = m * k * (k + 1) // 2
        # num1 - num2 = (total - sum_multiples) - sum_multiples
        return total - 2 * sum_multiples
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of 1..n
        total = n * (n + 1) // 2
        
        # Sum of multiples of m up to n
        k = n // m
        sum_multiples = m * k * (k + 1) // 2
        
        # num1 - num2 = (total - sum_multiples) - sum_multiples
        return total - 2 * sum_multiples
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of 1..n minus twice the sum of numbers divisible by m
        total = n * (n + 1) // 2
        k = n // m  # count of multiples of m
        mult_sum = m * k * (k + 1) // 2  # m * (1+2+...+k)
        return total - 2 * mult_sum
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
You are given positive integers n and m.
Define two integers, num1 and num2, as follows:

num1: The sum of all integers in the range [1, n] that are not divisible by m.
num2: The sum of all integers in the range [1, n] that are divisible by m.

Return the integer num1 - num2.
 
Example 1:

Input: n = 10, m = 3
Output: 19
Explanation: In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.

Example 2:

Input: n = 5, m = 6
Output: 15
Explanation: In the given example:
- Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], num1 is the sum of those integers = 15.
- Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.
We return 15 - 0 = 15 as the answer.

Example 3:

Input: n = 5, m = 1
Output: -15
Explanation: In the given example:
- Integers in the range [1, 5] that are not divisible by 1 are [], num1 is the sum of those integers = 0.
- Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], num2 is the sum of those integers = 15.
We return 0 - 15 = -15 as the answer.

 
Constraints:

1 <= n, m <= 1000

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # If m == 1, all numbers are divisible by m, so num1=0, num2 = sum 1..n
        # General approach below also works fine.
        sum_div = 0
        # Sum of multiples of m in [1, n]
        for x in range(m, n + 1, m):
            sum_div += x

        # Total sum of 1..n
        total = n * (n + 1) // 2
        # num1 - num2 = (total - sum_div) - sum_div = total - 2*sum_div
        return total - 2 * sum_div
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2  # sum of 1..n
        if m == 0:  # not needed per constraints, but safe
            return 0
        k = n // m  # count of multiples of m
        sum_multiples = m * k * (k + 1) // 2  # m*(1+2+...+k)
        return (total - sum_multiples) - sum_multiples
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of numbers divisible by m
        k = n // m
        sum_div = m * (k * (k + 1) // 2)
        
        # Total sum minus sum of divisible by m gives sum not divisible
        total = n * (n + 1) // 2
        return (total - sum_div) - sum_div
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        if m == 0:  # not needed per constraints, but safe
            return total

        # sum of multiples of m: m + 2m + ... + km where k = n//m
        k = n // m
        sum_multiples = m * k * (k + 1) // 2

        num1 = total - sum_multiples
        num2 = sum_multiples
        return num1 - num2
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all numbers 1..n
        total = n * (n + 1) // 2
        
        # Sum of numbers divisible by m: m * (1 + 2 + ... + k), where k = floor(n/m)
        k = n // m
        sum_divisible = m * k * (k + 1) // 2
        
        # num1 - num2 = (total - sum_divisible) - sum_divisible
        return total - 2 * sum_divisible
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all numbers from 1 to n
        total = n * (n + 1) // 2

        # Sum of numbers divisible by m: m + 2m + ... + km where k = n//m
        k = n // m
        sum_divisible = m * k * (k + 1) // 2

        # num1 - num2 = (total - sum_divisible) - sum_divisible
        return total - 2 * sum_divisible
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        k = n // m  # how many numbers in [1..n] are divisible by m
        div_sum = m * k * (k + 1) // 2  # m*(1+2+...+k)
        return total_sum - 2 * div_sum
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        if m == 0:  # not needed given constraints, but safe
            return 0
        k = n // m
        sum_divisible = m * k * (k + 1) // 2  # m * (1 + 2 + ... + k)
        return (total - sum_divisible) - sum_divisible
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_div = 0
        k = m
        while k <= n:
            sum_div += k
            k += m
        
        total = n * (n + 1) // 2
        sum_not_div = total - sum_div
        return sum_not_div - sum_div
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Total sum from 1 to n
        total = n * (n + 1) // 2
        
        # Sum of multiples of m: m * (1 + 2 + ... + k), where k = n // m
        k = n // m
        mult_sum = m * (k * (k + 1) // 2)
        
        # num1 - num2 = (total - mult_sum) - mult_sum = total - 2 * mult_sum
        return total - 2 * mult_sum
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
    def differenceOfSums(self, n: int, m: int) -> int:
        # If m == 1, all numbers are divisible by m, so num1=0, num2 = sum 1..n
        # General approach below also works fine.
        sum_div = 0
        # Sum of multiples of m in [1, n]
        for x in range(m, n + 1, m):
            sum_div += x

        # Total sum of 1..n
        total = n * (n + 1) // 2
        # num1 - num2 = (total - sum_div) - sum_div = total - 2*sum_div
        return total - 2 * sum_div
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2  # sum of 1..n
        if m == 0:  # not needed per constraints, but safe
            return 0
        k = n // m  # count of multiples of m
        sum_multiples = m * k * (k + 1) // 2  # m*(1+2+...+k)
        return (total - sum_multiples) - sum_multiples
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of numbers divisible by m
        k = n // m
        sum_div = m * (k * (k + 1) // 2)
        
        # Total sum minus sum of divisible by m gives sum not divisible
        total = n * (n + 1) // 2
        return (total - sum_div) - sum_div
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        if m == 0:  # not needed per constraints, but safe
            return total

        # sum of multiples of m: m + 2m + ... + km where k = n//m
        k = n // m
        sum_multiples = m * k * (k + 1) // 2

        num1 = total - sum_multiples
        num2 = sum_multiples
        return num1 - num2
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all numbers 1..n
        total = n * (n + 1) // 2
        
        # Sum of numbers divisible by m: m * (1 + 2 + ... + k), where k = floor(n/m)
        k = n // m
        sum_divisible = m * k * (k + 1) // 2
        
        # num1 - num2 = (total - sum_divisible) - sum_divisible
        return total - 2 * sum_divisible
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all numbers from 1 to n
        total = n * (n + 1) // 2

        # Sum of numbers divisible by m: m + 2m + ... + km where k = n//m
        k = n // m
        sum_divisible = m * k * (k + 1) // 2

        # num1 - num2 = (total - sum_divisible) - sum_divisible
        return total - 2 * sum_divisible
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        k = n // m  # how many numbers in [1..n] are divisible by m
        div_sum = m * k * (k + 1) // 2  # m*(1+2+...+k)
        return total_sum - 2 * div_sum
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        if m == 0:  # not needed given constraints, but safe
            return 0
        k = n // m
        sum_divisible = m * k * (k + 1) // 2  # m * (1 + 2 + ... + k)
        return (total - sum_divisible) - sum_divisible
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_div = 0
        k = m
        while k <= n:
            sum_div += k
            k += m
        
        total = n * (n + 1) // 2
        sum_not_div = total - sum_div
        return sum_not_div - sum_div
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Total sum from 1 to n
        total = n * (n + 1) // 2
        
        # Sum of multiples of m: m * (1 + 2 + ... + k), where k = n // m
        k = n // m
        mult_sum = m * (k * (k + 1) // 2)
        
        # num1 - num2 = (total - mult_sum) - mult_sum = total - 2 * mult_sum
        return total - 2 * mult_sum
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
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
      "expected": "19",
      "actual": "19",
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
      "expected": "-15",
      "actual": "-15",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "11",
      "actual": "11",
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
      "expected": "33",
      "actual": "33",
      "error": ""
    },
    {
      "passed": true,
      "expected": "36",
      "actual": "36",
      "error": ""
    },
    {
      "passed": true,
      "expected": "28",
      "actual": "28",
      "error": ""
    },
    {
      "passed": true,
      "expected": "-55",
      "actual": "-55",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1000",
      "actual": "1000",
      "error": ""
    },
    {
      "passed": true,
      "expected": "422259",
      "actual": "422259",
      "error": ""
    },
    {
      "passed": true,
      "expected": "498500",
      "actual": "498500",
      "error": ""
    }
  ]
}
```

</details>
