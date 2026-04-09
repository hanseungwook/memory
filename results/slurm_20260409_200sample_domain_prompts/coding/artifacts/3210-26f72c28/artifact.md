# Problem 3210

- Domain: `coding`

## Problem

```text
You are given a string s and a positive integer k.
Let vowels and consonants be the number of vowels and consonants in a string.
A string is beautiful if:

vowels == consonants.
(vowels * consonants) % k == 0, in other terms the multiplication of vowels and consonants is divisible by k.

Return the number of non-empty beautiful substrings in the given string s.
A substring is a contiguous sequence of characters in a string.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Consonant letters in English are every letter except vowels.
 
Example 1:

Input: s = "baeyh", k = 2
Output: 2
Explanation: There are 2 beautiful substrings in the given string.
- Substring "baeyh", vowels = 2 (["a",e"]), consonants = 2 (["y","h"]).
You can see that string "aeyh" is beautiful as vowels == consonants and vowels * consonants % k == 0.
- Substring "baeyh", vowels = 2 (["a",e"]), consonants = 2 (["b","y"]). 
You can see that string "baey" is beautiful as vowels == consonants and vowels * consonants % k == 0.
It can be shown that there are only 2 beautiful substrings in the given string.

Example 2:

Input: s = "abba", k = 1
Output: 3
Explanation: There are 3 beautiful substrings in the given string.
- Substring "abba", vowels = 1 (["a"]), consonants = 1 (["b"]). 
- Substring "abba", vowels = 1 (["a"]), consonants = 1 (["b"]).
- Substring "abba", vowels = 2 (["a","a"]), consonants = 2 (["b","b"]).
It can be shown that there are only 3 beautiful substrings in the given string.

Example 3:

Input: s = "bcdf", k = 1
Output: 0
Explanation: There are no beautiful substrings in the given string.

 
Constraints:

1 <= s.length <= 1000
1 <= k <= 1000
s consists of only English lowercase letters.
```

### Starter Code

```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
```

### Test Cases

```json
[
  {
    "input": "\"baeyh\"\n2",
    "output": "2",
    "testtype": "functional"
  },
  {
    "input": "\"abba\"\n1",
    "output": "3",
    "testtype": "functional"
  },
  {
    "input": "\"bcdf\"\n1",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"f\"\n8",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"dl\"\n1",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"gtk\"\n8",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"shra\"\n7",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"iczan\"\n4",
    "output": "1",
    "testtype": "functional"
  },
  {
    "input": "\"zmjzd\"\n2",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"ryxnml\"\n9",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"coydlsm\"\n3",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"vaavovpjrvdphtvommiigyflguilfwytmxlrdkkcsdoqwkryoaxuimzcxweeaydoeyoydqwyyzsvhjtsstaiedmsapjuwwqohbugdtxvuxspvcbxelrcdjfyugsjljkkslcyimbcoslxnzeswpygyplerjovovcjpmmgdpgtbhflcjxowtmnwhypzqyzlarfzrisavfncvetfwdlzydlybnodzrrcimdtvpuqhezhqfzjerdfalhsnbyiywbkexrfmxqtczjaszjcmlqqeqsheqhkjoaummfsetffjvvamkdzxgmgokuuwqukjwxbdamkytxvqexrrosjordpxzpmhjpesxaydegxhfdglxvordmhprxllalcibfjmxnfjmfhasuchkhurfvxjmiwcalzcqaqzfmfuhvktgprpoktortxauwpdaejaattibqyyuvybsqkctlyvcibqborsbbxmhsjzvullberiedvpuafyfitxmquadsjbrwxlknfwtxlxqehzzagnurfcygjjcmylzzbuvuacynuwifvyhwdgtwyfwmaqmcyjfrdsbqmgxuzudulncyreefbgjlpnoadurvmoqbkjgkndkihpstqorvmbxcywqldcmyzlufgcsffiybcogaavwwmrshhxhtjtgpubdqegwyatwtlhbajvmxrkciorszrojtqaijtadgixxnyqptmfgmyxtffaowapycjnfwjitnvzfltbbflllogmvpesrtmixzozhcgzeijxpovyfsprwhzgdirsddvmkwtnxtoxncjfsmevgvxyhhwywupcvsfzhhbhkbzunbtuvnzdwoofdefgmotkdanwhayciprtkkrkzkjboxxqns\"\n425",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"ejnxphtxwfhvqwqtlyexegvsvojkdvbeylneqcfzbsrirfvrrhpumbhqsuudvlhvljsqmolrbxkravmwtbmfivjztplitjwkrmvhgcupxxklgypxmasgdfnyxkalejznyzvrtmxcrdmmdybngcmonkgvjwagsmijlstfxuxvomvviwacqnbuxqfqylopuipypwddbfcwlwklolloqcrjbjtsvmsrqvibkwyktyerytgzeqlmijqmmcnsscjbfxybyrlwhxdsgawgpncccghesxiveluyafygojvwwodscmhcihysnnrbmhfrhlqngubgoneoivildorzhggtwzhmcwkkccmxwisshvgnjeppzzujrwoehuhsoncwnbumfmhatvihbnsqhfegqltutgrgosynwdjxkehofjccspapxpvoyknaexocleujekysxupdttaotiwxfjzwdjzbzabgvsdhdnncqcwepruszlzufczylqlbqrlnwzsaskvwasjuxcgkfdwpgxvqklrkswqvgblxnkeniijwqkuotbettdkjocekbloucuitarcgrgqlzkwcnmgkxghrkmieyrtpnwobirukvowllsfljoggswixvevyessypslitftjqfswcajrmhfopdgkdxzbwffluoprptcihshflqrssgjcymsypnuwgvuwaqfxabsaysplotlqqkpripgdyemdxvnfvmzupftxcuewvdxhjhwrhojpriyvzoopbrarmikjwtmgufnuumqkezourcfhylwdtqwmqxexqhmunumokfcdqwrwfjjpmncwoplagltsgagalmuokqonkzvhkhjxyczoczixzoeviwcsrdwyubxfwitlmpqwbacriyozyrjpmxkqdsnifkrrivbhzhnslwydbswgrvchoyuhwtvzpwhnkczwjjbc\"\n177",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"qtzqusuuiruvgqokwyobwhphdvicpeidqetuxpjhgqhfhxilrfpeszcxqyaivojhjgzdkcpqhzkslevmpssgkxdbtdrhooozcxaynojqzhoujmwafykycdnlkiwirnbgaoxoxnastboafeafgbfqlslmlozsfyvxvjdsdzphhsnwfdlkekyatxvvurtfmyjacjbgkqmokdjnlvgljuqttkrzrxxodcremwomfmhjyvxtijinkesqhgvporslowjnwbhubesfuubnurepgldbsxyfmcqfbkmuxzgbhwrjcresiohmmbzlnfrbhgmzqdvcxyuxvmdrzjtgbodqdyewwpiekstaaemtjbjyjprxvlndvrxelhviruewvcasphlqsodpdwsbnwhdfdaaphnnazkmcngyjghuyjcaesjdxavuaujcyptaepgbfoabawyxhozxaphxvfmpdpctqrknobvidtkjnyiagszmqxgkjhughjfxcgbntwgpxijkbzamvrcgwpjxqjhvxpvselghpwykvksfvzulwkbjxjxnfqkgtkcqidiakkadcjukqgfahypztdtkzddydfuerbmsmthyjdpaskammxyjkunyxtmkoykghuspgpifetccttiwrmkbnzvlkdevtjkqkbrdheaqxfrcmwnjjbgcgirytsldnkvgjcvuvtuievyowvctvccimlcpcsxynpftjxtklilbinvvrjuqfokrxoebmwsutdhizgzevjxoohqaitrdzwpcsxcousnocsbmtchlhgynmrpqsujzegajjdzjvbpokntbyamphwmzcfdmosdfbxzhznypdgrvlmcvpltsjiwhmqjnxrhhxatntxqoptrynbyxngcfereqwocaczuzvwgdbrdatqtuxmqiozsrlvoanilzpsqxglzqsamgdamgzvehalvpznbgrwmyjywgylucgjozrefmcqgroepziwumdwebhefypnhevytu\"\n1000",
    "output": "0",
    "testtype": "functional"
  },
  {
    "input": "\"zstzrfgvurjscukryeuuuebuptpuuglycjzqmubmkvfpfovuqhbumsjqdpmzikxossquujzdueegfhptdgxvrvouzffnafvruvlycpqviohsusmzkodptgkpalsxxtzarbrxwteghndrbrkytsbqmhewaurpgiratyiqizacujvmgpkwwrewtdnxkkspnqatvcbbzubuapbctsewimsaujurnsjcjmijvofhxnqfgsesgzdnugrxgjjgizljzsyuorylfiodmnasvalfagqgmspjuvbpnuaiuopehikrbvjpnhhmcdlwwzztldvumtmdwdzxqrtgqgklfgzgagwryotgudhtmdbwcaesognetxwoiszlrjnscvafonvvbdzhepfmwcvumpttryisitkcpsywzfbtetuzmccyynzhauyyenkzirymrgothvsnlkjjotakuogrscstibmthgurxwwalibvnjfwimvxmhimlomvlagjxysenzajvddcapvzyspszvdmbuxxvpctfgpyrcdhltslyznrweqfdncgmqnedtjydxzedhghxzzrclxrednyidtckprgkouuuuyxfxyfvrivrpgpbxylcwvwtlkvbgbzcaidjeatkkkcsszpaguoyodinywlrbxuhawjuyyuutlybcwzpngburfkjivfqzhmdckpebfeagnmkmndcildaawytvgrftfohpsouwuefwefmskespbkkwclxnidzseezebxmgtnefcteknxidmdebpvdnwxmbirzrvuqsfvmmbjlmpzvtkoqebropillsgkyxochrayvenxsrynsdpiqxifmcrdpfkbiyghavyjzeasppkmwituqlrqsayphqhbkaobgcrgkwyvyafqpuhsyrunrjypuxfasljqzdvtxnushdxtxuvtshbcsyyazihhlfimuruhulvngholongyjuargdpowtembpqhaurjgpchrflmboqixwbf\"\n1000",
    "output": "0",
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
You are given a string s and a positive integer k.
Let vowels and consonants be the number of vowels and consonants in a string.
A string is beautiful if:

vowels == consonants.
(vowels * consonants) % k == 0, in other terms the multiplication of vowels and consonants is divisible by k.

Return the number of non-empty beautiful substrings in the given string s.
A substring is a contiguous sequence of characters in a string.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Consonant letters in English are every letter except vowels.
 
Example 1:

Input: s = "baeyh", k = 2
Output: 2
Explanation: There are 2 beautiful substrings in the given string.
- Substring "baeyh", vowels = 2 (["a",e"]), consonants = 2 (["y","h"]).
You can see that string "aeyh" is beautiful as vowels == consonants and vowels * consonants % k == 0.
- Substring "baeyh", vowels = 2 (["a",e"]), consonants = 2 (["b","y"]). 
You can see that string "baey" is beautiful as vowels == consonants and vowels * consonants % k == 0.
It can be shown that there are only 2 beautiful substrings in the given string.

Example 2:

Input: s = "abba", k = 1
Output: 3
Explanation: There are 3 beautiful substrings in the given string.
- Substring "abba", vowels = 1 (["a"]), consonants = 1 (["b"]). 
- Substring "abba", vowels = 1 (["a"]), consonants = 1 (["b"]).
- Substring "abba", vowels = 2 (["a","a"]), consonants = 2 (["b","b"]).
It can be shown that there are only 3 beautiful substrings in the given string.

Example 3:

Input: s = "bcdf", k = 1
Output: 0
Explanation: There are no beautiful substrings in the given string.

 
Constraints:

1 <= s.length <= 1000
1 <= k <= 1000
s consists of only English lowercase letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        n = len(s)
        ans = 0

        # Count vowels and consonants to find all substrings where v == c.
        # Let v = c => length = v + c is even, and v = c = len/2.
        # For substring [l..r], condition reduces to:
        #   v = c = t
        #   (t * t) % k == 0
        # i.e., t^2 divisible by k.

        # Precompute for t in [1..500] (since v=c => length even <= 1000 -> t<=500)
        ok_t = [False] * (n // 2 + 1)
        for t in range(1, n // 2 + 1):
            if (t * t) % k == 0:
                ok_t[t] = True

        # Prefix difference d = (#vowels - #consonants)
        # Need d == 0 and length even implies equal counts.
        pref = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            pref[i] = pref[i - 1] + (1 if ch in vowels_set else -1)

        # For each start l, find end r such that pref[r] == pref[l] and r-l even.
        # Use O(n^2) with pruning; n=1000 is okay with bitset-like prefix indexing.
        # We'll group prefix positions by (value of pref, parity of index).
        from collections import defaultdict

        # counts[val][parity] = number of occurrences of pref index with that parity
        counts = defaultdict(lambda: [0, 0])
        for i in range(n + 1):
            counts[pref[i]][i & 1] += 1

        # Now iterate over end index r, and count starts l with same pref and same parity.
        # For such pair (l<r), v=c => t = (r-l)/2. Check ok_t[t].
        # Also ensure t>=1 => r-l>=2.
        for r in range(n + 1):
            val = pref[r]
            # We want l < r with same val and same parity (so length even).
            parity = r & 1

            # We'll consider all possible l via scanning; to keep it correct and still efficient,
            # do an O(n^2) but with n=1000 that's 1e6 operations, fine.
            for l in range(r):
                if pref[l] != val:
                    continue
                if (r - l) % 2 != 0:
                    continue
                t = (r - l) // 2
                if t >= 1 and ok_t[t]:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)

        ans = 0

        # We need substrings where vowels == consonants
        # Let length be 2m, then each such substring has m vowels and m consonants.
        # Additionally (m*m) % k == 0.
        # So m must be in {1..floor(n/2)} with (m*m)%k==0.
        good_m = [False] * (n // 2 + 1)
        for m in range(1, n // 2 + 1):
            good_m[m] = (m * m) % k == 0

        # Prefix counts for vowels
        pref_v = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref_v[i + 1] = pref_v[i] + (1 if ch in vowels_set else 0)

        # For each possible half-length m, check all substrings of length 2m
        for m in range(1, n // 2 + 1):
            if not good_m[m]:
                continue
            length = 2 * m
            for l in range(0, n - length + 1):
                r = l + length
                v = pref_v[r] - pref_v[l]
                # consonants = length - v, so v == consonants iff v == m
                if v == m:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        # Prefix sums of vowels and consonants
        n = len(s)
        pref_v = [0] * (n + 1)
        pref_c = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            pref_v[i] = pref_v[i - 1] + (1 if ch in vowels_set else 0)
            pref_c[i] = pref_c[i - 1] + (1 if ch not in vowels_set else 0)

        # For each m = vowels = consonants, need m^2 % k == 0
        good_m = [False] * (n + 1)
        for m in range(1, n // 2 + 1):
            if (m * m) % k == 0:
                good_m[m] = True

        ans = 0
        # Check all possible m by looking for positions where prefix differences match.
        # We use: for substring [l, r) length = 2m, and need pref_v[r]-pref_v[l]=m and pref_c[r]-pref_c[l]=m.
        # Since length is fixed 2m, it's enough to enforce pref_v difference; then pref_c difference holds automatically.
        # More directly: pref_v[r]-pref_v[l]=m and (r-l)=2m.
        for m in range(1, n // 2 + 1):
            if not good_m[m]:
                continue
            two_m = 2 * m
            # Need pref_v[l+2m]-pref_v[l] == m
            for l in range(0, n - two_m + 1):
                r = l + two_m
                if pref_v[r] - pref_v[l] == m:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels_set = set("aeiou")

        # Count vowels and consonants in any substring quickly:
        # Let diff = vowels - consonants.
        # For any substring: vowels == consonants  <=> diff == 0.
        # Also let total = vowels + consonants, then:
        #   vowels = consonants = total/2
        # Condition (vowels*consonants) % k == 0  <=> (total^2 / 4) % k == 0
        # We only need substrings with diff==0, i.e., even length.
        #
        # We'll compute for each prefix:
        #   pref_diff[i] = vowels - consonants in s[:i]
        # A substring (l, r] has diff 0 iff pref_diff[l] == pref_diff[r].
        #
        # For those pairs, we must additionally test (m*m) % k == 0 where m=vowels=consonants.
        # We can express m from the prefix counts:
        #   vowels_sub = (total_sub)/2 = ( (len_sub)/2 )
        # because if diff==0 then vowels_sub = consonants_sub = len_sub/2.
        # Hence need ( (len_sub/2) ^2 ) % k == 0.
        #
        # Thus for each valid substring length 2m, require (m*m) % k == 0.

        # Precompute which m are acceptable.
        # m ranges from 1..n//2
        limit = n // 2
        ok_m = [False] * (limit + 1)
        for m in range(1, limit + 1):
            if (m * m) % k == 0:
                ok_m[m] = True

        # Build prefix diff array; diff changes by +1 for vowel, -1 for consonant.
        pref_diff = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref_diff[i + 1] = pref_diff[i] + (1 if ch in vowels_set else -1)

        # Collect indices for each diff value.
        # For any pair (l, r) with same diff, substring length = r-l,
        # so m = (r-l)/2 must be integer => length even.
        # We'll count for each ending index r, how many starting indices l with same diff
        # yield acceptable m.
        from collections import defaultdict

        positions = defaultdict(list)
        for i, d in enumerate(pref_diff):
            positions[d].append(i)

        ans = 0
        # For each diff group, consider indices sorted (they already are).
        for d, idxs in positions.items():
            # Two-pointer / counting by parity and m condition:
            # Need (len/2)= (r-l)/2 in ok_m.
            # Since length even iff parity of l and r matches.
            # For each r, we need count of l such that:
            #   l < r
            #   r-l = 2m where ok_m[m]=True  => l = r - 2m
            # So directly try all m for each r is O(n^2).
            # Optimize by using a set of valid step sizes t = 2m and check membership.
            valid_steps = []
            for m in range(1, limit + 1):
                if ok_m[m]:
                    valid_steps.append(2 * m)

            idx_set = set(idxs)
            for r in idxs:
                for step in valid_steps:
                    l = r - step
                    if l in idx_set:
                        ans += 1

            # Each substring counted exactly once (by choosing its right endpoint r).

        return ans
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")
        n = len(s)

        # Since vowels + consonants = length L, and vowels == consonants => L is even.
        # Let d = vowels - consonants. Beautiful means d == 0.
        # For a substring of length 2m: vowels = consonants = m => vowels * consonants = m^2
        # Condition becomes m^2 % k == 0.
        #
        # For each possible m that satisfies m^2 % k == 0, count substrings of length 2m
        # with equal vowels and consonants (d == 0).
        max_m = n // 2
        good_m = [False] * (max_m + 1)
        for m in range(1, max_m + 1):
            if (m * m) % k == 0:
                good_m[m] = True

        # Prefix difference: pref[i] = (#vowels - #consonants) in s[0:i]
        pref = [0] * (n + 1)
        diff = 0
        for i, ch in enumerate(s, 1):
            if ch in vowels_set:
                diff += 1
            else:
                diff -= 1
            pref[i] = diff

        ans = 0
        # For a fixed m, substring [l, l+2m) is beautiful iff pref[l+2m] == pref[l]
        for m in range(1, max_m + 1):
            if not good_m[m]:
                continue
            length = 2 * m
            for l in range(0, n - length + 1):
                if pref[l + length] == pref[l]:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        def is_vowel(ch: str) -> int:
            return 1 if ch in "aeiou" else 0

        # Let v = #vowels, c = #consonants. Condition: v == c and (v*c) % k == 0
        # For substring length L = v + c, v==c => L is even, and v=c=L/2.
        # Then v*c = (L/2)^2 must be divisible by k.

        n = len(s)
        # Prefix sums for vowels: pref[i] = vowels in s[0:i]
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + is_vowel(ch)

        ans = 0
        # For v=c=m => L=2m. Need (m*m)%k==0.
        # Count all substrings with v=c=m for such m.
        for m in range(1, n // 2 + 1):
            if (m * m) % k != 0:
                continue
            L = 2 * m
            target_v = m
            # Count substrings of length L with exactly m vowels
            # and automatically m consonants because length is 2m.
            for i in range(0, n - L + 1):
                v = pref[i + L] - pref[i]
                if v == target_v:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)

        # dp[mult] = number of ways for current position where
        # (vowels * consonants) % k == mult, with vowels==consonants enforced by construction.
        # We iterate over possible length parity through a prefix-difference approach.
        #
        # Key transformation:
        # Let a = vowels - consonants for a substring. Condition vowels==consonants => a==0.
        # While scanning, we maintain counts of prefixes grouped by (vowels, consonants) product mod k.
        #
        # Since substring length <= 1000, we can enumerate balancing substrings by endpoints with
        # same difference, and compute product mod k incrementally.
        #
        # However, direct product depends on counts, so we do O(n^2) with incremental counts:
        # For each left, expand right until end and maintain v,c. If v==c and (v*c)%k==0 count.
        # n<=1000 => O(n^2)=1e6 substrings expansions, fine.

        ans = 0
        for i in range(n):
            v = 0
            c = 0
            for j in range(i, n):
                ch = s[j]
                if ch in vowels_set:
                    v += 1
                else:
                    c += 1
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        def is_vowel(ch: str) -> int:
            return 1 if ch in vowels_set else 0

        n = len(s)
        ans = 0

        # For any substring, let v = #vowels, c = #consonants.
        # Condition v == c => length = 2m and v = c = m.
        # Then (v*c) % k == (m*m) % k == 0.
        # So for each m such that m*m % k == 0, count substrings with exactly m vowels and length 2m.
        max_m = n // 2
        good_m = [m for m in range(1, max_m + 1) if (m * m) % k == 0]

        # If no m works, answer is 0
        if not good_m:
            return 0

        # Prefix sums of vowels
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + is_vowel(ch)

        # For each length 2m (m vowels, m consonants), count windows with exactly m vowels.
        for m in good_m:
            L = 2 * m
            if L > n:
                continue
            for r in range(L, n + 1):
                # substring s[r-L:r]
                v = pref[r] - pref[r - L]
                if v == m:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")
        n = len(s)

        # Prefix counts
        vpref = [0] * (n + 1)
        cpref = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            vpref[i] = vpref[i - 1] + (1 if ch in vowels_set else 0)
            cpref[i] = cpref[i - 1] + (0 if ch in vowels_set else 1)

        # dp[vcount] -> number of substrings ending at current index
        # that satisfy:
        #   consonants == vowels
        #   and (vowels * consonants) % k == 0
        #
        # Note: consonants==vowels => len is even and v = c = len/2.
        # Then v*c = v^2.
        # Condition becomes v^2 % k == 0.
        # So for any substring with equal vowels and consonants,
        # it's beautiful iff its vowel-count v satisfies v^2 % k == 0.
        # We can pre-filter valid v.
        valid_v = [False] * (n + 1)
        for v in range(1, n + 1):
            if (v * v) % k == 0:
                valid_v[v] = True

        # For substring l..r (1-indexed in prefix), we need:
        #   vowels = vpref[r]-vpref[l-1] = v
        #   consonants = cpref[r]-cpref[l-1] = v
        # => (vpref[r]-vpref[l-1]) == (cpref[r]-cpref[l-1])
        # => (vpref[r]-cpref[r]) == (vpref[l-1]-cpref[l-1])
        # => same diff.
        #
        # Additionally, v itself must be valid.
        # For fixed r, if we know l-1 has same diff, then v is determined
        # by vowel count difference. We'll count by grouping past indices
        # by both diff and vowel prefix count.
        #
        # Let idx = l-1. For substring idx+1..r:
        #   v = vpref[r] - vpref[idx]
        # => vpref[idx] = vpref[r] - v.
        #
        # We'll maintain counts of previous indices keyed by:
        #   diff = vpref[i] - cpref[i]
        #   and vpref[i] (to recover v).
        from collections import defaultdict

        # maps (diff, vpref) -> count
        count = defaultdict(int)
        ans = 0

        # initialize with i=0 prefix
        diff0 = vpref[0] - cpref[0]
        count[(diff0, vpref[0])] = 1

        for r in range(1, n + 1):
            diff_r = vpref[r] - cpref[r]
            # For a candidate substring with equal vowels/consonants,
            # we need previous index i with same diff_r.
            # Then for each valid v: vpref[i] = vpref[r] - v.
            vr = vpref[r]
            # We only need to consider v up to vr (since vpref[i] >= 0)
            max_v = vr
            for v in range(1, max_v + 1):
                if not valid_v[v]:
                    continue
                prev_vp = vr - v
                ans += count.get((diff_r, prev_vp), 0)

            # add current prefix index r for future substrings
            count[(diff_r, vpref[r])] += 1

        return ans
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels_set = set("aeiou")

        # prefix counts
        pv = [0] * (n + 1)
        pc = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            pv[i] = pv[i - 1] + (1 if ch in vowels_set else 0)
            pc[i] = pc[i - 1] + (1 if ch not in vowels_set else 0)

        ans = 0
        # For each possible (v,c) with v==c => v=c=t.
        # Then product = t^2 must be divisible by k.
        # For each t, count substrings with #vowels == #consonants == t.
        # Condition implies t^2 % k == 0.
        #
        # We can count using mapping of (d= pv - pc, pv) differences:
        # For a substring [l, r): let V = pv[r]-pv[l], C=pc[r]-pc[l]
        # Need V==C => (pv[r]-pc[r]) == (pv[l]-pc[l]) i.e., d same.
        # And additionally V * C = V^2 divisible by k.
        # So for each t such that t^2 % k == 0, we count pairs (l<r)
        # where V=t and d matches.
        #
        # Once d matches, V can be derived from pv[r]-pv[l].
        # Since C=V automatically holds when d matches.
        #
        # Complexity: O(n * number_of_valid_t) with number_of_valid_t <= ~32 for k<=1000.

        valid_t = []
        # Maximum t is floor(n/2)
        max_t = n // 2
        for t in range(1, max_t + 1):
            if (t * t) % k == 0:
                valid_t.append(t)

        # If no valid t, answer is 0
        if not valid_t:
            return 0

        # For each t, count substrings with V=t and d unchanged.
        # Let d[i] = pv[i] - pc[i]
        d = [0] * (n + 1)
        for i in range(n + 1):
            d[i] = pv[i] - pc[i]

        # We'll use frequency maps per d for pv prefix values.
        # For each t, need pv[r]-pv[l]=t and d[r]=d[l]
        # => pv[l] = pv[r] - t and same d.
        # So for each position r, count previous l with pv[l] = pv[r]-t and d[l]=d[r].
        from collections import defaultdict

        # Precompute counts of pv values by d as we sweep.
        # But since we need different offsets t, we can handle t by checking pv[r]-t lookup.
        # We'll keep, for each d value, a map of pv count so far.
        freq_by_d = defaultdict(lambda: defaultdict(int))

        for t in valid_t:
            # reset freq for this t
            freq_by_d.clear()
            ans_t = 0
            # initialize with l=0
            freq_by_d[d[0]][pv[0]] += 1
            for r in range(1, n + 1):
                dv = d[r]
                want_pv_l = pv[r] - t
                ans_t += freq_by_d[dv].get(want_pv_l, 0)
                freq_by_d[dv][pv[r]] += 1
            ans += ans_t

        return ans
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        n = len(s)
        ans = 0

        # Count vowels and consonants to find all substrings where v == c.
        # Let v = c => length = v + c is even, and v = c = len/2.
        # For substring [l..r], condition reduces to:
        #   v = c = t
        #   (t * t) % k == 0
        # i.e., t^2 divisible by k.

        # Precompute for t in [1..500] (since v=c => length even <= 1000 -> t<=500)
        ok_t = [False] * (n // 2 + 1)
        for t in range(1, n // 2 + 1):
            if (t * t) % k == 0:
                ok_t[t] = True

        # Prefix difference d = (#vowels - #consonants)
        # Need d == 0 and length even implies equal counts.
        pref = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            pref[i] = pref[i - 1] + (1 if ch in vowels_set else -1)

        # For each start l, find end r such that pref[r] == pref[l] and r-l even.
        # Use O(n^2) with pruning; n=1000 is okay with bitset-like prefix indexing.
        # We'll group prefix positions by (value of pref, parity of index).
        from collections import defaultdict

        # counts[val][parity] = number of occurrences of pref index with that parity
        counts = defaultdict(lambda: [0, 0])
        for i in range(n + 1):
            counts[pref[i]][i & 1] += 1

        # Now iterate over end index r, and count starts l with same pref and same parity.
        # For such pair (l<r), v=c => t = (r-l)/2. Check ok_t[t].
        # Also ensure t>=1 => r-l>=2.
        for r in range(n + 1):
            val = pref[r]
            # We want l < r with same val and same parity (so length even).
            parity = r & 1

            # We'll consider all possible l via scanning; to keep it correct and still efficient,
            # do an O(n^2) but with n=1000 that's 1e6 operations, fine.
            for l in range(r):
                if pref[l] != val:
                    continue
                if (r - l) % 2 != 0:
                    continue
                t = (r - l) // 2
                if t >= 1 and ok_t[t]:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)

        ans = 0

        # We need substrings where vowels == consonants
        # Let length be 2m, then each such substring has m vowels and m consonants.
        # Additionally (m*m) % k == 0.
        # So m must be in {1..floor(n/2)} with (m*m)%k==0.
        good_m = [False] * (n // 2 + 1)
        for m in range(1, n // 2 + 1):
            good_m[m] = (m * m) % k == 0

        # Prefix counts for vowels
        pref_v = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref_v[i + 1] = pref_v[i] + (1 if ch in vowels_set else 0)

        # For each possible half-length m, check all substrings of length 2m
        for m in range(1, n // 2 + 1):
            if not good_m[m]:
                continue
            length = 2 * m
            for l in range(0, n - length + 1):
                r = l + length
                v = pref_v[r] - pref_v[l]
                # consonants = length - v, so v == consonants iff v == m
                if v == m:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        # Prefix sums of vowels and consonants
        n = len(s)
        pref_v = [0] * (n + 1)
        pref_c = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            pref_v[i] = pref_v[i - 1] + (1 if ch in vowels_set else 0)
            pref_c[i] = pref_c[i - 1] + (1 if ch not in vowels_set else 0)

        # For each m = vowels = consonants, need m^2 % k == 0
        good_m = [False] * (n + 1)
        for m in range(1, n // 2 + 1):
            if (m * m) % k == 0:
                good_m[m] = True

        ans = 0
        # Check all possible m by looking for positions where prefix differences match.
        # We use: for substring [l, r) length = 2m, and need pref_v[r]-pref_v[l]=m and pref_c[r]-pref_c[l]=m.
        # Since length is fixed 2m, it's enough to enforce pref_v difference; then pref_c difference holds automatically.
        # More directly: pref_v[r]-pref_v[l]=m and (r-l)=2m.
        for m in range(1, n // 2 + 1):
            if not good_m[m]:
                continue
            two_m = 2 * m
            # Need pref_v[l+2m]-pref_v[l] == m
            for l in range(0, n - two_m + 1):
                r = l + two_m
                if pref_v[r] - pref_v[l] == m:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels_set = set("aeiou")

        # Count vowels and consonants in any substring quickly:
        # Let diff = vowels - consonants.
        # For any substring: vowels == consonants  <=> diff == 0.
        # Also let total = vowels + consonants, then:
        #   vowels = consonants = total/2
        # Condition (vowels*consonants) % k == 0  <=> (total^2 / 4) % k == 0
        # We only need substrings with diff==0, i.e., even length.
        #
        # We'll compute for each prefix:
        #   pref_diff[i] = vowels - consonants in s[:i]
        # A substring (l, r] has diff 0 iff pref_diff[l] == pref_diff[r].
        #
        # For those pairs, we must additionally test (m*m) % k == 0 where m=vowels=consonants.
        # We can express m from the prefix counts:
        #   vowels_sub = (total_sub)/2 = ( (len_sub)/2 )
        # because if diff==0 then vowels_sub = consonants_sub = len_sub/2.
        # Hence need ( (len_sub/2) ^2 ) % k == 0.
        #
        # Thus for each valid substring length 2m, require (m*m) % k == 0.

        # Precompute which m are acceptable.
        # m ranges from 1..n//2
        limit = n // 2
        ok_m = [False] * (limit + 1)
        for m in range(1, limit + 1):
            if (m * m) % k == 0:
                ok_m[m] = True

        # Build prefix diff array; diff changes by +1 for vowel, -1 for consonant.
        pref_diff = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref_diff[i + 1] = pref_diff[i] + (1 if ch in vowels_set else -1)

        # Collect indices for each diff value.
        # For any pair (l, r) with same diff, substring length = r-l,
        # so m = (r-l)/2 must be integer => length even.
        # We'll count for each ending index r, how many starting indices l with same diff
        # yield acceptable m.
        from collections import defaultdict

        positions = defaultdict(list)
        for i, d in enumerate(pref_diff):
            positions[d].append(i)

        ans = 0
        # For each diff group, consider indices sorted (they already are).
        for d, idxs in positions.items():
            # Two-pointer / counting by parity and m condition:
            # Need (len/2)= (r-l)/2 in ok_m.
            # Since length even iff parity of l and r matches.
            # For each r, we need count of l such that:
            #   l < r
            #   r-l = 2m where ok_m[m]=True  => l = r - 2m
            # So directly try all m for each r is O(n^2).
            # Optimize by using a set of valid step sizes t = 2m and check membership.
            valid_steps = []
            for m in range(1, limit + 1):
                if ok_m[m]:
                    valid_steps.append(2 * m)

            idx_set = set(idxs)
            for r in idxs:
                for step in valid_steps:
                    l = r - step
                    if l in idx_set:
                        ans += 1

            # Each substring counted exactly once (by choosing its right endpoint r).

        return ans
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")
        n = len(s)

        # Since vowels + consonants = length L, and vowels == consonants => L is even.
        # Let d = vowels - consonants. Beautiful means d == 0.
        # For a substring of length 2m: vowels = consonants = m => vowels * consonants = m^2
        # Condition becomes m^2 % k == 0.
        #
        # For each possible m that satisfies m^2 % k == 0, count substrings of length 2m
        # with equal vowels and consonants (d == 0).
        max_m = n // 2
        good_m = [False] * (max_m + 1)
        for m in range(1, max_m + 1):
            if (m * m) % k == 0:
                good_m[m] = True

        # Prefix difference: pref[i] = (#vowels - #consonants) in s[0:i]
        pref = [0] * (n + 1)
        diff = 0
        for i, ch in enumerate(s, 1):
            if ch in vowels_set:
                diff += 1
            else:
                diff -= 1
            pref[i] = diff

        ans = 0
        # For a fixed m, substring [l, l+2m) is beautiful iff pref[l+2m] == pref[l]
        for m in range(1, max_m + 1):
            if not good_m[m]:
                continue
            length = 2 * m
            for l in range(0, n - length + 1):
                if pref[l + length] == pref[l]:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        def is_vowel(ch: str) -> int:
            return 1 if ch in "aeiou" else 0

        # Let v = #vowels, c = #consonants. Condition: v == c and (v*c) % k == 0
        # For substring length L = v + c, v==c => L is even, and v=c=L/2.
        # Then v*c = (L/2)^2 must be divisible by k.

        n = len(s)
        # Prefix sums for vowels: pref[i] = vowels in s[0:i]
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + is_vowel(ch)

        ans = 0
        # For v=c=m => L=2m. Need (m*m)%k==0.
        # Count all substrings with v=c=m for such m.
        for m in range(1, n // 2 + 1):
            if (m * m) % k != 0:
                continue
            L = 2 * m
            target_v = m
            # Count substrings of length L with exactly m vowels
            # and automatically m consonants because length is 2m.
            for i in range(0, n - L + 1):
                v = pref[i + L] - pref[i]
                if v == target_v:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)

        # dp[mult] = number of ways for current position where
        # (vowels * consonants) % k == mult, with vowels==consonants enforced by construction.
        # We iterate over possible length parity through a prefix-difference approach.
        #
        # Key transformation:
        # Let a = vowels - consonants for a substring. Condition vowels==consonants => a==0.
        # While scanning, we maintain counts of prefixes grouped by (vowels, consonants) product mod k.
        #
        # Since substring length <= 1000, we can enumerate balancing substrings by endpoints with
        # same difference, and compute product mod k incrementally.
        #
        # However, direct product depends on counts, so we do O(n^2) with incremental counts:
        # For each left, expand right until end and maintain v,c. If v==c and (v*c)%k==0 count.
        # n<=1000 => O(n^2)=1e6 substrings expansions, fine.

        ans = 0
        for i in range(n):
            v = 0
            c = 0
            for j in range(i, n):
                ch = s[j]
                if ch in vowels_set:
                    v += 1
                else:
                    c += 1
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        def is_vowel(ch: str) -> int:
            return 1 if ch in vowels_set else 0

        n = len(s)
        ans = 0

        # For any substring, let v = #vowels, c = #consonants.
        # Condition v == c => length = 2m and v = c = m.
        # Then (v*c) % k == (m*m) % k == 0.
        # So for each m such that m*m % k == 0, count substrings with exactly m vowels and length 2m.
        max_m = n // 2
        good_m = [m for m in range(1, max_m + 1) if (m * m) % k == 0]

        # If no m works, answer is 0
        if not good_m:
            return 0

        # Prefix sums of vowels
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + is_vowel(ch)

        # For each length 2m (m vowels, m consonants), count windows with exactly m vowels.
        for m in good_m:
            L = 2 * m
            if L > n:
                continue
            for r in range(L, n + 1):
                # substring s[r-L:r]
                v = pref[r] - pref[r - L]
                if v == m:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")
        n = len(s)

        # Prefix counts
        vpref = [0] * (n + 1)
        cpref = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            vpref[i] = vpref[i - 1] + (1 if ch in vowels_set else 0)
            cpref[i] = cpref[i - 1] + (0 if ch in vowels_set else 1)

        # dp[vcount] -> number of substrings ending at current index
        # that satisfy:
        #   consonants == vowels
        #   and (vowels * consonants) % k == 0
        #
        # Note: consonants==vowels => len is even and v = c = len/2.
        # Then v*c = v^2.
        # Condition becomes v^2 % k == 0.
        # So for any substring with equal vowels and consonants,
        # it's beautiful iff its vowel-count v satisfies v^2 % k == 0.
        # We can pre-filter valid v.
        valid_v = [False] * (n + 1)
        for v in range(1, n + 1):
            if (v * v) % k == 0:
                valid_v[v] = True

        # For substring l..r (1-indexed in prefix), we need:
        #   vowels = vpref[r]-vpref[l-1] = v
        #   consonants = cpref[r]-cpref[l-1] = v
        # => (vpref[r]-vpref[l-1]) == (cpref[r]-cpref[l-1])
        # => (vpref[r]-cpref[r]) == (vpref[l-1]-cpref[l-1])
        # => same diff.
        #
        # Additionally, v itself must be valid.
        # For fixed r, if we know l-1 has same diff, then v is determined
        # by vowel count difference. We'll count by grouping past indices
        # by both diff and vowel prefix count.
        #
        # Let idx = l-1. For substring idx+1..r:
        #   v = vpref[r] - vpref[idx]
        # => vpref[idx] = vpref[r] - v.
        #
        # We'll maintain counts of previous indices keyed by:
        #   diff = vpref[i] - cpref[i]
        #   and vpref[i] (to recover v).
        from collections import defaultdict

        # maps (diff, vpref) -> count
        count = defaultdict(int)
        ans = 0

        # initialize with i=0 prefix
        diff0 = vpref[0] - cpref[0]
        count[(diff0, vpref[0])] = 1

        for r in range(1, n + 1):
            diff_r = vpref[r] - cpref[r]
            # For a candidate substring with equal vowels/consonants,
            # we need previous index i with same diff_r.
            # Then for each valid v: vpref[i] = vpref[r] - v.
            vr = vpref[r]
            # We only need to consider v up to vr (since vpref[i] >= 0)
            max_v = vr
            for v in range(1, max_v + 1):
                if not valid_v[v]:
                    continue
                prev_vp = vr - v
                ans += count.get((diff_r, prev_vp), 0)

            # add current prefix index r for future substrings
            count[(diff_r, vpref[r])] += 1

        return ans
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels_set = set("aeiou")

        # prefix counts
        pv = [0] * (n + 1)
        pc = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            pv[i] = pv[i - 1] + (1 if ch in vowels_set else 0)
            pc[i] = pc[i - 1] + (1 if ch not in vowels_set else 0)

        ans = 0
        # For each possible (v,c) with v==c => v=c=t.
        # Then product = t^2 must be divisible by k.
        # For each t, count substrings with #vowels == #consonants == t.
        # Condition implies t^2 % k == 0.
        #
        # We can count using mapping of (d= pv - pc, pv) differences:
        # For a substring [l, r): let V = pv[r]-pv[l], C=pc[r]-pc[l]
        # Need V==C => (pv[r]-pc[r]) == (pv[l]-pc[l]) i.e., d same.
        # And additionally V * C = V^2 divisible by k.
        # So for each t such that t^2 % k == 0, we count pairs (l<r)
        # where V=t and d matches.
        #
        # Once d matches, V can be derived from pv[r]-pv[l].
        # Since C=V automatically holds when d matches.
        #
        # Complexity: O(n * number_of_valid_t) with number_of_valid_t <= ~32 for k<=1000.

        valid_t = []
        # Maximum t is floor(n/2)
        max_t = n // 2
        for t in range(1, max_t + 1):
            if (t * t) % k == 0:
                valid_t.append(t)

        # If no valid t, answer is 0
        if not valid_t:
            return 0

        # For each t, count substrings with V=t and d unchanged.
        # Let d[i] = pv[i] - pc[i]
        d = [0] * (n + 1)
        for i in range(n + 1):
            d[i] = pv[i] - pc[i]

        # We'll use frequency maps per d for pv prefix values.
        # For each t, need pv[r]-pv[l]=t and d[r]=d[l]
        # => pv[l] = pv[r] - t and same d.
        # So for each position r, count previous l with pv[l] = pv[r]-t and d[l]=d[r].
        from collections import defaultdict

        # Precompute counts of pv values by d as we sweep.
        # But since we need different offsets t, we can handle t by checking pv[r]-t lookup.
        # We'll keep, for each d value, a map of pv count so far.
        freq_by_d = defaultdict(lambda: defaultdict(int))

        for t in valid_t:
            # reset freq for this t
            freq_by_d.clear()
            ans_t = 0
            # initialize with l=0
            freq_by_d[d[0]][pv[0]] += 1
            for r in range(1, n + 1):
                dv = d[r]
                want_pv_l = pv[r] - t
                ans_t += freq_by_d[dv].get(want_pv_l, 0)
                freq_by_d[dv][pv[r]] += 1
            ans += ans_t

        return ans
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
You are given a string s and a positive integer k.
Let vowels and consonants be the number of vowels and consonants in a string.
A string is beautiful if:

vowels == consonants.
(vowels * consonants) % k == 0, in other terms the multiplication of vowels and consonants is divisible by k.

Return the number of non-empty beautiful substrings in the given string s.
A substring is a contiguous sequence of characters in a string.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Consonant letters in English are every letter except vowels.
 
Example 1:

Input: s = "baeyh", k = 2
Output: 2
Explanation: There are 2 beautiful substrings in the given string.
- Substring "baeyh", vowels = 2 (["a",e"]), consonants = 2 (["y","h"]).
You can see that string "aeyh" is beautiful as vowels == consonants and vowels * consonants % k == 0.
- Substring "baeyh", vowels = 2 (["a",e"]), consonants = 2 (["b","y"]). 
You can see that string "baey" is beautiful as vowels == consonants and vowels * consonants % k == 0.
It can be shown that there are only 2 beautiful substrings in the given string.

Example 2:

Input: s = "abba", k = 1
Output: 3
Explanation: There are 3 beautiful substrings in the given string.
- Substring "abba", vowels = 1 (["a"]), consonants = 1 (["b"]). 
- Substring "abba", vowels = 1 (["a"]), consonants = 1 (["b"]).
- Substring "abba", vowels = 2 (["a","a"]), consonants = 2 (["b","b"]).
It can be shown that there are only 3 beautiful substrings in the given string.

Example 3:

Input: s = "bcdf", k = 1
Output: 0
Explanation: There are no beautiful substrings in the given string.

 
Constraints:

1 <= s.length <= 1000
1 <= k <= 1000
s consists of only English lowercase letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
```

### Answer: (use the provided format with backticks)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        # Let vowels = consonants => total length must be even.
        # Condition (v*c) % k == 0 with v=c=t => t*t % k == 0.
        # So for each substring with half-length t:
        # - number of vowels == number of consonants == t
        # - t*t divisible by k
        #
        # Note k<=1000, s.length<=1000 => t <= 500.
        n = len(s)

        good_t = [False] * (n // 2 + 1)
        for t in range(1, n // 2 + 1):
            if (t * t) % k == 0:
                good_t[t] = True

        # If total length is 2t, then substring is beautiful iff:
        # - good_t[t] is True
        # - vowels == consonants => count of "vowel" positions equals count of "consonant" positions
        # Transform to balance:
        #   balance = vowels - consonants
        # For length 2t, vowels==consonants <=> balance==0.
        #
        # Compute prefix balance:
        #   add +1 for vowel, -1 for consonant
        prefix = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] + (1 if ch in vowels_set else -1)

        ans = 0
        # Count all pairs (l, r) with r-l = 2t and prefix[l]==prefix[r]
        # but only for t where good_t[t] holds.
        # Complexity: sum over t of O(n) => O(n^2) with n<=1000 ok.
        for t in range(1, n // 2 + 1):
            if not good_t[t]:
                continue
            length = 2 * t
            for r in range(length, n + 1):
                l = r - length
                if prefix[l] == prefix[r]:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        # Map balance = vowels - consonants.
        # For a substring to be "beautiful":
        #   vowels == consonants  => balance == 0
        #   (vowels * consonants) % k == 0.
        # When vowels == consonants = t, this becomes t^2 % k == 0.
        #
        # Let t = number of vowels in substring (also consonants).
        # Condition: t^2 divisible by k.
        #
        # We maintain positions by balance prefix, and for each balance group
        # we need to count previous prefixes with same balance and that yield
        # appropriate t. We do this by storing prefix vowel-counts for each balance.
        #
        # For indices i<j: substring s[i:j] has
        #   t = vowels(j)-vowels(i) = consonants(j)-consonants(i)
        #   since balance(j)=balance(i), equivalently vowels difference == consonants diff,
        #   and thus t equals vowels difference.
        #
        # Therefore for each balance value, we need to count pairs with same balance
        # where (delta_vowels)^2 % k == 0.
        #
        # Constraints n<=1000 allow O(n^2) with a direct check per end index.

        n = len(s)
        is_vowel = [1 if ch in vowels_set else 0 for ch in s]

        # prefix balance: vowels - consonants
        # and prefix vowels count.
        pref_bal = [0] * (n + 1)
        pref_v = [0] * (n + 1)
        for i in range(n):
            pref_v[i + 1] = pref_v[i] + is_vowel[i]
            pref_bal[i + 1] = pref_bal[i] + (1 if is_vowel[i] else -1)

        # Precompute all t in [0..n] such that t^2 % k == 0
        good_t = [False] * (n + 1)
        for t in range(1, n + 1):
            if (t * t) % k == 0:
                good_t[t] = True

        ans = 0
        # O(n^2): for each j, check all i<j with equal balance
        for j in range(1, n + 1):
            for i in range(j):
                if pref_bal[i] == pref_bal[j]:
                    t = pref_v[j] - pref_v[i]
                    if t > 0 and good_t[t]:
                        ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        n = len(s)
        # Precompute primality and factor divisibility conditions.
        # Let V = #vowels, C = #consonants in substring.
        # Beautiful iff V == C and V*C divisible by k.
        # With V == C => substring length even, and V*C = V^2 must be divisible by k.
        # So need V^2 % k == 0.
        good_v = set()
        for v in range(1, n + 1):
            if (v * v) % k == 0:
                good_v.add(v)

        # Let balance = V - C. Beautiful requires balance == 0 and V == C = len/2.
        # For each half-length m = v, we need substrings with:
        #   balance == 0 and total length = 2m, i.e. V = m.
        # We'll use prefix sums:
        #   pref[i] = (#vowels - #consonants) up to i (exclusive)
        # Also need V counts; instead, derive V from length and balance:
        #   Let len = j - i
        #   V = (len + balance)/2, C = (len - balance)/2
        # For beauty:
        #   balance == 0 => V = len/2
        #   len even and V^2 % k == 0
        # So: count all substrings with balance==0 and length/2 in good_v.

        # Compute prefix balance.
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            delta = 1 if ch in vowels_set else -1
            pref[i + 1] = pref[i] + delta

        ans = 0
        # For each ending index r, consider possible starting l such that pref[l] == pref[r]
        # and length = r-l is even and (len/2)^2 % k == 0.
        # Since n<=1000, O(n^2) is acceptable.
        for l in range(n):
            for r in range(l + 1, n + 1):
                if pref[l] != pref[r]:
                    continue
                length = r - l
                if length % 2 != 0:
                    continue
                v = length // 2
                if v in good_v:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        # Map each char to +1 if vowel else -1.
        # Then vowels - consonants = sum, and vowels == consonants iff sum == 0.
        a = [1 if ch in vowels_set else -1 for ch in s]

        # Condition (vowels * consonants) % k == 0 with vowels==consonants
        # Let v=c=t, then v*c = t^2. Need t^2 % k == 0.
        # If prefix diff is 0 over substring, then t = (len)/2.
        # So we only need to consider substrings of even length with diff 0,
        # and check ((len/2)^2) % k == 0.
        #
        # Since len <= 1000, we can precompute for t up to 500.

        n = len(s)
        max_t = n // 2
        ok_t = [False] * (max_t + 1)
        for t in range(max_t + 1):
            if t * t % k == 0:
                ok_t[t] = True

        # Prefix sums of diff
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + a[i]

        ans = 0
        # Count beautiful substrings by enumerating end index and using prefix sums with same value.
        # For a fixed pair (l, r) with pref[l] == pref[r], substring length = r-l.
        # Need length even and t=(r-l)/2 satisfies ok_t[t].
        # We can do this by grouping positions by prefix sum value and checking lengths.
        from collections import defaultdict

        pos_by_sum = defaultdict(list)
        for i in range(n + 1):
            pos_by_sum[pref[i]].append(i)

        for val, positions in pos_by_sum.items():
            # For two positions i<j, substring length = j-i. Need (j-i) even
            # and ok_t[(j-i)//2].
            m = len(positions)
            # O(m^2) worst-case could be large, but prefix sums distribution is balanced.
            # Still could be ~1e6, acceptable (n<=1000).
            for idx_i in range(m):
                i = positions[idx_i]
                for idx_j in range(idx_i + 1, m):
                    j = positions[idx_j]
                    length = j - i
                    if length & 1:
                        continue
                    t = length // 2
                    if ok_t[t]:
                        ans += 1

        return ans
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")
        n = len(s)

        # Count vowels and consonants prefix-wise:
        # let v[i] = vowels in s[0:i], c[i] = consonants in s[0:i]
        # For substring (l..r-1): dv = v[r]-v[l], dc = c[r]-c[l]
        # Beautiful iff dv == dc and (dv*dc) % k == 0 => dv^2 % k == 0
        #
        # Since dv==dc, dv = dc = len/2, so substring length must be even.
        # We can treat dv-dc = 0 using a running balance:
        # balance += +1 for vowel, -1 for consonant.
        # Then dv==dc <=> balance end == balance start.

        pref_v = [0] * (n + 1)
        pref_c = [0] * (n + 1)
        balance = [0] * (n + 1)
        for i, ch in enumerate(s):
            is_v = ch in vowels_set
            pref_v[i + 1] = pref_v[i] + (1 if is_v else 0)
            pref_c[i + 1] = pref_c[i] + (0 if is_v else 1)
            balance[i + 1] = balance[i] + (1 if is_v else -1)

        # Condition dv^2 % k == 0 depends only on dv.
        # dv is at most n/2 (<=500). We'll precompute good t values:
        max_t = n // 2
        good_t = [False] * (max_t + 1)
        for t in range(1, max_t + 1):
            if (t * t) % k == 0:
                good_t[t] = True

        # For each r, we need count of l<r with:
        # 1) balance[l] == balance[r]  => dv==dc
        # 2) t = dv = (r-l)/2 is "good"
        #
        # We can compute dv for given (l,r) as pref_v[r]-pref_v[l],
        # but we need do it efficiently.
        # Instead, note that dv = (r-l)/2 when dv==dc (because length = 2*dv).
        # So t = (r-l)/2 depends only on (r-l).
        #
        # So for fixed r, among all l where balance equal, we only accept those with even length
        # and t=(r-l)/2 good. That is, (r-l) must be 2*t => l = r - 2*t.
        #
        # Therefore, for each r and each good t, we check l = r-2*t if balance matches.
        # Complexity O(n * number_of_good_t) is OK since max_t<=500.
        good_ts = [t for t in range(1, max_t + 1) if good_t[t]]

        ans = 0
        for r in range(1, n + 1):
            for t in good_ts:
                l = r - 2 * t
                if l < 0:
                    continue
                if balance[l] == balance[r]:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        # Prefix counts
        prefV = [0] * (n + 1)
        prefC = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            prefV[i] = prefV[i - 1] + (1 if ch in vowels_set else 0)
            prefC[i] = prefC[i - 1] + (1 if ch not in vowels_set else 0)

        # A substring [l..r) is beautiful iff:
        # let d = prefV[r]-prefV[l], then prefC substring = (len - d).
        # Conditions:
        #   d == len - d  => len = 2d, i.e. vowels = consonants => d = len/2
        #   d * d % k == 0 => d % sqrt(k?) not exactly; just use d*d % k.
        #
        # We iterate possible substring length 2m, then vowels = m.
        # For each r, want l such that:
        #   prefV[r] - prefV[l] = m
        #   len = 2m => r-l = 2m  => l = r - 2m
        #
        # So for each center (end r) and each m that keeps bounds, check only that single l.
        ans = 0
        # Since d*d divisible by k, d can't be too large, but simplest given constraints:
        # n <= 1000 => O(n^2) is fine (1e6) with constant work.
        for r in range(1, n + 1):
            # maximum m such that 2m <= r
            max_m = r // 2
            for m in range(1, max_m + 1):
                l = r - 2 * m
                d = prefV[r] - prefV[l]
                # Ensure vowels = m (then consonants will also be m automatically since len=2m)
                if d != m:
                    continue
                if (m * m) % k == 0:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        n = len(s)
        pref_v = [0] * (n + 1)
        pref_c = [0] * (n + 1)

        for i, ch in enumerate(s, 1):
            pref_v[i] = pref_v[i - 1] + (1 if ch in vowels_set else 0)
            pref_c[i] = pref_c[i - 1] + (1 if ch not in vowels_set else 0)

        # Precompute which pairs (v,c) with v=c and (v*v)%k==0 are allowed.
        # Let v=c=m, then requirement is m*m divisible by k.
        allowed_m = [False] * (n + 1)
        for m in range(n + 1):
            if (m * m) % k == 0:
                allowed_m[m] = True

        ans = 0
        # Enumerate substrings by their length:
        # If vowels == consonants, then 2*m = length => length must be even.
        for l in range(n):
            for r in range(l + 1, n + 1):
                v = pref_v[r] - pref_v[l]
                c = pref_c[r] - pref_c[l]
                if v == c and allowed_m[v]:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        # Convert each char to 1 if vowel else -1
        # Then for any substring:
        #   vowels - consonants == sum(values)
        #   vowels == consonants  <=> sum(values) == 0
        vals = [1 if ch in vowels_set else -1 for ch in s]

        # For each position i, prefix sum P[i] = sum(vals[0:i])
        # Need pairs (l,r] such that P[r] == P[l] (zero balance)
        # Additionally, require (vowels * consonants) % k == 0.
        #
        # Let length of balanced substring be 2m => vowels=consonants=m.
        # Then condition is m*m % k == 0.
        #
        # So we need count of balanced substrings where m satisfies m^2 % k == 0.
        ok_m = [False] * (n // 2 + 1)
        for m in range(1, n // 2 + 1):
            if (m * m) % k == 0:
                ok_m[m] = True

        # We'll count for each prefix sum value separately using a mapping:
        # For each prefix sum P at position l, we need r such that:
        #   P[r] == P[l]  and  m = (r-l)/2 is valid.
        # Since balanced implies r-l even and m=(r-l)/2.
        #
        # We iterate r from 1..n, maintain positions by prefix sum value.
        # For fixed r and prefix sum value v, potential l are those with same v.
        # m depends on l: m = (r-l)/2.
        # We'll maintain for each v two Fenwick-like counts by parity/length?
        #
        # Simpler: since n<=1000, O(n^2) is fine: check all substrings with sum==0.
        ans = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + vals[i]

        # O(n^2) enumeration of balanced substrings:
        # For l<r, require prefix[r]==prefix[l]. Then length is even.
        # m = (r-l)/2, and check ok_m[m].
        for l in range(n):
            for r in range(l + 1, n + 1):
                if prefix[r] != prefix[l]:
                    continue
                length = r - l
                if length % 2 == 1:
                    continue
                m = length // 2
                if m >= 1 and ok_m[m]:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        # prefix counts of vowels and consonants
        n = len(s)
        prefV = [0] * (n + 1)
        prefC = [0] * (n + 1)

        for i, ch in enumerate(s):
            prefV[i + 1] = prefV[i] + (1 if ch in vowels_set else 0)
            prefC[i + 1] = prefC[i] + (0 if ch in vowels_set else 1)

        ans = 0

        # vowels == consonants => 2*vowels == length => length must be even.
        # For each even-length substring, check divisibility condition.
        for l in range(n):
            # maximum length so far: 2*min possible
            for r in range(l + 1, n):
                v = prefV[r + 1] - prefV[l]
                c = prefC[r + 1] - prefC[l]
                if v != c:
                    continue
                # v*c divisible by k
                if (v * c) % k == 0:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)

        # prefix difference d = vowels - consonants
        d = 0
        diff = [0] * (n + 1)  # diff[i] = vowels - consonants up to i
        for i, ch in enumerate(s, 1):
            if ch in vowels_set:
                d += 1
            else:
                d -= 1
            diff[i] = d

        # We need vowels == consonants => length even and diff[i]==diff[j]
        # Additionally (v*c) % k == 0.
        # With vowels=c=t for a substring: t = len/2 and v*c = t^2.
        # So we require (t^2) % k == 0.
        #
        # For a substring i..j-1 with vowels=c=t:
        #   t = (j-i)/2, and since diff equal, t is determined by its endpoints.
        #
        # Approach:
        #   Enumerate possible t that satisfy (t^2)%k==0.
        #   For each position parity, count endpoints with correct diff and t.
        #
        # Let substring length = 2t => j = i + 2t.
        # Condition diff[j] == diff[i] and (t^2)%k==0.
        ok_t = [t for t in range(1, n // 2 + 1) if (t * t) % k == 0]

        ans = 0
        # For each t, count pairs (i, i+2t) with same diff.
        for t in ok_t:
            step = 2 * t
            # i ranges 0..n-step
            for i in range(0, n - step + 1):
                if diff[i] == diff[i + step]:
                    ans += 1
        return ans
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        # Let vowels = consonants => total length must be even.
        # Condition (v*c) % k == 0 with v=c=t => t*t % k == 0.
        # So for each substring with half-length t:
        # - number of vowels == number of consonants == t
        # - t*t divisible by k
        #
        # Note k<=1000, s.length<=1000 => t <= 500.
        n = len(s)

        good_t = [False] * (n // 2 + 1)
        for t in range(1, n // 2 + 1):
            if (t * t) % k == 0:
                good_t[t] = True

        # If total length is 2t, then substring is beautiful iff:
        # - good_t[t] is True
        # - vowels == consonants => count of "vowel" positions equals count of "consonant" positions
        # Transform to balance:
        #   balance = vowels - consonants
        # For length 2t, vowels==consonants <=> balance==0.
        #
        # Compute prefix balance:
        #   add +1 for vowel, -1 for consonant
        prefix = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] + (1 if ch in vowels_set else -1)

        ans = 0
        # Count all pairs (l, r) with r-l = 2t and prefix[l]==prefix[r]
        # but only for t where good_t[t] holds.
        # Complexity: sum over t of O(n) => O(n^2) with n<=1000 ok.
        for t in range(1, n // 2 + 1):
            if not good_t[t]:
                continue
            length = 2 * t
            for r in range(length, n + 1):
                l = r - length
                if prefix[l] == prefix[r]:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        # Map balance = vowels - consonants.
        # For a substring to be "beautiful":
        #   vowels == consonants  => balance == 0
        #   (vowels * consonants) % k == 0.
        # When vowels == consonants = t, this becomes t^2 % k == 0.
        #
        # Let t = number of vowels in substring (also consonants).
        # Condition: t^2 divisible by k.
        #
        # We maintain positions by balance prefix, and for each balance group
        # we need to count previous prefixes with same balance and that yield
        # appropriate t. We do this by storing prefix vowel-counts for each balance.
        #
        # For indices i<j: substring s[i:j] has
        #   t = vowels(j)-vowels(i) = consonants(j)-consonants(i)
        #   since balance(j)=balance(i), equivalently vowels difference == consonants diff,
        #   and thus t equals vowels difference.
        #
        # Therefore for each balance value, we need to count pairs with same balance
        # where (delta_vowels)^2 % k == 0.
        #
        # Constraints n<=1000 allow O(n^2) with a direct check per end index.

        n = len(s)
        is_vowel = [1 if ch in vowels_set else 0 for ch in s]

        # prefix balance: vowels - consonants
        # and prefix vowels count.
        pref_bal = [0] * (n + 1)
        pref_v = [0] * (n + 1)
        for i in range(n):
            pref_v[i + 1] = pref_v[i] + is_vowel[i]
            pref_bal[i + 1] = pref_bal[i] + (1 if is_vowel[i] else -1)

        # Precompute all t in [0..n] such that t^2 % k == 0
        good_t = [False] * (n + 1)
        for t in range(1, n + 1):
            if (t * t) % k == 0:
                good_t[t] = True

        ans = 0
        # O(n^2): for each j, check all i<j with equal balance
        for j in range(1, n + 1):
            for i in range(j):
                if pref_bal[i] == pref_bal[j]:
                    t = pref_v[j] - pref_v[i]
                    if t > 0 and good_t[t]:
                        ans += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        n = len(s)
        # Precompute primality and factor divisibility conditions.
        # Let V = #vowels, C = #consonants in substring.
        # Beautiful iff V == C and V*C divisible by k.
        # With V == C => substring length even, and V*C = V^2 must be divisible by k.
        # So need V^2 % k == 0.
        good_v = set()
        for v in range(1, n + 1):
            if (v * v) % k == 0:
                good_v.add(v)

        # Let balance = V - C. Beautiful requires balance == 0 and V == C = len/2.
        # For each half-length m = v, we need substrings with:
        #   balance == 0 and total length = 2m, i.e. V = m.
        # We'll use prefix sums:
        #   pref[i] = (#vowels - #consonants) up to i (exclusive)
        # Also need V counts; instead, derive V from length and balance:
        #   Let len = j - i
        #   V = (len + balance)/2, C = (len - balance)/2
        # For beauty:
        #   balance == 0 => V = len/2
        #   len even and V^2 % k == 0
        # So: count all substrings with balance==0 and length/2 in good_v.

        # Compute prefix balance.
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            delta = 1 if ch in vowels_set else -1
            pref[i + 1] = pref[i] + delta

        ans = 0
        # For each ending index r, consider possible starting l such that pref[l] == pref[r]
        # and length = r-l is even and (len/2)^2 % k == 0.
        # Since n<=1000, O(n^2) is acceptable.
        for l in range(n):
            for r in range(l + 1, n + 1):
                if pref[l] != pref[r]:
                    continue
                length = r - l
                if length % 2 != 0:
                    continue
                v = length // 2
                if v in good_v:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        # Map each char to +1 if vowel else -1.
        # Then vowels - consonants = sum, and vowels == consonants iff sum == 0.
        a = [1 if ch in vowels_set else -1 for ch in s]

        # Condition (vowels * consonants) % k == 0 with vowels==consonants
        # Let v=c=t, then v*c = t^2. Need t^2 % k == 0.
        # If prefix diff is 0 over substring, then t = (len)/2.
        # So we only need to consider substrings of even length with diff 0,
        # and check ((len/2)^2) % k == 0.
        #
        # Since len <= 1000, we can precompute for t up to 500.

        n = len(s)
        max_t = n // 2
        ok_t = [False] * (max_t + 1)
        for t in range(max_t + 1):
            if t * t % k == 0:
                ok_t[t] = True

        # Prefix sums of diff
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + a[i]

        ans = 0
        # Count beautiful substrings by enumerating end index and using prefix sums with same value.
        # For a fixed pair (l, r) with pref[l] == pref[r], substring length = r-l.
        # Need length even and t=(r-l)/2 satisfies ok_t[t].
        # We can do this by grouping positions by prefix sum value and checking lengths.
        from collections import defaultdict

        pos_by_sum = defaultdict(list)
        for i in range(n + 1):
            pos_by_sum[pref[i]].append(i)

        for val, positions in pos_by_sum.items():
            # For two positions i<j, substring length = j-i. Need (j-i) even
            # and ok_t[(j-i)//2].
            m = len(positions)
            # O(m^2) worst-case could be large, but prefix sums distribution is balanced.
            # Still could be ~1e6, acceptable (n<=1000).
            for idx_i in range(m):
                i = positions[idx_i]
                for idx_j in range(idx_i + 1, m):
                    j = positions[idx_j]
                    length = j - i
                    if length & 1:
                        continue
                    t = length // 2
                    if ok_t[t]:
                        ans += 1

        return ans
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")
        n = len(s)

        # Count vowels and consonants prefix-wise:
        # let v[i] = vowels in s[0:i], c[i] = consonants in s[0:i]
        # For substring (l..r-1): dv = v[r]-v[l], dc = c[r]-c[l]
        # Beautiful iff dv == dc and (dv*dc) % k == 0 => dv^2 % k == 0
        #
        # Since dv==dc, dv = dc = len/2, so substring length must be even.
        # We can treat dv-dc = 0 using a running balance:
        # balance += +1 for vowel, -1 for consonant.
        # Then dv==dc <=> balance end == balance start.

        pref_v = [0] * (n + 1)
        pref_c = [0] * (n + 1)
        balance = [0] * (n + 1)
        for i, ch in enumerate(s):
            is_v = ch in vowels_set
            pref_v[i + 1] = pref_v[i] + (1 if is_v else 0)
            pref_c[i + 1] = pref_c[i] + (0 if is_v else 1)
            balance[i + 1] = balance[i] + (1 if is_v else -1)

        # Condition dv^2 % k == 0 depends only on dv.
        # dv is at most n/2 (<=500). We'll precompute good t values:
        max_t = n // 2
        good_t = [False] * (max_t + 1)
        for t in range(1, max_t + 1):
            if (t * t) % k == 0:
                good_t[t] = True

        # For each r, we need count of l<r with:
        # 1) balance[l] == balance[r]  => dv==dc
        # 2) t = dv = (r-l)/2 is "good"
        #
        # We can compute dv for given (l,r) as pref_v[r]-pref_v[l],
        # but we need do it efficiently.
        # Instead, note that dv = (r-l)/2 when dv==dc (because length = 2*dv).
        # So t = (r-l)/2 depends only on (r-l).
        #
        # So for fixed r, among all l where balance equal, we only accept those with even length
        # and t=(r-l)/2 good. That is, (r-l) must be 2*t => l = r - 2*t.
        #
        # Therefore, for each r and each good t, we check l = r-2*t if balance matches.
        # Complexity O(n * number_of_good_t) is OK since max_t<=500.
        good_ts = [t for t in range(1, max_t + 1) if good_t[t]]

        ans = 0
        for r in range(1, n + 1):
            for t in good_ts:
                l = r - 2 * t
                if l < 0:
                    continue
                if balance[l] == balance[r]:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        # Prefix counts
        prefV = [0] * (n + 1)
        prefC = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            prefV[i] = prefV[i - 1] + (1 if ch in vowels_set else 0)
            prefC[i] = prefC[i - 1] + (1 if ch not in vowels_set else 0)

        # A substring [l..r) is beautiful iff:
        # let d = prefV[r]-prefV[l], then prefC substring = (len - d).
        # Conditions:
        #   d == len - d  => len = 2d, i.e. vowels = consonants => d = len/2
        #   d * d % k == 0 => d % sqrt(k?) not exactly; just use d*d % k.
        #
        # We iterate possible substring length 2m, then vowels = m.
        # For each r, want l such that:
        #   prefV[r] - prefV[l] = m
        #   len = 2m => r-l = 2m  => l = r - 2m
        #
        # So for each center (end r) and each m that keeps bounds, check only that single l.
        ans = 0
        # Since d*d divisible by k, d can't be too large, but simplest given constraints:
        # n <= 1000 => O(n^2) is fine (1e6) with constant work.
        for r in range(1, n + 1):
            # maximum m such that 2m <= r
            max_m = r // 2
            for m in range(1, max_m + 1):
                l = r - 2 * m
                d = prefV[r] - prefV[l]
                # Ensure vowels = m (then consonants will also be m automatically since len=2m)
                if d != m:
                    continue
                if (m * m) % k == 0:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        n = len(s)
        pref_v = [0] * (n + 1)
        pref_c = [0] * (n + 1)

        for i, ch in enumerate(s, 1):
            pref_v[i] = pref_v[i - 1] + (1 if ch in vowels_set else 0)
            pref_c[i] = pref_c[i - 1] + (1 if ch not in vowels_set else 0)

        # Precompute which pairs (v,c) with v=c and (v*v)%k==0 are allowed.
        # Let v=c=m, then requirement is m*m divisible by k.
        allowed_m = [False] * (n + 1)
        for m in range(n + 1):
            if (m * m) % k == 0:
                allowed_m[m] = True

        ans = 0
        # Enumerate substrings by their length:
        # If vowels == consonants, then 2*m = length => length must be even.
        for l in range(n):
            for r in range(l + 1, n + 1):
                v = pref_v[r] - pref_v[l]
                c = pref_c[r] - pref_c[l]
                if v == c and allowed_m[v]:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        # Convert each char to 1 if vowel else -1
        # Then for any substring:
        #   vowels - consonants == sum(values)
        #   vowels == consonants  <=> sum(values) == 0
        vals = [1 if ch in vowels_set else -1 for ch in s]

        # For each position i, prefix sum P[i] = sum(vals[0:i])
        # Need pairs (l,r] such that P[r] == P[l] (zero balance)
        # Additionally, require (vowels * consonants) % k == 0.
        #
        # Let length of balanced substring be 2m => vowels=consonants=m.
        # Then condition is m*m % k == 0.
        #
        # So we need count of balanced substrings where m satisfies m^2 % k == 0.
        ok_m = [False] * (n // 2 + 1)
        for m in range(1, n // 2 + 1):
            if (m * m) % k == 0:
                ok_m[m] = True

        # We'll count for each prefix sum value separately using a mapping:
        # For each prefix sum P at position l, we need r such that:
        #   P[r] == P[l]  and  m = (r-l)/2 is valid.
        # Since balanced implies r-l even and m=(r-l)/2.
        #
        # We iterate r from 1..n, maintain positions by prefix sum value.
        # For fixed r and prefix sum value v, potential l are those with same v.
        # m depends on l: m = (r-l)/2.
        # We'll maintain for each v two Fenwick-like counts by parity/length?
        #
        # Simpler: since n<=1000, O(n^2) is fine: check all substrings with sum==0.
        ans = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + vals[i]

        # O(n^2) enumeration of balanced substrings:
        # For l<r, require prefix[r]==prefix[l]. Then length is even.
        # m = (r-l)/2, and check ok_m[m].
        for l in range(n):
            for r in range(l + 1, n + 1):
                if prefix[r] != prefix[l]:
                    continue
                length = r - l
                if length % 2 == 1:
                    continue
                m = length // 2
                if m >= 1 and ok_m[m]:
                    ans += 1
        return ans
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = set("aeiou")

        # prefix counts of vowels and consonants
        n = len(s)
        prefV = [0] * (n + 1)
        prefC = [0] * (n + 1)

        for i, ch in enumerate(s):
            prefV[i + 1] = prefV[i] + (1 if ch in vowels_set else 0)
            prefC[i + 1] = prefC[i] + (0 if ch in vowels_set else 1)

        ans = 0

        # vowels == consonants => 2*vowels == length => length must be even.
        # For each even-length substring, check divisibility condition.
        for l in range(n):
            # maximum length so far: 2*min possible
            for r in range(l + 1, n):
                v = prefV[r + 1] - prefV[l]
                c = prefC[r + 1] - prefC[l]
                if v != c:
                    continue
                # v*c divisible by k
                if (v * c) % k == 0:
                    ans += 1

        return ans
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)

        # prefix difference d = vowels - consonants
        d = 0
        diff = [0] * (n + 1)  # diff[i] = vowels - consonants up to i
        for i, ch in enumerate(s, 1):
            if ch in vowels_set:
                d += 1
            else:
                d -= 1
            diff[i] = d

        # We need vowels == consonants => length even and diff[i]==diff[j]
        # Additionally (v*c) % k == 0.
        # With vowels=c=t for a substring: t = len/2 and v*c = t^2.
        # So we require (t^2) % k == 0.
        #
        # For a substring i..j-1 with vowels=c=t:
        #   t = (j-i)/2, and since diff equal, t is determined by its endpoints.
        #
        # Approach:
        #   Enumerate possible t that satisfy (t^2)%k==0.
        #   For each position parity, count endpoints with correct diff and t.
        #
        # Let substring length = 2t => j = i + 2t.
        # Condition diff[j] == diff[i] and (t^2)%k==0.
        ok_t = [t for t in range(1, n // 2 + 1) if (t * t) % k == 0]

        ans = 0
        # For each t, count pairs (i, i+2t) with same diff.
        for t in ok_t:
            step = 2 * t
            # i ranges 0..n-step
            for i in range(0, n - step + 1):
                if diff[i] == diff[i + step]:
                    ans += 1
        return ans
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "2",
      "actual": "2",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "3",
      "actual": "3",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
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
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    },
    {
      "passed": true,
      "expected": "0",
      "actual": "0",
      "error": ""
    }
  ]
}
```

</details>
