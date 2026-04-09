# Problem 3234

- Domain: `coding`

## Problem

```text
You are given a 0-indexed 2D array variables where variables[i] = [a_i, b_i, c_i, m_i], and an integer target.
An index i is good if the following formula holds:

0 <= i < variables.length
((a_i^bi % 10)^ci) % m_i == target

Return an array consisting of good indices in any order.
 
Example 1:

Input: variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
Output: [0,2]
Explanation: For each index i in the variables array:
1) For the index 0, variables[0] = [2,3,3,10], (2^3 % 10)^3 % 10 = 2.
2) For the index 1, variables[1] = [3,3,3,1], (3^3 % 10)^3 % 1 = 0.
3) For the index 2, variables[2] = [6,1,1,4], (6^1 % 10)^1 % 4 = 2.
Therefore we return [0,2] as the answer.

Example 2:

Input: variables = [[39,3,1000,1000]], target = 17
Output: []
Explanation: For each index i in the variables array:
1) For the index 0, variables[0] = [39,3,1000,1000], (39^3 % 10)^1000 % 1000 = 1.
Therefore we return [] as the answer.

 
Constraints:

1 <= variables.length <= 100
variables[i] == [a_i, b_i, c_i, m_i]
1 <= a_i, b_i, c_i, m_i <= 10^3
0 <= target <= 10^3
```

### Starter Code

```python
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
```

### Test Cases

```json
[
  {
    "input": "[[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]]\n2",
    "output": "[0, 2]",
    "testtype": "functional"
  },
  {
    "input": "[[39, 3, 1000, 1000]]\n17",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[2, 5, 6, 4]]\n2",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[5, 9, 8, 4]]\n8",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[1, 4, 10, 6]]\n7",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[10, 10, 4, 2]]\n8",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[364, 147, 701, 16]]\n316",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[999, 999, 999, 1000]]\n1",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[5, 5, 8, 1], [6, 8, 7, 4]]\n4",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[4, 8, 8, 3], [7, 6, 6, 10], [7, 4, 2, 4]]\n0",
    "output": "[0]",
    "testtype": "functional"
  },
  {
    "input": "[[90, 77, 32, 77], [54, 91, 34, 34], [87, 83, 23, 85], [8, 45, 35, 18], [60, 28, 10, 46], [49, 44, 66, 56], [38, 97, 93, 47], [34, 68, 12, 14], [42, 47, 82, 65], [26, 37, 54, 56], [98, 34, 13, 29], [55, 71, 29, 23], [68, 42, 96, 68], [79, 27, 31, 81], [39, 46, 53, 34], [18, 96, 68, 99], [93, 39, 17, 48], [91, 47, 14, 39], [49, 50, 47, 35], [75, 20, 14, 13], [17, 67, 40, 49], [89, 86, 100, 75], [91, 82, 97, 53], [15, 14, 72, 43], [32, 18, 76, 56], [17, 34, 92, 100], [69, 93, 4, 35], [27, 77, 11, 47], [83, 9, 83, 39], [33, 96, 5, 96], [71, 44, 54, 10], [90, 85, 17, 7], [35, 73, 12, 89], [59, 41, 90, 12], [44, 63, 82, 40]]\n0",
    "output": "[0, 4, 13, 31]",
    "testtype": "functional"
  },
  {
    "input": "[[33, 300, 912, 312], [792, 443, 105, 290], [921, 175, 577, 4], [39, 32, 864, 585], [561, 826, 929, 81], [710, 818, 578, 335], [305, 88, 828, 168], [3, 122, 21, 656], [300, 881, 553, 313], [642, 113, 644, 50], [9, 65, 580, 969], [522, 164, 113, 517], [508, 369, 227, 975], [276, 146, 203, 757], [429, 391, 18, 869], [393, 352, 730, 394], [811, 567, 433, 831], [715, 898, 736, 617], [181, 386, 575, 875], [104, 898, 193, 904], [248, 784, 578, 608], [323, 295, 768, 707], [839, 988, 345, 208], [996, 654, 295, 210], [175, 198, 997, 260], [504, 630, 624, 993], [640, 663, 873, 527], [86, 791, 846, 300], [241, 429, 295, 266], [202, 298, 415, 659], [883, 267, 113, 974], [183, 370, 981, 69], [463, 856, 509, 908], [734, 637, 665, 472], [166, 843, 842, 15], [620, 991, 629, 923], [897, 991, 763, 596], [440, 948, 778, 312], [543, 884, 79, 614], [338, 475, 999, 70], [713, 56, 916, 32], [451, 636, 304, 393], [307, 774, 867, 145], [844, 451, 697, 725], [702, 342, 43, 720], [611, 463, 661, 982], [27, 531, 740, 619], [367, 729, 608, 227], [467, 631, 934, 722], [767, 787, 660, 25], [21, 722, 761, 310], [103, 381, 970, 471], [212, 121, 21, 200], [665, 987, 783, 639], [192, 607, 448, 285], [914, 903, 63, 324], [120, 477, 140, 368], [489, 91, 371, 299], [372, 7, 494, 439], [684, 567, 77, 195], [906, 734, 722, 623], [27, 802, 248, 240], [761, 402, 946, 939], [72, 650, 515, 180], [112, 460, 483, 319], [988, 721, 345, 682], [81, 834, 971, 698], [730, 888, 807, 257], [913, 341, 538, 896], [505, 271, 779, 134], [105, 291, 587, 131], [267, 996, 321, 299], [225, 114, 485, 398], [850, 342, 349, 485], [401, 560, 6, 135], [110, 130, 425, 362], [88, 981, 55, 324], [985, 55, 763, 48], [695, 32, 258, 903], [100, 627, 521, 320], [599, 137, 661, 38], [496, 681, 371, 407], [100, 492, 114, 634], [951, 653, 159, 315], [564, 970, 296, 977], [86, 179, 643, 898], [639, 361, 408, 297], [523, 262, 585, 81], [676, 424, 429, 806], [887, 86, 438, 692], [643, 724, 126, 260], [965, 404, 164, 342], [463, 282, 656, 577], [254, 750, 77, 964], [958, 976, 975, 374], [435, 756, 313, 306], [547, 679, 883, 302]]\n882",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[293, 253, 113, 303], [459, 608, 249, 453], [586, 325, 72, 774], [74, 687, 168, 820], [229, 191, 329, 257], [187, 441, 423, 530], [422, 975, 298, 560], [695, 813, 942, 933], [662, 948, 690, 334], [981, 561, 101, 131], [815, 952, 324, 539], [159, 738, 558, 846], [755, 898, 772, 918], [513, 24, 985, 7], [13, 910, 433, 500], [211, 699, 902, 811], [856, 526, 62, 629], [254, 746, 555, 835], [55, 273, 568, 844], [712, 742, 532, 53], [229, 383, 871, 288], [838, 788, 49, 444], [864, 911, 898, 397], [128, 908, 902, 337], [168, 947, 147, 915], [933, 822, 805, 871], [299, 560, 888, 528], [640, 41, 771, 233], [97, 451, 425, 904], [447, 964, 615, 828], [299, 632, 122, 15], [450, 418, 975, 478], [245, 705, 315, 554], [57, 980, 387, 617], [52, 291, 683, 476], [207, 423, 758, 237], [612, 309, 310, 585], [228, 369, 332, 222], [475, 367, 105, 159], [878, 158, 413, 424], [69, 427, 139, 883], [339, 558, 952, 684], [326, 415, 389, 402], [992, 824, 842, 1000], [775, 350, 618, 430], [762, 162, 306, 62], [577, 538, 273, 418], [953, 891, 740, 287], [986, 357, 54, 170], [176, 347, 458, 294], [689, 384, 426, 93], [546, 510, 521, 34], [776, 738, 426, 621], [63, 443, 949, 525], [492, 629, 394, 136], [915, 163, 669, 143], [876, 750, 686, 865], [627, 276, 989, 436], [545, 197, 878, 801], [698, 761, 732, 454], [454, 805, 737, 209], [842, 792, 143, 571], [666, 452, 518, 587], [274, 238, 458, 452], [977, 986, 22, 778], [187, 170, 146, 525], [821, 357, 881, 257], [503, 109, 714, 493], [514, 147, 834, 125], [14, 835, 264, 894], [81, 522, 319, 222], [310, 184, 472, 306], [479, 409, 489, 481], [992, 640, 189, 739], [400, 349, 972, 284], [332, 771, 804, 12], [229, 928, 538, 219], [703, 956, 821, 33], [522, 527, 977, 408], [837, 756, 88, 353], [530, 324, 314, 87], [838, 90, 636, 923], [959, 7, 177, 174], [348, 204, 388, 136], [526, 269, 252, 436], [371, 496, 919, 939], [805, 419, 736, 983], [412, 908, 778, 488], [525, 851, 857, 502], [70, 83, 919, 201], [252, 529, 938, 269], [901, 633, 81, 513], [658, 566, 620, 332], [661, 698, 85, 909], [257, 102, 976, 533], [408, 747, 299, 955], [647, 164, 896, 540], [949, 368, 466, 472]]\n529",
    "output": "[]",
    "testtype": "functional"
  },
  {
    "input": "[[112, 859, 589, 203], [677, 525, 46, 676], [497, 98, 231, 611], [65, 338, 666, 795], [747, 291, 775, 228], [200, 230, 310, 686], [805, 609, 431, 851], [852, 775, 701, 605], [44, 620, 620, 773], [760, 592, 809, 173], [371, 857, 370, 145], [665, 46, 144, 542], [938, 22, 888, 824], [134, 635, 745, 450], [20, 497, 311, 75], [174, 575, 641, 86], [664, 235, 318, 235], [802, 770, 104, 60], [408, 577, 105, 387], [948, 817, 881, 252], [233, 855, 707, 232], [484, 897, 289, 256], [576, 121, 95, 343], [116, 513, 729, 281], [135, 703, 26, 539], [615, 834, 511, 371], [27, 138, 279, 299], [261, 521, 160, 376], [267, 440, 885, 452], [327, 290, 564, 355], [74, 420, 999, 47], [464, 266, 702, 939], [752, 144, 380, 808], [73, 827, 27, 132], [999, 641, 234, 439], [5, 605, 549, 218], [177, 902, 174, 681], [838, 871, 318, 646], [366, 853, 578, 730], [897, 388, 478, 118], [646, 872, 212, 346], [222, 187, 161, 79], [433, 271, 111, 728], [833, 68, 583, 1000], [479, 978, 882, 772], [359, 531, 144, 77], [39, 47, 914, 223], [106, 556, 347, 826], [940, 440, 29, 487], [66, 14, 291, 627], [704, 450, 291, 820], [357, 180, 410, 423], [307, 16, 602, 897], [526, 15, 820, 275], [48, 994, 963, 202], [531, 363, 168, 878], [187, 615, 945, 309], [633, 736, 518, 921], [129, 428, 786, 841], [744, 128, 360, 218], [343, 625, 610, 901], [801, 526, 781, 782], [118, 772, 429, 371], [590, 25, 162, 192], [494, 508, 24, 549], [14, 919, 799, 584], [336, 513, 414, 474], [884, 135, 891, 444], [695, 728, 3, 46], [176, 953, 760, 876], [716, 262, 131, 625], [639, 564, 223, 422], [973, 131, 445, 892], [793, 825, 239, 68], [15, 269, 225, 400], [353, 366, 739, 481], [464, 488, 389, 919], [117, 357, 523, 713], [97, 198, 422, 565], [181, 742, 981, 639], [746, 502, 43, 102], [815, 426, 537, 790], [906, 469, 136, 693], [979, 384, 734, 18], [696, 337, 61, 343], [815, 638, 340, 184], [823, 245, 24, 35], [966, 86, 944, 969], [216, 660, 454, 419], [908, 681, 870, 35], [289, 812, 889, 580], [188, 790, 33, 272], [326, 387, 280, 72], [128, 449, 107, 382], [238, 513, 919, 831], [270, 691, 431, 359], [532, 46, 79, 686], [230, 682, 403, 695], [151, 750, 443, 859], [139, 419, 715, 32]]\n975",
    "output": "[]",
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
You are given a 0-indexed 2D array variables where variables[i] = [a_i, b_i, c_i, m_i], and an integer target.
An index i is good if the following formula holds:

0 <= i < variables.length
((a_i^bi % 10)^ci) % m_i == target

Return an array consisting of good indices in any order.
 
Example 1:

Input: variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
Output: [0,2]
Explanation: For each index i in the variables array:
1) For the index 0, variables[0] = [2,3,3,10], (2^3 % 10)^3 % 10 = 2.
2) For the index 1, variables[1] = [3,3,3,1], (3^3 % 10)^3 % 1 = 0.
3) For the index 2, variables[2] = [6,1,1,4], (6^1 % 10)^1 % 4 = 2.
Therefore we return [0,2] as the answer.

Example 2:

Input: variables = [[39,3,1000,1000]], target = 17
Output: []
Explanation: For each index i in the variables array:
1) For the index 0, variables[0] = [39,3,1000,1000], (39^3 % 10)^1000 % 1000 = 1.
Therefore we return [] as the answer.

 
Constraints:

1 <= variables.length <= 100
variables[i] == [a_i, b_i, c_i, m_i]
1 <= a_i, b_i, c_i, m_i <= 10^3
0 <= target <= 10^3

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        good = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            x = pow(a, b, 10)          # a^b mod 10
            y = pow(x, c, m) if m != 1 else 0  # x^c mod m (handle m==1 quickly)
            if y == target:
                good.append(i)
        return good
```
```

</details>

<details>
<summary>Generation 2</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute: ((a^b % 10)^c) % m == target
            first = pow(a, b, 10)          # a^b mod 10
            second = pow(first, c, m)     # (first^c) mod m
            if second == target:
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # compute ((a^b % 10)^c) % m efficiently using pow with modulus
            x = pow(a, b, 10)          # a^b % 10
            y = pow(x, c, m)          # (x^c) % m
            if y == target:
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute (a^b % 10)^c % m using fast pow with mod
            first = pow(a, b, 10)          # a^b mod 10
            val = pow(first, c, m)        # (first)^c mod m
            if val == target:
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m safely using pow with modulus
            first = pow(a, b, 10)        # a^b mod 10
            second = pow(first, c, m)   # (first^c) mod m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Generation 6</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            first = pow(a, b, 10)          # a^b mod 10
            second = pow(first, c, m)    # (a^b mod 10)^c mod m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Generation 7</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        good = []
        for i, (a, b, c, m) in enumerate(variables):
            # ((a^b % 10)^c) % m == target
            first = pow(a, b, 10)          # a^b % 10
            second = pow(first, c, m)     # (a^b % 10)^c % m
            if second == target:
                good.append(i)
        return good
```
```

</details>

<details>
<summary>Generation 8</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Step 1: (a^b % 10)
            x = pow(a, b, 10)
            # Step 2: ((a^b % 10)^c) % m
            val = pow(x, c, m)
            if val == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Generation 9</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b mod 10)^c) mod m safely using pow with modulus
            first = pow(a, b, 10)          # a^b % 10
            second = pow(first, c, m)     # (first^c) % m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Generation 10</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            x = pow(a, b, 10)          # a^b mod 10
            y = pow(x, c, m)          # (x^c) mod m
            if y == target:
                ans.append(i)
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
  "passed": 14,
  "total": 14,
  "cases": [
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        good = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            x = pow(a, b, 10)          # a^b mod 10
            y = pow(x, c, m) if m != 1 else 0  # x^c mod m (handle m==1 quickly)
            if y == target:
                good.append(i)
        return good
```
```

</details>

<details>
<summary>full attempt 2</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute: ((a^b % 10)^c) % m == target
            first = pow(a, b, 10)          # a^b mod 10
            second = pow(first, c, m)     # (first^c) mod m
            if second == target:
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # compute ((a^b % 10)^c) % m efficiently using pow with modulus
            x = pow(a, b, 10)          # a^b % 10
            y = pow(x, c, m)          # (x^c) % m
            if y == target:
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute (a^b % 10)^c % m using fast pow with mod
            first = pow(a, b, 10)          # a^b mod 10
            val = pow(first, c, m)        # (first)^c mod m
            if val == target:
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m safely using pow with modulus
            first = pow(a, b, 10)        # a^b mod 10
            second = pow(first, c, m)   # (first^c) mod m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>full attempt 6</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            first = pow(a, b, 10)          # a^b mod 10
            second = pow(first, c, m)    # (a^b mod 10)^c mod m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>full attempt 7</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        good = []
        for i, (a, b, c, m) in enumerate(variables):
            # ((a^b % 10)^c) % m == target
            first = pow(a, b, 10)          # a^b % 10
            second = pow(first, c, m)     # (a^b % 10)^c % m
            if second == target:
                good.append(i)
        return good
```
```

</details>

<details>
<summary>full attempt 8</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Step 1: (a^b % 10)
            x = pow(a, b, 10)
            # Step 2: ((a^b % 10)^c) % m
            val = pow(x, c, m)
            if val == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>full attempt 9</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b mod 10)^c) mod m safely using pow with modulus
            first = pow(a, b, 10)          # a^b % 10
            second = pow(first, c, m)     # (first^c) % m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>full attempt 10</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            x = pow(a, b, 10)          # a^b mod 10
            y = pow(x, c, m)          # (x^c) mod m
            if y == target:
                ans.append(i)
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
You are given a 0-indexed 2D array variables where variables[i] = [a_i, b_i, c_i, m_i], and an integer target.
An index i is good if the following formula holds:

0 <= i < variables.length
((a_i^bi % 10)^ci) % m_i == target

Return an array consisting of good indices in any order.
 
Example 1:

Input: variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
Output: [0,2]
Explanation: For each index i in the variables array:
1) For the index 0, variables[0] = [2,3,3,10], (2^3 % 10)^3 % 10 = 2.
2) For the index 1, variables[1] = [3,3,3,1], (3^3 % 10)^3 % 1 = 0.
3) For the index 2, variables[2] = [6,1,1,4], (6^1 % 10)^1 % 4 = 2.
Therefore we return [0,2] as the answer.

Example 2:

Input: variables = [[39,3,1000,1000]], target = 17
Output: []
Explanation: For each index i in the variables array:
1) For the index 0, variables[0] = [39,3,1000,1000], (39^3 % 10)^1000 % 1000 = 1.
Therefore we return [] as the answer.

 
Constraints:

1 <= variables.length <= 100
variables[i] == [a_i, b_i, c_i, m_i]
1 <= a_i, b_i, c_i, m_i <= 10^3
0 <= target <= 10^3

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m efficiently using pow with modulo.
            x = pow(a, b, 10)          # a^b % 10
            y = pow(x, c, m)          # (x^c) % m
            if y == target:
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m efficiently using pow with modulus.
            first = pow(a, b, 10)          # a^b mod 10
            val = pow(first, c, m)        # (first^c) mod m
            if val == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b mod 10)^c mod m == target
            first = pow(a, b, 10)
            val = pow(first, c, m)
            if val == target:
                ans.append(i)
        return ans
```
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            first = pow(a, b, 10)          # a^b mod 10
            val = pow(first, c, m)        # (a^b mod 10)^c mod m
            if val == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m safely using Python pow with mod
            first = pow(a, b, 10)          # a^b % 10
            second = pow(first, c, m)     # (first^c) % m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # compute ((a^b % 10)^c) % m using modular exponentiation
            first = pow(a, b, 10)          # a^b mod 10
            second = pow(first, c, m)     # (first^c) mod m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m using pow with modular exponentiation
            x = pow(a, b, 10)     # a^b mod 10
            y = pow(x, c, m)      # (x^c) mod m
            if y == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            first = pow(a, b, 10)
            val = pow(first, c, m)
            if val == target:
                ans.append(i)
        return ans
```
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # ((a^b % 10)^c) % m == target
            first = pow(a, b, 10)          # a^b mod 10
            second = pow(first, c)        # (first^c) then mod m
            if m != 1:
                second %= m
            # If m == 1, result is always 0; handle via formula above too.
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m efficiently with pow(..., mod)
            x = pow(a, b, 10)          # a^b mod 10
            y = pow(x, c, m)          # (x^c) mod m
            if y == target:
                res.append(i)
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m efficiently using pow with modulo.
            x = pow(a, b, 10)          # a^b % 10
            y = pow(x, c, m)          # (x^c) % m
            if y == target:
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m efficiently using pow with modulus.
            first = pow(a, b, 10)          # a^b mod 10
            val = pow(first, c, m)        # (first^c) mod m
            if val == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b mod 10)^c mod m == target
            first = pow(a, b, 10)
            val = pow(first, c, m)
            if val == target:
                ans.append(i)
        return ans
```
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            first = pow(a, b, 10)          # a^b mod 10
            val = pow(first, c, m)        # (a^b mod 10)^c mod m
            if val == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m safely using Python pow with mod
            first = pow(a, b, 10)          # a^b % 10
            second = pow(first, c, m)     # (first^c) % m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # compute ((a^b % 10)^c) % m using modular exponentiation
            first = pow(a, b, 10)          # a^b mod 10
            second = pow(first, c, m)     # (first^c) mod m
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m using pow with modular exponentiation
            x = pow(a, b, 10)     # a^b mod 10
            y = pow(x, c, m)      # (x^c) mod m
            if y == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            # (a^b % 10)^c % m == target
            first = pow(a, b, 10)
            val = pow(first, c, m)
            if val == target:
                ans.append(i)
        return ans
```
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # ((a^b % 10)^c) % m == target
            first = pow(a, b, 10)          # a^b mod 10
            second = pow(first, c)        # (first^c) then mod m
            if m != 1:
                second %= m
            # If m == 1, result is always 0; handle via formula above too.
            if second == target:
                res.append(i)
        return res
```
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            # Compute ((a^b % 10)^c) % m efficiently with pow(..., mod)
            x = pow(a, b, 10)          # a^b mod 10
            y = pow(x, c, m)          # (x^c) mod m
            if y == target:
                res.append(i)
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
      "expected": "[0]",
      "actual": "[0]",
      "error": ""
    },
    {
      "passed": true,
      "expected": "[0, 4, 13, 31]",
      "actual": "[0, 4, 13, 31]",
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
    }
  ]
}
```

</details>
