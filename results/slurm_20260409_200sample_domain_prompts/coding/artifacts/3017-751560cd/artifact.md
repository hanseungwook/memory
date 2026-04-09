# Problem 3017

- Domain: `coding`

## Problem

```text
You are given positive integers low, high, and k.
A number is beautiful if it meets both of the following conditions:

The count of even digits in the number is equal to the count of odd digits.
The number is divisible by k.

Return the number of beautiful integers in the range [low, high].
 
Example 1:

Input: low = 10, high = 20, k = 3
Output: 2
Explanation: There are 2 beautiful integers in the given range: [12,18]. 
- 12 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
- 18 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
Additionally we can see that:
- 16 is not beautiful because it is not divisible by k = 3.
- 15 is not beautiful because it does not contain equal counts even and odd digits.
It can be shown that there are only 2 beautiful integers in the given range.

Example 2:

Input: low = 1, high = 10, k = 1
Output: 1
Explanation: There is 1 beautiful integer in the given range: [10].
- 10 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 1.
It can be shown that there is only 1 beautiful integer in the given range.

Example 3:

Input: low = 5, high = 5, k = 2
Output: 0
Explanation: There are 0 beautiful integers in the given range.
- 5 is not beautiful because it is not divisible by k = 2 and it does not contain equal even and odd digits.

 
Constraints:

0 < low <= high <= 10^9
0 < k <= 20
```

### Starter Code

```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
```

### Test Cases

```json
[
  {
    "input": "10\n20\n3",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "1\n10\n1",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "5\n5\n2",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "1\n1\n1",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "19\n50\n2",
    "output": "6",
    "testtype": "functional"
  },
  {
    "input": "94\n94\n9",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "94\n100\n1",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "52\n396\n9",
    "output": "5",
    "testtype": "functional"
  },
  {
    "input": "47\n735\n2",
    "output": "15",
    "testtype": "functional"
  },
  {
    "input": "90\n110\n16",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "934\n991\n1",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "1\n1000000000\n1",
    "output": "24894045",
    "testtype": "functional"
  },
  {
    "input": "33340762\n612987024\n1",
    "output": "18196584",
    "testtype": "functional"
  },
  {
    "input": "36954768\n642296821\n14",
    "output": "1240042",
    "testtype": "functional"
  },
  {
    "input": "17946863\n807558969\n17",
    "output": "1319380",
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
You are given positive integers low, high, and k.
A number is beautiful if it meets both of the following conditions:

The count of even digits in the number is equal to the count of odd digits.
The number is divisible by k.

Return the number of beautiful integers in the range [low, high].
 
Example 1:

Input: low = 10, high = 20, k = 3
Output: 2
Explanation: There are 2 beautiful integers in the given range: [12,18]. 
- 12 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
- 18 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
Additionally we can see that:
- 16 is not beautiful because it is not divisible by k = 3.
- 15 is not beautiful because it does not contain equal counts even and odd digits.
It can be shown that there are only 2 beautiful integers in the given range.

Example 2:

Input: low = 1, high = 10, k = 1
Output: 1
Explanation: There is 1 beautiful integer in the given range: [10].
- 10 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 1.
It can be shown that there is only 1 beautiful integer in the given range.

Example 3:

Input: low = 5, high = 5, k = 2
Output: 0
Explanation: There are 0 beautiful integers in the given range.
- 5 is not beautiful because it is not divisible by k = 2 and it does not contain equal even and odd digits.

 
Constraints:

0 < low <= high <= 10^9
0 < k <= 20

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][balance][mod][tight_started]
            # balance = (#even - #odd), must end at 0
            # Use offset to index negative balances.
            off = 20  # safe because balance range within [-m, m] and m<=10
            # We'll track started = whether we have placed a non-leading-zero digit.
            # Leading zeros do not contribute digits (so parity counts ignore them).
            from collections import defaultdict

            dp = defaultdict(int)
            # state: (balance, mod, started) -> ways
            dp[(0, 0, 0)] = 1

            for pos, lim in enumerate(digits):
                ndp = defaultdict(int)
                for (bal, mod, started), ways in dp.items():
                    for d in range(0, lim + 1):
                        nstarted = started or (d != 0)
                        if not nstarted:
                            # still leading zeros: no digit contributes
                            nbal, nmod = bal, 0  # mod should be 0 because no meaningful digits yet
                            # But to be consistent, if not started we keep mod=0.
                            nt = 0  # started flag tracked
                        else:
                            # determine parity contribution
                            if d % 2 == 0:
                                nbal = bal + 1
                            else:
                                nbal = bal - 1
                            nmod = (mod * 10 + d) % k

                        if nstarted:
                            # started is 1
                            ndp[(nbal, nmod, 1)] += ways
                        else:
                            ndp[(nbal, nmod, 0)] += ways

                dp = ndp

            # Now dp includes numbers with varying length up to m, including 0.
            # We need numbers in [1..n], so exclude number 0: started must be 1.
            ans = 0
            for (bal, mod, started), ways in dp.items():
                if started == 1 and bal == 0 and mod % k == 0:
                    ans += ways
            return ans

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)

            # DP over positions:
            # diff = (#even - #odd) shifted by +L (so range [-L..L])
            # rem = remainder mod k
            offset = L
            size_diff = 2 * L + 1

            # dp[pos][diff][rem] as rolling arrays
            # Using list comprehension for speed.
            dp = [[0] * k for _ in range(size_diff)]
            dp[offset][0] = 1  # at pos 0, diff=0, rem=0

            tight = [True]  # dummy to help structure; we'll use 4D rolling via dicts per tight state
            # We'll keep separate dp for tight/not tight.
            dp_tight = [[0] * k for _ in range(size_diff)]
            dp_not = [[0] * k for _ in range(size_diff)]
            dp_tight[offset][0] = 1

            for pos in range(L):
                next_tight = [[0] * k for _ in range(size_diff)]
                next_not = [[0] * k for _ in range(size_diff)]

                limit = digits[pos]

                # Transition for tight states
                for diff_i in range(size_diff):
                    row = dp_tight[diff_i]
                    if not any(row):
                        continue
                    for rem in range(k):
                        ways = row[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(limit + 1):
                            n_tight = (dig == limit)
                            new_rem = (rem * 10 + dig) % k
                            new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                            new_diff_i = new_diff + offset
                            if n_tight:
                                next_tight[new_diff_i][new_rem] += ways
                            else:
                                next_not[new_diff_i][new_rem] += ways

                # Transition for not tight states (limit=9)
                for diff_i in range(size_diff):
                    row = dp_not[diff_i]
                    if not any(row):
                        continue
                    for rem in range(k):
                        ways = row[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(10):
                            new_rem = (rem * 10 + dig) % k
                            new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                            new_diff_i = new_diff + offset
                            next_not[new_diff_i][new_rem] += ways

                dp_tight, dp_not = next_tight, next_not

            # Need exactly equal even/odd digits => diff = 0
            # Also exclude the number 0 (not in positive integers). Our DP counts all L-digit numbers including leading zeros.
            # Leading zeros contribute digits, but they are even digits (0), which changes diff.
            # To handle correctly, compute for each length separately without leading zeros by fixing first digit > 0.
            # Instead, we correct by subtracting count for numbers with leading zeros not allowed:
            # Easier: run a digit DP that disallows leading zero by treating "not started" state.
            # We'll implement that below and replace count_upto with correct one.

            return 0  # placeholder (will be overwritten)

        # Correct digit DP: keep started flag to avoid leading zeros affecting digit parity count.
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            offset = L
            size_diff = 2 * L + 1

            # dp[started][diff_i][rem]
            dp_started = [[0] * k for _ in range(size_diff)]
            dp_not = [[0] * k for _ in range(size_diff)]
            # started=False: no digits chosen yet => diff=0 rem=0
            dp_not[offset][0] = 1

            for pos in range(L):
                next_started = [[0] * k for _ in range(size_diff)]
                next_not = [[0] * k for _ in range(size_diff)]
                limit = digits[pos]

                for diff_i in range(size_diff):
                    # not started
                    row0 = dp_not[diff_i]
                    if not any(row0):
                        pass
                    for rem in range(k):
                        ways = row0[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(limit + 1):
                            n_started = (dig != 0)
                            new_rem = (rem * 10 + dig) % k if n_started else 0
                            if not n_started:
                                next_diff_i = offset  # still diff=0 because no digits counted
                                if dig == limit:
                                    next_not[next_diff_i][new_rem] += ways
                                else:
                                    next_not[next_diff_i][new_rem] += ways
                            else:
                                new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                                new_diff_i = new_diff + offset
                                if dig == limit:
                                    next_started[new_diff_i][new_rem] += ways
                                else:
                                    next_started[new_diff_i][new_rem] += ways

                    # started
                    row1 = dp_started[diff_i]
                    if not any(row1):
                        pass
                    for rem in range(k):
                        ways = row1[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(limit + 1):
                            new_rem = (rem * 10 + dig) % k
                            new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                            new_diff_i = new_diff + offset
                            if dig == limit:
                                next_started[new_diff_i][new_rem] += ways
                            else:
                                next_started[new_diff_i][new_rem] += ways

                # The above transitions ignore the "tight" aspect; so it's incorrect.
                # We'll implement proper tight DP.

                # ---- Implement proper tight DP below and return immediately (replacing this whole function) ----
                return 0

            return 0  # unused

        # Proper digit DP with memoization: tight + started + diff + rem
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            offset = L
            size_diff = 2 * L + 1

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, diff_i: int, rem: int) -> int:
                if pos == L:
                    if started == 1 and diff_i == offset and rem == 0:
                        return 1
                    return 0

                limit = digits[pos] if tight else 9
                total = 0
                cur_diff = diff_i - offset

                for dig in range(limit + 1):
                    ntight = 1 if (tight and dig == limit) else 0
                    if started == 0 and dig == 0:
                        # still not started; diff stays 0, rem stays 0
                        total += dp(pos + 1, ntight, 0, offset, 0)
                    else:
                        if started == 0:
                            new_diff = (1 if dig % 2 == 0 else -1)
                            new_diff_i = new_diff + offset
                            new_rem = dig % k
                            total += dp(pos + 1, ntight, 1, new_diff_i, new_rem)
                        else:
                            new_diff = cur_diff + (1 if dig % 2 == 0 else -1)
                            new_diff_i = new_diff + offset
                            new_rem = (rem * 10 + dig) % k
                            total += dp(pos + 1, ntight, 1, new_diff_i, new_rem)
                return total

            return dp(0, 1, 0, offset, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(x: int) -> int:
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            # dp[pos][diff+offset][rem][tight][started]
            # diff = #odd - #even among digits chosen after starting (zeros in front not counted)
            offset = n  # diff range [-n, n]
            from functools import lru_cache

            @lru_cache(None)
            def dp(pos: int, diff: int, rem: int, tight: int, started: int) -> int:
                if pos == n:
                    # Beautiful if started and diff == 0 and remainder == 0
                    # Note: "count of even digits equals count of odd digits" => diff == 0
                    return 1 if started and diff == 0 and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                total = 0

                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0

                    if started == 0 and d == 0:
                        # still not started: don't count digit, keep remainder as 0
                        total += dp(pos + 1, diff, 0, ntight, 0)
                    else:
                        # started (leading zeros are no longer possible)
                        # update diff by digit parity; update remainder with digit
                        if d % 2 == 0:
                            ndiff = diff - 1  # even increases even count => odd-even decreases
                        else:
                            ndiff = diff + 1  # odd increases odd count => odd-even increases
                        nrem = (rem * 10 + d) % k
                        total += dp(pos + 1, ndiff, nrem, ntight, 1)

                return total

            return dp(0, 0, 0, 1, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][diff][rem][started] but keep it compact:
            # diff = even_count - odd_count, shifted by +offset
            # diff range is [-m, m]
            offset = m
            size_diff = 2 * m + 1
            MOD = 10**18  # no mod needed; just avoid accidental large issues

            # Use dict-based DP to keep states manageable:
            # key: (diff_index, rem, started)
            cur = {(offset, 0, 0): 1}

            for pos in range(m):
                nd = digits[pos]
                nxt = {}
                for (diff_idx, rem, started), ways in cur.items():
                    for dig in range(0, nd + 1):
                        tight_new = False  # handled by per-digit approach below
                    # We will do standard tight DP by including tight in state.
                # Let's redo with tight properly (dict states)

            # Standard digit DP with memoization:
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, diff_idx: int, rem: int, started: int, tight: int) -> int:
                if pos == m:
                    # If never started => number 0, exclude (range starts from >=1)
                    if started == 0:
                        return 0
                    return 1 if diff_idx == offset and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                ans = 0
                for dig in range(0, limit + 1):
                    started2 = started or (dig != 0)
                    diff_idx2 = diff_idx

                    if started2:
                        if dig % 2 == 0:
                            diff_idx2 += 1  # even digit
                        else:
                            diff_idx2 -= 1  # odd digit

                    # Only keep diff within [-m, m]
                    if diff_idx2 < 0 or diff_idx2 >= size_diff:
                        continue

                    rem2 = rem
                    if started2:
                        rem2 = (rem * 10 + dig) % k

                    ans += dfs(
                        pos + 1,
                        diff_idx2,
                        rem2,
                        1 if started2 else 0,
                        1 if (tight and dig == limit) else 0
                    )
                return ans

            # The "tight" transition above is incorrect: we used limit, not digit[pos].
            # Fix by rewriting dfs with correct tight handling.

            dfs.cache_clear()

            @lru_cache(None)
            def dfs(pos: int, diff_idx: int, rem: int, started: int, tight: int) -> int:
                if pos == m:
                    if started == 0:
                        return 0
                    return 1 if diff_idx == offset and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                ans = 0
                for dig in range(0, limit + 1):
                    started2 = started or (dig != 0)

                    diff_idx2 = diff_idx
                    rem2 = rem

                    if started2:
                        if dig % 2 == 0:
                            diff_idx2 += 1
                        else:
                            diff_idx2 -= 1
                        rem2 = (rem * 10 + dig) % k

                    if diff_idx2 < 0 or diff_idx2 >= size_diff:
                        continue

                    ans += dfs(
                        pos + 1,
                        diff_idx2,
                        rem2,
                        1 if started2 else 0,
                        1 if (tight and dig == limit) else 0
                    )
                return ans

            # Correct tight update should compare dig with digits[pos] when tight==1.
            # Since limit equals digits[pos] in that case, using dig == limit is correct.

            return dfs(0, offset, 0, 0, 1)

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            s = str(n)
            m = len(s)
            digits = list(map(int, s))

            @lru_cache(None)
            def dp(pos: int, diff: int, mod: int, tight: int, started: int) -> int:
                # diff = (#even - #odd) so far, on started part
                if pos == m:
                    return 1 if started and diff == 0 and mod == 0 else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    nstarted = started or (d != 0)
                    if not nstarted:
                        # still not started: don't count digits, diff/mod remain
                        res += dp(pos + 1, diff, mod, ntight, 0)
                    else:
                        ndiff = diff + (1 if (d % 2 == 0) else -1)
                        nmod = (mod * 10 + d) % k
                        res += dp(pos + 1, ndiff, nmod, ntight, 1)
                return res

            # diff range is [-m, m], state space is manageable for m<=10
            return dp(0, 0, 0, 1, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][diff][rem][tight][started]
            # diff = (#even - #odd) among digits chosen so far
            # Rem = value mod k
            # We use dict maps to keep state small.
            from collections import defaultdict

            # Use offset so diff indices are non-negative
            # diff range in absolute value <= m, so [-m..m]
            offset = m

            # Initialize at pos 0
            dp = { (0, 0, 0, True, False): 1 }  # (pos, diff, rem, tight, started) -> count

            for pos in range(m):
                new_dp = defaultdict(int)
                limit_digit = digits[pos]
                for (p, diff, rem, tight, started), ways in dp.items():
                    # p should equal pos
                    mx = limit_digit if tight else 9
                    for dig in range(mx + 1):
                        ntight = tight and (dig == mx if not tight else dig == limit_digit)
                        # careful with ntight:
                        ntight = tight and (dig == limit_digit)

                        if not started and dig == 0:
                            # Still not started; diff/rem unchanged
                            # Note: number length shorter than m.
                            nstarted = False
                            ndiff = diff
                            nrem = 0  # irrelevant while not started; keep 0
                            new_dp[(pos + 1, ndiff, nrem, ntight, nstarted)] += ways
                        else:
                            nstarted = True
                            if dig % 2 == 0:
                                ndiff = diff + 1
                            else:
                                ndiff = diff - 1
                            nrem = (rem * 10 + dig) % k
                            new_dp[(pos + 1, ndiff, nrem, ntight, nstarted)] += ways
                dp = new_dp

            # Final count: started must be True, diff must be 0, rem must be 0
            ans = 0
            for (p, diff, rem, tight, started), ways in dp.items():
                if p != m:
                    continue
                if started and diff == 0 and rem % k == 0:
                    ans += ways
            return ans

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(x: int) -> int:
            if x <= 0:
                return 0

            s = str(x)
            n = len(s)

            # dp[pos][diff][rem][tight] not used; we do iterative DP with tight.
            # diff = even_count - odd_count, must end at 0
            # diff range: [-n, n] but we can keep offset
            offset = n
            size_diff = 2 * n + 1

            from collections import defaultdict

            # states: rem, diff -> count
            cur = defaultdict(int)
            cur[(0, 0)] = 1  # before placing any digit: rem=0, diff=0, count=1

            for i, ch in enumerate(s):
                digit_limit = int(ch)
                nxt = defaultdict(int)

                tight_states = [(0, cur)]  # dummy, we handle tight by splitting keys
                # We'll do classic digit DP keeping "tight" as part of key.
                # To simplify: we reinitialize with proper structure per position using dicts keyed by (tight, rem, diff).
                # But easiest: maintain two layers: tight=0/1.

            # Re-implement cleanly with tight state:
            cur = {(1, 0, 0): 1}  # (tight, rem, diff) -> ways

            for i, ch in enumerate(s):
                limit = int(ch)
                nxt = {}
                for (tight, rem, diff), ways in cur.items():
                    max_d = limit if tight == 1 else 9
                    for d in range(max_d + 1):
                        ntight = 1 if (tight == 1 and d == max_d) else 0
                        # update rem
                        nrem = (rem * 10 + d) % k
                        # update diff: even digit +1, odd digit -1
                        ndiff = diff + (1 if d % 2 == 0 else -1)
                        key = (ntight, nrem, ndiff)
                        nxt[key] = nxt.get(key, 0) + ways
                cur = nxt

            # We counted leading zeros as digits too; but that's fine because:
            # - leading zeros contribute even digits (0 is even),
            # - we want numbers in [1..x], not including 0.
            # Our DP includes 0..x inclusive, but only numbers whose diff ends at 0 and rem at 0.
            # For x>0, number 0 could be counted; ensure it's excluded.
            ans = 0
            for (tight, rem, diff), ways in cur.items():
                if rem == 0 and diff == 0:
                    # tight can be 0 or 1; both are included in dp results.
                    ans += ways

            # Exclude number 0 if it was counted.
            # Number 0 has all digits as '0' (length n), so diff = (#even) - 0 = n, not 0 unless n=0.
            # So it won't be counted. But to be safe, handle x==0 already returns 0.
            return ans

        # Digit DP above used a simplified ntight calculation that is incorrect.
        # We'll correct by rewriting with proper tight transitions.

        def count_beautiful_upto_fixed(x: int) -> int:
            if x <= 0:
                return 0
            s = str(x)
            n = len(s)

            cur = {(1, 0, 0): 1}  # (tight, rem, diff) -> ways; diff is even-odd across n digits

            for i, ch in enumerate(s):
                limit = int(ch)
                nxt = {}
                for (tight, rem, diff), ways in cur.items():
                    max_d = limit if tight == 1 else 9
                    for d in range(max_d + 1):
                        ntight = 1 if (tight == 1 and d == limit) else 0
                        nrem = (rem * 10 + d) % k
                        ndiff = diff + (1 if d % 2 == 0 else -1)
                        key = (ntight, nrem, ndiff)
                        nxt[key] = nxt.get(key, 0) + ways
                cur = nxt

            ans = 0
            for (tight, rem, diff), ways in cur.items():
                if rem == 0 and diff == 0:
                    ans += ways
            return ans

        return count_beautiful_upto_fixed(high) - count_beautiful_upto_fixed(low - 1)
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_up_to(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)
            # shift even_minus_odd by +L (range [-L, L])
            SHIFT = L
            OFFSET = 2 * L + 1

            # dp[pos][diff_index][mod] = ways, using rolling arrays
            # diff = (#even - #odd) so that equality (#even == #odd) => diff == 0
            dp = [[0] * k for _ in range(OFFSET)]
            dp[SHIFT][0] = 1

            for i in range(L):
                ndp = [[0] * k for _ in range(OFFSET)]
                limit = digits[i]
                for diff_i in range(OFFSET):
                    for mod in range(k):
                        ways = dp[diff_i][mod]
                        if ways == 0:
                            continue
                        diff = diff_i - SHIFT
                        for d in range(0, limit + 1):
                            new_diff = diff + (1 if d % 2 == 0 else -1)
                            new_diff_i = new_diff + SHIFT
                            if 0 <= new_diff_i < OFFSET:
                                new_mod = (mod * 10 + d) % k
                                ndp[new_diff_i][new_mod] += ways
                dp = ndp

            # Count numbers with diff==0 and mod==0, but must exclude 0 itself.
            # Our digit-DP counts all L-digit sequences with leading zeros allowed,
            # which includes the all-zero number. That number has diff=+L (all even digits),
            # so it won't be counted anyway. However, we still ensure we don't count
            # numbers outside [1..n] by using diff==0 and mod==0.
            return dp[SHIFT][0]

        return count_up_to(high) - count_up_to(low - 1)
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)

            # dp[pos][diff_offset][rem][tight] -> count
            # diff = even_count - odd_count, range [-L..L], offset by L
            offset = L
            size = 2 * L + 1

            # Use two layers for pos to save memory.
            # We'll represent dp[tight] as dict for sparse remainder/diff, but k<=20 so
            # dense over rem is fine; keep arrays for speed.
            # dp_tight0/1: at each pos, with diff and remainder.
            import array

            # dp arrays: [diff][rem]
            def make_layer():
                return [[0] * k for _ in range(size)]

            dp_tight0 = make_layer()  # tight=0
            dp_tight1 = make_layer()  # tight=1

            # start: no digits yet, diff=0, rem=0
            dp_tight1[offset][0] = 1

            for pos, lim in enumerate(digits):
                ndp_tight0 = make_layer()
                ndp_tight1 = make_layer()

                for diff_idx in range(size):
                    for rem in range(k):
                        # tight = 0 transitions (already below prefix)
                        cnt0 = dp_tight0[diff_idx][rem]
                        if cnt0:
                            cur_diff = diff_idx - offset
                            for d in range(10):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    ndp_tight0[ndiff + offset][nrem] += cnt0

                        # tight = 1 transitions (follow prefix)
                        cnt1 = dp_tight1[diff_idx][rem]
                        if cnt1:
                            cur_diff = diff_idx - offset
                            for d in range(lim + 1):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    if d == lim:
                                        ndp_tight1[ndiff + offset][nrem] += cnt1
                                    else:
                                        ndp_tight0[ndiff + offset][nrem] += cnt1

                dp_tight0, dp_tight1 = ndp_tight0, ndp_tight1

            # We count only numbers with equal even/odd digit counts => diff==0
            # and divisible by k => rem==0.
            # Also must exclude leading zeros because the representation has exactly L digits.
            # Our DP currently allows leading zeros as actual digits, which would affect parity counts.
            # Fix: count numbers in [0..n] with exactly L digits including leading zeros, then subtract those
            # with leading zeros by computing for length < L and using digit-DP on exact length.
            # Instead, we correct by using a standard trick: disallow leading zero by tracking started flag.
            # We'll implement a second DP that includes "started" to ensure correct digit parity counts.
            return count_upto_with_started(n)

        def count_upto_with_started(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            offset = L
            size = 2 * L + 1

            def make_layer():
                return [[0] * k for _ in range(size)]

            # dp[tight][started][diff][rem]
            # We'll use two tight layers and started flag.
            dp00 = make_layer()  # tight=0, started=0
            dp01 = make_layer()  # tight=0, started=1
            dp10 = make_layer()  # tight=1, started=0
            dp11 = make_layer()  # tight=1, started=1

            # started=0: no digits placed yet => diff=0, rem=0
            dp10[offset][0] = 1

            for pos, lim in enumerate(digits):
                ndp00 = make_layer()
                ndp01 = make_layer()
                ndp10 = make_layer()
                ndp11 = make_layer()

                for diff_idx in range(size):
                    for rem in range(k):
                        cur_diff = diff_idx - offset

                        # tight=0, started=0
                        cnt = dp00[diff_idx][rem]
                        if cnt:
                            for d in range(10):
                                if d == 0:
                                    # still not started
                                    ndiff = cur_diff
                                    nrem = 0  # rem irrelevant while not started; keep 0
                                    ndp00[ndiff + offset][nrem] += cnt
                                else:
                                    ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                    nrem = d % k
                                    if -L <= ndiff <= L:
                                        ndp01[ndiff + offset][nrem] += cnt

                        # tight=0, started=1
                        cnt = dp01[diff_idx][rem]
                        if cnt:
                            for d in range(10):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    ndp01[ndiff + offset][nrem] += cnt

                        # tight=1, started=0
                        cnt = dp10[diff_idx][rem]
                        if cnt:
                            for d in range(lim + 1):
                                tight1 = (d == lim)
                                if d == 0:
                                    ndiff = cur_diff
                                    nrem = 0
                                    if tight1:
                                        ndp10[ndiff + offset][nrem] += cnt
                                    else:
                                        ndp00[ndiff + offset][nrem] += cnt
                                else:
                                    ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                    if -L <= ndiff <= L:
                                        nrem = d % k
                                        if tight1:
                                            ndp11[ndiff + offset][nrem] += cnt
                                        else:
                                            ndp01[ndiff + offset][nrem] += cnt

                        # tight=1, started=1
                        cnt = dp11[diff_idx][rem]
                        if cnt:
                            for d in range(lim + 1):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    if d == lim:
                                        ndp11[ndiff + offset][nrem] += cnt
                                    else:
                                        ndp01[ndiff + offset][nrem] += cnt

                dp00, dp01, dp10, dp11 = ndp00, ndp01, ndp10, ndp11

            # Count started=1 only (exclude 0)
            return dp01[offset][0] + dp11[offset][0]

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(x: int) -> int:
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            # dp[pos][diff][rem][started]
            # diff = even_count - odd_count, shift by +n to make non-negative
            # rem = number mod k
            # started = whether we've placed any non-leading-zero digit
            shift = n
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, diff: int, rem: int, started: int) -> int:
                if pos == n:
                    if not started:
                        return 0  # exclude 0
                    return 1 if diff == 0 and rem == 0 else 0

                limit = digits[pos]
                total = 0
                for d in range(0, limit + 1):
                    nt_started = started or d != 0
                    if not nt_started:
                        # still leading zeros: diff and rem unchanged
                        total += dfs(pos + 1, diff, rem, 0)
                    else:
                        ndiff = diff
                        if d % 2 == 0:
                            ndiff += 1
                        else:
                            ndiff -= 1
                        nrem = (rem * 10 + d) % k
                        total += dfs(pos + 1, ndiff, nrem, 1)
                return total

            # bound diff within [-n, n]
            # Our recursion never steps outside when starting from 0; still safe.
            return dfs(0, shift, 0, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.2000 | `partial` |
| 1 | 1.0000 | `full` |
| 2 | 1.0000 | `full` |
| 3 | 1.0000 | `full` |
| 4 | 1.0000 | `full` |
| 5 | 1.0000 | `full` |
| 6 | 0.3333 | `partial` |
| 7 | 0.2667 | `partial` |
| 8 | 1.0000 | `full` |
| 9 | 0.1333 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 3,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
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
      "passed": false,
      "expected": "6",
      "actual": "-2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "-18",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "5",
      "actual": "7",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "-2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "-2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "24894045",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18196584",
      "actual": "4193",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240042",
      "actual": "-54959",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1319380",
      "actual": "-6656",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "4",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "6",
      "error": "Wrong Answer"
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "-47",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "5",
      "actual": "-5",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "-10",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "-2",
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
      "expected": "24894045",
      "actual": "246093750",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18196584",
      "actual": "-9147166",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240042",
      "actual": "-713083",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1319380",
      "actual": "-289076",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "passed": 4,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
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
      "passed": false,
      "expected": "6",
      "actual": "-2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "-20",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "5",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "-8",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "-2",
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
      "expected": "24894045",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18196584",
      "actual": "-9280",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240042",
      "actual": "-67609",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1319380",
      "actual": "-16231",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
  "passed": 2,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "-2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "0",
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
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "6",
      "actual": "0",
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
      "expected": "3",
      "actual": "-10",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "5",
      "actual": "6",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "5",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "24894045",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18196584",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240042",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1319380",
      "actual": "-85",
      "error": "Wrong Answer"
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
You are given positive integers low, high, and k.
A number is beautiful if it meets both of the following conditions:

The count of even digits in the number is equal to the count of odd digits.
The number is divisible by k.

Return the number of beautiful integers in the range [low, high].
 
Example 1:

Input: low = 10, high = 20, k = 3
Output: 2
Explanation: There are 2 beautiful integers in the given range: [12,18]. 
- 12 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
- 18 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
Additionally we can see that:
- 16 is not beautiful because it is not divisible by k = 3.
- 15 is not beautiful because it does not contain equal counts even and odd digits.
It can be shown that there are only 2 beautiful integers in the given range.

Example 2:

Input: low = 1, high = 10, k = 1
Output: 1
Explanation: There is 1 beautiful integer in the given range: [10].
- 10 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 1.
It can be shown that there is only 1 beautiful integer in the given range.

Example 3:

Input: low = 5, high = 5, k = 2
Output: 0
Explanation: There are 0 beautiful integers in the given range.
- 5 is not beautiful because it is not divisible by k = 2 and it does not contain equal even and odd digits.

 
Constraints:

0 < low <= high <= 10^9
0 < k <= 20

### Solutions
#### Correct
Attempt 1
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)

            # DP over positions:
            # diff = (#even - #odd) shifted by +L (so range [-L..L])
            # rem = remainder mod k
            offset = L
            size_diff = 2 * L + 1

            # dp[pos][diff][rem] as rolling arrays
            # Using list comprehension for speed.
            dp = [[0] * k for _ in range(size_diff)]
            dp[offset][0] = 1  # at pos 0, diff=0, rem=0

            tight = [True]  # dummy to help structure; we'll use 4D rolling via dicts per tight state
            # We'll keep separate dp for tight/not tight.
            dp_tight = [[0] * k for _ in range(size_diff)]
            dp_not = [[0] * k for _ in range(size_diff)]
            dp_tight[offset][0] = 1

            for pos in range(L):
                next_tight = [[0] * k for _ in range(size_diff)]
                next_not = [[0] * k for _ in range(size_diff)]

                limit = digits[pos]

                # Transition for tight states
                for diff_i in range(size_diff):
                    row = dp_tight[diff_i]
                    if not any(row):
                        continue
                    for rem in range(k):
                        ways = row[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(limit + 1):
                            n_tight = (dig == limit)
                            new_rem = (rem * 10 + dig) % k
                            new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                            new_diff_i = new_diff + offset
                            if n_tight:
                                next_tight[new_diff_i][new_rem] += ways
                            else:
                                next_not[new_diff_i][new_rem] += ways

                # Transition for not tight states (limit=9)
                for diff_i in range(size_diff):
                    row = dp_not[diff_i]
                    if not any(row):
                        continue
                    for rem in range(k):
                        ways = row[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(10):
                            new_rem = (rem * 10 + dig) % k
                            new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                            new_diff_i = new_diff + offset
                            next_not[new_diff_i][new_rem] += ways

                dp_tight, dp_not = next_tight, next_not

            # Need exactly equal even/odd digits => diff = 0
            # Also exclude the number 0 (not in positive integers). Our DP counts all L-digit numbers including leading zeros.
            # Leading zeros contribute digits, but they are even digits (0), which changes diff.
            # To handle correctly, compute for each length separately without leading zeros by fixing first digit > 0.
            # Instead, we correct by subtracting count for numbers with leading zeros not allowed:
            # Easier: run a digit DP that disallows leading zero by treating "not started" state.
            # We'll implement that below and replace count_upto with correct one.

            return 0  # placeholder (will be overwritten)

        # Correct digit DP: keep started flag to avoid leading zeros affecting digit parity count.
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            offset = L
            size_diff = 2 * L + 1

            # dp[started][diff_i][rem]
            dp_started = [[0] * k for _ in range(size_diff)]
            dp_not = [[0] * k for _ in range(size_diff)]
            # started=False: no digits chosen yet => diff=0 rem=0
            dp_not[offset][0] = 1

            for pos in range(L):
                next_started = [[0] * k for _ in range(size_diff)]
                next_not = [[0] * k for _ in range(size_diff)]
                limit = digits[pos]

                for diff_i in range(size_diff):
                    # not started
                    row0 = dp_not[diff_i]
                    if not any(row0):
                        pass
                    for rem in range(k):
                        ways = row0[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(limit + 1):
                            n_started = (dig != 0)
                            new_rem = (rem * 10 + dig) % k if n_started else 0
                            if not n_started:
                                next_diff_i = offset  # still diff=0 because no digits counted
                                if dig == limit:
                                    next_not[next_diff_i][new_rem] += ways
                                else:
                                    next_not[next_diff_i][new_rem] += ways
                            else:
                                new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                                new_diff_i = new_diff + offset
                                if dig == limit:
                                    next_started[new_diff_i][new_rem] += ways
                                else:
                                    next_started[new_diff_i][new_rem] += ways

                    # started
                    row1 = dp_started[diff_i]
                    if not any(row1):
                        pass
                    for rem in range(k):
                        ways = row1[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(limit + 1):
                            new_rem = (rem * 10 + dig) % k
                            new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                            new_diff_i = new_diff + offset
                            if dig == limit:
                                next_started[new_diff_i][new_rem] += ways
                            else:
                                next_started[new_diff_i][new_rem] += ways

                # The above transitions ignore the "tight" aspect; so it's incorrect.
                # We'll implement proper tight DP.

                # ---- Implement proper tight DP below and return immediately (replacing this whole function) ----
                return 0

            return 0  # unused

        # Proper digit DP with memoization: tight + started + diff + rem
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            offset = L
            size_diff = 2 * L + 1

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, diff_i: int, rem: int) -> int:
                if pos == L:
                    if started == 1 and diff_i == offset and rem == 0:
                        return 1
                    return 0

                limit = digits[pos] if tight else 9
                total = 0
                cur_diff = diff_i - offset

                for dig in range(limit + 1):
                    ntight = 1 if (tight and dig == limit) else 0
                    if started == 0 and dig == 0:
                        # still not started; diff stays 0, rem stays 0
                        total += dp(pos + 1, ntight, 0, offset, 0)
                    else:
                        if started == 0:
                            new_diff = (1 if dig % 2 == 0 else -1)
                            new_diff_i = new_diff + offset
                            new_rem = dig % k
                            total += dp(pos + 1, ntight, 1, new_diff_i, new_rem)
                        else:
                            new_diff = cur_diff + (1 if dig % 2 == 0 else -1)
                            new_diff_i = new_diff + offset
                            new_rem = (rem * 10 + dig) % k
                            total += dp(pos + 1, ntight, 1, new_diff_i, new_rem)
                return total

            return dp(0, 1, 0, offset, 0)

        return count_upto(high) - count_upto(low - 1)
```

Attempt 2
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(x: int) -> int:
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            # dp[pos][diff+offset][rem][tight][started]
            # diff = #odd - #even among digits chosen after starting (zeros in front not counted)
            offset = n  # diff range [-n, n]
            from functools import lru_cache

            @lru_cache(None)
            def dp(pos: int, diff: int, rem: int, tight: int, started: int) -> int:
                if pos == n:
                    # Beautiful if started and diff == 0 and remainder == 0
                    # Note: "count of even digits equals count of odd digits" => diff == 0
                    return 1 if started and diff == 0 and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                total = 0

                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0

                    if started == 0 and d == 0:
                        # still not started: don't count digit, keep remainder as 0
                        total += dp(pos + 1, diff, 0, ntight, 0)
                    else:
                        # started (leading zeros are no longer possible)
                        # update diff by digit parity; update remainder with digit
                        if d % 2 == 0:
                            ndiff = diff - 1  # even increases even count => odd-even decreases
                        else:
                            ndiff = diff + 1  # odd increases odd count => odd-even increases
                        nrem = (rem * 10 + d) % k
                        total += dp(pos + 1, ndiff, nrem, ntight, 1)

                return total

            return dp(0, 0, 0, 1, 0)

        return count_upto(high) - count_upto(low - 1)
```

Attempt 3
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][diff][rem][started] but keep it compact:
            # diff = even_count - odd_count, shifted by +offset
            # diff range is [-m, m]
            offset = m
            size_diff = 2 * m + 1
            MOD = 10**18  # no mod needed; just avoid accidental large issues

            # Use dict-based DP to keep states manageable:
            # key: (diff_index, rem, started)
            cur = {(offset, 0, 0): 1}

            for pos in range(m):
                nd = digits[pos]
                nxt = {}
                for (diff_idx, rem, started), ways in cur.items():
                    for dig in range(0, nd + 1):
                        tight_new = False  # handled by per-digit approach below
                    # We will do standard tight DP by including tight in state.
                # Let's redo with tight properly (dict states)

            # Standard digit DP with memoization:
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, diff_idx: int, rem: int, started: int, tight: int) -> int:
                if pos == m:
                    # If never started => number 0, exclude (range starts from >=1)
                    if started == 0:
                        return 0
                    return 1 if diff_idx == offset and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                ans = 0
                for dig in range(0, limit + 1):
                    started2 = started or (dig != 0)
                    diff_idx2 = diff_idx

                    if started2:
                        if dig % 2 == 0:
                            diff_idx2 += 1  # even digit
                        else:
                            diff_idx2 -= 1  # odd digit

                    # Only keep diff within [-m, m]
                    if diff_idx2 < 0 or diff_idx2 >= size_diff:
                        continue

                    rem2 = rem
                    if started2:
                        rem2 = (rem * 10 + dig) % k

                    ans += dfs(
                        pos + 1,
                        diff_idx2,
                        rem2,
                        1 if started2 else 0,
                        1 if (tight and dig == limit) else 0
                    )
                return ans

            # The "tight" transition above is incorrect: we used limit, not digit[pos].
            # Fix by rewriting dfs with correct tight handling.

            dfs.cache_clear()

            @lru_cache(None)
            def dfs(pos: int, diff_idx: int, rem: int, started: int, tight: int) -> int:
                if pos == m:
                    if started == 0:
                        return 0
                    return 1 if diff_idx == offset and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                ans = 0
                for dig in range(0, limit + 1):
                    started2 = started or (dig != 0)

                    diff_idx2 = diff_idx
                    rem2 = rem

                    if started2:
                        if dig % 2 == 0:
                            diff_idx2 += 1
                        else:
                            diff_idx2 -= 1
                        rem2 = (rem * 10 + dig) % k

                    if diff_idx2 < 0 or diff_idx2 >= size_diff:
                        continue

                    ans += dfs(
                        pos + 1,
                        diff_idx2,
                        rem2,
                        1 if started2 else 0,
                        1 if (tight and dig == limit) else 0
                    )
                return ans

            # Correct tight update should compare dig with digits[pos] when tight==1.
            # Since limit equals digits[pos] in that case, using dig == limit is correct.

            return dfs(0, offset, 0, 0, 1)

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```

Attempt 4
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            s = str(n)
            m = len(s)
            digits = list(map(int, s))

            @lru_cache(None)
            def dp(pos: int, diff: int, mod: int, tight: int, started: int) -> int:
                # diff = (#even - #odd) so far, on started part
                if pos == m:
                    return 1 if started and diff == 0 and mod == 0 else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    nstarted = started or (d != 0)
                    if not nstarted:
                        # still not started: don't count digits, diff/mod remain
                        res += dp(pos + 1, diff, mod, ntight, 0)
                    else:
                        ndiff = diff + (1 if (d % 2 == 0) else -1)
                        nmod = (mod * 10 + d) % k
                        res += dp(pos + 1, ndiff, nmod, ntight, 1)
                return res

            # diff range is [-m, m], state space is manageable for m<=10
            return dp(0, 0, 0, 1, 0)

        return count_upto(high) - count_upto(low - 1)
```

Attempt 5
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][diff][rem][tight][started]
            # diff = (#even - #odd) among digits chosen so far
            # Rem = value mod k
            # We use dict maps to keep state small.
            from collections import defaultdict

            # Use offset so diff indices are non-negative
            # diff range in absolute value <= m, so [-m..m]
            offset = m

            # Initialize at pos 0
            dp = { (0, 0, 0, True, False): 1 }  # (pos, diff, rem, tight, started) -> count

            for pos in range(m):
                new_dp = defaultdict(int)
                limit_digit = digits[pos]
                for (p, diff, rem, tight, started), ways in dp.items():
                    # p should equal pos
                    mx = limit_digit if tight else 9
                    for dig in range(mx + 1):
                        ntight = tight and (dig == mx if not tight else dig == limit_digit)
                        # careful with ntight:
                        ntight = tight and (dig == limit_digit)

                        if not started and dig == 0:
                            # Still not started; diff/rem unchanged
                            # Note: number length shorter than m.
                            nstarted = False
                            ndiff = diff
                            nrem = 0  # irrelevant while not started; keep 0
                            new_dp[(pos + 1, ndiff, nrem, ntight, nstarted)] += ways
                        else:
                            nstarted = True
                            if dig % 2 == 0:
                                ndiff = diff + 1
                            else:
                                ndiff = diff - 1
                            nrem = (rem * 10 + dig) % k
                            new_dp[(pos + 1, ndiff, nrem, ntight, nstarted)] += ways
                dp = new_dp

            # Final count: started must be True, diff must be 0, rem must be 0
            ans = 0
            for (p, diff, rem, tight, started), ways in dp.items():
                if p != m:
                    continue
                if started and diff == 0 and rem % k == 0:
                    ans += ways
            return ans

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```

Attempt 6
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)

            # dp[pos][diff_offset][rem][tight] -> count
            # diff = even_count - odd_count, range [-L..L], offset by L
            offset = L
            size = 2 * L + 1

            # Use two layers for pos to save memory.
            # We'll represent dp[tight] as dict for sparse remainder/diff, but k<=20 so
            # dense over rem is fine; keep arrays for speed.
            # dp_tight0/1: at each pos, with diff and remainder.
            import array

            # dp arrays: [diff][rem]
            def make_layer():
                return [[0] * k for _ in range(size)]

            dp_tight0 = make_layer()  # tight=0
            dp_tight1 = make_layer()  # tight=1

            # start: no digits yet, diff=0, rem=0
            dp_tight1[offset][0] = 1

            for pos, lim in enumerate(digits):
                ndp_tight0 = make_layer()
                ndp_tight1 = make_layer()

                for diff_idx in range(size):
                    for rem in range(k):
                        # tight = 0 transitions (already below prefix)
                        cnt0 = dp_tight0[diff_idx][rem]
                        if cnt0:
                            cur_diff = diff_idx - offset
                            for d in range(10):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    ndp_tight0[ndiff + offset][nrem] += cnt0

                        # tight = 1 transitions (follow prefix)
                        cnt1 = dp_tight1[diff_idx][rem]
                        if cnt1:
                            cur_diff = diff_idx - offset
                            for d in range(lim + 1):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    if d == lim:
                                        ndp_tight1[ndiff + offset][nrem] += cnt1
                                    else:
                                        ndp_tight0[ndiff + offset][nrem] += cnt1

                dp_tight0, dp_tight1 = ndp_tight0, ndp_tight1

            # We count only numbers with equal even/odd digit counts => diff==0
            # and divisible by k => rem==0.
            # Also must exclude leading zeros because the representation has exactly L digits.
            # Our DP currently allows leading zeros as actual digits, which would affect parity counts.
            # Fix: count numbers in [0..n] with exactly L digits including leading zeros, then subtract those
            # with leading zeros by computing for length < L and using digit-DP on exact length.
            # Instead, we correct by using a standard trick: disallow leading zero by tracking started flag.
            # We'll implement a second DP that includes "started" to ensure correct digit parity counts.
            return count_upto_with_started(n)

        def count_upto_with_started(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            offset = L
            size = 2 * L + 1

            def make_layer():
                return [[0] * k for _ in range(size)]

            # dp[tight][started][diff][rem]
            # We'll use two tight layers and started flag.
            dp00 = make_layer()  # tight=0, started=0
            dp01 = make_layer()  # tight=0, started=1
            dp10 = make_layer()  # tight=1, started=0
            dp11 = make_layer()  # tight=1, started=1

            # started=0: no digits placed yet => diff=0, rem=0
            dp10[offset][0] = 1

            for pos, lim in enumerate(digits):
                ndp00 = make_layer()
                ndp01 = make_layer()
                ndp10 = make_layer()
                ndp11 = make_layer()

                for diff_idx in range(size):
                    for rem in range(k):
                        cur_diff = diff_idx - offset

                        # tight=0, started=0
                        cnt = dp00[diff_idx][rem]
                        if cnt:
                            for d in range(10):
                                if d == 0:
                                    # still not started
                                    ndiff = cur_diff
                                    nrem = 0  # rem irrelevant while not started; keep 0
                                    ndp00[ndiff + offset][nrem] += cnt
                                else:
                                    ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                    nrem = d % k
                                    if -L <= ndiff <= L:
                                        ndp01[ndiff + offset][nrem] += cnt

                        # tight=0, started=1
                        cnt = dp01[diff_idx][rem]
                        if cnt:
                            for d in range(10):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    ndp01[ndiff + offset][nrem] += cnt

                        # tight=1, started=0
                        cnt = dp10[diff_idx][rem]
                        if cnt:
                            for d in range(lim + 1):
                                tight1 = (d == lim)
                                if d == 0:
                                    ndiff = cur_diff
                                    nrem = 0
                                    if tight1:
                                        ndp10[ndiff + offset][nrem] += cnt
                                    else:
                                        ndp00[ndiff + offset][nrem] += cnt
                                else:
                                    ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                    if -L <= ndiff <= L:
                                        nrem = d % k
                                        if tight1:
                                            ndp11[ndiff + offset][nrem] += cnt
                                        else:
                                            ndp01[ndiff + offset][nrem] += cnt

                        # tight=1, started=1
                        cnt = dp11[diff_idx][rem]
                        if cnt:
                            for d in range(lim + 1):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    if d == lim:
                                        ndp11[ndiff + offset][nrem] += cnt
                                    else:
                                        ndp01[ndiff + offset][nrem] += cnt

                dp00, dp01, dp10, dp11 = ndp00, ndp01, ndp10, ndp11

            # Count started=1 only (exclude 0)
            return dp01[offset][0] + dp11[offset][0]

        return count_upto(high) - count_upto(low - 1)
```

#### Partially Correct
Attempt 1
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][balance][mod][tight_started]
            # balance = (#even - #odd), must end at 0
            # Use offset to index negative balances.
            off = 20  # safe because balance range within [-m, m] and m<=10
            # We'll track started = whether we have placed a non-leading-zero digit.
            # Leading zeros do not contribute digits (so parity counts ignore them).
            from collections import defaultdict

            dp = defaultdict(int)
            # state: (balance, mod, started) -> ways
            dp[(0, 0, 0)] = 1

            for pos, lim in enumerate(digits):
                ndp = defaultdict(int)
                for (bal, mod, started), ways in dp.items():
                    for d in range(0, lim + 1):
                        nstarted = started or (d != 0)
                        if not nstarted:
                            # still leading zeros: no digit contributes
                            nbal, nmod = bal, 0  # mod should be 0 because no meaningful digits yet
                            # But to be consistent, if not started we keep mod=0.
                            nt = 0  # started flag tracked
                        else:
                            # determine parity contribution
                            if d % 2 == 0:
                                nbal = bal + 1
                            else:
                                nbal = bal - 1
                            nmod = (mod * 10 + d) % k

                        if nstarted:
                            # started is 1
                            ndp[(nbal, nmod, 1)] += ways
                        else:
                            ndp[(nbal, nmod, 0)] += ways

                dp = ndp

            # Now dp includes numbers with varying length up to m, including 0.
            # We need numbers in [1..n], so exclude number 0: started must be 1.
            ans = 0
            for (bal, mod, started), ways in dp.items():
                if started == 1 and bal == 0 and mod % k == 0:
                    ans += ways
            return ans

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```

Attempt 2
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(x: int) -> int:
            if x <= 0:
                return 0

            s = str(x)
            n = len(s)

            # dp[pos][diff][rem][tight] not used; we do iterative DP with tight.
            # diff = even_count - odd_count, must end at 0
            # diff range: [-n, n] but we can keep offset
            offset = n
            size_diff = 2 * n + 1

            from collections import defaultdict

            # states: rem, diff -> count
            cur = defaultdict(int)
            cur[(0, 0)] = 1  # before placing any digit: rem=0, diff=0, count=1

            for i, ch in enumerate(s):
                digit_limit = int(ch)
                nxt = defaultdict(int)

                tight_states = [(0, cur)]  # dummy, we handle tight by splitting keys
                # We'll do classic digit DP keeping "tight" as part of key.
                # To simplify: we reinitialize with proper structure per position using dicts keyed by (tight, rem, diff).
                # But easiest: maintain two layers: tight=0/1.

            # Re-implement cleanly with tight state:
            cur = {(1, 0, 0): 1}  # (tight, rem, diff) -> ways

            for i, ch in enumerate(s):
                limit = int(ch)
                nxt = {}
                for (tight, rem, diff), ways in cur.items():
                    max_d = limit if tight == 1 else 9
                    for d in range(max_d + 1):
                        ntight = 1 if (tight == 1 and d == max_d) else 0
                        # update rem
                        nrem = (rem * 10 + d) % k
                        # update diff: even digit +1, odd digit -1
                        ndiff = diff + (1 if d % 2 == 0 else -1)
                        key = (ntight, nrem, ndiff)
                        nxt[key] = nxt.get(key, 0) + ways
                cur = nxt

            # We counted leading zeros as digits too; but that's fine because:
            # - leading zeros contribute even digits (0 is even),
            # - we want numbers in [1..x], not including 0.
            # Our DP includes 0..x inclusive, but only numbers whose diff ends at 0 and rem at 0.
            # For x>0, number 0 could be counted; ensure it's excluded.
            ans = 0
            for (tight, rem, diff), ways in cur.items():
                if rem == 0 and diff == 0:
                    # tight can be 0 or 1; both are included in dp results.
                    ans += ways

            # Exclude number 0 if it was counted.
            # Number 0 has all digits as '0' (length n), so diff = (#even) - 0 = n, not 0 unless n=0.
            # So it won't be counted. But to be safe, handle x==0 already returns 0.
            return ans

        # Digit DP above used a simplified ntight calculation that is incorrect.
        # We'll correct by rewriting with proper tight transitions.

        def count_beautiful_upto_fixed(x: int) -> int:
            if x <= 0:
                return 0
            s = str(x)
            n = len(s)

            cur = {(1, 0, 0): 1}  # (tight, rem, diff) -> ways; diff is even-odd across n digits

            for i, ch in enumerate(s):
                limit = int(ch)
                nxt = {}
                for (tight, rem, diff), ways in cur.items():
                    max_d = limit if tight == 1 else 9
                    for d in range(max_d + 1):
                        ntight = 1 if (tight == 1 and d == limit) else 0
                        nrem = (rem * 10 + d) % k
                        ndiff = diff + (1 if d % 2 == 0 else -1)
                        key = (ntight, nrem, ndiff)
                        nxt[key] = nxt.get(key, 0) + ways
                cur = nxt

            ans = 0
            for (tight, rem, diff), ways in cur.items():
                if rem == 0 and diff == 0:
                    ans += ways
            return ans

        return count_beautiful_upto_fixed(high) - count_beautiful_upto_fixed(low - 1)
```

Attempt 3
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_up_to(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)
            # shift even_minus_odd by +L (range [-L, L])
            SHIFT = L
            OFFSET = 2 * L + 1

            # dp[pos][diff_index][mod] = ways, using rolling arrays
            # diff = (#even - #odd) so that equality (#even == #odd) => diff == 0
            dp = [[0] * k for _ in range(OFFSET)]
            dp[SHIFT][0] = 1

            for i in range(L):
                ndp = [[0] * k for _ in range(OFFSET)]
                limit = digits[i]
                for diff_i in range(OFFSET):
                    for mod in range(k):
                        ways = dp[diff_i][mod]
                        if ways == 0:
                            continue
                        diff = diff_i - SHIFT
                        for d in range(0, limit + 1):
                            new_diff = diff + (1 if d % 2 == 0 else -1)
                            new_diff_i = new_diff + SHIFT
                            if 0 <= new_diff_i < OFFSET:
                                new_mod = (mod * 10 + d) % k
                                ndp[new_diff_i][new_mod] += ways
                dp = ndp

            # Count numbers with diff==0 and mod==0, but must exclude 0 itself.
            # Our digit-DP counts all L-digit sequences with leading zeros allowed,
            # which includes the all-zero number. That number has diff=+L (all even digits),
            # so it won't be counted anyway. However, we still ensure we don't count
            # numbers outside [1..n] by using diff==0 and mod==0.
            return dp[SHIFT][0]

        return count_up_to(high) - count_up_to(low - 1)
```

Attempt 4
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(x: int) -> int:
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            # dp[pos][diff][rem][started]
            # diff = even_count - odd_count, shift by +n to make non-negative
            # rem = number mod k
            # started = whether we've placed any non-leading-zero digit
            shift = n
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, diff: int, rem: int, started: int) -> int:
                if pos == n:
                    if not started:
                        return 0  # exclude 0
                    return 1 if diff == 0 and rem == 0 else 0

                limit = digits[pos]
                total = 0
                for d in range(0, limit + 1):
                    nt_started = started or d != 0
                    if not nt_started:
                        # still leading zeros: diff and rem unchanged
                        total += dfs(pos + 1, diff, rem, 0)
                    else:
                        ndiff = diff
                        if d % 2 == 0:
                            ndiff += 1
                        else:
                            ndiff -= 1
                        nrem = (rem * 10 + d) % k
                        total += dfs(pos + 1, ndiff, nrem, 1)
                return total

            # bound diff within [-n, n]
            # Our recursion never steps outside when starting from 0; still safe.
            return dfs(0, shift, 0, 0)

        return count_upto(high) - count_upto(low - 1)
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
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)

            # DP over positions:
            # diff = (#even - #odd) shifted by +L (so range [-L..L])
            # rem = remainder mod k
            offset = L
            size_diff = 2 * L + 1

            # dp[pos][diff][rem] as rolling arrays
            # Using list comprehension for speed.
            dp = [[0] * k for _ in range(size_diff)]
            dp[offset][0] = 1  # at pos 0, diff=0, rem=0

            tight = [True]  # dummy to help structure; we'll use 4D rolling via dicts per tight state
            # We'll keep separate dp for tight/not tight.
            dp_tight = [[0] * k for _ in range(size_diff)]
            dp_not = [[0] * k for _ in range(size_diff)]
            dp_tight[offset][0] = 1

            for pos in range(L):
                next_tight = [[0] * k for _ in range(size_diff)]
                next_not = [[0] * k for _ in range(size_diff)]

                limit = digits[pos]

                # Transition for tight states
                for diff_i in range(size_diff):
                    row = dp_tight[diff_i]
                    if not any(row):
                        continue
                    for rem in range(k):
                        ways = row[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(limit + 1):
                            n_tight = (dig == limit)
                            new_rem = (rem * 10 + dig) % k
                            new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                            new_diff_i = new_diff + offset
                            if n_tight:
                                next_tight[new_diff_i][new_rem] += ways
                            else:
                                next_not[new_diff_i][new_rem] += ways

                # Transition for not tight states (limit=9)
                for diff_i in range(size_diff):
                    row = dp_not[diff_i]
                    if not any(row):
                        continue
                    for rem in range(k):
                        ways = row[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(10):
                            new_rem = (rem * 10 + dig) % k
                            new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                            new_diff_i = new_diff + offset
                            next_not[new_diff_i][new_rem] += ways

                dp_tight, dp_not = next_tight, next_not

            # Need exactly equal even/odd digits => diff = 0
            # Also exclude the number 0 (not in positive integers). Our DP counts all L-digit numbers including leading zeros.
            # Leading zeros contribute digits, but they are even digits (0), which changes diff.
            # To handle correctly, compute for each length separately without leading zeros by fixing first digit > 0.
            # Instead, we correct by subtracting count for numbers with leading zeros not allowed:
            # Easier: run a digit DP that disallows leading zero by treating "not started" state.
            # We'll implement that below and replace count_upto with correct one.

            return 0  # placeholder (will be overwritten)

        # Correct digit DP: keep started flag to avoid leading zeros affecting digit parity count.
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            offset = L
            size_diff = 2 * L + 1

            # dp[started][diff_i][rem]
            dp_started = [[0] * k for _ in range(size_diff)]
            dp_not = [[0] * k for _ in range(size_diff)]
            # started=False: no digits chosen yet => diff=0 rem=0
            dp_not[offset][0] = 1

            for pos in range(L):
                next_started = [[0] * k for _ in range(size_diff)]
                next_not = [[0] * k for _ in range(size_diff)]
                limit = digits[pos]

                for diff_i in range(size_diff):
                    # not started
                    row0 = dp_not[diff_i]
                    if not any(row0):
                        pass
                    for rem in range(k):
                        ways = row0[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(limit + 1):
                            n_started = (dig != 0)
                            new_rem = (rem * 10 + dig) % k if n_started else 0
                            if not n_started:
                                next_diff_i = offset  # still diff=0 because no digits counted
                                if dig == limit:
                                    next_not[next_diff_i][new_rem] += ways
                                else:
                                    next_not[next_diff_i][new_rem] += ways
                            else:
                                new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                                new_diff_i = new_diff + offset
                                if dig == limit:
                                    next_started[new_diff_i][new_rem] += ways
                                else:
                                    next_started[new_diff_i][new_rem] += ways

                    # started
                    row1 = dp_started[diff_i]
                    if not any(row1):
                        pass
                    for rem in range(k):
                        ways = row1[rem]
                        if ways == 0:
                            continue
                        cur_diff = diff_i - offset
                        for dig in range(limit + 1):
                            new_rem = (rem * 10 + dig) % k
                            new_diff = cur_diff + (1 if (dig % 2 == 0) else -1)
                            new_diff_i = new_diff + offset
                            if dig == limit:
                                next_started[new_diff_i][new_rem] += ways
                            else:
                                next_started[new_diff_i][new_rem] += ways

                # The above transitions ignore the "tight" aspect; so it's incorrect.
                # We'll implement proper tight DP.

                # ---- Implement proper tight DP below and return immediately (replacing this whole function) ----
                return 0

            return 0  # unused

        # Proper digit DP with memoization: tight + started + diff + rem
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            offset = L
            size_diff = 2 * L + 1

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, diff_i: int, rem: int) -> int:
                if pos == L:
                    if started == 1 and diff_i == offset and rem == 0:
                        return 1
                    return 0

                limit = digits[pos] if tight else 9
                total = 0
                cur_diff = diff_i - offset

                for dig in range(limit + 1):
                    ntight = 1 if (tight and dig == limit) else 0
                    if started == 0 and dig == 0:
                        # still not started; diff stays 0, rem stays 0
                        total += dp(pos + 1, ntight, 0, offset, 0)
                    else:
                        if started == 0:
                            new_diff = (1 if dig % 2 == 0 else -1)
                            new_diff_i = new_diff + offset
                            new_rem = dig % k
                            total += dp(pos + 1, ntight, 1, new_diff_i, new_rem)
                        else:
                            new_diff = cur_diff + (1 if dig % 2 == 0 else -1)
                            new_diff_i = new_diff + offset
                            new_rem = (rem * 10 + dig) % k
                            total += dp(pos + 1, ntight, 1, new_diff_i, new_rem)
                return total

            return dp(0, 1, 0, offset, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(x: int) -> int:
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            # dp[pos][diff+offset][rem][tight][started]
            # diff = #odd - #even among digits chosen after starting (zeros in front not counted)
            offset = n  # diff range [-n, n]
            from functools import lru_cache

            @lru_cache(None)
            def dp(pos: int, diff: int, rem: int, tight: int, started: int) -> int:
                if pos == n:
                    # Beautiful if started and diff == 0 and remainder == 0
                    # Note: "count of even digits equals count of odd digits" => diff == 0
                    return 1 if started and diff == 0 and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                total = 0

                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0

                    if started == 0 and d == 0:
                        # still not started: don't count digit, keep remainder as 0
                        total += dp(pos + 1, diff, 0, ntight, 0)
                    else:
                        # started (leading zeros are no longer possible)
                        # update diff by digit parity; update remainder with digit
                        if d % 2 == 0:
                            ndiff = diff - 1  # even increases even count => odd-even decreases
                        else:
                            ndiff = diff + 1  # odd increases odd count => odd-even increases
                        nrem = (rem * 10 + d) % k
                        total += dp(pos + 1, ndiff, nrem, ntight, 1)

                return total

            return dp(0, 0, 0, 1, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][diff][rem][started] but keep it compact:
            # diff = even_count - odd_count, shifted by +offset
            # diff range is [-m, m]
            offset = m
            size_diff = 2 * m + 1
            MOD = 10**18  # no mod needed; just avoid accidental large issues

            # Use dict-based DP to keep states manageable:
            # key: (diff_index, rem, started)
            cur = {(offset, 0, 0): 1}

            for pos in range(m):
                nd = digits[pos]
                nxt = {}
                for (diff_idx, rem, started), ways in cur.items():
                    for dig in range(0, nd + 1):
                        tight_new = False  # handled by per-digit approach below
                    # We will do standard tight DP by including tight in state.
                # Let's redo with tight properly (dict states)

            # Standard digit DP with memoization:
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, diff_idx: int, rem: int, started: int, tight: int) -> int:
                if pos == m:
                    # If never started => number 0, exclude (range starts from >=1)
                    if started == 0:
                        return 0
                    return 1 if diff_idx == offset and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                ans = 0
                for dig in range(0, limit + 1):
                    started2 = started or (dig != 0)
                    diff_idx2 = diff_idx

                    if started2:
                        if dig % 2 == 0:
                            diff_idx2 += 1  # even digit
                        else:
                            diff_idx2 -= 1  # odd digit

                    # Only keep diff within [-m, m]
                    if diff_idx2 < 0 or diff_idx2 >= size_diff:
                        continue

                    rem2 = rem
                    if started2:
                        rem2 = (rem * 10 + dig) % k

                    ans += dfs(
                        pos + 1,
                        diff_idx2,
                        rem2,
                        1 if started2 else 0,
                        1 if (tight and dig == limit) else 0
                    )
                return ans

            # The "tight" transition above is incorrect: we used limit, not digit[pos].
            # Fix by rewriting dfs with correct tight handling.

            dfs.cache_clear()

            @lru_cache(None)
            def dfs(pos: int, diff_idx: int, rem: int, started: int, tight: int) -> int:
                if pos == m:
                    if started == 0:
                        return 0
                    return 1 if diff_idx == offset and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                ans = 0
                for dig in range(0, limit + 1):
                    started2 = started or (dig != 0)

                    diff_idx2 = diff_idx
                    rem2 = rem

                    if started2:
                        if dig % 2 == 0:
                            diff_idx2 += 1
                        else:
                            diff_idx2 -= 1
                        rem2 = (rem * 10 + dig) % k

                    if diff_idx2 < 0 or diff_idx2 >= size_diff:
                        continue

                    ans += dfs(
                        pos + 1,
                        diff_idx2,
                        rem2,
                        1 if started2 else 0,
                        1 if (tight and dig == limit) else 0
                    )
                return ans

            # Correct tight update should compare dig with digits[pos] when tight==1.
            # Since limit equals digits[pos] in that case, using dig == limit is correct.

            return dfs(0, offset, 0, 0, 1)

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            s = str(n)
            m = len(s)
            digits = list(map(int, s))

            @lru_cache(None)
            def dp(pos: int, diff: int, mod: int, tight: int, started: int) -> int:
                # diff = (#even - #odd) so far, on started part
                if pos == m:
                    return 1 if started and diff == 0 and mod == 0 else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    nstarted = started or (d != 0)
                    if not nstarted:
                        # still not started: don't count digits, diff/mod remain
                        res += dp(pos + 1, diff, mod, ntight, 0)
                    else:
                        ndiff = diff + (1 if (d % 2 == 0) else -1)
                        nmod = (mod * 10 + d) % k
                        res += dp(pos + 1, ndiff, nmod, ntight, 1)
                return res

            # diff range is [-m, m], state space is manageable for m<=10
            return dp(0, 0, 0, 1, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][diff][rem][tight][started]
            # diff = (#even - #odd) among digits chosen so far
            # Rem = value mod k
            # We use dict maps to keep state small.
            from collections import defaultdict

            # Use offset so diff indices are non-negative
            # diff range in absolute value <= m, so [-m..m]
            offset = m

            # Initialize at pos 0
            dp = { (0, 0, 0, True, False): 1 }  # (pos, diff, rem, tight, started) -> count

            for pos in range(m):
                new_dp = defaultdict(int)
                limit_digit = digits[pos]
                for (p, diff, rem, tight, started), ways in dp.items():
                    # p should equal pos
                    mx = limit_digit if tight else 9
                    for dig in range(mx + 1):
                        ntight = tight and (dig == mx if not tight else dig == limit_digit)
                        # careful with ntight:
                        ntight = tight and (dig == limit_digit)

                        if not started and dig == 0:
                            # Still not started; diff/rem unchanged
                            # Note: number length shorter than m.
                            nstarted = False
                            ndiff = diff
                            nrem = 0  # irrelevant while not started; keep 0
                            new_dp[(pos + 1, ndiff, nrem, ntight, nstarted)] += ways
                        else:
                            nstarted = True
                            if dig % 2 == 0:
                                ndiff = diff + 1
                            else:
                                ndiff = diff - 1
                            nrem = (rem * 10 + dig) % k
                            new_dp[(pos + 1, ndiff, nrem, ntight, nstarted)] += ways
                dp = new_dp

            # Final count: started must be True, diff must be 0, rem must be 0
            ans = 0
            for (p, diff, rem, tight, started), ways in dp.items():
                if p != m:
                    continue
                if started and diff == 0 and rem % k == 0:
                    ans += ways
            return ans

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)

            # dp[pos][diff_offset][rem][tight] -> count
            # diff = even_count - odd_count, range [-L..L], offset by L
            offset = L
            size = 2 * L + 1

            # Use two layers for pos to save memory.
            # We'll represent dp[tight] as dict for sparse remainder/diff, but k<=20 so
            # dense over rem is fine; keep arrays for speed.
            # dp_tight0/1: at each pos, with diff and remainder.
            import array

            # dp arrays: [diff][rem]
            def make_layer():
                return [[0] * k for _ in range(size)]

            dp_tight0 = make_layer()  # tight=0
            dp_tight1 = make_layer()  # tight=1

            # start: no digits yet, diff=0, rem=0
            dp_tight1[offset][0] = 1

            for pos, lim in enumerate(digits):
                ndp_tight0 = make_layer()
                ndp_tight1 = make_layer()

                for diff_idx in range(size):
                    for rem in range(k):
                        # tight = 0 transitions (already below prefix)
                        cnt0 = dp_tight0[diff_idx][rem]
                        if cnt0:
                            cur_diff = diff_idx - offset
                            for d in range(10):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    ndp_tight0[ndiff + offset][nrem] += cnt0

                        # tight = 1 transitions (follow prefix)
                        cnt1 = dp_tight1[diff_idx][rem]
                        if cnt1:
                            cur_diff = diff_idx - offset
                            for d in range(lim + 1):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    if d == lim:
                                        ndp_tight1[ndiff + offset][nrem] += cnt1
                                    else:
                                        ndp_tight0[ndiff + offset][nrem] += cnt1

                dp_tight0, dp_tight1 = ndp_tight0, ndp_tight1

            # We count only numbers with equal even/odd digit counts => diff==0
            # and divisible by k => rem==0.
            # Also must exclude leading zeros because the representation has exactly L digits.
            # Our DP currently allows leading zeros as actual digits, which would affect parity counts.
            # Fix: count numbers in [0..n] with exactly L digits including leading zeros, then subtract those
            # with leading zeros by computing for length < L and using digit-DP on exact length.
            # Instead, we correct by using a standard trick: disallow leading zero by tracking started flag.
            # We'll implement a second DP that includes "started" to ensure correct digit parity counts.
            return count_upto_with_started(n)

        def count_upto_with_started(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            offset = L
            size = 2 * L + 1

            def make_layer():
                return [[0] * k for _ in range(size)]

            # dp[tight][started][diff][rem]
            # We'll use two tight layers and started flag.
            dp00 = make_layer()  # tight=0, started=0
            dp01 = make_layer()  # tight=0, started=1
            dp10 = make_layer()  # tight=1, started=0
            dp11 = make_layer()  # tight=1, started=1

            # started=0: no digits placed yet => diff=0, rem=0
            dp10[offset][0] = 1

            for pos, lim in enumerate(digits):
                ndp00 = make_layer()
                ndp01 = make_layer()
                ndp10 = make_layer()
                ndp11 = make_layer()

                for diff_idx in range(size):
                    for rem in range(k):
                        cur_diff = diff_idx - offset

                        # tight=0, started=0
                        cnt = dp00[diff_idx][rem]
                        if cnt:
                            for d in range(10):
                                if d == 0:
                                    # still not started
                                    ndiff = cur_diff
                                    nrem = 0  # rem irrelevant while not started; keep 0
                                    ndp00[ndiff + offset][nrem] += cnt
                                else:
                                    ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                    nrem = d % k
                                    if -L <= ndiff <= L:
                                        ndp01[ndiff + offset][nrem] += cnt

                        # tight=0, started=1
                        cnt = dp01[diff_idx][rem]
                        if cnt:
                            for d in range(10):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    ndp01[ndiff + offset][nrem] += cnt

                        # tight=1, started=0
                        cnt = dp10[diff_idx][rem]
                        if cnt:
                            for d in range(lim + 1):
                                tight1 = (d == lim)
                                if d == 0:
                                    ndiff = cur_diff
                                    nrem = 0
                                    if tight1:
                                        ndp10[ndiff + offset][nrem] += cnt
                                    else:
                                        ndp00[ndiff + offset][nrem] += cnt
                                else:
                                    ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                    if -L <= ndiff <= L:
                                        nrem = d % k
                                        if tight1:
                                            ndp11[ndiff + offset][nrem] += cnt
                                        else:
                                            ndp01[ndiff + offset][nrem] += cnt

                        # tight=1, started=1
                        cnt = dp11[diff_idx][rem]
                        if cnt:
                            for d in range(lim + 1):
                                ndiff = cur_diff + (1 if d % 2 == 0 else -1)
                                if -L <= ndiff <= L:
                                    nrem = (rem * 10 + d) % k
                                    if d == lim:
                                        ndp11[ndiff + offset][nrem] += cnt
                                    else:
                                        ndp01[ndiff + offset][nrem] += cnt

                dp00, dp01, dp10, dp11 = ndp00, ndp01, ndp10, ndp11

            # Count started=1 only (exclude 0)
            return dp01[offset][0] + dp11[offset][0]

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

#### Tier: `partial`

<details>
<summary>partial attempt 1</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][balance][mod][tight_started]
            # balance = (#even - #odd), must end at 0
            # Use offset to index negative balances.
            off = 20  # safe because balance range within [-m, m] and m<=10
            # We'll track started = whether we have placed a non-leading-zero digit.
            # Leading zeros do not contribute digits (so parity counts ignore them).
            from collections import defaultdict

            dp = defaultdict(int)
            # state: (balance, mod, started) -> ways
            dp[(0, 0, 0)] = 1

            for pos, lim in enumerate(digits):
                ndp = defaultdict(int)
                for (bal, mod, started), ways in dp.items():
                    for d in range(0, lim + 1):
                        nstarted = started or (d != 0)
                        if not nstarted:
                            # still leading zeros: no digit contributes
                            nbal, nmod = bal, 0  # mod should be 0 because no meaningful digits yet
                            # But to be consistent, if not started we keep mod=0.
                            nt = 0  # started flag tracked
                        else:
                            # determine parity contribution
                            if d % 2 == 0:
                                nbal = bal + 1
                            else:
                                nbal = bal - 1
                            nmod = (mod * 10 + d) % k

                        if nstarted:
                            # started is 1
                            ndp[(nbal, nmod, 1)] += ways
                        else:
                            ndp[(nbal, nmod, 0)] += ways

                dp = ndp

            # Now dp includes numbers with varying length up to m, including 0.
            # We need numbers in [1..n], so exclude number 0: started must be 1.
            ans = 0
            for (bal, mod, started), ways in dp.items():
                if started == 1 and bal == 0 and mod % k == 0:
                    ans += ways
            return ans

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```
```

</details>

<details>
<summary>partial attempt 2</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_beautiful_upto(x: int) -> int:
            if x <= 0:
                return 0

            s = str(x)
            n = len(s)

            # dp[pos][diff][rem][tight] not used; we do iterative DP with tight.
            # diff = even_count - odd_count, must end at 0
            # diff range: [-n, n] but we can keep offset
            offset = n
            size_diff = 2 * n + 1

            from collections import defaultdict

            # states: rem, diff -> count
            cur = defaultdict(int)
            cur[(0, 0)] = 1  # before placing any digit: rem=0, diff=0, count=1

            for i, ch in enumerate(s):
                digit_limit = int(ch)
                nxt = defaultdict(int)

                tight_states = [(0, cur)]  # dummy, we handle tight by splitting keys
                # We'll do classic digit DP keeping "tight" as part of key.
                # To simplify: we reinitialize with proper structure per position using dicts keyed by (tight, rem, diff).
                # But easiest: maintain two layers: tight=0/1.

            # Re-implement cleanly with tight state:
            cur = {(1, 0, 0): 1}  # (tight, rem, diff) -> ways

            for i, ch in enumerate(s):
                limit = int(ch)
                nxt = {}
                for (tight, rem, diff), ways in cur.items():
                    max_d = limit if tight == 1 else 9
                    for d in range(max_d + 1):
                        ntight = 1 if (tight == 1 and d == max_d) else 0
                        # update rem
                        nrem = (rem * 10 + d) % k
                        # update diff: even digit +1, odd digit -1
                        ndiff = diff + (1 if d % 2 == 0 else -1)
                        key = (ntight, nrem, ndiff)
                        nxt[key] = nxt.get(key, 0) + ways
                cur = nxt

            # We counted leading zeros as digits too; but that's fine because:
            # - leading zeros contribute even digits (0 is even),
            # - we want numbers in [1..x], not including 0.
            # Our DP includes 0..x inclusive, but only numbers whose diff ends at 0 and rem at 0.
            # For x>0, number 0 could be counted; ensure it's excluded.
            ans = 0
            for (tight, rem, diff), ways in cur.items():
                if rem == 0 and diff == 0:
                    # tight can be 0 or 1; both are included in dp results.
                    ans += ways

            # Exclude number 0 if it was counted.
            # Number 0 has all digits as '0' (length n), so diff = (#even) - 0 = n, not 0 unless n=0.
            # So it won't be counted. But to be safe, handle x==0 already returns 0.
            return ans

        # Digit DP above used a simplified ntight calculation that is incorrect.
        # We'll correct by rewriting with proper tight transitions.

        def count_beautiful_upto_fixed(x: int) -> int:
            if x <= 0:
                return 0
            s = str(x)
            n = len(s)

            cur = {(1, 0, 0): 1}  # (tight, rem, diff) -> ways; diff is even-odd across n digits

            for i, ch in enumerate(s):
                limit = int(ch)
                nxt = {}
                for (tight, rem, diff), ways in cur.items():
                    max_d = limit if tight == 1 else 9
                    for d in range(max_d + 1):
                        ntight = 1 if (tight == 1 and d == limit) else 0
                        nrem = (rem * 10 + d) % k
                        ndiff = diff + (1 if d % 2 == 0 else -1)
                        key = (ntight, nrem, ndiff)
                        nxt[key] = nxt.get(key, 0) + ways
                cur = nxt

            ans = 0
            for (tight, rem, diff), ways in cur.items():
                if rem == 0 and diff == 0:
                    ans += ways
            return ans

        return count_beautiful_upto_fixed(high) - count_beautiful_upto_fixed(low - 1)
```
```

</details>

<details>
<summary>partial attempt 3</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_up_to(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)
            # shift even_minus_odd by +L (range [-L, L])
            SHIFT = L
            OFFSET = 2 * L + 1

            # dp[pos][diff_index][mod] = ways, using rolling arrays
            # diff = (#even - #odd) so that equality (#even == #odd) => diff == 0
            dp = [[0] * k for _ in range(OFFSET)]
            dp[SHIFT][0] = 1

            for i in range(L):
                ndp = [[0] * k for _ in range(OFFSET)]
                limit = digits[i]
                for diff_i in range(OFFSET):
                    for mod in range(k):
                        ways = dp[diff_i][mod]
                        if ways == 0:
                            continue
                        diff = diff_i - SHIFT
                        for d in range(0, limit + 1):
                            new_diff = diff + (1 if d % 2 == 0 else -1)
                            new_diff_i = new_diff + SHIFT
                            if 0 <= new_diff_i < OFFSET:
                                new_mod = (mod * 10 + d) % k
                                ndp[new_diff_i][new_mod] += ways
                dp = ndp

            # Count numbers with diff==0 and mod==0, but must exclude 0 itself.
            # Our digit-DP counts all L-digit sequences with leading zeros allowed,
            # which includes the all-zero number. That number has diff=+L (all even digits),
            # so it won't be counted anyway. However, we still ensure we don't count
            # numbers outside [1..n] by using diff==0 and mod==0.
            return dp[SHIFT][0]

        return count_up_to(high) - count_up_to(low - 1)
```
```

</details>

<details>
<summary>partial attempt 4</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(x: int) -> int:
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            # dp[pos][diff][rem][started]
            # diff = even_count - odd_count, shift by +n to make non-negative
            # rem = number mod k
            # started = whether we've placed any non-leading-zero digit
            shift = n
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, diff: int, rem: int, started: int) -> int:
                if pos == n:
                    if not started:
                        return 0  # exclude 0
                    return 1 if diff == 0 and rem == 0 else 0

                limit = digits[pos]
                total = 0
                for d in range(0, limit + 1):
                    nt_started = started or d != 0
                    if not nt_started:
                        # still leading zeros: diff and rem unchanged
                        total += dfs(pos + 1, diff, rem, 0)
                    else:
                        ndiff = diff
                        if d % 2 == 0:
                            ndiff += 1
                        else:
                            ndiff -= 1
                        nrem = (rem * 10 + d) % k
                        total += dfs(pos + 1, ndiff, nrem, 1)
                return total

            # bound diff within [-n, n]
            # Our recursion never steps outside when starting from 0; still safe.
            return dfs(0, shift, 0, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

### Parsed Memory Items

1. Constraint-Driven Digit DP State Design
Description: Build the DP state from the exact constraints you must satisfy at the end, not from superficial implementation choices.
<details>
<summary>Content 1</summary>

```text
For range-counting problems with digit properties, choose DP dimensions that directly encode the invariants needed to decide beauty (e.g., a running balance for parity counts and a remainder for divisibility). Then the acceptance condition at the end becomes a simple check on those state components, reducing the chance of subtle logical mismatch.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
The successful direction consistently used a correct “digit DP” formulation: represent the number by its decimal digits, track exactly the properties that must hold at the end (balanced parity counts and divisibility by k), and enforce the upper bound via a proper tight mechanism. Failures tended to come from (1) mishandling the “tight” update (confusing limits/index comparisons so the bounded range becomes wrong), (2) incorrect treatment of leading zeros (either accidentally counting them as digits affecting parity/divisibility, or needing extra correction passes), and (3) inconsistent state definitions (e.g., using a DP transition that doesn’t actually correspond to the intended constraints like started/tight/diff interactions). The best attempts also validated that the final acceptance condition is checked against the original property set (diff equals zero and remainder equals zero, with started true to exclude zero).
```

</details>

2. Implement “Tight” Correctly for Upper-Bound Digit DP
Description: When using digit DP, the tight/boundedness logic must be updated by comparing chosen digits to the current bound digit.
<details>
<summary>Content 2</summary>

```text
A common failure mode is updating the tight flag using an incorrect comparison (e.g., using the wrong limit variable), which silently changes the range being counted. Ensure transitions use: if tight is true, the next tight is true only when the chosen digit equals the current bound digit; otherwise tight becomes false and the remaining digits range freely.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
The successful direction consistently used a correct “digit DP” formulation: represent the number by its decimal digits, track exactly the properties that must hold at the end (balanced parity counts and divisibility by k), and enforce the upper bound via a proper tight mechanism. Failures tended to come from (1) mishandling the “tight” update (confusing limits/index comparisons so the bounded range becomes wrong), (2) incorrect treatment of leading zeros (either accidentally counting them as digits affecting parity/divisibility, or needing extra correction passes), and (3) inconsistent state definitions (e.g., using a DP transition that doesn’t actually correspond to the intended constraints like started/tight/diff interactions). The best attempts also validated that the final acceptance condition is checked against the original property set (diff equals zero and remainder equals zero, with started true to exclude zero).
```

</details>

3. Handle Leading Zeros with an Explicit Started Flag
Description: If digit-count properties should ignore leading zeros, track whether the number has started to prevent leading zeros from affecting the invariants.
<details>
<summary>Content 3</summary>

```text
Balanced digit-count constraints often break when leading zeros are treated as actual digits (they can flip parity counts and affect remainders). Introduce a started/not-started state: only update parity balance and remainder once started becomes true, and exclude the all-not-started case to avoid counting zero.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
The successful direction consistently used a correct “digit DP” formulation: represent the number by its decimal digits, track exactly the properties that must hold at the end (balanced parity counts and divisibility by k), and enforce the upper bound via a proper tight mechanism. Failures tended to come from (1) mishandling the “tight” update (confusing limits/index comparisons so the bounded range becomes wrong), (2) incorrect treatment of leading zeros (either accidentally counting them as digits affecting parity/divisibility, or needing extra correction passes), and (3) inconsistent state definitions (e.g., using a DP transition that doesn’t actually correspond to the intended constraints like started/tight/diff interactions). The best attempts also validated that the final acceptance condition is checked against the original property set (diff equals zero and remainder equals zero, with started true to exclude zero).
```

</details>

4. Use Offset/Sentinel Values to Safely Index Negative Balances
Description: When a DP variable naturally ranges over negative values (like an even-odd balance), use an offset or bounds-check to keep array indexing valid.
<details>
<summary>Content 4</summary>

```text
Track balances with an offset so indices stay non-negative, and/or skip transitions that would go out of the feasible range. This prevents off-by-one and out-of-bounds errors and makes the invariant range explicit during transitions.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
The successful direction consistently used a correct “digit DP” formulation: represent the number by its decimal digits, track exactly the properties that must hold at the end (balanced parity counts and divisibility by k), and enforce the upper bound via a proper tight mechanism. Failures tended to come from (1) mishandling the “tight” update (confusing limits/index comparisons so the bounded range becomes wrong), (2) incorrect treatment of leading zeros (either accidentally counting them as digits affecting parity/divisibility, or needing extra correction passes), and (3) inconsistent state definitions (e.g., using a DP transition that doesn’t actually correspond to the intended constraints like started/tight/diff interactions). The best attempts also validated that the final acceptance condition is checked against the original property set (diff equals zero and remainder equals zero, with started true to exclude zero).
```

</details>

5. Validate by Reducing to Count(Upto) Difference with Consistent Semantics
Description: For counting in [low, high], compute count(≤high) − count(≤low−1) only when the “number definition” and leading-zero handling are consistent in both calls.
<details>
<summary>Content 5</summary>

```text
This difference trick is powerful, but it only works if each count_upto uses identical digit-DP semantics for whether zero is included and how started/leading zeros affect the constraints. Keep the same started handling and final acceptance rule across both calls to avoid asymmetrical bugs.
```

</details>

<details>
<summary>Reasoning 5</summary>

```text
The successful direction consistently used a correct “digit DP” formulation: represent the number by its decimal digits, track exactly the properties that must hold at the end (balanced parity counts and divisibility by k), and enforce the upper bound via a proper tight mechanism. Failures tended to come from (1) mishandling the “tight” update (confusing limits/index comparisons so the bounded range becomes wrong), (2) incorrect treatment of leading zeros (either accidentally counting them as digits affecting parity/divisibility, or needing extra correction passes), and (3) inconsistent state definitions (e.g., using a DP transition that doesn’t actually correspond to the intended constraints like started/tight/diff interactions). The best attempts also validated that the final acceptance condition is checked against the original property set (diff equals zero and remainder equals zero, with started true to exclude zero).
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
The successful direction consistently used a correct “digit DP” formulation: represent the number by its decimal digits, track exactly the properties that must hold at the end (balanced parity counts and divisibility by k), and enforce the upper bound via a proper tight mechanism. Failures tended to come from (1) mishandling the “tight” update (confusing limits/index comparisons so the bounded range becomes wrong), (2) incorrect treatment of leading zeros (either accidentally counting them as digits affecting parity/divisibility, or needing extra correction passes), and (3) inconsistent state definitions (e.g., using a DP transition that doesn’t actually correspond to the intended constraints like started/tight/diff interactions). The best attempts also validated that the final acceptance condition is checked against the original property set (diff equals zero and remainder equals zero, with started true to exclude zero).
</reasoning>

<memories>
<memory>
<title>Constraint-Driven Digit DP State Design</title>
<description>Build the DP state from the exact constraints you must satisfy at the end, not from superficial implementation choices.</description>
<content>For range-counting problems with digit properties, choose DP dimensions that directly encode the invariants needed to decide beauty (e.g., a running balance for parity counts and a remainder for divisibility). Then the acceptance condition at the end becomes a simple check on those state components, reducing the chance of subtle logical mismatch.</content>
</memory>

<memory>
<title>Implement “Tight” Correctly for Upper-Bound Digit DP</title>
<description>When using digit DP, the tight/boundedness logic must be updated by comparing chosen digits to the current bound digit.</description>
<content>A common failure mode is updating the tight flag using an incorrect comparison (e.g., using the wrong limit variable), which silently changes the range being counted. Ensure transitions use: if tight is true, the next tight is true only when the chosen digit equals the current bound digit; otherwise tight becomes false and the remaining digits range freely.</content>
</memory>

<memory>
<title>Handle Leading Zeros with an Explicit Started Flag</title>
<description>If digit-count properties should ignore leading zeros, track whether the number has started to prevent leading zeros from affecting the invariants.</description>
<content>Balanced digit-count constraints often break when leading zeros are treated as actual digits (they can flip parity counts and affect remainders). Introduce a started/not-started state: only update parity balance and remainder once started becomes true, and exclude the all-not-started case to avoid counting zero.</content>
</memory>

<memory>
<title>Use Offset/Sentinel Values to Safely Index Negative Balances</title>
<description>When a DP variable naturally ranges over negative values (like an even-odd balance), use an offset or bounds-check to keep array indexing valid.</description>
<content>Track balances with an offset so indices stay non-negative, and/or skip transitions that would go out of the feasible range. This prevents off-by-one and out-of-bounds errors and makes the invariant range explicit during transitions.</content>
</memory>

<memory>
<title>Validate by Reducing to Count(Upto) Difference with Consistent Semantics</title>
<description>For counting in [low, high], compute count(≤high) − count(≤low−1) only when the “number definition” and leading-zero handling are consistent in both calls.</description>
<content>This difference trick is powerful, but it only works if each count_upto uses identical digit-DP semantics for whether zero is included and how started/leading zeros affect the constraints. Keep the same started handling and final acceptance rule across both calls to avoid asymmetrical bugs.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `0.6000`
- Augmented pass@1: `0.9000`
- Improvement: `+0.3000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
You are given positive integers low, high, and k.
A number is beautiful if it meets both of the following conditions:

The count of even digits in the number is equal to the count of odd digits.
The number is divisible by k.

Return the number of beautiful integers in the range [low, high].
 
Example 1:

Input: low = 10, high = 20, k = 3
Output: 2
Explanation: There are 2 beautiful integers in the given range: [12,18]. 
- 12 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
- 18 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
Additionally we can see that:
- 16 is not beautiful because it is not divisible by k = 3.
- 15 is not beautiful because it does not contain equal counts even and odd digits.
It can be shown that there are only 2 beautiful integers in the given range.

Example 2:

Input: low = 1, high = 10, k = 1
Output: 1
Explanation: There is 1 beautiful integer in the given range: [10].
- 10 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 1.
It can be shown that there is only 1 beautiful integer in the given range.

Example 3:

Input: low = 5, high = 5, k = 2
Output: 0
Explanation: There are 0 beautiful integers in the given range.
- 5 is not beautiful because it is not divisible by k = 2 and it does not contain equal even and odd digits.

 
Constraints:

0 < low <= high <= 10^9
0 < k <= 20

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # parity of counts: we only care about (even_count - odd_count) == 0
            # Let diff = even_count - odd_count; start at 0.
            # For each digit: if even -> diff+1 else diff-1.
            # Additionally track remainder mod k.
            # Digit DP with tight flag.
            from functools import lru_cache

            @lru_cache(None)
            def dp(i: int, diff: int, r: int, tight: int) -> int:
                if i == m:
                    return 1 if diff == 0 and r == 0 else 0
                limit = digits[i] if tight else 9
                total = 0
                ntight = 1
                for d in range(limit + 1):
                    # leading zeros are allowed in DP, but they don't count as digits.
                    # However, our constraints consider "number" normally without leading zeros.
                    # To handle that, we treat leading zeros as "not yet started".
                    # We'll implement by a "started" flag via diff/r not being meaningful before start.
                    # Instead of adding another state, do a separate DP that forbids all leading zeros
                    # by forcing at least one non-zero digit. Simpler: track started in state.
                    pass
                return total

            # Redo DP with an explicit started flag.
            @lru_cache(None)
            def dp2(i: int, diff: int, r: int, tight: int, started: int) -> int:
                if i == m:
                    return 1 if started == 1 and diff == 0 and r == 0 else 0
                limit = digits[i] if tight else 9
                total = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    if started == 0 and d == 0:
                        # still leading zeros: digit doesn't contribute
                        total += dp2(i + 1, diff, r, ntight, 0)
                    else:
                        ndiff = diff + (1 if d % 2 == 0 else -1)
                        nr = (r * 10 + d) % k
                        total += dp2(i + 1, ndiff, nr, ntight, 1)
                return total

            # diff range: at most m, so within [-m, m]
            return dp2(0, 0, 0, 1, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        from functools import lru_cache

        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)

            # dp[pos][diff][rem] where diff = (#even - #odd) so far shifted by +L
            # We require final diff == 0 (equal counts) after filling all positions.
            shift = L  # diff in [-L, L]
            maxdiff = 2 * L

            @lru_cache(None)
            def dp(pos: int, diff: int, rem: int, started: int, tight: int) -> int:
                if pos == L:
                    if started and diff == 0 and rem % k == 0:
                        return 1
                    return 0

                limit = digits[pos] if tight else 9
                ans = 0
                for d in range(0, limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    if not started and d == 0:
                        # Still not started: don't count digits (no even/odd contribution)
                        ans += dp(pos + 1, diff, (rem * 10) % k, 0, ntight)
                    else:
                        ne = 1 if d % 2 == 0 else 0
                        no = 1 if d % 2 == 1 else 0
                        ndiff = diff + (ne - no)
                        if -L <= ndiff <= L:
                            nrem = (rem * 10 + d) % k
                            ans += dp(pos + 1, ndiff, nrem, 1, ntight)
                return ans

            # started indicates number has begun (so we don't include leading zeros as digits)
            return dp(0, 0, 0, 0, 1)

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)
            L = len(s)

            # Leading zeros are allowed in the digit DP; they don't contribute to odd/even counts.
            # For a fixed length with leading zeros, the number's digits still have equal
            # odd/even *among actual digits*; however leading zeros would be even digits.
            # To avoid that, we track whether we've started (non-leading digit).
            @lru_cache(None)
            def dp(pos: int, started: int, balance: int, rem: int, tight: int) -> int:
                """
                balance = (#even_digits - #odd_digits) among digits after started==1
                Rem is value mod k of the constructed number.
                started: 0 if all previous digits are leading zeros, else 1
                tight: 1 if prefix equals upper bound prefix, else 0
                """
                if pos == L:
                    # Beautiful if started (number>0) and balance==0 and rem==0
                    return 1 if started == 1 and balance == 0 and rem == 0 else 0

                limit = int(s[pos]) if tight else 9
                total = 0
                for d in range(0, limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    if started == 0 and d == 0:
                        # still leading zeros: don't count as even/odd digits
                        total += dp(pos + 1, 0, balance, (0 if rem == 0 else (rem * 10) % k), ntight)
                    else:
                        nstarted = 1
                        nbalance = balance
                        if d % 2 == 0:
                            nbalance += 1
                        else:
                            nbalance -= 1
                        nrem = (rem * 10 + d) % k
                        total += dp(pos + 1, nstarted, nbalance, nrem, ntight)
                return total

            # The balance range: up to 10 digits (since n<=1e9 => <=10 digits for safety), so [-10,10].
            # Our DP uses balance as an unbounded integer but recursion limits by length, fine.
            return dp(0, 0, 0, 0, 1)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        # Digit DP: count numbers in [0..N] such that
        # - #even_digits == #odd_digits across digits of the number (with leading zeros ignored)
        # - number % k == 0
        #
        # While building the number, maintain:
        #   diff = (#even - #odd) so diff == 0 at the end
        #   rem = current value modulo k
        #   started = whether we've placed a non-leading-zero digit
        #
        # For started == False, diff/rem are neutral (rem=0).
        def count_upto(N: int) -> int:
            if N < 0:
                return 0
            digits = list(map(int, str(N)))
            L = len(digits)

            # dp[pos][diff_offset][rem][started] -> ways
            # diff in [-L..L], offset by L to index
            diff_offset = L
            size_diff = 2 * L + 1

            # Initialize: at pos=0, started=False, diff=0, rem=0
            from collections import defaultdict

            cur = defaultdict(int)
            cur[(0, 0, 0)] = 1  # (diff, rem, started)

            for pos in range(L):
                nxt = defaultdict(int)
                limit = digits[pos]
                for (diff, rem, started), ways in cur.items():
                    maxd = limit
                    for dig in range(0, maxd + 1):
                        ntight = True  # not used; we incorporate tight via dimension below
                    # We'll implement tight explicitly to avoid confusion.
                # Re-do with tight dimension properly:
                nxt = defaultdict(int)
                # key: (diff, rem, started, tight)
                cur2 = defaultdict(int)
                # seed with tight=True
                for (diff, rem, started), ways in cur.items():
                    cur2[(diff, rem, started, 1)] += ways

                cur = cur2
                break  # We'll replace loop entirely below

            # Proper digit DP with tight:
            cur = defaultdict(int)
            cur[(0, 0, 0, 1)] = 1  # (diff, rem, started, tight)

            for pos in range(L):
                nxt = defaultdict(int)
                limit = digits[pos]
                for (diff, rem, started, tight), ways in cur.items():
                    ub = limit if tight else 9
                    for dig in range(ub + 1):
                        ntight = 1 if (tight and dig == ub) else 0  # incorrect: ub depends on tight
                # We'll correct with proper ntight:
                # (tight -> restrict to digits[pos], else 9)
                nxt = defaultdict(int)
                for (diff, rem, started, tight), ways in cur.items():
                    ub = limit if tight else 9
                    for dig in range(ub + 1):
                        nstarted = started or (dig != 0)
                        ndiff = diff
                        nrem = rem
                        if not nstarted:
                            # still leading zeros: digits not counted, value effectively 0 so far
                            ndiff = 0
                            nrem = 0
                        else:
                            # count digit parity
                            if dig % 2 == 0:
                                ndiff = diff + 1
                            else:
                                ndiff = diff - 1
                            nrem = (rem * 10 + dig) % k
                        nrem_t = nrem
                        ntight = 1 if (tight and dig == ub) else 0
                        # wait: ntight condition should be: tight && dig==limit (the digit at pos)
                        ntight = 1 if (tight and dig == limit) else 0
                        nxt[(ndiff, nrem_t, 1 if nstarted else 0, ntight)] += ways
                cur = nxt

            ans = 0
            # At end, need diff==0 and started==1? The problem considers positive integers range [low, high].
            # We'll count numbers >=1; so started must be 1. Also number divisible by k, i.e. rem==0.
            for (diff, rem, started, tight), ways in cur.items():
                if started == 1 and diff == 0 and rem % k == 0:
                    ans += ways
            return ans

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # dp[pos][balance][rem] -> ways
            # balance = (#even - #odd) so final balance must be 0.
            # shift to make balance index non-negative: balance in [-m, m]
            shift = m
            size_bal = 2 * m + 1

            from collections import defaultdict

            # Use dicts for sparsity: dp[bal][rem] -> ways
            dp = [defaultdict(int) for _ in range(size_bal)]
            dp[shift][0] = 1

            for pos in range(m):
                ndp = [defaultdict(int) for _ in range(size_bal)]
                limit = digits[pos]
                for bal_idx in range(size_bal):
                    if not dp[bal_idx]:
                        continue
                    for rem, ways in dp[bal_idx].items():
                        if ways == 0:
                            continue
                        for d in range(0, limit + 1):
                            nb = bal_idx
                            if d == 0 or d % 2 == 0:
                                # even digit
                                nb = bal_idx + 1
                            else:
                                # odd digit
                                nb = bal_idx - 1

                            if 0 <= nb < size_bal:
                                nrem = (rem * 10 + d) % k
                                ndp[nb][nrem] += ways
                dp = ndp

            return dp[shift][0]

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)
            # dp[pos][diff][rem][started] is too big; use rolling dicts:
            # diff = (#even - #odd) over started digits so far
            # started=0 means no non-leading digit picked yet
            from collections import defaultdict

            # diff range is [-L, L]
            # We'll represent diff with offset.
            offset = L
            # dp maps (diff, rem, started) -> ways
            dp = defaultdict(int)
            dp[(0, 0, 0)] = 1  # no digits chosen yet

            for pos in range(L):
                ndp = defaultdict(int)
                limit = digits[pos]
                for (diff, rem, started), ways in dp.items():
                    maxd = limit
                    for dig in range(0, maxd + 1):
                        ntight_started = started
                        if started == 0 and dig == 0:
                            # still not started; no digit contributes to parity counts
                            ndp[(diff, rem, 0)] += ways
                        else:
                            # start now (or already started)
                            ntight_started = 1
                            is_even = (dig % 2 == 0)
                            ndiff = diff + (1 if is_even else -1)
                            nrem = (rem * 10 + dig) % k
                            ndp[(ndiff, nrem, 1)] += ways
                dp = ndp

            # finished numbers must be started (positive integer), and diff == 0
            ans = 0
            for (diff, rem, started), ways in dp.items():
                if started == 1 and diff == 0 and rem == 0:
                    ans += ways
            return ans

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # DP over positions with:
            #  - diff = (#even - #odd) tracked with offset
            #  - rem = value % k
            # Leading zeros are not allowed (numbers must be positive).
            offset = m  # diff range: [-m, m]
            size_diff = 2 * m + 1

            # dp[state] -> ways so far
            # state: diff_index, rem, started(0/1)
            dp = [[[0] * k for _ in range(size_diff)] for __ in range(2)]
            dp[0][offset][0] = 1  # before starting, diff = 0, rem = 0

            for pos in range(m):
                ndp = [[[0] * k for _ in range(size_diff)] for __ in range(2)]
                cur = digits[pos]
                for started in (0, 1):
                    for diff_idx in range(size_diff):
                        base_diff = diff_idx - offset
                        row = dp[started][diff_idx]
                        for rem in range(k):
                            ways = row[rem]
                            if ways == 0:
                                continue
                            limit = cur if started == 0 else cur  # same for started; below logic handles started anyway
                            # Try next digit
                            for dig in range(0, limit + 1):
                                tight_ok = dig == cur  # We'll handle tight by using standard tight DP instead.
                    # The above attempt mixes concepts; use proper digit-DP with tight.
                # Re-implement with tight for correctness

            # Proper digit DP with tight:
            # dp[tight][started][diff_idx][rem]
            dp = [[[[0] * k for _ in range(size_diff)] for _ in range(2)] for __ in range(2)]
            dp[1][0][offset][0] = 1

            for pos in range(m):
                ndp = [[[[0] * k for _ in range(size_diff)] for _ in range(2)] for __ in range(2)]
                cur = digits[pos]
                for tight in (0, 1):
                    maxd = cur if tight else 9
                    for started in (0, 1):
                        for diff_idx in range(size_diff):
                            for rem in range(k):
                                ways = dp[tight][started][diff_idx][rem]
                                if ways == 0:
                                    continue
                                for dig in range(maxd + 1):
                                    ntight = 1 if (tight and dig == cur) else 0
                                    if started == 0 and dig == 0:
                                        # Still not started: diff unchanged, rem unchanged (since number has no digits yet)
                                        ndp[ntight][0][diff_idx][rem] += ways
                                    else:
                                        # Start or continue: classify digit parity
                                        nt_started = 1
                                        ndiff_idx = diff_idx + (1 if dig % 2 == 0 else -1)
                                        if 0 <= ndiff_idx < size_diff:
                                            nrem = (rem * 10 + dig) % k
                                            ndp[ntight][nt_started][ndiff_idx][nrem] += ways

                dp = ndp

            # Count numbers with equal even/odd digits => diff = 0
            return sum(
                dp[tight][1][offset][0]
                for tight in (0, 1)
            )

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)
            half = m // 2

            # dp[pos][diff][rem][tight_started]
            # diff = (#even - #odd) using sign where even:+1, odd:-1
            # We only need diff values in [-m, m], shift by +m.
            SHIFT = m
            # Use sparse dicts for efficiency: key=(diff, rem, started)
            dp = {(0, 0, False): 1}  # pos=0 initially

            for pos in range(m):
                ndp = {}
                limit = digits[pos]
                for (diff, rem, started), ways in dp.items():
                    for dig in range(0, (limit + 1) if True else 0):
                        pass  # placeholder

                # We'll implement standard digit DP with tight via separate maps
                ndp = {}
                for (diff, rem, started, tight), ways in {(d, r, s, t): w for (d, r, s, t), w in [((k1[0], k1[1], k1[2], 0), 0)]}.items():
                    pass

            # The above attempt is too messy; implement clean digit DP with explicit state maps:
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, diff: int, rem: int, started: bool, tight: bool) -> int:
                if pos == m:
                    if not started:
                        # number 0 excluded from range since low>0, and even/odd counts can't be equal meaningfully
                        return 0
                    return 1 if diff == 0 and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                total = 0

                for dig in range(0, limit + 1):
                    ntight = tight and (dig == limit)
                    nstarted = started or (dig != 0)
                    if not nstarted:
                        # Still leading zeros: they should not be counted as digits.
                        total += dfs(pos + 1, diff, rem, False, ntight)
                    else:
                        # Update diff using digit parity; even:+1 odd:-1
                        ndiff = diff + (1 if dig % 2 == 0 else -1)
                        nrem = (rem * 10 + dig) % k
                        total += dfs(pos + 1, ndiff, nrem, True, ntight)
                return total

            # However, the original problem counts all digits in the number as written without leading zeros.
            # Our dfs with "started" ensures leading zeros are not counted.
            return dfs(0, 0, 0, False, True)

        # count numbers in [low, high] = upto(high) - upto(low-1)
        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        from functools import lru_cache

        def count_beautiful_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos: int, diff: int, rem: int, tight: int) -> int:
                """
                pos: current index [0..m]
                diff: (#even_digits - #odd_digits) so far, shifted by offset.
                rem: current remainder mod k
                tight: 1 if prefix equals n's prefix; 0 otherwise
                """
                if pos == m:
                    # Need even and odd counts equal => diff == 0, and divisible by k
                    return 1 if diff == 0 and rem == 0 else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    ndiff = diff + (1 if d % 2 == 0 else -1)
                    if -m <= ndiff <= m:
                        res += dp(pos + 1, ndiff, (rem * 10 + d) % k, ntight)
                return res

            # Initialize diff as 0, remainder 0; tight=1
            return dp(0, 0, 0, 1)

        return count_beautiful_upto(high) - count_beautiful_upto(low - 1)
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        # Digit DP:
        # count numbers with:
        # - equal number of even/odd digits
        # - value % k == 0
        # Leading zeros are allowed in DP length; they are treated as digits '0' (even),
        # which is fine as long as we exclude the all-zero number and handle parity correctly.
        
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            s = str(n)
            L = len(s)
            digits = list(map(int, s))
            
            # Precompute powers of 10? Not needed; remainder is built incrementally.
            
            # dp[pos][diff_shift][rem][tight][started] would be large.
            # We'll avoid 'started' by allowing leading zeros and then later subtract the all-zero case.
            # diff = (#even - #odd) with leading zeros counting as even digits.
            # Need diff == 0 at end.
            
            # diff range: [-L, L] => shift by L
            shift = L
            from functools import lru_cache
            
            @lru_cache(None)
            def dfs(pos: int, diff: int, rem: int, tight: int) -> int:
                if pos == L:
                    return 1 if diff == 0 and rem % k == 0 else 0
                
                limit = digits[pos] if tight else 9
                total = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    # Even/odd digit classification
                    ndiff = diff + (1 if d % 2 == 0 else -1)
                    nrem = (rem * 10 + d) % k
                    total += dfs(pos + 1, ndiff, nrem, ntight)
                return total
            
            # Start with pos=0, diff=0, rem=0, tight=1. Note: leading zeros count as even digits,
            # so final diff==0 enforces equal even/odd including those zeros. That matches typical
            # digit-DP interpretations for fixed length; but we need actual numbers without leading zeros.
            # We fix this by counting over all lengths <= L using separate DP per length.
            
            # Therefore, implement per exact length with leading zeros not allowed (first digit >=1).
            # We'll compute count for all lengths from 1..L and sum, each with its own DP.

            return 0  # placeholder

        def count_exact_length(length: int, upper_str: str | None) -> int:
            # If upper_str is provided, count numbers of this length <= int(upper_str) with exactly that length.
            # Otherwise, count all numbers of this exact length (no upper bound) -> upper_str is None.
            if length == 0:
                return 0
            if upper_str is not None:
                digits = list(map(int, upper_str))
                assert len(digits) == length
                tight_allowed = True
            else:
                digits = None
                tight_allowed = False

            shift = length
            from functools import lru_cache

            # We'll disallow leading zeros: first digit from 1..9.
            @lru_cache(None)
            def dfs(pos: int, diff: int, rem: int, tight: int) -> int:
                if pos == length:
                    return 1 if diff == 0 and rem % k == 0 else 0
                if tight_allowed:
                    limit = digits[pos] if tight else 9
                else:
                    limit = 9

                lo = 0
                if pos == 0:
                    lo = 1  # no leading zero
                total = 0
                for d in range(lo, limit + 1):
                    ntight = 0
                    if tight_allowed and tight and d == limit:
                        ntight = 1
                    ndiff = diff + (1 if d % 2 == 0 else -1)
                    nrem = (rem * 10 + d) % k
                    total += dfs(pos + 1, ndiff, nrem, ntight)
                return total

            return dfs(0, 0, 0, 1 if tight_allowed else 0)

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            s = str(n)
            L = len(s)
            ans = 0
            # Count for lengths 1..L-1 fully
            for ln in range(1, L):
                ans += count_exact_length(ln, None)
            # Count for length L up to n
            ans += count_exact_length(L, s)
            return ans

        return count_upto(high) - count_upto(low - 1)
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
| 4 | 0.2667 | `partial` |
| 5 | 0.2000 | `partial` |
| 6 | 1.0000 | `full` |
| 7 | 0.0000 | `fail` |
| 8 | 0.3333 | `partial` |
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
  "passed": 4,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
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
      "passed": false,
      "expected": "6",
      "actual": "-2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "-20",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "5",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "-8",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "-2",
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
      "expected": "24894045",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18196584",
      "actual": "-9280",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240042",
      "actual": "-67609",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1319380",
      "actual": "-16231",
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
  "passed": 3,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
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
      "passed": false,
      "expected": "6",
      "actual": "-2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "-18",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "5",
      "actual": "7",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "-2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "-2",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "3",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "24894045",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18196584",
      "actual": "4193",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240042",
      "actual": "-54959",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1319380",
      "actual": "-6656",
      "error": "Wrong Answer"
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "",
      "error": "Runtime Error: name 'k1' is not defined"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "6",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "5",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "24894045",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "18196584",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1240042",
      "actual": "",
      "error": "Skipped (earlier failure)"
    },
    {
      "passed": false,
      "expected": "1319380",
      "actual": "",
      "error": "Skipped (earlier failure)"
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
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "4",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "6",
      "error": "Wrong Answer"
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": false,
      "expected": "3",
      "actual": "-47",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "5",
      "actual": "-5",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "-10",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "-2",
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
      "expected": "24894045",
      "actual": "246093750",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18196584",
      "actual": "-9147166",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240042",
      "actual": "-713083",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1319380",
      "actual": "-289076",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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

  1. Constraint-Driven Digit DP State Design: Build the DP state from the exact constraints you must satisfy at the end, not from superficial implementation choices.
     For range-counting problems with digit properties, choose DP dimensions that directly encode the invariants needed to decide beauty (e.g., a running balance for parity counts and a remainder for divisibility). Then the acceptance condition at the end becomes a simple check on those state components, reducing the chance of subtle logical mismatch.
  2. Implement “Tight” Correctly for Upper-Bound Digit DP: When using digit DP, the tight/boundedness logic must be updated by comparing chosen digits to the current bound digit.
     A common failure mode is updating the tight flag using an incorrect comparison (e.g., using the wrong limit variable), which silently changes the range being counted. Ensure transitions use: if tight is true, the next tight is true only when the chosen digit equals the current bound digit; otherwise tight becomes false and the remaining digits range freely.
  3. Handle Leading Zeros with an Explicit Started Flag: If digit-count properties should ignore leading zeros, track whether the number has started to prevent leading zeros from affecting the invariants.
     Balanced digit-count constraints often break when leading zeros are treated as actual digits (they can flip parity counts and affect remainders). Introduce a started/not-started state: only update parity balance and remainder once started becomes true, and exclude the all-not-started case to avoid counting zero.
  4. Use Offset/Sentinel Values to Safely Index Negative Balances: When a DP variable naturally ranges over negative values (like an even-odd balance), use an offset or bounds-check to keep array indexing valid.
     Track balances with an offset so indices stay non-negative, and/or skip transitions that would go out of the feasible range. This prevents off-by-one and out-of-bounds errors and makes the invariant range explicit during transitions.
  5. Validate by Reducing to Count(Upto) Difference with Consistent Semantics: For counting in [low, high], compute count(≤high) − count(≤low−1) only when the “number definition” and leading-zero handling are consistent in both calls.
     This difference trick is powerful, but it only works if each count_upto uses identical digit-DP semantics for whether zero is included and how started/leading zeros affect the constraints. Keep the same started handling and final acceptance rule across both calls to avoid asymmetrical bugs.

Apply these insights to the problem below.

### Question:
You are given positive integers low, high, and k.
A number is beautiful if it meets both of the following conditions:

The count of even digits in the number is equal to the count of odd digits.
The number is divisible by k.

Return the number of beautiful integers in the range [low, high].
 
Example 1:

Input: low = 10, high = 20, k = 3
Output: 2
Explanation: There are 2 beautiful integers in the given range: [12,18]. 
- 12 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
- 18 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 3.
Additionally we can see that:
- 16 is not beautiful because it is not divisible by k = 3.
- 15 is not beautiful because it does not contain equal counts even and odd digits.
It can be shown that there are only 2 beautiful integers in the given range.

Example 2:

Input: low = 1, high = 10, k = 1
Output: 1
Explanation: There is 1 beautiful integer in the given range: [10].
- 10 is beautiful because it contains 1 odd digit and 1 even digit, and is divisible by k = 1.
It can be shown that there is only 1 beautiful integer in the given range.

Example 3:

Input: low = 5, high = 5, k = 2
Output: 0
Explanation: There are 0 beautiful integers in the given range.
- 5 is not beautiful because it is not divisible by k = 2 and it does not contain equal even and odd digits.

 
Constraints:

0 < low <= high <= 10^9
0 < k <= 20

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Augmented generation 1</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # balance = (#even - #odd); in range [-m, m]
            off = m
            max_bal = 2 * m

            # dp[pos][tight][started][balance_index][rem] -> count
            # We'll keep only current/next layers.
            from collections import defaultdict

            # state key: (tight, started, bal, rem)
            cur = defaultdict(int)
            # start at pos=0
            cur[(1, 0, off, 0)] = 1  # tight=True, not started, balance=0, rem=0

            for pos in range(m):
                nxt = defaultdict(int)
                bound = digits[pos]
                for (tight, started, bal, rem), ways in cur.items():
                    limit = bound if tight else 9
                    for d in range(limit + 1):
                        ntight = 1 if (tight and d == limit and tight) else (1 if (tight and d == bound) else 0)
                        # simpler and correct:
                        ntight = 1 if (tight and d == bound) else 0

                        if started == 0 and d == 0:
                            # still not started; digits don't count toward even/odd
                            # remainder stays 0 because we haven't formed a number
                            nxt[(ntight, 0, off, 0)] += ways
                        else:
                            # number has started; update balance and remainder
                            nstarted = 1
                            if d % 2 == 0:
                                nbal = bal + 1
                            else:
                                nbal = bal - 1
                            if 0 <= nbal <= max_bal:
                                nrem = (rem * 10 + d) % k
                                nxt[(ntight, nstarted, nbal, nrem)] += ways
                cur = nxt

            # acceptance: started==1, balance==0, rem==0
            ans = 0
            for (tight, started, bal, rem), ways in cur.items():
                if started == 1 and bal == off and rem == 0:
                    ans += ways
            return ans

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        # Digit DP: count beautiful numbers in [1..n]
        # Beautiful:
        # 1) #even_digits == #odd_digits  (only over started part)
        # 2) divisible by k
        #
        # Represent balance = (#even - #odd), with offset for indexing.
        # Balance starts at 0 once started; while not started, we don't update balance/remainder.
        # Exclude the all-not-started (i.e., number 0) by requiring started at the end.

        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)

            # Balance range: [-L, L]
            off = L
            # dp[pos][tight][started][balance][rem]
            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, bal: int, rem: int) -> int:
                if pos == L:
                    if not started:
                        return 0  # exclude 0
                    # even == odd  <=> bal == 0
                    return 1 if bal == 0 and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                total = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0  # correct tight propagation
                    if not started and d == 0:
                        # remain not started; balance/remainder unchanged
                        total += dp(pos + 1, ntight, 0, bal, rem)
                    else:
                        # now started
                        nb = bal
                        if d % 2 == 0:
                            nb += 1
                        else:
                            nb -= 1
                        # prune impossible balance
                        if nb < -off or nb > off:
                            continue
                        nrem = (rem * 10 + d) % k
                        total += dp(pos + 1, ntight, 1, nb, nrem)
                return total

            return dp(0, 1, 0, 0, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)
            L = len(s)
            digits = list(map(int, s))

            # balance = (#even - #odd) among digits after started=True
            # We need balance == 0 at end; ignore the all-not-started (i.e., number 0) case.
            # balance range after at most L digits: [-L, L]
            OFFSET = L
            BAL_MIN, BAL_MAX = -L, L

            # dp[pos][tight][started][balance+OFFSET][rem] => count
            # We'll roll over pos to save memory.
            # Dimensions:
            # balance size = 2L+1 <= 19
            # rem size = k <= 20
            # pos <= 10
            bal_size = 2 * L + 1

            # Use dict for sparse transitions; state space is small but dict keeps it tidy.
            from collections import defaultdict

            cur = defaultdict(int)
            # state: (tight, started, balance, rem)
            cur[(1, 0, 0, 0)] = 1

            for pos in range(L):
                nxt = defaultdict(int)
                bound = digits[pos]
                for (tight, started, balance, rem), ways in cur.items():
                    lim = bound if tight else 9
                    for d in range(lim + 1):
                        ntight = 1 if (tight and d == lim) else 0  # careful: lim is bound only when tight
                        # Fix tight update: if tight was true, tight remains true iff d == bound.
                        if tight:
                            ntight = 1 if d == bound else 0
                        else:
                            ntight = 0

                        nstarted = started
                        nbalance = balance
                        nrem = rem

                        if started == 0 and d == 0:
                            # still not started; do not update balance/rem
                            pass
                        else:
                            if started == 0 and d != 0:
                                nstarted = 1
                            # when started (either already or becomes started now), update invariants
                            if nstarted == 1:
                                if d % 2 == 0:
                                    nbalance += 1
                                else:
                                    nbalance -= 1
                                nrem = (rem * 10 + d) % k

                        # balance bounds sanity
                        if nbalance < BAL_MIN or nbalance > BAL_MAX:
                            continue
                        nxt[(ntight, nstarted, nbalance, nrem)] += ways
                cur = nxt

            ans = 0
            for (tight, started, balance, rem), ways in cur.items():
                if started == 1 and balance == 0 and rem == 0:
                    ans += ways
            return ans

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        # Count beautiful numbers in [1, n] (zero excluded by "started" flag)
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)

            # balance = (#even - #odd) among started digits
            # balance ranges from -L..L but never smaller than 0 started digits => keep fixed bounds
            off = L
            size_bal = 2 * L + 1

            # dp[pos][tight][started][balance][rem] is too big; compress by layer.
            # We'll store only current layer states in a dict keyed by (started, balance, rem, tight).
            from collections import defaultdict

            cur = defaultdict(int)
            # at pos=0: not started, balance=0, rem=0
            cur[(1, 0, 0, 1)] = 1  # started=1 means "not started yet" (use flag 0/1 inverted later)

            for pos in range(L):
                nxt = defaultdict(int)
                bound = digits[pos]
                for (ns, bal, rem, tight), ways in cur.items():
                    # ns: 1 => not started yet, 0 => started
                    limit = bound if tight else 9
                    for d in range(limit + 1):
                        ntight = 1 if (tight and d == bound) else 0
                        if ns == 1:  # still not started
                            if d == 0:
                                # remain not started, no digit contributes
                                nxt[(1, bal, rem, ntight)] += ways
                            else:
                                # start now
                                new_bal = bal + (1 if d % 2 == 0 else -1)
                                new_rem = d % k
                                nxt[(0, new_bal, new_rem, ntight)] += ways
                        else:
                            # already started; digit always contributes
                            new_bal = bal + (1 if d % 2 == 0 else -1)
                            new_rem = (rem * 10 + d) % k
                            nxt[(0, new_bal, new_rem, ntight)] += ways
                cur = nxt

            # Accept: started==0 (meaning started), balance==0, rem==0
            ans = 0
            for (ns, bal, rem, tight), ways in cur.items():
                if ns == 0 and bal == 0 and rem == 0:
                    ans += ways
            return ans

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)

            # balance = (#even - #odd) over started digits.
            # started flag ensures leading zeros don't affect parity balance / remainder.
            # We exclude the all-not-started case (number 0).
            BAL = L  # balance in [-L, L]
            OFF = BAL

            # dp[pos][tight][started][balance_index][rem] -> ways
            # Use rolling layers to save memory.
            # Map balance index to array index [0..2L]
            from collections import defaultdict

            cur = defaultdict(int)
            # key: (tight, started, bal_idx, rem)
            cur[(1, 0, OFF, 0)] = 1  # started=0, balance=0, remainder=0

            for i in range(L):
                nxt = defaultdict(int)
                bound = digits[i]
                for (tight, started, bal_idx, rem), ways in cur.items():
                    max_d = bound if tight else 9
                    for d in range(max_d + 1):
                        ntight = 1 if (tight and d == bound) else 0
                        if started == 0 and d == 0:
                            # still not started: invariants unchanged
                            key = (ntight, 0, OFF, 0)
                            nxt[key] += ways
                        else:
                            # number has started; leading zeros are not considered digits
                            nstarted = 1
                            if d % 2 == 0:
                                nbal_idx = bal_idx + 1  # even digit increases (even-odd)
                            else:
                                nbal_idx = bal_idx - 1
                            if 0 <= nbal_idx <= 2 * BAL:
                                nrem = (rem * 10 + d) % k
                                key = (ntight, 1, nbal_idx, nrem)
                                nxt[key] += ways
                cur = nxt

            ans = 0
            # Beautiful at end:
            # 1) even count == odd count => balance == 0
            # 2) divisible by k => rem == 0
            for (tight, started, bal_idx, rem), ways in cur.items():
                if started == 1 and bal_idx == OFF and rem == 0:
                    ans += ways
            return ans

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from functools import lru_cache

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        digits = list(map(int, str(high)))
        n = len(digits)
        # count(<=x) then subtract count(<=low-1)
        def count_upto(x: int) -> int:
            if x <= 0:
                return 0
            s = list(map(int, str(x)))
            m = len(s)
            offset = m  # balance in [-m, m]
            # dp[pos][balance_index][rem][started]
            @lru_cache(None)
            def dp(pos: int, bal: int, rem: int, started: int, tight: int) -> int:
                if pos == m:
                    # Must have at least one digit (exclude 0), and satisfy:
                    # even_count == odd_count  <=> balance == 0
                    # balance tracks (#even - #odd) only after started
                    if started == 0:
                        return 0
                    return 1 if bal == 0 and rem % k == 0 else 0

                limit = s[pos] if tight else 9
                total = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    if started == 0 and d == 0:
                        total += dp(pos + 1, bal, 0, 0, ntight)
                    else:
                        # started becomes 1
                        nstarted = 1
                        # Update balance and remainder with actual digit d
                        if d % 2 == 0:
                            nbal = bal + 1
                        else:
                            nbal = bal - 1
                        # prune impossible balance range (optional but keeps safe array not needed)
                        if -m <= nbal <= m:
                            nrem = (rem * 10 + d) % k
                            total += dp(pos + 1, nbal, nrem, nstarted, ntight)
                return total

            # Start with bal=0, rem=0, started=0, tight=1
            return dp(0, 0, 0, 0, 1)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            L = len(digits)

            # balance = (#even - #odd) => must be 0 at end
            # balance range: [-L, L]
            off = L
            bal_size = 2 * L + 1

            # dp[pos][tight][started][bal_index][rem] - we roll over pos
            # We'll store only current layer as a dict for sparsity.
            from collections import defaultdict

            # state: (tight, started, balance_index, rem) -> count
            cur = defaultdict(int)
            cur[(1, 0, off, 0)] = 1  # before any digits: not started, balance 0, rem 0

            for pos in range(L):
                nd = digits[pos]
                nxt = defaultdict(int)
                for (tight, started, bal_idx, rem), ways in cur.items():
                    limit = nd if tight else 9
                    for dig in range(limit + 1):
                        ntight = 1 if (tight and dig == limit) else 0  # careful: limit is wrong here
                    # We'll re-implement ntight correctly using nd directly.
                # redo loop properly
                nxt = defaultdict(int)
                for (tight, started, bal_idx, rem), ways in cur.items():
                    nd = digits[pos]
                    limit = nd if tight else 9
                    for dig in range(limit + 1):
                        ntight = 1 if (tight and dig == nd) else 0
                        if started == 0 and dig == 0:
                            # still not started; don't update balance or remainder
                            nxt[(ntight, 0, off, 0)] += ways
                        else:
                            # started becomes 1
                            started2 = 1
                            # update balance based on parity of this digit
                            if dig % 2 == 0:
                                bal2 = bal_idx + 1
                            else:
                                bal2 = bal_idx - 1
                            if 0 <= bal2 < bal_size:
                                rem2 = (rem * 10 + dig) % k
                                nxt[(ntight, started2, bal2, rem2)] += ways
                cur = nxt

            # accept: started==1, balance==0, remainder==0
            ans = 0
            bal0 = off
            for (tight, started, bal_idx, rem), ways in cur.items():
                if started == 1 and bal_idx == bal0 and rem == 0:
                    ans += ways
            return ans

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        from functools import lru_cache

        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # balance = (#even - #odd) while started.
            # balance can range from -m..m, use offset to index.
            off = m
            max_states = 2 * m + 1

            @lru_cache(None)
            def dp(pos: int, tight: int, started: int, balance: int, rem: int) -> int:
                if pos == m:
                    # Must have started (exclude 0) and final balance is 0, rem is 0
                    return 1 if started == 1 and balance == 0 and rem == 0 else 0

                limit = digits[pos] if tight else 9
                res = 0

                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0
                    if started == 0 and d == 0:
                        # Still leading zeros, do not affect balance or remainder
                        res += dp(pos + 1, ntight, 0, off, 0)
                    else:
                        # Number has started; update balance by digit parity
                        # even digit contributes +1, odd digit contributes -1
                        new_started = 1
                        parity = 1 if (d % 2 == 0) else -1
                        new_balance = balance + parity
                        if -m <= new_balance <= m:
                            new_rem = (rem * 10 + d) % k
                            res += dp(pos + 1, ntight, new_started, new_balance, new_rem)
                return res

            # When not started, we store balance as 0-indexed value using off sentinel.
            # In dp, balance parameter holds "actual balance" except for started==0 where we pass off.
            return dp(0, 1, 0, off, 0)

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        # Digit DP: count beautiful numbers in [1..n]
        # Track:
        #  - started: have we placed a non-leading-zero digit yet?
        #  - balance = (#even - #odd) among started digits, shifted by offset
        #  - rem = value % k among started digits
        #
        # A number is beautiful iff started=True, balance==0, rem==0.
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))
            m = len(digits)

            # balance range: started length up to m, so balance in [-m..m]
            offset = m
            bal_size = 2 * m + 1

            # dp[pos][tight][started][balance][rem]
            # We'll use rolling dict for memory efficiency.
            from collections import defaultdict

            # state: (tight, started, balance_index, rem) -> ways
            cur = defaultdict(int)
            cur[(1, 0, offset, 0)] = 1  # started=0 => balance irrelevant; keep at 0

            for pos in range(m):
                nxt = defaultdict(int)
                bound_digit = digits[pos]
                for (tight, started, bal_i, rem), ways in cur.items():
                    max_d = bound_digit if tight else 9
                    for d in range(max_d + 1):
                        ntight = 1 if (tight and d == bound_digit) else 0
                        if started == 0 and d == 0:
                            # still leading zeros: started remains 0
                            # balance and rem stay unchanged
                            key = (ntight, 0, offset, 0)
                            nxt[key] += ways
                        else:
                            # started becomes 1
                            neven = 1 if d % 2 == 0 else 0
                            nodd = 1 - neven
                            nbalance = (bal_i - offset) + (neven - nodd)
                            if -m <= nbalance <= m:
                                nbal_i = nbalance + offset
                                nrem = (rem * 10 + d) % k
                                key = (ntight, 1, nbal_i, nrem)
                                nxt[key] += ways
                cur = nxt

            ans = 0
            for (tight, started, bal_i, rem), ways in cur.items():
                if started == 1 and bal_i == offset and rem == 0:
                    ans += ways
            return ans

        return count_upto(high) - count_upto(low - 1)
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # balance = (#even - #odd). Range: [-m, m]
            off = m
            bal_size = 2 * m + 1

            # dp[pos][tight][started][balance_offset][rem]
            # We'll compress pos dimension.
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, tight: int, started: int, balance: int, rem: int) -> int:
                if pos == m:
                    if not started:
                        return 0  # exclude 0 (numbers are positive in problem statement)
                    return 1 if balance == 0 and rem % k == 0 else 0

                limit = digits[pos] if tight else 9
                res = 0
                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0

                    nstarted = started or (d != 0)
                    if not nstarted:
                        # still leading zeros: balance/rem unchanged
                        nbal = balance
                        nrem = 0
                    else:
                        # update balance and remainder with this digit
                        if d % 2 == 0:
                            nbal = balance + 1
                        else:
                            nbal = balance - 1
                        nrem = (rem * 10 + d) % k
                    # balance is always within [-m, m] given started digits <= m
                    if -m <= nbal <= m:
                        res += dfs(pos + 1, ntight, nstarted, nbal, nrem)
                return res

            # start with balance 0 and rem 0, not started yet
            return dfs(0, 1, 0, 0, 0)

        return count_upto(high) - count_upto(low - 1)
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
| 7 | 0.1333 | `partial` |
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
  "passed": 2,
  "total": 15,
  "cases": [
    {
      "passed": false,
      "expected": "2",
      "actual": "-1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "0",
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
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "6",
      "actual": "0",
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
      "expected": "3",
      "actual": "-22",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "5",
      "actual": "7",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "15",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "14",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "24894045",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "18196584",
      "actual": "1073750",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1240042",
      "actual": "0",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "1319380",
      "actual": "88346",
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
  "passed": 15,
  "total": 15,
  "cases": [
    {
      "passed": true,
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "6",
      "actual": "6",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "5",
      "actual": "5",
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
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "24894045",
      "actual": "24894045",
      "error": ""
    },
    {
      "passed": true,
      "expected": "18196584",
      "actual": "18196584",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1240042",
      "actual": "1240042",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1319380",
      "actual": "1319380",
      "error": ""
    }
  ]
}
```

</details>
