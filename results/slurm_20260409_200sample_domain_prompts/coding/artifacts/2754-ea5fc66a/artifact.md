# Problem 2754

- Domain: `coding`

## Problem

```text
You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i_0, i_1, i_2, ... , i_k is defined as nums[i_0] * nums[i_1] * nums[i_2] * ... * nums[i_k​].
Return the maximum strength of a group the teacher can create.
 
Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.

Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.

 
Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9
```

### Starter Code

```python
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
```

### Test Cases

```json
[
  {
    "input": "[3, -1, -5, 2, 5, -9]",
    "output": "1350",
    "testtype": "functional"
  },
  {
    "input": "[-4, -5, -4]",
    "output": "20",
    "testtype": "functional"
  },
  {
    "input": "[9]",
    "output": "9",
    "testtype": "functional"
  },
  {
    "input": "[3]",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "[8]",
    "output": "8",
    "testtype": "functional"
  },
  {
    "input": "[0]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[7]",
    "output": "7",
    "testtype": "functional"
  },
  {
    "input": "[1]",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "[-5]",
    "output": "-5",
    "testtype": "functional"
  },
  {
    "input": "[-5, 0]",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "[8, 8, -8, 1, 9]",
    "output": "576",
    "testtype": "functional"
  },
  {
    "input": "[7, 6, 9, 9, 8]",
    "output": "27216",
    "testtype": "functional"
  },
  {
    "input": "[-9, 1, 1, 0, -1, 9]",
    "output": "81",
    "testtype": "functional"
  },
  {
    "input": "[-9, -9, -6, -7, -3, -7, -6, -4, -1, -9, -2, -2, -3]",
    "output": "185177664",
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
You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i_0, i_1, i_2, ... , i_k is defined as nums[i_0] * nums[i_1] * nums[i_2] * ... * nums[i_k​].
Return the maximum strength of a group the teacher can create.
 
Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.

Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.

 
Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
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
    def maxStrength(self, nums: List[int]) -> int:
        # DP over sign: track best (max value) for positive and negative products.
        # dp_pos = maximum positive product achievable so far
        # dp_neg = maximum negative product achievable so far
        # Also track possibility of having chosen at least one element via None checks.
        dp_pos = None
        dp_neg = None

        for x in nums:
            new_pos, new_neg = dp_pos, dp_neg

            # Option 1: start new group with just x
            if x > 0:
                new_pos = x if new_pos is None else max(new_pos, x)
            elif x < 0:
                new_neg = x if new_neg is None else min(new_neg, x)

            # Option 2: extend existing groups
            if dp_pos is not None:
                # pos * x
                v = dp_pos * x
                if v > 0:
                    new_pos = v if new_pos is None else max(new_pos, v)
                elif v < 0:
                    new_neg = v if new_neg is None else min(new_neg, v)

            if dp_neg is not None:
                # neg * x
                v = dp_neg * x
                if v > 0:
                    new_pos = v if new_pos is None else max(new_pos, v)
                elif v < 0:
                    new_neg = v if new_neg is None else min(new_neg, v)

            dp_pos, dp_neg = new_pos, new_neg

        # We need maximum strength among all non-empty groups.
        # If we have any positive product, that's always >= any negative product.
        if dp_pos is not None:
            return dp_pos
        return dp_neg  # must exist since nums is non-empty
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        # DP on sign and absolute product magnitude using subset-splitting:
        # best[pos/neg] = max product with positive/negative sign formed so far
        # We do this with multiplicative DP on absolute values, but must keep sign.
        #
        # Typical approach: split by zeros not needed since nums[i] != 0? (not stated),
        # handle zeros naturally by allowing empty product not allowed.
        #
        # Instead use DP over subsets count: keep best product for positive/negative.
        # Since n <= 13, bitmask DP is also fine: compute max product over all subsets.
        # But product can be large; Python handles big ints.
        
        ans = None
        m = 1 << n
        for mask in range(1, m):  # non-empty subsets
            prod = 1
            for i in range(n):
                if mask & (1 << i):
                    prod *= nums[i]
            if ans is None or prod > ans:
                ans = prod
        return ans
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        # Split negatives/zeros/positives
        negatives = [x for x in nums if x < 0]
        zeros = sum(1 for x in nums if x == 0)
        positives = [x for x in nums if x > 0]

        # If we have no positive numbers
        if not positives:
            # If we can make at least one positive product using two negatives
            if len(negatives) == 0:
                # only zeros (or empty group not allowed, but we have at least one element)
                return 0
            if len(negatives) == 1:
                # single negative => best might be 0 if exists, otherwise negative
                return 0 if zeros > 0 else negatives[0]
            # if count of negatives is even, take all; else exclude the negative with smallest abs
            negatives_sorted = sorted(negatives)  # most negative first (smallest abs not necessarily last)
            # Sort by abs ascending to easily drop the smallest abs negative when needed
            negatives_by_abs = sorted(negatives, key=abs)

            if len(negatives) % 2 == 0:
                prod = 1
                for x in negatives:
                    prod *= x
                return prod
            else:
                # drop one negative with smallest abs to make count even
                prod = 1
                for x in negatives_by_abs[1:]:
                    prod *= x
                return prod

        # We have at least one positive
        # We'll form product by taking:
        # - all positives
        # - all negatives except possibly dropping one negative (with smallest abs) if total negatives count is odd
        # But if all negatives removed leads to empty? It can't, since positives non-empty.
        prod = 1
        for x in positives:
            prod *= x

        if len(negatives) % 2 == 0:
            for x in negatives:
                prod *= x
        else:
            # drop one negative with smallest abs
            negs_by_abs = sorted(negatives, key=abs)
            for x in negs_by_abs[1:]:
                prod *= x

        return prod
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Max product can be found by choosing a subset with either:
        # - an even number of negative numbers (positive product)
        # - or (if all products are negative) the best negative product by picking
        #   a subset whose magnitude is maximal (i.e., keep the "least bad" negative).
        #
        # But with a small n<=13, simplest correct approach:
        # - If count of zeros is present, a non-empty subset can also yield 0.
        # - Use DP tracking best products for even/odd count of negatives.
        #   (DP size is small; we can use integer DP with sentinel for impossible.)

        has_zero = 0 in nums
        negs = sum(1 for x in nums if x < 0)

        # DP: dp_even = best (max) product using some subset with even #negatives
        # dp_odd  = best product using some subset with odd #negatives
        # Initialize with "impossible" states.
        NEG_INF = None  # sentinel for impossible

        dp_even = 1   # empty subset (even negatives) as starting point
        dp_odd = NEG_INF

        # We must ensure group is non-empty at the end.
        # We'll process numbers one by one, updating products.
        for a in nums:
            new_even = dp_even
            new_odd = dp_odd

            # Form subset either by taking a and combining with previous subsets
            # or by not taking a (already represented by new_even/new_odd).
            if a == 0:
                # Taking zero makes product 0 with parity unchanged in terms of negatives count.
                # Starting from even subset (empty) gives non-empty product 0 as well.
                # Starting from both parities still yields 0.
                # We should consider subset that includes 0; that results in 0.
                if dp_even is not NEG_INF:
                    new_even = max(new_even, 0)
                if dp_odd is not NEG_INF:
                    new_odd = max(new_odd, 0)
            else:
                # Taking a flips parity if a is negative
                if a > 0:
                    # even stays even, odd stays odd
                    if dp_even is not NEG_INF:
                        new_even = max(new_even, dp_even * a)
                    if dp_odd is not NEG_INF:
                        new_odd = max(new_odd, dp_odd * a)
                else:
                    # a < 0: even -> odd, odd -> even
                    if dp_even is not NEG_INF:
                        new_odd = a * dp_even
                        # but new_odd might already exist; take max
                        if dp_odd is not NEG_INF:
                            new_odd = max(new_odd, dp_odd * 1)  # keep old if better (parity unchanged by not taking)
                    # Actually we also need to compute properly:
                    # new_odd = max(old_odd, dp_even * a)
                    # new_even = max(old_even, dp_odd * a)
                    candidate_odd = dp_even * a
                    new_odd = candidate_odd if dp_odd is NEG_INF else max(dp_odd, candidate_odd)
                    if dp_odd is not NEG_INF:
                        candidate_even = dp_odd * a
                        new_even = max(new_even, candidate_even)

            dp_even, dp_odd = new_even, new_odd

        # The above DP started from empty subset (dp_even=1),
        # so we need to exclude empty subset from answer.
        # How to do that robustly:
        # - Enumerate subset products since n<=13 is small.
        best = -10**18
        n = len(nums)
        for mask in range(1, 1 << n):
            prod = 1
            for i in range(n):
                if mask & (1 << i):
                    prod *= nums[i]
            if prod > best:
                best = prod
        return best
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        # Split by sign and handle separately.
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        zeros = n - len(pos) - len(neg)

        # If no positive numbers:
        # - If we have at least 2 negatives, best is product of all negatives with even count
        # - If we have exactly 1 negative, we can only do 0 (if zeros exist) or the negative itself
        if not pos:
            if len(neg) >= 2:
                neg.sort()  # most negative first
                if len(neg) % 2 == 1:
                    # Drop the one with smallest absolute value (closest to 0) to make even count
                    neg.sort(key=abs, reverse=True)  # largest abs first
                    neg = neg[0:len(neg)-1]
                prod = 1
                for x in neg:
                    prod *= x
                return prod
            # len(neg) is 0 or 1
            if neg:
                return 0 if zeros > 0 else neg[0]
            return 0  # all zeros

        # If we have positives:
        # The max product will use all positives.
        # For negatives:
        # - If count of negatives is even: include all
        # - If count is odd: exclude the negative with smallest absolute value
        prod = 1
        for x in pos:
            prod *= x

        if len(neg) % 2 == 0:
            for x in neg:
                prod *= x
        else:
            # Need to drop one negative (the one with smallest absolute value)
            neg.sort(key=abs)  # ascending abs; drop smallest abs
            for x in neg[1:]:
                prod *= x

        return prod
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List
from math import inf

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Split into non-zero parts and count zeros
        zeros = nums.count(0)
        nz = [x for x in nums if x != 0]

        # If all are zero, best non-empty group is strength 0
        if not nz:
            return 0

        # If no zeros, we must take all elements to maximize absolute product,
        # but sign may flip based on number of negatives.
        # Standard approach with DP over sign/max.
        has_even_neg = False
        # Use DP for maximum product for each sign state.
        # dp_pos: max positive product achievable
        # dp_neg: min (most negative) product achievable (i.e., negative with largest abs)
        dp_pos = -inf
        dp_neg = inf

        for x in nz:
            # When x is negative, sign flips
            if x > 0:
                new_pos = max(dp_pos * x, x, -dp_neg * x if dp_neg != inf else -inf)
                # dp_neg comes from dp_neg * x or starting new negative (not possible with x>0)
                new_neg = dp_neg * x if dp_neg != inf else inf
            else:
                # x < 0
                # positive product can come from dp_neg * x (two negatives)
                new_pos = max(dp_neg * x if dp_neg != inf else -inf, x * 0)  # placeholder
                # starting new group with negative gives negative product, not positive
                # We'll compute properly:
                cand_from_neg = dp_neg * x if dp_neg != inf else -inf
                new_pos = max(dp_pos * x if dp_pos != -inf else -inf, cand_from_neg, -inf)

                # negative product can come from dp_pos * x or starting new group with x
                cand1 = dp_pos * x if dp_pos != -inf else inf
                cand2 = x
                new_neg = min(cand1, cand2) if cand1 != inf else cand2

            # Fix up for placeholder issue in new_pos when dp_pos and dp_neg are infinities
            # We'll recompute with clean transitions:
            if x > 0:
                pos_from_pos = dp_pos * x if dp_pos != -inf else -inf
                pos_from_neg = (-dp_neg) * x if dp_neg != inf else -inf
                new_pos = max(pos_from_pos, x, pos_from_neg)
                new_neg = dp_neg * x if dp_neg != inf else inf
            else:
                neg_from_pos = dp_pos * x if dp_pos != -inf else inf
                # starting new group
                new_neg = min(neg_from_pos, x)
                pos_from_neg = dp_neg * x if dp_neg != inf else -inf
                pos_from_pos = dp_pos * x if dp_pos != -inf else -inf
                new_pos = max(pos_from_neg, pos_from_pos)

            dp_pos, dp_neg = new_pos, new_neg

        # If zeros exist, we can also get strength 0 by choosing any zero alone.
        # Optimal is the maximum strength among positive products; if none, 0 or negative best.
        ans = 0 if zeros > 0 else -inf
        if dp_pos != -inf:
            ans = max(ans, dp_pos)
        elif zeros == 0:
            # No positive product possible; take the least negative (closest to zero)
            # dp_neg is negative product with largest abs; but we want maximum => closest to zero:
            if dp_neg != inf:
                ans = dp_neg  # dp_neg is negative; max among negatives is closest to zero but
                               # our dp_neg tracks the minimum value (most negative) during build,
                               # so we need a different DP. We'll handle via subset logic below.
        # The above DP for negative branch doesn't guarantee "closest to zero" for dp_neg.
        # Use a safer subset approach based on counting negatives:
        # If dp_pos exists, that's optimal; otherwise, we either pick one negative (if no zeros)
        # or 0 (if zeros exist).
        if ans == 0 and dp_pos == -inf:
            return 0

        # Safe fallback: compute by removing minimal absolute value to make product positive,
        # or take maximum negative if zeros==0 and positives impossible.
        neg_count = sum(1 for x in nz if x < 0)
        # product magnitude of all non-zeros
        prod = 1
        for x in nz:
            prod *= x

        if neg_count % 2 == 0:
            # Product of all is positive and maximal in magnitude
            return prod
        else:
            # Must make it non-negative: either drop smallest abs negative to make product positive,
            # or if zeros exist allow 0.
            min_abs_neg = min(abs(x) for x in nz if x < 0)
            if zeros > 0:
                # choosing empty sign? not allowed; but 0 from choosing a zero alone is valid
                # Compare positive product (after dropping) against 0
                pos_prod = prod // (-min_abs_neg)  # prod / negative gives positive; integer division safe
                return max(0, pos_prod)
            else:
                # No zeros: drop smallest abs negative to make positive
                return prod // (-min_abs_neg)
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Sort by absolute value descending, since we only need max product
        nums.sort(key=lambda x: abs(x), reverse=True)
        n = len(nums)
        
        # dp[parity] = maximum product achievable using some prefix with given parity of negatives
        # parity 0 => product has even number of negative factors (non-negative product)
        # parity 1 => product has odd number of negative factors (negative product)
        # We use Python ints; numbers are small enough, but sign handling matters.
        dp0, dp1 = 1, None  # dp0 starts with empty product=1 (even negatives=0)
        
        for x in nums:
            if x == 0:
                # Optionally, zero could be chosen as a group element; it yields product 0.
                # But since we want maximum, zero is only relevant if all non-zero products are negative.
                # We'll incorporate it by allowing product 0 as a candidate.
                # Because product becomes 0 regardless of sign parity, treat it separately.
                continue
            
            new_dp0, new_dp1 = None, None
            # extend with x
            if dp0 is not None:
                prod = dp0 * x
                if prod >= 0:
                    new_dp0 = prod if new_dp0 is None else max(new_dp0, prod)
                else:
                    new_dp1 = prod if new_dp1 is None else max(new_dp1, prod)
            if dp1 is not None:
                prod = dp1 * x
                if prod >= 0:
                    new_dp0 = prod if new_dp0 is None else max(new_dp0, prod)
                else:
                    new_dp1 = prod if new_dp1 is None else max(new_dp1, prod)
            
            # also start a new group with just x (parity depends on sign)
            if x >= 0:
                new_dp0 = x if new_dp0 is None else max(new_dp0, x)
            else:
                new_dp1 = x if new_dp1 is None else max(new_dp1, x)
            
            dp0, dp1 = new_dp0, new_dp1
        
        # Include possible effect of zeros:
        has_zero = any(x == 0 for x in nums)
        ans = None
        if dp0 is not None:
            ans = dp0
        if has_zero and (ans is None or ans < 0):
            ans = 0
        if ans is None:
            # Only possible if all nums are 0 (but then group product is 0) or something went wrong.
            ans = 0
        
        # dp0 could represent empty product; disallow empty by ensuring group is non-empty.
        # Our dp0 initialization with 1 (empty) gets overwritten by actual picks through updates.
        # If all products were negative and dp0 is 1 from empty, we'd need correction.
        # To robustly fix, compute using classic approach:
        nonzero = [x for x in nums if x != 0]
        if not nonzero:
            return 0
        
        # Classic greedy-by-absolute-value with sign handling:
        nonzero.sort(key=lambda x: abs(x), reverse=True)
        prod = 1
        neg_count = 0
        for x in nonzero:
            prod *= x
            if x < 0:
                neg_count += 1
        
        if neg_count % 2 == 0:
            return prod
        # If odd negatives, remove the one with smallest absolute value to make negatives even
        smallest_abs = min(nonzero, key=lambda x: abs(x))
        return prod // smallest_abs  # exact division since smallest_abs divides prod

```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = [x for x in nums if x > 0]
        neg = sorted([x for x in nums if x < 0])  # most negative first
        npos = len(pos)
        nneg = len(neg)

        # If there are no non-negative/positive numbers:
        if npos == 0:
            # Only negatives (or no elements, but constraints say length>=1)
            # To maximize product with negatives only, we want:
            # - even count => positive product (best)
            # - odd count => best positive product? we can only have odd => negative; max would be closest to 0
            if nneg == 0:
                # all zeros
                return 0
            if nneg % 2 == 0:
                prod = 1
                for x in neg:
                    prod *= x
                return prod
            else:
                # drop the negative with smallest magnitude (largest value, closest to 0)
                # since neg is sorted ascending, remove last
                prod = 1
                for x in neg[:-1]:
                    prod *= x
                return prod

        # Handle zeros: they can be used to avoid having an odd number of negatives
        zeros = sum(1 for x in nums if x == 0)

        # If we have at least one positive, optimal strategy:
        # take all positives, and take as many negatives as possible with even count.
        # If remaining negatives count is odd, drop one negative with smallest absolute value.
        take_neg = nneg
        if take_neg % 2 == 1:
            if zeros == 0:
                # must drop one negative to make even count
                # drop the negative closest to 0 (largest value)
                # neg sorted ascending => remove last
                take_neg -= 1
                prod_neg = 1
                for x in neg[:-1]:
                    prod_neg *= x
                prod_pos = 1
                for x in pos:
                    prod_pos *= x
                return prod_pos * prod_neg
            else:
                # zeros exist: we can drop all negatives if they can't be paired,
                # but since we have positives, better to still drop exactly one negative
                # to keep product as positive (or use zeros only if product would be negative).
                take_neg -= 1
                prod_neg = 1
                for x in neg[:-1]:
                    prod_neg *= x
                prod_pos = 1
                for x in pos:
                    prod_pos *= x
                return prod_pos * prod_neg

        # Even number of negatives: take all
        prod = 1
        for x in pos:
            prod *= x
        for x in neg:
            prod *= x
        return prod
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List
from functools import lru_cache
import math

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i: int, parity: int) -> int:
            """
            Returns the maximum product from nums[i:] using at least one element,
            where the product's sign parity is:
              parity = 0 -> product is non-negative (0 or +)
              parity = 1 -> product is negative
            """
            if i == n:
                # No elements chosen; invalid state for "at least one element"
                return -math.inf

            # Option 1: skip nums[i]
            best = dp(i + 1, parity)

            x = nums[i]
            # Option 2: take nums[i] and then maybe more
            # Start with just x
            if x >= 0:
                cand = x
                if cand >= 0:
                    best = max(best, cand)
            else:
                # x < 0
                best = max(best, x)

            # Option 3: take x, then take more from dp(i+1, new_parity)
            # If we previously chose a product P from dp(i+1, p2) (with at least one element),
            # total product = x * P.
            for p2 in (0, 1):
                p_val = dp(i + 1, p2)
                if p_val == -math.inf:
                    continue
                total = x * p_val
                new_parity = 0 if total >= 0 else 1
                if new_parity == parity:
                    best = max(best, total)

            return best

        # The answer must be from a non-empty group.
        # Best among non-negative and negative depending on max.
        nonneg = dp(0, 0)
        neg = dp(0, 1)

        # If all products are negative, nonneg may still be -inf; handle.
        return max(nonneg, neg)
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Meet-in-the-middle over sign/zero handling.
        # Let m = 2^(n/2) subsets; compute product for non-empty subsets.
        # Track best positive and best negative (closest to zero) since
        # combining subsets depends on sign.
        n = len(nums)
        mid = n // 2
        A = nums[:mid]
        B = nums[mid:]

        def gen(subarr):
            m = len(subarr)
            out = []
            # Iterate all non-empty subsets
            for mask in range(1, 1 << m):
                prod = 1
                for i in range(m):
                    if mask & (1 << i):
                        prod *= subarr[i]
                out.append(prod)
            return out

        SA = gen(A)
        SB = gen(B)

        # We need max over all non-empty unions:
        # union may be entirely within A, within B, or across both.
        # If we take prodA * prodB, union is non-empty iff:
        # - both non-empty (subset from A and subset from B)
        # We'll compute candidates:
        # 1) max of subsets entirely in A
        # 2) max of subsets entirely in B
        ans = max(max(SA) if SA else -10**18, max(SB) if SB else -10**18)

        # For cross-subsets, we need maximize prodA * prodB.
        # Since nums[i] are small and n<=13, brute cross is feasible:
        # |SA| <= 2^6-1=63, |SB|<=2^7-1=127, product <= ~8000.
        for pa in SA:
            for pb in SB:
                val = pa * pb
                if val > ans:
                    ans = val
        return ans
```
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.8571 | `partial` |
| 1 | 1.0000 | `full` |
| 2 | 1.0000 | `full` |
| 3 | 1.0000 | `full` |
| 4 | 1.0000 | `full` |
| 5 | 0.9286 | `partial` |
| 6 | 0.7857 | `partial` |
| 7 | 0.8571 | `partial` |
| 8 | 0.7857 | `partial` |
| 9 | 1.0000 | `full` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 12,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "None",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "-5",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "-5",
      "actual": "1",
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
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
      "passed": true,
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "-5",
      "actual": "1",
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
      "expected": "576",
      "actual": "-4608",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
  "passed": 12,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
      "error": ""
    },
    {
      "passed": true,
      "expected": "1",
      "actual": "1",
      "error": ""
    },
    {
      "passed": false,
      "expected": "-5",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
  "passed": 11,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "30",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "18",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i_0, i_1, i_2, ... , i_k is defined as nums[i_0] * nums[i_1] * nums[i_2] * ... * nums[i_k​].
Return the maximum strength of a group the teacher can create.
 
Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.

Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.

 
Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9

### Solutions
#### Correct
Attempt 1
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        # DP on sign and absolute product magnitude using subset-splitting:
        # best[pos/neg] = max product with positive/negative sign formed so far
        # We do this with multiplicative DP on absolute values, but must keep sign.
        #
        # Typical approach: split by zeros not needed since nums[i] != 0? (not stated),
        # handle zeros naturally by allowing empty product not allowed.
        #
        # Instead use DP over subsets count: keep best product for positive/negative.
        # Since n <= 13, bitmask DP is also fine: compute max product over all subsets.
        # But product can be large; Python handles big ints.
        
        ans = None
        m = 1 << n
        for mask in range(1, m):  # non-empty subsets
            prod = 1
            for i in range(n):
                if mask & (1 << i):
                    prod *= nums[i]
            if ans is None or prod > ans:
                ans = prod
        return ans
```

Attempt 2
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        # Split negatives/zeros/positives
        negatives = [x for x in nums if x < 0]
        zeros = sum(1 for x in nums if x == 0)
        positives = [x for x in nums if x > 0]

        # If we have no positive numbers
        if not positives:
            # If we can make at least one positive product using two negatives
            if len(negatives) == 0:
                # only zeros (or empty group not allowed, but we have at least one element)
                return 0
            if len(negatives) == 1:
                # single negative => best might be 0 if exists, otherwise negative
                return 0 if zeros > 0 else negatives[0]
            # if count of negatives is even, take all; else exclude the negative with smallest abs
            negatives_sorted = sorted(negatives)  # most negative first (smallest abs not necessarily last)
            # Sort by abs ascending to easily drop the smallest abs negative when needed
            negatives_by_abs = sorted(negatives, key=abs)

            if len(negatives) % 2 == 0:
                prod = 1
                for x in negatives:
                    prod *= x
                return prod
            else:
                # drop one negative with smallest abs to make count even
                prod = 1
                for x in negatives_by_abs[1:]:
                    prod *= x
                return prod

        # We have at least one positive
        # We'll form product by taking:
        # - all positives
        # - all negatives except possibly dropping one negative (with smallest abs) if total negatives count is odd
        # But if all negatives removed leads to empty? It can't, since positives non-empty.
        prod = 1
        for x in positives:
            prod *= x

        if len(negatives) % 2 == 0:
            for x in negatives:
                prod *= x
        else:
            # drop one negative with smallest abs
            negs_by_abs = sorted(negatives, key=abs)
            for x in negs_by_abs[1:]:
                prod *= x

        return prod
```

Attempt 3
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Max product can be found by choosing a subset with either:
        # - an even number of negative numbers (positive product)
        # - or (if all products are negative) the best negative product by picking
        #   a subset whose magnitude is maximal (i.e., keep the "least bad" negative).
        #
        # But with a small n<=13, simplest correct approach:
        # - If count of zeros is present, a non-empty subset can also yield 0.
        # - Use DP tracking best products for even/odd count of negatives.
        #   (DP size is small; we can use integer DP with sentinel for impossible.)

        has_zero = 0 in nums
        negs = sum(1 for x in nums if x < 0)

        # DP: dp_even = best (max) product using some subset with even #negatives
        # dp_odd  = best product using some subset with odd #negatives
        # Initialize with "impossible" states.
        NEG_INF = None  # sentinel for impossible

        dp_even = 1   # empty subset (even negatives) as starting point
        dp_odd = NEG_INF

        # We must ensure group is non-empty at the end.
        # We'll process numbers one by one, updating products.
        for a in nums:
            new_even = dp_even
            new_odd = dp_odd

            # Form subset either by taking a and combining with previous subsets
            # or by not taking a (already represented by new_even/new_odd).
            if a == 0:
                # Taking zero makes product 0 with parity unchanged in terms of negatives count.
                # Starting from even subset (empty) gives non-empty product 0 as well.
                # Starting from both parities still yields 0.
                # We should consider subset that includes 0; that results in 0.
                if dp_even is not NEG_INF:
                    new_even = max(new_even, 0)
                if dp_odd is not NEG_INF:
                    new_odd = max(new_odd, 0)
            else:
                # Taking a flips parity if a is negative
                if a > 0:
                    # even stays even, odd stays odd
                    if dp_even is not NEG_INF:
                        new_even = max(new_even, dp_even * a)
                    if dp_odd is not NEG_INF:
                        new_odd = max(new_odd, dp_odd * a)
                else:
                    # a < 0: even -> odd, odd -> even
                    if dp_even is not NEG_INF:
                        new_odd = a * dp_even
                        # but new_odd might already exist; take max
                        if dp_odd is not NEG_INF:
                            new_odd = max(new_odd, dp_odd * 1)  # keep old if better (parity unchanged by not taking)
                    # Actually we also need to compute properly:
                    # new_odd = max(old_odd, dp_even * a)
                    # new_even = max(old_even, dp_odd * a)
                    candidate_odd = dp_even * a
                    new_odd = candidate_odd if dp_odd is NEG_INF else max(dp_odd, candidate_odd)
                    if dp_odd is not NEG_INF:
                        candidate_even = dp_odd * a
                        new_even = max(new_even, candidate_even)

            dp_even, dp_odd = new_even, new_odd

        # The above DP started from empty subset (dp_even=1),
        # so we need to exclude empty subset from answer.
        # How to do that robustly:
        # - Enumerate subset products since n<=13 is small.
        best = -10**18
        n = len(nums)
        for mask in range(1, 1 << n):
            prod = 1
            for i in range(n):
                if mask & (1 << i):
                    prod *= nums[i]
            if prod > best:
                best = prod
        return best
```

Attempt 4
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        # Split by sign and handle separately.
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        zeros = n - len(pos) - len(neg)

        # If no positive numbers:
        # - If we have at least 2 negatives, best is product of all negatives with even count
        # - If we have exactly 1 negative, we can only do 0 (if zeros exist) or the negative itself
        if not pos:
            if len(neg) >= 2:
                neg.sort()  # most negative first
                if len(neg) % 2 == 1:
                    # Drop the one with smallest absolute value (closest to 0) to make even count
                    neg.sort(key=abs, reverse=True)  # largest abs first
                    neg = neg[0:len(neg)-1]
                prod = 1
                for x in neg:
                    prod *= x
                return prod
            # len(neg) is 0 or 1
            if neg:
                return 0 if zeros > 0 else neg[0]
            return 0  # all zeros

        # If we have positives:
        # The max product will use all positives.
        # For negatives:
        # - If count of negatives is even: include all
        # - If count is odd: exclude the negative with smallest absolute value
        prod = 1
        for x in pos:
            prod *= x

        if len(neg) % 2 == 0:
            for x in neg:
                prod *= x
        else:
            # Need to drop one negative (the one with smallest absolute value)
            neg.sort(key=abs)  # ascending abs; drop smallest abs
            for x in neg[1:]:
                prod *= x

        return prod
```

Attempt 5
```python
from typing import List
from functools import lru_cache

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Meet-in-the-middle over sign/zero handling.
        # Let m = 2^(n/2) subsets; compute product for non-empty subsets.
        # Track best positive and best negative (closest to zero) since
        # combining subsets depends on sign.
        n = len(nums)
        mid = n // 2
        A = nums[:mid]
        B = nums[mid:]

        def gen(subarr):
            m = len(subarr)
            out = []
            # Iterate all non-empty subsets
            for mask in range(1, 1 << m):
                prod = 1
                for i in range(m):
                    if mask & (1 << i):
                        prod *= subarr[i]
                out.append(prod)
            return out

        SA = gen(A)
        SB = gen(B)

        # We need max over all non-empty unions:
        # union may be entirely within A, within B, or across both.
        # If we take prodA * prodB, union is non-empty iff:
        # - both non-empty (subset from A and subset from B)
        # We'll compute candidates:
        # 1) max of subsets entirely in A
        # 2) max of subsets entirely in B
        ans = max(max(SA) if SA else -10**18, max(SB) if SB else -10**18)

        # For cross-subsets, we need maximize prodA * prodB.
        # Since nums[i] are small and n<=13, brute cross is feasible:
        # |SA| <= 2^6-1=63, |SB|<=2^7-1=127, product <= ~8000.
        for pa in SA:
            for pb in SB:
                val = pa * pb
                if val > ans:
                    ans = val
        return ans
```

#### Partially Correct
Attempt 1
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # DP over sign: track best (max value) for positive and negative products.
        # dp_pos = maximum positive product achievable so far
        # dp_neg = maximum negative product achievable so far
        # Also track possibility of having chosen at least one element via None checks.
        dp_pos = None
        dp_neg = None

        for x in nums:
            new_pos, new_neg = dp_pos, dp_neg

            # Option 1: start new group with just x
            if x > 0:
                new_pos = x if new_pos is None else max(new_pos, x)
            elif x < 0:
                new_neg = x if new_neg is None else min(new_neg, x)

            # Option 2: extend existing groups
            if dp_pos is not None:
                # pos * x
                v = dp_pos * x
                if v > 0:
                    new_pos = v if new_pos is None else max(new_pos, v)
                elif v < 0:
                    new_neg = v if new_neg is None else min(new_neg, v)

            if dp_neg is not None:
                # neg * x
                v = dp_neg * x
                if v > 0:
                    new_pos = v if new_pos is None else max(new_pos, v)
                elif v < 0:
                    new_neg = v if new_neg is None else min(new_neg, v)

            dp_pos, dp_neg = new_pos, new_neg

        # We need maximum strength among all non-empty groups.
        # If we have any positive product, that's always >= any negative product.
        if dp_pos is not None:
            return dp_pos
        return dp_neg  # must exist since nums is non-empty
```

Attempt 2
```python
from typing import List
from math import inf

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Split into non-zero parts and count zeros
        zeros = nums.count(0)
        nz = [x for x in nums if x != 0]

        # If all are zero, best non-empty group is strength 0
        if not nz:
            return 0

        # If no zeros, we must take all elements to maximize absolute product,
        # but sign may flip based on number of negatives.
        # Standard approach with DP over sign/max.
        has_even_neg = False
        # Use DP for maximum product for each sign state.
        # dp_pos: max positive product achievable
        # dp_neg: min (most negative) product achievable (i.e., negative with largest abs)
        dp_pos = -inf
        dp_neg = inf

        for x in nz:
            # When x is negative, sign flips
            if x > 0:
                new_pos = max(dp_pos * x, x, -dp_neg * x if dp_neg != inf else -inf)
                # dp_neg comes from dp_neg * x or starting new negative (not possible with x>0)
                new_neg = dp_neg * x if dp_neg != inf else inf
            else:
                # x < 0
                # positive product can come from dp_neg * x (two negatives)
                new_pos = max(dp_neg * x if dp_neg != inf else -inf, x * 0)  # placeholder
                # starting new group with negative gives negative product, not positive
                # We'll compute properly:
                cand_from_neg = dp_neg * x if dp_neg != inf else -inf
                new_pos = max(dp_pos * x if dp_pos != -inf else -inf, cand_from_neg, -inf)

                # negative product can come from dp_pos * x or starting new group with x
                cand1 = dp_pos * x if dp_pos != -inf else inf
                cand2 = x
                new_neg = min(cand1, cand2) if cand1 != inf else cand2

            # Fix up for placeholder issue in new_pos when dp_pos and dp_neg are infinities
            # We'll recompute with clean transitions:
            if x > 0:
                pos_from_pos = dp_pos * x if dp_pos != -inf else -inf
                pos_from_neg = (-dp_neg) * x if dp_neg != inf else -inf
                new_pos = max(pos_from_pos, x, pos_from_neg)
                new_neg = dp_neg * x if dp_neg != inf else inf
            else:
                neg_from_pos = dp_pos * x if dp_pos != -inf else inf
                # starting new group
                new_neg = min(neg_from_pos, x)
                pos_from_neg = dp_neg * x if dp_neg != inf else -inf
                pos_from_pos = dp_pos * x if dp_pos != -inf else -inf
                new_pos = max(pos_from_neg, pos_from_pos)

            dp_pos, dp_neg = new_pos, new_neg

        # If zeros exist, we can also get strength 0 by choosing any zero alone.
        # Optimal is the maximum strength among positive products; if none, 0 or negative best.
        ans = 0 if zeros > 0 else -inf
        if dp_pos != -inf:
            ans = max(ans, dp_pos)
        elif zeros == 0:
            # No positive product possible; take the least negative (closest to zero)
            # dp_neg is negative product with largest abs; but we want maximum => closest to zero:
            if dp_neg != inf:
                ans = dp_neg  # dp_neg is negative; max among negatives is closest to zero but
                               # our dp_neg tracks the minimum value (most negative) during build,
                               # so we need a different DP. We'll handle via subset logic below.
        # The above DP for negative branch doesn't guarantee "closest to zero" for dp_neg.
        # Use a safer subset approach based on counting negatives:
        # If dp_pos exists, that's optimal; otherwise, we either pick one negative (if no zeros)
        # or 0 (if zeros exist).
        if ans == 0 and dp_pos == -inf:
            return 0

        # Safe fallback: compute by removing minimal absolute value to make product positive,
        # or take maximum negative if zeros==0 and positives impossible.
        neg_count = sum(1 for x in nz if x < 0)
        # product magnitude of all non-zeros
        prod = 1
        for x in nz:
            prod *= x

        if neg_count % 2 == 0:
            # Product of all is positive and maximal in magnitude
            return prod
        else:
            # Must make it non-negative: either drop smallest abs negative to make product positive,
            # or if zeros exist allow 0.
            min_abs_neg = min(abs(x) for x in nz if x < 0)
            if zeros > 0:
                # choosing empty sign? not allowed; but 0 from choosing a zero alone is valid
                # Compare positive product (after dropping) against 0
                pos_prod = prod // (-min_abs_neg)  # prod / negative gives positive; integer division safe
                return max(0, pos_prod)
            else:
                # No zeros: drop smallest abs negative to make positive
                return prod // (-min_abs_neg)
```

Attempt 3
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Sort by absolute value descending, since we only need max product
        nums.sort(key=lambda x: abs(x), reverse=True)
        n = len(nums)
        
        # dp[parity] = maximum product achievable using some prefix with given parity of negatives
        # parity 0 => product has even number of negative factors (non-negative product)
        # parity 1 => product has odd number of negative factors (negative product)
        # We use Python ints; numbers are small enough, but sign handling matters.
        dp0, dp1 = 1, None  # dp0 starts with empty product=1 (even negatives=0)
        
        for x in nums:
            if x == 0:
                # Optionally, zero could be chosen as a group element; it yields product 0.
                # But since we want maximum, zero is only relevant if all non-zero products are negative.
                # We'll incorporate it by allowing product 0 as a candidate.
                # Because product becomes 0 regardless of sign parity, treat it separately.
                continue
            
            new_dp0, new_dp1 = None, None
            # extend with x
            if dp0 is not None:
                prod = dp0 * x
                if prod >= 0:
                    new_dp0 = prod if new_dp0 is None else max(new_dp0, prod)
                else:
                    new_dp1 = prod if new_dp1 is None else max(new_dp1, prod)
            if dp1 is not None:
                prod = dp1 * x
                if prod >= 0:
                    new_dp0 = prod if new_dp0 is None else max(new_dp0, prod)
                else:
                    new_dp1 = prod if new_dp1 is None else max(new_dp1, prod)
            
            # also start a new group with just x (parity depends on sign)
            if x >= 0:
                new_dp0 = x if new_dp0 is None else max(new_dp0, x)
            else:
                new_dp1 = x if new_dp1 is None else max(new_dp1, x)
            
            dp0, dp1 = new_dp0, new_dp1
        
        # Include possible effect of zeros:
        has_zero = any(x == 0 for x in nums)
        ans = None
        if dp0 is not None:
            ans = dp0
        if has_zero and (ans is None or ans < 0):
            ans = 0
        if ans is None:
            # Only possible if all nums are 0 (but then group product is 0) or something went wrong.
            ans = 0
        
        # dp0 could represent empty product; disallow empty by ensuring group is non-empty.
        # Our dp0 initialization with 1 (empty) gets overwritten by actual picks through updates.
        # If all products were negative and dp0 is 1 from empty, we'd need correction.
        # To robustly fix, compute using classic approach:
        nonzero = [x for x in nums if x != 0]
        if not nonzero:
            return 0
        
        # Classic greedy-by-absolute-value with sign handling:
        nonzero.sort(key=lambda x: abs(x), reverse=True)
        prod = 1
        neg_count = 0
        for x in nonzero:
            prod *= x
            if x < 0:
                neg_count += 1
        
        if neg_count % 2 == 0:
            return prod
        # If odd negatives, remove the one with smallest absolute value to make negatives even
        smallest_abs = min(nonzero, key=lambda x: abs(x))
        return prod // smallest_abs  # exact division since smallest_abs divides prod

```

Attempt 4
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = [x for x in nums if x > 0]
        neg = sorted([x for x in nums if x < 0])  # most negative first
        npos = len(pos)
        nneg = len(neg)

        # If there are no non-negative/positive numbers:
        if npos == 0:
            # Only negatives (or no elements, but constraints say length>=1)
            # To maximize product with negatives only, we want:
            # - even count => positive product (best)
            # - odd count => best positive product? we can only have odd => negative; max would be closest to 0
            if nneg == 0:
                # all zeros
                return 0
            if nneg % 2 == 0:
                prod = 1
                for x in neg:
                    prod *= x
                return prod
            else:
                # drop the negative with smallest magnitude (largest value, closest to 0)
                # since neg is sorted ascending, remove last
                prod = 1
                for x in neg[:-1]:
                    prod *= x
                return prod

        # Handle zeros: they can be used to avoid having an odd number of negatives
        zeros = sum(1 for x in nums if x == 0)

        # If we have at least one positive, optimal strategy:
        # take all positives, and take as many negatives as possible with even count.
        # If remaining negatives count is odd, drop one negative with smallest absolute value.
        take_neg = nneg
        if take_neg % 2 == 1:
            if zeros == 0:
                # must drop one negative to make even count
                # drop the negative closest to 0 (largest value)
                # neg sorted ascending => remove last
                take_neg -= 1
                prod_neg = 1
                for x in neg[:-1]:
                    prod_neg *= x
                prod_pos = 1
                for x in pos:
                    prod_pos *= x
                return prod_pos * prod_neg
            else:
                # zeros exist: we can drop all negatives if they can't be paired,
                # but since we have positives, better to still drop exactly one negative
                # to keep product as positive (or use zeros only if product would be negative).
                take_neg -= 1
                prod_neg = 1
                for x in neg[:-1]:
                    prod_neg *= x
                prod_pos = 1
                for x in pos:
                    prod_pos *= x
                return prod_pos * prod_neg

        # Even number of negatives: take all
        prod = 1
        for x in pos:
            prod *= x
        for x in neg:
            prod *= x
        return prod
```

Attempt 5
```python
from typing import List
from functools import lru_cache
import math

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i: int, parity: int) -> int:
            """
            Returns the maximum product from nums[i:] using at least one element,
            where the product's sign parity is:
              parity = 0 -> product is non-negative (0 or +)
              parity = 1 -> product is negative
            """
            if i == n:
                # No elements chosen; invalid state for "at least one element"
                return -math.inf

            # Option 1: skip nums[i]
            best = dp(i + 1, parity)

            x = nums[i]
            # Option 2: take nums[i] and then maybe more
            # Start with just x
            if x >= 0:
                cand = x
                if cand >= 0:
                    best = max(best, cand)
            else:
                # x < 0
                best = max(best, x)

            # Option 3: take x, then take more from dp(i+1, new_parity)
            # If we previously chose a product P from dp(i+1, p2) (with at least one element),
            # total product = x * P.
            for p2 in (0, 1):
                p_val = dp(i + 1, p2)
                if p_val == -math.inf:
                    continue
                total = x * p_val
                new_parity = 0 if total >= 0 else 1
                if new_parity == parity:
                    best = max(best, total)

            return best

        # The answer must be from a non-empty group.
        # Best among non-negative and negative depending on max.
        nonneg = dp(0, 0)
        neg = dp(0, 1)

        # If all products are negative, nonneg may still be -inf; handle.
        return max(nonneg, neg)
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
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        # DP on sign and absolute product magnitude using subset-splitting:
        # best[pos/neg] = max product with positive/negative sign formed so far
        # We do this with multiplicative DP on absolute values, but must keep sign.
        #
        # Typical approach: split by zeros not needed since nums[i] != 0? (not stated),
        # handle zeros naturally by allowing empty product not allowed.
        #
        # Instead use DP over subsets count: keep best product for positive/negative.
        # Since n <= 13, bitmask DP is also fine: compute max product over all subsets.
        # But product can be large; Python handles big ints.
        
        ans = None
        m = 1 << n
        for mask in range(1, m):  # non-empty subsets
            prod = 1
            for i in range(n):
                if mask & (1 << i):
                    prod *= nums[i]
            if ans is None or prod > ans:
                ans = prod
        return ans
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        # Split negatives/zeros/positives
        negatives = [x for x in nums if x < 0]
        zeros = sum(1 for x in nums if x == 0)
        positives = [x for x in nums if x > 0]

        # If we have no positive numbers
        if not positives:
            # If we can make at least one positive product using two negatives
            if len(negatives) == 0:
                # only zeros (or empty group not allowed, but we have at least one element)
                return 0
            if len(negatives) == 1:
                # single negative => best might be 0 if exists, otherwise negative
                return 0 if zeros > 0 else negatives[0]
            # if count of negatives is even, take all; else exclude the negative with smallest abs
            negatives_sorted = sorted(negatives)  # most negative first (smallest abs not necessarily last)
            # Sort by abs ascending to easily drop the smallest abs negative when needed
            negatives_by_abs = sorted(negatives, key=abs)

            if len(negatives) % 2 == 0:
                prod = 1
                for x in negatives:
                    prod *= x
                return prod
            else:
                # drop one negative with smallest abs to make count even
                prod = 1
                for x in negatives_by_abs[1:]:
                    prod *= x
                return prod

        # We have at least one positive
        # We'll form product by taking:
        # - all positives
        # - all negatives except possibly dropping one negative (with smallest abs) if total negatives count is odd
        # But if all negatives removed leads to empty? It can't, since positives non-empty.
        prod = 1
        for x in positives:
            prod *= x

        if len(negatives) % 2 == 0:
            for x in negatives:
                prod *= x
        else:
            # drop one negative with smallest abs
            negs_by_abs = sorted(negatives, key=abs)
            for x in negs_by_abs[1:]:
                prod *= x

        return prod
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Max product can be found by choosing a subset with either:
        # - an even number of negative numbers (positive product)
        # - or (if all products are negative) the best negative product by picking
        #   a subset whose magnitude is maximal (i.e., keep the "least bad" negative).
        #
        # But with a small n<=13, simplest correct approach:
        # - If count of zeros is present, a non-empty subset can also yield 0.
        # - Use DP tracking best products for even/odd count of negatives.
        #   (DP size is small; we can use integer DP with sentinel for impossible.)

        has_zero = 0 in nums
        negs = sum(1 for x in nums if x < 0)

        # DP: dp_even = best (max) product using some subset with even #negatives
        # dp_odd  = best product using some subset with odd #negatives
        # Initialize with "impossible" states.
        NEG_INF = None  # sentinel for impossible

        dp_even = 1   # empty subset (even negatives) as starting point
        dp_odd = NEG_INF

        # We must ensure group is non-empty at the end.
        # We'll process numbers one by one, updating products.
        for a in nums:
            new_even = dp_even
            new_odd = dp_odd

            # Form subset either by taking a and combining with previous subsets
            # or by not taking a (already represented by new_even/new_odd).
            if a == 0:
                # Taking zero makes product 0 with parity unchanged in terms of negatives count.
                # Starting from even subset (empty) gives non-empty product 0 as well.
                # Starting from both parities still yields 0.
                # We should consider subset that includes 0; that results in 0.
                if dp_even is not NEG_INF:
                    new_even = max(new_even, 0)
                if dp_odd is not NEG_INF:
                    new_odd = max(new_odd, 0)
            else:
                # Taking a flips parity if a is negative
                if a > 0:
                    # even stays even, odd stays odd
                    if dp_even is not NEG_INF:
                        new_even = max(new_even, dp_even * a)
                    if dp_odd is not NEG_INF:
                        new_odd = max(new_odd, dp_odd * a)
                else:
                    # a < 0: even -> odd, odd -> even
                    if dp_even is not NEG_INF:
                        new_odd = a * dp_even
                        # but new_odd might already exist; take max
                        if dp_odd is not NEG_INF:
                            new_odd = max(new_odd, dp_odd * 1)  # keep old if better (parity unchanged by not taking)
                    # Actually we also need to compute properly:
                    # new_odd = max(old_odd, dp_even * a)
                    # new_even = max(old_even, dp_odd * a)
                    candidate_odd = dp_even * a
                    new_odd = candidate_odd if dp_odd is NEG_INF else max(dp_odd, candidate_odd)
                    if dp_odd is not NEG_INF:
                        candidate_even = dp_odd * a
                        new_even = max(new_even, candidate_even)

            dp_even, dp_odd = new_even, new_odd

        # The above DP started from empty subset (dp_even=1),
        # so we need to exclude empty subset from answer.
        # How to do that robustly:
        # - Enumerate subset products since n<=13 is small.
        best = -10**18
        n = len(nums)
        for mask in range(1, 1 << n):
            prod = 1
            for i in range(n):
                if mask & (1 << i):
                    prod *= nums[i]
            if prod > best:
                best = prod
        return best
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        # Split by sign and handle separately.
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        zeros = n - len(pos) - len(neg)

        # If no positive numbers:
        # - If we have at least 2 negatives, best is product of all negatives with even count
        # - If we have exactly 1 negative, we can only do 0 (if zeros exist) or the negative itself
        if not pos:
            if len(neg) >= 2:
                neg.sort()  # most negative first
                if len(neg) % 2 == 1:
                    # Drop the one with smallest absolute value (closest to 0) to make even count
                    neg.sort(key=abs, reverse=True)  # largest abs first
                    neg = neg[0:len(neg)-1]
                prod = 1
                for x in neg:
                    prod *= x
                return prod
            # len(neg) is 0 or 1
            if neg:
                return 0 if zeros > 0 else neg[0]
            return 0  # all zeros

        # If we have positives:
        # The max product will use all positives.
        # For negatives:
        # - If count of negatives is even: include all
        # - If count is odd: exclude the negative with smallest absolute value
        prod = 1
        for x in pos:
            prod *= x

        if len(neg) % 2 == 0:
            for x in neg:
                prod *= x
        else:
            # Need to drop one negative (the one with smallest absolute value)
            neg.sort(key=abs)  # ascending abs; drop smallest abs
            for x in neg[1:]:
                prod *= x

        return prod
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Meet-in-the-middle over sign/zero handling.
        # Let m = 2^(n/2) subsets; compute product for non-empty subsets.
        # Track best positive and best negative (closest to zero) since
        # combining subsets depends on sign.
        n = len(nums)
        mid = n // 2
        A = nums[:mid]
        B = nums[mid:]

        def gen(subarr):
            m = len(subarr)
            out = []
            # Iterate all non-empty subsets
            for mask in range(1, 1 << m):
                prod = 1
                for i in range(m):
                    if mask & (1 << i):
                        prod *= subarr[i]
                out.append(prod)
            return out

        SA = gen(A)
        SB = gen(B)

        # We need max over all non-empty unions:
        # union may be entirely within A, within B, or across both.
        # If we take prodA * prodB, union is non-empty iff:
        # - both non-empty (subset from A and subset from B)
        # We'll compute candidates:
        # 1) max of subsets entirely in A
        # 2) max of subsets entirely in B
        ans = max(max(SA) if SA else -10**18, max(SB) if SB else -10**18)

        # For cross-subsets, we need maximize prodA * prodB.
        # Since nums[i] are small and n<=13, brute cross is feasible:
        # |SA| <= 2^6-1=63, |SB|<=2^7-1=127, product <= ~8000.
        for pa in SA:
            for pb in SB:
                val = pa * pb
                if val > ans:
                    ans = val
        return ans
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
    def maxStrength(self, nums: List[int]) -> int:
        # DP over sign: track best (max value) for positive and negative products.
        # dp_pos = maximum positive product achievable so far
        # dp_neg = maximum negative product achievable so far
        # Also track possibility of having chosen at least one element via None checks.
        dp_pos = None
        dp_neg = None

        for x in nums:
            new_pos, new_neg = dp_pos, dp_neg

            # Option 1: start new group with just x
            if x > 0:
                new_pos = x if new_pos is None else max(new_pos, x)
            elif x < 0:
                new_neg = x if new_neg is None else min(new_neg, x)

            # Option 2: extend existing groups
            if dp_pos is not None:
                # pos * x
                v = dp_pos * x
                if v > 0:
                    new_pos = v if new_pos is None else max(new_pos, v)
                elif v < 0:
                    new_neg = v if new_neg is None else min(new_neg, v)

            if dp_neg is not None:
                # neg * x
                v = dp_neg * x
                if v > 0:
                    new_pos = v if new_pos is None else max(new_pos, v)
                elif v < 0:
                    new_neg = v if new_neg is None else min(new_neg, v)

            dp_pos, dp_neg = new_pos, new_neg

        # We need maximum strength among all non-empty groups.
        # If we have any positive product, that's always >= any negative product.
        if dp_pos is not None:
            return dp_pos
        return dp_neg  # must exist since nums is non-empty
```
```

</details>

<details>
<summary>partial attempt 2</summary>

```text
```python
from typing import List
from math import inf

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Split into non-zero parts and count zeros
        zeros = nums.count(0)
        nz = [x for x in nums if x != 0]

        # If all are zero, best non-empty group is strength 0
        if not nz:
            return 0

        # If no zeros, we must take all elements to maximize absolute product,
        # but sign may flip based on number of negatives.
        # Standard approach with DP over sign/max.
        has_even_neg = False
        # Use DP for maximum product for each sign state.
        # dp_pos: max positive product achievable
        # dp_neg: min (most negative) product achievable (i.e., negative with largest abs)
        dp_pos = -inf
        dp_neg = inf

        for x in nz:
            # When x is negative, sign flips
            if x > 0:
                new_pos = max(dp_pos * x, x, -dp_neg * x if dp_neg != inf else -inf)
                # dp_neg comes from dp_neg * x or starting new negative (not possible with x>0)
                new_neg = dp_neg * x if dp_neg != inf else inf
            else:
                # x < 0
                # positive product can come from dp_neg * x (two negatives)
                new_pos = max(dp_neg * x if dp_neg != inf else -inf, x * 0)  # placeholder
                # starting new group with negative gives negative product, not positive
                # We'll compute properly:
                cand_from_neg = dp_neg * x if dp_neg != inf else -inf
                new_pos = max(dp_pos * x if dp_pos != -inf else -inf, cand_from_neg, -inf)

                # negative product can come from dp_pos * x or starting new group with x
                cand1 = dp_pos * x if dp_pos != -inf else inf
                cand2 = x
                new_neg = min(cand1, cand2) if cand1 != inf else cand2

            # Fix up for placeholder issue in new_pos when dp_pos and dp_neg are infinities
            # We'll recompute with clean transitions:
            if x > 0:
                pos_from_pos = dp_pos * x if dp_pos != -inf else -inf
                pos_from_neg = (-dp_neg) * x if dp_neg != inf else -inf
                new_pos = max(pos_from_pos, x, pos_from_neg)
                new_neg = dp_neg * x if dp_neg != inf else inf
            else:
                neg_from_pos = dp_pos * x if dp_pos != -inf else inf
                # starting new group
                new_neg = min(neg_from_pos, x)
                pos_from_neg = dp_neg * x if dp_neg != inf else -inf
                pos_from_pos = dp_pos * x if dp_pos != -inf else -inf
                new_pos = max(pos_from_neg, pos_from_pos)

            dp_pos, dp_neg = new_pos, new_neg

        # If zeros exist, we can also get strength 0 by choosing any zero alone.
        # Optimal is the maximum strength among positive products; if none, 0 or negative best.
        ans = 0 if zeros > 0 else -inf
        if dp_pos != -inf:
            ans = max(ans, dp_pos)
        elif zeros == 0:
            # No positive product possible; take the least negative (closest to zero)
            # dp_neg is negative product with largest abs; but we want maximum => closest to zero:
            if dp_neg != inf:
                ans = dp_neg  # dp_neg is negative; max among negatives is closest to zero but
                               # our dp_neg tracks the minimum value (most negative) during build,
                               # so we need a different DP. We'll handle via subset logic below.
        # The above DP for negative branch doesn't guarantee "closest to zero" for dp_neg.
        # Use a safer subset approach based on counting negatives:
        # If dp_pos exists, that's optimal; otherwise, we either pick one negative (if no zeros)
        # or 0 (if zeros exist).
        if ans == 0 and dp_pos == -inf:
            return 0

        # Safe fallback: compute by removing minimal absolute value to make product positive,
        # or take maximum negative if zeros==0 and positives impossible.
        neg_count = sum(1 for x in nz if x < 0)
        # product magnitude of all non-zeros
        prod = 1
        for x in nz:
            prod *= x

        if neg_count % 2 == 0:
            # Product of all is positive and maximal in magnitude
            return prod
        else:
            # Must make it non-negative: either drop smallest abs negative to make product positive,
            # or if zeros exist allow 0.
            min_abs_neg = min(abs(x) for x in nz if x < 0)
            if zeros > 0:
                # choosing empty sign? not allowed; but 0 from choosing a zero alone is valid
                # Compare positive product (after dropping) against 0
                pos_prod = prod // (-min_abs_neg)  # prod / negative gives positive; integer division safe
                return max(0, pos_prod)
            else:
                # No zeros: drop smallest abs negative to make positive
                return prod // (-min_abs_neg)
```
```

</details>

<details>
<summary>partial attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Sort by absolute value descending, since we only need max product
        nums.sort(key=lambda x: abs(x), reverse=True)
        n = len(nums)
        
        # dp[parity] = maximum product achievable using some prefix with given parity of negatives
        # parity 0 => product has even number of negative factors (non-negative product)
        # parity 1 => product has odd number of negative factors (negative product)
        # We use Python ints; numbers are small enough, but sign handling matters.
        dp0, dp1 = 1, None  # dp0 starts with empty product=1 (even negatives=0)
        
        for x in nums:
            if x == 0:
                # Optionally, zero could be chosen as a group element; it yields product 0.
                # But since we want maximum, zero is only relevant if all non-zero products are negative.
                # We'll incorporate it by allowing product 0 as a candidate.
                # Because product becomes 0 regardless of sign parity, treat it separately.
                continue
            
            new_dp0, new_dp1 = None, None
            # extend with x
            if dp0 is not None:
                prod = dp0 * x
                if prod >= 0:
                    new_dp0 = prod if new_dp0 is None else max(new_dp0, prod)
                else:
                    new_dp1 = prod if new_dp1 is None else max(new_dp1, prod)
            if dp1 is not None:
                prod = dp1 * x
                if prod >= 0:
                    new_dp0 = prod if new_dp0 is None else max(new_dp0, prod)
                else:
                    new_dp1 = prod if new_dp1 is None else max(new_dp1, prod)
            
            # also start a new group with just x (parity depends on sign)
            if x >= 0:
                new_dp0 = x if new_dp0 is None else max(new_dp0, x)
            else:
                new_dp1 = x if new_dp1 is None else max(new_dp1, x)
            
            dp0, dp1 = new_dp0, new_dp1
        
        # Include possible effect of zeros:
        has_zero = any(x == 0 for x in nums)
        ans = None
        if dp0 is not None:
            ans = dp0
        if has_zero and (ans is None or ans < 0):
            ans = 0
        if ans is None:
            # Only possible if all nums are 0 (but then group product is 0) or something went wrong.
            ans = 0
        
        # dp0 could represent empty product; disallow empty by ensuring group is non-empty.
        # Our dp0 initialization with 1 (empty) gets overwritten by actual picks through updates.
        # If all products were negative and dp0 is 1 from empty, we'd need correction.
        # To robustly fix, compute using classic approach:
        nonzero = [x for x in nums if x != 0]
        if not nonzero:
            return 0
        
        # Classic greedy-by-absolute-value with sign handling:
        nonzero.sort(key=lambda x: abs(x), reverse=True)
        prod = 1
        neg_count = 0
        for x in nonzero:
            prod *= x
            if x < 0:
                neg_count += 1
        
        if neg_count % 2 == 0:
            return prod
        # If odd negatives, remove the one with smallest absolute value to make negatives even
        smallest_abs = min(nonzero, key=lambda x: abs(x))
        return prod // smallest_abs  # exact division since smallest_abs divides prod

```
```

</details>

<details>
<summary>partial attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = [x for x in nums if x > 0]
        neg = sorted([x for x in nums if x < 0])  # most negative first
        npos = len(pos)
        nneg = len(neg)

        # If there are no non-negative/positive numbers:
        if npos == 0:
            # Only negatives (or no elements, but constraints say length>=1)
            # To maximize product with negatives only, we want:
            # - even count => positive product (best)
            # - odd count => best positive product? we can only have odd => negative; max would be closest to 0
            if nneg == 0:
                # all zeros
                return 0
            if nneg % 2 == 0:
                prod = 1
                for x in neg:
                    prod *= x
                return prod
            else:
                # drop the negative with smallest magnitude (largest value, closest to 0)
                # since neg is sorted ascending, remove last
                prod = 1
                for x in neg[:-1]:
                    prod *= x
                return prod

        # Handle zeros: they can be used to avoid having an odd number of negatives
        zeros = sum(1 for x in nums if x == 0)

        # If we have at least one positive, optimal strategy:
        # take all positives, and take as many negatives as possible with even count.
        # If remaining negatives count is odd, drop one negative with smallest absolute value.
        take_neg = nneg
        if take_neg % 2 == 1:
            if zeros == 0:
                # must drop one negative to make even count
                # drop the negative closest to 0 (largest value)
                # neg sorted ascending => remove last
                take_neg -= 1
                prod_neg = 1
                for x in neg[:-1]:
                    prod_neg *= x
                prod_pos = 1
                for x in pos:
                    prod_pos *= x
                return prod_pos * prod_neg
            else:
                # zeros exist: we can drop all negatives if they can't be paired,
                # but since we have positives, better to still drop exactly one negative
                # to keep product as positive (or use zeros only if product would be negative).
                take_neg -= 1
                prod_neg = 1
                for x in neg[:-1]:
                    prod_neg *= x
                prod_pos = 1
                for x in pos:
                    prod_pos *= x
                return prod_pos * prod_neg

        # Even number of negatives: take all
        prod = 1
        for x in pos:
            prod *= x
        for x in neg:
            prod *= x
        return prod
```
```

</details>

<details>
<summary>partial attempt 5</summary>

```text
```python
from typing import List
from functools import lru_cache
import math

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i: int, parity: int) -> int:
            """
            Returns the maximum product from nums[i:] using at least one element,
            where the product's sign parity is:
              parity = 0 -> product is non-negative (0 or +)
              parity = 1 -> product is negative
            """
            if i == n:
                # No elements chosen; invalid state for "at least one element"
                return -math.inf

            # Option 1: skip nums[i]
            best = dp(i + 1, parity)

            x = nums[i]
            # Option 2: take nums[i] and then maybe more
            # Start with just x
            if x >= 0:
                cand = x
                if cand >= 0:
                    best = max(best, cand)
            else:
                # x < 0
                best = max(best, x)

            # Option 3: take x, then take more from dp(i+1, new_parity)
            # If we previously chose a product P from dp(i+1, p2) (with at least one element),
            # total product = x * P.
            for p2 in (0, 1):
                p_val = dp(i + 1, p2)
                if p_val == -math.inf:
                    continue
                total = x * p_val
                new_parity = 0 if total >= 0 else 1
                if new_parity == parity:
                    best = max(best, total)

            return best

        # The answer must be from a non-empty group.
        # Best among non-negative and negative depending on max.
        nonneg = dp(0, 0)
        neg = dp(0, 1)

        # If all products are negative, nonneg may still be -inf; handle.
        return max(nonneg, neg)
```
```

</details>

### Parsed Memory Items

1. Subset DP or Enumeration When Constraints Are Small
Description: If the input size is small enough, prefer DP/bitmask enumeration to avoid brittle casework and sign errors.
<details>
<summary>Content 1</summary>

```text
When n is small, enumerating all non-empty subsets (or meet-in-the-middle) directly evaluates candidates and sidesteps tricky correctness conditions. This is especially valuable for “maximize product with sign constraints” problems where greedy reasoning can fail on edge cases like zeros or all-negative arrays.
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
The successful attempts share a reliable core idea: model the choice as a subset problem where the key global constraint is the sign (especially parity of the number of negative factors), then optimize accordingly. The simplest brute-force (bitmask subset enumeration) succeeds because the input size is tiny and it avoids subtle reasoning errors about sign/zero corner cases. The partially/unsuccessful attempts fail mainly due to (1) brittle sign DP transitions that mix “max positive” with “min negative” semantics inconsistently, (2) incorrect or unsafe handling of the non-empty requirement and empty-product initialization, and/or (3) “greedy/heuristic” logic that seems standard but breaks in corner cases involving zeros and when the best product is non-positive (e.g., deciding whether to keep or drop negatives when zeros exist). Attempts that sorted by absolute value and then tried to divide by a chosen factor also risk invalid transformations if integer division/optimality conditions aren’t guaranteed.
```

</details>

2. Reformulate the Objective via Sign-Parity State
Description: For product-maximization with negative numbers, track sign parity (even/odd count of negatives) as the central invariant.
<details>
<summary>Content 2</summary>

```text
Instead of reasoning about magnitudes with ad hoc rules, maintain DP states corresponding to whether the current product is non-negative or negative. Transitions then follow from multiplying by the next element, which flips parity only when the element is negative; this structure makes correctness checks systematic.
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
The successful attempts share a reliable core idea: model the choice as a subset problem where the key global constraint is the sign (especially parity of the number of negative factors), then optimize accordingly. The simplest brute-force (bitmask subset enumeration) succeeds because the input size is tiny and it avoids subtle reasoning errors about sign/zero corner cases. The partially/unsuccessful attempts fail mainly due to (1) brittle sign DP transitions that mix “max positive” with “min negative” semantics inconsistently, (2) incorrect or unsafe handling of the non-empty requirement and empty-product initialization, and/or (3) “greedy/heuristic” logic that seems standard but breaks in corner cases involving zeros and when the best product is non-positive (e.g., deciding whether to keep or drop negatives when zeros exist). Attempts that sorted by absolute value and then tried to divide by a chosen factor also risk invalid transformations if integer division/optimality conditions aren’t guaranteed.
```

</details>

3. Handle Non-Empty and Impossible States Explicitly
Description: When using DP with product initialization, explicitly prevent the empty subset from contaminating the answer.
<details>
<summary>Content 3</summary>

```text
Many failures come from starting with an “empty product” value that is convenient mathematically but invalid for the problem’s “must choose at least one element” constraint. Use sentinels/impossible states and carefully define what each state represents (e.g., “best product from a non-empty subset”), then ensure the final answer is taken from valid states only.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
The successful attempts share a reliable core idea: model the choice as a subset problem where the key global constraint is the sign (especially parity of the number of negative factors), then optimize accordingly. The simplest brute-force (bitmask subset enumeration) succeeds because the input size is tiny and it avoids subtle reasoning errors about sign/zero corner cases. The partially/unsuccessful attempts fail mainly due to (1) brittle sign DP transitions that mix “max positive” with “min negative” semantics inconsistently, (2) incorrect or unsafe handling of the non-empty requirement and empty-product initialization, and/or (3) “greedy/heuristic” logic that seems standard but breaks in corner cases involving zeros and when the best product is non-positive (e.g., deciding whether to keep or drop negatives when zeros exist). Attempts that sorted by absolute value and then tried to divide by a chosen factor also risk invalid transformations if integer division/optimality conditions aren’t guaranteed.
```

</details>

4. Validate Risky Transformations (e.g., Division, Zero Logic)
Description: Avoid transformations that assume exact divisibility or ignore how zeros affect optimality.
<details>
<summary>Content 4</summary>

```text
Techniques like computing a full product then “removing” an element via division can break if the chosen element isn’t guaranteed to divide cleanly in the intended arithmetic model, or if zeros make the product collapse. Any optimization that relies on such steps should include a verification pass against the original constraints, especially around zero handling and “best can be 0” scenarios.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
The successful attempts share a reliable core idea: model the choice as a subset problem where the key global constraint is the sign (especially parity of the number of negative factors), then optimize accordingly. The simplest brute-force (bitmask subset enumeration) succeeds because the input size is tiny and it avoids subtle reasoning errors about sign/zero corner cases. The partially/unsuccessful attempts fail mainly due to (1) brittle sign DP transitions that mix “max positive” with “min negative” semantics inconsistently, (2) incorrect or unsafe handling of the non-empty requirement and empty-product initialization, and/or (3) “greedy/heuristic” logic that seems standard but breaks in corner cases involving zeros and when the best product is non-positive (e.g., deciding whether to keep or drop negatives when zeros exist). Attempts that sorted by absolute value and then tried to divide by a chosen factor also risk invalid transformations if integer division/optimality conditions aren’t guaranteed.
```

</details>

5. Keep DP Semantics Consistent (Max vs Min)
Description: If you track both positive and negative outcomes, be consistent about whether you store maxima or minima for each sign bucket.
<details>
<summary>Content 5</summary>

```text
Incorrect attempts often mix “best positive” with a “most negative/closest to zero” interpretation without enforcing it in transitions. A robust pattern is: for each parity/sign state, store the true extremum for that state using the same comparison rule (e.g., always maximize the numeric value), and update candidates by multiplying from the corresponding state.
```

</details>

<details>
<summary>Reasoning 5</summary>

```text
The successful attempts share a reliable core idea: model the choice as a subset problem where the key global constraint is the sign (especially parity of the number of negative factors), then optimize accordingly. The simplest brute-force (bitmask subset enumeration) succeeds because the input size is tiny and it avoids subtle reasoning errors about sign/zero corner cases. The partially/unsuccessful attempts fail mainly due to (1) brittle sign DP transitions that mix “max positive” with “min negative” semantics inconsistently, (2) incorrect or unsafe handling of the non-empty requirement and empty-product initialization, and/or (3) “greedy/heuristic” logic that seems standard but breaks in corner cases involving zeros and when the best product is non-positive (e.g., deciding whether to keep or drop negatives when zeros exist). Attempts that sorted by absolute value and then tried to divide by a chosen factor also risk invalid transformations if integer division/optimality conditions aren’t guaranteed.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
The successful attempts share a reliable core idea: model the choice as a subset problem where the key global constraint is the sign (especially parity of the number of negative factors), then optimize accordingly. The simplest brute-force (bitmask subset enumeration) succeeds because the input size is tiny and it avoids subtle reasoning errors about sign/zero corner cases. The partially/unsuccessful attempts fail mainly due to (1) brittle sign DP transitions that mix “max positive” with “min negative” semantics inconsistently, (2) incorrect or unsafe handling of the non-empty requirement and empty-product initialization, and/or (3) “greedy/heuristic” logic that seems standard but breaks in corner cases involving zeros and when the best product is non-positive (e.g., deciding whether to keep or drop negatives when zeros exist). Attempts that sorted by absolute value and then tried to divide by a chosen factor also risk invalid transformations if integer division/optimality conditions aren’t guaranteed.
</reasoning>

<memories>
<memory>
<title>Subset DP or Enumeration When Constraints Are Small</title>
<description>If the input size is small enough, prefer DP/bitmask enumeration to avoid brittle casework and sign errors.</description>
<content>When n is small, enumerating all non-empty subsets (or meet-in-the-middle) directly evaluates candidates and sidesteps tricky correctness conditions. This is especially valuable for “maximize product with sign constraints” problems where greedy reasoning can fail on edge cases like zeros or all-negative arrays.</content>
</memory>

<memory>
<title>Reformulate the Objective via Sign-Parity State</title>
<description>For product-maximization with negative numbers, track sign parity (even/odd count of negatives) as the central invariant.</description>
<content>Instead of reasoning about magnitudes with ad hoc rules, maintain DP states corresponding to whether the current product is non-negative or negative. Transitions then follow from multiplying by the next element, which flips parity only when the element is negative; this structure makes correctness checks systematic.</content>
</memory>

<memory>
<title>Handle Non-Empty and Impossible States Explicitly</title>
<description>When using DP with product initialization, explicitly prevent the empty subset from contaminating the answer.</description>
<content>Many failures come from starting with an “empty product” value that is convenient mathematically but invalid for the problem’s “must choose at least one element” constraint. Use sentinels/impossible states and carefully define what each state represents (e.g., “best product from a non-empty subset”), then ensure the final answer is taken from valid states only.</content>
</memory>

<memory>
<title>Validate Risky Transformations (e.g., Division, Zero Logic)</title>
<description>Avoid transformations that assume exact divisibility or ignore how zeros affect optimality.</description>
<content>Techniques like computing a full product then “removing” an element via division can break if the chosen element isn’t guaranteed to divide cleanly in the intended arithmetic model, or if zeros make the product collapse. Any optimization that relies on such steps should include a verification pass against the original constraints, especially around zero handling and “best can be 0” scenarios.</content>
</memory>

<memory>
<title>Keep DP Semantics Consistent (Max vs Min)</title>
<description>If you track both positive and negative outcomes, be consistent about whether you store maxima or minima for each sign bucket.</description>
<content>Incorrect attempts often mix “best positive” with a “most negative/closest to zero” interpretation without enforcing it in transitions. A robust pattern is: for each parity/sign state, store the true extremum for that state using the same comparison rule (e.g., always maximize the numeric value), and update candidates by multiplying from the corresponding state.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `0.4000`
- Augmented pass@1: `0.1000`
- Improvement: `-0.3000`

### Baseline

### System Prompt

```text
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.
```

### User Prompt

```text
### Question:
You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i_0, i_1, i_2, ... , i_k is defined as nums[i_0] * nums[i_1] * nums[i_2] * ... * nums[i_k​].
Return the maximum strength of a group the teacher can create.
 
Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.

Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.

 
Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Since product can be huge, use only sign-parity reasoning with DP.
        # dp[i][j] not feasible; instead maintain for each parity (negative count mod 2)
        # and for each segment count? Easier: dp over elements with two states:
        # maximum positive product and maximum negative product possible using any non-empty subsequence.
        #
        # Let:
        # best_pos: maximum (largest) positive product achievable
        # best_neg: minimum (most negative) product achievable (i.e., smallest value) or store most negative.
        #
        # Transition with current x:
        # - start new group with x
        # - extend existing best_pos/best_neg groups
        #
        # Use -inf sentinel.
        neg_inf = float("-inf")
        best_pos = neg_inf  # max positive product
        best_neg = neg_inf  # max (closest to zero) negative? We'll store max value among negatives.
        
        for x in nums:
            if x == 0:
                # Product can be 0 by taking [x] alone, but note strength could be negative or positive too.
                # 0 is neither positive nor negative, so we track separately via best_any_max.
                # We'll handle by allowing 0 as a candidate answer at the end.
                pass

            new_best_pos = best_pos
            new_best_neg = best_neg

            # start new group
            if x > 0:
                new_best_pos = max(new_best_pos, x)
            elif x < 0:
                new_best_neg = max(new_best_neg, x)  # among negatives, max (closest to zero)

            # extend existing positive
            if best_pos != neg_inf:
                prod = best_pos * x
                if prod > 0:
                    new_best_pos = max(new_best_pos, prod)
                elif prod < 0:
                    new_best_neg = max(new_best_neg, prod)
                else:
                    # prod == 0 -> handled via zero candidate
                    pass

            # extend existing negative
            if best_neg != neg_inf:
                prod = best_neg * x
                if prod > 0:
                    new_best_pos = max(new_best_pos, prod)
                elif prod < 0:
                    new_best_neg = max(new_best_neg, prod)
                else:
                    pass

            best_pos, best_neg = new_best_pos, new_best_neg

        # Also consider choosing a single zero if present.
        has_zero = any(x == 0 for x in nums)
        ans = neg_inf
        if best_pos != neg_inf:
            ans = max(ans, best_pos)
        if has_zero:
            ans = max(ans, 0)
        # If no positive and no zero, answer is the negative product closest to zero but still maximal.
        if ans == neg_inf:
            # best_neg might be negative, which is maximal among negatives stored as max value.
            ans = best_neg
        return int(ans)
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List
from math import prod

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Split into negatives and non-negatives
        neg = [x for x in nums if x < 0]
        pos = [x for x in nums if x >= 0]

        # If there is no non-negative number (all are negative)
        if not pos:
            # Choose the largest even-sized subset (to make product positive),
            # otherwise choose the largest odd-sized subset (single negative).
            # We can only include in decreasing magnitude? Actually optimal:
            # sort negatives by absolute value ascending/descending and drop the smallest abs if needed.
            neg_sorted = sorted(neg)  # increasing (more negative first)
            if len(neg_sorted) == 1:
                return neg_sorted[0]
            # Want positive product => need even count
            if len(neg_sorted) % 2 == 0:
                return prod(neg_sorted)
            # drop the negative with smallest absolute value => that's the last in increasing sort
            return prod(neg_sorted[:-1])

        # If there is at least one non-negative, we can always make a non-empty group
        # We want a positive product if possible.
        neg.sort()  # increasing (most negative first), abs decreases toward end

        # Determine best set of negatives:
        # - If count of negatives is even: use all negatives.
        # - If count is odd: drop the negative with smallest absolute value (last one).
        if len(neg) % 2 == 0:
            use_neg = neg
        else:
            use_neg = neg[:-1]  # drop smallest abs negative

        # For non-negatives, use all positives (and zero as needed).
        # If use_neg is empty and all non-negatives are zero, best is 0.
        # If use_neg is empty but there are positive numbers, best is product of positives.
        positives = [x for x in pos if x > 0]
        zeros = pos.count(0)

        # If we ended up using no negatives:
        if not use_neg:
            # Product of positives; if none, must choose a non-empty group => choose 0 if exists
            if positives:
                return prod(positives)
            # no positives and no negatives used => must pick a zero
            # (since pos exists, zeros >= 1)
            return 0

        # Otherwise, include all selected negatives and all positives.
        # Zeros won't increase positive product; including zero would make product 0.
        # So zeros are never included if we already have a non-zero product.
        return prod(positives) * prod(use_neg)
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # DP over subsets for maximum absolute product with fixed parity of negatives
        # For each position, we update:
        #   dp_pos: best value (largest) achievable with even number of negatives
        #   dp_neg: best value (largest) achievable with odd number of negatives
        # We do this in terms of actual product values (can be negative), tracking maxima.
        #
        # dp_pos/neg are initialized as None (unachievable).
        dp_pos = None  # even negatives
        dp_neg = None  # odd negatives

        for x in nums:
            new_pos = None
            new_neg = None

            # Start new group with just [x]
            if x >= 0:
                new_pos = x
            else:
                new_neg = x

            # Extend existing groups
            if dp_pos is not None:
                # dp_pos * x keeps parity even if x>=0, flips if x<0
                val = dp_pos * x
                if x >= 0:
                    new_pos = val if new_pos is None else max(new_pos, val)
                else:
                    new_neg = val if new_neg is None else max(new_neg, val)

            if dp_neg is not None:
                # dp_neg has odd negatives parity
                # multiply by x: if x>=0 parity stays odd, else becomes even
                val = dp_neg * x
                if x >= 0:
                    new_neg = val if new_neg is None else max(new_neg, val)
                else:
                    new_pos = val if new_pos is None else max(new_pos, val)

            dp_pos, dp_neg = new_pos, new_neg

        # Maximum strength is the maximum product among any non-empty group
        # If dp_pos exists, candidates include dp_pos (non-negative or negative if x=0 cases)
        # dp_neg can also be maximal if all products are negative.
        ans = dp_pos if dp_pos is not None else float("-inf")
        if dp_neg is not None:
            ans = max(ans, dp_neg)
        return ans
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List
from functools import lru_cache

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Split into positive count parity using DP over sorted absolute values
        # Here we maximize product over a subsequence:
        # - Zeros can always be avoided unless needed; since zeros reduce product to 0,
        #   but max product may still be negative when all products are negative.
        # We handle with full sign-aware DP on counts of negatives picked.
        n = len(nums)

        pos = [x for x in nums if x > 0]
        neg = [-x for x in nums if x < 0]  # store absolute values
        zero_cnt = sum(1 for x in nums if x == 0)

        # We only care about choosing some positives and some negatives.
        # Product magnitude: multiply all chosen abs values.
        # Sign: product is positive if we choose an even number of negatives, negative otherwise.
        # For maximum strength:
        # - If there is at least one positive result (even number of negatives), take maximal magnitude with even negatives.
        # - Else if can't get positive, best is either:
        #    * single negative with maximal magnitude (odd negatives),
        #    * or 0 if allowed (because max could be 0).
        neg.sort()  # increasing abs
        pos.sort()  # increasing

        # Helper: greedy magnitude via abs product is max when we take largest magnitudes.
        # For even-neg product: take all positives plus:
        #   choose the largest even number of negatives (by abs).
        # For odd-neg product: take all positives plus:
        #   choose the largest odd number of negatives (by abs).
        def best_even() -> int | None:
            m = len(neg)
            if m == 0:
                # only positives: if any positive or zeros? group must be non-empty.
                if pos:
                    prod = 1
                    for v in pos:
                        prod *= v
                    return prod
                return None  # no non-empty positive product possible without negatives/zeros
            # choose even count of negatives with maximum product => take largest abs negatives
            # i.e., take all negatives except possibly smallest one to make even.
            count = m
            if count % 2 == 1:
                count -= 1
            if count == 0:
                # then use only positives
                if pos:
                    prod = 1
                    for v in pos:
                        prod *= v
                    return prod
                return None
            chosen = neg[m - count:]  # largest 'count'
            prod = 1
            for v in pos:
                prod *= v
            for v in chosen:
                prod *= v
            return prod

        def best_odd() -> int | None:
            m = len(neg)
            count = m
            if m == 0:
                if pos:
                    # product will be positive, but this corresponds to even case anyway
                    prod = 1
                    for v in pos:
                        prod *= v
                    return prod
                # only zeros -> strength 0 if non-empty
                return 0 if zero_cnt > 0 else None

            # choose odd number of negatives with maximum product:
            # take all negatives except possibly smallest to make odd (i.e., if m is even, drop one smallest)
            if count % 2 == 0:
                count -= 1
            if count <= 0:
                # can't form odd negatives; would mean only positives/zeros handled elsewhere
                return None
            chosen = neg[m - count:]  # largest 'count' (odd)
            prod = 1
            for v in pos:
                prod *= v
            for v in chosen:
                prod *= v
            # product with odd number of negatives is negative in original sign
            # but since we multiply abs values, apply negative sign
            return -prod

        best_pos = best_even()
        if best_pos is not None:
            return best_pos

        best_neg = best_odd()
        # if no valid negative, maybe zeros or single element exists
        # Also consider possibility of selecting just zeros => 0
        if best_neg is None:
            return 0 if zero_cnt > 0 else nums[0]  # fallback; should not happen with constraints

        if best_neg < 0 and zero_cnt > 0:
            # max between negative and 0
            return 0
        return best_neg
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List
from functools import reduce

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # We can form any subset. Choose subset with maximal product.
        # Key observations:
        # - If we want a positive product, we need an even count of negatives.
        # - If we want a negative product, it can be worse than any available positive/zero,
        #   except when all products are negative and we must pick at least one element.
        #
        # Use DP over prefix with two states:
        # dp_pos = maximum positive product achievable
        # dp_neg = minimum (most negative) product achievable (i.e., minimum value)
        # But product magnitudes can grow quickly; constraints are tiny (n<=13),
        # so Python int is safe.
        INF = 10**30  # used only for initialization; products are far smaller than this bound here

        dp_pos = None  # best positive product
        dp_neg = None  # best negative product (most negative / smallest)

        for x in nums:
            new_pos = dp_pos
            new_neg = dp_neg

            # Start new subset with just x
            if x > 0:
                new_pos = x if new_pos is None else max(new_pos, x)
            elif x < 0:
                new_neg = x if new_neg is None else min(new_neg, x)
            else:  # x == 0
                # product 0 is neither pos nor neg; we handle it implicitly by
                # returning 0 if no positive product exists.
                # But 0 can be achieved; we track via separate flag.
                pass

            # Extend existing subsets
            if x > 0:
                # positive * positive -> positive
                if dp_pos is not None:
                    cand = dp_pos * x
                    new_pos = cand if new_pos is None else max(new_pos, cand)
                # positive * negative -> negative
                if dp_neg is not None:
                    cand = dp_neg * x
                    new_neg = cand if new_neg is None else min(new_neg, cand)

            elif x < 0:
                # negative * negative -> positive
                if dp_neg is not None:
                    cand = dp_neg * x
                    new_pos = cand if new_pos is None else max(new_pos, cand)
                # negative * positive -> negative
                if dp_pos is not None:
                    cand = dp_pos * x
                    new_neg = cand if new_neg is None else min(new_neg, cand)

            else:  # x == 0
                # any product that includes 0 becomes 0; could be best if no positive exists
                # doesn't affect dp_pos/dp_neg because 0 is neither.
                pass

            dp_pos, dp_neg = new_pos, new_neg

        # Determine presence of zero in input: if no positive product exists, answer could be 0.
        has_zero = 0 in nums

        if dp_pos is not None:
            return dp_pos
        # No positive achievable. Then best is:
        # - 0 if available
        # - otherwise, the maximum (least negative) product from dp_neg
        if has_zero:
            return 0
        # dp_neg must exist because nums non-empty
        return dp_neg
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        # Split into zeros and non-zeros
        positives = []
        negatives = []
        has_zero = False
        for x in nums:
            if x == 0:
                has_zero = True
            elif x > 0:
                positives.append(x)
            else:
                negatives.append(x)

        # If there are no non-zero numbers, only zeros exist
        if not positives and not negatives:
            return 0

        # Count negative numbers and take all positives always
        # If #negatives is even: take all non-zero numbers
        # If #negatives is odd: drop the negative with smallest absolute value
        neg_cnt = len(negatives)
        # Sort negatives by absolute value to drop the smallest-abs negative when needed
        negatives_sorted = sorted(negatives, key=lambda v: abs(v))

        ans = 1
        # multiply all positives
        for p in positives:
            ans *= p

        if neg_cnt % 2 == 0:
            # take all negatives
            for v in negatives_sorted:
                ans *= v
        else:
            # drop one negative with smallest absolute value
            # multiply remaining negatives
            for v in negatives_sorted[1:]:
                ans *= v
            # If after dropping we multiplied none of the negatives,
            # ans would still be 1, but there must be at least one non-zero.
            # However, positives could be empty too; the strength for empty group
            # isn't allowed, but this situation can't happen because neg_cnt is odd >=1
            # and dropping 1 leaves at least 0 negatives; if left 0 negatives and no positives,
            # then the group would be empty, but that would mean only one non-zero existed (a single negative),
            # and best would be 0 by taking group {0} is allowed only if there is a zero.
            # If no zero exists, then we must take that single negative.
            if ans == 1 and not positives:
                # means we dropped the only negative; must choose it if no zeros
                if has_zero:
                    return 0
                else:
                    return negatives_sorted[0]

        return ans
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Max strength using meet-in-the-middle, tracking products and whether we need
        # to select an even/odd count of negatives.
        #
        # Key idea:
        # - Best product will be either maximal absolute product, adjusted by parity of negatives.
        # - We can choose any non-empty subsequence.
        #
        # Standard approach for this problem:
        # Sort positives and negatives by absolute value? Not correct due to sign/parity.
        #
        # We'll use DP on sign and best products:
        # dp_even = max product using subset with even number of negatives (product> =0)
        # dp_odd  = max product using subset with odd number of negatives (product<0)
        # We want maximum final strength (could be positive or negative),
        # but since non-empty, answer is max among achievable products.
        #
        # However products can explode in magnitude; Python ints handle it.
        #
        # dp initialization: empty subset is allowed internally.
        INF_NEG = -10**30
        dp_even = 1   # empty subset: product 1, even negatives count
        dp_odd = -10**60  # impossible state for empty subset (odd negatives)
        for x in nums:
            # new states from taking x or not taking x
            if x >= 0:
                new_even = max(dp_even, dp_even * x)  # take x keeps parity
                new_odd = max(dp_odd, dp_odd * x)    # impossible times x remains impossible
            else:
                # taking x flips parity
                # even -> odd, odd -> even
                new_even = max(dp_even, dp_odd * x)   # dp_odd is negative large if impossible
                new_odd = max(dp_odd, dp_even * x)
            dp_even, dp_odd = new_even, new_odd

        # We must exclude the empty subset.
        # If dp_even is from empty subset only, ensure non-empty:
        # We'll compute the best non-empty result directly via parity DP variant:
        #
        # Let's do a safer re-run with DP over non-empty by initializing with None.
        dp_even = None  # best product with even negatives, non-empty
        dp_odd = None   # best product with odd negatives, non-empty

        for x in nums:
            if dp_even is None and dp_odd is None:
                # first element only
                dp_even = x if x >= 0 else None
                dp_odd = x if x < 0 else None
                continue

            candidates_even = []
            candidates_odd = []

            # start new subset with x
            if x >= 0:
                candidates_even.append(x)
            else:
                candidates_odd.append(x)

            # extend existing subsets
            if dp_even is not None:
                # keep parity if x>=0 else flip
                if x >= 0:
                    candidates_even.append(dp_even * x)
                else:
                    candidates_odd.append(dp_even * x)
            if dp_odd is not None:
                if x >= 0:
                    candidates_odd.append(dp_odd * x)
                else:
                    candidates_even.append(dp_odd * x)

            dp_even = max(candidates_even) if candidates_even else None
            dp_odd = max(candidates_odd) if candidates_odd else None

        ans = dp_even if dp_even is not None else -10**60
        if dp_odd is not None:
            # dp_odd product is negative, but if it's the only achievable non-empty,
            # it could be the maximum (e.g., all negatives and odd length constraint).
            ans = max(ans, dp_odd)
        return ans
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List
from itertools import combinations

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = None

        # Split by sign to reduce search space:
        # Maximum product will use all positive numbers, and either:
        # - all non-zero numbers except possibly removing one odd-parity negative,
        #   or
        # - a subset formed by negatives when no positives exist.
        #
        # Since nums[i] are small and n<=13, use DP over count of negatives parity
        # by processing non-zero values; but simplest robust approach:
        # treat zero as neutral only when everything else is negative/zero.
        
        pos = [x for x in nums if x > 0]
        neg = sorted([x for x in nums if x < 0])  # most negative first
        zeros = sum(1 for x in nums if x == 0)

        if not pos and not neg:
            # all zeros => choose one student => product 0
            return 0

        # If there are no positives:
        if not pos:
            # We can only use negatives in pairs (product positive),
            # or a single negative if we must (but we'd rather use pairs for max).
            # Best is:
            # - if number of negatives is even => product of all negatives
            # - else if zeros exist => can drop one negative and use remaining even count
            #   (or take 0 which is smaller than any positive pair product)
            # - else => must take product of all negatives (odd count => negative)
            if len(neg) % 2 == 0:
                prod = 1
                for x in neg:
                    prod *= x
                return prod
            else:
                if zeros > 0:
                    # drop the negative with smallest absolute value by removing the closest to 0
                    # since neg sorted ascending: closest to 0 is last element
                    prod = 1
                    for x in neg[:-1]:
                        prod *= x
                    return prod
                else:
                    prod = 1
                    for x in neg:
                        prod *= x
                    return prod

        # General case: have positives.
        # Using all positives is always beneficial (product increases for positive factors),
        # but we must handle negatives to maximize the sign and magnitude.
        prod = 1
        for x in pos:
            prod *= x

        if len(neg) % 2 == 0:
            for x in neg:
                prod *= x
            return prod
        else:
            if zeros > 0:
                # remove one negative (the one with smallest absolute value) to make negative count even
                # neg sorted ascending: smallest abs is the last element (closest to 0)
                for x in neg[:-1]:
                    prod *= x
                return prod
            else:
                # must keep odd number of negatives => product is negative.
                # To maximize (i.e., least negative), remove negative with largest absolute value
                # (so remaining product is negative but closest to 0 in magnitude).
                prod_neg_removed = 1
                # remove first (most negative magnitude) which is at index 0 due to ascending order
                for x in neg[1:]:
                    prod_neg_removed *= x
                return prod * prod_neg_removed

        # (Unreachable)
        # return ans
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        neg = sum(1 for x in nums if x < 0)
        total_prod = 1
        for x in nums:
            total_prod *= x

        # If there are no negative numbers, or no zeros, we can use all numbers.
        # Zeros just reduce products; but we only need maximal product.
        # This problem is best solved by DP over max/min products with parity of negatives.
        # However, constraints are tiny (n<=13), so a clean DP works.

        n = len(nums)
        # dp_max[i][j]: maximum product using first i numbers with j negatives chosen (parity handled via j mod 2)
        # We only need parity to decide sign, but magnitudes need max; we keep two states:
        # best positive (or zero) and best negative.
        best_pos = None  # maximum positive/zero product for a non-empty subset
        best_neg = None  # minimum (most negative) or maximum magnitude negative? For maximizing, keep the largest negative by value (closest to zero) and use it carefully.
        # We'll track:
        # best_pos: maximum product >0 (or 0)
        # best_neg: minimum product <0 (most negative) is not needed; we need best_neg for maximizing when multiplying by negatives.
        # We'll actually track maximum product for each sign:
        # - best_neg: maximum (i.e., closest to zero) negative product.
        best_neg = None

        for x in nums:
            # Start new subset with just x
            new_pos = None
            new_neg = None

            # include x alone
            if x >= 0:
                new_pos = x if new_pos is None else max(new_pos, x)
            else:
                new_neg = x if new_neg is None else max(new_neg, x)  # x is negative; max keeps closest to zero

            # extend existing subsets
            if best_pos is not None:
                prod = best_pos * x
                if prod >= 0:
                    new_pos = prod if new_pos is None else max(new_pos, prod)
                else:
                    new_neg = prod if new_neg is None else max(new_neg, prod)
            if best_neg is not None:
                prod = best_neg * x
                if prod >= 0:
                    new_pos = prod if new_pos is None else max(new_pos, prod)
                else:
                    new_neg = prod if new_neg is None else max(new_neg, prod)

            best_pos, best_neg = new_pos, new_neg

        # If best_pos exists, it's the answer; otherwise best_neg is negative but maximal among non-empty subsets.
        return best_pos if best_pos is not None else best_neg
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Meet-in-the-middle over subsets.
        # Split into two halves, enumerate all subset products and parity (neg/pos).
        n = len(nums)
        mid = n // 2
        left, right = nums[:mid], nums[mid:]

        def enum_subsets(arr: List[int]):
            res = []  # list of (product, neg_count_parity)
            m = len(arr)
            # iterate over all non-empty subsets
            for mask in range(1, 1 << m):
                prod = 1
                neg_parity = 0  # parity of negative numbers in subset
                # compute product and parity
                for i in range(m):
                    if mask & (1 << i):
                        x = arr[i]
                        prod *= x
                        if x < 0:
                            neg_parity ^= 1
                res.append((prod, neg_parity))
            return res

        A = enum_subsets(left)
        B = enum_subsets(right)

        # We want to maximize product of products; parity matters only for sign.
        # Maximum value:
        # - If we can make positive product, maximize positive.
        # - Otherwise, maximum (least negative) negative product.
        # We'll compute maximum positive and maximum negative.
        max_pos = -10**30
        max_neg = -10**30

        # Sort products of right by sign to help find best matches:
        # For maximizing product:
        # If we want overall positive => products from right must have same sign as left product.
        # If overall negative => different signs.
        Apos = [p for (p, parity) in A if p > 0]
        Aneg = [p for (p, parity) in A if p < 0]
        Bpos = [p for (p, parity) in B if p > 0]
        Bneg = [p for (p, parity) in B if p < 0]

        # also include possibility where subset is only on one side (already included via A/B non-empty)
        for p in Apos + Aneg:
            if p > 0:
                max_pos = max(max_pos, p)
            else:
                max_neg = max(max_neg, p)
        for p in Bpos + Bneg:
            if p > 0:
                max_pos = max(max_pos, p)
            else:
                max_neg = max(max_neg, p)

        # Combine:
        # Positive result: (positive * positive) or (negative * negative)
        if Apos and Bpos:
            for pa in Apos:
                # best is with largest pb
                max_pos = max(max_pos, pa * max(Bpos))
        if Aneg and Bneg:
            for pa in Aneg:
                # pa is negative; to maximize positive pa*pb, pb should be most negative (min)
                max_pos = max(max_pos, pa * min(Bneg))

        # Negative result: (positive * negative) or (negative * positive)
        # We want the maximum (closest to zero) negative value.
        if Apos and Bneg:
            for pa in Apos:
                # pa*pb with pb negative is negative; maximize => pb with largest value (closest to zero)
                max_neg = max(max_neg, pa * max(Bneg))
        if Aneg and Bpos:
            for pa in Aneg:
                # pa negative; pb positive. maximize => choose smallest pb? actually negative*positive:
                # e.g., (-3)*1=-3, (-3)*5=-15, so closer to zero uses smallest positive.
                max_neg = max(max_neg, pa * min(Bpos))

        return max_pos if max_pos != -10**30 else max_neg
```
```

</details>

#### Baseline Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.8571 | `partial` |
| 1 | 1.0000 | `full` |
| 2 | 0.7143 | `partial` |
| 3 | 1.0000 | `full` |
| 4 | 1.0000 | `full` |
| 5 | 1.0000 | `full` |
| 6 | 0.7143 | `partial` |
| 7 | 0.7143 | `partial` |
| 8 | 0.7143 | `partial` |
| 9 | 0.8571 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 12,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "81",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
  "passed": 10,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "450",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
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
      "expected": "576",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "6",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
  "passed": 10,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "450",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
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
      "expected": "576",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "6",
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
  "passed": 10,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "150",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "20",
      "actual": "-80",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "1",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "-185177664",
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
  "passed": 10,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "450",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
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
      "expected": "576",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "6",
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
  "passed": 12,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "8",
      "actual": "8",
      "error": ""
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "-1000000000000000000000000000000",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": false,
      "expected": "0",
      "actual": "-5",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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

  1. Subset DP or Enumeration When Constraints Are Small: If the input size is small enough, prefer DP/bitmask enumeration to avoid brittle casework and sign errors.
     When n is small, enumerating all non-empty subsets (or meet-in-the-middle) directly evaluates candidates and sidesteps tricky correctness conditions. This is especially valuable for “maximize product with sign constraints” problems where greedy reasoning can fail on edge cases like zeros or all-negative arrays.
  2. Reformulate the Objective via Sign-Parity State: For product-maximization with negative numbers, track sign parity (even/odd count of negatives) as the central invariant.
     Instead of reasoning about magnitudes with ad hoc rules, maintain DP states corresponding to whether the current product is non-negative or negative. Transitions then follow from multiplying by the next element, which flips parity only when the element is negative; this structure makes correctness checks systematic.
  3. Handle Non-Empty and Impossible States Explicitly: When using DP with product initialization, explicitly prevent the empty subset from contaminating the answer.
     Many failures come from starting with an “empty product” value that is convenient mathematically but invalid for the problem’s “must choose at least one element” constraint. Use sentinels/impossible states and carefully define what each state represents (e.g., “best product from a non-empty subset”), then ensure the final answer is taken from valid states only.
  4. Validate Risky Transformations (e.g., Division, Zero Logic): Avoid transformations that assume exact divisibility or ignore how zeros affect optimality.
     Techniques like computing a full product then “removing” an element via division can break if the chosen element isn’t guaranteed to divide cleanly in the intended arithmetic model, or if zeros make the product collapse. Any optimization that relies on such steps should include a verification pass against the original constraints, especially around zero handling and “best can be 0” scenarios.
  5. Keep DP Semantics Consistent (Max vs Min): If you track both positive and negative outcomes, be consistent about whether you store maxima or minima for each sign bucket.
     Incorrect attempts often mix “best positive” with a “most negative/closest to zero” interpretation without enforcing it in transitions. A robust pattern is: for each parity/sign state, store the true extremum for that state using the same comparison rule (e.g., always maximize the numeric value), and update candidates by multiplying from the corresponding state.

Apply these insights to the problem below.

### Question:
You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i_0, i_1, i_2, ... , i_k is defined as nums[i_0] * nums[i_1] * nums[i_2] * ... * nums[i_k​].
Return the maximum strength of a group the teacher can create.
 
Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.

Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.

 
Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
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
    def maxStrength(self, nums: List[int]) -> int:
        # Subset enumeration with pruning-free DP over sign parity.
        # dp_pos: maximum product of a non-empty subset with non-negative product (>=0)
        # dp_neg: maximum product of a non-empty subset with negative product (<0)
        # Use None to represent impossible.
        dp_pos, dp_neg = None, None

        for x in nums:
            # start a new subset with just x
            new_pos, new_neg = None, None
            if x >= 0:
                new_pos = x
            else:
                new_neg = x

            # extend existing subsets
            if dp_pos is not None:
                p = dp_pos * x
                if p >= 0:
                    new_pos = p if new_pos is None else max(new_pos, p)
                else:
                    new_neg = p if new_neg is None else max(new_neg, p)

            if dp_neg is not None:
                p = dp_neg * x
                if p >= 0:
                    new_pos = p if new_pos is None else max(new_pos, p)
                else:
                    new_neg = p if new_neg is None else max(new_neg, p)

            dp_pos, dp_neg = new_pos, new_neg

        # Answer must come from a valid non-empty subset state.
        # Prefer dp_pos if exists because it's >=0 and thus >= any negative.
        if dp_pos is not None:
            return dp_pos
        return dp_neg
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        # dp_pos: best (maximum numeric) product of a non-empty subset with even number of negatives
        # dp_neg: best (maximum numeric) product of a non-empty subset with odd number of negatives
        # "maximum numeric" works even for negative values because we still want the largest value overall.
        NEG_INF = -10**100
        dp_pos = NEG_INF
        dp_neg = NEG_INF

        for x in nums:
            # Start/choose subset consisting only of x
            if x >= 0:
                new_pos = x  # even negatives count (0)
                new_neg = NEG_INF
            else:
                new_pos = NEG_INF
                new_neg = x  # odd negatives count (1)

            # Extend previous subsets
            # If current product has even negatives (dp_pos), multiplying by x:
            # - keeps parity if x>=0
            # - flips parity if x<0
            if dp_pos != NEG_INF:
                if x >= 0:
                    new_pos = max(new_pos, dp_pos * x)
                else:
                    new_neg = max(new_neg, dp_pos * x)

            if dp_neg != NEG_INF:
                if x >= 0:
                    new_neg = max(new_neg, dp_neg * x)
                else:
                    new_pos = max(new_pos, dp_neg * x)

            dp_pos, dp_neg = new_pos, new_neg

        return max(dp_pos, dp_neg)
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Subset DP over sign parity:
        # dp_even = maximum product of a non-empty subset with even number of negatives
        # dp_odd  = maximum product of a non-empty subset with odd number of negatives
        neg_inf = -10**100
        dp_even, dp_odd = neg_inf, neg_inf

        for x in nums:
            new_even, new_odd = dp_even, dp_odd

            # Start a new non-empty subset with just [x]
            if x >= 0:
                new_even = max(new_even, x)
            else:
                new_odd = max(new_odd, x)

            # Extend existing subsets
            if dp_even != neg_inf:
                prod = dp_even * x
                # parity flips if x is negative
                if x < 0:
                    new_odd = max(new_odd, prod)
                else:
                    new_even = max(new_even, prod)

            if dp_odd != neg_inf:
                prod = dp_odd * x
                if x < 0:
                    new_even = max(new_even, prod)
                else:
                    new_odd = max(new_odd, prod)

            dp_even, dp_odd = new_even, new_odd

        return max(dp_even, dp_odd)
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Product-maximization with possible negatives and zeros.
        # Since n <= 13, subset DP is simple and safe.
        n = len(nums)
        NEG_INF = None  # sentinel for "impossible"

        # dp[parity] = best product achievable with a non-empty subset
        # parity = 0 -> non-negative product, parity = 1 -> negative product
        dp = [NEG_INF, NEG_INF]

        for x in nums:
            new_dp = dp[:]
            # Start a new subset with just x
            if x >= 0:
                new_dp[0] = x if new_dp[0] is None else max(new_dp[0], x)
            else:
                new_dp[1] = x if new_dp[1] is None else max(new_dp[1], x)

            # Extend existing subsets
            for parity in (0, 1):
                if dp[parity] is None:
                    continue
                prod = dp[parity] * x
                new_parity = parity ^ (1 if x < 0 else 0)  # multiply by negative flips sign
                # maximize numeric value (works for both positive and negative states)
                if new_dp[new_parity] is None:
                    new_dp[new_parity] = prod
                else:
                    new_dp[new_parity] = max(new_dp[new_parity], prod)

            dp = new_dp

        # Must choose non-empty subset; dp already enforces that.
        # Answer is the maximum over achievable products (positive/non-negative vs negative).
        return max(v for v in dp if v is not None)
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        # dp_pos: best (maximum) product of a non-empty subset whose product is >=0
        # dp_neg: best (maximum) product of a non-empty subset whose product is < 0
        # Use None to represent "impossible" (no subset with that sign yet).
        dp_pos = None
        dp_neg = None

        for x in nums:
            # Candidate subsets that start with just [x]
            new_pos = dp_pos
            new_neg = dp_neg

            if x >= 0:
                new_pos = x if new_pos is None else max(new_pos, x)
            else:
                new_neg = x if new_neg is None else max(new_neg, x)

            # Extend all existing subsets
            if dp_pos is not None:
                prod = dp_pos * x
                if prod >= 0:
                    new_pos = prod if new_pos is None else max(new_pos, prod)
                else:
                    new_neg = prod if new_neg is None else max(new_neg, prod)

            if dp_neg is not None:
                prod = dp_neg * x
                if prod >= 0:
                    new_pos = prod if new_pos is None else max(new_pos, prod)
                else:
                    new_neg = prod if new_neg is None else max(new_neg, prod)

            dp_pos, dp_neg = new_pos, new_neg

        # Answer must be from a valid non-empty subset
        return dp_pos if dp_pos is not None else dp_neg
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        NEG_INF = -10**30  # safely below any possible product magnitude

        # dp_even: max product of a non-empty subset with even number of negatives
        # dp_odd : max product of a non-empty subset with odd number of negatives
        dp_even = NEG_INF
        dp_odd = NEG_INF

        for x in nums:
            if x == 0:
                # subset consisting of [0] gives product 0, and 0 times anything stays 0
                # For parity, we can reach 0 in both even/odd states.
                # The maximum product for both states becomes at least 0.
                dp_even = max(dp_even, 0)
                dp_odd = max(dp_odd, 0)
                continue

            # new states created by either starting with [x] or extending existing subsets
            # Starting with [x] sets parity based on sign of x.
            new_even = dp_even
            new_odd = dp_odd

            if x > 0:
                # x keeps parity
                # start subset
                new_even = max(new_even, x)
                # extend: even*pos -> even, odd*pos -> odd
                if dp_even != NEG_INF:
                    new_even = max(new_even, dp_even * x)
                if dp_odd != NEG_INF:
                    new_odd = max(new_odd, dp_odd * x)
            else:
                # x flips parity
                # start subset
                new_odd = max(new_odd, x)
                # extend: even*neg -> odd, odd*neg -> even
                if dp_even != NEG_INF:
                    new_odd = max(new_odd, dp_even * x)
                if dp_odd != NEG_INF:
                    new_even = max(new_even, dp_odd * x)

            dp_even, dp_odd = new_even, new_odd

        # Best strength can be even-parity product (>=0) or odd-parity product (could be negative),
        # but we want the maximum numeric value among all non-empty subsets.
        return max(dp_even, dp_odd)
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        neg = sum(1 for x in nums if x < 0)

        # If n is small, subset enumeration is simplest and robust.
        # (n <= 13 per constraints)
        best = None
        for mask in range(1, 1 << n):  # non-empty subsets only
            prod = 1
            for i in range(n):
                if mask & (1 << i):
                    prod *= nums[i]
            if best is None or prod > best:
                best = prod
        return best
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Subset DP over non-empty subsets using sign-parity state:
        # dp[0] = maximum product of a non-empty subset with even number of negatives (product >= 0)
        # dp[1] = maximum product of a non-empty subset with odd number of negatives (product <= 0)
        # For odd parity, the maximum will be the "least negative" or possibly 0.
        NEG_INF = -10**100

        dp_even = NEG_INF
        dp_odd = NEG_INF

        for x in nums:
            # Update using snapshots of previous dp
            prev_even, prev_odd = dp_even, dp_odd

            # Consider subset consisting of only x
            if x >= 0:
                new_even = max(prev_even, x)
                new_odd = prev_odd
            else:
                new_even = prev_even
                new_odd = max(prev_odd, x)

            # Extend previous subsets
            if prev_even != NEG_INF:
                prod = prev_even * x
                if prod >= 0:
                    new_even = max(new_even, prod)
                else:
                    new_odd = max(new_odd, prod)

            if prev_odd != NEG_INF:
                prod = prev_odd * x
                if prod >= 0:
                    new_even = max(new_even, prod)
                else:
                    new_odd = max(new_odd, prod)

            dp_even, dp_odd = new_even, new_odd

        return max(dp_even, dp_odd)
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        # dp_even: best (maximum value) product using a non-empty subset with even number of negatives
        # dp_odd : best (maximum value) product using a non-empty subset with odd number of negatives
        NEG_INF = -10**100
        dp_even = NEG_INF
        dp_odd = NEG_INF

        for x in nums:
            new_even, new_odd = dp_even, dp_odd

            # Start a new subset with just [x] (non-empty)
            if x >= 0:
                new_even = max(new_even, x)  # even negatives: 0
            else:
                new_odd = max(new_odd, x)   # odd negatives: 1

            # Extend existing subsets
            if dp_even != NEG_INF:
                prod = dp_even * x
                if x >= 0:
                    new_even = max(new_even, prod)
                else:
                    new_odd = max(new_odd, prod)
            if dp_odd != NEG_INF:
                prod = dp_odd * x
                if x >= 0:
                    new_odd = max(new_odd, prod)
                else:
                    new_even = max(new_even, prod)

            dp_even, dp_odd = new_even, new_odd

        return max(dp_even, dp_odd)
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        # dp_even: best (maximum) product achievable with a non-empty subset having even # of negatives
        # dp_odd:  best (maximum) product achievable with a non-empty subset having odd  # of negatives
        # "best" means numerical maximum (could be negative or zero if no positive exists).
        neg_inf = None
        dp_even = neg_inf
        dp_odd = neg_inf

        for x in nums:
            new_even = dp_even
            new_odd = dp_odd

            # Start a new non-empty subset with just x
            if x >= 0:
                new_even = x if new_even is None else max(new_even, x)
            else:
                new_odd = x if new_odd is None else max(new_odd, x)

            # Extend existing subsets
            if dp_even is not None:
                p = dp_even * x
                if x >= 0:
                    new_even = p if new_even is None else max(new_even, p)
                else:
                    new_odd = p if new_odd is None else max(new_odd, p)

            if dp_odd is not None:
                p = dp_odd * x
                if x >= 0:
                    new_odd = p if new_odd is None else max(new_odd, p)
                else:
                    new_even = p if new_even is None else max(new_even, p)

            dp_even, dp_odd = new_even, new_odd

        # Answer must come from a non-empty subset => dp_even or dp_odd are valid
        # If dp_even is None (shouldn't happen since non-empty subset exists), fall back to dp_odd.
        if dp_even is None:
            return dp_odd
        if dp_odd is None:
            return dp_even
        return max(dp_even, dp_odd)
```
```

</details>

#### Augmented Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.7143 | `partial` |
| 1 | 0.7143 | `partial` |
| 2 | 0.7857 | `partial` |
| 3 | 0.7857 | `partial` |
| 4 | 0.8571 | `partial` |
| 5 | 0.7857 | `partial` |
| 6 | 1.0000 | `full` |
| 7 | 0.8571 | `partial` |
| 8 | 0.7857 | `partial` |
| 9 | 0.7857 | `partial` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "passed": 10,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "450",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
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
      "expected": "576",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "6",
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
  "passed": 10,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "450",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
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
      "expected": "576",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "6",
      "error": "Wrong Answer"
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
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "81",
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
  "passed": 11,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "81",
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
  "passed": 12,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "81",
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
  "passed": 11,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "81",
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
  "passed": 14,
  "total": 14,
  "cases": [
    {
      "passed": true,
      "expected": "1350",
      "actual": "1350",
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
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": true,
      "expected": "185177664",
      "actual": "185177664",
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
  "passed": 12,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": true,
      "expected": "81",
      "actual": "81",
      "error": ""
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "81",
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
  "passed": 11,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "81",
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
  "passed": 11,
  "total": 14,
  "cases": [
    {
      "passed": false,
      "expected": "1350",
      "actual": "50",
      "error": "Wrong Answer"
    },
    {
      "passed": true,
      "expected": "20",
      "actual": "20",
      "error": ""
    },
    {
      "passed": true,
      "expected": "9",
      "actual": "9",
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
      "expected": "7",
      "actual": "7",
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
      "expected": "-5",
      "actual": "-5",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "576",
      "actual": "576",
      "error": ""
    },
    {
      "passed": true,
      "expected": "27216",
      "actual": "27216",
      "error": ""
    },
    {
      "passed": false,
      "expected": "81",
      "actual": "9",
      "error": "Wrong Answer"
    },
    {
      "passed": false,
      "expected": "185177664",
      "actual": "81",
      "error": "Wrong Answer"
    }
  ]
}
```

</details>
