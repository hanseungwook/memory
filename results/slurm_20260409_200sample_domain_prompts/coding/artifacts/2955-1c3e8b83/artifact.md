# Problem 2955

- Domain: `coding`

## Problem

```text
Initially, you have a bank account balance of 100 dollars.
You are given an integer purchaseAmount representing the amount you will spend on a purchase in dollars.
At the store where you will make the purchase, the purchase amount is rounded to the nearest multiple of 10. In other words, you pay a non-negative amount, roundedAmount, such that roundedAmount is a multiple of 10 and abs(roundedAmount - purchaseAmount) is minimized.
If there is more than one nearest multiple of 10, the largest multiple is chosen.
Return an integer denoting your account balance after making a purchase worth purchaseAmount dollars from the store.
Note: 0 is considered to be a multiple of 10 in this problem.
 
Example 1:

Input: purchaseAmount = 9
Output: 90
Explanation: In this example, the nearest multiple of 10 to 9 is 10. Hence, your account balance becomes 100 - 10 = 90.

Example 2:

Input: purchaseAmount = 15
Output: 80
Explanation: In this example, there are two nearest multiples of 10 to 15: 10 and 20. So, the larger multiple, 20, is chosen.
Hence, your account balance becomes 100 - 20 = 80.

 
Constraints:

0 <= purchaseAmount <= 100
```

### Starter Code

```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
```

### Test Cases

```json
[
  {
    "input": "9",
    "output": "90",
    "testtype": "functional"
  },
  {
    "input": "15",
    "output": "80",
    "testtype": "functional"
  },
  {
    "input": "7",
    "output": "90",
    "testtype": "functional"
  },
  {
    "input": "8",
    "output": "90",
    "testtype": "functional"
  },
  {
    "input": "9",
    "output": "90",
    "testtype": "functional"
  },
  {
    "input": "6",
    "output": "90",
    "testtype": "functional"
  },
  {
    "input": "99",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "98",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "95",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "1",
    "output": "100",
    "testtype": "functional"
  },
  {
    "input": "4",
    "output": "100",
    "testtype": "functional"
  },
  {
    "input": "30",
    "output": "70",
    "testtype": "functional"
  },
  {
    "input": "88",
    "output": "10",
    "testtype": "functional"
  },
  {
    "input": "64",
    "output": "40",
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
Initially, you have a bank account balance of 100 dollars.
You are given an integer purchaseAmount representing the amount you will spend on a purchase in dollars.
At the store where you will make the purchase, the purchase amount is rounded to the nearest multiple of 10. In other words, you pay a non-negative amount, roundedAmount, such that roundedAmount is a multiple of 10 and abs(roundedAmount - purchaseAmount) is minimized.
If there is more than one nearest multiple of 10, the largest multiple is chosen.
Return an integer denoting your account balance after making a purchase worth purchaseAmount dollars from the store.
Note: 0 is considered to be a multiple of 10 in this problem.
 
Example 1:

Input: purchaseAmount = 9
Output: 90
Explanation: In this example, the nearest multiple of 10 to 9 is 10. Hence, your account balance becomes 100 - 10 = 90.

Example 2:

Input: purchaseAmount = 15
Output: 80
Explanation: In this example, there are two nearest multiples of 10 to 15: 10 and 20. So, the larger multiple, 20, is chosen.
Hence, your account balance becomes 100 - 20 = 80.

 
Constraints:

0 <= purchaseAmount <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10  # nearest multiple of 10, ties go up
        return 100 - rounded
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Determine the nearest multiple of 10 (ties go to the larger multiple).
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # nearest multiples of 10 are k*10 where k is integer
        # handle tie by choosing the larger multiple
        if purchaseAmount % 10 == 0:
            rounded = purchaseAmount
        else:
            lower = (purchaseAmount // 10) * 10
            upper = lower + 10
            # distances: tie goes to upper (larger multiple)
            if purchaseAmount - lower <= upper - purchaseAmount:
                rounded = upper
            else:
                rounded = lower
        return 100 - rounded
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10  # usual nearest rounding
        # Tie case: when remainder is exactly 5, choose the larger multiple.
        # The formula above already chooses larger because of +5.
        return 100 - rounded
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Candidates are nearest multiples of 10: floor and ceil relative to purchaseAmount
        lower = (purchaseAmount // 10) * 10
        upper = lower if purchaseAmount % 10 == 0 else lower + 10

        # Choose the multiple with minimum distance; if tie, choose the larger
        if abs(upper - purchaseAmount) < abs(lower - purchaseAmount):
            rounded = upper
        elif abs(upper - purchaseAmount) > abs(lower - purchaseAmount):
            rounded = lower
        else:
            rounded = max(lower, upper)

        return 100 - rounded
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # nearest multiple of 10; if tie, choose the larger multiple
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10; if tie, choose the larger one.
        rounded = ((purchaseAmount + 5) // 10) * 10
        if rounded > purchaseAmount + 5:
            # Not needed for integer math with (x+5)//10, but kept safe.
            rounded = (purchaseAmount // 10) * 10
        # Special handling for exact midpoints like 15 (between 10 and 20):
        # For purchaseAmount % 10 == 5, formula above already picks the larger.
        return 100 - rounded
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10; if tie, choose the larger one
        remainder = purchaseAmount % 10
        rounded = purchaseAmount - remainder
        if remainder > 5:
            rounded += 10
        elif remainder == 5:
            rounded += 10  # tie: choose larger multiple
        # remainder < 5 => keep rounded as lower multiple

        return 100 - rounded
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        roundedAmount = (purchaseAmount // 10) * 10
        remainder = purchaseAmount % 10

        if remainder < 5:
            roundedAmount = (purchaseAmount // 10) * 10
        elif remainder > 5:
            roundedAmount = (purchaseAmount // 10 + 1) * 10
        else:
            # remainder == 5: tie between current multiple and next multiple; choose larger
            roundedAmount = (purchaseAmount // 10 + 1) * 10

        return 100 - roundedAmount
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 1.0000 | `full` |
| 1 | 1.0000 | `full` |
| 2 | 1.0000 | `full` |
| 3 | 0.2143 | `partial` |
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
  "passed": 3,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "90",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": false,
      "expected": "90",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "90",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "90",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "90",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "10",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "10",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "100",
      "actual": "90",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "100",
      "actual": "90",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": false,
      "expected": "10",
      "actual": "20",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "30",
      "error": "Wrong Answer"
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
Initially, you have a bank account balance of 100 dollars.
You are given an integer purchaseAmount representing the amount you will spend on a purchase in dollars.
At the store where you will make the purchase, the purchase amount is rounded to the nearest multiple of 10. In other words, you pay a non-negative amount, roundedAmount, such that roundedAmount is a multiple of 10 and abs(roundedAmount - purchaseAmount) is minimized.
If there is more than one nearest multiple of 10, the largest multiple is chosen.
Return an integer denoting your account balance after making a purchase worth purchaseAmount dollars from the store.
Note: 0 is considered to be a multiple of 10 in this problem.
 
Example 1:

Input: purchaseAmount = 9
Output: 90
Explanation: In this example, the nearest multiple of 10 to 9 is 10. Hence, your account balance becomes 100 - 10 = 90.

Example 2:

Input: purchaseAmount = 15
Output: 80
Explanation: In this example, there are two nearest multiples of 10 to 15: 10 and 20. So, the larger multiple, 20, is chosen.
Hence, your account balance becomes 100 - 20 = 80.

 
Constraints:

0 <= purchaseAmount <= 100

### Solutions
#### Correct
Attempt 1
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10  # nearest multiple of 10, ties go up
        return 100 - rounded
```

Attempt 2
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```

Attempt 3
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Determine the nearest multiple of 10 (ties go to the larger multiple).
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```

Attempt 4
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10  # usual nearest rounding
        # Tie case: when remainder is exactly 5, choose the larger multiple.
        # The formula above already chooses larger because of +5.
        return 100 - rounded
```

Attempt 5
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Candidates are nearest multiples of 10: floor and ceil relative to purchaseAmount
        lower = (purchaseAmount // 10) * 10
        upper = lower if purchaseAmount % 10 == 0 else lower + 10

        # Choose the multiple with minimum distance; if tie, choose the larger
        if abs(upper - purchaseAmount) < abs(lower - purchaseAmount):
            rounded = upper
        elif abs(upper - purchaseAmount) > abs(lower - purchaseAmount):
            rounded = lower
        else:
            rounded = max(lower, upper)

        return 100 - rounded
```

Attempt 6
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # nearest multiple of 10; if tie, choose the larger multiple
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```

Attempt 7
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10; if tie, choose the larger one.
        rounded = ((purchaseAmount + 5) // 10) * 10
        if rounded > purchaseAmount + 5:
            # Not needed for integer math with (x+5)//10, but kept safe.
            rounded = (purchaseAmount // 10) * 10
        # Special handling for exact midpoints like 15 (between 10 and 20):
        # For purchaseAmount % 10 == 5, formula above already picks the larger.
        return 100 - rounded
```

Attempt 8
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10; if tie, choose the larger one
        remainder = purchaseAmount % 10
        rounded = purchaseAmount - remainder
        if remainder > 5:
            rounded += 10
        elif remainder == 5:
            rounded += 10  # tie: choose larger multiple
        # remainder < 5 => keep rounded as lower multiple

        return 100 - rounded
```

Attempt 9
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        roundedAmount = (purchaseAmount // 10) * 10
        remainder = purchaseAmount % 10

        if remainder < 5:
            roundedAmount = (purchaseAmount // 10) * 10
        elif remainder > 5:
            roundedAmount = (purchaseAmount // 10 + 1) * 10
        else:
            # remainder == 5: tie between current multiple and next multiple; choose larger
            roundedAmount = (purchaseAmount // 10 + 1) * 10

        return 100 - roundedAmount
```

#### Partially Correct
Attempt 1
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # nearest multiples of 10 are k*10 where k is integer
        # handle tie by choosing the larger multiple
        if purchaseAmount % 10 == 0:
            rounded = purchaseAmount
        else:
            lower = (purchaseAmount // 10) * 10
            upper = lower + 10
            # distances: tie goes to upper (larger multiple)
            if purchaseAmount - lower <= upper - purchaseAmount:
                rounded = upper
            else:
                rounded = lower
        return 100 - rounded
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
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10  # nearest multiple of 10, ties go up
        return 100 - rounded
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Determine the nearest multiple of 10 (ties go to the larger multiple).
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10  # usual nearest rounding
        # Tie case: when remainder is exactly 5, choose the larger multiple.
        # The formula above already chooses larger because of +5.
        return 100 - rounded
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Candidates are nearest multiples of 10: floor and ceil relative to purchaseAmount
        lower = (purchaseAmount // 10) * 10
        upper = lower if purchaseAmount % 10 == 0 else lower + 10

        # Choose the multiple with minimum distance; if tie, choose the larger
        if abs(upper - purchaseAmount) < abs(lower - purchaseAmount):
            rounded = upper
        elif abs(upper - purchaseAmount) > abs(lower - purchaseAmount):
            rounded = lower
        else:
            rounded = max(lower, upper)

        return 100 - rounded
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # nearest multiple of 10; if tie, choose the larger multiple
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10; if tie, choose the larger one.
        rounded = ((purchaseAmount + 5) // 10) * 10
        if rounded > purchaseAmount + 5:
            # Not needed for integer math with (x+5)//10, but kept safe.
            rounded = (purchaseAmount // 10) * 10
        # Special handling for exact midpoints like 15 (between 10 and 20):
        # For purchaseAmount % 10 == 5, formula above already picks the larger.
        return 100 - rounded
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10; if tie, choose the larger one
        remainder = purchaseAmount % 10
        rounded = purchaseAmount - remainder
        if remainder > 5:
            rounded += 10
        elif remainder == 5:
            rounded += 10  # tie: choose larger multiple
        # remainder < 5 => keep rounded as lower multiple

        return 100 - rounded
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        roundedAmount = (purchaseAmount // 10) * 10
        remainder = purchaseAmount % 10

        if remainder < 5:
            roundedAmount = (purchaseAmount // 10) * 10
        elif remainder > 5:
            roundedAmount = (purchaseAmount // 10 + 1) * 10
        else:
            # remainder == 5: tie between current multiple and next multiple; choose larger
            roundedAmount = (purchaseAmount // 10 + 1) * 10

        return 100 - roundedAmount
```
```

</details>

#### Tier: `partial`

<details>
<summary>partial attempt 1</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # nearest multiples of 10 are k*10 where k is integer
        # handle tie by choosing the larger multiple
        if purchaseAmount % 10 == 0:
            rounded = purchaseAmount
        else:
            lower = (purchaseAmount // 10) * 10
            upper = lower + 10
            # distances: tie goes to upper (larger multiple)
            if purchaseAmount - lower <= upper - purchaseAmount:
                rounded = upper
            else:
                rounded = lower
        return 100 - rounded
```
```

</details>

### Parsed Memory Items

1. Constraint-first rounding specification
Description: Translate “nearest with tie-breaking” into an explicit, testable rounding rule before coding.
<details>
<summary>Content 1</summary>

```text
Identify the two candidate values (the floor-multiple and the next multiple) and formalize how to choose between them: minimize distance, then apply the tie-breaking rule deterministically. This prevents subtle mistakes when converting descriptive text into integer logic.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
Successful attempts consistently encoded the rounding rule precisely as a deterministic nearest-multiple-of-10 operation, especially handling the tie case by selecting the larger multiple. They mainly used either (1) a compact arithmetic rounding formula that bakes in “ties go up” behavior or (2) an explicit “lower/upper candidates + distance comparison + tie-to-upper” selection. The partially correct attempt likely relied on an inequality with equal-distance cases, but subtle off-by-one or condition branching errors can easily arise when translating distances into integer comparisons. Overall, correctness came from either a verified closed-form rounding expression or a careful candidate-based approach with an explicit tie rule.
```

</details>

2. Bake tie-breaking into the arithmetic
Description: When possible, use a closed-form rounding expression that inherently implements the tie case.
<details>
<summary>Content 2</summary>

```text
For rounding to a base multiple, you can often implement “ties go to the larger candidate” by shifting the value before integer division (e.g., adding half the base with the correct direction). This reduces branching and lowers the risk of incorrect edge-case handling.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
Successful attempts consistently encoded the rounding rule precisely as a deterministic nearest-multiple-of-10 operation, especially handling the tie case by selecting the larger multiple. They mainly used either (1) a compact arithmetic rounding formula that bakes in “ties go up” behavior or (2) an explicit “lower/upper candidates + distance comparison + tie-to-upper” selection. The partially correct attempt likely relied on an inequality with equal-distance cases, but subtle off-by-one or condition branching errors can easily arise when translating distances into integer comparisons. Overall, correctness came from either a verified closed-form rounding expression or a careful candidate-based approach with an explicit tie rule.
```

</details>

3. Prefer candidate-distance selection for correctness
Description: If a closed form feels risky, compute the lower and upper candidates and compare distances explicitly.
<details>
<summary>Content 3</summary>

```text
Construct the two nearest candidates relative to the target, then choose the one with smaller absolute difference; if equal, select the one dictated by the tie rule. This strategy is slower than a formula but is easy to validate against edge cases.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
Successful attempts consistently encoded the rounding rule precisely as a deterministic nearest-multiple-of-10 operation, especially handling the tie case by selecting the larger multiple. They mainly used either (1) a compact arithmetic rounding formula that bakes in “ties go up” behavior or (2) an explicit “lower/upper candidates + distance comparison + tie-to-upper” selection. The partially correct attempt likely relied on an inequality with equal-distance cases, but subtle off-by-one or condition branching errors can easily arise when translating distances into integer comparisons. Overall, correctness came from either a verified closed-form rounding expression or a careful candidate-based approach with an explicit tie rule.
```

</details>

4. Run a mental edge-case audit
Description: Edge cases often occur at exact midpoints and exact multiples; explicitly verify them.
<details>
<summary>Content 4</summary>

```text
After implementing either a formula or branch logic, check scenarios where the value is exactly divisible by the base and where it lands precisely halfway between two multiples. Ensuring these match the specified tie-breaking behavior catches most real failures.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
Successful attempts consistently encoded the rounding rule precisely as a deterministic nearest-multiple-of-10 operation, especially handling the tie case by selecting the larger multiple. They mainly used either (1) a compact arithmetic rounding formula that bakes in “ties go up” behavior or (2) an explicit “lower/upper candidates + distance comparison + tie-to-upper” selection. The partially correct attempt likely relied on an inequality with equal-distance cases, but subtle off-by-one or condition branching errors can easily arise when translating distances into integer comparisons. Overall, correctness came from either a verified closed-form rounding expression or a careful candidate-based approach with an explicit tie rule.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
Successful attempts consistently encoded the rounding rule precisely as a deterministic nearest-multiple-of-10 operation, especially handling the tie case by selecting the larger multiple. They mainly used either (1) a compact arithmetic rounding formula that bakes in “ties go up” behavior or (2) an explicit “lower/upper candidates + distance comparison + tie-to-upper” selection. The partially correct attempt likely relied on an inequality with equal-distance cases, but subtle off-by-one or condition branching errors can easily arise when translating distances into integer comparisons. Overall, correctness came from either a verified closed-form rounding expression or a careful candidate-based approach with an explicit tie rule.
</reasoning>

<memories>
<memory>
<title>Constraint-first rounding specification</title>
<description>Translate “nearest with tie-breaking” into an explicit, testable rounding rule before coding.</description>
<content>Identify the two candidate values (the floor-multiple and the next multiple) and formalize how to choose between them: minimize distance, then apply the tie-breaking rule deterministically. This prevents subtle mistakes when converting descriptive text into integer logic.</content>
</memory>

<memory>
<title>Bake tie-breaking into the arithmetic</title>
<description>When possible, use a closed-form rounding expression that inherently implements the tie case.</description>
<content>For rounding to a base multiple, you can often implement “ties go to the larger candidate” by shifting the value before integer division (e.g., adding half the base with the correct direction). This reduces branching and lowers the risk of incorrect edge-case handling.</content>
</memory>

<memory>
<title>Prefer candidate-distance selection for correctness</title>
<description>If a closed form feels risky, compute the lower and upper candidates and compare distances explicitly.</description>
<content>Construct the two nearest candidates relative to the target, then choose the one with smaller absolute difference; if equal, select the one dictated by the tie rule. This strategy is slower than a formula but is easy to validate against edge cases.</content>
</memory>

<memory>
<title>Run a mental edge-case audit</title>
<description>Edge cases often occur at exact midpoints and exact multiples; explicitly verify them.</description>
<content>After implementing either a formula or branch logic, check scenarios where the value is exactly divisible by the base and where it lands precisely halfway between two multiples. Ensuring these match the specified tie-breaking behavior catches most real failures.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `1.0000`
- Augmented pass@1: `1.0000`
- Improvement: `+0.0000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
Initially, you have a bank account balance of 100 dollars.
You are given an integer purchaseAmount representing the amount you will spend on a purchase in dollars.
At the store where you will make the purchase, the purchase amount is rounded to the nearest multiple of 10. In other words, you pay a non-negative amount, roundedAmount, such that roundedAmount is a multiple of 10 and abs(roundedAmount - purchaseAmount) is minimized.
If there is more than one nearest multiple of 10, the largest multiple is chosen.
Return an integer denoting your account balance after making a purchase worth purchaseAmount dollars from the store.
Note: 0 is considered to be a multiple of 10 in this problem.
 
Example 1:

Input: purchaseAmount = 9
Output: 90
Explanation: In this example, the nearest multiple of 10 to 9 is 10. Hence, your account balance becomes 100 - 10 = 90.

Example 2:

Input: purchaseAmount = 15
Output: 80
Explanation: In this example, there are two nearest multiples of 10 to 15: 10 and 20. So, the larger multiple, 20, is chosen.
Hence, your account balance becomes 100 - 20 = 80.

 
Constraints:

0 <= purchaseAmount <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10 to purchaseAmount.
        # If tie, choose the larger multiple.
        roundedAmount = ((purchaseAmount + 5) // 10) * 10
        return 100 - roundedAmount
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10  # ties go to the larger multiple
        return 100 - rounded
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Round to nearest multiple of 10; if tie, choose the larger multiple.
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = (purchaseAmount + 5) // 10 * 10  # ties go to the larger multiple
        return 100 - rounded
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Round to nearest multiple of 10, tie goes to the larger multiple.
        rounded = ((purchaseAmount + 5) // 10) * 10
        if purchaseAmount % 10 == 5:
            rounded = (purchaseAmount // 10 + 1) * 10  # tie -> larger
        return 100 - rounded
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10. If tie, choose the larger multiple.
        a = (purchaseAmount // 10) * 10          # lower multiple of 10
        b = a + 10                               # upper multiple of 10

        if abs(b - purchaseAmount) <= abs(a - purchaseAmount):
            roundedAmount = b
        else:
            roundedAmount = a

        return 100 - roundedAmount
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Nearest multiple of 10; if tie, choose the larger multiple.
        lower = (purchaseAmount // 10) * 10
        upper = lower if purchaseAmount % 10 == 0 else lower + 10

        if purchaseAmount % 10 == 0:
            rounded = purchaseAmount
        else:
            if upper - purchaseAmount <= purchaseAmount - lower:
                rounded = upper
            else:
                rounded = lower

        return 100 - rounded
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # nearest multiple of 10; if tie, choose the larger multiple
        lower = (purchaseAmount // 10) * 10
        upper = lower if purchaseAmount % 10 == 0 else lower + 10
        
        # if purchaseAmount is exactly between lower and upper, choose upper
        if abs(upper - purchaseAmount) <= abs(purchaseAmount - lower):
            rounded = upper
        else:
            rounded = lower
        
        return 100 - rounded
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = round(purchaseAmount, -1)  # nearest multiple of 10; ties go to larger
        # Python's round handles .5 ties by choosing the larger magnitude.
        return 100 - int(rounded)
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10.
        # If tie, choose the larger multiple.
        lower = (purchaseAmount // 10) * 10
        upper = lower + 10

        # Distances to nearest multiples
        d_lower = purchaseAmount - lower
        d_upper = upper - purchaseAmount

        rounded = upper if d_upper <= d_lower else lower
        return 100 - rounded
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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

  1. Constraint-first rounding specification: Translate “nearest with tie-breaking” into an explicit, testable rounding rule before coding.
     Identify the two candidate values (the floor-multiple and the next multiple) and formalize how to choose between them: minimize distance, then apply the tie-breaking rule deterministically. This prevents subtle mistakes when converting descriptive text into integer logic.
  2. Bake tie-breaking into the arithmetic: When possible, use a closed-form rounding expression that inherently implements the tie case.
     For rounding to a base multiple, you can often implement “ties go to the larger candidate” by shifting the value before integer division (e.g., adding half the base with the correct direction). This reduces branching and lowers the risk of incorrect edge-case handling.
  3. Prefer candidate-distance selection for correctness: If a closed form feels risky, compute the lower and upper candidates and compare distances explicitly.
     Construct the two nearest candidates relative to the target, then choose the one with smaller absolute difference; if equal, select the one dictated by the tie rule. This strategy is slower than a formula but is easy to validate against edge cases.
  4. Run a mental edge-case audit: Edge cases often occur at exact midpoints and exact multiples; explicitly verify them.
     After implementing either a formula or branch logic, check scenarios where the value is exactly divisible by the base and where it lands precisely halfway between two multiples. Ensuring these match the specified tie-breaking behavior catches most real failures.

Apply these insights to the problem below.

### Question:
Initially, you have a bank account balance of 100 dollars.
You are given an integer purchaseAmount representing the amount you will spend on a purchase in dollars.
At the store where you will make the purchase, the purchase amount is rounded to the nearest multiple of 10. In other words, you pay a non-negative amount, roundedAmount, such that roundedAmount is a multiple of 10 and abs(roundedAmount - purchaseAmount) is minimized.
If there is more than one nearest multiple of 10, the largest multiple is chosen.
Return an integer denoting your account balance after making a purchase worth purchaseAmount dollars from the store.
Note: 0 is considered to be a multiple of 10 in this problem.
 
Example 1:

Input: purchaseAmount = 9
Output: 90
Explanation: In this example, the nearest multiple of 10 to 9 is 10. Hence, your account balance becomes 100 - 10 = 90.

Example 2:

Input: purchaseAmount = 15
Output: 80
Explanation: In this example, there are two nearest multiples of 10 to 15: 10 and 20. So, the larger multiple, 20, is chosen.
Hence, your account balance becomes 100 - 20 = 80.

 
Constraints:

0 <= purchaseAmount <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Augmented generation 1</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        base = 10

        # Candidate multiples
        lower = (purchaseAmount // base) * base
        upper = lower if purchaseAmount % base == 0 else lower + base

        # Choose the nearest; on tie choose the larger multiple
        if abs(upper - purchaseAmount) < abs(purchaseAmount - lower):
            rounded = upper
        elif abs(upper - purchaseAmount) > abs(purchaseAmount - lower):
            rounded = lower
        else:
            rounded = max(lower, upper)

        return 100 - rounded
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find the nearest multiple of 10; if tied, choose the larger multiple.
        # Candidates: floor to multiple and next multiple.
        base = 10
        lower = (purchaseAmount // base) * base
        upper = lower if purchaseAmount % base == 0 else lower + base

        # If purchaseAmount is exactly between lower and upper, pick upper (largest).
        if abs(upper - purchaseAmount) <= abs(purchaseAmount - lower):
            roundedAmount = upper
        else:
            roundedAmount = lower

        return 100 - roundedAmount
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        base = 10

        # Find the two candidate multiples of 10 surrounding purchaseAmount
        down = (purchaseAmount // base) * base
        up = down if purchaseAmount % base == 0 else down + base

        # Choose nearest; if tie, choose the larger multiple
        if abs(up - purchaseAmount) < abs(purchaseAmount - down):
            rounded = up
        elif abs(up - purchaseAmount) > abs(purchaseAmount - down):
            rounded = down
        else:
            rounded = max(down, up)

        return 100 - rounded
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        base = 10

        lower = (purchaseAmount // base) * base
        upper = lower if purchaseAmount % base == 0 else lower + base

        # If purchaseAmount is exactly on a multiple, lower == upper already.
        # Otherwise compare distances; if tied, pick the larger multiple (upper).
        dist_lower = abs(purchaseAmount - lower)
        dist_upper = abs(upper - purchaseAmount)

        if dist_lower < dist_upper:
            rounded = lower
        elif dist_upper < dist_lower:
            rounded = upper
        else:
            rounded = upper  # tie -> larger multiple

        return 100 - rounded
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        base = 10
        # Nearest multiple of 10; tie -> larger multiple.
        lower = (purchaseAmount // base) * base
        upper = lower if purchaseAmount % base == 0 else lower + base

        # If exactly at a midpoint (distance equal), pick upper (larger).
        if abs(upper - purchaseAmount) <= abs(purchaseAmount - lower):
            roundedAmount = upper
        else:
            roundedAmount = lower

        return 100 - roundedAmount
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        base = 10
        lower = (purchaseAmount // base) * base
        upper = lower if purchaseAmount % base == 0 else lower + base

        # Choose nearest; if tie, choose larger multiple (upper)
        if abs(upper - purchaseAmount) < abs(purchaseAmount - lower):
            rounded = upper
        elif abs(upper - purchaseAmount) > abs(purchaseAmount - lower):
            rounded = lower
        else:
            rounded = upper  # tie -> larger multiple

        return 100 - rounded
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find nearest multiple of 10 with tie going to the larger multiple.
        base = 10

        lower = (purchaseAmount // base) * base
        upper = lower if purchaseAmount % base == 0 else lower + base

        # If exactly on a multiple, upper == lower.
        if upper == lower:
            rounded = lower
        else:
            d_lower = purchaseAmount - lower
            d_upper = upper - purchaseAmount
            if d_lower < d_upper:
                rounded = lower
            elif d_upper < d_lower:
                rounded = upper
            else:
                # tie -> larger multiple
                rounded = upper

        return 100 - rounded
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # nearest multiple of 10; ties (equal distance) -> choose the larger multiple
        q, r = divmod(purchaseAmount, 10)  # purchaseAmount = 10*q + r, 0<=r<10

        if r < 5:
            rounded = 10 * q
        elif r > 5:
            rounded = 10 * (q + 1)
        else:
            # r == 5 -> exactly halfway: choose the larger multiple
            rounded = 10 * (q + 1)

        return 100 - rounded
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Find nearest multiple of 10 with tie going to the larger multiple
        lower = (purchaseAmount // 10) * 10
        upper = lower + 10

        # Distance comparison; tie -> upper
        if abs(upper - purchaseAmount) <= abs(purchaseAmount - lower):
            roundedAmount = upper
        else:
            roundedAmount = lower

        return 100 - roundedAmount
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        base = 10

        # Nearest multiple candidates
        lower = (purchaseAmount // base) * base
        upper = lower + base

        # If purchaseAmount is exactly on a multiple, roundedAmount is that multiple
        if purchaseAmount % base == 0:
            rounded = purchaseAmount
        else:
            # Choose the nearest; if tie, choose the larger multiple (upper)
            if abs(upper - purchaseAmount) <= abs(purchaseAmount - lower):
                rounded = upper
            else:
                rounded = lower

        return 100 - rounded
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "90",
      "actual": "90",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "100",
      "actual": "100",
      "error": ""
    },
    {
      "passed": true,
      "expected": "70",
      "actual": "70",
      "error": ""
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
      "error": ""
    }
  ]
}
```

</details>
