# Problem 2757

- Domain: `coding`

## Problem

```text
You are given two numeric strings num1 and num2 and two integers max_sum and min_sum. We denote an integer x to be good if:

num1 <= x <= num2
min_sum <= digit_sum(x) <= max_sum.

Return the number of good integers. Since the answer may be large, return it modulo 10^9 + 7.
Note that digit_sum(x) denotes the sum of the digits of x.
 
Example 1:

Input: num1 = "1", num2 = "12", min_sum = 1, max_sum = 8
Output: 11
Explanation: There are 11 integers whose sum of digits lies between 1 and 8 are 1,2,3,4,5,6,7,8,10,11, and 12. Thus, we return 11.

Example 2:

Input: num1 = "1", num2 = "5", min_sum = 1, max_sum = 5
Output: 5
Explanation: The 5 integers whose sum of digits lies between 1 and 5 are 1,2,3,4, and 5. Thus, we return 5.

 
Constraints:

1 <= num1 <= num2 <= 10^22
1 <= min_sum <= max_sum <= 400
```

### Starter Code

```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
```

### Test Cases

```json
[
  {
    "input": "\"1\"\n\"12\"\n1\n8",
    "output": "11",
    "testtype": "functional"
  },
  {
    "input": "\"1\"\n\"5\"\n1\n5",
    "output": "5",
    "testtype": "functional"
  },
  {
    "input": "\"1\"\n\"1\"\n1\n1",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"71\"\n\"78\"\n6\n32",
    "output": "8",
    "testtype": "functional"
  },
  {
    "input": "\"4\"\n\"9\"\n287\n304",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"29\"\n\"69\"\n25\n39",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"6\"\n\"9\"\n208\n313",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"4\"\n\"8\"\n250\n394",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"96\"\n\"96\"\n33\n35",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"4353191\"\n\"7832334\"\n61\n141",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"44181649\"\n\"68139596\"\n285\n324",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"738081037827515190649\"\n\"2197300974439040693603\"\n147\n196",
    "output": "258362773",
    "testtype": "functional"
  },
  {
    "input": "\"9674839970147070251866\"\n\"9732662129160783127981\"\n66\n253",
    "output": "289633652",
    "testtype": "functional"
  },
  {
    "input": "\"3046150261507503990489\"\n\"7775829181095068737136\"\n127\n169",
    "output": "157138097",
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
You are given two numeric strings num1 and num2 and two integers max_sum and min_sum. We denote an integer x to be good if:

num1 <= x <= num2
min_sum <= digit_sum(x) <= max_sum.

Return the number of good integers. Since the answer may be large, return it modulo 10^9 + 7.
Note that digit_sum(x) denotes the sum of the digits of x.
 
Example 1:

Input: num1 = "1", num2 = "12", min_sum = 1, max_sum = 8
Output: 11
Explanation: There are 11 integers whose sum of digits lies between 1 and 8 are 1,2,3,4,5,6,7,8,10,11, and 12. Thus, we return 11.

Example 2:

Input: num1 = "1", num2 = "5", min_sum = 1, max_sum = 5
Output: 5
Explanation: The 5 integers whose sum of digits lies between 1 and 5 are 1,2,3,4, and 5. Thus, we return 5.

 
Constraints:

1 <= num1 <= num2 <= 10^22
1 <= min_sum <= max_sum <= 400

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def add_one_str(s: str) -> str:
            a = list(s)
            i = len(a) - 1
            carry = 1
            while i >= 0 and carry:
                d = ord(a[i]) - 48
                d += carry
                if d == 10:
                    a[i] = '0'
                    carry = 1
                else:
                    a[i] = chr(48 + d)
                    carry = 0
                i -= 1
            if carry:
                a.insert(0, '1')
            # strip leading zeros if any (shouldn't happen)
            return ''.join(a).lstrip('0') or "0"

        def dec_one_str(s: str) -> str:
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            borrow = 1
            while i >= 0 and borrow:
                d = ord(a[i]) - 48
                if d >= borrow:
                    d -= borrow
                    a[i] = chr(48 + d)
                    borrow = 0
                else:
                    d = d + 10 - borrow
                    a[i] = chr(48 + d)
                    borrow = 1
                i -= 1
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digit_dp_upto(bound: str) -> int:
            """
            Count x in [0, bound] such that digit_sum(x) in [min_sum, max_sum].
            """
            if bound == "0":
                return 1 if min_sum <= 0 <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)
            # dp[pos][tight][sum] -> count
            # We'll use rolling arrays for pos.
            maxS = max_sum
            # initialize
            from collections import defaultdict

            # Use list-of-dicts for speed; sum range <= 400.
            dp_tight0 = [0] * (maxS + 1)  # tight==0
            dp_tight1 = [0] * (maxS + 1)  # tight==1
            dp_tight1[0] = 1

            for pos in range(n):
                ndp_tight0 = [0] * (maxS + 1)
                ndp_tight1 = [0] * (maxS + 1)
                lim = digits[pos]

                # From tight==0: upper digit always 9
                # Transition to tight==0 always
                for s_val in range(0, maxS + 1):
                    cnt = dp_tight0[s_val]
                    if not cnt:
                        continue
                    base = s_val
                    # add digit 0..9
                    # shift counts by digit
                    for dig in range(10):
                        ns = base + dig
                        if ns <= maxS:
                            ndp_tight0[ns] = (ndp_tight0[ns] + cnt) % MOD

                # From tight==1: upper digit constrained by lim
                for s_val in range(0, maxS + 1):
                    cnt = dp_tight1[s_val]
                    if not cnt:
                        continue
                    base = s_val
                    for dig in range(lim + 1):
                        ns = base + dig
                        if ns > maxS:
                            continue
                        if dig == lim:
                            ndp_tight1[ns] = (ndp_tight1[ns] + cnt) % MOD
                        else:
                            ndp_tight0[ns] = (ndp_tight0[ns] + cnt) % MOD

                dp_tight0, dp_tight1 = ndp_tight0, ndp_tight1

            ans = 0
            for s_val in range(min_sum, max_sum + 1):
                ans = (ans + dp_tight0[s_val] + dp_tight1[s_val]) % MOD
            return ans

        # Count in [0, num2] - count in [0, num1-1]
        num1m1 = dec_one_str(num1)
        res2 = digit_dp_upto(num2)
        res1 = digit_dp_upto(num1m1) if num1m1 != "0" or min_sum <= 0 <= max_sum else digit_dp_upto(num1m1)
        # Note: digit_dp_upto handles "0" correctly anyway.
        return (res2 - res1) % MOD
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    MOD = 10**9 + 7

    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # digit DP: count numbers in [0..N] with digit sum in [min_sum..max_sum]
        def count_upto(N: str) -> int:
            digits = list(map(int, N))
            L = len(digits)

            # dp[pos][tight] = array over sums
            # We'll store only for current pos to save memory.
            # dp_tight[s] for tight=1, dp_loose[s] for tight=0
            # tight means prefix equals N so far; loose means already smaller.
            dp_loose = [0] * (max_sum + 1)  # loose at current pos
            dp_tight = [0] * (max_sum + 1)  # tight at current pos

            # start: before placing any digits, sum=0
            dp_tight[0] = 1

            for pos in range(L):
                ndp_loose = [0] * (max_sum + 1)
                ndp_tight = [0] * (max_sum + 1)
                limit = digits[pos]

                # Transition for loose states: can put digits 0..9 always, remains loose
                for s in range(max_sum + 1):
                    ways = dp_loose[s]
                    if not ways:
                        continue
                    for d in range(10):
                        ns = s + d
                        if ns <= max_sum:
                            ndp_loose[ns] = (ndp_loose[ns] + ways) % self.MOD

                # Transition for tight states
                for s in range(max_sum + 1):
                    ways = dp_tight[s]
                    if not ways:
                        continue
                    for d in range(limit + 1):
                        ns = s + d
                        if ns > max_sum:
                            continue
                        if d == limit:
                            ndp_tight[ns] = (ndp_tight[ns] + ways) % self.MOD
                        else:
                            ndp_loose[ns] = (ndp_loose[ns] + ways) % self.MOD

                dp_loose, dp_tight = ndp_loose, ndp_tight

            # Sum counts for sums in [min_sum..max_sum], excluding leading-zero issue:
            # The DP counts numbers from 0..N including 0 with digit sum 0.
            # Since min_sum >= 1, excluding 0 is automatic.
            ans = 0
            for s in range(min_sum, max_sum + 1):
                ans = (ans + dp_loose[s] + dp_tight[s]) % self.MOD
            return ans

        def dec_one_str(s: str) -> str:
            # returns (s - 1) as string, assuming s represents an integer >= 1
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        # Answer = count_upto(num2) - count_upto(num1-1)
        left = dec_one_str(num1)
        right_count = count_upto(num2)
        left_count = 0 if left == "0" else count_upto(left)

        return (right_count - left_count) % self.MOD
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def add_one_str(s: str) -> str:
            # not used
            return s

        def dec_str(s: str) -> str:
            # s is positive integer string without leading zeros
            if s == "0":
                return "0"
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            out = ''.join(arr).lstrip('0')
            return out if out else "0"

        def count_upto(limit: str) -> int:
            # count x in [0, limit] with min_sum<=digit_sum(x)<=max_sum
            if limit == "0":
                total = 0
                ds = 0
                if min_sum <= ds <= max_sum:
                    total = 1
                return total

            digits = list(map(int, limit))
            n = len(digits)

            # dp[pos][tight][sum] -> ways
            # Use rolling arrays over sum and tight
            # Initialize at pos=0
            dp_tight = [0] * (max_sum + 1)  # ways with tight=True at this pos
            dp_loose = [0] * (max_sum + 1) # ways with tight=False at this pos
            dp_tight[0] = 1

            for pos in range(n):
                new_tight = [0] * (max_sum + 1)
                new_loose = [0] * (max_sum + 1)
                cur = digits[pos]
                for ssum in range(max_sum + 1):
                    # From tight state
                    w = dp_tight[ssum]
                    if w:
                        for d in range(cur + 1):
                            ns = ssum + d
                            if ns > max_sum:
                                continue
                            if d == cur:
                                new_tight[ns] = (new_tight[ns] + w) % MOD
                            else:
                                new_loose[ns] = (new_loose[ns] + w) % MOD
                    # From loose state
                    w2 = dp_loose[ssum]
                    if w2:
                        for d in range(10):
                            ns = ssum + d
                            if ns > max_sum:
                                continue
                            new_loose[ns] = (new_loose[ns] + w2) % MOD

                dp_tight, dp_loose = new_tight, new_loose

            ans = 0
            for ssum in range(min_sum, max_sum + 1):
                ans = (ans + dp_tight[ssum] + dp_loose[ssum]) % MOD
            return ans

        def mod_sub(a, b):
            return (a - b) % MOD

        # Count in [num1, num2] = count_upto(num2) - count_upto(num1-1)
        num1_minus = dec_str(num1)  # if num1=="1", gives "0"
        res = mod_sub(count_upto(num2), count_upto(num1_minus))
        return res % MOD
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def count_leq(s: str) -> int:
            # Count x in [0, s] such that digit_sum(x) in [min_sum, max_sum]
            # (Leading zeros allowed; then exclude x=0 by zero-sum handling via min_sum>=1)
            n = len(s)
            digits = list(map(int, s))

            dp = [0] * (max_sum + 1)
            dp[0] = 1  # no digits processed, sum=0

            tight_states = dp[:]  # dp for tight=1 at start: only sum 0 has 1 way
            # We'll use standard DP with tight flag:
            # dp_tight[sum] for tight=1; dp_loose[sum] for tight=0
            dp_tight = [0] * (max_sum + 1)
            dp_loose = [0] * (max_sum + 1)
            dp_tight[0] = 1

            for i in range(n):
                ndp_tight = [0] * (max_sum + 1)
                ndp_loose = [0] * (max_sum + 1)
                limit = digits[i]

                # transitions from tight
                for sm in range(max_sum + 1):
                    ways = dp_tight[sm]
                    if not ways:
                        continue
                    # choose digit d
                    for d in range(limit + 1):
                        nsm = sm + d
                        if nsm > max_sum:
                            continue
                        if d == limit:
                            ndp_tight[nsm] = (ndp_tight[nsm] + ways) % MOD
                        else:
                            ndp_loose[nsm] = (ndp_loose[nsm] + ways) % MOD

                # transitions from loose: digit can be 0..9
                for sm in range(max_sum + 1):
                    ways = dp_loose[sm]
                    if not ways:
                        continue
                    for d in range(10):
                        nsm = sm + d
                        if nsm > max_sum:
                            continue
                        ndp_loose[nsm] = (ndp_loose[nsm] + ways) % MOD

                dp_tight, dp_loose = ndp_tight, ndp_loose

            ans = 0
            for sm in range(min_sum, max_sum + 1):
                ans = (ans + dp_tight[sm] + dp_loose[sm]) % MOD
            # min_sum >= 1 in constraints, so x=0 (sum=0) is naturally excluded
            return ans

        def dec_one(s: str) -> str:
            # return string for (int(s) - 1), assuming s represents a positive integer
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            res = ''.join(arr).lstrip('0')
            return res if res else "0"

        res2 = count_leq(num2)
        # count_leq(num1 - 1)
        if num1 == "0":
            res1 = 0
        else:
            prev = dec_one(num1)
            res1 = count_leq(prev) if prev != "0" else 0

        return (res2 - res1) % MOD
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # decrement a non-negative integer string >= "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            j = 0
            while j < len(a) - 1 and a[j] == '0':
                j += 1
            return ''.join(a[j:])

        def add_leading_zeroes(s: str, n: int) -> str:
            return s.rjust(n, '0')

        def count_upto(bound: str) -> int:
            # Count x in [0, bound] with digit sum in [min_sum, max_sum]
            if bound == "0":
                return 1 if min_sum <= 0 <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)

            # dp[pos][sum][tight] where tight in {0,1}
            # Use rolling arrays: dp_sum_tight[sum][tight]
            maxS = max_sum
            dp = [[0, 0] for _ in range(maxS + 1)]
            dp[0][1] = 1  # pos=0, sum=0, tight=1 initially

            for pos in range(n):
                new = [[0, 0] for _ in range(maxS + 1)]
                limit = digits[pos]
                for ssum in range(maxS + 1):
                    for tight in (0, 1):
                        ways = dp[ssum][tight]
                        if ways == 0:
                            continue
                        up = limit if tight == 1 else 9
                        for d in range(up + 1):
                            ns = ssum + d
                            if ns > maxS:
                                continue
                            ntight = 1 if (tight == 1 and d == up) else 0
                            new[ns][ntight] = (new[ns][ntight] + ways) % MOD
                dp = new

            ans = 0
            for ssum in range(min_sum, max_sum + 1):
                ans = (ans + dp[ssum][0] + dp[ssum][1]) % MOD
            return ans

        # Result = count <= num2 - count <= (num1 - 1)
        if num1 == "0":
            return count_upto(num2)

        num1m1 = dec_str(num1)
        return (count_upto(num2) - count_upto(num1m1)) % MOD
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_one(s: str) -> str:
            # returns max(s-1, 0) as string
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digits_of(n: str):
            return list(map(int, n))

        def count_upto(n: str) -> int:
            # count x in [0, n] with digit sum in [min_sum, max_sum]
            if n == "0":
                return 0 if not (min_sum <= 0 <= max_sum) else 1

            ds = digits_of(n)
            L = len(ds)

            # dp[pos][sum] where pos processed left->right, tight handling via two layers
            # Use rolling arrays for tight=0/1
            maxS = max_sum
            # dp_tight: sum -> ways
            dp_tight = [0] * (maxS + 1)
            dp_loose = [0] * (maxS + 1)
            dp_tight[0] = 1

            for pos in range(L):
                ndp_tight = [0] * (maxS + 1)
                ndp_loose = [0] * (maxS + 1)
                limit = ds[pos]

                # transition from tight
                for ssum in range(maxS + 1):
                    ways = dp_tight[ssum]
                    if not ways:
                        continue
                    for dig in range(limit + 1):
                        ns = ssum + dig
                        if ns > maxS:
                            break
                        if dig == limit:
                            ndp_tight[ns] = (ndp_tight[ns] + ways) % MOD
                        else:
                            ndp_loose[ns] = (ndp_loose[ns] + ways) % MOD

                # transition from loose (already less, so any digit 0..9)
                for ssum in range(maxS + 1):
                    ways = dp_loose[ssum]
                    if not ways:
                        continue
                    for dig in range(10):
                        ns = ssum + dig
                        if ns > maxS:
                            break
                        ndp_loose[ns] = (ndp_loose[ns] + ways) % MOD

                dp_tight, dp_loose = ndp_tight, ndp_loose

            total = 0
            for ssum in range(min_sum, max_sum + 1):
                total = (total + dp_tight[ssum] + dp_loose[ssum]) % MOD
            return total

        upper = count_upto(num2)
        lower_bound = dec_one(num1)
        lower = count_upto(lower_bound)

        ans = (upper - lower) % MOD
        return ans
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def digit_sum_up_to(s: str):
            """
            Returns dp[s][k]? -> Actually returns list ways[k] = count of integers in [0, s]
            with digit sum exactly k. Includes x=0 (digit sum 0).
            """
            digits = list(map(int, s))
            n = len(digits)

            # dp[pos][sum][tight]
            # We'll use rolling arrays: dp_tight for each sum.
            max_possible = 9 * n
            dp_tight_0 = [0] * (max_possible + 1)  # tight = 0 (already less)
            dp_tight_1 = [0] * (max_possible + 1)  # tight = 1 (equal so far)
            dp_tight_1[0] = 1

            for i in range(n):
                ndp0 = [0] * (max_possible + 1)
                ndp1 = [0] * (max_possible + 1)
                lim = digits[i]

                # From tight = 0: next digit can be 0..9, remains tight = 0
                for sm in range(max_possible + 1):
                    val = dp_tight_0[sm]
                    if val:
                        for dig in range(10):
                            ns = sm + dig
                            ndp0[ns] = (ndp0[ns] + val) % MOD

                # From tight = 1: digit 0..lim
                for sm in range(max_possible + 1):
                    val = dp_tight_1[sm]
                    if not val:
                        continue
                    for dig in range(lim + 1):
                        ns = sm + dig
                        if dig == lim:
                            ndp1[ns] = (ndp1[ns] + val) % MOD
                        else:
                            ndp0[ns] = (ndp0[ns] + val) % MOD

                dp_tight_0, dp_tight_1 = ndp0, ndp1

            # Combine tight states: count in [0, s]
            res = [0] * (max_possible + 1)
            for sm in range(max_possible + 1):
                res[sm] = (dp_tight_0[sm] + dp_tight_1[sm]) % MOD
            return res

        def dec_one(s: str) -> str:
            # s represents a positive integer string; returns max(s-1, 0) as string.
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = chr(ord(arr[i]) - 1)
            # strip leading zeros
            t = ''.join(arr).lstrip('0')
            return t if t else "0"

        def count_leq(s: str) -> int:
            if s == "0":
                # only x=0
                return 1 if min_sum <= 0 <= max_sum else 0
            ways = digit_sum_up_to(s)
            lo, hi = min_sum, max_sum
            lo = max(lo, 0)
            hi = min(hi, len(ways) - 1)
            if lo > hi:
                return 0
            ans = 0
            for sm in range(lo, hi + 1):
                ans = (ans + ways[sm]) % MOD
            return ans

        upper = count_leq(num2)
        lower_num = dec_one(num1)
        lower = count_leq(lower_num)
        return (upper - lower) % MOD
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # s is positive numeric string; return max(s-1, 0) as string
            if s == "0":
                return "0"
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            res = ''.join(arr).lstrip('0')
            return res if res else "0"

        def count_upto(bound: str) -> int:
            # Count x in [0, bound] such that digit_sum(x) in [min_sum, max_sum]
            if bound == "0":
                return 0 if not (min_sum <= 0 <= max_sum) else 1

            digits = list(map(int, bound))
            n = len(digits)
            # dp[pos][sum][tight]
            # We'll do iterative DP with only two layers for tight states.
            # Initialize: at pos 0, tight=1, sum=0
            maxS = max_sum
            dp_tight = [0] * (maxS + 1)
            dp_loose = [0] * (maxS + 1)
            dp_tight[0] = 1

            for pos in range(n):
                ndp_tight = [0] * (maxS + 1)
                ndp_loose = [0] * (maxS + 1)
                limit = digits[pos]

                # Transitions from tight
                for ssum in range(maxS + 1):
                    ways = dp_tight[ssum]
                    if ways == 0:
                        continue
                    # choose digit d
                    for d in range(limit + 1):
                        ns = ssum + d
                        if ns > maxS:
                            continue
                        if d == limit:
                            ndp_tight[ns] = (ndp_tight[ns] + ways) % MOD
                        else:
                            ndp_loose[ns] = (ndp_loose[ns] + ways) % MOD

                # Transitions from loose
                for ssum in range(maxS + 1):
                    ways = dp_loose[ssum]
                    if ways == 0:
                        continue
                    for d in range(10):
                        ns = ssum + d
                        if ns > maxS:
                            continue
                        ndp_loose[ns] = (ndp_loose[ns] + ways) % MOD

                dp_tight, dp_loose = ndp_tight, ndp_loose

            ans = 0
            for ssum in range(min_sum, max_sum + 1):
                if ssum <= maxS:
                    ans = (ans + dp_tight[ssum] + dp_loose[ssum]) % MOD
            return ans

        ans2 = count_upto(num2)
        nm1 = dec_str(num1)
        ans1 = count_upto(nm1)
        return (ans2 - ans1) % MOD
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # s is positive integer string
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            j = 0
            while j < len(a) and a[j] == '0':
                j += 1
            return "".join(a[j:]) if j < len(a) else "0"

        def count_upto(upper: str) -> int:
            # count x in [0, upper] with min_sum<=digit_sum(x)<=max_sum
            # If upper == "0", digit sum is 0 (won't count unless min_sum==0, but min_sum>=1)
            if upper == "0":
                return 0

            # DP over digits: position, tight, sum
            digits = list(map(int, upper))
            n = len(digits)

            # dp_tight0[s], dp_tight1[s] for current position
            dp0 = [0] * (max_sum + 1)  # tight = 0
            dp1 = [0] * (max_sum + 1)  # tight = 1
            dp1[0] = 1

            for pos in range(n):
                ndp0 = [0] * (max_sum + 1)
                ndp1 = [0] * (max_sum + 1)

                limit = digits[pos]
                for s in range(max_sum + 1):
                    v1 = dp1[s]
                    if v1:
                        # choose digit d
                        for d in range(0, limit + 1):
                            ns = s + d
                            if ns > max_sum:
                                break
                            if d == limit:
                                ndp1[ns] = (ndp1[ns] + v1) % MOD
                            else:
                                ndp0[ns] = (ndp0[ns] + v1) % MOD

                    v0 = dp0[s]
                    if v0:
                        # tight=0 -> any digit 0..9
                        for d in range(10):
                            ns = s + d
                            if ns > max_sum:
                                break
                            ndp0[ns] = (ndp0[ns] + v0) % MOD

                dp0, dp1 = ndp0, ndp1

            ans = 0
            for s in range(min_sum, max_sum + 1):
                ans = (ans + dp0[s] + dp1[s]) % MOD
            return ans

        # Answer = count_upto(num2) - count_upto(num1-1)
        low = dec_str(num1)
        res = (count_upto(num2) - count_upto(low)) % MOD
        return res
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_one(s: str) -> str:
            # returns max(s-1, 0) as string without leading zeros (unless "0")
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i < 0:
                return "0"
            a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digit_sum_count_upto(bound: str) -> int:
            # count x in [0, bound] with digit sum in [min_sum, max_sum]
            if bound == "0":
                # digit sum(0)=0, but min_sum>=1 by constraints
                return 0

            digits = list(map(int, bound))
            n = len(digits)

            # If min_sum..max_sum outside possible range, early return
            if min_sum > 9 * n or max_sum < 0:
                return 0
            lo = max(min_sum, 0)
            hi = min(max_sum, 9 * n)

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, s: int) -> int:
                # started==0 means all previous digits were 0 (we haven't placed any non-leading digit)
                # digit sum counts only digits placed after started (i.e., leading zeros don't add)
                if s > hi:
                    return 0
                if pos == n:
                    # x=0 has started==0 and sum==0
                    if started == 0:
                        return 1 if (lo <= 0 <= hi) else 0
                    return 1 if (lo <= s <= hi) else 0

                limit = digits[pos] if tight else 9
                ans = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    nstarted = started or (d != 0)
                    ns = s + d if nstarted else 0
                    ans += dp(pos + 1, ntight, nstarted, ns)
                return ans % MOD

            return dp(0, 1, 0, 0)

        # count in [0, num2] minus count in [0, num1-1]
        num1m1 = dec_one(num1)
        return (digit_sum_count_upto(num2) - digit_sum_count_upto(num1m1)) % MOD
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def add_one_str(s: str) -> str:
            a = list(s)
            i = len(a) - 1
            carry = 1
            while i >= 0 and carry:
                d = ord(a[i]) - 48
                d += carry
                if d == 10:
                    a[i] = '0'
                    carry = 1
                else:
                    a[i] = chr(48 + d)
                    carry = 0
                i -= 1
            if carry:
                a.insert(0, '1')
            # strip leading zeros if any (shouldn't happen)
            return ''.join(a).lstrip('0') or "0"

        def dec_one_str(s: str) -> str:
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            borrow = 1
            while i >= 0 and borrow:
                d = ord(a[i]) - 48
                if d >= borrow:
                    d -= borrow
                    a[i] = chr(48 + d)
                    borrow = 0
                else:
                    d = d + 10 - borrow
                    a[i] = chr(48 + d)
                    borrow = 1
                i -= 1
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digit_dp_upto(bound: str) -> int:
            """
            Count x in [0, bound] such that digit_sum(x) in [min_sum, max_sum].
            """
            if bound == "0":
                return 1 if min_sum <= 0 <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)
            # dp[pos][tight][sum] -> count
            # We'll use rolling arrays for pos.
            maxS = max_sum
            # initialize
            from collections import defaultdict

            # Use list-of-dicts for speed; sum range <= 400.
            dp_tight0 = [0] * (maxS + 1)  # tight==0
            dp_tight1 = [0] * (maxS + 1)  # tight==1
            dp_tight1[0] = 1

            for pos in range(n):
                ndp_tight0 = [0] * (maxS + 1)
                ndp_tight1 = [0] * (maxS + 1)
                lim = digits[pos]

                # From tight==0: upper digit always 9
                # Transition to tight==0 always
                for s_val in range(0, maxS + 1):
                    cnt = dp_tight0[s_val]
                    if not cnt:
                        continue
                    base = s_val
                    # add digit 0..9
                    # shift counts by digit
                    for dig in range(10):
                        ns = base + dig
                        if ns <= maxS:
                            ndp_tight0[ns] = (ndp_tight0[ns] + cnt) % MOD

                # From tight==1: upper digit constrained by lim
                for s_val in range(0, maxS + 1):
                    cnt = dp_tight1[s_val]
                    if not cnt:
                        continue
                    base = s_val
                    for dig in range(lim + 1):
                        ns = base + dig
                        if ns > maxS:
                            continue
                        if dig == lim:
                            ndp_tight1[ns] = (ndp_tight1[ns] + cnt) % MOD
                        else:
                            ndp_tight0[ns] = (ndp_tight0[ns] + cnt) % MOD

                dp_tight0, dp_tight1 = ndp_tight0, ndp_tight1

            ans = 0
            for s_val in range(min_sum, max_sum + 1):
                ans = (ans + dp_tight0[s_val] + dp_tight1[s_val]) % MOD
            return ans

        # Count in [0, num2] - count in [0, num1-1]
        num1m1 = dec_one_str(num1)
        res2 = digit_dp_upto(num2)
        res1 = digit_dp_upto(num1m1) if num1m1 != "0" or min_sum <= 0 <= max_sum else digit_dp_upto(num1m1)
        # Note: digit_dp_upto handles "0" correctly anyway.
        return (res2 - res1) % MOD
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    MOD = 10**9 + 7

    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # digit DP: count numbers in [0..N] with digit sum in [min_sum..max_sum]
        def count_upto(N: str) -> int:
            digits = list(map(int, N))
            L = len(digits)

            # dp[pos][tight] = array over sums
            # We'll store only for current pos to save memory.
            # dp_tight[s] for tight=1, dp_loose[s] for tight=0
            # tight means prefix equals N so far; loose means already smaller.
            dp_loose = [0] * (max_sum + 1)  # loose at current pos
            dp_tight = [0] * (max_sum + 1)  # tight at current pos

            # start: before placing any digits, sum=0
            dp_tight[0] = 1

            for pos in range(L):
                ndp_loose = [0] * (max_sum + 1)
                ndp_tight = [0] * (max_sum + 1)
                limit = digits[pos]

                # Transition for loose states: can put digits 0..9 always, remains loose
                for s in range(max_sum + 1):
                    ways = dp_loose[s]
                    if not ways:
                        continue
                    for d in range(10):
                        ns = s + d
                        if ns <= max_sum:
                            ndp_loose[ns] = (ndp_loose[ns] + ways) % self.MOD

                # Transition for tight states
                for s in range(max_sum + 1):
                    ways = dp_tight[s]
                    if not ways:
                        continue
                    for d in range(limit + 1):
                        ns = s + d
                        if ns > max_sum:
                            continue
                        if d == limit:
                            ndp_tight[ns] = (ndp_tight[ns] + ways) % self.MOD
                        else:
                            ndp_loose[ns] = (ndp_loose[ns] + ways) % self.MOD

                dp_loose, dp_tight = ndp_loose, ndp_tight

            # Sum counts for sums in [min_sum..max_sum], excluding leading-zero issue:
            # The DP counts numbers from 0..N including 0 with digit sum 0.
            # Since min_sum >= 1, excluding 0 is automatic.
            ans = 0
            for s in range(min_sum, max_sum + 1):
                ans = (ans + dp_loose[s] + dp_tight[s]) % self.MOD
            return ans

        def dec_one_str(s: str) -> str:
            # returns (s - 1) as string, assuming s represents an integer >= 1
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        # Answer = count_upto(num2) - count_upto(num1-1)
        left = dec_one_str(num1)
        right_count = count_upto(num2)
        left_count = 0 if left == "0" else count_upto(left)

        return (right_count - left_count) % self.MOD
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def add_one_str(s: str) -> str:
            # not used
            return s

        def dec_str(s: str) -> str:
            # s is positive integer string without leading zeros
            if s == "0":
                return "0"
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            out = ''.join(arr).lstrip('0')
            return out if out else "0"

        def count_upto(limit: str) -> int:
            # count x in [0, limit] with min_sum<=digit_sum(x)<=max_sum
            if limit == "0":
                total = 0
                ds = 0
                if min_sum <= ds <= max_sum:
                    total = 1
                return total

            digits = list(map(int, limit))
            n = len(digits)

            # dp[pos][tight][sum] -> ways
            # Use rolling arrays over sum and tight
            # Initialize at pos=0
            dp_tight = [0] * (max_sum + 1)  # ways with tight=True at this pos
            dp_loose = [0] * (max_sum + 1) # ways with tight=False at this pos
            dp_tight[0] = 1

            for pos in range(n):
                new_tight = [0] * (max_sum + 1)
                new_loose = [0] * (max_sum + 1)
                cur = digits[pos]
                for ssum in range(max_sum + 1):
                    # From tight state
                    w = dp_tight[ssum]
                    if w:
                        for d in range(cur + 1):
                            ns = ssum + d
                            if ns > max_sum:
                                continue
                            if d == cur:
                                new_tight[ns] = (new_tight[ns] + w) % MOD
                            else:
                                new_loose[ns] = (new_loose[ns] + w) % MOD
                    # From loose state
                    w2 = dp_loose[ssum]
                    if w2:
                        for d in range(10):
                            ns = ssum + d
                            if ns > max_sum:
                                continue
                            new_loose[ns] = (new_loose[ns] + w2) % MOD

                dp_tight, dp_loose = new_tight, new_loose

            ans = 0
            for ssum in range(min_sum, max_sum + 1):
                ans = (ans + dp_tight[ssum] + dp_loose[ssum]) % MOD
            return ans

        def mod_sub(a, b):
            return (a - b) % MOD

        # Count in [num1, num2] = count_upto(num2) - count_upto(num1-1)
        num1_minus = dec_str(num1)  # if num1=="1", gives "0"
        res = mod_sub(count_upto(num2), count_upto(num1_minus))
        return res % MOD
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def count_leq(s: str) -> int:
            # Count x in [0, s] such that digit_sum(x) in [min_sum, max_sum]
            # (Leading zeros allowed; then exclude x=0 by zero-sum handling via min_sum>=1)
            n = len(s)
            digits = list(map(int, s))

            dp = [0] * (max_sum + 1)
            dp[0] = 1  # no digits processed, sum=0

            tight_states = dp[:]  # dp for tight=1 at start: only sum 0 has 1 way
            # We'll use standard DP with tight flag:
            # dp_tight[sum] for tight=1; dp_loose[sum] for tight=0
            dp_tight = [0] * (max_sum + 1)
            dp_loose = [0] * (max_sum + 1)
            dp_tight[0] = 1

            for i in range(n):
                ndp_tight = [0] * (max_sum + 1)
                ndp_loose = [0] * (max_sum + 1)
                limit = digits[i]

                # transitions from tight
                for sm in range(max_sum + 1):
                    ways = dp_tight[sm]
                    if not ways:
                        continue
                    # choose digit d
                    for d in range(limit + 1):
                        nsm = sm + d
                        if nsm > max_sum:
                            continue
                        if d == limit:
                            ndp_tight[nsm] = (ndp_tight[nsm] + ways) % MOD
                        else:
                            ndp_loose[nsm] = (ndp_loose[nsm] + ways) % MOD

                # transitions from loose: digit can be 0..9
                for sm in range(max_sum + 1):
                    ways = dp_loose[sm]
                    if not ways:
                        continue
                    for d in range(10):
                        nsm = sm + d
                        if nsm > max_sum:
                            continue
                        ndp_loose[nsm] = (ndp_loose[nsm] + ways) % MOD

                dp_tight, dp_loose = ndp_tight, ndp_loose

            ans = 0
            for sm in range(min_sum, max_sum + 1):
                ans = (ans + dp_tight[sm] + dp_loose[sm]) % MOD
            # min_sum >= 1 in constraints, so x=0 (sum=0) is naturally excluded
            return ans

        def dec_one(s: str) -> str:
            # return string for (int(s) - 1), assuming s represents a positive integer
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            res = ''.join(arr).lstrip('0')
            return res if res else "0"

        res2 = count_leq(num2)
        # count_leq(num1 - 1)
        if num1 == "0":
            res1 = 0
        else:
            prev = dec_one(num1)
            res1 = count_leq(prev) if prev != "0" else 0

        return (res2 - res1) % MOD
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # decrement a non-negative integer string >= "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            j = 0
            while j < len(a) - 1 and a[j] == '0':
                j += 1
            return ''.join(a[j:])

        def add_leading_zeroes(s: str, n: int) -> str:
            return s.rjust(n, '0')

        def count_upto(bound: str) -> int:
            # Count x in [0, bound] with digit sum in [min_sum, max_sum]
            if bound == "0":
                return 1 if min_sum <= 0 <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)

            # dp[pos][sum][tight] where tight in {0,1}
            # Use rolling arrays: dp_sum_tight[sum][tight]
            maxS = max_sum
            dp = [[0, 0] for _ in range(maxS + 1)]
            dp[0][1] = 1  # pos=0, sum=0, tight=1 initially

            for pos in range(n):
                new = [[0, 0] for _ in range(maxS + 1)]
                limit = digits[pos]
                for ssum in range(maxS + 1):
                    for tight in (0, 1):
                        ways = dp[ssum][tight]
                        if ways == 0:
                            continue
                        up = limit if tight == 1 else 9
                        for d in range(up + 1):
                            ns = ssum + d
                            if ns > maxS:
                                continue
                            ntight = 1 if (tight == 1 and d == up) else 0
                            new[ns][ntight] = (new[ns][ntight] + ways) % MOD
                dp = new

            ans = 0
            for ssum in range(min_sum, max_sum + 1):
                ans = (ans + dp[ssum][0] + dp[ssum][1]) % MOD
            return ans

        # Result = count <= num2 - count <= (num1 - 1)
        if num1 == "0":
            return count_upto(num2)

        num1m1 = dec_str(num1)
        return (count_upto(num2) - count_upto(num1m1)) % MOD
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_one(s: str) -> str:
            # returns max(s-1, 0) as string
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digits_of(n: str):
            return list(map(int, n))

        def count_upto(n: str) -> int:
            # count x in [0, n] with digit sum in [min_sum, max_sum]
            if n == "0":
                return 0 if not (min_sum <= 0 <= max_sum) else 1

            ds = digits_of(n)
            L = len(ds)

            # dp[pos][sum] where pos processed left->right, tight handling via two layers
            # Use rolling arrays for tight=0/1
            maxS = max_sum
            # dp_tight: sum -> ways
            dp_tight = [0] * (maxS + 1)
            dp_loose = [0] * (maxS + 1)
            dp_tight[0] = 1

            for pos in range(L):
                ndp_tight = [0] * (maxS + 1)
                ndp_loose = [0] * (maxS + 1)
                limit = ds[pos]

                # transition from tight
                for ssum in range(maxS + 1):
                    ways = dp_tight[ssum]
                    if not ways:
                        continue
                    for dig in range(limit + 1):
                        ns = ssum + dig
                        if ns > maxS:
                            break
                        if dig == limit:
                            ndp_tight[ns] = (ndp_tight[ns] + ways) % MOD
                        else:
                            ndp_loose[ns] = (ndp_loose[ns] + ways) % MOD

                # transition from loose (already less, so any digit 0..9)
                for ssum in range(maxS + 1):
                    ways = dp_loose[ssum]
                    if not ways:
                        continue
                    for dig in range(10):
                        ns = ssum + dig
                        if ns > maxS:
                            break
                        ndp_loose[ns] = (ndp_loose[ns] + ways) % MOD

                dp_tight, dp_loose = ndp_tight, ndp_loose

            total = 0
            for ssum in range(min_sum, max_sum + 1):
                total = (total + dp_tight[ssum] + dp_loose[ssum]) % MOD
            return total

        upper = count_upto(num2)
        lower_bound = dec_one(num1)
        lower = count_upto(lower_bound)

        ans = (upper - lower) % MOD
        return ans
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def digit_sum_up_to(s: str):
            """
            Returns dp[s][k]? -> Actually returns list ways[k] = count of integers in [0, s]
            with digit sum exactly k. Includes x=0 (digit sum 0).
            """
            digits = list(map(int, s))
            n = len(digits)

            # dp[pos][sum][tight]
            # We'll use rolling arrays: dp_tight for each sum.
            max_possible = 9 * n
            dp_tight_0 = [0] * (max_possible + 1)  # tight = 0 (already less)
            dp_tight_1 = [0] * (max_possible + 1)  # tight = 1 (equal so far)
            dp_tight_1[0] = 1

            for i in range(n):
                ndp0 = [0] * (max_possible + 1)
                ndp1 = [0] * (max_possible + 1)
                lim = digits[i]

                # From tight = 0: next digit can be 0..9, remains tight = 0
                for sm in range(max_possible + 1):
                    val = dp_tight_0[sm]
                    if val:
                        for dig in range(10):
                            ns = sm + dig
                            ndp0[ns] = (ndp0[ns] + val) % MOD

                # From tight = 1: digit 0..lim
                for sm in range(max_possible + 1):
                    val = dp_tight_1[sm]
                    if not val:
                        continue
                    for dig in range(lim + 1):
                        ns = sm + dig
                        if dig == lim:
                            ndp1[ns] = (ndp1[ns] + val) % MOD
                        else:
                            ndp0[ns] = (ndp0[ns] + val) % MOD

                dp_tight_0, dp_tight_1 = ndp0, ndp1

            # Combine tight states: count in [0, s]
            res = [0] * (max_possible + 1)
            for sm in range(max_possible + 1):
                res[sm] = (dp_tight_0[sm] + dp_tight_1[sm]) % MOD
            return res

        def dec_one(s: str) -> str:
            # s represents a positive integer string; returns max(s-1, 0) as string.
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = chr(ord(arr[i]) - 1)
            # strip leading zeros
            t = ''.join(arr).lstrip('0')
            return t if t else "0"

        def count_leq(s: str) -> int:
            if s == "0":
                # only x=0
                return 1 if min_sum <= 0 <= max_sum else 0
            ways = digit_sum_up_to(s)
            lo, hi = min_sum, max_sum
            lo = max(lo, 0)
            hi = min(hi, len(ways) - 1)
            if lo > hi:
                return 0
            ans = 0
            for sm in range(lo, hi + 1):
                ans = (ans + ways[sm]) % MOD
            return ans

        upper = count_leq(num2)
        lower_num = dec_one(num1)
        lower = count_leq(lower_num)
        return (upper - lower) % MOD
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # s is positive numeric string; return max(s-1, 0) as string
            if s == "0":
                return "0"
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            res = ''.join(arr).lstrip('0')
            return res if res else "0"

        def count_upto(bound: str) -> int:
            # Count x in [0, bound] such that digit_sum(x) in [min_sum, max_sum]
            if bound == "0":
                return 0 if not (min_sum <= 0 <= max_sum) else 1

            digits = list(map(int, bound))
            n = len(digits)
            # dp[pos][sum][tight]
            # We'll do iterative DP with only two layers for tight states.
            # Initialize: at pos 0, tight=1, sum=0
            maxS = max_sum
            dp_tight = [0] * (maxS + 1)
            dp_loose = [0] * (maxS + 1)
            dp_tight[0] = 1

            for pos in range(n):
                ndp_tight = [0] * (maxS + 1)
                ndp_loose = [0] * (maxS + 1)
                limit = digits[pos]

                # Transitions from tight
                for ssum in range(maxS + 1):
                    ways = dp_tight[ssum]
                    if ways == 0:
                        continue
                    # choose digit d
                    for d in range(limit + 1):
                        ns = ssum + d
                        if ns > maxS:
                            continue
                        if d == limit:
                            ndp_tight[ns] = (ndp_tight[ns] + ways) % MOD
                        else:
                            ndp_loose[ns] = (ndp_loose[ns] + ways) % MOD

                # Transitions from loose
                for ssum in range(maxS + 1):
                    ways = dp_loose[ssum]
                    if ways == 0:
                        continue
                    for d in range(10):
                        ns = ssum + d
                        if ns > maxS:
                            continue
                        ndp_loose[ns] = (ndp_loose[ns] + ways) % MOD

                dp_tight, dp_loose = ndp_tight, ndp_loose

            ans = 0
            for ssum in range(min_sum, max_sum + 1):
                if ssum <= maxS:
                    ans = (ans + dp_tight[ssum] + dp_loose[ssum]) % MOD
            return ans

        ans2 = count_upto(num2)
        nm1 = dec_str(num1)
        ans1 = count_upto(nm1)
        return (ans2 - ans1) % MOD
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # s is positive integer string
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            j = 0
            while j < len(a) and a[j] == '0':
                j += 1
            return "".join(a[j:]) if j < len(a) else "0"

        def count_upto(upper: str) -> int:
            # count x in [0, upper] with min_sum<=digit_sum(x)<=max_sum
            # If upper == "0", digit sum is 0 (won't count unless min_sum==0, but min_sum>=1)
            if upper == "0":
                return 0

            # DP over digits: position, tight, sum
            digits = list(map(int, upper))
            n = len(digits)

            # dp_tight0[s], dp_tight1[s] for current position
            dp0 = [0] * (max_sum + 1)  # tight = 0
            dp1 = [0] * (max_sum + 1)  # tight = 1
            dp1[0] = 1

            for pos in range(n):
                ndp0 = [0] * (max_sum + 1)
                ndp1 = [0] * (max_sum + 1)

                limit = digits[pos]
                for s in range(max_sum + 1):
                    v1 = dp1[s]
                    if v1:
                        # choose digit d
                        for d in range(0, limit + 1):
                            ns = s + d
                            if ns > max_sum:
                                break
                            if d == limit:
                                ndp1[ns] = (ndp1[ns] + v1) % MOD
                            else:
                                ndp0[ns] = (ndp0[ns] + v1) % MOD

                    v0 = dp0[s]
                    if v0:
                        # tight=0 -> any digit 0..9
                        for d in range(10):
                            ns = s + d
                            if ns > max_sum:
                                break
                            ndp0[ns] = (ndp0[ns] + v0) % MOD

                dp0, dp1 = ndp0, ndp1

            ans = 0
            for s in range(min_sum, max_sum + 1):
                ans = (ans + dp0[s] + dp1[s]) % MOD
            return ans

        # Answer = count_upto(num2) - count_upto(num1-1)
        low = dec_str(num1)
        res = (count_upto(num2) - count_upto(low)) % MOD
        return res
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_one(s: str) -> str:
            # returns max(s-1, 0) as string without leading zeros (unless "0")
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i < 0:
                return "0"
            a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digit_sum_count_upto(bound: str) -> int:
            # count x in [0, bound] with digit sum in [min_sum, max_sum]
            if bound == "0":
                # digit sum(0)=0, but min_sum>=1 by constraints
                return 0

            digits = list(map(int, bound))
            n = len(digits)

            # If min_sum..max_sum outside possible range, early return
            if min_sum > 9 * n or max_sum < 0:
                return 0
            lo = max(min_sum, 0)
            hi = min(max_sum, 9 * n)

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, s: int) -> int:
                # started==0 means all previous digits were 0 (we haven't placed any non-leading digit)
                # digit sum counts only digits placed after started (i.e., leading zeros don't add)
                if s > hi:
                    return 0
                if pos == n:
                    # x=0 has started==0 and sum==0
                    if started == 0:
                        return 1 if (lo <= 0 <= hi) else 0
                    return 1 if (lo <= s <= hi) else 0

                limit = digits[pos] if tight else 9
                ans = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    nstarted = started or (d != 0)
                    ns = s + d if nstarted else 0
                    ans += dp(pos + 1, ntight, nstarted, ns)
                return ans % MOD

            return dp(0, 1, 0, 0)

        # count in [0, num2] minus count in [0, num1-1]
        num1m1 = dec_one(num1)
        return (digit_sum_count_upto(num2) - digit_sum_count_upto(num1m1)) % MOD
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
You are given two numeric strings num1 and num2 and two integers max_sum and min_sum. We denote an integer x to be good if:

num1 <= x <= num2
min_sum <= digit_sum(x) <= max_sum.

Return the number of good integers. Since the answer may be large, return it modulo 10^9 + 7.
Note that digit_sum(x) denotes the sum of the digits of x.
 
Example 1:

Input: num1 = "1", num2 = "12", min_sum = 1, max_sum = 8
Output: 11
Explanation: There are 11 integers whose sum of digits lies between 1 and 8 are 1,2,3,4,5,6,7,8,10,11, and 12. Thus, we return 11.

Example 2:

Input: num1 = "1", num2 = "5", min_sum = 1, max_sum = 5
Output: 5
Explanation: The 5 integers whose sum of digits lies between 1 and 5 are 1,2,3,4, and 5. Thus, we return 5.

 
Constraints:

1 <= num1 <= num2 <= 10^22
1 <= min_sum <= max_sum <= 400

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_one(s: str) -> str:
            # s >= "0"
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digit_sum_count_upto(bound: str) -> int:
            """
            Counts x in [0, bound] with digit_sum in [min_sum, max_sum].
            """
            if bound == "0":
                # Only x=0; digit_sum(0)=0
                return 0 if not (min_sum <= 0 <= max_sum) else 1

            digits = list(map(int, bound))
            n = len(digits)
            pref = digits

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, s: int) -> int:
                """
                pos: current index
                tight: whether prefix equals bound so far (1) or already smaller (0)
                started: whether we've placed a non-leading digit yet (1) else still leading zeros (0)
                s: current digit sum accumulated (only counts digits after started==1)
                """
                if s > max_sum:
                    return 0
                if pos == n:
                    if not started:
                        # x=0
                        return 1 if min_sum <= 0 <= max_sum else 0
                    return 1 if min_sum <= s <= max_sum else 0

                limit = pref[pos] if tight else 9
                total = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0  # careful: limit changes with tight
                    # We should compute ntight properly:
                    # Condition: tight==1 and d == pref[pos]
                    ntight = 1 if (tight == 1 and d == pref[pos]) else 0

                    nstarted = started or (d != 0)
                    ns = s + d if nstarted else 0
                    total = (total + dp(pos + 1, ntight, 1 if nstarted else 0, ns)) % MOD
                return total

            return dp(0, 1, 0, 0)

        # Answer = count in [0, num2] - count in [0, num1-1]
        num1_minus = dec_one(num1)
        ans2 = digit_sum_count_upto(num2)
        ans1 = digit_sum_count_upto(num1_minus)
        return (ans2 - ans1) % MOD
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def count_upto(s: str) -> int:
            # count of x in [0, s] with digit sum in [min_sum, max_sum]
            n = len(s)
            digits = list(map(int, s))

            # dp[pos][sum][tight] -> ways
            # We'll roll over pos to save memory
            maxS = max_sum
            # dp_tight: sums for tight=0 and tight=1 for current position
            dp0 = [0] * (maxS + 1)  # not tight
            dp1 = [0] * (maxS + 1)  # tight
            dp1[0] = 1  # at pos 0, sum=0, tight=True

            for i in range(n):
                ndp0 = [0] * (maxS + 1)
                ndp1 = [0] * (maxS + 1)

                limit = digits[i]
                for sm in range(maxS + 1):
                    if dp0[sm]:
                        ways = dp0[sm]
                        # from not tight, next digit can be 0..9, stays not tight
                        for d in range(10):
                            if sm + d <= maxS:
                                ndp0[sm + d] = (ndp0[sm + d] + ways) % MOD

                    if dp1[sm]:
                        ways = dp1[sm]
                        # from tight, next digit 0..limit
                        for d in range(limit + 1):
                            if sm + d > maxS:
                                break
                            if d == limit:
                                ndp1[sm + d] = (ndp1[sm + d] + ways) % MOD
                            else:
                                ndp0[sm + d] = (ndp0[sm + d] + ways) % MOD

                dp0, dp1 = ndp0, ndp1

            res = 0
            for sm in range(min_sum, max_sum + 1):
                res = (res + dp0[sm] + dp1[sm]) % MOD
            return res

        def dec_one(s: str) -> str:
            # return string for (s - 1), where s is positive numeric string
            if s == "0":
                return "-1"
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            j = 0
            while j < len(arr) - 1 and arr[j] == '0':
                j += 1
            return ''.join(arr[j:])

        # Answer = count_upto(num2) - count_upto(num1 - 1), mod MOD
        num1m1 = dec_one(num1)
        if num1m1 == "-1":
            return count_upto(num2)

        ans = (count_upto(num2) - count_upto(num1m1)) % MOD
        return ans
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_one(s: str) -> str:
            # s is a positive integer string (no leading zeros)
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = str(int(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digit_dp_upto(bound: str) -> int:
            """
            Count x in [0, bound] such that digit_sum(x) in [min_sum, max_sum].
            """
            if bound == "0":
                # only x=0 is included; digit_sum(0)=0
                return 1 if min_sum <= 0 <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)

            @lru_cache(None)
            def dp(pos: int, tight: int, ssum: int) -> int:
                if ssum > max_sum:
                    return 0
                if pos == n:
                    return 1 if min_sum <= ssum <= max_sum else 0
                limit = digits[pos] if tight else 9
                total = 0
                ntight = tight
                for d in range(limit + 1):
                    total += dp(pos + 1, 1 if (tight and d == limit) else 0, ssum + d)
                return total % MOD

            return dp(0, 1, 0)

        # Count up to num2 minus count up to num1-1
        num1_minus_1 = dec_one(num1)
        ans = (digit_dp_upto(num2) - digit_dp_upto(num1_minus_1)) % MOD
        return ans
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_one(s: str) -> str:
            # assumes s represents a positive integer
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            res = ''.join(arr).lstrip('0')
            return res if res else "0"

        def count_upto(bound: str) -> int:
            # counts x in [0, bound] with min_sum <= digit_sum(x) <= max_sum
            if bound == "0":
                return 1 if min_sum <= 0 <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, sm: int) -> int:
                # started: 0 if no non-leading digit chosen yet; 1 otherwise
                if sm > max_sum:
                    return 0
                if pos == n:
                    if not started:
                        total_sum = 0
                    else:
                        total_sum = sm
                    return 1 if min_sum <= total_sum <= max_sum else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    if started == 0 and d == 0:
                        # still not started: sum stays 0
                        res += dp(pos + 1, ntight, 0, sm)
                    else:
                        res += dp(pos + 1, ntight, 1, sm + d)
                    if res >= 1 << 63:  # avoid huge Python ints occasionally
                        res %= MOD
                return res % MOD

            return dp(0, 1, 0, 0)

        lower = num1
        if lower == "0":
            cnt_low = 0
        else:
            lower = dec_one(lower)
            cnt_low = count_upto(lower) if lower != "0" else (1 if min_sum <= 0 <= max_sum else 0)

        cnt_high = count_upto(num2)
        return (cnt_high - cnt_low) % MOD
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec1(s: str) -> str:
            # returns (s - 1) as string, assuming s represents an integer >= 0
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i < 0:
                return "0"
            a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def count_upto(bound: str) -> int:
            # count x in [0, bound] with digit sum in [min_sum, max_sum]
            # using digit DP
            if bound == "0":
                ds = 0
                return 1 if min_sum <= ds <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)

            # dp[pos][sum][tight]
            # We'll roll over pos for memory.
            # sums up to max_sum only.
            dp = [[0] * (max_sum + 1) for _ in range(2)]
            dp[1][0] = 1  # tight=1 at start, sum=0

            for pos in range(n):
                ndp = [[0] * (max_sum + 1) for _ in range(2)]
                lim = digits[pos]
                for tight in (0, 1):
                    max_d = lim if tight == 1 else 9
                    cur = dp[tight]
                    for ssum in range(max_sum + 1):
                        ways = cur[ssum]
                        if not ways:
                            continue
                        for d in range(max_d + 1):
                            ns = ssum + d
                            if ns > max_sum:
                                continue
                            ntight = 1 if (tight == 1 and d == lim) else 0
                            ndp[ntight][ns] = (ndp[ntight][ns] + ways) % MOD
                dp = ndp

            ans = 0
            for tight in (0, 1):
                for ssum in range(min_sum, max_sum + 1):
                    ans = (ans + dp[tight][ssum]) % MOD
            return ans

        upper = count_upto(num2)
        lower_bound = dec1(num1)
        lower = count_upto(lower_bound) if lower_bound != "0" or min_sum <= 0 else 0
        # count [num1, num2] = upto(num2) - upto(num1-1)
        return (upper - lower) % MOD
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def digits_of(s: str):
            return list(map(int, s))

        def count_upto(s: str) -> int:
            """
            Count x in [0, s] such that digit_sum(x) in [min_sum, max_sum].
            Leading zeros are allowed in DP, and x=0 is included if its digit_sum=0 matches.
            """
            digs = digits_of(s)
            n = len(digs)

            # dp[pos][sum][tight]: use two layers to save memory
            # We'll use dp_sum_tight[sum][tight]
            from collections import defaultdict

            dp = [[0, 0] for _ in range(max_sum + 1)]  # sums 0..max_sum, tight=0/1
            dp[0][1] = 1  # at pos=0, sum=0, tight=true

            for pos in range(n):
                newdp = [[0, 0] for _ in range(max_sum + 1)]
                limit = digs[pos]
                for ssum in range(max_sum + 1):
                    for tight in (0, 1):
                        ways = dp[ssum][tight]
                        if ways == 0:
                            continue
                        max_digit = limit if tight == 1 else 9
                        for d in range(max_digit + 1):
                            ns = ssum + d
                            if ns > max_sum:
                                continue
                            ntight = 1 if (tight == 1 and d == max_digit) else 0
                            newdp[ns][ntight] = (newdp[ns][ntight] + ways) % MOD
                dp = newdp

            ans = 0
            for ssum in range(min_sum, max_sum + 1):
                ans = (ans + dp[ssum][0] + dp[ssum][1]) % MOD
            return ans

        def dec_str(s: str) -> str:
            """Return string of (s-1), assuming s represents a positive integer (>=1)."""
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # remove leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        # Count up to num2 minus count up to num1-1
        total = count_upto(num2)
        if num1 == "0":
            res = total
        else:
            num1m1 = dec_str(num1)
            res = (total - count_upto(num1m1)) % MOD
        return res
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # s represents a positive integer (no leading zeros except possibly "0")
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        from functools import lru_cache

        def count_upto(bound: str) -> int:
            # count x in [0, bound] with digit sum within [min_sum, max_sum]
            digits = list(map(int, bound))
            n = len(digits)

            @lru_cache(None)
            def dp(pos: int, tight: int, s: int) -> int:
                # pos: current index [0..n], tight: 1 if prefix equals bound
                if s > max_sum:
                    return 0
                if pos == n:
                    return 1 if min_sum <= s <= max_sum else 0
                limit = digits[pos] if tight else 9
                res = 0
                for d in range(limit + 1):
                    nt = 1 if (tight and d == limit) else 0
                    res += dp(pos + 1, nt, s + d)
                return res % MOD

            return dp(0, 1, 0)

        ans2 = count_upto(num2)
        num1_minus_1 = dec_str(num1)
        ans1 = count_upto(num1_minus_1) if num1_minus_1 != "0" else 0
        return (ans2 - ans1) % MOD
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # s >= "0"
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def count_upto(bound: str) -> int:
            # Count x in [0, bound] with digit sum in [min_sum, max_sum]
            if bound == "0":
                return 0 if not (min_sum <= 0 <= max_sum) else 1

            digits = list(map(int, bound))
            n = len(digits)

            # dp[pos][sum][tight] compressed to 2 layers and tight=0/1
            # dp for current prefix; sums clipped to max_sum
            prev_t0 = [0] * (max_sum + 1)  # tight=0
            prev_t1 = [0] * (max_sum + 1)  # tight=1
            prev_t1[0] = 1

            for pos in range(n):
                cur_t0 = [0] * (max_sum + 1)
                cur_t1 = [0] * (max_sum + 1)
                limit_digit = digits[pos]

                # From tight=0: next tight stays 0 and digit can be 0..9
                for s in range(max_sum + 1):
                    val = prev_t0[s]
                    if not val:
                        continue
                    for d in range(10):
                        ns = s + d
                        if ns > max_sum:
                            break
                        cur_t0[ns] = (cur_t0[ns] + val) % MOD

                # From tight=1: next digit 0..limit_digit
                for s in range(max_sum + 1):
                    val = prev_t1[s]
                    if not val:
                        continue
                    for d in range(limit_digit + 1):
                        ns = s + d
                        if ns > max_sum:
                            break
                        if d == limit_digit:
                            cur_t1[ns] = (cur_t1[ns] + val) % MOD
                        else:
                            cur_t0[ns] = (cur_t0[ns] + val) % MOD

                prev_t0, prev_t1 = cur_t0, cur_t1

            ans = 0
            for s in range(min_sum, max_sum + 1):
                ans = (ans + prev_t0[s] + prev_t1[s]) % MOD
            return ans

        # count in [num1, num2] = f(num2) - f(num1-1)
        num1_minus_1 = dec_str(num1)
        res = (count_upto(num2) - count_upto(num1_minus_1)) % MOD
        return res
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_str(s: str) -> str:
            # subtract 1 from a positive integer string (s >= "0")
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def count_leq(bound: str) -> int:
            # counts x in [0, bound] with min_sum <= digit_sum(x) <= max_sum
            if bound == "0":
                return 1 if (min_sum <= 0 <= max_sum) else 0

            digits = list(map(int, bound))
            n = len(digits)

            # Pre-sum bounds: sums can only be 0..9*n, but max_sum <= 400
            lo = min_sum
            hi = max_sum

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, ssum: int) -> int:
                # pos: current index, tight: whether prefix equals bound,
                # started: whether any non-leading digit has been placed,
                # ssum: current digit sum of the started part
                if pos == n:
                    return 1 if started and (lo <= ssum <= hi) else (1 if not started and lo <= 0 <= hi else 0)

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    ntight = 1 if (tight and d == limit) else 0  # careful: limit changes with tight; use equality with bound digit
                    # The above is incorrect because "limit" depends on tight. Fix:
                return res

            # Let's implement dp properly with correct tight handling
            digits = list(map(int, bound))
            n = len(digits)

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, ssum: int) -> int:
                if pos == n:
                    if started:
                        return 1 if lo <= ssum <= hi else 0
                    else:
                        return 1 if lo <= 0 <= hi else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0  # when tight, limit == digits[pos]
                    if started == 0 and d == 0:
                        res += dp(pos + 1, ntight, 0, ssum)
                    else:
                        ns = ssum + d
                        if ns <= hi:  # prune
                            res += dp(pos + 1, ntight, 1, ns)
                    res %= MOD
                return res

            return dp(0, 1, 0, 0)

        # Count [0, num2] - count [0, num1-1]
        num1m1 = dec_str(num1)
        ans = (count_leq(num2) - (count_leq(num1m1) if num1m1 != "0" or min_sum <= 0 <= max_sum else count_leq("0"))) % MOD
        # The subtraction above can be simplified, but keep it safe around "0".
        return ans
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        digits_cache = {}

        def digit_dp_le(s: str) -> int:
            """Count x in [0, s] with digit_sum in [min_sum, max_sum]."""
            if not s:
                return 0
            if s in digits_cache:
                return digits_cache[s]

            n = len(s)
            dp = [[0] * (max_sum + 1) for _ in range(n + 1)]
            dp[0][0] = 1

            for i in range(n):
                limit = int(s[i])
                new = [[0] * (max_sum + 1) for _ in range(n + 1)]
                # We'll use a standard tight/non-tight DP via two states:
                # tight=0 (already less), tight=1 (equal so far).
                # To keep memory small, we do iterative with two 1D arrays.
                # But easiest with two arrays for each sum.

            # Implement properly with tight flag:
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, tight: int, sm: int) -> int:
                if sm > max_sum:
                    return 0
                if pos == n:
                    return 1 if min_sum <= sm <= max_sum else 0
                lim = int(s[pos]) if tight else 9
                res = 0
                for d in range(lim + 1):
                    res += dfs(pos + 1, 1 if (tight and d == lim) else 0, sm + d)
                    if res >= MOD:
                        res -= MOD
                return res

            ans = dfs(0, 1, 0) % MOD
            digits_cache[s] = ans
            return ans

        def dec_one(s: str) -> str:
            """Return string for (int(s) - 1), assuming s represents positive integer."""
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = str(int(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        left = dec_one(num1) if num1 != "0" else "0"
        res = (digit_dp_le(num2) - digit_dp_le(left)) % MOD
        return res
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_one(s: str) -> str:
            # s >= "0"
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digit_sum_count_upto(bound: str) -> int:
            """
            Counts x in [0, bound] with digit_sum in [min_sum, max_sum].
            """
            if bound == "0":
                # Only x=0; digit_sum(0)=0
                return 0 if not (min_sum <= 0 <= max_sum) else 1

            digits = list(map(int, bound))
            n = len(digits)
            pref = digits

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, s: int) -> int:
                """
                pos: current index
                tight: whether prefix equals bound so far (1) or already smaller (0)
                started: whether we've placed a non-leading digit yet (1) else still leading zeros (0)
                s: current digit sum accumulated (only counts digits after started==1)
                """
                if s > max_sum:
                    return 0
                if pos == n:
                    if not started:
                        # x=0
                        return 1 if min_sum <= 0 <= max_sum else 0
                    return 1 if min_sum <= s <= max_sum else 0

                limit = pref[pos] if tight else 9
                total = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0  # careful: limit changes with tight
                    # We should compute ntight properly:
                    # Condition: tight==1 and d == pref[pos]
                    ntight = 1 if (tight == 1 and d == pref[pos]) else 0

                    nstarted = started or (d != 0)
                    ns = s + d if nstarted else 0
                    total = (total + dp(pos + 1, ntight, 1 if nstarted else 0, ns)) % MOD
                return total

            return dp(0, 1, 0, 0)

        # Answer = count in [0, num2] - count in [0, num1-1]
        num1_minus = dec_one(num1)
        ans2 = digit_sum_count_upto(num2)
        ans1 = digit_sum_count_upto(num1_minus)
        return (ans2 - ans1) % MOD
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def count_upto(s: str) -> int:
            # count of x in [0, s] with digit sum in [min_sum, max_sum]
            n = len(s)
            digits = list(map(int, s))

            # dp[pos][sum][tight] -> ways
            # We'll roll over pos to save memory
            maxS = max_sum
            # dp_tight: sums for tight=0 and tight=1 for current position
            dp0 = [0] * (maxS + 1)  # not tight
            dp1 = [0] * (maxS + 1)  # tight
            dp1[0] = 1  # at pos 0, sum=0, tight=True

            for i in range(n):
                ndp0 = [0] * (maxS + 1)
                ndp1 = [0] * (maxS + 1)

                limit = digits[i]
                for sm in range(maxS + 1):
                    if dp0[sm]:
                        ways = dp0[sm]
                        # from not tight, next digit can be 0..9, stays not tight
                        for d in range(10):
                            if sm + d <= maxS:
                                ndp0[sm + d] = (ndp0[sm + d] + ways) % MOD

                    if dp1[sm]:
                        ways = dp1[sm]
                        # from tight, next digit 0..limit
                        for d in range(limit + 1):
                            if sm + d > maxS:
                                break
                            if d == limit:
                                ndp1[sm + d] = (ndp1[sm + d] + ways) % MOD
                            else:
                                ndp0[sm + d] = (ndp0[sm + d] + ways) % MOD

                dp0, dp1 = ndp0, ndp1

            res = 0
            for sm in range(min_sum, max_sum + 1):
                res = (res + dp0[sm] + dp1[sm]) % MOD
            return res

        def dec_one(s: str) -> str:
            # return string for (s - 1), where s is positive numeric string
            if s == "0":
                return "-1"
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            j = 0
            while j < len(arr) - 1 and arr[j] == '0':
                j += 1
            return ''.join(arr[j:])

        # Answer = count_upto(num2) - count_upto(num1 - 1), mod MOD
        num1m1 = dec_one(num1)
        if num1m1 == "-1":
            return count_upto(num2)

        ans = (count_upto(num2) - count_upto(num1m1)) % MOD
        return ans
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_one(s: str) -> str:
            # s is a positive integer string (no leading zeros)
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = str(int(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def digit_dp_upto(bound: str) -> int:
            """
            Count x in [0, bound] such that digit_sum(x) in [min_sum, max_sum].
            """
            if bound == "0":
                # only x=0 is included; digit_sum(0)=0
                return 1 if min_sum <= 0 <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)

            @lru_cache(None)
            def dp(pos: int, tight: int, ssum: int) -> int:
                if ssum > max_sum:
                    return 0
                if pos == n:
                    return 1 if min_sum <= ssum <= max_sum else 0
                limit = digits[pos] if tight else 9
                total = 0
                ntight = tight
                for d in range(limit + 1):
                    total += dp(pos + 1, 1 if (tight and d == limit) else 0, ssum + d)
                return total % MOD

            return dp(0, 1, 0)

        # Count up to num2 minus count up to num1-1
        num1_minus_1 = dec_one(num1)
        ans = (digit_dp_upto(num2) - digit_dp_upto(num1_minus_1)) % MOD
        return ans
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_one(s: str) -> str:
            # assumes s represents a positive integer
            arr = list(s)
            i = len(arr) - 1
            while i >= 0 and arr[i] == '0':
                arr[i] = '9'
                i -= 1
            if i >= 0:
                arr[i] = str(int(arr[i]) - 1)
            # strip leading zeros
            res = ''.join(arr).lstrip('0')
            return res if res else "0"

        def count_upto(bound: str) -> int:
            # counts x in [0, bound] with min_sum <= digit_sum(x) <= max_sum
            if bound == "0":
                return 1 if min_sum <= 0 <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, sm: int) -> int:
                # started: 0 if no non-leading digit chosen yet; 1 otherwise
                if sm > max_sum:
                    return 0
                if pos == n:
                    if not started:
                        total_sum = 0
                    else:
                        total_sum = sm
                    return 1 if min_sum <= total_sum <= max_sum else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    if started == 0 and d == 0:
                        # still not started: sum stays 0
                        res += dp(pos + 1, ntight, 0, sm)
                    else:
                        res += dp(pos + 1, ntight, 1, sm + d)
                    if res >= 1 << 63:  # avoid huge Python ints occasionally
                        res %= MOD
                return res % MOD

            return dp(0, 1, 0, 0)

        lower = num1
        if lower == "0":
            cnt_low = 0
        else:
            lower = dec_one(lower)
            cnt_low = count_upto(lower) if lower != "0" else (1 if min_sum <= 0 <= max_sum else 0)

        cnt_high = count_upto(num2)
        return (cnt_high - cnt_low) % MOD
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec1(s: str) -> str:
            # returns (s - 1) as string, assuming s represents an integer >= 0
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i < 0:
                return "0"
            a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def count_upto(bound: str) -> int:
            # count x in [0, bound] with digit sum in [min_sum, max_sum]
            # using digit DP
            if bound == "0":
                ds = 0
                return 1 if min_sum <= ds <= max_sum else 0

            digits = list(map(int, bound))
            n = len(digits)

            # dp[pos][sum][tight]
            # We'll roll over pos for memory.
            # sums up to max_sum only.
            dp = [[0] * (max_sum + 1) for _ in range(2)]
            dp[1][0] = 1  # tight=1 at start, sum=0

            for pos in range(n):
                ndp = [[0] * (max_sum + 1) for _ in range(2)]
                lim = digits[pos]
                for tight in (0, 1):
                    max_d = lim if tight == 1 else 9
                    cur = dp[tight]
                    for ssum in range(max_sum + 1):
                        ways = cur[ssum]
                        if not ways:
                            continue
                        for d in range(max_d + 1):
                            ns = ssum + d
                            if ns > max_sum:
                                continue
                            ntight = 1 if (tight == 1 and d == lim) else 0
                            ndp[ntight][ns] = (ndp[ntight][ns] + ways) % MOD
                dp = ndp

            ans = 0
            for tight in (0, 1):
                for ssum in range(min_sum, max_sum + 1):
                    ans = (ans + dp[tight][ssum]) % MOD
            return ans

        upper = count_upto(num2)
        lower_bound = dec1(num1)
        lower = count_upto(lower_bound) if lower_bound != "0" or min_sum <= 0 else 0
        # count [num1, num2] = upto(num2) - upto(num1-1)
        return (upper - lower) % MOD
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def digits_of(s: str):
            return list(map(int, s))

        def count_upto(s: str) -> int:
            """
            Count x in [0, s] such that digit_sum(x) in [min_sum, max_sum].
            Leading zeros are allowed in DP, and x=0 is included if its digit_sum=0 matches.
            """
            digs = digits_of(s)
            n = len(digs)

            # dp[pos][sum][tight]: use two layers to save memory
            # We'll use dp_sum_tight[sum][tight]
            from collections import defaultdict

            dp = [[0, 0] for _ in range(max_sum + 1)]  # sums 0..max_sum, tight=0/1
            dp[0][1] = 1  # at pos=0, sum=0, tight=true

            for pos in range(n):
                newdp = [[0, 0] for _ in range(max_sum + 1)]
                limit = digs[pos]
                for ssum in range(max_sum + 1):
                    for tight in (0, 1):
                        ways = dp[ssum][tight]
                        if ways == 0:
                            continue
                        max_digit = limit if tight == 1 else 9
                        for d in range(max_digit + 1):
                            ns = ssum + d
                            if ns > max_sum:
                                continue
                            ntight = 1 if (tight == 1 and d == max_digit) else 0
                            newdp[ns][ntight] = (newdp[ns][ntight] + ways) % MOD
                dp = newdp

            ans = 0
            for ssum in range(min_sum, max_sum + 1):
                ans = (ans + dp[ssum][0] + dp[ssum][1]) % MOD
            return ans

        def dec_str(s: str) -> str:
            """Return string of (s-1), assuming s represents a positive integer (>=1)."""
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # remove leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        # Count up to num2 minus count up to num1-1
        total = count_upto(num2)
        if num1 == "0":
            res = total
        else:
            num1m1 = dec_str(num1)
            res = (total - count_upto(num1m1)) % MOD
        return res
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # s represents a positive integer (no leading zeros except possibly "0")
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        from functools import lru_cache

        def count_upto(bound: str) -> int:
            # count x in [0, bound] with digit sum within [min_sum, max_sum]
            digits = list(map(int, bound))
            n = len(digits)

            @lru_cache(None)
            def dp(pos: int, tight: int, s: int) -> int:
                # pos: current index [0..n], tight: 1 if prefix equals bound
                if s > max_sum:
                    return 0
                if pos == n:
                    return 1 if min_sum <= s <= max_sum else 0
                limit = digits[pos] if tight else 9
                res = 0
                for d in range(limit + 1):
                    nt = 1 if (tight and d == limit) else 0
                    res += dp(pos + 1, nt, s + d)
                return res % MOD

            return dp(0, 1, 0)

        ans2 = count_upto(num2)
        num1_minus_1 = dec_str(num1)
        ans1 = count_upto(num1_minus_1) if num1_minus_1 != "0" else 0
        return (ans2 - ans1) % MOD
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # s >= "0"
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            a[i] = str(int(a[i]) - 1)
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def count_upto(bound: str) -> int:
            # Count x in [0, bound] with digit sum in [min_sum, max_sum]
            if bound == "0":
                return 0 if not (min_sum <= 0 <= max_sum) else 1

            digits = list(map(int, bound))
            n = len(digits)

            # dp[pos][sum][tight] compressed to 2 layers and tight=0/1
            # dp for current prefix; sums clipped to max_sum
            prev_t0 = [0] * (max_sum + 1)  # tight=0
            prev_t1 = [0] * (max_sum + 1)  # tight=1
            prev_t1[0] = 1

            for pos in range(n):
                cur_t0 = [0] * (max_sum + 1)
                cur_t1 = [0] * (max_sum + 1)
                limit_digit = digits[pos]

                # From tight=0: next tight stays 0 and digit can be 0..9
                for s in range(max_sum + 1):
                    val = prev_t0[s]
                    if not val:
                        continue
                    for d in range(10):
                        ns = s + d
                        if ns > max_sum:
                            break
                        cur_t0[ns] = (cur_t0[ns] + val) % MOD

                # From tight=1: next digit 0..limit_digit
                for s in range(max_sum + 1):
                    val = prev_t1[s]
                    if not val:
                        continue
                    for d in range(limit_digit + 1):
                        ns = s + d
                        if ns > max_sum:
                            break
                        if d == limit_digit:
                            cur_t1[ns] = (cur_t1[ns] + val) % MOD
                        else:
                            cur_t0[ns] = (cur_t0[ns] + val) % MOD

                prev_t0, prev_t1 = cur_t0, cur_t1

            ans = 0
            for s in range(min_sum, max_sum + 1):
                ans = (ans + prev_t0[s] + prev_t1[s]) % MOD
            return ans

        # count in [num1, num2] = f(num2) - f(num1-1)
        num1_minus_1 = dec_str(num1)
        res = (count_upto(num2) - count_upto(num1_minus_1)) % MOD
        return res
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dec_str(s: str) -> str:
            # subtract 1 from a positive integer string (s >= "0")
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = chr(ord(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def count_leq(bound: str) -> int:
            # counts x in [0, bound] with min_sum <= digit_sum(x) <= max_sum
            if bound == "0":
                return 1 if (min_sum <= 0 <= max_sum) else 0

            digits = list(map(int, bound))
            n = len(digits)

            # Pre-sum bounds: sums can only be 0..9*n, but max_sum <= 400
            lo = min_sum
            hi = max_sum

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, ssum: int) -> int:
                # pos: current index, tight: whether prefix equals bound,
                # started: whether any non-leading digit has been placed,
                # ssum: current digit sum of the started part
                if pos == n:
                    return 1 if started and (lo <= ssum <= hi) else (1 if not started and lo <= 0 <= hi else 0)

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    ntight = 1 if (tight and d == limit) else 0  # careful: limit changes with tight; use equality with bound digit
                    # The above is incorrect because "limit" depends on tight. Fix:
                return res

            # Let's implement dp properly with correct tight handling
            digits = list(map(int, bound))
            n = len(digits)

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, ssum: int) -> int:
                if pos == n:
                    if started:
                        return 1 if lo <= ssum <= hi else 0
                    else:
                        return 1 if lo <= 0 <= hi else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0  # when tight, limit == digits[pos]
                    if started == 0 and d == 0:
                        res += dp(pos + 1, ntight, 0, ssum)
                    else:
                        ns = ssum + d
                        if ns <= hi:  # prune
                            res += dp(pos + 1, ntight, 1, ns)
                    res %= MOD
                return res

            return dp(0, 1, 0, 0)

        # Count [0, num2] - count [0, num1-1]
        num1m1 = dec_str(num1)
        ans = (count_leq(num2) - (count_leq(num1m1) if num1m1 != "0" or min_sum <= 0 <= max_sum else count_leq("0"))) % MOD
        # The subtraction above can be simplified, but keep it safe around "0".
        return ans
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        digits_cache = {}

        def digit_dp_le(s: str) -> int:
            """Count x in [0, s] with digit_sum in [min_sum, max_sum]."""
            if not s:
                return 0
            if s in digits_cache:
                return digits_cache[s]

            n = len(s)
            dp = [[0] * (max_sum + 1) for _ in range(n + 1)]
            dp[0][0] = 1

            for i in range(n):
                limit = int(s[i])
                new = [[0] * (max_sum + 1) for _ in range(n + 1)]
                # We'll use a standard tight/non-tight DP via two states:
                # tight=0 (already less), tight=1 (equal so far).
                # To keep memory small, we do iterative with two 1D arrays.
                # But easiest with two arrays for each sum.

            # Implement properly with tight flag:
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, tight: int, sm: int) -> int:
                if sm > max_sum:
                    return 0
                if pos == n:
                    return 1 if min_sum <= sm <= max_sum else 0
                lim = int(s[pos]) if tight else 9
                res = 0
                for d in range(lim + 1):
                    res += dfs(pos + 1, 1 if (tight and d == lim) else 0, sm + d)
                    if res >= MOD:
                        res -= MOD
                return res

            ans = dfs(0, 1, 0) % MOD
            digits_cache[s] = ans
            return ans

        def dec_one(s: str) -> str:
            """Return string for (int(s) - 1), assuming s represents positive integer."""
            a = list(s)
            i = len(a) - 1
            while i >= 0 and a[i] == '0':
                a[i] = '9'
                i -= 1
            if i >= 0:
                a[i] = str(int(a[i]) - 1)
            # strip leading zeros
            res = ''.join(a).lstrip('0')
            return res if res else "0"

        left = dec_one(num1) if num1 != "0" else "0"
        res = (digit_dp_le(num2) - digit_dp_le(left)) % MOD
        return res
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
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
      "expected": "11",
      "actual": "11",
      "error": ""
    },
    {
      "passed": true,
      "expected": "5",
      "actual": "5",
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
      "expected": "8",
      "actual": "8",
      "error": ""
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
      "expected": "258362773",
      "actual": "258362773",
      "error": ""
    },
    {
      "passed": true,
      "expected": "289633652",
      "actual": "289633652",
      "error": ""
    },
    {
      "passed": true,
      "expected": "157138097",
      "actual": "157138097",
      "error": ""
    }
  ]
}
```

</details>
