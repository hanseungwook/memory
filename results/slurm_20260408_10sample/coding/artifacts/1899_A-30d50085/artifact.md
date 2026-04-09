# Problem 1899_A

- Domain: `coding`

## Problem

```text
Vanya and Vova are playing a game. Players are given an integer $n$. On their turn, the player can add $1$ to the current integer or subtract $1$. The players take turns; Vanya starts. If after Vanya's move the integer is divisible by $3$, then he wins. If $10$ moves have passed and Vanya has not won, then Vova wins.

Write a program that, based on the integer $n$, determines who will win if both players play optimally.

Input

The first line contains the integer $t$ ($1 \leq t \leq 100$) — the number of test cases.

The single line of each test case contains the integer $n$ ($1 \leq n \leq 1000$).

Output

For each test case, print "First" without quotes if Vanya wins, and "Second" without quotes if Vova wins.Sample Input 1:
6

1

3

5

100

999

1000



Sample Output 1:

First
Second
First
First
Second
First
```

### Test Cases

```json
[
  {
    "input": "6\n1\n3\n5\n100\n999\n1000\n",
    "output": "First\nSecond\nFirst\nFirst\nSecond\nFirst\n",
    "testtype": "stdin"
  },
  {
    "input": "1\n2\n",
    "output": "First\n",
    "testtype": "stdin"
  },
  {
    "input": "1\n994\n",
    "output": "First\n",
    "testtype": "stdin"
  },
  {
    "input": "1\n12\n",
    "output": "Second\n",
    "testtype": "stdin"
  },
  {
    "input": "10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n",
    "output": "First\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst",
    "testtype": "stdin"
  },
  {
    "input": "13\n3\n3\n3\n3\n3\n3\n3\n3\n3\n3\n3\n3\n1\n",
    "output": "Second\nSecond\nSecond\nSecond\nSecond\nSecond\nSecond\nSecond\nSecond\nSecond\nSecond\nSecond\nFirst\n",
    "testtype": "stdin"
  },
  {
    "input": "50\n100\n101\n102\n103\n104\n105\n106\n107\n108\n109\n110\n111\n112\n113\n114\n115\n116\n117\n118\n119\n120\n121\n122\n123\n124\n125\n126\n127\n128\n129\n130\n131\n132\n133\n134\n135\n136\n137\n138\n139\n140\n141\n142\n143\n144\n145\n146\n147\n148\n149\n",
    "output": "First\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst",
    "testtype": "stdin"
  },
  {
    "input": "60\n145\n146\n147\n148\n149\n150\n151\n152\n153\n154\n155\n156\n157\n158\n159\n160\n161\n162\n163\n164\n165\n166\n167\n168\n169\n170\n171\n172\n173\n174\n175\n176\n177\n178\n179\n180\n181\n182\n183\n184\n185\n186\n187\n188\n189\n190\n191\n192\n193\n194\n195\n196\n197\n198\n199\n200\n201\n202\n203\n204\n",
    "output": "First\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond",
    "testtype": "stdin"
  },
  {
    "input": "100\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n32\n33\n34\n35\n36\n37\n38\n39\n40\n41\n42\n43\n44\n45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55\n56\n57\n58\n59\n60\n61\n62\n63\n64\n65\n66\n67\n68\n69\n70\n71\n72\n73\n74\n75\n76\n77\n78\n79\n80\n81\n82\n83\n84\n85\n86\n87\n88\n89\n90\n91\n92\n93\n94\n95\n96\n97\n98\n99\n100\n101\n102\n103\n104\n105\n106\n107\n108\n109\n110\n",
    "output": "First\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst",
    "testtype": "stdin"
  },
  {
    "input": "100\n201\n202\n203\n204\n205\n206\n207\n208\n209\n210\n211\n212\n213\n214\n215\n216\n217\n218\n219\n220\n221\n222\n223\n224\n225\n226\n227\n228\n229\n230\n231\n232\n233\n234\n235\n236\n237\n238\n239\n240\n241\n242\n243\n244\n245\n246\n247\n248\n249\n250\n251\n252\n253\n254\n255\n256\n257\n258\n259\n260\n261\n262\n263\n264\n265\n266\n267\n268\n269\n270\n271\n272\n273\n274\n275\n276\n277\n278\n279\n280\n281\n282\n283\n284\n285\n286\n287\n288\n289\n290\n291\n292\n293\n294\n295\n296\n297\n298\n299\n300\n",
    "output": "Second\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond",
    "testtype": "stdin"
  },
  {
    "input": "100\n501\n502\n503\n504\n505\n506\n507\n508\n509\n510\n511\n512\n513\n514\n515\n516\n517\n518\n519\n520\n521\n522\n523\n524\n525\n526\n527\n528\n529\n530\n531\n532\n533\n534\n535\n536\n537\n538\n539\n540\n541\n542\n543\n544\n545\n546\n547\n548\n549\n550\n551\n552\n553\n554\n555\n556\n557\n558\n559\n560\n561\n562\n563\n564\n565\n566\n567\n568\n569\n570\n571\n572\n573\n574\n575\n576\n577\n578\n579\n580\n581\n582\n583\n584\n585\n586\n587\n588\n589\n590\n591\n592\n593\n594\n595\n596\n597\n598\n599\n600\n",
    "output": "Second\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond",
    "testtype": "stdin"
  },
  {
    "input": "100\n801\n802\n803\n804\n805\n806\n807\n808\n809\n810\n811\n812\n813\n814\n815\n816\n817\n818\n819\n820\n821\n822\n823\n824\n825\n826\n827\n828\n829\n830\n831\n832\n833\n834\n835\n836\n837\n838\n839\n840\n841\n842\n843\n844\n845\n846\n847\n848\n849\n850\n851\n852\n853\n854\n855\n856\n857\n858\n859\n860\n861\n862\n863\n864\n865\n866\n867\n868\n869\n870\n871\n872\n873\n874\n875\n876\n877\n878\n879\n880\n881\n882\n883\n884\n885\n886\n887\n888\n889\n890\n891\n892\n893\n894\n895\n896\n897\n898\n899\n900\n",
    "output": "Second\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond",
    "testtype": "stdin"
  },
  {
    "input": "100\n901\n902\n903\n904\n905\n906\n907\n908\n909\n910\n911\n912\n913\n914\n915\n916\n917\n918\n919\n920\n921\n922\n923\n924\n925\n926\n927\n928\n929\n930\n931\n932\n933\n934\n935\n936\n937\n938\n939\n940\n941\n942\n943\n944\n945\n946\n947\n948\n949\n950\n951\n952\n953\n954\n955\n956\n957\n958\n959\n960\n961\n962\n963\n964\n965\n966\n967\n968\n969\n970\n971\n972\n973\n974\n975\n976\n977\n978\n979\n980\n981\n982\n983\n984\n985\n986\n987\n988\n989\n990\n991\n992\n993\n994\n995\n996\n997\n998\n999\n1000\n",
    "output": "First\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst\nFirst\nSecond\nFirst",
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
Vanya and Vova are playing a game. Players are given an integer $n$. On their turn, the player can add $1$ to the current integer or subtract $1$. The players take turns; Vanya starts. If after Vanya's move the integer is divisible by $3$, then he wins. If $10$ moves have passed and Vanya has not won, then Vova wins.

Write a program that, based on the integer $n$, determines who will win if both players play optimally.

Input

The first line contains the integer $t$ ($1 \leq t \leq 100$) — the number of test cases.

The single line of each test case contains the integer $n$ ($1 \leq n \leq 1000$).

Output

For each test case, print "First" without quotes if Vanya wins, and "Second" without quotes if Vova wins.Sample Input 1:
6

1

3

5

100

999

1000



Sample Output 1:

First
Second
First
First
Second
First


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

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])

        # If Vanya can make it divisible by 3 within his first move (max 1 step),
        # he wins immediately.
        r = n % 3
        if r == 0:
            out.append("First")
            continue
        if r == 1:
            # n-1 is divisible by 3 (one move)
            out.append("First")
            continue
        # r == 2: n+1 is divisible by 3 (one move)
        out.append("First")

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

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        # Win condition after Vanya's move (1st,3rd,5th,... moves)
        # Vova wins if no one made divisible by 3 after 10 moves.
        # Vanya has 5 turns: moves 1,3,5,7,9 (0-indexed turns 0..4 for Vanya).
        # After k-th Vanya move, total moves = 2k+1, so net change from n has same parity as (2k+1).
        # Equivalent known solution: compare n mod 3 with move limit of 9 difference.
        r = n % 3
        # If n divisible by 3 => Vanya wins immediately.
        # Otherwise, Vanya can make it divisible by 3 within his 1st move if possible,
        # and in general within 5 turns, which reduces to:
        # If n mod 3 == 1 => Vanya wins unless n > 999? no, constraints small.
        # Standard result for this problem:
        # - If n % 3 == 0: First
        # - If n % 3 == 1: First only when n <= 100? Actually use direct optimal logic:
        #   Vanya needs to reach a multiple of 3 within at most 9 total moves for his 5th turn.
        #   Since players can shift by +/-1, optimal play gives:
        #   First wins iff the distance to nearest multiple of 3 is <= 9 and parity matches.
        #
        # But easiest robust method: minimax on remaining moves state with small horizon (10).
        #
        # State: current value mod 3 and whose turn, with move count.
        # Only mod 3 matters; with +/-1 changes mod 3 deterministically.
        #
        # We'll do DP for optimal play over 10 moves.

        # DP over turns: 0..9 moves have been made. Turn player is Vanya on even move numbers (0,2,4,6,8).
        # After Vanya move (when it's Vanya's turn and he moves), if divisible by 3 he wins immediately.
        # We'll compute from initial remainder only.
        rem0 = r
        # dp[move][rem][turn] where turn 0 means Vanya to move, 1 means Vova to move.
        # But move parity already gives turn; so just use move index.
        # We'll compute recursively with memo.
        from functools import lru_cache

        @lru_cache(None)
        def win(move, rem):
            # move: number of moves already made (0..10)
            # rem: current value mod 3 after those moves
            if move == 10:
                return False  # Vova wins
            turn_is_vanya = (move % 2 == 0)
            if turn_is_vanya:
                # Vanya chooses +/-1
                for delta in (-1, 1):
                    nrem = (rem + delta) % 3
                    if nrem == 0:
                        return True  # wins on this move
                    if win(move + 1, nrem):  # then Vova will play
                        return True
                return False
            else:
                # Vova tries to make Vanya lose
                for delta in (-1, 1):
                    nrem = (rem + delta) % 3
                    if not win(move + 1, nrem):
                        return False
                return True

        out.append("First" if win(0, rem0) else "Second")

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

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        # Vanya moves first. After each move, check divisibility by 3.
        # If Vanya can make (n +/- moves) divisible by 3 within his turns, he wins.
        # After 10 moves total, Vova wins if no one won; Vanya has moves 1,3,5,7,9.
        # So Vanya can win iff there exists an odd k in [1,9] such that
        # n +/- k is divisible by 3 => n mod 3 == (k mod 3) or (-k mod 3).
        # Equivalent: (k - n) % 3 == 0 or (-k - n) % 3 == 0 always reduces to
        # checking k ≡ n (mod 3) for +k, or k ≡ -n (mod 3) for -k.
        # We'll just simulate the reachable winning condition for Vanya's odd move counts.
        won = False
        mod = n % 3
        for k in [1, 3, 5, 7, 9]:
            if (k % 3) == mod:  # n + k divisible by 3
                won = True
                break
            if ((-k) % 3) == mod:  # n - k divisible by 3
                won = True
                break
        out.append("First" if won else "Second")
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

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        # Vanya can win on his move #1..5 (since Vova wins after 10 moves total,
        # and Vanya moves first: his moves are 1,3,5,7,9 => 5 opportunities)
        # Need (n + delta) % 3 == 0 after some Vanya move, where delta has parity
        # consistent with move count. Since Vanya and Vova both move by 1, after
        # k total moves the integer changes by +/- k relative to n.
        # A simple known solution: check if within 9 moves Vanya can reach multiple of 3
        # on his turn; equivalently compute minimal moves from n to nearest multiple of 3
        # and see if it is <= 9 and has same parity as Vanya's turn count.
        #
        # For each of Vanya's possible turn numbers: 1,3,5,7,9,
        # total change magnitude is that turn number, so reachable values after that
        # Vanya move are n + x where x has same parity as turn number and |x|<=turn.
        # We can just brute over those small options: for each Vanya move number m,
        # if exists d in [-m,m] with d%2==m%2 such that (n+d)%3==0 then First.
        #
        # This is fast since m<=9.
        first = False
        for m in (1, 3, 5, 7, 9):
            r = n % 3
            # Need (n + d) % 3 == 0 => d % 3 == (-r) % 3
            target = (-r) % 3
            # Enumerate possible d values with correct parity within [-m,m]
            for d in range(-m, m + 1):
                if (d & 1) == (m & 1) and (d % 3) == target:
                    first = True
                    break
            if first:
                break
        out.append("First" if first else "Second")
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

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        # After Vanya's move (move 1): integer becomes n + d where d in {-1, +1}
        # Vanya wins if n+d is divisible by 3.
        r = n % 3
        if r == 0:
            # Vanya can add 1 to make it 1 mod 3 (not divisible) or subtract 1 to make it 2 mod 3.
            # Wait: n % 3 == 0 => n-1 %3 == 2, n+1 %3 == 1, no option makes divisible.
            # So he cannot win on his first move.
            # Within 10 moves total (Vanya has 5 moves max), standard solution:
            # Vova wins when n % 3 == 0 and n >= 1.
            out.append("Second")
        else:
            # If n % 3 != 0, Vanya can always win on his first move by choosing ±1
            # to reach the next multiple of 3.
            out.append("First")
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

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        # Vanya wins in his move if (n ± 1) is divisible by 3
        # because the game starts with Vanya and checks after his move.
        if (n - 1) % 3 == 0 or (n + 1) % 3 == 0:
            out.append("First")
        else:
            out.append("Second")
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

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        # Vanya wins if he can make the number divisible by 3 on his move
        # within his move count (his moves are 1,3,5,7,9).
        # For k-th Vanya move, total moves passed = 2k-1, so modulo window:
        # require (n +/- d) divisible by 3 with d <= 2k-1 for some k in [1..5].
        # Equivalent: there exists m in {1,3,5,7,9} such that m >= d and parity matches.
        # Since we can reach any +/- distance, simply check minimal distance to a multiple of 3.
        r = n % 3
        if r == 0:
            out.append("First")
            continue
        # distance to nearest multiples of 3 is either 1 or 2
        d = r  # to go down to multiple of 3: subtract r (distance r)
        # But if r=1 => d=1; r=2 => d=2. We can also go up: distance 3-r.
        # However optimal player can choose direction, so minimal distance is min(r, 3-r)
        min_d = min(r, 3 - r)
        # Need to achieve divisible by 3 on one of Vanya's moves: move numbers {1,3,5,7,9}
        # That means required distance must be <= 9 and also feasible in step count:
        # Since he can choose +1 or -1 each move, reaching exact target after m moves
        # is possible iff m >= dist and (m - dist) is even.
        win = False
        for m in (1, 3, 5, 7, 9):
            # try both directions by checking exact distances 1 or 2
            for dist in (min_d, 3 - min_d):
                if dist <= m and (m - dist) % 2 == 0:
                    win = True
                    break
            if win:
                break
        out.append("First" if win else "Second")
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

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        # Vanya can win on his first move by reaching a multiple of 3.
        # The game ends after 10 moves total (Vanya moves 1st,3rd,5th,7th,9th).
        # Optimal play reduces to whether Vanya can reach a multiple of 3
        # within his available moves (at most 9 steps from start, on his 5th move).
        r = n % 3
        if r == 0:
            # Vanya moves first, so after 1 move: n±1 => not divisible by 3.
            # Check if he can make it divisible within his 5 moves (<=9 total steps).
            # For r==0, need +/-1 to reach r==2 or 1, then further; effectively
            # Vanya wins iff 1 + 1? Actually smallest winning distance from n
            # to nearest multiple of 3 is 1. But he can only win right after his move,
            # and after his move integer must be divisible by 3.
            # From n multiple of 3, Vanya can reach another multiple of 3 in 2 moves,
            # but he only moves every other turn. His first winning opportunity is on move 3
            # (after 3 total moves). Net change from start after 3 total moves is odd steps.
            # The known solution for this CF task: First wins iff n%3 != 0 or n>=? with 10 moves.
            # Let's implement the standard reachability for 5 Vanya moves:
            # He can add/subtract 1 each time, so positions after his k-th move are n + delta
            # with delta congruent to k (mod 2) and |delta| <= k. Need n+delta %3==0.
            possible = False
            for k in range(1, 10, 2):  # Vanya moves at total moves 1,3,5,7,9 => k=1,3,5,7,9
                # At his k-th move, he has made k steps from start (net delta parity = k).
                # He can reach any delta with same parity as k and abs(delta)<=k.
                # Check if there exists such delta such that (n+delta)%3==0.
                # We just brute over possible deltas within bounds (small up to 9).
                for delta in range(-k, k + 1, 2):
                    if (n + delta) % 3 == 0:
                        possible = True
                        break
                if possible:
                    break
            out.append("First" if possible else "Second")
        else:
            # General case: brute within Vanya's available moves (k=1,3,5,7,9)
            possible = False
            for k in range(1, 10, 2):
                for delta in range(-k, k + 1, 2):
                    if (n + delta) % 3 == 0:
                        possible = True
                        break
                if possible:
                    break
            out.append("First" if possible else "Second")

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

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        # Vanya wins if he can make number divisible by 3 in <= 10 moves.
        # On Vanya's k-th move (k=1..10), parity of moves doesn't matter; both players
        # could adjust similarly. With optimal play, this game reduces to:
        # If distance to nearest multiple of 3 is <= 10, then Vanya can force win.
        # More specifically, consider minimal d in {0,1,2} such that n+d or n-d divisible by 3.
        # Vanya has 10 moves total before Vova wins, but Vanya moves on odd-numbered turns;
        # still Vanya has 10 of his own moves? Actually total moves=10, starting with Vanya,
        # so Vanya moves on turns 1,3,5,7,9 => 5 moves max. However the statement says:
        # "If 10 moves have passed and Vanya has not won, then Vova wins."
        # That means Vova has made 5 moves and game ends right after Vova's 5th move,
        # so Vanya has exactly 5 moves.
        #
        # Hence Vanya can adjust by at most 5 (in absolute value) to reach a multiple of 3.
        # Minimal distance to multiple of 3 must be <= 5.
        r = n % 3
        # distances to nearest multiple in both directions:
        dist = 0 if r == 0 else min(r, 3 - r)
        out.append("First" if dist <= 5 else "Second")
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

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        # Vanya wins if he can reach a multiple of 3 in at most 5 moves (10 moves total, Vova moves at 10th)
        # Optimal play reduces to whether distance to nearest multiple of 3 is <= 5.
        r = n % 3
        if r == 0:
            out.append("First")
        else:
            # minimal moves to reach multiple of 3 by +/-1 each move
            # distance is r to go down (subtract r) or (3-r) to go up
            dist = min(r, 3 - r)
            out.append("First" if dist <= 5 else "Second")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```
```

</details>
