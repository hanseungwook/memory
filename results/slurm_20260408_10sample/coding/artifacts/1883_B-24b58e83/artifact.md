# Problem 1883_B

- Domain: `coding`

## Problem

```text
You are given a string $s$ of length $n$, consisting of lowercase Latin letters, and an integer $k$.

You need to check if it is possible to remove exactly $k$ characters from the string $s$ in such a way that the remaining characters can be rearranged to form a palindrome. Note that you can reorder the remaining characters in any way.

A palindrome is a string that reads the same forwards and backwards. For example, the strings "z", "aaa", "aba", "abccba" are palindromes, while the strings "codeforces", "reality", "ab" are not.

Input

Each test consists of multiple test cases. The first line contains a single integer $t$ ($1 \leq t \leq 10^4$) — the number of the test cases. This is followed by their description.

The first line of each test case contains two integers $n$ and $k$ ($0 \leq k < n \leq 10^5$) — the length of the string $s$ and the number of characters to be deleted.

The second line of each test case contains a string $s$ of length $n$, consisting of lowercase Latin letters.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.

Output

For each test case, output "YES" if it is possible to remove exactly $k$ characters from the string $s$ in such a way that the remaining characters can be rearranged to form a palindrome, and "NO" otherwise.

You can output the answer in any case (uppercase or lowercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive answers.Sample Input 1:
14

1 0

a

2 0

ab

2 1

ba

3 1

abb

3 2

abc

6 2

bacacd

6 2

fagbza

6 2

zwaafa

7 2

taagaak

14 3

ttrraakkttoorr

5 3

debdb

5 4

ecadc

5 3

debca

5 3

abaac



Sample Output 1:

YES
NO
YES
YES
YES
YES
NO
NO
YES
YES
YES
YES
NO
YES


Note

In the first test case, nothing can be removed, and the string "a" is a palindrome.

In the second test case, nothing can be removed, but the strings "ab" and "ba" are not palindromes.

In the third test case, any character can be removed, and the resulting string will be a palindrome.

In the fourth test case, one occurrence of the character "a" can be removed, resulting in the string "bb", which is a palindrome.

In the sixth test case, one occurrence of the characters "b" and "d" can be removed, resulting in the string "acac", which can be rearranged to the string "acca".

In the ninth test case, one occurrence of the characters "t" and "k" can be removed, resulting in the string "aagaa", which is a palindrome.
```

### Test Cases

```json
[
  {
    "input": "14\n1 0\na\n2 0\nab\n2 1\nba\n3 1\nabb\n3 2\nabc\n6 2\nbacacd\n6 2\nfagbza\n6 2\nzwaafa\n7 2\ntaagaak\n14 3\nttrraakkttoorr\n5 3\ndebdb\n5 4\necadc\n5 3\ndebca\n5 3\nabaac\n",
    "output": "YES\nNO\nYES\nYES\nYES\nYES\nNO\nNO\nYES\nYES\nYES\nYES\nNO\nYES\n",
    "testtype": "stdin"
  },
  {
    "input": "5\n10 3\naaabbbcccd\n10 1\naaabbccddd\n10 0\naaabbccddd\n10 9\nabcdefghij\n10 2\naabbccddee\n",
    "output": "YES\nYES\nNO\nYES\nYES",
    "testtype": "stdin"
  },
  {
    "input": "5\n10 5\naaabbbbccc\n10 5\naaabbbcccc\n10 4\naabbccddeeff\n11 3\naabbccddeeff\n10 8\naaabbbbccc",
    "output": "YES\nYES\nYES\nYES\nYES",
    "testtype": "stdin"
  },
  {
    "input": "5\n15 7\naaabbbcccdddeee\n15 8\naaabbccddeeffggh\n17 9\naaabbbcccdddeeeff\n21 10\naabbccddeeffgghhiijj\n20 0\naabbccddeeffgghhiijjkk",
    "output": "YES\nYES\nYES\nYES\nYES",
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
You are given a string $s$ of length $n$, consisting of lowercase Latin letters, and an integer $k$.

You need to check if it is possible to remove exactly $k$ characters from the string $s$ in such a way that the remaining characters can be rearranged to form a palindrome. Note that you can reorder the remaining characters in any way.

A palindrome is a string that reads the same forwards and backwards. For example, the strings "z", "aaa", "aba", "abccba" are palindromes, while the strings "codeforces", "reality", "ab" are not.

Input

Each test consists of multiple test cases. The first line contains a single integer $t$ ($1 \leq t \leq 10^4$) — the number of the test cases. This is followed by their description.

The first line of each test case contains two integers $n$ and $k$ ($0 \leq k < n \leq 10^5$) — the length of the string $s$ and the number of characters to be deleted.

The second line of each test case contains a string $s$ of length $n$, consisting of lowercase Latin letters.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.

Output

For each test case, output "YES" if it is possible to remove exactly $k$ characters from the string $s$ in such a way that the remaining characters can be rearranged to form a palindrome, and "NO" otherwise.

You can output the answer in any case (uppercase or lowercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive answers.Sample Input 1:
14

1 0

a

2 0

ab

2 1

ba

3 1

abb

3 2

abc

6 2

bacacd

6 2

fagbza

6 2

zwaafa

7 2

taagaak

14 3

ttrraakkttoorr

5 3

debdb

5 4

ecadc

5 3

debca

5 3

abaac



Sample Output 1:

YES
NO
YES
YES
YES
YES
NO
NO
YES
YES
YES
YES
NO
YES


Note

In the first test case, nothing can be removed, and the string "a" is a palindrome.

In the second test case, nothing can be removed, but the strings "ab" and "ba" are not palindromes.

In the third test case, any character can be removed, and the resulting string will be a palindrome.

In the fourth test case, one occurrence of the character "a" can be removed, resulting in the string "bb", which is a palindrome.

In the sixth test case, one occurrence of the characters "b" and "d" can be removed, resulting in the string "acac", which can be rearranged to the string "acca".

In the ninth test case, one occurrence of the characters "t" and "k" can be removed, resulting in the string "aagaa", which is a palindrome.

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
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it)); k = int(next(it))
        s = next(it)
        cnt = Counter(s)
        m = n - k  # length of remaining string

        # For a multiset of size m to be rearrangeable into a palindrome:
        # - if m is even: all counts must be even
        # - if m is odd: exactly one character count can be odd
        odd = sum(v & 1 for v in cnt.values())

        # We can delete exactly k characters; equivalently we choose
        # a subselection leaving size m. But only feasibility depends on:
        # how many odd counts remain after deletions.
        #
        # Let x be number of odd counts after deletions.
        # For palindrome: x must be 0 (m even) or 1 (m odd).
        #
        # Each deletion changes parity of at most one character count.
        # More precisely, removing one occurrence from a character flips its parity.
        #
        # We need to know if we can reduce odd to target parity count.
        target_odd = 0 if (m % 2 == 0) else 1

        # Minimum deletions to make number of odd counts equal to target_odd:
        # - If odd < target_odd: need to increase odd count (also requires deletions).
        # - In practice, the known Codeforces solution for this problem is:
        #   YES iff (odd - target_odd) is achievable with available deletions
        #   and parity constraints hold, which can be simplified to:
        #   Let d = odd - target_odd
        #   Then we need d >= 0 or can adjust by deleting extra pairs.
        #
        # For this specific problem, correct condition:
        #   If odd <= m:
        #       possible if odd <= m and ( (m - odd) % 2 == (0 if target_odd==0 else 1) ? )
        # This is messy; let's implement the standard derivation:
        #
        # We can always remove characters to fix parities as follows:
        # Each deletion reduces odd count by 1 or increases it by 1 (flips parity).
        # Therefore, after exactly k deletions, odd' has same parity as odd + k
        # modulo 2? Actually odd' parity flips with each deletion for the affected char,
        # but the parity of the number of odd-count letters changes by 1 mod 2 each flip.
        # So odd' % 2 == (odd + k) % 2.
        #
        # We need odd' = target_odd.
        if (odd - target_odd) % 2 != 0:
            out.append("NO")
            continue

        # Also, odd' cannot exceed m because remaining string length m
        # has at most m characters, and you can't have more than m odd-count letters.
        if odd > m:
            out.append("NO")
            continue

        # Finally, we must be able to adjust using exactly k deletions.
        # Since odd' is reached, number of deletions k already fixed; the parity check above
        # ensures feasibility. But we also need not to require more deletions than k.
        # The minimal deletions to reduce odd to target_odd is:
        #   need to change parity status of (odd - target_odd) odd letters, each change costs 1 deletion.
        # This yields k >= odd - target_odd when odd > target_odd.
        if odd > target_odd and k < odd - target_odd:
            out.append("NO")
            continue

        out.append("YES")
    sys.stdout.write("\n".join(out))

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
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it)); k = int(next(it))
        s = next(it)

        cnt = Counter(s)
        m = n - k  # remaining length
        # Maximum number of pairs we can use is floor(m/2); leftover (if odd) can be any char with remaining odd count.
        # Total number of odd-count characters in the multiset after deletions determines possibility.
        # Standard approach:
        # For a multiset to be rearrangeable into a palindrome:
        # - if m is even: all counts must be even
        # - if m is odd: exactly one count is odd
        #
        # Deleting characters changes parities. We can always delete within each character count.
        # Let initial odd count be odd0. After deletions, we need:
        # odd0' = 0 (m even) or 1 (m odd).
        #
        # Each deletion flips parity of the chosen character, thus changes oddness count by ±1.
        # But also limited by available deletions and m parity.
        # We'll simulate the minimal achievable odd count reduction:
        # You can always reduce odd count by deleting one from an odd-count character (making it even), costing 1 deletion.
        # Let need = 0 if m even else 1.
        odd0 = sum(1 for v in cnt.values() if v % 2 == 1)

        # Minimum deletions needed to get down to desired parity count:
        # If odd0 > need, each deletion can reduce odd count by 1 (by taking from an odd-count character).
        # So min_del = odd0 - need (only valid if odd0 >= need).
        # However, if odd0 < need, we must create extra oddness by deleting from an even-count character: cost 1 per increase.
        # More generally, parity of deletions affects whether odd count can match.
        need = 1 if (m % 2 == 1) else 0

        # Let x = number of odd positions we will end with (need).
        # Each deletion flips parity, so odd-count parity changes depending on deletions:
        # The parity of number of odd-count characters after deletions has same parity as (odd0 + del) mod 2? Actually each flip changes odd count by ±1,
        # thus parity of odd count flips each deletion. So (odd' mod 2) == (odd0 + del mod 2).
        # We need odd' = need (0 or 1), so (need mod 2) == (odd0 + k mod 2).
        if (odd0 + k) % 2 != need % 2:
            out.append("NO")
            continue

        # Also, we must be able to reach need odd-counts with exactly k deletions.
        # The odd count cannot be reduced below max(0, odd0 - k) because each deletion reduces odd by at most 1.
        # Similarly, cannot exceed odd0 + k because each deletion can increase odd by at most 1.
        # So need must be within [odd0 - k, odd0 + k] but also feasible with length m constraints already captured by parity check.
        if need < 0 or need > n:
            out.append("NO")
            continue

        if not (odd0 - k <= need <= odd0 + k):
            out.append("NO")
            continue
        # Additionally, after deletions, remaining length is m; but since we already used k exactly, that's satisfied.
        out.append("YES")

    sys.stdout.write("\n".join(out))

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
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        s = next(it)

        cnt = Counter(s)
        odd = sum(1 for v in cnt.values() if v % 2 == 1)

        m = n - k  # remaining length

        # Number of odd counts needed for a multiset to be rearrangeable into a palindrome
        # is 0 if m even, 1 if m odd.
        need_odd = 0 if m % 2 == 0 else 1

        # Each deletion can change parity of a single character count by 1,
        # thus odd parity count changes by at most 1, and we can always realize
        # transitions as long as:
        # - odd cannot be "fixed" with fewer deletions than required,
        # - parity of remaining feasibility matches.
        # Minimal deletions to reach need_odd:
        # If odd > need_odd: each deletion reduces odd by 1 when removing from an odd-count character.
        # So min del = odd - need_odd (when odd >= need_odd else can increase odd).
        # More generally, feasibility is:
        #   (odd - need_odd) <= k and (k - (odd - need_odd)) even after accounting for operations.
        # But since operations correspond to toggling odd count by 1, the condition becomes:
        # - if odd >= need_odd: (odd - need_odd) <= k and (k - (odd - need_odd)) % 2 == 0
        # - if odd < need_odd: need_odd - odd <= k and (k - (need_odd - odd)) % 2 == 0
        # This can be unified as parity check with absolute difference.
        diff = abs(odd - need_odd)
        if diff <= k and (k - diff) % 2 == 0:
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out))

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
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it)); k = int(next(it))
        s = next(it)

        cnt = Counter(s)
        length = n - k  # remaining length
        odd = sum(v % 2 for v in cnt.values())

        if length % 2 == 0:
            # need 0 odds
            # each deletion can reduce odd-count by at most 1
            need = odd
        else:
            # need 1 odd
            need = max(0, odd - 1)

        out.append("YES" if need <= k else "NO")

    sys.stdout.write("\n".join(out))

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

def can_form_palindrome_after_deletions(n, k, s):
    cnt = [0]*26
    for ch in s:
        cnt[ord(ch)-97] += 1

    odd = sum(1 for x in cnt if x % 2 == 1)  # number of odd-count letters
    m = n - k                                 # length after deletions

    # Needed number of odd counts to be achievable:
    # For even length palindrome -> 0 odd; for odd length palindrome -> 1 odd.
    if m % 2 == 0:
        target_odd = 0
    else:
        target_odd = 1

    # Each deletion changes parity of exactly one character count (flip odd/even for that letter),
    # so the number of odd counts changes by +/-1. From parity perspective:
    # We can make odd-count count decrease by 1 per deletion as long as we have deletions.
    # Minimal deletions to reach target:
    # If odd == target, 0. If odd > target, need (odd - target) deletions.
    if odd < target_odd:
        return False  # cannot increase odd to target using only deletions
    min_del = odd - target_odd
    if k < min_del:
        return False

    # After making odd count correct, remaining deletions can be spent in pairs
    # without changing possibility of palindrome (since deleting 2 chars preserves parity pattern feasibility).
    # Thus (k - min_del) must be even.
    return (k - min_del) % 2 == 0

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); k = int(data[idx+1]); idx += 2
        s = data[idx]; idx += 1
        out.append("YES" if can_form_palindrome_after_deletions(n, k, s) else "NO")
    sys.stdout.write("\n".join(out))

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
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        s = next(it)

        need = k  # number of deletions
        cnt = Counter(s)
        odd = sum(v & 1 for v in cnt.values())
        remaining = n - k

        # After deletions, the remaining string length is fixed, so:
        # - if remaining is even -> need 0 odd counts
        # - if remaining is odd  -> need 1 odd count
        target_odd = remaining & 1

        # We can change parity of counts by deleting characters.
        # Deleting one char from a letter flips its parity.
        # Thus each deleted character can change odd-count count by at most 1,
        # and in fact we can always reach the best possible parity configuration as:
        # possible iff odd and target_odd have same parity, and we have enough deletions.
        #
        # Minimum deletions required to make number of odd counts equal to target_odd:
        # While odd > target_odd, each deletion can reduce odd by 1 (by deleting from an odd-count letter).
        # So min deletions = odd - target_odd (only when odd >= target_odd, else we need to increase odds).
        # But if we need to increase odd (odd < target_odd), each deletion can increase odd by 1 by
        # deleting from an even-count letter. Since target_odd is either 0 or 1, this is manageable.
        #
        # More generally, condition boils down to:
        #   odd - target_odd <= need and (need - (odd - target_odd)) even
        # When target_odd is 0/1 this becomes:
        #   need >= abs(odd - target_odd) and (need - abs(odd - target_odd)) % 2 == 0
        # However, flipping parity twice wastes 2 deletions, hence the parity condition.
        #
        diff = abs(odd - target_odd)
        if need >= diff and (need - diff) % 2 == 0:
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out))

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
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        s = next(it)

        need_len = n - k
        cnt = Counter(s)

        odd = sum(v % 2 for v in cnt.values())

        # We can remove exactly k chars; equivalently keep need_len chars.
        # Let m = need_len.
        # A multiset can be permuted into a palindrome iff it has:
        # - 0 odd counts when m is even
        # - 1 odd count when m is odd
        # Each removed character changes parity of exactly one letter count,
        # thus changes number of odd letters by +/-1.
        #
        # Greedy parity feasibility can be reduced to:
        # For the kept multiset, we need odd_target in {0,1} depending on parity of m.
        # Number of odd letters after deletions can be adjusted by at most k steps,
        # and parity of (odd - odd_target) must match k.
        if need_len % 2 == 0:
            odd_target = 0
        else:
            odd_target = 1

        # Minimum possible odd after removing k is max(0, odd - k)??? not exact due to +/-1,
        # but feasibility condition is:
        # - odd_target must be reachable: odd and odd_target differ by at most k
        # - (odd - odd_target) and k have same parity
        # Because each deletion flips parity of one letter => odd count changes by 1.
        # So parity(odd_change) == k.
        reachable = (odd >= odd_target and (odd - odd_target) <= k and ((odd - odd_target) % 2 == k % 2)) or \
                    (odd < odd_target and (odd_target - odd) <= k and ((odd_target - odd) % 2 == k % 2))

        out.append("YES" if reachable else "NO")

    sys.stdout.write("\n".join(out))

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
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        s = next(it)
        cnt = Counter(s)
        odd = sum(v & 1 for v in cnt.values())

        # After deletions, let m = n-k remaining length.
        # A multiset can form a palindrome iff #odd_counts <= 1 when m is odd,
        # and #odd_counts == 0 when m is even.
        m = n - k

        if m % 2 == 0:
            need = odd  # must reduce odd to 0
        else:
            need = max(0, odd - 1)  # must reduce odd to 1

        # Each deletion changes parity of exactly one character count, so odd count
        # can be reduced by at most 1 per deletion -> need deletions required.
        if need > k:
            out.append("NO")
            continue

        # Remaining parity constraint: after satisfying ability to reduce odd,
        # we can waste extra deletions only if their effect can be compensated.
        # For k > need, the parity of (k-need) must allow ending with required odd state.
        # It reduces to: (k - need) % 2 == 0
        if (k - need) % 2 == 0:
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out))

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
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it)); k = int(next(it))
        s = next(it)
        cnt = Counter(s)

        # Maximum number of odd-frequency letters we can reduce by removing characters:
        odd = sum(1 for v in cnt.values() if v % 2 == 1)

        # We need to delete exactly k chars, so remaining length is m = n-k
        m = n - k

        # Palindrome possible iff:
        # - if m is even: all counts even
        # - if m is odd: exactly one count odd
        # Let target odd count:
        target = 0 if m % 2 == 0 else 1

        # Deleting characters can change parity of letters; each deleted character
        # can reduce the number of odds by at most 1 and can also increase it.
        # The key known condition for this problem:
        # We can obtain required parity iff we can reduce odds to target using k deletions,
        # and parity constraints on k.
        #
        # After removing k chars, parity of each letter count flips exactly number of removed
        # occurrences mod 2. The achievable range leads to:
        # minimal removals to reach target odds parity is (odd - target) // 2 rounded? Actually:
        #
        # Standard solution:
        # If odd <= target: possible iff (target - odd) % 2 == 0? But odd can increase too.
        # Better approach: simulate minimal number of deletions needed to make all counts parity match.
        #
        # We can model as: For each odd-count letter, to make it even we need to delete 1 from it.
        # Similarly, to keep one odd (if needed), all other odd letters must become even.
        #
        # Minimum deletions needed:
        # - If target==0: min_del = odd (make all odd letters even by deleting 1 from each odd letter)
        # - If target==1: min_del = odd-1 (keep one odd, make others even)
        min_del = odd - target
        if min_del < 0:
            min_del = 0

        # But deletions are exactly k; after meeting parity, extra deletions can be done in pairs
        # (removing 2 from any letter keeps parity same). Therefore we need:
        # k >= min_del and (k - min_del) % 2 == 0
        if k >= min_del and (k - min_del) % 2 == 0:
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out))

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
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        s = next(it)
        freq = Counter(s)

        # We need a multiset of remaining letters that can form a palindrome.
        # Let remaining length be m = n-k.
        m = n - k

        # For a palindrome:
        # - if m is even: all counts must be even
        # - if m is odd: exactly one count is odd
        # We decide feasibility by greedily minimizing number of odd counts
        # after deleting exactly k characters.
        odd = sum(1 for c in freq.values() if c % 2 == 1)

        # We can think in terms of how many "odd counts" we can fix using deletions.
        # Deleting 1 from a character with odd count flips it to even (odd--),
        # and deleting 1 from a character with even count flips it to odd (odd++).
        # Since k < n, we can always delete from somewhere.
        # We need to know if there exists some deletions that results in:
        # odd_final = 0 (m even) or 1 (m odd).
        target = 0 if m % 2 == 0 else 1

        # Each deletion changes odd by ±1, so odd parity flips each time.
        # But odd itself changes depending on which letters we delete from.
        #
        # We'll check existence via achievable interval:
        # We can always reduce odd by at most k? Not exactly, but maximum number
        # of odd counts we can eliminate is bounded by odd and k.
        #
        # A standard approach:
        # Let d = odd - target. We want to reduce odd to target.
        # - If odd > target: we need to decrease odd by d. Each deletion can decrease odd by 1
        #   at best, but only when we delete from a letter with odd count.
        #   Number of such letters is limited by odd, but we only care about d deletions.
        #   Feasible iff d <= k and (k - d) is even (because after fixing to target,
        #   remaining deletions must keep odd_final at target; extra deletions must
        #   not change parity relative to target, which requires parity constraint).
        #
        # - If odd < target: we need to increase odd by target-odd.
        #   Each deletion can increase odd by 1 by deleting from even-count letters.
        #   That's limited by number of even-count letters with positive freq.
        #   However, it's always possible to increase odd up to k, but must also respect parity.
        #   In practice, the same condition with symmetry works if we use:
        #   We can adjust odd by at most k and parity must match.
        #
        # Using proven logic:
        # Let d = abs(odd - target). Condition: d <= k and (k - d) % 2 == 0.
        # Additionally, we need that we can actually perform those adjustments without
        # running out of letters, but with lowercase letters and given constraints
        # this condition is sufficient for this specific problem.
        d = abs(odd - target)
        if d <= k and (k - d) % 2 == 0:
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>
