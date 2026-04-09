# Problem 2857

- Domain: `coding`

## Problem

```text
A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in liters and additionalTank representing the fuel present in the additional tank in liters.
The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.
Return the maximum distance which can be traveled.
Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.
 
Example 1:

Input: mainTank = 5, additionalTank = 10
Output: 60
Explanation: 
After spending 5 litre of fuel, fuel remaining is (5 - 5 + 1) = 1 litre and distance traveled is 50km.
After spending another 1 litre of fuel, no fuel gets injected in the main tank and the main tank becomes empty.
Total distance traveled is 60km.

Example 2:

Input: mainTank = 1, additionalTank = 2
Output: 10
Explanation: 
After spending 1 litre of fuel, the main tank becomes empty.
Total distance traveled is 10km.


 
Constraints:

1 <= mainTank, additionalTank <= 100
```

### Starter Code

```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
```

### Test Cases

```json
[
  {
    "input": "5\n10",
    "output": "60",
    "testtype": "functional"
  },
  {
    "input": "1\n2",
    "output": "10",
    "testtype": "functional"
  },
  {
    "input": "2\n1",
    "output": "20",
    "testtype": "functional"
  },
  {
    "input": "2\n2",
    "output": "20",
    "testtype": "functional"
  },
  {
    "input": "5\n5",
    "output": "60",
    "testtype": "functional"
  },
  {
    "input": "7\n2",
    "output": "80",
    "testtype": "functional"
  },
  {
    "input": "9\n9",
    "output": "110",
    "testtype": "functional"
  },
  {
    "input": "4\n57",
    "output": "40",
    "testtype": "functional"
  },
  {
    "input": "1\n10",
    "output": "10",
    "testtype": "functional"
  },
  {
    "input": "3\n20",
    "output": "30",
    "testtype": "functional"
  },
  {
    "input": "99\n2",
    "output": "1010",
    "testtype": "functional"
  },
  {
    "input": "100\n55",
    "output": "1240",
    "testtype": "functional"
  },
  {
    "input": "100\n60",
    "output": "1240",
    "testtype": "functional"
  },
  {
    "input": "100\n100",
    "output": "1240",
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
A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in liters and additionalTank representing the fuel present in the additional tank in liters.
The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.
Return the maximum distance which can be traveled.
Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.
 
Example 1:

Input: mainTank = 5, additionalTank = 10
Output: 60
Explanation: 
After spending 5 litre of fuel, fuel remaining is (5 - 5 + 1) = 1 litre and distance traveled is 50km.
After spending another 1 litre of fuel, no fuel gets injected in the main tank and the main tank becomes empty.
Total distance traveled is 60km.

Example 2:

Input: mainTank = 1, additionalTank = 2
Output: 10
Explanation: 
After spending 1 litre of fuel, the main tank becomes empty.
Total distance traveled is 10km.


 
Constraints:

1 <= mainTank, additionalTank <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Use simulation: every 5 liters consumed from main tank triggers
        # an immediate transfer of 1 liter if available in additional tank.
        distance = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            if main >= 5:
                # consume 5 liters
                main -= 5
                distance += 50  # 10 km per liter * 5 liters
                # inject 1 liter if possible
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # consume remaining liters
                distance += main * 10
                break

        return distance
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 5 liters consumed from main tank triggers transfer of 1 liter
        # (if additionalTank has at least 1 liter).
        main = mainTank
        add = additionalTank
        liters_used = 0

        while main > 0:
            # Determine how many liters can be consumed before main tank would hit 0
            # Note: transfer happens after every 5 liters consumed.
            if main >= 5:
                main -= 5
                liters_used += 5
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # Consume remaining liters in main tank; no injection triggered
                liters_used += main
                main = 0

        return liters_used * 10
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each liter gives 10 km
        distance_per_liter = 10
        main = mainTank
        add = additionalTank

        # Simulate by liters to account for the "only after every 5 liters" transfers.
        # total_used_since_injection tracks how many liters have been consumed
        # since the last transfer check.
        used_since_check = 0
        while main > 0:
            # Consume 1 liter from main
            main -= 1
            distance_per_liter  # just for clarity; value used below
            # Update consumed count toward the next injection
            used_since_check += 1

            # Every time 5 liters have been consumed from main, inject 1 liter if possible
            if used_since_check == 5:
                used_since_check = 0
                if add >= 1:
                    add -= 1
                    main += 1

        # Total distance: number of liters consumed from main * 10
        # We can compute consumed liters from initial totals and remaining fuel.
        # Since simulation ended with main==0, consumed = mainTank + (number of injections).
        # Instead, compute directly from loop by tracking distance.
        # We'll re-run more simply by tracking distance in the loop.
        return (distance_per_liter) * self._liters_consumed(mainTank, additionalTank)

    def _liters_consumed(self, mainTank: int, additionalTank: int) -> int:
        main = mainTank
        add = additionalTank
        used_since_check = 0
        liters = 0
        while main > 0:
            main -= 1
            liters += 1
            used_since_check += 1
            if used_since_check == 5:
                used_since_check = 0
                if add >= 1:
                    add -= 1
                    main += 1
        return liters
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        km_per_liter = 10
        distance = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            distance += main * km_per_liter
            main = 0

            # If main tank has been emptied, check how much can be replenished.
            # Refill happens only after every 5 liters are consumed from main.
            # For each transfer, it effectively adds 1 liter to main,
            # and requires that 5 liters were consumed from main.
            # In our loop, when main hits 0, it means we just consumed all main,
            # but we need to simulate stepwise by 5-liter batches.
            # Therefore, handle differently:
            break

        # Simulate batch consumption of 5 liters from main, transferring 1 from additional each time.
        main = mainTank
        add = additionalTank
        distance = 0

        while main > 0:
            if main >= 5:
                # consume 5 liters
                main -= 5
                distance += 5 * km_per_liter
                # inject immediately if possible
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # consume remaining liters
                distance += main * km_per_liter
                main = 0

        return distance
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        km_per_liter = 10
        main, add = mainTank, additionalTank
        distance = 0

        while main > 0:
            # Use up whatever is in main; during this period,
            # injections happen only after every 5 liters spent in the main tank.
            while main > 0:
                if main >= 5:
                    main -= 5
                    distance += 5 * km_per_liter
                    if add >= 1:
                        main += 1
                        add -= 1
                    else:
                        # no more injection possible; main will eventually run out
                        continue
                else:
                    distance += main * km_per_liter
                    main = 0

        return distance
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        main = mainTank
        add = additionalTank
        km = 0

        while main > 0:
            # consume fuel from main tank one by one, injecting when it reaches a multiple of 5 used up
            # Equivalent approach:
            # use chunks of 5 liters from main; each full 5-liter chunk triggers (if possible) +1 liter injection.
            if main >= 5:
                main -= 5
                km += 50
                if add > 0:
                    main += 1
                    add -= 1
            else:
                # remaining main fuel can be used directly without injection
                km += main * 10
                break

        return km
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 5 liters consumed triggers an injection of 1 liter (if available).
        # Truck mileage: 10 km per liter.
        distance = 0
        tank = mainTank
        add = additionalTank

        # Travel while we still have fuel in main tank
        while tank > 0:
            if tank >= 5:
                # Consume 5 liters
                tank -= 5
                distance += 50  # 5 liters * 10 km/l
                # Inject 1 liter if possible
                if add > 0:
                    add -= 1
                    tank += 1
            else:
                # Consume remaining liters in main tank
                distance += tank * 10
                break

        return distance
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # 10 km per liter, so compute total liters that can be burned.
        total_liters = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            total_liters += main
            if add == 0:
                break

            # After every 5 liters consumed from main, we may inject 1 liter
            # But if main has less than 5 liters remaining, loop ends naturally.
            if main < 5:
                break

            injections = min(add, main // 5)  # number of injection events we can complete
            added_fuel_to_main = injections  # each event adds 1 liter to main
            add -= injections

            # Remaining main after consuming all but the last partial chunk:
            # We already accounted for burning all current main by adding `main` to total_liters.
            # So we just extend by the injected liters.
            # Set main to the injected liters to continue.
            main = added_fuel_to_main

        return total_liters * 10
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 1 liter moves the truck 10 km.
        # Every time mainTank drops by 5 liters, attempt to inject 1 liter
        # from additionalTank into mainTank (instant/sudden).
        distance = 0
        while mainTank > 0:
            if mainTank >= 5:
                # Use 5 liters from mainTank first
                mainTank -= 5
                distance += 5 * 10
                # Inject 1 liter if possible
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                # Consume remaining liters in mainTank
                distance += mainTank * 10
                mainTank = 0
        return distance
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        tank = mainTank
        add = additionalTank

        while tank > 0:
            tank -= 1
            distance += 10

            # Every time 5 liters are consumed from the main tank, transfer 1 if possible.
            # We track this via counting liters used from the "current main-tank batch".
            # The batch resets after a transfer; to model this simply, we use a counter.
            # However, easiest is to use modulo with how much has been consumed since last transfer.
            # We'll implement a counter:
        return distance
```

```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        tank = mainTank
        add = additionalTank
        distance = 0
        consumed_in_batch = 0  # how many liters have been consumed since last transfer

        while tank > 0:
            # Use 1 liter from main tank
            tank -= 1
            distance += 10
            consumed_in_batch += 1

            # After 5 liters consumed, try to inject 1 liter from additional tank
            if consumed_in_batch == 5:
                consumed_in_batch = 0
                if add > 0 and tank == 0 or tank >= 0:  # transfer can happen even if tank became 0
                    tank += 1
                    add -= 1
                # Note: Injection happens immediately for every 5 liters consumed.

            # If main tank is empty and we can't inject, we're done
            if tank == 0 and add == 0:
                break

        return distance
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
| 7 | 0.9286 | `partial` |
| 8 | 1.0000 | `full` |
| 9 | 0.9286 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
  "passed": 13,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": false,
      "expected": "110",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
  "passed": 13,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": false,
      "expected": "1010",
      "actual": "1230",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in liters and additionalTank representing the fuel present in the additional tank in liters.
The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.
Return the maximum distance which can be traveled.
Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.
 
Example 1:

Input: mainTank = 5, additionalTank = 10
Output: 60
Explanation: 
After spending 5 litre of fuel, fuel remaining is (5 - 5 + 1) = 1 litre and distance traveled is 50km.
After spending another 1 litre of fuel, no fuel gets injected in the main tank and the main tank becomes empty.
Total distance traveled is 60km.

Example 2:

Input: mainTank = 1, additionalTank = 2
Output: 10
Explanation: 
After spending 1 litre of fuel, the main tank becomes empty.
Total distance traveled is 10km.


 
Constraints:

1 <= mainTank, additionalTank <= 100

### Solutions
#### Correct
Attempt 1
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Use simulation: every 5 liters consumed from main tank triggers
        # an immediate transfer of 1 liter if available in additional tank.
        distance = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            if main >= 5:
                # consume 5 liters
                main -= 5
                distance += 50  # 10 km per liter * 5 liters
                # inject 1 liter if possible
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # consume remaining liters
                distance += main * 10
                break

        return distance
```

Attempt 2
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 5 liters consumed from main tank triggers transfer of 1 liter
        # (if additionalTank has at least 1 liter).
        main = mainTank
        add = additionalTank
        liters_used = 0

        while main > 0:
            # Determine how many liters can be consumed before main tank would hit 0
            # Note: transfer happens after every 5 liters consumed.
            if main >= 5:
                main -= 5
                liters_used += 5
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # Consume remaining liters in main tank; no injection triggered
                liters_used += main
                main = 0

        return liters_used * 10
```

Attempt 3
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each liter gives 10 km
        distance_per_liter = 10
        main = mainTank
        add = additionalTank

        # Simulate by liters to account for the "only after every 5 liters" transfers.
        # total_used_since_injection tracks how many liters have been consumed
        # since the last transfer check.
        used_since_check = 0
        while main > 0:
            # Consume 1 liter from main
            main -= 1
            distance_per_liter  # just for clarity; value used below
            # Update consumed count toward the next injection
            used_since_check += 1

            # Every time 5 liters have been consumed from main, inject 1 liter if possible
            if used_since_check == 5:
                used_since_check = 0
                if add >= 1:
                    add -= 1
                    main += 1

        # Total distance: number of liters consumed from main * 10
        # We can compute consumed liters from initial totals and remaining fuel.
        # Since simulation ended with main==0, consumed = mainTank + (number of injections).
        # Instead, compute directly from loop by tracking distance.
        # We'll re-run more simply by tracking distance in the loop.
        return (distance_per_liter) * self._liters_consumed(mainTank, additionalTank)

    def _liters_consumed(self, mainTank: int, additionalTank: int) -> int:
        main = mainTank
        add = additionalTank
        used_since_check = 0
        liters = 0
        while main > 0:
            main -= 1
            liters += 1
            used_since_check += 1
            if used_since_check == 5:
                used_since_check = 0
                if add >= 1:
                    add -= 1
                    main += 1
        return liters
```

Attempt 4
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        km_per_liter = 10
        distance = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            distance += main * km_per_liter
            main = 0

            # If main tank has been emptied, check how much can be replenished.
            # Refill happens only after every 5 liters are consumed from main.
            # For each transfer, it effectively adds 1 liter to main,
            # and requires that 5 liters were consumed from main.
            # In our loop, when main hits 0, it means we just consumed all main,
            # but we need to simulate stepwise by 5-liter batches.
            # Therefore, handle differently:
            break

        # Simulate batch consumption of 5 liters from main, transferring 1 from additional each time.
        main = mainTank
        add = additionalTank
        distance = 0

        while main > 0:
            if main >= 5:
                # consume 5 liters
                main -= 5
                distance += 5 * km_per_liter
                # inject immediately if possible
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # consume remaining liters
                distance += main * km_per_liter
                main = 0

        return distance
```

Attempt 5
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        km_per_liter = 10
        main, add = mainTank, additionalTank
        distance = 0

        while main > 0:
            # Use up whatever is in main; during this period,
            # injections happen only after every 5 liters spent in the main tank.
            while main > 0:
                if main >= 5:
                    main -= 5
                    distance += 5 * km_per_liter
                    if add >= 1:
                        main += 1
                        add -= 1
                    else:
                        # no more injection possible; main will eventually run out
                        continue
                else:
                    distance += main * km_per_liter
                    main = 0

        return distance
```

Attempt 6
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        main = mainTank
        add = additionalTank
        km = 0

        while main > 0:
            # consume fuel from main tank one by one, injecting when it reaches a multiple of 5 used up
            # Equivalent approach:
            # use chunks of 5 liters from main; each full 5-liter chunk triggers (if possible) +1 liter injection.
            if main >= 5:
                main -= 5
                km += 50
                if add > 0:
                    main += 1
                    add -= 1
            else:
                # remaining main fuel can be used directly without injection
                km += main * 10
                break

        return km
```

Attempt 7
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 5 liters consumed triggers an injection of 1 liter (if available).
        # Truck mileage: 10 km per liter.
        distance = 0
        tank = mainTank
        add = additionalTank

        # Travel while we still have fuel in main tank
        while tank > 0:
            if tank >= 5:
                # Consume 5 liters
                tank -= 5
                distance += 50  # 5 liters * 10 km/l
                # Inject 1 liter if possible
                if add > 0:
                    add -= 1
                    tank += 1
            else:
                # Consume remaining liters in main tank
                distance += tank * 10
                break

        return distance
```

Attempt 8
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 1 liter moves the truck 10 km.
        # Every time mainTank drops by 5 liters, attempt to inject 1 liter
        # from additionalTank into mainTank (instant/sudden).
        distance = 0
        while mainTank > 0:
            if mainTank >= 5:
                # Use 5 liters from mainTank first
                mainTank -= 5
                distance += 5 * 10
                # Inject 1 liter if possible
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                # Consume remaining liters in mainTank
                distance += mainTank * 10
                mainTank = 0
        return distance
```

#### Partially Correct
Attempt 1
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # 10 km per liter, so compute total liters that can be burned.
        total_liters = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            total_liters += main
            if add == 0:
                break

            # After every 5 liters consumed from main, we may inject 1 liter
            # But if main has less than 5 liters remaining, loop ends naturally.
            if main < 5:
                break

            injections = min(add, main // 5)  # number of injection events we can complete
            added_fuel_to_main = injections  # each event adds 1 liter to main
            add -= injections

            # Remaining main after consuming all but the last partial chunk:
            # We already accounted for burning all current main by adding `main` to total_liters.
            # So we just extend by the injected liters.
            # Set main to the injected liters to continue.
            main = added_fuel_to_main

        return total_liters * 10
```

Attempt 2
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        tank = mainTank
        add = additionalTank

        while tank > 0:
            tank -= 1
            distance += 10

            # Every time 5 liters are consumed from the main tank, transfer 1 if possible.
            # We track this via counting liters used from the "current main-tank batch".
            # The batch resets after a transfer; to model this simply, we use a counter.
            # However, easiest is to use modulo with how much has been consumed since last transfer.
            # We'll implement a counter:
        return distance
```

```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        tank = mainTank
        add = additionalTank
        distance = 0
        consumed_in_batch = 0  # how many liters have been consumed since last transfer

        while tank > 0:
            # Use 1 liter from main tank
            tank -= 1
            distance += 10
            consumed_in_batch += 1

            # After 5 liters consumed, try to inject 1 liter from additional tank
            if consumed_in_batch == 5:
                consumed_in_batch = 0
                if add > 0 and tank == 0 or tank >= 0:  # transfer can happen even if tank became 0
                    tank += 1
                    add -= 1
                # Note: Injection happens immediately for every 5 liters consumed.

            # If main tank is empty and we can't inject, we're done
            if tank == 0 and add == 0:
                break

        return distance
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
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Use simulation: every 5 liters consumed from main tank triggers
        # an immediate transfer of 1 liter if available in additional tank.
        distance = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            if main >= 5:
                # consume 5 liters
                main -= 5
                distance += 50  # 10 km per liter * 5 liters
                # inject 1 liter if possible
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # consume remaining liters
                distance += main * 10
                break

        return distance
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 5 liters consumed from main tank triggers transfer of 1 liter
        # (if additionalTank has at least 1 liter).
        main = mainTank
        add = additionalTank
        liters_used = 0

        while main > 0:
            # Determine how many liters can be consumed before main tank would hit 0
            # Note: transfer happens after every 5 liters consumed.
            if main >= 5:
                main -= 5
                liters_used += 5
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # Consume remaining liters in main tank; no injection triggered
                liters_used += main
                main = 0

        return liters_used * 10
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each liter gives 10 km
        distance_per_liter = 10
        main = mainTank
        add = additionalTank

        # Simulate by liters to account for the "only after every 5 liters" transfers.
        # total_used_since_injection tracks how many liters have been consumed
        # since the last transfer check.
        used_since_check = 0
        while main > 0:
            # Consume 1 liter from main
            main -= 1
            distance_per_liter  # just for clarity; value used below
            # Update consumed count toward the next injection
            used_since_check += 1

            # Every time 5 liters have been consumed from main, inject 1 liter if possible
            if used_since_check == 5:
                used_since_check = 0
                if add >= 1:
                    add -= 1
                    main += 1

        # Total distance: number of liters consumed from main * 10
        # We can compute consumed liters from initial totals and remaining fuel.
        # Since simulation ended with main==0, consumed = mainTank + (number of injections).
        # Instead, compute directly from loop by tracking distance.
        # We'll re-run more simply by tracking distance in the loop.
        return (distance_per_liter) * self._liters_consumed(mainTank, additionalTank)

    def _liters_consumed(self, mainTank: int, additionalTank: int) -> int:
        main = mainTank
        add = additionalTank
        used_since_check = 0
        liters = 0
        while main > 0:
            main -= 1
            liters += 1
            used_since_check += 1
            if used_since_check == 5:
                used_since_check = 0
                if add >= 1:
                    add -= 1
                    main += 1
        return liters
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        km_per_liter = 10
        distance = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            distance += main * km_per_liter
            main = 0

            # If main tank has been emptied, check how much can be replenished.
            # Refill happens only after every 5 liters are consumed from main.
            # For each transfer, it effectively adds 1 liter to main,
            # and requires that 5 liters were consumed from main.
            # In our loop, when main hits 0, it means we just consumed all main,
            # but we need to simulate stepwise by 5-liter batches.
            # Therefore, handle differently:
            break

        # Simulate batch consumption of 5 liters from main, transferring 1 from additional each time.
        main = mainTank
        add = additionalTank
        distance = 0

        while main > 0:
            if main >= 5:
                # consume 5 liters
                main -= 5
                distance += 5 * km_per_liter
                # inject immediately if possible
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # consume remaining liters
                distance += main * km_per_liter
                main = 0

        return distance
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        km_per_liter = 10
        main, add = mainTank, additionalTank
        distance = 0

        while main > 0:
            # Use up whatever is in main; during this period,
            # injections happen only after every 5 liters spent in the main tank.
            while main > 0:
                if main >= 5:
                    main -= 5
                    distance += 5 * km_per_liter
                    if add >= 1:
                        main += 1
                        add -= 1
                    else:
                        # no more injection possible; main will eventually run out
                        continue
                else:
                    distance += main * km_per_liter
                    main = 0

        return distance
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        main = mainTank
        add = additionalTank
        km = 0

        while main > 0:
            # consume fuel from main tank one by one, injecting when it reaches a multiple of 5 used up
            # Equivalent approach:
            # use chunks of 5 liters from main; each full 5-liter chunk triggers (if possible) +1 liter injection.
            if main >= 5:
                main -= 5
                km += 50
                if add > 0:
                    main += 1
                    add -= 1
            else:
                # remaining main fuel can be used directly without injection
                km += main * 10
                break

        return km
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 5 liters consumed triggers an injection of 1 liter (if available).
        # Truck mileage: 10 km per liter.
        distance = 0
        tank = mainTank
        add = additionalTank

        # Travel while we still have fuel in main tank
        while tank > 0:
            if tank >= 5:
                # Consume 5 liters
                tank -= 5
                distance += 50  # 5 liters * 10 km/l
                # Inject 1 liter if possible
                if add > 0:
                    add -= 1
                    tank += 1
            else:
                # Consume remaining liters in main tank
                distance += tank * 10
                break

        return distance
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 1 liter moves the truck 10 km.
        # Every time mainTank drops by 5 liters, attempt to inject 1 liter
        # from additionalTank into mainTank (instant/sudden).
        distance = 0
        while mainTank > 0:
            if mainTank >= 5:
                # Use 5 liters from mainTank first
                mainTank -= 5
                distance += 5 * 10
                # Inject 1 liter if possible
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                # Consume remaining liters in mainTank
                distance += mainTank * 10
                mainTank = 0
        return distance
```
```

</details>

#### Tier: `partial`

<details>
<summary>partial attempt 1</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # 10 km per liter, so compute total liters that can be burned.
        total_liters = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            total_liters += main
            if add == 0:
                break

            # After every 5 liters consumed from main, we may inject 1 liter
            # But if main has less than 5 liters remaining, loop ends naturally.
            if main < 5:
                break

            injections = min(add, main // 5)  # number of injection events we can complete
            added_fuel_to_main = injections  # each event adds 1 liter to main
            add -= injections

            # Remaining main after consuming all but the last partial chunk:
            # We already accounted for burning all current main by adding `main` to total_liters.
            # So we just extend by the injected liters.
            # Set main to the injected liters to continue.
            main = added_fuel_to_main

        return total_liters * 10
```
```

</details>

<details>
<summary>partial attempt 2</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        tank = mainTank
        add = additionalTank

        while tank > 0:
            tank -= 1
            distance += 10

            # Every time 5 liters are consumed from the main tank, transfer 1 if possible.
            # We track this via counting liters used from the "current main-tank batch".
            # The batch resets after a transfer; to model this simply, we use a counter.
            # However, easiest is to use modulo with how much has been consumed since last transfer.
            # We'll implement a counter:
        return distance
```

```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        tank = mainTank
        add = additionalTank
        distance = 0
        consumed_in_batch = 0  # how many liters have been consumed since last transfer

        while tank > 0:
            # Use 1 liter from main tank
            tank -= 1
            distance += 10
            consumed_in_batch += 1

            # After 5 liters consumed, try to inject 1 liter from additional tank
            if consumed_in_batch == 5:
                consumed_in_batch = 0
                if add > 0 and tank == 0 or tank >= 0:  # transfer can happen even if tank became 0
                    tank += 1
                    add -= 1
                # Note: Injection happens immediately for every 5 liters consumed.

            # If main tank is empty and we can't inject, we're done
            if tank == 0 and add == 0:
                break

        return distance
```
```

</details>

### Parsed Memory Items

1. Event-Driven Simulation Using the Rule’s Natural Unit
Description: Simulate in the same discrete “trigger events” that the problem statement uses to define when state changes occur.
<details>
<summary>Content 1</summary>

```text
Because the transfer happens immediately after each fixed amount of consumption, using that consumption quantum as your simulation step keeps timing correct and avoids subtle off-by-one or “when does the trigger fire” errors. In similar problems, pick the smallest unit that directly corresponds to a stated rule trigger, then update distance and fuel consistently per step.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
The successful attempts share a clean modeling choice: they simulate the process in the natural “event units” implied by the rule (consuming from the main tank in chunks of five liters) and update state only in ways that respect the instantaneous transfer timing. Several failures stem from incorrect or incomplete accounting—either trying to batch without correctly handling when the “after every 5 liters consumed” event occurs relative to stopping conditions, or attempting to compute the number of injections/total liters without a reliable invariant, leading to mismatch in partial final segments. Partially correct attempts show the hazard of partial shortcuts: they start counting but break the simulation logic when the last incomplete batch matters or when the state transition (main reaching empty) interacts with the injection rule.
```

</details>

2. Maintain a Consistent State-Invariant Through Transitions
Description: Track all variables that fully determine future behavior, and ensure every loop iteration preserves the intended invariant about what has been consumed and what remains.
<details>
<summary>Content 2</summary>

```text
Successful solutions keep a coherent model of the remaining fuel in both tanks and update them only when an allowed transfer event occurs. When you introduce a helper counter or batch calculation, verify it matches the exact semantics of the rule (especially around stopping when the main tank becomes partially filled or empty).
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
The successful attempts share a clean modeling choice: they simulate the process in the natural “event units” implied by the rule (consuming from the main tank in chunks of five liters) and update state only in ways that respect the instantaneous transfer timing. Several failures stem from incorrect or incomplete accounting—either trying to batch without correctly handling when the “after every 5 liters consumed” event occurs relative to stopping conditions, or attempting to compute the number of injections/total liters without a reliable invariant, leading to mismatch in partial final segments. Partially correct attempts show the hazard of partial shortcuts: they start counting but break the simulation logic when the last incomplete batch matters or when the state transition (main reaching empty) interacts with the injection rule.
```

</details>

3. Never Short-Circuit Without Handling the Last Partial Segment
Description: A common source of wrong answers is replacing a triggered process with a formula that ignores how the final incomplete cycle behaves.
<details>
<summary>Content 3</summary>

```text
In event-based problems, the last step often doesn’t complete a full trigger unit, so the injected-transfer opportunities stop earlier than a naive “full cycles” count might suggest. If you compute “how many injections” or “total usable fuel” directly, add an explicit check for the residual portion that cannot trigger further events.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
The successful attempts share a clean modeling choice: they simulate the process in the natural “event units” implied by the rule (consuming from the main tank in chunks of five liters) and update state only in ways that respect the instantaneous transfer timing. Several failures stem from incorrect or incomplete accounting—either trying to batch without correctly handling when the “after every 5 liters consumed” event occurs relative to stopping conditions, or attempting to compute the number of injections/total liters without a reliable invariant, leading to mismatch in partial final segments. Partially correct attempts show the hazard of partial shortcuts: they start counting but break the simulation logic when the last incomplete batch matters or when the state transition (main reaching empty) interacts with the injection rule.
```

</details>

4. Risk Check for Timing Semantics After Transformations
Description: Any time you compress time (chunking, modulo/counters, or derived counts), perform a direct verification against the original step-by-step definition.
<details>
<summary>Content 4</summary>

```text
Some attempts failed because they effectively altered when the transfer could occur relative to main tank depletion. A robust pattern is: after any batching or formula simplification, test it conceptually (or with small edge cases) to confirm that the trigger fires exactly when required and that no transfer is counted when the process would already have stopped.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
The successful attempts share a clean modeling choice: they simulate the process in the natural “event units” implied by the rule (consuming from the main tank in chunks of five liters) and update state only in ways that respect the instantaneous transfer timing. Several failures stem from incorrect or incomplete accounting—either trying to batch without correctly handling when the “after every 5 liters consumed” event occurs relative to stopping conditions, or attempting to compute the number of injections/total liters without a reliable invariant, leading to mismatch in partial final segments. Partially correct attempts show the hazard of partial shortcuts: they start counting but break the simulation logic when the last incomplete batch matters or when the state transition (main reaching empty) interacts with the injection rule.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
The successful attempts share a clean modeling choice: they simulate the process in the natural “event units” implied by the rule (consuming from the main tank in chunks of five liters) and update state only in ways that respect the instantaneous transfer timing. Several failures stem from incorrect or incomplete accounting—either trying to batch without correctly handling when the “after every 5 liters consumed” event occurs relative to stopping conditions, or attempting to compute the number of injections/total liters without a reliable invariant, leading to mismatch in partial final segments. Partially correct attempts show the hazard of partial shortcuts: they start counting but break the simulation logic when the last incomplete batch matters or when the state transition (main reaching empty) interacts with the injection rule.
</reasoning>

<memories>
<memory>
<title>Event-Driven Simulation Using the Rule’s Natural Unit</title>
<description>Simulate in the same discrete “trigger events” that the problem statement uses to define when state changes occur.</description>
<content>Because the transfer happens immediately after each fixed amount of consumption, using that consumption quantum as your simulation step keeps timing correct and avoids subtle off-by-one or “when does the trigger fire” errors. In similar problems, pick the smallest unit that directly corresponds to a stated rule trigger, then update distance and fuel consistently per step.</content>
</memory>

<memory>
<title>Maintain a Consistent State-Invariant Through Transitions</title>
<description>Track all variables that fully determine future behavior, and ensure every loop iteration preserves the intended invariant about what has been consumed and what remains.</description>
<content>Successful solutions keep a coherent model of the remaining fuel in both tanks and update them only when an allowed transfer event occurs. When you introduce a helper counter or batch calculation, verify it matches the exact semantics of the rule (especially around stopping when the main tank becomes partially filled or empty).</content>
</memory>

<memory>
<title>Never Short-Circuit Without Handling the Last Partial Segment</title>
<description>A common source of wrong answers is replacing a triggered process with a formula that ignores how the final incomplete cycle behaves.</description>
<content>In event-based problems, the last step often doesn’t complete a full trigger unit, so the injected-transfer opportunities stop earlier than a naive “full cycles” count might suggest. If you compute “how many injections” or “total usable fuel” directly, add an explicit check for the residual portion that cannot trigger further events.</content>
</memory>

<memory>
<title>Risk Check for Timing Semantics After Transformations</title>
<description>Any time you compress time (chunking, modulo/counters, or derived counts), perform a direct verification against the original step-by-step definition.</description>
<content>Some attempts failed because they effectively altered when the transfer could occur relative to main tank depletion. A robust pattern is: after any batching or formula simplification, test it conceptually (or with small edge cases) to confirm that the trigger fires exactly when required and that no transfer is counted when the process would already have stopped.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `0.6000`
- Augmented pass@1: `0.8000`
- Improvement: `+0.2000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in liters and additionalTank representing the fuel present in the additional tank in liters.
The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.
Return the maximum distance which can be traveled.
Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.
 
Example 1:

Input: mainTank = 5, additionalTank = 10
Output: 60
Explanation: 
After spending 5 litre of fuel, fuel remaining is (5 - 5 + 1) = 1 litre and distance traveled is 50km.
After spending another 1 litre of fuel, no fuel gets injected in the main tank and the main tank becomes empty.
Total distance traveled is 60km.

Example 2:

Input: mainTank = 1, additionalTank = 2
Output: 10
Explanation: 
After spending 1 litre of fuel, the main tank becomes empty.
Total distance traveled is 10km.


 
Constraints:

1 <= mainTank, additionalTank <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Every 5 liters consumed from mainTank triggers transfer of 1 liter
        total_liters = mainTank

        if mainTank > 0:
            transfers = min(additionalTank, mainTank // 5)
            # Each transfer adds 1 liter to mainTank
            total_liters += transfers
            # If mainTank has some remainder < 5, it can be consumed as well,
            # but those liters are already included in `total_liters` via mainTank.

        return total_liters * 10
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        tank = mainTank
        add = additionalTank

        while tank > 0:
            # Spend 1 liter from the main tank
            tank -= 1
            distance += 10

            # Track when 5 liters have been consumed since the last injection
            # Using a simple counter avoids simulating liters with extra state.
            # We'll decrement a counter; whenever it hits 0, inject if possible.
            if not hasattr(self, "_consumed"):
                self._consumed = 0

            self._consumed += 1
            if self._consumed == 5 and tank == 0:
                # If main tank is empty exactly after consuming 5, try to inject
                # (Injection happens suddenly and immediately for every 5 liters consumed)
                self._consumed = 0
                if add > 0:
                    add -= 1
                    tank += 1

            # Also handle injection timing when main tank still has fuel
            # The rule says: whenever 5 liters get used up in main tank, if additional has >=1,
            # immediately transfer 1 liter to main tank.
            if self._consumed == 5 and tank > 0:
                self._consumed = 0
                if add > 0:
                    add -= 1
                    tank += 1

        # Clean up the attribute for potential reuse in other calls
        if hasattr(self, "_consumed"):
            delattr(self, "_consumed")

        return distance
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 5 liters consumed from main tank triggers an immediate +1 liter transfer
        liters = mainTank
        # Maximum number of transfers is limited by how many times we can consume 5 liters
        # from the main tank while still having fuel available to transfer.
        while additionalTank > 0:
            # Need 5 liters in main tank to trigger a transfer after consuming them
            if liters < 5:
                break
            # After consuming 5 liters, 1 liter is injected (if available in additional tank)
            liters = liters - 5 + 1
            additionalTank -= 1

        # Total distance: 10 km per liter
        return (mainTank + (initial_additional := 0)) * 0 + (mainTank + 0)  # placeholder to keep structure
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        main = mainTank
        add = additionalTank

        # Process consumption in chunks of up to 5L from main tank
        while main > 0:
            # consume what we can from main
            if main >= 5:
                distance += 5 * 10
                main -= 5
                # inject 1L from additional if possible
                if add >= 1:
                    add -= 1
                    main += 1
            else:
                # consume remaining main
                distance += main * 10
                break

        return distance
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each liter gives 10 km.
        # Every 5 liters consumed from main tank triggers transfer of 1 liter
        # from additional to main (if available), immediately after the 5 liters are used.
        
        distance_km = mainTank * 10
        
        # After mainTank is drained, each transfer effectively adds 1 liter
        # of fuel, but transfers require consuming 5 liters from the current main tank.
        # The process can be modeled as:
        # - While there is at least 5 liters total in main "source" to trigger transfers,
        #   transfer 1 liter from additional to main.
        
        # Number of full 5-liter chunks that can be consumed from the combined fuel stream
        # starting from mainTank. Each time we consume 5 liters from main,
        # we may get +1 liter if additionalTank > 0.
        
        # A simpler direct simulation is safe within constraints.
        while mainTank > 0:
            # Consume remaining mainTank.
            if mainTank < 5:
                break
            # Consume exactly 5 liters to trigger possible transfer.
            mainTank -= 5
            distance_km += 50
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
            # else: no refill, loop continues
        
        return distance_km
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 10 km per liter. Simulate liters used; every 5 liters consumed
        # triggers an instantaneous 1-liter transfer from additional if available.
        main = mainTank
        add = additionalTank
        liters_made = 0
        remaining_to_trigger = 5  # after this many liters consumed in main, try transfer

        while main > 0:
            # Use one liter from main
            main -= 1
            liters_made += 1
            remaining_to_trigger -= 1

            # If we just consumed 5 liters worth since last transfer point,
            # transfer 1 liter from additional tank (sudden) if possible.
            if remaining_to_trigger == 0:
                if add > 0:
                    add -= 1
                    main += 1
                remaining_to_trigger = 5

        return liters_made * 10
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        km_per_liter = 10
        distance = 0

        while mainTank > 0:
            # How many liters can we consume from main tank until it becomes empty
            if mainTank >= 5:
                # Spend 5 liters, then inject 1 if possible
                mainTank -= 5
                distance += 5 * km_per_liter
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                # Consume remaining liters and stop
                distance += mainTank * km_per_liter
                break

        return distance
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each liter provides 10 km
        km_per_liter = 10
        distance = 0

        main = mainTank
        add = additionalTank

        # Inject happens immediately after every 5 liters are consumed from main,
        # if additional has at least 1 liter.
        while main > 0:
            distance += main * km_per_liter
            # consume all main, but we may need to inject in-between.
            # Instead simulate in chunks of 5 consumption from main:
            main -= 5
            # If main was exactly 0 after consuming 5, we might inject;
            # injection occurs whenever 5 liters get used up in main.
            # So we only attempt injection if we just completed a 5-liter consumption.
            if main >= 0:
                # If we reached negative, we consumed more than available; handle below
                pass

            # The above is not correct for remaining < 5; re-simulate properly:
            # We'll discard and implement a correct loop below.

        # Correct simulation:
        main = mainTank
        add = additionalTank
        while main > 0:
            if main >= 5:
                # spend 5 liters from main
                distance += 5 * km_per_liter
                main -= 5
                # injection if possible
                if add >= 1:
                    add -= 1
                    main += 1
            else:
                # spend remaining liters in main
                distance += main * km_per_liter
                main = 0

        return distance
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        main = mainTank
        add = additionalTank
        distance = 0

        # Each time 5 liters are consumed from main, we may inject 1 liter from additional
        while main > 0:
            if main >= 5:
                # consume 5 liters from main
                main -= 5
                distance += 5 * 10
                if add > 0:
                    add -= 1
                    main += 1
            else:
                # consume remaining main
                distance += main * 10
                break

        return distance
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each "fuel event": truck consumes 1 liter; for every 5 liters consumed from main tank,
        # if additionalTank has at least 1 liter, transfer 1 liter into main tank immediately.
        # We'll simulate consumption in mainTank, tracking how many mainTank liters have been used
        # since last possible injection.
        
        main = mainTank
        add = additionalTank
        used_since_injection = 0
        distance = 0

        while main > 0:
            # consume 1 liter from main tank
            main -= 1
            distance += 10
            used_since_injection += 1

            # whenever 5 liters have been consumed from the main tank, inject if possible
            if used_since_injection == 5:
                used_since_injection = 0
                if add > 0:
                    add -= 1
                    main += 1

        return distance
```
```

</details>

#### Baseline Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.7143 | `partial` |
| 1 | 1.0000 | `full` |
| 2 | 0.0000 | `fail` |
| 3 | 1.0000 | `full` |
| 4 | 0.4286 | `partial` |
| 5 | 1.0000 | `full` |
| 6 | 1.0000 | `full` |
| 7 | 0.0000 | `fail` |
| 8 | 1.0000 | `full` |
| 9 | 1.0000 | `full` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 10,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
      "error": ""
    },
    {
      "passed": true,
      "expected": "80",
      "actual": "80",
      "error": ""
    },
    {
      "passed": false,
      "expected": "110",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "1200",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "1200",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "1200",
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
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "60",
      "actual": "5",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "10",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "20",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "20",
      "actual": "2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "60",
      "actual": "5",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "80",
      "actual": "7",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "110",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "4",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "10",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "30",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1010",
      "actual": "99",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "100",
      "error": "Wrong Answer"
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
  "passed": 6,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "60",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": false,
      "expected": "60",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "80",
      "actual": "120",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "110",
      "actual": "190",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": false,
      "expected": "1010",
      "actual": "1990",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "2200",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "2200",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "2200",
      "error": "Wrong Answer"
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
  "passed": 0,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "60",
      "actual": "110",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "10",
      "actual": "20",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "20",
      "actual": "40",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "20",
      "actual": "40",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "60",
      "actual": "110",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "80",
      "actual": "170",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "110",
      "actual": "240",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "40",
      "actual": "80",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "10",
      "actual": "20",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "30",
      "actual": "60",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1010",
      "actual": "11310",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "11740",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "11740",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "11740",
      "error": "Wrong Answer"
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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

  1. Event-Driven Simulation Using the Rule’s Natural Unit: Simulate in the same discrete “trigger events” that the problem statement uses to define when state changes occur.
     Because the transfer happens immediately after each fixed amount of consumption, using that consumption quantum as your simulation step keeps timing correct and avoids subtle off-by-one or “when does the trigger fire” errors. In similar problems, pick the smallest unit that directly corresponds to a stated rule trigger, then update distance and fuel consistently per step.
  2. Maintain a Consistent State-Invariant Through Transitions: Track all variables that fully determine future behavior, and ensure every loop iteration preserves the intended invariant about what has been consumed and what remains.
     Successful solutions keep a coherent model of the remaining fuel in both tanks and update them only when an allowed transfer event occurs. When you introduce a helper counter or batch calculation, verify it matches the exact semantics of the rule (especially around stopping when the main tank becomes partially filled or empty).
  3. Never Short-Circuit Without Handling the Last Partial Segment: A common source of wrong answers is replacing a triggered process with a formula that ignores how the final incomplete cycle behaves.
     In event-based problems, the last step often doesn’t complete a full trigger unit, so the injected-transfer opportunities stop earlier than a naive “full cycles” count might suggest. If you compute “how many injections” or “total usable fuel” directly, add an explicit check for the residual portion that cannot trigger further events.
  4. Risk Check for Timing Semantics After Transformations: Any time you compress time (chunking, modulo/counters, or derived counts), perform a direct verification against the original step-by-step definition.
     Some attempts failed because they effectively altered when the transfer could occur relative to main tank depletion. A robust pattern is: after any batching or formula simplification, test it conceptually (or with small edge cases) to confirm that the trigger fires exactly when required and that no transfer is counted when the process would already have stopped.

Apply these insights to the problem below.

### Question:
A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in liters and additionalTank representing the fuel present in the additional tank in liters.
The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.
Return the maximum distance which can be traveled.
Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.
 
Example 1:

Input: mainTank = 5, additionalTank = 10
Output: 60
Explanation: 
After spending 5 litre of fuel, fuel remaining is (5 - 5 + 1) = 1 litre and distance traveled is 50km.
After spending another 1 litre of fuel, no fuel gets injected in the main tank and the main tank becomes empty.
Total distance traveled is 60km.

Example 2:

Input: mainTank = 1, additionalTank = 2
Output: 10
Explanation: 
After spending 1 litre of fuel, the main tank becomes empty.
Total distance traveled is 10km.


 
Constraints:

1 <= mainTank, additionalTank <= 100

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Augmented generation 1</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each "event" happens right after the main tank loses 5 liters.
        # If main tank hits a multiple-of-5 threshold and additionalTank >= 1,
        # we inject exactly 1 liter immediately.
        distance = 0
        while mainTank > 0:
            # consume 5 liters at most (or less if mainTank < 5)
            if mainTank >= 5:
                mainTank -= 5
                distance += 50  # 5 liters * 10 km per liter
                if additionalTank >= 1:
                    additionalTank -= 1
                    mainTank += 1
            else:
                # final partial segment: main tank runs out
                distance += mainTank * 10
                break
        return distance
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Simulation in the natural trigger unit: each time main tank loses 5 liters,
        # we may inject 1 liter from the additional tank (if available).
        dist = 0
        main = mainTank
        add = additionalTank

        while main > 0:
            # How much fuel we can burn before the next possible injection trigger
            # (or until main tank becomes empty).
            burn = min(main, 5)
            main -= burn
            dist += burn * 10

            # If we just consumed exactly 5 liters, an injection may happen.
            if burn == 5 and add > 0:
                main += 1
                add -= 1

        return dist
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Simulate in the natural trigger unit: every time mainTank consumes 5 liters
        # and then (immediately) may receive 1 liter from additionalTank.
        km_per_liter = 10
        main = mainTank
        add = additionalTank
        dist = 0

        while main > 0:
            if main >= 5:
                # consume 5 liters -> +50 km, main becomes main-5
                main -= 5
                dist += 5 * km_per_liter
                # injection happens right after this consumption event
                if add >= 1:
                    add -= 1
                    main += 1
            else:
                # consume the remaining liters in main (no more 5-liter trigger possible)
                dist += main * km_per_liter
                break

        return dist
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each trigger happens right after every 5 liters are consumed from main tank.
        # Truck mileage is 10 km per liter, so total distance = 10 * total liters consumed.
        distance_per_liter = 10
        
        main = mainTank
        additional = additionalTank
        liters_consumed = 0
        
        while main > 0:
            # Consume from main until it runs out or until the next 5L trigger point.
            if main >= 5:
                # Consume exactly 5 liters to trigger possible transfer.
                main -= 5
                liters_consumed += 5
                
                # Immediately transfer 1 liter if possible.
                if additional >= 1:
                    additional -= 1
                    main += 1
            else:
                # Last partial segment: consume remaining main and stop.
                liters_consumed += main
                main = 0
        
        return liters_consumed * distance_per_liter
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Simulate in event-sized steps: every time 5 liters are consumed from main tank,
        # a transfer of 1 liter happens immediately if available.
        km_per_liter = 10
        step = 5

        distance_liters_used = 0

        while mainTank > 0:
            # If mainTank has less than 5 liters, it will run out before any transfer trigger.
            if mainTank < step:
                distance_liters_used += mainTank
                break

            # Consume 5 liters from main tank (trigger point)
            mainTank -= step
            distance_liters_used += step

            # Trigger transfer if possible
            if additionalTank >= 1:
                additionalTank -= 1
                mainTank += 1

        return distance_liters_used * km_per_liter
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # 1 liter consumption -> +10 km
        km_per_liter = 10

        fuel_main = mainTank
        fuel_add = additionalTank
        distance = 0

        # Consume until main tank empties
        while fuel_main > 0:
            if fuel_main >= 5:
                # Spend 5 liters in the main tank
                fuel_main -= 5
                distance += 5 * km_per_liter

                # Injection happens immediately after each 5 liters are used up
                if fuel_add >= 1:
                    fuel_add -= 1
                    fuel_main += 1
            else:
                # Final partial segment: main tank has < 5 liters left, consume it all
                distance += fuel_main * km_per_liter
                break

        return distance
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Simulate in the same discrete trigger units:
        # each 5 liters consumed in main tank triggers a possible 1-liter transfer.
        distance_per_liter = 10
        step = 5

        main = mainTank
        add = additionalTank
        dist = 0

        # Keep consuming until main tank is empty
        while main > 0:
            # Consume as much as possible before either main empties
            # or we hit a 5-liter boundary that allows injection.
            consume = min(main, step)
            main -= consume
            dist += consume * distance_per_liter

            # If main tank is still positive and we consumed exactly 5 liters,
            # then immediately after that, try to inject 1 liter.
            if consume == step and main > 0 and add > 0:
                main += 1
                add -= 1

        return dist
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # We simulate in natural trigger steps:
        # each time mainTank loses exactly 5 liters, we *may* inject 1 liter
        # from additionalTank (if available) immediately after that 5 liters are consumed.
        distance = 0
        mileage = 10

        while mainTank > 0:
            if mainTank >= 5:
                # Consume 5 liters from main tank
                mainTank -= 5
                distance += 5 * mileage

                # Then, if additional tank has at least 1 liter, inject 1 liter
                if additionalTank >= 1:
                    additionalTank -= 1
                    mainTank += 1
            else:
                # Consume remaining main tank fuel and stop (no further injection can occur)
                distance += mainTank * mileage
                break

        return distance
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Each 1 liter consumption moves 10 km.
        # Transfer event happens immediately after consuming each chunk of 5 liters from main tank,
        # but only if additionalTank has at least 1 liter available.
        km_per_liter = 10
        distance = 0

        while mainTank > 0:
            if mainTank >= 5:
                # Spend 5 liters
                mainTank -= 5
                additionalTank -= 1 if additionalTank > 0 else 0  # (safe, we'll check below)
                distance += 5 * km_per_liter

                # Injection happens if we actually have additional fuel.
                if additionalTank >= 0:
                    # The transfer should only occur if additionalTank had at least 1 BEFORE transfer.
                    # So undo the above decrement if it was invalid.
                    # Better: handle explicitly instead of relying on decrement above.
                    pass
            else:
                # Consume remaining liters in main tank
                distance += mainTank * km_per_liter
                break

            # Correct injection semantics:
            # If after spending 5 liters mainTank is (old - 5), then transfer 1 liter if available.
            # We'll re-check availability by tracking with explicit logic (no incorrect decrement).
            # To do that, we need to remove the earlier wrong block. Let's rewrite cleanly below.

        # Clean implementation:
        main = mainTank
        add = additionalTank
        distance = 0

        while main > 0:
            # Determine how many liters we can consume before next possible injection decision.
            if main >= 5:
                # Consume exactly 5 liters to trigger a possible injection
                main -= 5
                distance += 50  # 5 * 10
                if add >= 1:
                    add -= 1
                    main += 1
                # Loop continues (possibly with main == 0 or >=0)
            else:
                # Consume remaining liters; no injection can happen because less than 5 liters remain
                distance += main * 10
                break

        return distance
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Simulation in the natural trigger unit: each time we consume 1 liter.
        # After every 5 liters consumed *from the main tank*, if additionalTank >= 1,
        # transfer 1 liter immediately into mainTank.
        km_per_liter = 10

        remaining_main = mainTank
        remaining_additional = additionalTank

        consumed_in_cycle = 0  # how many liters have been consumed since last possible transfer
        distance_km = 0

        while remaining_main > 0:
            # consume 1 liter from main tank
            remaining_main -= 1
            consumed_in_cycle += 1
            distance_km += km_per_liter

            # when we reach exactly 5 liters consumed, attempt injection
            if consumed_in_cycle == 5:
                consumed_in_cycle = 0
                if remaining_additional > 0:
                    remaining_additional -= 1
                    remaining_main += 1

        return distance_km
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
| 6 | 0.7857 | `partial` |
| 7 | 1.0000 | `full` |
| 8 | 0.4286 | `partial` |
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "60",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": false,
      "expected": "60",
      "actual": "50",
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
      "expected": "110",
      "actual": "100",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
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
  "passed": 6,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "60",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "10",
      "actual": "10",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": false,
      "expected": "60",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "80",
      "actual": "20",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "110",
      "actual": "40",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": false,
      "expected": "1010",
      "actual": "40",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240",
      "actual": "0",
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
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "60",
      "actual": "60",
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
      "expected": "110",
      "actual": "110",
      "error": ""
    },
    {
      "passed": true,
      "expected": "40",
      "actual": "40",
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
      "expected": "30",
      "actual": "30",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1010",
      "actual": "1010",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240",
      "actual": "1240",
      "error": ""
    }
  ]
}
```

</details>
