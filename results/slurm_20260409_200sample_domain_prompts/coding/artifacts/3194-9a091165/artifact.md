# Problem 3194

- Domain: `coding`

## Problem

```text
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.
 
Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Example 2:

Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.

Example 3:

Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
Output: []
Explanation: "z" does not occur in any of the words. Hence, we return an empty array.

 
Constraints:

1 <= words.length <= 50
1 <= words[i].length <= 50
x is a lowercase English letter.
words[i] consists only of lowercase English letters.
```

### Starter Code

```python
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
```

### Test Cases

```json
[
  {
    "input": "[\"leet\", \"code\"]\n\"e\"",
    "output": "[0, 1]",
    "testtype": "functional"
  },
  {
    "input": "[\"abc\", \"bcd\", \"aaaa\", \"cbc\"]\n\"a\"",
    "output": "[0, 2]",
    "testtype": "functional"
  },
  {
    "input": "[\"abc\", \"bcd\", \"aaaa\", \"cbc\"]\n\"z\"",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[\"up\"]\n\"k\"",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[\"wn\", \"aeh\"]\n\"t\"",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[\"em\", \"lfqpu\"]\n\"i\"",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[\"o\", \"bn\", \"l\"]\n\"s\"",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[\"iftim\", \"aohcs\", \"zia\", \"hku\"]\n\"i\"",
    "output": "[0, 2]",
    "testtype": "functional"
  },
  {
    "input": "[\"wtkm\", \"msnf\", \"z\", \"yzl\", \"agfk\"]\n\"c\"",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[\"potl\", \"bm\", \"r\", \"uxuga\", \"qcepm\"]\n\"f\"",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[\"szpse\", \"jfj\", \"kgb\", \"t\", \"vmfgp\"]\n\"b\"",
    "output": "[2]",
    "testtype": "functional"
  },
  {
    "input": "[\"rbdu\", \"ptd\", \"jl\", \"fupbt\", \"pgp\"]\n\"j\"",
    "output": "[2]",
    "testtype": "functional"
  },
  {
    "input": "[\"kbejcvnxlmfxbffcnjgvshklvebhypvgazrnuozyetyyhaju\", \"mhjfuwzecfttjqqbrvgvzpxfzrlwmioevmrhktfsuaufdpl\", \"qxvtsducsonjekxtyfbmlojgnbyxujjvggdoiwvhbkr\", \"ltzxahncxfhpasulxnyipoliyivlizrmf\", \"tebwiiktawvxhdovuuorww\", \"bbbmbrgzxfxsopbnmpzdwcfsfvzfe\", \"cnxijuydoanojyenvulprsceuf\", \"wifkjeloyamovvxapdsaj\", \"dgryrnczxlrwoadbausdfjgmzrperqn\", \"mlgugxsexmtgjwgufneivzxptqdbwajtbyox\", \"slayklnpoiuqjcgzdhifjjxjzphtpnlogd\", \"vgsziqfdqszstgpimccoteuzzvvqmogwbsuctzxdvzupv\", \"noktlyzmvpfgwrbthnpvvebfoboh\", \"vpxejkbueafhiflsjxmvl\", \"busjltaxdshhozxgindodltzpapiacyxxqdganmtnmt\", \"focpqogzxmmawvodrwqcmkmbtjjpwhconiomubmlwu\", \"opwsgswjqhbevoreywhsdkkindxqrxyqgilku\", \"xtezztspvcibkwwhprljvsvtg\", \"mwomqhxnjefoeogqmsbmursilasavcbmhvdmnpew\", \"lktwlqxkmrtgxcposoirsyzyiusbu\", \"tipnnmdecxinlieoxvarneqhanbrnmkyoolncwzfmvppfxo\", \"mawvsgjiuinrncmksfhsc\", \"ufsbrjvfdzvzljxoayzszdtxianorvdtaoelpbvutxzpib\", \"ngzzdglbewvnotbafnpakapjuybnhfdliauimcjnynkr\", \"kjokfbaslrrtnqokxgkqepdztoicnityubrobwgibbez\", \"xpuzrhgouwlnqkmzbccnhafrasfeagzafawjeduiwgfreefriw\", \"rdetsskqsrydxunygvzwdwsemzdswjwkxznj\", \"vwfwhqntsttpeachvkyknplm\", \"ujgxgahgnxsyzrhvksicfurboaqodzkwfzwbhtuptiajdc\", \"cxlagbquzxlplmrxzoqhyzhfdqpeqycuzshwkcsxvjyctqxz\", \"azokvdthuwyihxkaalmskvuzszqhdlsszgaj\", \"jcxtdgrpqalazjvdehgspfjmf\", \"jkiyvwutljwgphxnvczssciqkpyocpokxwejcq\", \"bvxybwgudhclvwpwijwtoyvqr\", \"vbuhqaiazqsrmfdihgfdrivqbmudlxjfdlrq\", \"kzmzeepjryiyhxgvbfmafkm\", \"nhtfmutfiqrilznxpfpbdqsdnufxypvpug\", \"hwpjebysweytrtbkyaiytczuet\", \"mdxjmvbtirlynvniqdpqy\", \"kfzzoipcaazcdabezuaixohmcgvatdhjloi\", \"wyllnbnctghpwoghfnyavhftlazkfnbvovaoxw\", \"tspznywrhwmdqjatlhsnqqlhtfyusmdpnftgjkilqct\", \"mborrflkkcmbuqkydohmnfh\", \"vevutfdaylwrrjgqmbreztkomfwrzablyuknejo\"]\n\"x\"",
    "output": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
    "testtype": "functional"
  },
  {
    "input": "[\"ktmftanyvapprwroyihcafidtjwmrv\", \"ncszofucbxlxewbjbfnngilaaecbvpjoqfmkhp\", \"lefyucdzdyvnbximhzhqbncfyqlyatymrppqv\", \"wservhfditixgqhmauswiaiicljpbtltgkgjvkh\", \"fplnvkyromzukgiautjczbiqreqixkttdeoyg\", \"yebwncvqedgnnievfsekqb\", \"ecjafgdanuvikffrawslydcucabjtgqfeccdzpgoue\", \"vlrmjvewojhiwyzawvjejmnaypct\", \"qxmkqgmjooaqsaqlkqedskig\", \"pklwuuxsmefvxujivhdekkogiaghsyaj\", \"jpwmirqzbdmpqqoaysasufgudvdwsjgobirudjfztqrtqjndkd\", \"wffdbxyunbnyzedargkludneahnjttygnhpwrvyrtgpveczqah\", \"ozeebrxzffqbcwtgtvvfhtgzkqvtxlngcgzncokupsmrcedpwa\", \"kfyinczvsijeaytmvifwpybykcnxkvrocwhf\", \"eqbqpybwsegbbvmnvpbqwvpcr\", \"jnopigqjwyuzxhojvyoilsfkpaswvbwkqtiwoqzc\", \"ijqpfkuclqgcqjdbqvryicitjisvjdqneileybxztw\", \"rjulaxwwapltyfxoybulfuob\", \"mibjvxhprvpbxpfksbymnadsxtw\", \"zazdcnjmazacxwsfhdavjw\", \"eynqnpmsudafljvxjxkzxeedmcgkurkw\", \"qewpuxqgisltkqwsntabalgrbghtgv\", \"kxhxmdqgoqjjyukfqkuqxdszritbkopdkgrplptcadrkrkaum\", \"udgjlcbpniveczohitwbyedogayvzip\", \"yjswlmqgabzhxlwyrpbahlbbjovvbwcqdwsjivwqzeauwpis\", \"ufsvcyvsxkclzbnhmyhzyjopxc\", \"spjzjimxpwuakljjwdvadzbeluysufyzvt\", \"ipjpynrpkpogwzrwopusztnlimp\", \"tpbgccmoveedtbltbxmcqnngibdpw\", \"gehbhpzxnslrgndqvxbycipj\", \"zwfoiwndphkkmwkdtltqxdu\", \"pbdezhbsrizaaihkkeqnmmjugqyfmreouckkfc\", \"nejubxbhxvhhalsufscjcjoq\", \"rcmayzriaflrhgcaynzmkqtyouxbkxwjbgsdlmfuljkxh\", \"bqbclnunzktwbzczcdyrinknoymqzxjiliqufosqtrqdekz\", \"eznwevryhkywrknlnnvgirmnbhehehwuxtgaiwjavuvob\", \"cwipeyakowweovjtcxeuczcxszgfporcsszgdzajqoub\", \"uigqiroskpujrxugikfvzscqffxinhij\", \"flodpmbiwemcwapapeqeivhdhyxiuocjaa\", \"oylkkcstgnhzhsmcdaytzadgcdrncckpczgwetplia\", \"ieeujdeqkeksxcxvtppunxbmfbggycdojldvlv\", \"nkutalxkajiaidyfjcahwwl\", \"nftcgzjhpdlggdlnufpcknzuqmfcapxhokloizknuicagd\", \"efynpflqqmwjcgmllbqijyflzdkvmzqzaeebnoycili\", \"xdwmwkymmynzjnnkjkybzzf\"]\n\"b\"",
    "output": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
    "testtype": "functional"
  },
  {
    "input": "[\"aipqlhhujbqocvnotkfvl\", \"ibjsurngatzqdzbmvgpdxkdjzeqkofqrhernemcxinjx\", \"nyqdwxpwlkansjqyymynldyrzttfbxonszkzb\", \"gfxlunvsqjethlkhudthqlojiev\", \"vwgjuvxicykmbdoebhigfaldjaxpwwlystdtfpodnnefmdvh\", \"kgyiktmppanabtjftmrnqnb\", \"sizhtphcshhvnuujzjtsoqfejxur\", \"tfigysajeftgxleadayhvjjcpzzhtylgwn\", \"cvsuwdchmoaiftzkrghaypoqqjwoobxx\", \"pbrsctlzxcgkbygwpzmuuubrkeewmyrohjsgvsnogmsbw\", \"yrrbzamztwvxyprrtnqenzwyjzworgrmttkpxwjapgoofv\", \"lvqrtrbvsagflcybnfmjxqmsgtgpancwpots\", \"exrruwdpnojyrqamktgwejxjw\", \"uhalgmfqpbinabtkuibgmbevjjcylgaljvqjbrhiopcs\", \"jocttcbggywscandevrgfqunvthfnittubhkfwwk\", \"angrxcbunqsywkdkvjzyyggkntoscvlmeuamvsykjmpnk\", \"rnhfxfogkgmgykcqkilrkkggizfhvdvkiloindwtzdg\", \"fwhewghjxilbaohltjswqoaloxiynljhrojad\", \"ghdjojppnrieilhcilbbctuvhfmxx\", \"cuqmsyyotaaundddlytmris\", \"nsegogbafugwangbtrzykipfnyqdhnfgadionjcrgctpuxo\", \"ksunliqajogosyqjqrmkqatbdj\", \"pgbzyujniiiupbbgzbwumlrumqmwmgbqfiostzjinsyjjthqse\", \"gfsozzstvrdzypxvottdwdro\", \"fjmiskykhdljykmqpyarmofe\", \"igusmtxelleenzxvrsrnuxdlwznrdsv\", \"upkpxkhsrvljxrdnvjjojzdpxuxblzjkogcignargyz\", \"qcvdfhxsleqbfqwawoakvykolalttulrhgvictzjelok\", \"ffxicqxobsdjtytcenytwjjsdmbsxukpwjelatnyzdkjb\", \"zmhownhwbqpqpymkxqdrncstbamioxjxicmndxcnnscvtum\", \"fhioqbheesumjlvijeeoygbsdomuxcjkkvubzcmfqfp\", \"bsqbbjkwuygwurjsmhidfoqojqxxwz\", \"ezyiadqaopnvkhmxumvoupwvwlswlppnnbhfgzgrddiz\", \"iscgxtcsvvlezfxkyqlpvsaxlnnybazdaoqww\", \"rexzbghfduxyvyfhbzwlinifrgyjjcwrjwlqvizodqzcc\", \"sdvyvpaiiikprmsmmxeelroyehtamiucfqwd\", \"mghbrymzmylbezkxpbnmuqdlzthcekvgszlkywjipb\", \"tsxxuagxihaldcmehoirztuxhqughslnislpwrshomdhi\", \"xkqdpionntevjceewvairpnlhrykgvqwzltqiugtaypdoy\", \"oqijquzvbqcqkfhkaadcqzjsuuhyqkxcebqlp\", \"sdekqdqzeylwyvjyytsioffdrnoprdygimpgaa\", \"ibxjsmutmnaxgfgawgncgznighwjgitlqoscwzp\", \"szlqwaphknhkjjyuqxltpjbjxjy\", \"oerwtfuijckcuuygxinjeocydvdgtqoziqxhgvfovxfw\", \"sjutqltgllbmrtytmrudraoefcwalvgnjtsotahfaipdmwjj\", \"wkuftetgiffbtsrzxuoblqici\"]\n\"i\"",
    "output": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.
 
Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Example 2:

Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.

Example 3:

Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
Output: []
Explanation: "z" does not occur in any of the words. Hence, we return an empty array.

 
Constraints:

1 <= words.length <= 50
1 <= words[i].length <= 50
x is a lowercase English letter.
words[i] consists only of lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
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
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, w in enumerate(words):
            if x in w:
                result.append(i)
        return result
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Generation 3</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Generation 4</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Generation 5</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, w in enumerate(words):
            if x in w:
                result.append(i)
        return result
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, w in enumerate(words):
            if x in w:
                result.append(i)
        return result
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, w in enumerate(words):
            if x in w:
                result.append(i)
        return result
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>full attempt 3</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>full attempt 4</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>full attempt 5</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, w in enumerate(words):
            if x in w:
                result.append(i)
        return result
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, w in enumerate(words):
            if x in w:
                result.append(i)
        return result
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
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
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.
 
Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Example 2:

Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.

Example 3:

Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
Output: []
Explanation: "z" does not occur in any of the words. Hence, we return an empty array.

 
Constraints:

1 <= words.length <= 50
1 <= words[i].length <= 50
x is a lowercase English letter.
words[i] consists only of lowercase English letters.

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
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
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
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
      "expected": "[0, 1]",
      "actual": "[0, 1]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[]",
      "actual": "[]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 2]",
      "actual": "[0, 2]",
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
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[2]",
      "actual": "[2]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "actual": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "actual": "[1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 36, 38, 40, 43, 44]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "actual": "[0, 1, 3, 4, 5, 6, 7, 8, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45]",
      "error": ""
    }
  ]
}
```

</details>
