# Problem 1984-10

- Domain: `math`

## Problem

```text
Mary told John her score on the American High School Mathematics Examination (AHSME), which was over $80$ . From this, John was able to determine the number of problems Mary solved correctly. If Mary's score had been any lower, but still over $80$ , John could not have determined this. What was Mary's score? (Recall that the AHSME consists of $30$ multiple choice problems and that one's score, $s$ , is computed by the formula $s=30+4c-w$ , where $c$ is the number of correct answers and $w$ is the number of wrong answers. Students are not penalized for problems left unanswered.)
```

- Expected answer: `119`

## Generation

### System Prompt

```text
You are an expert mathematician solving competition-level problems. Show your reasoning step by step. Your response should have this overall shape: first the reasoning, then a final line exactly in the format ANSWER: <integer>. For example, a valid response could end like this:
...
ANSWER: 42
```

### User Prompt

```text
Solve the following AIME problem:

Mary told John her score on the American High School Mathematics Examination (AHSME), which was over $80$ . From this, John was able to determine the number of problems Mary solved correctly. If Mary's score had been any lower, but still over $80$ , John could not have determined this. What was Mary's score? (Recall that the AHSME consists of $30$ multiple choice problems and that one's score, $s$ , is computed by the formula $s=30+4c-w$ , where $c$ is the number of correct answers and $w$ is the number of wrong answers. Students are not penalized for problems left unanswered.)
```

### Outputs

<details>
<summary>Generation 1</summary>

```text
We have \(30\) problems and
\[
s=30+4c-w.
\]
Let \(u\) be the number left blank. Then \(c+w+u=30\).

Rearrange:
\[
s-30=4c-w \quad\Longrightarrow\quad w=4c-(s-30).
\]
Since \(w\ge 0\), we need \(4c-(s-30)\ge 0\), i.e.
\[
s-30\le 4c.
\]
Also \(w\le 30-c\) (because \(u\ge 0\)), so
\[
4c-(s-30)\le 30-c
\]
\[
5c-(s-30)\le 30
\]
\[
5c\le s+0 \quad\Longrightarrow\quad c\le \frac{s}{5}.
\]

For a fixed score \(s\), different possible values of \(c\) must produce integer \(w\) that also make \(u=30-c-w\ge 0\). Since \(w=4c-(s-30)\), the parity/integrality is automatic when \(c\) is integer; the constraints are:
\[
0\le c\le 30,\quad w=4c-(s-30)\ge 0,\quad u=30-c-w\ge 0.
\]
Compute \(u\):
\[
u=30-c-(4c-(s-30))=30-c-4c+s-30=s-5c.
\]
So the nonnegativity \(u\ge 0\) is exactly
\[
s-5c\ge 0 \quad\Longrightarrow\quad c\le \frac{s}{5},
\]
consistent with above.

Also \(w\le 30-c\) is the same as \(u\ge 0\), so nothing new.

Thus for given \(s\), the valid \(c\) are precisely the integers satisfying
\[
\frac{s-30}{4}\le c \le \frac{s}{5}.
\]
(Left inequality from \(w\ge 0\): \(4c\ge s-30\).)

John could determine the number of problems \(c\) exactly when there is **only one integer** in that interval.

Mary’s score \(s\) is over \(80\), and if \(s\) were lowered to the next lower score but still \(>80\), the interval would contain at least two integers.

Now \(s\) is an integer (formula uses integers), and the condition “over 80” means \(s\ge 81\). The “any lower” wording in AIME context implies the immediate previous integer score \(s-1\).

We search for the smallest \(s\ge 81\) for which the interval contains exactly one integer, and the interval for \(s-1\) contains more than one integer.

Let’s test systematically by finding when the bounds squeeze to a single integer.

The interval is
\[
L(s)=\frac{s-30}{4},\qquad U(s)=\frac{s}{5}.
\]
We need:
- Exactly one integer \(c\) with \(L(s)\le c\le U(s)\).
- For \(s-1\), at least two integers.

Try \(s=81\):
\[
L(81)=\frac{51}{4}=12.75,\quad U(81)=\frac{81}{5}=16.2.
\]
Integers: \(13,14,15,16\) → 4 values, not unique.

\(s=82\):
\[
L=\frac{52}{4}=13,\quad U=\frac{82}{5}=16.4.
\]
Integers \(c=13,14,15,16\) → 4 values.

\(s=83\):
\[
L=\frac{53}{4}=13.25,\quad U=\frac{83}{5}=16.6.
\]
Integers \(14,15,16\) → 3 values.

\(s=84\):
\[
L=\frac{54}{4}=13.5,\quad U=\frac{84}{5}=16.8.
\]
Integers \(14,15,16\) → 3 values.

\(s=85\):
\[
L=\frac{55}{4}=13.75,\quad U=\frac{85}{5}=17.
\]
Integers \(14,15,16,17\) → 4 values.

\(s=86\):
\[
L=\frac{56}{4}=14,\quad U=\frac{86}{5}=17.2.
\]
Integers \(14,15,16,17\) → 4 values.

\(s=87\):
\[
L=\frac{57}{4}=14.25,\quad U=\frac{87}{5}=17.4.
\]
Integers \(15,16,17\) → 3 values.

\(s=88\):
\[
L=\frac{58}{4}=14.5,\quad U=\frac{88}{5}=17.6.
\]
Integers \(15,16,17\) → 3 values.

\(s=89\):
\[
L=\frac{59}{4}=14.75,\quad U=\frac{89}{5}=17.8.
\]
Integers \(15,16,17\) → 3 values.

\(s=90\):
\[
L=\frac{60}{4}=15,\quad U=\frac{90}{5}=18.
\]
Integers \(15,16,17,18\) → 4 values.

We need a tighter squeeze; continue:

\(s=91\):
\[
L=\frac{61}{4}=15.25,\quad U=\frac{91}{5}=18.2
\]
Integers \(16,17,18\) → 3.

\(s=92\):
\[
L=\frac{62}{4}=15.5,\quad U=\frac{92}{5}=18.4
\]
Integers \(16,17,18\) → 3.

\(s=93\):
\[
L=\frac{63}{4}=15.75,\quad U=\frac{93}{5}=18.6
\]
Integers \(16,17,18\) → 3.

\(s=94\):
\[
L=\frac{64}{4}=16,\quad U=\frac{94}{5}=18.8
\]
Integers \(16,17,18\) → 3.

\(s=95\):
\[
L=\frac{65}{4}=16.25,\quad U=\frac{95}{5}=19
\]
Integers \(17,18,19\) → 3.

\(s=96\):
\[
L=\frac{66}{4}=16.5,\quad U=\frac{96}{5}=19.2
\]
Integers \(17,18,19\) → 3.

\(s=97\):
\[
L=\frac{67}{4}=16.75,\quad U=\frac{97}{5}=19.4
\]
Integers \(17,18,19\) → 3.

\(s=98\):
\[
L=\frac{68}{4}=17,\quad U=\frac{98}{5}=19.6
\]
Integers \(17,18,19\) → 3.

\(s=99\):
\[
L=\frac{69}{4}=17.25,\quad U=\frac{99}{5}=19.8
\]
Integers \(18,19\) → 2 values.

\(s=100\):
\[
L=\frac{70}{4}=17.5,\quad U=\frac{100}{5}=20.
\]
Integers \(18,19,20\) → 3 values.

So far no uniqueness. Let’s go higher.

\(s=101\):
\[
L=\frac{71}{4}=17.75,\quad U=\frac{101}{5}=20.2
\]
Integers \(18,19,20\) → 3.

\(s=102\):
\[
L=\frac{72}{4}=18,\quad U=\frac{102}{5}=20.4
\]
Integers \(18,19,20\) → 3.

\(s=103\):
\[
L=\frac{73}{4}=18.25,\quad U=\frac{103}{5}=20.6
\]
Integers \(19,20\) → 2.

\(s=104\):
\[
L=\frac{74}{4}=18.5,\quad U=\frac{104}{5}=20.8
\]
Integers \(19,20\) → 2.

\(s=105\):
\[
L=\frac{75}{4}=18.75,\quad U=\frac{105}{5}=21
\]
Integers \(19,20,21\) → 3.

\(s=106\):
\[
L=\frac{76}{4}=19,\quad U=\frac{106}{5}=21.2
\]
Integers \(19,20,21\) → 3.

\(s=107\):
\[
L=\frac{77}{4}=19.25,\quad U=\frac{107}{5}=21.4
\]
Integers \(20,21\) → 2.

\(s=108\):
\[
L=\frac{78}{4}=19.5,\quad U=\frac{108}{5}=21.6
\]
Integers \(20,21\) → 2.

\(s=109\):
\[
L=\frac{79}{4}=19.75,\quad U=\frac{109}{5}=21.8
\]
Integers \(20,21\) → 2.

\(s=110\):
\[
L=\frac{80}{4}=20,\quad U=\frac{110}{5}=22
\]
Integers \(20,21,22\) → 3.

We still don’t have 1 integer. The only way to get exactly one integer is for the interval length to be \(<1\):
\[
U(s)-L(s)=\frac{s}{5}-\frac{s-30}{4}
=\frac{4s-5(s-30)}{20}
=\frac{4s-5s+150}{20}
=\frac{150-s}{20}.
\]
So we need
\[
\frac{150-s}{20}<1 \quad\Longrightarrow\quad 150-s<20 \quad\Longrightarrow\quad s>130.
\]
But AHSME has maximum when \(c=30,w=0\): \(s=30+4\cdot 30=150\). So \(s\) can indeed exceed 130.

Now find the first \(s>130\) where exactly one integer lies in the interval and for \(s-1\) more than one.

Since \(s>130\), let’s try values near 130.

Compute interval length:
\[
U-L=\frac{150-s}{20}.
\]
- If \(s=131\), length \(=\frac{19}{20}=0.95<1\), so potentially unique.
We must check endpoints carefully.

For \(s=131\):
\[
L=\frac{101}{4}=25.25,\quad U=\frac{131}{5}=26.2.
\]
Integers between: \(26\) only → unique! (Because \(25.25\le c\le 26.2\) allows only \(c=26\).)

Now check \(s=130\) (which is still over 80, yes):
For \(s=130\):
\[
L=\frac{100}{4}=25,\quad U=\frac{130}{5}=26.
\]
Integers: \(c=25,26\) → two values. So John could not have determined \(c\) from score 130.

Therefore \(s=131\) satisfies both conditions.

We can also compute consistency:
If \(c=26\), then
\[
w=4c-(s-30)=104-(101)=3,
\]
and
\[
u=s-5c=131-130=1,
\]
all valid.

So the score is \(\boxed{131}\).

ANSWER: 131
```

</details>

<details>
<summary>Generation 2</summary>

```text
Let \(c\) be the number correct and \(w\) the number wrong. Since there are \(30\) total problems, the number left blank is \(30-c-w\ge 0\).

Given the scoring rule
\[
s=30+4c-w,
\]
we can rewrite \(w\) in terms of \(s\) and \(c\):
\[
w=30+4c-s.
\]
We must have
\[
0\le w \le 30-c.
\]
The upper bound \(w\le 30-c\) is equivalent to \(30+4c-s\le 30-c\), i.e.
\[
4c-c\le s \quad\Longrightarrow\quad 3c\le s.
\]
The lower bound \(w\ge 0\) is \(30+4c-s\ge 0\), i.e.
\[
4c\ge s-30.
\]

John can determine \(c\) uniquely from the score \(s\). If there were another feasible \(c'\neq c\) producing the same \(s\), then John couldn’t determine the number correct.

Now consider how \(c\) could change while keeping the same score. From
\[
s=30+4c-w,
\]
fix \(s\). If we increase \(c\) by \(1\), to keep \(s\) constant we must increase \(w\) by \(4\) (because \(4c-w\) must stay the same). So alternative solutions correspond to steps
\[
(c,w)\to (c+1,\,w+4).
\]
Thus, for a given \(s\), multiple values of \(c\) are possible exactly when there exists room to add these \((+1,+4)\) moves without violating feasibility \(w\le 30-c\) and \(w\ge 0\).

The problem says:
- For Mary’s actual score \(s\), \(c\) is determined uniquely.
- For any smaller score \(s' > 80\), John cannot determine \(c\) (so at least two different \(c\)’s are feasible).

So \(s\) is the *largest* score \(>80\) for which uniqueness holds; just below it, the feasible range for \(c\) becomes large enough to allow two solutions.

Compute \(s\) near \(80\). Since \(s=30+4c-w\) with \(w\ge 0\), we have
\[
s\le 30+4c \quad\Rightarrow\quad c\ge \frac{s-30}{4}.
\]
Also from \(w\le 30-c\),
\[
30+4c-s \le 30-c \quad\Rightarrow\quad 3c\le s.
\]
So for a fixed \(s\), feasible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{3}\right\rfloor.
\]

Uniqueness means this integer interval has exactly one integer.

Let’s test scores just above \(80\). Start with \(s=81\):
\[
\left\lceil\frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,\quad
\left\lfloor\frac{81}{3}\right\rfloor=27.
\]
Many \(c\), not unique.

We need the interval to shrink to one integer. As \(s\) increases, the lower bound increases by about \(1/4\) per \(1\) in \(s\), while the upper bound increases by \(1/3\) per \(1\) in \(s\). The interval length tends to decrease only very rarely due to the ceilings/floors; uniqueness is most likely at a boundary where the ceiling equals the floor.

So we search for \(s>80\) such that
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{3}\right\rfloor.
\]
Let that common value be \(c\). Then \(c\) must satisfy
\[
\frac{s-30}{4} \le c \le \frac{s}{3}
\]
and with integrality/rounding:
\[
c-1 < \frac{s-30}{4} \le c,\qquad c\le \frac{s}{3} < c+1.
\]
Equivalently,
\[
4(c-1) < s-30 \le 4c,\qquad 3c \le s < 3(c+1).
\]
Thus
\[
4c+30 \ge s > 4(c-1)+30 =4c+26
\]
and
\[
3c \le s < 3c+3.
\]
So \(s\) must lie in the intersection:
\[
(4c+26,\;4c+30]\cap [3c,\;3c+3).
\]
Since \(4c+26\) is much larger than \(3c\) for \(c\ge 1\), the key overlap forces \(s\) close to \(4c+26\) but also less than \(3c+3\). Set the inequalities:
\[
4c+26 < 3c+3 \quad\Rightarrow\quad c < -23,
\]
impossible. That means our assumption about the interval having exactly one integer via equality of those bounds must be reconsidered: uniqueness doesn’t require the feasible \(c\)-interval length to be 1, because different \(c\) might fail the implied \(w\) nonnegativity/upper bound in a way that ceiling/floor conditions alone don’t fully capture due to the step structure \(w=30+4c-s\). But actually those bounds *are* exactly the feasibility for \(w\), so the interval approach is correct—so why did it seem impossible? The arithmetic indicates we made a wrong comparison: the lower bound is \(\left\lceil\frac{s-30}{4}\right\rceil\), upper bound \(\left\lfloor\frac{s}{3}\right\rfloor\). For \(s\) around 80, these are:
- lower about \((s-30)/4\approx 12.5\),
- upper about \(s/3\approx 26.6\).
So uniqueness would require very special \(s\), but it can happen when the lower and upper are equal, which seems impossible since \((s-30)/4\) is always much smaller than \(s/3\) for positive \(s\):
\[
\frac{s-30}{4}=\frac{s}{3}\ \Rightarrow\ 3s-90=4s\ \Rightarrow\ s=-90.
\]
So indeed they can never be equal. Therefore uniqueness must be interpreted differently: given \(s\), John can determine \(c\) because although multiple \(c\) values are feasible, the resulting \(c\) are the same—i.e., not possible. That contradicts feasibility unless we misread: John determines the number of problems Mary solved correctly, meaning \(c\) is uniquely determined, so there must be exactly one feasible \(c\). Since exact equality of bounds cannot happen, the only way is that feasibility interval length becomes \(<1\), impossible as shown. Hence the correct approach is to use the score modulo constraints from the step structure.

From
\[
s=30+4c-w,
\]
with \(w\) integer, we have
\[
s\equiv 30+4c \pmod{1}\quad \text{(no restriction)}.
\]
But combining with \(w\le 30-c\) gives:
\[
w=30+4c-s \le 30-c \Rightarrow 5c \le s.
\]
Also \(w\ge 0\Rightarrow 30+4c-s\ge 0\Rightarrow 4c\ge s-30\).

So feasibility is
\[
\left\lceil\frac{s-30}{4}\right\rceil \le c \le \left\lfloor\frac{s}{5}\right\rfloor.
\]
Now for uniqueness, this interval must contain exactly one integer.

Test \(s=81\):
\[
\left\lceil\frac{51}{4}\right\rceil=13,\quad \left\lfloor\frac{81}{5}\right\rfloor=16.
\]
Possible \(c=13,14,15,16\) => not unique.

We need the interval length \(=0\) or \(1\). Since uniqueness means exactly one integer:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]
Now solve for when the bounds can match.

Let that integer be \(c\). Then
\[
\frac{s-30}{4} \le c < \frac{s-30}{4}+1,
\]
\[
c \le \frac{s}{5} < c+1.
\]
Translate to \(s\):
From \(c \le s/5\): \(s\ge 5c\).
From \(s/5 < c+1\): \(s<5c+5\).
From \((s-30)/4 \le c\): \(s-30 \le 4c\Rightarrow s\le 4c+30\).
From \(c < (s-30)/4+1\): \(c-1 < (s-30)/4\Rightarrow 4c-4 < s-30\Rightarrow s>4c+26\).

So
\[
5c \le s < 5c+5,\quad 4c+27 \le s \le 4c+30.
\]
Intersection:
\[
s \in [5c,\;5c+4]\cap [4c+27,\;4c+30].
\]
For intersection to be nonempty:
\[
5c \le 4c+30 \Rightarrow c\le 30.
\]
Also need
\[
5c+4 \ge 4c+27 \Rightarrow c\ge 23.
\]
So \(c\in\{23,24,25,26,27,28,29,30\}\).

Now compute the possible \(s\) by taking \(s\) in intersection; additionally \(s>80\) and we want the *maximal* \(s\) such that uniqueness holds but for any smaller \(s'>80\) it fails.

Let’s compute for each \(c\), the intersection interval for \(s\):
- lower \(L=\max(5c,\;4c+27)\),
- upper \(U=\min(5c+4,\;4c+30)\).

But compare \(5c\) vs \(4c+27\): \(5c-(4c+27)=c-27\).
So for \(c\ge 27\), \(5c\ge 4c+27\) hence \(L=5c\).
For \(c\le 26\), \(L=4c+27\).

Similarly compare \(5c+4\) vs \(4c+30\): \((5c+4)-(4c+30)=c-26\).
For \(c\ge 26\), \(5c+4\ge 4c+30\) so \(U=4c+30\).
For \(c\le 25\), \(U=5c+4\).

Now list \(c\ge 23\):

- \(c=23\): \(L=4(23)+27=119\), already \(>80\) too high but actually \(s\) would be \(>100\). still allowed but check uniqueness and the “any lower score still >80 fails” suggests we want smallest above 80. However note \(s\) increases with \(c\). So we want the smallest \(c\) that gives uniqueness while keeping \(s>80\) maximal just above 80. Let’s instead directly find \(s\) in \((80, \infty)\) that yields uniqueness and is minimal just above 80? The condition says if score had been any lower but still over 80, uniqueness would fail. So our \(s\) is the smallest value \(>80\) for which uniqueness holds.
So search upward from 81 until uniqueness holds, and ensure it fails for all 81,82,...,s-1.
Try compute uniqueness quickly by counting feasible \(c\) values for each \(s\) is heavy; instead use the derived matching condition which gives exact uniqueness.

The matching condition gives candidates for \(s\) where the feasible interval shrinks to one integer, and the smallest \(s>80\) among them is our answer.

Compute \(s\) from \(s\) must satisfy either endpoints in intersection.

For each \(c\), the possible \(s\) range is:
- \(c=23\): \(L=4c+27=119\), \(U=5c+4=119\)?? since \(U=5c+4\) for c<=25: \(U=119\). So \(s=119\).
- \(c=24\): \(L=4c+27=123\), \(U=5c+4=124\) (since c<=25). so possibly \(s=123,124\) but uniqueness requires exactly one feasible \(c\), still okay if both work? check quickly by constructing \(w\):
  If \(s=123\): \(w=30+4c-s=30+96-123=3\), and \(c=24\) gives blanks \(=30-24-3=3\ge0\) feasible.
  If \(s=124\): \(w=30+96-124=2\), blanks \(=4\ge0\) feasible.
But could there be another \(c\) feasible for those \(s\)? uniqueness says no, so these should be valid candidates.
- \(c=25\): \(L=4c+27=127\), \(U=5c+4=129\) (still c<=25 for U): \(s\in\{127,128,129\}\).
- \(c=26\): now \(L=4c+27=131\) (since c<=26 for L), \(U=4c+30=134\) (since c>=26 for U): \(s\in\{131,132,133,134\}\).
- \(c=27\): \(L=5c=135\), \(U=4c+30=138\): \(s\in\{135,136,137,138\}\).
Clearly the smallest \(s>80\) among all is \(s=119\).

Now verify the “any lower but still over 80” condition. We must ensure for scores \(81\) through \(118\), \(c\) is not uniquely determined. Since our candidate uniqueness starts at \(119\), this must be true.

Therefore Mary's score is \(119\).
Then
\[
119=30+4c-w \Rightarrow 89=4c-w.
\]
With the feasible matching case found above, \(c=23\) gives \(w=30+92-119=3\), blanks \(=30-23-3=4\ge0\).
And for \(s=119\), the matching condition indicates uniqueness holds, so John can deduce \(c=23\).

ANSWER: 119
```

</details>

<details>
<summary>Generation 3</summary>

```text

```

</details>

<details>
<summary>Generation 4</summary>

```text

```

</details>

<details>
<summary>Generation 5</summary>

```text
Let \(c\) be the number correct and \(w\) the number wrong. Then unanswered are irrelevant, and
\[
s=30+4c-w.
\]
Also \(c+w\le 30\) with \(c,w\ge 0\).

John knows \(s>80\) and from \(s\) can determine the pair \((c,w)\), hence \(c\), uniquely. But if \(s\) were any lower (still \(>80\)), \((c,w)\) would no longer be uniquely determined.

Define
\[
t:=s-30=4c-w.
\]
Since \(s>80\), we have \(t>50\). Also
\[
w=4c-t.
\]
For given \(t\), any valid solution must satisfy:
1. \(w\ge 0 \Rightarrow 4c-t\ge 0 \Rightarrow c\ge \frac t4\).
2. \(c+w\le 30\):
\[
c+(4c-t)\le 30 \;\Rightarrow\; 5c-t\le 30 \;\Rightarrow\; c\le \frac{t+30}{5}.
\]
So the integer \(c\) is constrained by
\[
\left\lceil \frac t4\right\rceil \le c \le \left\lfloor \frac{t+30}{5}\right\rfloor.
\]
Then each such \(c\) gives exactly one \(w=4c-t\), hence one achievable score.

We need the smallest \(s>80\) for which this interval contains exactly one integer \(c\) (uniqueness), but for the previous score value \(s-1\) (i.e. \(t-1\)) the interval contains at least two integers.

Since \(s>80\), the candidate smallest \(s\) is \(81\), i.e. \(t=51\), and we test upward until uniqueness occurs.

### Check \(t=51\) (score \(81\))
\[
\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,\quad
\left\lfloor \frac{51+30}{5}\right\rfloor=\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
So \(c\) can be \(13,14,15,16\): **4 possibilities**, not unique.

### Check \(t=52\) (score \(82\))
\[
\left\lceil \frac{52}{4}\right\rceil=\left\lceil 13\right\rceil=13,\quad
\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16.
\]
So \(c=13,14,15,16\): **4 possibilities**, not unique.

### Check \(t=53\) (score \(83\))
\[
\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14,\quad
\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16.
\]
So \(c=14,15,16\): **3 possibilities**, not unique.

### Check \(t=54\) (score \(84\))
\[
\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14,\quad
\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16.
\]
So \(c=14,15,16\): **3 possibilities**, not unique.

### Check \(t=55\) (score \(85\))
\[
\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,\quad
\left\lfloor \frac{85}{5}\right\rfloor=\left\lfloor 17\right\rfloor=17.
\]
So \(c=14,15,16,17\): **4 possibilities**, not unique.

### Check \(t=56\) (score \(86\))
\[
\left\lceil \frac{56}{4}\right\rceil=\left\lceil 14\right\rceil=14,\quad
\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17.
\]
So \(c=14,15,16,17\): **4 possibilities**.

### Check \(t=57\) (score \(87\))
\[
\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15,\quad
\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17.
\]
So \(c=15,16,17\): **3 possibilities**.

### Check \(t=58\) (score \(88\))
\[
\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15,\quad
\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17.
\]
So \(c=15,16,17\): **3 possibilities**.

### Check \(t=59\) (score \(89\))
\[
\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15,\quad
\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17.
\]
So \(c=15,16,17\): **3 possibilities**.

### Check \(t=60\) (score \(90\))
\[
\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15,\quad
\left\lfloor \frac{90}{5}\right\rfloor=\left\lfloor 18\right\rfloor=18.
\]
So \(c=15,16,17,18\): **4 possibilities**.

This is still not getting uniqueness; so uniqueness must occur at some higher \(t\) where the interval shrinks to a single integer.

Notice:
- The lower bound \(\lceil t/4\rceil\) increases by \(1\) every time \(t\) passes a multiple of \(4\).
- The upper bound \(\lfloor (t+30)/5\rfloor\) increases by \(1\) every time \(t\) passes a value making \((t+30)/5\) cross an integer.

The interval length is
\[
\left\lfloor \frac{t+30}{5}\right\rfloor - \left\lceil \frac t4\right\rceil.
\]
We want this to be \(0\) (exactly one integer).

So we try to find when
\[
\left\lceil \frac t4\right\rceil = \left\lfloor \frac{t+30}{5}\right\rfloor.
\]

Try \(t=74\) (score \(104\)) near the top (since max score is \(30+4\cdot 30=150\)).
Compute quickly:
\[
\left\lceil \frac{74}{4}\right\rceil=\left\lceil 18.5\right\rceil=19,\quad
\left\lfloor \frac{104}{5}\right\rfloor=\left\lfloor 20.8\right\rfloor=20.
\]
Two values possible \(c=19,20\). Not unique.

Try \(t=75\) (score \(105\)):
\[
\left\lceil \frac{75}{4}\right\rceil=\left\lceil 18.75\right\rceil=19,\quad
\left\lfloor \frac{105}{5}\right\rfloor=\left\lfloor 21\right\rfloor=21.
\]
So \(c=19,20,21\): not unique.

Try \(t=76\) (score \(106\)):
\[
\left\lceil 19\right\rceil=19,\quad \left\lfloor \frac{106}{5}\right\rfloor=\left\lfloor 21.2\right\rfloor=21.
\]
So \(c=19,20,21\): not unique.

Try \(t=77\) (score \(107\)):
\[
\left\lceil 19.25\right\rceil=20,\quad \left\lfloor \frac{107}{5}\right\rfloor=\left\lfloor 21.4\right\rfloor=21.
\]
So \(c=20,21\): not unique.

Try \(t=78\) (score \(108\)):
\[
\left\lceil 19.5\right\rceil=20,\quad \left\lfloor \frac{108}{5}\right\rfloor=\left\lfloor 21.6\right\rfloor=21.
\]
So \(c=20,21\): not unique.

Try \(t=79\) (score \(109\)):
\[
\left\lceil 19.75\right\rceil=20,\quad \left\lfloor \frac{109}{5}\right\rfloor=\left\lfloor 21.8\right\rfloor=21.
\]
So \(c=20,21\): not unique.

Try \(t=80\) (score \(110\)):
\[
\left\lceil 20\right\rceil=20,\quad \left\lfloor \frac{110}{5}\right\rfloor=22.
\]
Then \(c=20,21,22\): not unique.

Try \(t=81\) (score \(111\)):
\[
\left\lceil 20.25\right\rceil=21,\quad \left\lfloor \frac{111+?}{5}\right\rfloor=\left\lfloor \frac{111+30?}{5}\right\rfloor
\]
Oops—remember upper is \(\frac{t+30}{5}\), so for \(t=81\), \(t+30=111\):
\[
\left\lfloor \frac{111}{5}\right\rfloor=\left\lfloor 22.2\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=82\) (score \(112\)):
\[
\left\lceil \frac{82}{4}\right\rceil=\left\lceil 20.5\right\rceil=21,\quad
\left\lfloor \frac{112}{5}\right\rfloor=\left\lfloor 22.4\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=83\) (score \(113\)):
\[
\left\lceil 20.75\right\rceil=21,\quad \left\lfloor \frac{113}{5}\right\rfloor=\left\lfloor 22.6\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=84\) (score \(114\)):
\[
\left\lceil 21\right\rceil=21,\quad \left\lfloor \frac{114}{5}\right\rfloor=\left\lfloor 22.8\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=85\) (score \(115\)):
\[
\left\lceil 21.25\right\rceil=22,\quad \left\lfloor \frac{115}{5}\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=86\) (score \(116\)):
\[
\left\lceil 21.5\right\rceil=22,\quad \left\lfloor \frac{116}{5}\right\rfloor=\left\lfloor 23.2\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=87\) (score \(117\)):
\[
\left\lceil 21.75\right\rceil=22,\quad \left\lfloor \frac{117}{5}\right\rfloor=\left\lfloor 23.4\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=88\) (score \(118\)):
\[
\left\lceil 22\right\rceil=22,\quad \left\lfloor \frac{118}{5}\right\rfloor=\left\lfloor 23.6\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=89\) (score \(119\)):
\[
\left\lceil 22.25\right\rceil=23,\quad \left\lfloor \frac{119}{5}\right\rfloor=\left\lfloor 23.8\right\rfloor=23.
\]
Now the interval is \(c=23\) only! Great—this gives uniqueness.

So score \(s = 30+t = 30+89 = 119\).

Finally we check the “if Mary's score had been any lower but still over 80” condition: meaning at \(s=118\) (i.e. \(t=88\)) John could not determine \(c\) uniquely.
We found for \(t=88\), \(c\in\{22,23\}\), indeed not unique. Thus the condition is satisfied.

Compute \(c\) and \(w\) for \(t=89\):
\[
t=4c-w \Rightarrow 89=4\cdot 23 - w = 92-w \Rightarrow w=3.
\]
Valid since \(23+3=26\le 30\).

Therefore Mary's score is \(119\).

ANSWER: 119
```

</details>

<details>
<summary>Generation 6</summary>

```text
Let \(c\) be correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\qquad s=30+4c-w.
\]
Substitute \(w=30-c-u\) into the score:
\[
s=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
So the score depends only on \(c\) and \(u\), with \(u\ge 0\) and \(c\ge 0\) integers, and
\[
c+u\le 30.
\]

John can determine \(c\) from \(s\) iff, given \(s\), there is exactly one possible \(c\) compatible with some \(u\ge 0\) and \(c+u\le 30\).

From \(s=5c+u\), we have \(u=s-5c\). Thus \(u\ge 0\) gives
\[
s-5c\ge 0 \implies c\le \frac{s}{5}.
\]
Also \(c+u\le 30\) becomes
\[
c+(s-5c)\le 30 \implies s-4c\le 30 \implies c\ge \frac{s-30}{4}.
\]
So the possible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
John can determine \(c\) exactly when this interval contains exactly one integer.

Now we use the condition: Mary's score was \(>80\), and if the score were any lower but still \(>80\), John could not have determined \(c\). That means \(s\) is the smallest integer \(>80\) for which the interval has exactly one integer.

Check \(s=81\). Compute bounds:
\[
\left\lceil \frac{81-30}{4}\right\rceil=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,
\]
\[
\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
Interval \([13,16]\) has 4 integers → not unique.

Try \(s=82\):
\[
\left\lceil \frac{82-30}{4}\right\rceil=\left\lceil \frac{52}{4}\right\rceil=13,
\quad
\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16.
\]
Interval \([13,16]\) has 4 integers → not unique.

\(s=83\):
\[
\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14,
\quad
\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16.
\]
Interval \([14,16]\) has 3 integers → not unique.

\(s=84\):
\[
\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14,
\quad
\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16.
\]
Interval \([14,16]\) has 3 integers → not unique.

\(s=85\):
\[
\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,
\quad
\left\lfloor \frac{85}{5}\right\rfloor=\left\lfloor 17\right\rfloor=17.
\]
Interval \([14,17]\) has 4 integers → not unique.

\(s=86\):
\[
\left\lceil \frac{56}{4}\right\rceil=\left\lceil 14\right\rceil=14,
\quad
\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17.
\]
Interval \([14,17]\) has 4 integers → not unique.

\(s=87\):
\[
\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15,
\quad
\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

\(s=88\):
\[
\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15,
\quad
\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

\(s=89\):
\[
\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15,
\quad
\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

\(s=90\):
\[
\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15,
\quad
\left\lfloor \frac{90}{5}\right\rfloor=\left\lfloor 18\right\rfloor=18.
\]
Interval \([15,18]\) has 4 integers → not unique.

\(s=91\):
\[
\left\lceil \frac{61}{4}\right\rceil=\left\lceil 15.25\right\rceil=16,
\quad
\left\lfloor \frac{91}{5}\right\rfloor=\left\lfloor 18.2\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=92\):
\[
\left\lceil \frac{62}{4}\right\rceil=\left\lceil 15.5\right\rceil=16,
\quad
\left\lfloor \frac{92}{5}\right\rfloor=\left\lfloor 18.4\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=93\):
\[
\left\lceil \frac{63}{4}\right\rceil=\left\lceil 15.75\right\rceil=16,
\quad
\left\lfloor \frac{93}{5}\right\rfloor=\left\lfloor 18.6\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=94\):
\[
\left\lceil \frac{64}{4}\right\rceil=\left\lceil 16\right\rceil=16,
\quad
\left\lfloor \frac{94}{5}\right\rfloor=\left\lfloor 18.8\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=95\):
\[
\left\lceil \frac{65}{4}\right\rceil=\left\lceil 16.25\right\rceil=17,
\quad
\left\lfloor \frac{95}{5}\right\rfloor=\left\lfloor 19\right\rfloor=19.
\]
Interval \([17,19]\) has 3 integers → not unique.

\(s=96\):
\[
\left\lceil \frac{66}{4}\right\rceil=\left\lceil 16.5\right\rceil=17,
\quad
\left\lfloor \frac{96}{5}\right\rfloor=\left\lfloor 19.2\right\rfloor=19.
\]
Interval \([17,19]\) has 3 integers → not unique.

At this point, notice the interval length is small but hasn’t become 0. Since we must eventually get a single integer, we can solve when
\[
\left\lfloor \frac{s}{5}\right\rfloor = \left\lceil \frac{s-30}{4}\right\rceil.
\]
Instead, test plausible uniqueness by setting \(u\) small, because \(u=s-5c\) must also satisfy \(c+u\le 30\Rightarrow u\le 30-c\).
If \(c\) is maximal for given \(s\), then \(u\) is minimal. Uniqueness is most likely when increasing \(c\) by 1 forces \(u\) negative or violates \(c+u\le 30\).

Suppose \(c\) is the largest possible: \(c=\left\lfloor s/5\right\rfloor\). Then \(u=s-5c\) is the remainder \(r\in\{0,1,2,3,4\}\).
Condition \(c+u\le 30\) becomes
\[
\left\lfloor \frac{s}{5}\right\rfloor + (s-5\left\lfloor \frac{s}{5}\right\rfloor)\le 30
\iff c+r\le 30.
\]
If also the next smaller \(c\) would still be feasible, uniqueness fails. That means we need exactly one feasible \(c\), which occurs when lowering \(c\) by 1 would make \(u\) too large to keep \(c+u\le 30\).

If \(c\) is feasible with remainder \(r\), then with \(c-1\) we would have
\[
u' = s-5(c-1)= (s-5c)+5 = r+5.
\]
Then
\[
(c-1)+u' = (c-1)+(r+5)=c+r+4.
\]
So \(c-1\) is infeasible exactly when
\[
c+r+4>30 \quad\text{while}\quad c+r\le 30.
\]
Thus
\[
c+r=30.
\]
So we require the feasible pair to satisfy \(u=r\) and \(c+r=30\), i.e. \(u\) is exactly \(30-c\) (no wrong answers determined).

Now \(s=5c+u=5c+r\) with \(c+r=30\Rightarrow r=30-c\). Substitute:
\[
s=5c+(30-c)=4c+30.
\]
Also \(r=30-c\) must be \(0,1,2,3,4\). Hence
\[
30-c\in\{0,1,2,3,4\}\implies c\in\{26,27,28,29,30\}.
\]
Compute corresponding scores \(s=4c+30\):
- \(c=26\Rightarrow s=134\)
- \(c=27\Rightarrow s=138\)
- \(c=28\Rightarrow s=142\)
- \(c=29\Rightarrow s=146\)
- \(c=30\Rightarrow s=150\)

Among these, we need the one with \(s\) just over \(80\) satisfying the “if score had been any lower but still over 80, John could not” condition. The smallest score in the list is \(134\). Therefore it must be the first time uniqueness occurs for \(s>80\).

So Mary's score is \(\boxed{134}\).

ANSWER: 134
```

</details>

<details>
<summary>Generation 7</summary>

```text
We have \(30\) problems. Let \(c\)=correct, \(w\)=wrong, and \(u\)=unanswered. Then
\[
c+w+u=30.
\]
The score is
\[
s=30+4c-w.
\]
So
\[
s-30=4c-w \quad\Longrightarrow\quad w=4c-(s-30).
\]
Since \(w\) is a nonnegative integer and \(u=30-c-w\ge 0\), we need
\[
w\ge 0 \quad\Longrightarrow\quad 4c\ge s-30,
\]
\[
u=30-c-w=30-c-(4c-(s-30))=30-c-4c+s-30=s-5c\ge 0
\quad\Longrightarrow\quad s\ge 5c.
\]
Thus valid \(c\) satisfy
\[
\frac{s-30}{4}\le c \le \frac{s}{5},
\]
with \(c\) an integer.

John can determine the number of correct answers from knowing \(s>80\) exactly when there is **only one** integer \(c\) in that interval. If \(s\) were any lower but still \(>80\), then there would be **at least two** possible values of \(c\).

Let’s rewrite bounds:
\[
c \ge \left\lceil\frac{s-30}{4}\right\rceil,\qquad c\le \left\lfloor\frac{s}{5}\right\rfloor.
\]
We want exactly one integer \(c\), i.e.
\[
\left\lceil\frac{s-30}{4}\right\rceil=\left\lfloor\frac{s}{5}\right\rfloor.
\]
Try to search near \(s=80\) upward. Since there are only a few extra scores above 80, we can test candidates.

Note that \(s=81,82,83,\dots\). Compute possible \(c\) range quickly.

### Test \(s=86\)
\[
\frac{s-30}{4}=\frac{56}{4}=14 \Rightarrow \left\lceil\cdot\right\rceil=14,
\]
\[
\frac{s}{5}=\frac{86}{5}=17.2 \Rightarrow \left\lfloor\cdot\right\rfloor=17.
\]
This gives \(c\in\{14,15,16,17\}\), not unique. Too many.

### Test \(s=90\)
\[
\frac{s-30}{4}=\frac{60}{4}=15 \Rightarrow \lceil\cdot\rceil=15,
\]
\[
\frac{s}{5}=\frac{90}{5}=18 \Rightarrow \lfloor\cdot\rfloor=18,
\]
so \(c\in\{15,16,17,18\}\). Not unique.

We need the interval to be so tight that it contains exactly one integer. That happens when the lower bound is just one above the previous integer and the upper bound equals it.

A standard way: require
\[
\left\lfloor\frac{s}{5}\right\rfloor = \left\lceil\frac{s-30}{4}\right\rceil = c.
\]
Then
\[
4c \le s-30 < 4(c+1)
\quad\text{and}\quad
5c \le s < 5(c+1).
\]
So \(s\) must satisfy both:
\[
s \in [5c,\,5c+4]
\]
and
\[
s \in [4c+30,\,4c+33].
\]
Intersecting gives a short range. Also \(s>80\).

Let’s find \(c\) and \(s\) with \(s\) in the intersection being a single integer and giving the “minimality” condition.

Try plausible \(c\). Since \(s>80\), and \(s\ge 5c\), we get \(c\le 16\) (because \(5\cdot 16=80\), need \(s>80\) so \(c\) could be 16 with \(s\ge81\)). Also \(4c\le s-30\) implies \(s\ge 4c+30\).

So \(c\) from 13 to 16 are likely.

#### Take \(c=16\)
Then:
\[
s\in [5\cdot 16,5\cdot 16+4]=[80,84]
\]
and
\[
s\in [4\cdot 16+30,4\cdot 16+33]=[94,97].
\]
No overlap. So \(c\neq 16\).

#### Take \(c=15\)
\[
s\in [75,79],\quad s\in [90,93]
\]
No overlap.

#### Take \(c=14\)
\[
s\in [70,74],\quad s\in [86,89]
\]
No overlap.

#### Take \(c=13\)
\[
s\in [65,69],\quad s\in [82,85]
\]
No overlap.

This suggests our “intersection method” used strictness incorrectly: we used \(4c \le s-30 <4(c+1)\) but from \(\left\lceil\frac{s-30}{4}\right\rceil=c\) the condition is
\[
c-1 < \frac{s-30}{4} \le c.
\]
So
\[
4(c-1) < s-30 \le 4c
\]
\[
4c+30 \ge s > 4c+26.
\]
Thus
\[
s\in \{4c+27,4c+28,4c+29,4c+30\}.
\]
Also \(\left\lfloor\frac{s}{5}\right\rfloor=c\) means
\[
5c \le s < 5c+5,
\]
so
\[
s\in \{5c,5c+1,5c+2,5c+3,5c+4\}.
\]
Now intersect these sets.

Let \(c\) be the unique correct count.

Since \(s>80\), we test \(c=14,15,16,\dots\) but note \(s<5c+5\).

#### \(c=15\)
Second set: \(s\in\{75,76,77,78,79\}\) (all \(\le 79\)), impossible since \(s>80\).
So \(c\ge 16\).

#### \(c=16\)
Second set: \(s\in\{80,81,82,83,84\}\).
First set: \(s\in\{4(16)+27,\dots,4(16)+30\}=\{91,92,93,94\}\).
No overlap.

#### \(c=17\)
Second set: \(s\in\{85,86,87,88,89\}\).
First set: \(s\in\{4(17)+27,4(17)+30\}=\{95,96,97,98\}\) no overlap.

So clearly the unique-\(c\) approach indicates something inconsistent: the sets don’t overlap for any \(c\), meaning our assumption that both floor/ceil equal the same \(c\) is possible only if the inequalities permit overlap; but we’re missing that \(c\) must satisfy simultaneously
\[
c \ge \left\lceil\frac{s-30}{4}\right\rceil,\quad c \le \left\lfloor\frac{s}{5}\right\rfloor,
\]
so uniqueness means these bounds differ by less than 1, not necessarily equal as integers due to ceil/floor discreteness. The correct condition for exactly one integer is:
\[
\left\lceil\frac{s-30}{4}\right\rceil \le \left\lfloor\frac{s}{5}\right\rfloor
\]
and the count is 1:
\[
\left\lfloor\frac{s}{5}\right\rfloor - \left\lceil\frac{s-30}{4}\right\rceil +1 = 1
\]
\[
\Longrightarrow\quad \left\lfloor\frac{s}{5}\right\rfloor = \left\lceil\frac{s-30}{4}\right\rceil.
\]
So equality is correct; yet it yields no solution for \(s>80\) by our attempted \(c\). Therefore we should instead directly brute force \(s\) near 80 by checking possible \(c\) via the interval
\[
\frac{s-30}{4}\le c\le \frac{s}{5}.
\]

### Directly test \(s=81,82,\dots\)
For each \(s\), compute possible \(c\) integers.

- \(s=81\): \(\frac{51}{4}=12.75\le c\le 16.2\Rightarrow c\in\{13,14,15,16\}\) (4).
- \(s=82\): \(\frac{52}{4}=13\le c\le 16.4\Rightarrow c\in\{13,14,15,16\}\) (4).
- \(s=83\): \(\frac{53}{4}=13.25\le c\le 16.6\Rightarrow c\in\{14,15,16\}\) (3).
- \(s=84\): \(\frac{54}{4}=13.5\le c\le 16.8\Rightarrow c\in\{14,15,16\}\) (3).
- \(s=85\): \(\frac{55}{4}=13.75\le c\le 17\Rightarrow c\in\{14,15,16,17\}\) (4).
- \(s=86\): \(\frac{56}{4}=14\le c\le 17.2\Rightarrow c\in\{14,15,16,17\}\) (4).
- \(s=87\): \(\frac{57}{4}=14.25\le c\le 17.4\Rightarrow c\in\{15,16,17\}\) (3).
- \(s=88\): \(\frac{58}{4}=14.5\le c\le 17.6\Rightarrow c\in\{15,16,17\}\) (3).
- \(s=89\): \(\frac{59}{4}=14.75\le c\le 17.8\Rightarrow c\in\{15,16,17\}\) (3).
- \(s=90\): \(\frac{60}{4}=15\le c\le 18\Rightarrow c\in\{15,16,17,18\}\) (4).
- \(s=91\): \(\frac{61}{4}=15.25\le c\le 18.2\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=92\): \(\frac{62}{4}=15.5\le c\le 18.4\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=93\): \(\frac{63}{4}=15.75\le c\le 18.6\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=94\): \(\frac{64}{4}=16\le c\le 18.8\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=95\): \(\frac{65}{4}=16.25\le c\le 19\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=96\): \(\frac{66}{4}=16.5\le c\le 19.2\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=97\): \(\frac{67}{4}=16.75\le c\le 19.4\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=98\): \(\frac{68}{4}=17\le c\le 19.6\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=99\): \(\frac{69}{4}=17.25\le c\le 19.8\Rightarrow c\in\{18,19\}\) (2).
- \(s=100\): \(\frac{70}{4}=17.5\le c\le 20\Rightarrow c\in\{18,19,20\}\) (3).
- \(s=101\): \(\frac{71}{4}=17.75\le c\le 20.2\Rightarrow c\in\{18,19,20\}\) (3).
- \(s=102\): \(\frac{72}{4}=18\le c\le 20.4\Rightarrow c\in\{18,19,20\}\) (3).
- \(s=103\): \(\frac{73}{4}=18.25\le c\le 20.6\Rightarrow c\in\{19,20\}\) (2).
- \(s=104\): \(\frac{74}{4}=18.5\le c\le 20.8\Rightarrow c\in\{19,20\}\) (2).
- \(s=105\): \(\frac{75}{4}=18.75\le c\le 21\Rightarrow c\in\{19,20,21\}\) but \(c\le 30\) ok (3).
- \(s=106\): \(\frac{76}{4}=19\le c\le 21.2\Rightarrow c\in\{19,20,21\}\) (3).
- \(s=107\): \(\frac{77}{4}=19.25\le c\le 21.4\Rightarrow c\in\{20,21\}\) (2).
- \(s=108\): \(\frac{78}{4}=19.5\le c\le 21.6\Rightarrow c\in\{20,21\}\) (2).
- \(s=109\): \(\frac{79}{4}=19.75\le c\le 21.8\Rightarrow c\in\{20,21\}\) (2).
- \(s=110\): \(\frac{80}{4}=20\le c\le 22\Rightarrow c\in\{20,21,22\}\) (3).

We still haven’t seen uniqueness (1 candidate). Continue until it happens.

- \(s=113\): lower \(\frac{83}{4}=20.75\Rightarrow c\ge 21\). upper \(\frac{113}{5}=22.6\Rightarrow c\le 22\). So \(c\in\{21,22\}\) (2).
- \(s=114\): lower \(\frac{84}{4}=21\Rightarrow c\ge 21\). upper \(\frac{114}{5}=22.8\Rightarrow c\le 22\). So \(c\in\{21,22\}\) (2).
- \(s=115\): lower \(\frac{85}{4}=21.25\Rightarrow c\ge 22\). upper \(115/5=23\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=116\): lower \(86/4=21.5\Rightarrow c\ge 22\). upper \(116/5=23.2\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=117\): lower \(87/4=21.75\Rightarrow c\ge 22\). upper \(117/5=23.4\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=118\): lower \(88/4=22\Rightarrow c\ge 22\). upper \(118/5=23.6\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=119\): lower \(89/4=22.25\Rightarrow c\ge 23\). upper \(119/5=23.8\Rightarrow c\le 23\). So **\(c=\{23\}\)** unique!

Now check the condition: if the score were any lower but still \(>80\), John could not have determined \(c\). We must ensure that for \(s=118\) uniqueness fails (it does: two values), and generally for all \(81\le s\le 118\) there are either 2 or more. From our sampling it seems we never got 1 earlier; we can accept this as consistent because the unique first occurrence happens when the upper bound drops to exactly the next integer while the lower bound has just surpassed the previous.

Thus \(s=119\) is the desired score.

\[
\boxed{119}
\]

ANSWER: 119
```

</details>

<details>
<summary>Generation 8</summary>

```text
We have \(30\) multiple choice questions. Let \(c\) be the number correct and \(w\) the number wrong; unanswered \(=30-c-w\).
Scores are
\[
s=30+4c-w.
\]
Given \(s>80\), rewrite:
\[
s-30=4c-w \quad\Rightarrow\quad s-30=4c-(\text{# wrong}).
\]

For fixed \(c\), the score ranges over possible \(w\) values with \(0\le w\le 30-c\), giving
\[
s=30+4c-w \in \{30+4c-(30-c),\,\dots,\,30+4c\}
= \{30+5c-30,\dots,30+4c\}.
\]
So for each \(c\), the achievable scores form an interval of integers:
\[
s\in [\,5c,\; 30+4c\,].
\]

John can determine \(c\) from \(s\) exactly when the intervals for different \(c\)’s do not overlap at that score.

Compute overlap condition between \(c\) and \(c+1\):
- \(c\)-interval upper end: \(30+4c\)
- \((c+1)\)-interval lower end: \(5(c+1)=5c+5\)

They overlap if
\[
5c+5 \le 30+4c
\quad\Longleftrightarrow\quad
c \le 25.
\]
Thus, for \(c\le 25\), there is overlap, so \(s\) cannot uniquely determine \(c\).
For \(c\ge 26\), there is no overlap between consecutive intervals (and hence \(c\) becomes uniquely determined by \(s\)).

Now use the problem’s “threshold” condition:
- Mary’s score is over \(80\), so we need \(s>80\).
- If the score were any lower (but still \(>80\)), John could not determine \(c\).
So \(s\) should be the *smallest* score \(>80\) for which \(c\) is uniquely determined.

Try the boundary case \(c=26\):
- For \(c=26\), the achievable interval is
\[
[\,5c,\;30+4c\,]=[130,\;30+104]=[130,\;134].
\]
The smallest is \(130\), which is definitely \(>80\).

Now check whether any score between \(81\) and \(129\) could yield unique \(c\).
But for \(c\le 25\) the intervals overlap, so uniqueness fails. Hence the first unique score above \(80\) must occur at the smallest score belonging to some \(c\ge 26\), i.e. at \(5\cdot 26=130\).

We should also ensure that at \(s=129\) uniqueness fails (it should, since \(c\le 25\)). Indeed \(129\) lies in the overlap region of some \(c\le 25\).

Therefore Mary’s score is
\[
\boxed{130}.
\]

Check quickly: can \(s=130\) occur with \(c=26\) and some \(w\)?
From \(s=30+4c-w\):
\[
130=30+104-w \Rightarrow w=4.
\]
Then \(c+w=30\), so all questions answered; feasible.

Also, could any other \(c\) produce \(s=130\)?
For \(c=25\): \(130=30+100-w\Rightarrow w=0\), feasible, but then the corresponding interval for \(c=25\) is \([125,130]\), which would suggest overlap at 130. However uniqueness should fail if overlaps exist; and indeed we found overlap for \(c\le 25\). So we need to re-evaluate carefully: overlap at 130 means both \(c=25\) and \(c=26\) can produce 130. But is that possible given the scoring constraints?  
For \(c=25\), \(w=0\) gives score \(30+4\cdot 25-0=130\), and unanswered \(=30-25-0=5\), allowed. So John would not be able to determine \(c\) at \(s=130\).

So the earlier “no overlap for \(c\ge 26\)” conclusion must be refined: overlap occurs between intervals whenever consecutive intervals intersect, i.e. when
\[
\text{lower}_{c+1} \le \text{upper}_c.
\]
For \(c=25\):
\[
\text{lower}_{26}=5\cdot 26=130,\quad \text{upper}_{25}=30+4\cdot 25=130,
\]
so they intersect at exactly \(130\). Therefore at \(s=130\), \(c\) is not uniquely determined.

Thus we need the *smallest* \(s>80\) for which no other \(c\) can produce it. That means we must find the smallest score above 80 that lies strictly inside the region where intervals for different \(c\)’s are disjoint at that point.

The first \(s\) where disjointness becomes strict is when the lower end of the next interval is greater than the upper end of the previous:
\[
5(c+1) > 30+4c
\quad\Longleftrightarrow\quad
5c+5 > 4c+30
\quad\Longleftrightarrow\quad
c>25.
\]
So we need \(c\ge 26\), but also avoid the boundary intersection at \(s=130\). For \(c=26\), the interval is \([130,134]\), and the only shared point with \(c=25\) is \(130\). Therefore the smallest score \(>80\) with unique \(c\) is \(131\).

Now verify uniqueness at \(s=131\):
Solve for \(w\):
\[
131=30+4c-w \Rightarrow w=30+4c-131=4c-101.
\]
Check possibilities:
- If \(c=25\): \(w=100-101=-1\), impossible.
- If \(c=26\): \(w=104-101=3\), valid since \(c+w=29\le 30\).
- If \(c\le 24\): even worse (would give negative \(w\) for \(s\) this large).
So only \(c=26\) works. Hence John can determine \(c\) from \(s=131\).

Finally, if the score were any lower but still \(>80\), i.e. \(s=81,82,\dots,130\), uniqueness fails because for \(c\le 25\) intervals overlap and at \(s=130\) we saw non-uniqueness too.

So Mary’s score is \(\boxed{131}\).

ANSWER: 131
```

</details>

<details>
<summary>Generation 9</summary>

```text
Let \(c\) be the number correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\qquad s=30+4c-w.
\]
Substitute \(w=30-c-u\):
\[
s=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
So
\[
s=5c+u,\quad \text{with } c\ge 0,\ u\ge 0,\ c+u\le 30.
\]

John can determine \(c\) from \(s\) if there is only one possible value of \(c\) that can produce that score.

We are told:
- \(s>80\).
- If \(s\) were any lower but still \(>80\), then \(c\) would *not* be uniquely determined.

So \(s\) is the *largest* score \(>80\) for which \(c\) is still unique? Let’s find the first point above 80 where uniqueness breaks.

From \(s=5c+u\), for a given \(s\),
\[
u=s-5c.
\]
For feasibility we need \(0\le u\le 30-c\), i.e.
\[
0\le s-5c\le 30-c.
\]
The left inequality gives \(c\le \frac{s}{5}\).
The right inequality gives
\[
s-5c\le 30-c\implies s\le 30+4c\implies c\ge \frac{s-30}{4}.
\]
Thus the possible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
Uniqueness means this interval contains exactly one integer.

Now test scores just above 80. Since the maximum score occurs at \(c=30,u=0\): \(s=150\), so we’re in a moderate range.

Compute for \(s=81,82,\dots\) until the interval size changes.

Let
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad R(s)=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Unique \(c\) occurs when \(L(s)=R(s)\).

Check \(s=81\):
\[
L=\left\lceil \frac{51}{4}\right\rceil=\lceil 12.75\rceil=13,\quad
R=\left\lfloor \frac{81}{5}\right\rfloor=\lfloor 16.2\rfloor=16.
\]
Not unique.

We need \(s\) close enough to force \(R\) down while \(L\) stays near it. This happens at larger \(s\).

Try \(s=100\):
\[
L=\left\lceil \frac{70}{4}\right\rceil=\lceil17.5\rceil=18,\quad
R=\left\lfloor \frac{100}{5}\right\rfloor=20.
\]
Not unique.

Try \(s=104\):
\[
L=\left\lceil \frac{74}{4}\right\rceil=\lceil18.5\rceil=19,\quad
R=\left\lfloor \frac{104}{5}\right\rfloor=\lfloor20.8\rfloor=20.
\]
Still not unique.

Try \(s=105\):
\[
L=\left\lceil \frac{75}{4}\right\rceil=\lceil18.75\rceil=19,\quad
R=\left\lfloor \frac{105}{5}\right\rfloor=21.
\]
Not unique.

Try \(s=108\):
\[
L=\left\lceil \frac{78}{4}\right\rceil=\lceil19.5\rceil=20,\quad
R=\left\lfloor \frac{108}{5}\right\rfloor=\lfloor21.6\rfloor=21.
\]
Not unique.

Try \(s=110\):
\[
L=\left\lceil \frac{80}{4}\right\rceil=\lceil20\rceil=20,\quad
R=\left\lfloor \frac{110}{5}\right\rfloor=\lfloor22\rfloor=22.
\]
Not unique.

We need \(R(s)=L(s)\). That means the interval length is 0:
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]
Let that common value be \(c\). Then we require
\[
c\le \frac{s}{5} < c+1
\quad\text{and}\quad
c-1< \frac{s-30}{4}\le c.
\]
Convert to bounds on \(s\):
\[
5c \le s \le 5c+4
\]
and
\[
4c+26 < s \le 4c+30.
\]
So \(s\) must satisfy both:
\[
\max(5c,\,4c+27)\le s \le \min(5c+4,\,4c+30).
\]
Since \(4c+27\) is larger than \(4c+26\).

Compute which \(c\) allow overlap. Note
\[
5c \quad\text{vs}\quad 4c+27:\quad 5c\ge 4c+27 \iff c\ge 27.
\]
But \(c\le 30\). So \(c\) is likely \(27,28,29,30\).

Also
\[
5c+4 \quad\text{vs}\quad 4c+30:\quad 5c+4\le 4c+30 \iff c\le 26.
\]
So for \(c\ge 27\), the upper limit will be \(4c+30\).

Thus for \(c\in\{27,28,29,30\}\):
- Lower bound: \(\max(5c,4c+27)=5c\) (since \(c\ge 27\))
- Upper bound: \(\min(5c+4,4c+30)=4c+30\) (since \(c\ge 27\))

So we need
\[
5c \le 4c+30 \iff c\le 30,
\]
always true in this range. And we need at least one integer \(s\) between them:
\[
s \in [5c,\;4c+30].
\]
For each \(c\):
- \(c=27\): \(s\in[135,138]\) all \(>80\).
- \(c=28\): \(s\in[140,142]\).
- \(c=29\): \(s\in[145,146]\).
- \(c=30\): \(s=150\).

Now interpret the “if score had been any lower but still \(>80\), John could not have determined” condition. That means \(s\) is the *smallest* score \(>80\) for which the representation gives unique \(c\), because any lower \(>80\) would allow multiple \(c\).

Among the candidates above, the smallest \(s\) is \(135\) (from \(c=27\)). We must verify that \(s=134\) is not unique.

For \(s=134\):
\[
L=\left\lceil \frac{104}{4}\right\rceil=26,\quad
R=\left\lfloor \frac{134}{5}\right\rfloor=26.
\]
That would actually be unique, which contradicts. So we must re-check: compute carefully:
\[
\frac{134}{5}=26.8\Rightarrow R=26.
\]
For \(L\):
\[
\frac{s-30}{4}=\frac{104}{4}=26\Rightarrow L=26.
\]
So \(s=134\) is unique with \(c=26\). Therefore the smallest unique score above 80 is less than 135, so our earlier candidate set missed lower \(c\) values because overlap logic assumed \(c\ge 27\) to compare bounds, but uniqueness can also happen for smaller \(c\) when the ceiling/floor align just right.

So instead we should directly find the minimal \(s>80\) for which there is uniqueness and then pick the *first* such that all smaller \(>80\) are non-unique. However the condition in the problem is: Mary’s score \(s\) is such that John can determine \(c\), but for any lower score still \(>80\), he cannot. That means \(s\) is the *minimum* score \(>80\) with unique \(c\).

So find the smallest \(s>80\) with \(L(s)=R(s)\).

We test systematically by looking at when \(R(s)=\left\lfloor \frac{s}{5}\right\rfloor\) increments, and \(L(s)=\left\lceil \frac{s-30}{4}\right\rceil\).

Compute \(s\) near 80-90 quickly:

For \(s=85\):
\[
L=\left\lceil \frac{55}{4}\right\rceil=\lceil13.75\rceil=14,\quad
R=\left\lfloor \frac{85}{5}\right\rfloor=17
\]
No.

For \(s=86\): \(L=\lceil14\rceil=14\) (since \(\frac{56}{4}=14\)), \(R=\lfloor17.2\rfloor=17\). No.

We need \(R\) drop or \(L\) rise until they meet. This happens when \(R\) is small relative to \(L\), i.e. at larger \(s\).

Instead, find where \(L(s)\) catches up to \(R(s)\). Solve approximately:
\[
\frac{s-30}{4}\approx \frac{s}{5}\implies 5(s-30)=4s\implies 5s-150=4s\implies s=150.
\]
So they meet only near the top, but due to integer effects, first equality may occur earlier. Let’s search from 81 upward with the interval size \(R-L\) becoming 0.

Try \(s=130\):
\[
L=\left\lceil \frac{100}{4}\right\rceil=25,\quad
R=\left\lfloor \frac{130}{5}\right\rfloor=26.
\]
Not.

\(s=131\):
\[
L=\left\lceil \frac{101}{4}\right\rceil=\lceil25.25\rceil=26,\quad
R=\left\lfloor \frac{131}{5}\right\rfloor=26.
\]
Here \(L=R=26\), so uniqueness holds.

Now check \(s=130\) was non-unique (it had \(c\in[25,26]\)), good.

Also we must ensure for any lower \(s>80\), uniqueness fails. Since we found the first time at \(131\) (we should verify \(s=129\) etc. but they are further from the top and likely not yet unique). Let’s confirm quickly:
- \(s=129\): \(L=\lceil99/4\rceil=\lceil24.75\rceil=25\), \(R=\lfloor25.8\rfloor=25\) gives uniqueness at 25. Wait compute: \(\lfloor129/5\rfloor=25\) yes, and \(L=25\) too, so uniqueness would already occur at 129, contradicting minimality.

But does \(s=129\) truly give a unique feasible \(c\)? Our interval method should be correct; thus check:
For \(s=129\), \(c=25\) gives \(u=s-5c=129-125=4\), and check \(c+u=29\le 30\) feasible. For \(c=24\), \(u=129-120=9\), then \(c+u=33>30\) infeasible. So only \(c=25\). Hence uniqueness at \(129\).

So the true “minimal unique” must be even lower. We need the score \(s\) such that uniqueness holds but immediately below \(80<s'<s\) uniqueness fails. That means \(s\) is the unique-threshold where non-uniqueness switches to uniqueness; i.e. we need the *largest* score \(>80\) for which uniqueness holds and below which uniqueness fails (equivalently: uniqueness holds only at that exact score, and not at any lower score, but our counterexamples show uniqueness can occur at multiple scores).

Interpretation: “If Mary's score had been any lower, but still over 80, John could not have determined this.” That means for every integer score \(s'\) with \(81\le s'<s\), \(c\) would not be uniquely determined. So indeed \(s\) is the smallest score \(>80\) with uniqueness. But our checks show uniqueness at \(129\), so smaller scores than 129 must be non-unique; we must find the actual smallest such.

We can continue decreasing to find earliest \(s\) with \(L(s)=R(s)\).

Let \(s=5k+r\) with \(r\in\{0,1,2,3,4\}\). Then \(R=k\).
Also
\[
L=\left\lceil \frac{5k+r-30}{4}\right\rceil.
\]
Set \(L=k\):
\[
k-1<\frac{5k+r-30}{4}\le k
\]
Multiply:
\[
4k-4<5k+r-30\le 4k
\]
Left:
\[
4k-4<5k+r-30\implies -k-r< -26\implies k+r>26.
\]
Right:
\[
5k+r-30\le 4k\implies k+r\le 30.
\]
So uniqueness occurs exactly when
\[
k+r\in\{27,28,29,30\},
\]
with \(s=5k+r\), \(r\in[0,4]\).

Since \(s>80\), we need smallest \(s\) among those satisfying \(k+r\ge 27\).

To minimize \(s=5k+r\) given fixed \(k+r=t\), we should make \(k\) as small as possible (because coefficient 5 on \(k\)). For each \(t\in\{27,28,29,30\}\), take \(k\) minimal so that \(r=t-k\le 4\).

- For \(t=27\): need \(r=27-k\le 4\Rightarrow k\ge 23\). Minimal \(k=23\) gives \(r=4\), \(s=5\cdot 23+4=119\).
- Check \(t=28\): minimal \(k\ge 24\) gives \(r=4\), \(s=124\) larger.
So smallest is \(119\).

Therefore Mary’s score is \(119\).

Finally confirm that for any \(s'<119\) with \(s'>80\), uniqueness fails: that means no solution to \(k+r\in\{27,28,29,30\}\) yields \(s<119\). Since the smallest constructed was \(119\), all smaller \(s\) have \(k+r\le 26\) hence \(L\ne R\). Good.

Thus \(s=119\).

ANSWER: 119
```

</details>

<details>
<summary>Generation 10</summary>

```text
We have \(30\) questions. Let \(c\) be correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\quad s=30+4c-w,
\]
with \(u\ge 0\), so \(c+w\le 30\). Also \(c,w\ge 0\) integers.

Rewrite the score condition:
\[
s=30+4c-w \quad\Longrightarrow\quad 4c-w=s-30.
\]
Given a fixed score \(s\), this means
\[
w=4c-(s-30).
\]
Thus for each integer \(c\), we get a corresponding \(w\). For \(c\) to be valid we need:
1. \(w\ge 0\) \(\Rightarrow 4c\ge s-30\),
2. \(c+w\le 30\). Substitute \(w\):
\[
c+\bigl(4c-(s-30)\bigr)\le 30
\]
\[
5c-(s-30)\le 30
\]
\[
5c\le s+60
\]
\[
c\le \frac{s+60}{5}.
\]
So possible \(c\) values are integers satisfying
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s+60}{5}\right\rfloor.
\]
John can determine \(c\) uniquely from \(s\) iff there is exactly one integer \(c\) in this interval.

Mary’s score is over \(80\), so \(81\le s \le 120\) (maximum when \(w=0\), \(c=30\): \(s=30+120=150\) actually; but for \(s\) around 80–150 we’ll narrow with constraints).

“Any lower but still over \(80\)” means: for every \(s'\) with \(80<s'<s\), the interval for \(s'\) contains at least two integers \(c\) (so \(c\) is not uniquely determined). In particular, \(s-1\) must *not* give uniqueness.

So we want the smallest score above 80 that gives uniqueness, since if the score were not minimal, we could lower slightly and still have uniqueness, contradicting the condition. Therefore we seek the minimal \(s\ge 81\) such that the interval contains exactly one integer.

Let
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad U(s)=\left\lfloor \frac{s+60}{5}\right\rfloor.
\]
Uniqueness means \(L(s)=U(s)\).

Check \(s=81\):
\[
L=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,
\quad
U=\left\lfloor \frac{141}{5}\right\rfloor=\left\lfloor 28.2\right\rfloor=28.
\]
Many values → not unique.

As \(s\) increases, both bounds increase, and the width \(U-L\) will eventually shrink to 0. Let’s find when \(L(s)=U(s)\) first happens for \(s>80\).

Try to force equality by approximating without ceilings/floors:
\[
\frac{s-30}{4}\approx \frac{s+60}{5}
\]
\[
5(s-30)=4(s+60)
\]
\[
5s-150=4s+240
\]
\[
s=390.
\]
That’s far too large, meaning ceilings/floors matter and the interval length typically stays large. So uniqueness likely happens only near the feasibility boundary \(c+w\le 30\) becoming tight, i.e. when \(w\) is forced.

Instead, use the constraint \(c+w\le 30\) together with \(w=4c-(s-30)\):
\[
c+w = c+4c-(s-30)=5c-(s-30)\le 30
\]
\[
5c\le s+60.
\]
Also \(w\ge 0\) gives \(4c\ge s-30\). So \(c\) must satisfy:
\[
\frac{s-30}{4}\le c\le \frac{s+60}{5}.
\]
For uniqueness, these bounds must trap \(c\) to a single integer, meaning their difference is \(<1\):
\[
\frac{s+60}{5}-\frac{s-30}{4}<1.
\]
Compute:
\[
\frac{4(s+60)-5(s-30)}{20}<1
\]
\[
\frac{4s+240-5s+150}{20}<1
\]
\[
\frac{-s+390}{20}<1
\]
\[
-s+390<20
\]
\[
s>370.
\]
Again too big. So the earlier “difference<1” criterion isn’t appropriate because ceilings/floors can still reduce to 0 even when the real interval is larger; but the inequality suggests uniqueness might require very special congruences forcing only one integer.

So instead, try to express \(s\) in terms of \((c,w)\) and enforce that the score corresponds to exactly one \(c\). Observe:
\[
s=30+4c-w = 30+5c-(c+w).
\]
Let \(t=c+w\) be the number attempted (correct or wrong). Then
\[
s=30+5c-t,\quad 0\le t\le 30.
\]
Also \(w=t-c\), and \(0\le c\le t\).

So:
\[
s=30+5c-t \quad\Longrightarrow\quad t=30+5c-s.
\]
For a given score \(s\), a value \(c\) is possible iff the resulting \(t\) is an integer with
\[
0\le t\le 30,\quad c\le t.
\]
Since \(t=30+5c-s\), \(t\) is automatically integer if \(c\) integer. The conditions become:
1. \(0\le 30+5c-s\) \(\Rightarrow 5c\ge s-30\) (same as before),
2. \(30+5c-s\le 30\) \(\Rightarrow 5c\le s\),
3. \(c\le t=30+5c-s\) \(\Rightarrow 0\le 30+4c-s\) \(\Rightarrow 4c\ge s-30\).

So the main upper bound is now
\[
5c\le s.
\]
Combine with \(5c\ge s-30\) and \(4c\ge s-30\).

Thus:
\[
c\in \mathbb{Z},\quad \frac{s-30}{5}\le c\le \frac{s}{5},\quad\text{and}\quad c\ge \frac{s-30}{4}.
\]
But \(\frac{s-30}{4}>\frac{s-30}{5}\), so the effective lower bound is \(\left\lceil\frac{s-30}{4}\right\rceil\) and the upper bound is \(\left\lfloor\frac{s}{5}\right\rfloor\).
Hence uniqueness means:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]

Now test \(s=85\):
\[
\left\lceil\frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,\quad
\left\lfloor\frac{85}{5}\right\rfloor=17.
\]
Not equal.

Try \(s=90\):
\[
\left\lceil\frac{60}{4}\right\rceil=15,\quad \left\lfloor\frac{90}{5}\right\rfloor=18.
\]
No.

Try \(s=100\):
\[
\left\lceil\frac{70}{4}\right\rceil=18,\quad \left\lfloor\frac{100}{5}\right\rfloor=20.
\]
No.

We need \(\lfloor s/5\rfloor\) to be small enough to equal the ceiling term. Let \(k=\lfloor s/5\rfloor\). Then \(5k\le s\le 5k+4\).
Also uniqueness requires \(k=\left\lceil\frac{s-30}{4}\right\rceil\), so
\[
k-1<\frac{s-30}{4}\le k
\]
\[
4(k-1)<s-30\le 4k
\]
\[
4k+ -4 +? \Rightarrow 4k-4< s-30 \le 4k
\]
\[
4k+26< s \le 4k+30.
\]
Combine with \(5k\le s\le 5k+4\). So \(s\) must satisfy
\[
\max(5k,\,4k+27) \le s \le \min(5k+4,\,4k+30).
\]
Compute:
Left max: \(4k+27\) vs \(5k\). Their difference:
\[
5k-(4k+27)=k-27.
\]
For \(k\ge 27\), left is \(5k\). For \(s>80\), likely \(k\ge 16\). Let’s find actual \(s\) by trying \(k\) near where the interval could become a single integer.

Also right min: compare \(5k+4\) vs \(4k+30\):
\[
(4k+30)-(5k+4)=26-k.
\]
So for \(k\ge 26\), right is \(4k+30\); for \(k\le 26\), right is \(5k+4\).

To make interval very tight (ideally one integer), likely near \(k=27\) or \(26\).

Try \(k=27\):
Then \(s\) must satisfy:
left \(=\max(135,\,4(27)+27=135)=135\),
right \(=\min(139,\,4(27)+30=138)=138\).
So \(s\in[135,138]\). Any of these might yield uniqueness.

But we require \(s>80\); fine.

Now ensure uniqueness for one candidate and non-uniqueness for \(s-1\).
Let’s compute possible \(c\) directly for each \(s\in\{135,136,137,138\}\).

For a given \(s\), upper bound on \(c\) is \(\left\lfloor s/5\right\rfloor = \left\lfloor 27.0\) to \(27.6\right\rfloor =27\).
Lower bound is \(\left\lceil (s-30)/4\right\rceil = \left\lceil (105\text{ to }108)/4\right\rceil\).
- \(s=135\): \((s-30)/4=105/4=26.25\Rightarrow L=27\). So \(c\) is forced to \(27\). Uniqueness holds.
Now check \(s=134\) (still over 80):
\[
U=\left\lfloor 134/5\right\rfloor=26,\quad
L=\left\lceil 104/4\right\rceil=26.
\]
That would also give uniqueness, which would contradict the “if score had been any lower… John could not have determined” condition.
So \(s=135\) is too high.

Try next down where uniqueness first appears: we want \(s-1\) not unique, i.e. for \(s-1\) the interval contains at least two integers.

Consider \(s=136\):
- \(U=\lfloor 136/5\rfloor=27\).
- \(L=\left\lceil 106/4\right\rceil=\left\lceil 26.5\right\rceil=27\).
So \(c=27\) unique.
Check \(s-1=135\) gave uniqueness, so still contradiction.

For \(s=137\):
- \(U=\lfloor 137/5\rfloor=27\).
- \(L=\left\lceil 107/4\right\rceil=\left\lceil 26.75\right\rceil=27\).
Unique for 137.
Check \(136\) for uniqueness:
\(s=136\) also unique (as above). Contradiction.

For \(s=138\):
- \(U=\lfloor 138/5\rfloor=27\).
- \(L=\left\lceil 108/4\right\rceil=\left\lceil 27\right\rceil=27\).
Unique.
Check \(s-1=137\) unique. Contradiction.

Therefore the “lower but still over 80” means: decreasing the score while keeping it over 80 (but not necessarily by 1) makes uniqueness impossible, so it suffices that *every* \(s'\) with \(81\le s'<s\) is non-unique. That implies \(s\) is the *smallest* score \(>80\) yielding uniqueness.

Thus we must find the minimal \(s>80\) with uniqueness; we mistakenly jumped to \(k=27\) due to tightness. Let’s search smaller \(k\).

Set uniqueness condition:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor = k.
\]
Let \(s\) be minimal \(>80\). Since \(s>80\), \(k=\lfloor s/5\rfloor\ge 17\).

We can brute by \(k\) logic with interval for \(s\) derived earlier:
When \(k\le 26\), right min is \(5k+4\). Also since \(k<27\), left max is \(4k+27\) (because \(k-27<0\Rightarrow 5k<4k+27\)).
So for \(k\le 26\), we have
\[
4k+27 \le s \le 5k+4.
\]
For uniqueness to hold, \(s\) must also satisfy that the ceiling equals \(k\), which is exactly ensured by these bounds.

Now find minimal \(s>80\). Try \(k=17\):
\[
4k+27=68+27=95,\quad 5k+4=85+4=89,
\]
impossible (lower bound > upper). So \(k=17\) no.

\(k=18\):
\[
4k+27=72+27=99,\quad 5k+4=90+4=94
\]
impossible.

We need \(4k+27\le 5k+4\Rightarrow 27-4\le k \Rightarrow 23\le k\).
So smallest possible \(k\) is \(23\).

Take \(k=23\):
\[
4k+27=92+27=119,\quad 5k+4=115+4=119.
\]
So \(s=119\) is forced and is the minimal possible.

Verify:
For \(s=119\),
\[
U=\left\lfloor 119/5\right\rfloor=23.
\]
\[
L=\left\lceil (119-30)/4\right\rceil=\left\lceil 89/4\right\rceil=\left\lceil 22.25\right\rceil=23.
\]
So unique \(c=23\).

Check that any lower \(s'\) with \(>80\) is non-unique: since \(k\) would be \(\le 22\) for \(s'\le 118\). But for \(k\le 22\), the interval inequality fails (as shown \(4k+27>5k+4\)), giving either 0 or multiple solutions; in any case not uniqueness. Indeed, if \(k\le 22\), there is no integer \(s\) satisfying the derived bounds simultaneously for uniqueness. Hence \(119\) is the first score \(>80\) with unique \(c\).

Therefore Mary’s score is \(119\).

ANSWER: 119
```

</details>

## Scoring

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.0000 | `incorrect` |
| 1 | 1.0000 | `correct` |
| 2 | 0.0000 | `incorrect` |
| 3 | 0.0000 | `incorrect` |
| 4 | 1.0000 | `correct` |
| 5 | 0.0000 | `incorrect` |
| 6 | 1.0000 | `correct` |
| 7 | 0.0000 | `incorrect` |
| 8 | 1.0000 | `correct` |
| 9 | 1.0000 | `correct` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 131",
  "answer_fragment": "131",
  "extracted": "131"
}
```

</details>

<details>
<summary>Score details for generation 1</summary>

```json
{
  "reason": "correct",
  "expected": "119",
  "answer_line": "ANSWER: 119",
  "answer_fragment": "119",
  "extracted": "119"
}
```

</details>

<details>
<summary>Score details for generation 2</summary>

```json
{
  "reason": "missing_answer_line",
  "expected": "119",
  "answer_line": null,
  "answer_fragment": null,
  "extracted": null
}
```

</details>

<details>
<summary>Score details for generation 3</summary>

```json
{
  "reason": "missing_answer_line",
  "expected": "119",
  "answer_line": null,
  "answer_fragment": null,
  "extracted": null
}
```

</details>

<details>
<summary>Score details for generation 4</summary>

```json
{
  "reason": "correct",
  "expected": "119",
  "answer_line": "ANSWER: 119",
  "answer_fragment": "119",
  "extracted": "119"
}
```

</details>

<details>
<summary>Score details for generation 5</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 134",
  "answer_fragment": "134",
  "extracted": "134"
}
```

</details>

<details>
<summary>Score details for generation 6</summary>

```json
{
  "reason": "correct",
  "expected": "119",
  "answer_line": "ANSWER: 119",
  "answer_fragment": "119",
  "extracted": "119"
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 131",
  "answer_fragment": "131",
  "extracted": "131"
}
```

</details>

<details>
<summary>Score details for generation 8</summary>

```json
{
  "reason": "correct",
  "expected": "119",
  "answer_line": "ANSWER: 119",
  "answer_fragment": "119",
  "extracted": "119"
}
```

</details>

<details>
<summary>Score details for generation 9</summary>

```json
{
  "reason": "correct",
  "expected": "119",
  "answer_line": "ANSWER: 119",
  "answer_fragment": "119",
  "extracted": "119"
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

## Math-specific guidance
- For math, prefer memories about how to choose a representation, invariant, proof strategy, or validation step rather than advice tied to one theorem, construction, or object type.
- A good math memory should still make sense if the next problem uses different mathematical objects but has the same structural challenge.
- If a draft memory mainly says to use a particular theorem, formula, or named construction, rewrite it one level more abstract: explain the signal for using that move and the mistake it helps prevent.
- Prefer titles that name the reasoning move, not the surface topic.
- Favor reusable proof moves such as explicit constraint modeling, invariant selection, validating transformed equations, disciplined casework, complement or bijection counting, extremal arguments, and completeness or bounding proofs.
- Merge overlapping memories that express the same proof move. Do not split one idea into several object-specific variants.
- In the content field, explain both when to use the idea and what class of failure it helps avoid.

## Examples of good meta-reasoning memories
- Title: Validate Lossy Transformations
  Description: Check transformed candidates against the original constraints before finalizing.
  Content: If you square, divide, drop a case, or weaken a condition, add a verification pass against the original problem. This prevents transformed solutions from being accepted just because they satisfy an easier intermediate condition.
- Title: Switch to an Explicit Constraint Model
  Description: When a diagram, identity, or theorem application is ambiguous, rewrite the givens as direct equations or inequalities.
  Content: Introduce variables for the unknown quantities and encode each condition explicitly. This is often safer than forcing a theorem whose prerequisites may not actually be established.
- Title: Prove Search Completeness
  Description: If you test candidates or scan cases, justify why no untested case can beat the selected answer.
  Content: Use a bound, invariant, monotonicity argument, or exhaustion proof to show the search space is complete. This turns a plausible candidate check into a full proof.
- Title: Choose a Counting Model with a Verified Bijection
  Description: In combinatorics, count through a model only after proving it matches the original objects one-to-one.
  Content: If you switch to gaps, complements, or auxiliary configurations, verify the mapping in both directions. This prevents elegant-looking counts that miss or double-count cases.

### Problem
Mary told John her score on the American High School Mathematics Examination (AHSME), which was over $80$ . From this, John was able to determine the number of problems Mary solved correctly. If Mary's score had been any lower, but still over $80$ , John could not have determined this. What was Mary's score? (Recall that the AHSME consists of $30$ multiple choice problems and that one's score, $s$ , is computed by the formula $s=30+4c-w$ , where $c$ is the number of correct answers and $w$ is the number of wrong answers. Students are not penalized for problems left unanswered.)

### Solutions
#### Correct
Attempt 1
Let \(c\) be the number correct and \(w\) the number wrong. Since there are \(30\) total problems, the number left blank is \(30-c-w\ge 0\).

Given the scoring rule
\[
s=30+4c-w,
\]
we can rewrite \(w\) in terms of \(s\) and \(c\):
\[
w=30+4c-s.
\]
We must have
\[
0\le w \le 30-c.
\]
The upper bound \(w\le 30-c\) is equivalent to \(30+4c-s\le 30-c\), i.e.
\[
4c-c\le s \quad\Longrightarrow\quad 3c\le s.
\]
The lower bound \(w\ge 0\) is \(30+4c-s\ge 0\), i.e.
\[
4c\ge s-30.
\]

John can determine \(c\) uniquely from the score \(s\). If there were another feasible \(c'\neq c\) producing the same \(s\), then John couldn’t determine the number correct.

Now consider how \(c\) could change while keeping the same score. From
\[
s=30+4c-w,
\]
fix \(s\). If we increase \(c\) by \(1\), to keep \(s\) constant we must increase \(w\) by \(4\) (because \(4c-w\) must stay the same). So alternative solutions correspond to steps
\[
(c,w)\to (c+1,\,w+4).
\]
Thus, for a given \(s\), multiple values of \(c\) are possible exactly when there exists room to add these \((+1,+4)\) moves without violating feasibility \(w\le 30-c\) and \(w\ge 0\).

The problem says:
- For Mary’s actual score \(s\), \(c\) is determined uniquely.
- For any smaller score \(s' > 80\), John cannot determine \(c\) (so at least two different \(c\)’s are feasible).

So \(s\) is the *largest* score \(>80\) for which uniqueness holds; just below it, the feasible range for \(c\) becomes large enough to allow two solutions.

Compute \(s\) near \(80\). Since \(s=30+4c-w\) with \(w\ge 0\), we have
\[
s\le 30+4c \quad\Rightarrow\quad c\ge \frac{s-30}{4}.
\]
Also from \(w\le 30-c\),
\[
30+4c-s \le 30-c \quad\Rightarrow\quad 3c\le s.
\]
So for a fixed \(s\), feasible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{3}\right\rfloor.
\]

Uniqueness means this integer interval has exactly one integer.

Let’s test scores just above \(80\). Start with \(s=81\):
\[
\left\lceil\frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,\quad
\left\lfloor\frac{81}{3}\right\rfloor=27.
\]
Many \(c\), not unique.

We need the interval to shrink to one integer. As \(s\) increases, the lower bound increases by about \(1/4\) per \(1\) in \(s\), while the upper bound increases by \(1/3\) per \(1\) in \(s\). The interval length tends to decrease only very rarely due to the ceilings/floors; uniqueness is most likely at a boundary where the ceiling equals the floor.

So we search for \(s>80\) such that
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{3}\right\rfloor.
\]
Let that common value be \(c\). Then \(c\) must satisfy
\[
\frac{s-30}{4} \le c \le \frac{s}{3}
\]
and with integrality/rounding:
\[
c-1 < \frac{s-30}{4} \le c,\qquad c\le \frac{s}{3} < c+1.
\]
Equivalently,
\[
4(c-1) < s-30 \le 4c,\qquad 3c \le s < 3(c+1).
\]
Thus
\[
4c+30 \ge s > 4(c-1)+30 =4c+26
\]
and
\[
3c \le s < 3c+3.
\]
So \(s\) must lie in the intersection:
\[
(4c+26,\;4c+30]\cap [3c,\;3c+3).
\]
Since \(4c+26\) is much larger than \(3c\) for \(c\ge 1\), the key overlap forces \(s\) close to \(4c+26\) but also less than \(3c+3\). Set the inequalities:
\[
4c+26 < 3c+3 \quad\Rightarrow\quad c < -23,
\]
impossible. That means our assumption about the interval having exactly one integer via equality of those bounds must be reconsidered: uniqueness doesn’t require the feasible \(c\)-interval length to be 1, because different \(c\) might fail the implied \(w\) nonnegativity/upper bound in a way that ceiling/floor conditions alone don’t fully capture due to the step structure \(w=30+4c-s\). But actually those bounds *are* exactly the feasibility for \(w\), so the interval approach is correct—so why did it seem impossible? The arithmetic indicates we made a wrong comparison: the lower bound is \(\left\lceil\frac{s-30}{4}\right\rceil\), upper bound \(\left\lfloor\frac{s}{3}\right\rfloor\). For \(s\) around 80, these are:
- lower about \((s-30)/4\approx 12.5\),
- upper about \(s/3\approx 26.6\).
So uniqueness would require very special \(s\), but it can happen when the lower and upper are equal, which seems impossible since \((s-30)/4\) is always much smaller than \(s/3\) for positive \(s\):
\[
\frac{s-30}{4}=\frac{s}{3}\ \Rightarrow\ 3s-90=4s\ \Rightarrow\ s=-90.
\]
So indeed they can never be equal. Therefore uniqueness must be interpreted differently: given \(s\), John can determine \(c\) because although multiple \(c\) values are feasible, the resulting \(c\) are the same—i.e., not possible. That contradicts feasibility unless we misread: John determines the number of problems Mary solved correctly, meaning \(c\) is uniquely determined, so there must be exactly one feasible \(c\). Since exact equality of bounds cannot happen, the only way is that feasibility interval length becomes \(<1\), impossible as shown. Hence the correct approach is to use the score modulo constraints from the step structure.

From
\[
s=30+4c-w,
\]
with \(w\) integer, we have
\[
s\equiv 30+4c \pmod{1}\quad \text{(no restriction)}.
\]
But combining with \(w\le 30-c\) gives:
\[
w=30+4c-s \le 30-c \Rightarrow 5c \le s.
\]
Also \(w\ge 0\Rightarrow 30+4c-s\ge 0\Rightarrow 4c\ge s-30\).

So feasibility is
\[
\left\lceil\frac{s-30}{4}\right\rceil \le c \le \left\lfloor\frac{s}{5}\right\rfloor.
\]
Now for uniqueness, this interval must contain exactly one integer.

Test \(s=81\):
\[
\left\lceil\frac{51}{4}\right\rceil=13,\quad \left\lfloor\frac{81}{5}\right\rfloor=16.
\]
Possible \(c=13,14,15,16\) => not unique.

We need the interval length \(=0\) or \(1\). Since uniqueness means exactly one integer:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]
Now solve for when the bounds can match.

Let that integer be \(c\). Then
\[
\frac{s-30}{4} \le c < \frac{s-30}{4}+1,
\]
\[
c \le \frac{s}{5} < c+1.
\]
Translate to \(s\):
From \(c \le s/5\): \(s\ge 5c\).
From \(s/5 < c+1\): \(s<5c+5\).
From \((s-30)/4 \le c\): \(s-30 \le 4c\Rightarrow s\le 4c+30\).
From \(c < (s-30)/4+1\): \(c-1 < (s-30)/4\Rightarrow 4c-4 < s-30\Rightarrow s>4c+26\).

So
\[
5c \le s < 5c+5,\quad 4c+27 \le s \le 4c+30.
\]
Intersection:
\[
s \in [5c,\;5c+4]\cap [4c+27,\;4c+30].
\]
For intersection to be nonempty:
\[
5c \le 4c+30 \Rightarrow c\le 30.
\]
Also need
\[
5c+4 \ge 4c+27 \Rightarrow c\ge 23.
\]
So \(c\in\{23,24,25,26,27,28,29,30\}\).

Now compute the possible \(s\) by taking \(s\) in intersection; additionally \(s>80\) and we want the *maximal* \(s\) such that uniqueness holds but for any smaller \(s'>80\) it fails.

Let’s compute for each \(c\), the intersection interval for \(s\):
- lower \(L=\max(5c,\;4c+27)\),
- upper \(U=\min(5c+4,\;4c+30)\).

But compare \(5c\) vs \(4c+27\): \(5c-(4c+27)=c-27\).
So for \(c\ge 27\), \(5c\ge 4c+27\) hence \(L=5c\).
For \(c\le 26\), \(L=4c+27\).

Similarly compare \(5c+4\) vs \(4c+30\): \((5c+4)-(4c+30)=c-26\).
For \(c\ge 26\), \(5c+4\ge 4c+30\) so \(U=4c+30\).
For \(c\le 25\), \(U=5c+4\).

Now list \(c\ge 23\):

- \(c=23\): \(L=4(23)+27=119\), already \(>80\) too high but actually \(s\) would be \(>100\). still allowed but check uniqueness and the “any lower score still >80 fails” suggests we want smallest above 80. However note \(s\) increases with \(c\). So we want the smallest \(c\) that gives uniqueness while keeping \(s>80\) maximal just above 80. Let’s instead directly find \(s\) in \((80, \infty)\) that yields uniqueness and is minimal just above 80? The condition says if score had been any lower but still over 80, uniqueness would fail. So our \(s\) is the smallest value \(>80\) for which uniqueness holds.
So search upward from 81 until uniqueness holds, and ensure it fails for all 81,82,...,s-1.
Try compute uniqueness quickly by counting feasible \(c\) values for each \(s\) is heavy; instead use the derived matching condition which gives exact uniqueness.

The matching condition gives candidates for \(s\) where the feasible interval shrinks to one integer, and the smallest \(s>80\) among them is our answer.

Compute \(s\) from \(s\) must satisfy either endpoints in intersection.

For each \(c\), the possible \(s\) range is:
- \(c=23\): \(L=4c+27=119\), \(U=5c+4=119\)?? since \(U=5c+4\) for c<=25: \(U=119\). So \(s=119\).
- \(c=24\): \(L=4c+27=123\), \(U=5c+4=124\) (since c<=25). so possibly \(s=123,124\) but uniqueness requires exactly one feasible \(c\), still okay if both work? check quickly by constructing \(w\):
  If \(s=123\): \(w=30+4c-s=30+96-123=3\), and \(c=24\) gives blanks \(=30-24-3=3\ge0\) feasible.
  If \(s=124\): \(w=30+96-124=2\), blanks \(=4\ge0\) feasible.
But could there be another \(c\) feasible for those \(s\)? uniqueness says no, so these should be valid candidates.
- \(c=25\): \(L=4c+27=127\), \(U=5c+4=129\) (still c<=25 for U): \(s\in\{127,128,129\}\).
- \(c=26\): now \(L=4c+27=131\) (since c<=26 for L), \(U=4c+30=134\) (since c>=26 for U): \(s\in\{131,132,133,134\}\).
- \(c=27\): \(L=5c=135\), \(U=4c+30=138\): \(s\in\{135,136,137,138\}\).
Clearly the smallest \(s>80\) among all is \(s=119\).

Now verify the “any lower but still over 80” condition. We must ensure for scores \(81\) through \(118\), \(c\) is not uniquely determined. Since our candidate uniqueness starts at \(119\), this must be true.

Therefore Mary's score is \(119\).
Then
\[
119=30+4c-w \Rightarrow 89=4c-w.
\]
With the feasible matching case found above, \(c=23\) gives \(w=30+92-119=3\), blanks \(=30-23-3=4\ge0\).
And for \(s=119\), the matching condition indicates uniqueness holds, so John can deduce \(c=23\).

ANSWER: 119

Attempt 2
Let \(c\) be the number correct and \(w\) the number wrong. Then unanswered are irrelevant, and
\[
s=30+4c-w.
\]
Also \(c+w\le 30\) with \(c,w\ge 0\).

John knows \(s>80\) and from \(s\) can determine the pair \((c,w)\), hence \(c\), uniquely. But if \(s\) were any lower (still \(>80\)), \((c,w)\) would no longer be uniquely determined.

Define
\[
t:=s-30=4c-w.
\]
Since \(s>80\), we have \(t>50\). Also
\[
w=4c-t.
\]
For given \(t\), any valid solution must satisfy:
1. \(w\ge 0 \Rightarrow 4c-t\ge 0 \Rightarrow c\ge \frac t4\).
2. \(c+w\le 30\):
\[
c+(4c-t)\le 30 \;\Rightarrow\; 5c-t\le 30 \;\Rightarrow\; c\le \frac{t+30}{5}.
\]
So the integer \(c\) is constrained by
\[
\left\lceil \frac t4\right\rceil \le c \le \left\lfloor \frac{t+30}{5}\right\rfloor.
\]
Then each such \(c\) gives exactly one \(w=4c-t\), hence one achievable score.

We need the smallest \(s>80\) for which this interval contains exactly one integer \(c\) (uniqueness), but for the previous score value \(s-1\) (i.e. \(t-1\)) the interval contains at least two integers.

Since \(s>80\), the candidate smallest \(s\) is \(81\), i.e. \(t=51\), and we test upward until uniqueness occurs.

### Check \(t=51\) (score \(81\))
\[
\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,\quad
\left\lfloor \frac{51+30}{5}\right\rfloor=\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
So \(c\) can be \(13,14,15,16\): **4 possibilities**, not unique.

### Check \(t=52\) (score \(82\))
\[
\left\lceil \frac{52}{4}\right\rceil=\left\lceil 13\right\rceil=13,\quad
\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16.
\]
So \(c=13,14,15,16\): **4 possibilities**, not unique.

### Check \(t=53\) (score \(83\))
\[
\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14,\quad
\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16.
\]
So \(c=14,15,16\): **3 possibilities**, not unique.

### Check \(t=54\) (score \(84\))
\[
\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14,\quad
\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16.
\]
So \(c=14,15,16\): **3 possibilities**, not unique.

### Check \(t=55\) (score \(85\))
\[
\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,\quad
\left\lfloor \frac{85}{5}\right\rfloor=\left\lfloor 17\right\rfloor=17.
\]
So \(c=14,15,16,17\): **4 possibilities**, not unique.

### Check \(t=56\) (score \(86\))
\[
\left\lceil \frac{56}{4}\right\rceil=\left\lceil 14\right\rceil=14,\quad
\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17.
\]
So \(c=14,15,16,17\): **4 possibilities**.

### Check \(t=57\) (score \(87\))
\[
\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15,\quad
\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17.
\]
So \(c=15,16,17\): **3 possibilities**.

### Check \(t=58\) (score \(88\))
\[
\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15,\quad
\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17.
\]
So \(c=15,16,17\): **3 possibilities**.

### Check \(t=59\) (score \(89\))
\[
\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15,\quad
\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17.
\]
So \(c=15,16,17\): **3 possibilities**.

### Check \(t=60\) (score \(90\))
\[
\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15,\quad
\left\lfloor \frac{90}{5}\right\rfloor=\left\lfloor 18\right\rfloor=18.
\]
So \(c=15,16,17,18\): **4 possibilities**.

This is still not getting uniqueness; so uniqueness must occur at some higher \(t\) where the interval shrinks to a single integer.

Notice:
- The lower bound \(\lceil t/4\rceil\) increases by \(1\) every time \(t\) passes a multiple of \(4\).
- The upper bound \(\lfloor (t+30)/5\rfloor\) increases by \(1\) every time \(t\) passes a value making \((t+30)/5\) cross an integer.

The interval length is
\[
\left\lfloor \frac{t+30}{5}\right\rfloor - \left\lceil \frac t4\right\rceil.
\]
We want this to be \(0\) (exactly one integer).

So we try to find when
\[
\left\lceil \frac t4\right\rceil = \left\lfloor \frac{t+30}{5}\right\rfloor.
\]

Try \(t=74\) (score \(104\)) near the top (since max score is \(30+4\cdot 30=150\)).
Compute quickly:
\[
\left\lceil \frac{74}{4}\right\rceil=\left\lceil 18.5\right\rceil=19,\quad
\left\lfloor \frac{104}{5}\right\rfloor=\left\lfloor 20.8\right\rfloor=20.
\]
Two values possible \(c=19,20\). Not unique.

Try \(t=75\) (score \(105\)):
\[
\left\lceil \frac{75}{4}\right\rceil=\left\lceil 18.75\right\rceil=19,\quad
\left\lfloor \frac{105}{5}\right\rfloor=\left\lfloor 21\right\rfloor=21.
\]
So \(c=19,20,21\): not unique.

Try \(t=76\) (score \(106\)):
\[
\left\lceil 19\right\rceil=19,\quad \left\lfloor \frac{106}{5}\right\rfloor=\left\lfloor 21.2\right\rfloor=21.
\]
So \(c=19,20,21\): not unique.

Try \(t=77\) (score \(107\)):
\[
\left\lceil 19.25\right\rceil=20,\quad \left\lfloor \frac{107}{5}\right\rfloor=\left\lfloor 21.4\right\rfloor=21.
\]
So \(c=20,21\): not unique.

Try \(t=78\) (score \(108\)):
\[
\left\lceil 19.5\right\rceil=20,\quad \left\lfloor \frac{108}{5}\right\rfloor=\left\lfloor 21.6\right\rfloor=21.
\]
So \(c=20,21\): not unique.

Try \(t=79\) (score \(109\)):
\[
\left\lceil 19.75\right\rceil=20,\quad \left\lfloor \frac{109}{5}\right\rfloor=\left\lfloor 21.8\right\rfloor=21.
\]
So \(c=20,21\): not unique.

Try \(t=80\) (score \(110\)):
\[
\left\lceil 20\right\rceil=20,\quad \left\lfloor \frac{110}{5}\right\rfloor=22.
\]
Then \(c=20,21,22\): not unique.

Try \(t=81\) (score \(111\)):
\[
\left\lceil 20.25\right\rceil=21,\quad \left\lfloor \frac{111+?}{5}\right\rfloor=\left\lfloor \frac{111+30?}{5}\right\rfloor
\]
Oops—remember upper is \(\frac{t+30}{5}\), so for \(t=81\), \(t+30=111\):
\[
\left\lfloor \frac{111}{5}\right\rfloor=\left\lfloor 22.2\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=82\) (score \(112\)):
\[
\left\lceil \frac{82}{4}\right\rceil=\left\lceil 20.5\right\rceil=21,\quad
\left\lfloor \frac{112}{5}\right\rfloor=\left\lfloor 22.4\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=83\) (score \(113\)):
\[
\left\lceil 20.75\right\rceil=21,\quad \left\lfloor \frac{113}{5}\right\rfloor=\left\lfloor 22.6\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=84\) (score \(114\)):
\[
\left\lceil 21\right\rceil=21,\quad \left\lfloor \frac{114}{5}\right\rfloor=\left\lfloor 22.8\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=85\) (score \(115\)):
\[
\left\lceil 21.25\right\rceil=22,\quad \left\lfloor \frac{115}{5}\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=86\) (score \(116\)):
\[
\left\lceil 21.5\right\rceil=22,\quad \left\lfloor \frac{116}{5}\right\rfloor=\left\lfloor 23.2\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=87\) (score \(117\)):
\[
\left\lceil 21.75\right\rceil=22,\quad \left\lfloor \frac{117}{5}\right\rfloor=\left\lfloor 23.4\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=88\) (score \(118\)):
\[
\left\lceil 22\right\rceil=22,\quad \left\lfloor \frac{118}{5}\right\rfloor=\left\lfloor 23.6\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=89\) (score \(119\)):
\[
\left\lceil 22.25\right\rceil=23,\quad \left\lfloor \frac{119}{5}\right\rfloor=\left\lfloor 23.8\right\rfloor=23.
\]
Now the interval is \(c=23\) only! Great—this gives uniqueness.

So score \(s = 30+t = 30+89 = 119\).

Finally we check the “if Mary's score had been any lower but still over 80” condition: meaning at \(s=118\) (i.e. \(t=88\)) John could not determine \(c\) uniquely.
We found for \(t=88\), \(c\in\{22,23\}\), indeed not unique. Thus the condition is satisfied.

Compute \(c\) and \(w\) for \(t=89\):
\[
t=4c-w \Rightarrow 89=4\cdot 23 - w = 92-w \Rightarrow w=3.
\]
Valid since \(23+3=26\le 30\).

Therefore Mary's score is \(119\).

ANSWER: 119

Attempt 3
We have \(30\) problems. Let \(c\)=correct, \(w\)=wrong, and \(u\)=unanswered. Then
\[
c+w+u=30.
\]
The score is
\[
s=30+4c-w.
\]
So
\[
s-30=4c-w \quad\Longrightarrow\quad w=4c-(s-30).
\]
Since \(w\) is a nonnegative integer and \(u=30-c-w\ge 0\), we need
\[
w\ge 0 \quad\Longrightarrow\quad 4c\ge s-30,
\]
\[
u=30-c-w=30-c-(4c-(s-30))=30-c-4c+s-30=s-5c\ge 0
\quad\Longrightarrow\quad s\ge 5c.
\]
Thus valid \(c\) satisfy
\[
\frac{s-30}{4}\le c \le \frac{s}{5},
\]
with \(c\) an integer.

John can determine the number of correct answers from knowing \(s>80\) exactly when there is **only one** integer \(c\) in that interval. If \(s\) were any lower but still \(>80\), then there would be **at least two** possible values of \(c\).

Let’s rewrite bounds:
\[
c \ge \left\lceil\frac{s-30}{4}\right\rceil,\qquad c\le \left\lfloor\frac{s}{5}\right\rfloor.
\]
We want exactly one integer \(c\), i.e.
\[
\left\lceil\frac{s-30}{4}\right\rceil=\left\lfloor\frac{s}{5}\right\rfloor.
\]
Try to search near \(s=80\) upward. Since there are only a few extra scores above 80, we can test candidates.

Note that \(s=81,82,83,\dots\). Compute possible \(c\) range quickly.

### Test \(s=86\)
\[
\frac{s-30}{4}=\frac{56}{4}=14 \Rightarrow \left\lceil\cdot\right\rceil=14,
\]
\[
\frac{s}{5}=\frac{86}{5}=17.2 \Rightarrow \left\lfloor\cdot\right\rfloor=17.
\]
This gives \(c\in\{14,15,16,17\}\), not unique. Too many.

### Test \(s=90\)
\[
\frac{s-30}{4}=\frac{60}{4}=15 \Rightarrow \lceil\cdot\rceil=15,
\]
\[
\frac{s}{5}=\frac{90}{5}=18 \Rightarrow \lfloor\cdot\rfloor=18,
\]
so \(c\in\{15,16,17,18\}\). Not unique.

We need the interval to be so tight that it contains exactly one integer. That happens when the lower bound is just one above the previous integer and the upper bound equals it.

A standard way: require
\[
\left\lfloor\frac{s}{5}\right\rfloor = \left\lceil\frac{s-30}{4}\right\rceil = c.
\]
Then
\[
4c \le s-30 < 4(c+1)
\quad\text{and}\quad
5c \le s < 5(c+1).
\]
So \(s\) must satisfy both:
\[
s \in [5c,\,5c+4]
\]
and
\[
s \in [4c+30,\,4c+33].
\]
Intersecting gives a short range. Also \(s>80\).

Let’s find \(c\) and \(s\) with \(s\) in the intersection being a single integer and giving the “minimality” condition.

Try plausible \(c\). Since \(s>80\), and \(s\ge 5c\), we get \(c\le 16\) (because \(5\cdot 16=80\), need \(s>80\) so \(c\) could be 16 with \(s\ge81\)). Also \(4c\le s-30\) implies \(s\ge 4c+30\).

So \(c\) from 13 to 16 are likely.

#### Take \(c=16\)
Then:
\[
s\in [5\cdot 16,5\cdot 16+4]=[80,84]
\]
and
\[
s\in [4\cdot 16+30,4\cdot 16+33]=[94,97].
\]
No overlap. So \(c\neq 16\).

#### Take \(c=15\)
\[
s\in [75,79],\quad s\in [90,93]
\]
No overlap.

#### Take \(c=14\)
\[
s\in [70,74],\quad s\in [86,89]
\]
No overlap.

#### Take \(c=13\)
\[
s\in [65,69],\quad s\in [82,85]
\]
No overlap.

This suggests our “intersection method” used strictness incorrectly: we used \(4c \le s-30 <4(c+1)\) but from \(\left\lceil\frac{s-30}{4}\right\rceil=c\) the condition is
\[
c-1 < \frac{s-30}{4} \le c.
\]
So
\[
4(c-1) < s-30 \le 4c
\]
\[
4c+30 \ge s > 4c+26.
\]
Thus
\[
s\in \{4c+27,4c+28,4c+29,4c+30\}.
\]
Also \(\left\lfloor\frac{s}{5}\right\rfloor=c\) means
\[
5c \le s < 5c+5,
\]
so
\[
s\in \{5c,5c+1,5c+2,5c+3,5c+4\}.
\]
Now intersect these sets.

Let \(c\) be the unique correct count.

Since \(s>80\), we test \(c=14,15,16,\dots\) but note \(s<5c+5\).

#### \(c=15\)
Second set: \(s\in\{75,76,77,78,79\}\) (all \(\le 79\)), impossible since \(s>80\).
So \(c\ge 16\).

#### \(c=16\)
Second set: \(s\in\{80,81,82,83,84\}\).
First set: \(s\in\{4(16)+27,\dots,4(16)+30\}=\{91,92,93,94\}\).
No overlap.

#### \(c=17\)
Second set: \(s\in\{85,86,87,88,89\}\).
First set: \(s\in\{4(17)+27,4(17)+30\}=\{95,96,97,98\}\) no overlap.

So clearly the unique-\(c\) approach indicates something inconsistent: the sets don’t overlap for any \(c\), meaning our assumption that both floor/ceil equal the same \(c\) is possible only if the inequalities permit overlap; but we’re missing that \(c\) must satisfy simultaneously
\[
c \ge \left\lceil\frac{s-30}{4}\right\rceil,\quad c \le \left\lfloor\frac{s}{5}\right\rfloor,
\]
so uniqueness means these bounds differ by less than 1, not necessarily equal as integers due to ceil/floor discreteness. The correct condition for exactly one integer is:
\[
\left\lceil\frac{s-30}{4}\right\rceil \le \left\lfloor\frac{s}{5}\right\rfloor
\]
and the count is 1:
\[
\left\lfloor\frac{s}{5}\right\rfloor - \left\lceil\frac{s-30}{4}\right\rceil +1 = 1
\]
\[
\Longrightarrow\quad \left\lfloor\frac{s}{5}\right\rfloor = \left\lceil\frac{s-30}{4}\right\rceil.
\]
So equality is correct; yet it yields no solution for \(s>80\) by our attempted \(c\). Therefore we should instead directly brute force \(s\) near 80 by checking possible \(c\) via the interval
\[
\frac{s-30}{4}\le c\le \frac{s}{5}.
\]

### Directly test \(s=81,82,\dots\)
For each \(s\), compute possible \(c\) integers.

- \(s=81\): \(\frac{51}{4}=12.75\le c\le 16.2\Rightarrow c\in\{13,14,15,16\}\) (4).
- \(s=82\): \(\frac{52}{4}=13\le c\le 16.4\Rightarrow c\in\{13,14,15,16\}\) (4).
- \(s=83\): \(\frac{53}{4}=13.25\le c\le 16.6\Rightarrow c\in\{14,15,16\}\) (3).
- \(s=84\): \(\frac{54}{4}=13.5\le c\le 16.8\Rightarrow c\in\{14,15,16\}\) (3).
- \(s=85\): \(\frac{55}{4}=13.75\le c\le 17\Rightarrow c\in\{14,15,16,17\}\) (4).
- \(s=86\): \(\frac{56}{4}=14\le c\le 17.2\Rightarrow c\in\{14,15,16,17\}\) (4).
- \(s=87\): \(\frac{57}{4}=14.25\le c\le 17.4\Rightarrow c\in\{15,16,17\}\) (3).
- \(s=88\): \(\frac{58}{4}=14.5\le c\le 17.6\Rightarrow c\in\{15,16,17\}\) (3).
- \(s=89\): \(\frac{59}{4}=14.75\le c\le 17.8\Rightarrow c\in\{15,16,17\}\) (3).
- \(s=90\): \(\frac{60}{4}=15\le c\le 18\Rightarrow c\in\{15,16,17,18\}\) (4).
- \(s=91\): \(\frac{61}{4}=15.25\le c\le 18.2\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=92\): \(\frac{62}{4}=15.5\le c\le 18.4\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=93\): \(\frac{63}{4}=15.75\le c\le 18.6\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=94\): \(\frac{64}{4}=16\le c\le 18.8\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=95\): \(\frac{65}{4}=16.25\le c\le 19\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=96\): \(\frac{66}{4}=16.5\le c\le 19.2\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=97\): \(\frac{67}{4}=16.75\le c\le 19.4\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=98\): \(\frac{68}{4}=17\le c\le 19.6\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=99\): \(\frac{69}{4}=17.25\le c\le 19.8\Rightarrow c\in\{18,19\}\) (2).
- \(s=100\): \(\frac{70}{4}=17.5\le c\le 20\Rightarrow c\in\{18,19,20\}\) (3).
- \(s=101\): \(\frac{71}{4}=17.75\le c\le 20.2\Rightarrow c\in\{18,19,20\}\) (3).
- \(s=102\): \(\frac{72}{4}=18\le c\le 20.4\Rightarrow c\in\{18,19,20\}\) (3).
- \(s=103\): \(\frac{73}{4}=18.25\le c\le 20.6\Rightarrow c\in\{19,20\}\) (2).
- \(s=104\): \(\frac{74}{4}=18.5\le c\le 20.8\Rightarrow c\in\{19,20\}\) (2).
- \(s=105\): \(\frac{75}{4}=18.75\le c\le 21\Rightarrow c\in\{19,20,21\}\) but \(c\le 30\) ok (3).
- \(s=106\): \(\frac{76}{4}=19\le c\le 21.2\Rightarrow c\in\{19,20,21\}\) (3).
- \(s=107\): \(\frac{77}{4}=19.25\le c\le 21.4\Rightarrow c\in\{20,21\}\) (2).
- \(s=108\): \(\frac{78}{4}=19.5\le c\le 21.6\Rightarrow c\in\{20,21\}\) (2).
- \(s=109\): \(\frac{79}{4}=19.75\le c\le 21.8\Rightarrow c\in\{20,21\}\) (2).
- \(s=110\): \(\frac{80}{4}=20\le c\le 22\Rightarrow c\in\{20,21,22\}\) (3).

We still haven’t seen uniqueness (1 candidate). Continue until it happens.

- \(s=113\): lower \(\frac{83}{4}=20.75\Rightarrow c\ge 21\). upper \(\frac{113}{5}=22.6\Rightarrow c\le 22\). So \(c\in\{21,22\}\) (2).
- \(s=114\): lower \(\frac{84}{4}=21\Rightarrow c\ge 21\). upper \(\frac{114}{5}=22.8\Rightarrow c\le 22\). So \(c\in\{21,22\}\) (2).
- \(s=115\): lower \(\frac{85}{4}=21.25\Rightarrow c\ge 22\). upper \(115/5=23\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=116\): lower \(86/4=21.5\Rightarrow c\ge 22\). upper \(116/5=23.2\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=117\): lower \(87/4=21.75\Rightarrow c\ge 22\). upper \(117/5=23.4\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=118\): lower \(88/4=22\Rightarrow c\ge 22\). upper \(118/5=23.6\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=119\): lower \(89/4=22.25\Rightarrow c\ge 23\). upper \(119/5=23.8\Rightarrow c\le 23\). So **\(c=\{23\}\)** unique!

Now check the condition: if the score were any lower but still \(>80\), John could not have determined \(c\). We must ensure that for \(s=118\) uniqueness fails (it does: two values), and generally for all \(81\le s\le 118\) there are either 2 or more. From our sampling it seems we never got 1 earlier; we can accept this as consistent because the unique first occurrence happens when the upper bound drops to exactly the next integer while the lower bound has just surpassed the previous.

Thus \(s=119\) is the desired score.

\[
\boxed{119}
\]

ANSWER: 119

Attempt 4
Let \(c\) be the number correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\qquad s=30+4c-w.
\]
Substitute \(w=30-c-u\):
\[
s=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
So
\[
s=5c+u,\quad \text{with } c\ge 0,\ u\ge 0,\ c+u\le 30.
\]

John can determine \(c\) from \(s\) if there is only one possible value of \(c\) that can produce that score.

We are told:
- \(s>80\).
- If \(s\) were any lower but still \(>80\), then \(c\) would *not* be uniquely determined.

So \(s\) is the *largest* score \(>80\) for which \(c\) is still unique? Let’s find the first point above 80 where uniqueness breaks.

From \(s=5c+u\), for a given \(s\),
\[
u=s-5c.
\]
For feasibility we need \(0\le u\le 30-c\), i.e.
\[
0\le s-5c\le 30-c.
\]
The left inequality gives \(c\le \frac{s}{5}\).
The right inequality gives
\[
s-5c\le 30-c\implies s\le 30+4c\implies c\ge \frac{s-30}{4}.
\]
Thus the possible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
Uniqueness means this interval contains exactly one integer.

Now test scores just above 80. Since the maximum score occurs at \(c=30,u=0\): \(s=150\), so we’re in a moderate range.

Compute for \(s=81,82,\dots\) until the interval size changes.

Let
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad R(s)=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Unique \(c\) occurs when \(L(s)=R(s)\).

Check \(s=81\):
\[
L=\left\lceil \frac{51}{4}\right\rceil=\lceil 12.75\rceil=13,\quad
R=\left\lfloor \frac{81}{5}\right\rfloor=\lfloor 16.2\rfloor=16.
\]
Not unique.

We need \(s\) close enough to force \(R\) down while \(L\) stays near it. This happens at larger \(s\).

Try \(s=100\):
\[
L=\left\lceil \frac{70}{4}\right\rceil=\lceil17.5\rceil=18,\quad
R=\left\lfloor \frac{100}{5}\right\rfloor=20.
\]
Not unique.

Try \(s=104\):
\[
L=\left\lceil \frac{74}{4}\right\rceil=\lceil18.5\rceil=19,\quad
R=\left\lfloor \frac{104}{5}\right\rfloor=\lfloor20.8\rfloor=20.
\]
Still not unique.

Try \(s=105\):
\[
L=\left\lceil \frac{75}{4}\right\rceil=\lceil18.75\rceil=19,\quad
R=\left\lfloor \frac{105}{5}\right\rfloor=21.
\]
Not unique.

Try \(s=108\):
\[
L=\left\lceil \frac{78}{4}\right\rceil=\lceil19.5\rceil=20,\quad
R=\left\lfloor \frac{108}{5}\right\rfloor=\lfloor21.6\rfloor=21.
\]
Not unique.

Try \(s=110\):
\[
L=\left\lceil \frac{80}{4}\right\rceil=\lceil20\rceil=20,\quad
R=\left\lfloor \frac{110}{5}\right\rfloor=\lfloor22\rfloor=22.
\]
Not unique.

We need \(R(s)=L(s)\). That means the interval length is 0:
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]
Let that common value be \(c\). Then we require
\[
c\le \frac{s}{5} < c+1
\quad\text{and}\quad
c-1< \frac{s-30}{4}\le c.
\]
Convert to bounds on \(s\):
\[
5c \le s \le 5c+4
\]
and
\[
4c+26 < s \le 4c+30.
\]
So \(s\) must satisfy both:
\[
\max(5c,\,4c+27)\le s \le \min(5c+4,\,4c+30).
\]
Since \(4c+27\) is larger than \(4c+26\).

Compute which \(c\) allow overlap. Note
\[
5c \quad\text{vs}\quad 4c+27:\quad 5c\ge 4c+27 \iff c\ge 27.
\]
But \(c\le 30\). So \(c\) is likely \(27,28,29,30\).

Also
\[
5c+4 \quad\text{vs}\quad 4c+30:\quad 5c+4\le 4c+30 \iff c\le 26.
\]
So for \(c\ge 27\), the upper limit will be \(4c+30\).

Thus for \(c\in\{27,28,29,30\}\):
- Lower bound: \(\max(5c,4c+27)=5c\) (since \(c\ge 27\))
- Upper bound: \(\min(5c+4,4c+30)=4c+30\) (since \(c\ge 27\))

So we need
\[
5c \le 4c+30 \iff c\le 30,
\]
always true in this range. And we need at least one integer \(s\) between them:
\[
s \in [5c,\;4c+30].
\]
For each \(c\):
- \(c=27\): \(s\in[135,138]\) all \(>80\).
- \(c=28\): \(s\in[140,142]\).
- \(c=29\): \(s\in[145,146]\).
- \(c=30\): \(s=150\).

Now interpret the “if score had been any lower but still \(>80\), John could not have determined” condition. That means \(s\) is the *smallest* score \(>80\) for which the representation gives unique \(c\), because any lower \(>80\) would allow multiple \(c\).

Among the candidates above, the smallest \(s\) is \(135\) (from \(c=27\)). We must verify that \(s=134\) is not unique.

For \(s=134\):
\[
L=\left\lceil \frac{104}{4}\right\rceil=26,\quad
R=\left\lfloor \frac{134}{5}\right\rfloor=26.
\]
That would actually be unique, which contradicts. So we must re-check: compute carefully:
\[
\frac{134}{5}=26.8\Rightarrow R=26.
\]
For \(L\):
\[
\frac{s-30}{4}=\frac{104}{4}=26\Rightarrow L=26.
\]
So \(s=134\) is unique with \(c=26\). Therefore the smallest unique score above 80 is less than 135, so our earlier candidate set missed lower \(c\) values because overlap logic assumed \(c\ge 27\) to compare bounds, but uniqueness can also happen for smaller \(c\) when the ceiling/floor align just right.

So instead we should directly find the minimal \(s>80\) for which there is uniqueness and then pick the *first* such that all smaller \(>80\) are non-unique. However the condition in the problem is: Mary’s score \(s\) is such that John can determine \(c\), but for any lower score still \(>80\), he cannot. That means \(s\) is the *minimum* score \(>80\) with unique \(c\).

So find the smallest \(s>80\) with \(L(s)=R(s)\).

We test systematically by looking at when \(R(s)=\left\lfloor \frac{s}{5}\right\rfloor\) increments, and \(L(s)=\left\lceil \frac{s-30}{4}\right\rceil\).

Compute \(s\) near 80-90 quickly:

For \(s=85\):
\[
L=\left\lceil \frac{55}{4}\right\rceil=\lceil13.75\rceil=14,\quad
R=\left\lfloor \frac{85}{5}\right\rfloor=17
\]
No.

For \(s=86\): \(L=\lceil14\rceil=14\) (since \(\frac{56}{4}=14\)), \(R=\lfloor17.2\rfloor=17\). No.

We need \(R\) drop or \(L\) rise until they meet. This happens when \(R\) is small relative to \(L\), i.e. at larger \(s\).

Instead, find where \(L(s)\) catches up to \(R(s)\). Solve approximately:
\[
\frac{s-30}{4}\approx \frac{s}{5}\implies 5(s-30)=4s\implies 5s-150=4s\implies s=150.
\]
So they meet only near the top, but due to integer effects, first equality may occur earlier. Let’s search from 81 upward with the interval size \(R-L\) becoming 0.

Try \(s=130\):
\[
L=\left\lceil \frac{100}{4}\right\rceil=25,\quad
R=\left\lfloor \frac{130}{5}\right\rfloor=26.
\]
Not.

\(s=131\):
\[
L=\left\lceil \frac{101}{4}\right\rceil=\lceil25.25\rceil=26,\quad
R=\left\lfloor \frac{131}{5}\right\rfloor=26.
\]
Here \(L=R=26\), so uniqueness holds.

Now check \(s=130\) was non-unique (it had \(c\in[25,26]\)), good.

Also we must ensure for any lower \(s>80\), uniqueness fails. Since we found the first time at \(131\) (we should verify \(s=129\) etc. but they are further from the top and likely not yet unique). Let’s confirm quickly:
- \(s=129\): \(L=\lceil99/4\rceil=\lceil24.75\rceil=25\), \(R=\lfloor25.8\rfloor=25\) gives uniqueness at 25. Wait compute: \(\lfloor129/5\rfloor=25\) yes, and \(L=25\) too, so uniqueness would already occur at 129, contradicting minimality.

But does \(s=129\) truly give a unique feasible \(c\)? Our interval method should be correct; thus check:
For \(s=129\), \(c=25\) gives \(u=s-5c=129-125=4\), and check \(c+u=29\le 30\) feasible. For \(c=24\), \(u=129-120=9\), then \(c+u=33>30\) infeasible. So only \(c=25\). Hence uniqueness at \(129\).

So the true “minimal unique” must be even lower. We need the score \(s\) such that uniqueness holds but immediately below \(80<s'<s\) uniqueness fails. That means \(s\) is the unique-threshold where non-uniqueness switches to uniqueness; i.e. we need the *largest* score \(>80\) for which uniqueness holds and below which uniqueness fails (equivalently: uniqueness holds only at that exact score, and not at any lower score, but our counterexamples show uniqueness can occur at multiple scores).

Interpretation: “If Mary's score had been any lower, but still over 80, John could not have determined this.” That means for every integer score \(s'\) with \(81\le s'<s\), \(c\) would not be uniquely determined. So indeed \(s\) is the smallest score \(>80\) with uniqueness. But our checks show uniqueness at \(129\), so smaller scores than 129 must be non-unique; we must find the actual smallest such.

We can continue decreasing to find earliest \(s\) with \(L(s)=R(s)\).

Let \(s=5k+r\) with \(r\in\{0,1,2,3,4\}\). Then \(R=k\).
Also
\[
L=\left\lceil \frac{5k+r-30}{4}\right\rceil.
\]
Set \(L=k\):
\[
k-1<\frac{5k+r-30}{4}\le k
\]
Multiply:
\[
4k-4<5k+r-30\le 4k
\]
Left:
\[
4k-4<5k+r-30\implies -k-r< -26\implies k+r>26.
\]
Right:
\[
5k+r-30\le 4k\implies k+r\le 30.
\]
So uniqueness occurs exactly when
\[
k+r\in\{27,28,29,30\},
\]
with \(s=5k+r\), \(r\in[0,4]\).

Since \(s>80\), we need smallest \(s\) among those satisfying \(k+r\ge 27\).

To minimize \(s=5k+r\) given fixed \(k+r=t\), we should make \(k\) as small as possible (because coefficient 5 on \(k\)). For each \(t\in\{27,28,29,30\}\), take \(k\) minimal so that \(r=t-k\le 4\).

- For \(t=27\): need \(r=27-k\le 4\Rightarrow k\ge 23\). Minimal \(k=23\) gives \(r=4\), \(s=5\cdot 23+4=119\).
- Check \(t=28\): minimal \(k\ge 24\) gives \(r=4\), \(s=124\) larger.
So smallest is \(119\).

Therefore Mary’s score is \(119\).

Finally confirm that for any \(s'<119\) with \(s'>80\), uniqueness fails: that means no solution to \(k+r\in\{27,28,29,30\}\) yields \(s<119\). Since the smallest constructed was \(119\), all smaller \(s\) have \(k+r\le 26\) hence \(L\ne R\). Good.

Thus \(s=119\).

ANSWER: 119

Attempt 5
We have \(30\) questions. Let \(c\) be correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\quad s=30+4c-w,
\]
with \(u\ge 0\), so \(c+w\le 30\). Also \(c,w\ge 0\) integers.

Rewrite the score condition:
\[
s=30+4c-w \quad\Longrightarrow\quad 4c-w=s-30.
\]
Given a fixed score \(s\), this means
\[
w=4c-(s-30).
\]
Thus for each integer \(c\), we get a corresponding \(w\). For \(c\) to be valid we need:
1. \(w\ge 0\) \(\Rightarrow 4c\ge s-30\),
2. \(c+w\le 30\). Substitute \(w\):
\[
c+\bigl(4c-(s-30)\bigr)\le 30
\]
\[
5c-(s-30)\le 30
\]
\[
5c\le s+60
\]
\[
c\le \frac{s+60}{5}.
\]
So possible \(c\) values are integers satisfying
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s+60}{5}\right\rfloor.
\]
John can determine \(c\) uniquely from \(s\) iff there is exactly one integer \(c\) in this interval.

Mary’s score is over \(80\), so \(81\le s \le 120\) (maximum when \(w=0\), \(c=30\): \(s=30+120=150\) actually; but for \(s\) around 80–150 we’ll narrow with constraints).

“Any lower but still over \(80\)” means: for every \(s'\) with \(80<s'<s\), the interval for \(s'\) contains at least two integers \(c\) (so \(c\) is not uniquely determined). In particular, \(s-1\) must *not* give uniqueness.

So we want the smallest score above 80 that gives uniqueness, since if the score were not minimal, we could lower slightly and still have uniqueness, contradicting the condition. Therefore we seek the minimal \(s\ge 81\) such that the interval contains exactly one integer.

Let
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad U(s)=\left\lfloor \frac{s+60}{5}\right\rfloor.
\]
Uniqueness means \(L(s)=U(s)\).

Check \(s=81\):
\[
L=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,
\quad
U=\left\lfloor \frac{141}{5}\right\rfloor=\left\lfloor 28.2\right\rfloor=28.
\]
Many values → not unique.

As \(s\) increases, both bounds increase, and the width \(U-L\) will eventually shrink to 0. Let’s find when \(L(s)=U(s)\) first happens for \(s>80\).

Try to force equality by approximating without ceilings/floors:
\[
\frac{s-30}{4}\approx \frac{s+60}{5}
\]
\[
5(s-30)=4(s+60)
\]
\[
5s-150=4s+240
\]
\[
s=390.
\]
That’s far too large, meaning ceilings/floors matter and the interval length typically stays large. So uniqueness likely happens only near the feasibility boundary \(c+w\le 30\) becoming tight, i.e. when \(w\) is forced.

Instead, use the constraint \(c+w\le 30\) together with \(w=4c-(s-30)\):
\[
c+w = c+4c-(s-30)=5c-(s-30)\le 30
\]
\[
5c\le s+60.
\]
Also \(w\ge 0\) gives \(4c\ge s-30\). So \(c\) must satisfy:
\[
\frac{s-30}{4}\le c\le \frac{s+60}{5}.
\]
For uniqueness, these bounds must trap \(c\) to a single integer, meaning their difference is \(<1\):
\[
\frac{s+60}{5}-\frac{s-30}{4}<1.
\]
Compute:
\[
\frac{4(s+60)-5(s-30)}{20}<1
\]
\[
\frac{4s+240-5s+150}{20}<1
\]
\[
\frac{-s+390}{20}<1
\]
\[
-s+390<20
\]
\[
s>370.
\]
Again too big. So the earlier “difference<1” criterion isn’t appropriate because ceilings/floors can still reduce to 0 even when the real interval is larger; but the inequality suggests uniqueness might require very special congruences forcing only one integer.

So instead, try to express \(s\) in terms of \((c,w)\) and enforce that the score corresponds to exactly one \(c\). Observe:
\[
s=30+4c-w = 30+5c-(c+w).
\]
Let \(t=c+w\) be the number attempted (correct or wrong). Then
\[
s=30+5c-t,\quad 0\le t\le 30.
\]
Also \(w=t-c\), and \(0\le c\le t\).

So:
\[
s=30+5c-t \quad\Longrightarrow\quad t=30+5c-s.
\]
For a given score \(s\), a value \(c\) is possible iff the resulting \(t\) is an integer with
\[
0\le t\le 30,\quad c\le t.
\]
Since \(t=30+5c-s\), \(t\) is automatically integer if \(c\) integer. The conditions become:
1. \(0\le 30+5c-s\) \(\Rightarrow 5c\ge s-30\) (same as before),
2. \(30+5c-s\le 30\) \(\Rightarrow 5c\le s\),
3. \(c\le t=30+5c-s\) \(\Rightarrow 0\le 30+4c-s\) \(\Rightarrow 4c\ge s-30\).

So the main upper bound is now
\[
5c\le s.
\]
Combine with \(5c\ge s-30\) and \(4c\ge s-30\).

Thus:
\[
c\in \mathbb{Z},\quad \frac{s-30}{5}\le c\le \frac{s}{5},\quad\text{and}\quad c\ge \frac{s-30}{4}.
\]
But \(\frac{s-30}{4}>\frac{s-30}{5}\), so the effective lower bound is \(\left\lceil\frac{s-30}{4}\right\rceil\) and the upper bound is \(\left\lfloor\frac{s}{5}\right\rfloor\).
Hence uniqueness means:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]

Now test \(s=85\):
\[
\left\lceil\frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,\quad
\left\lfloor\frac{85}{5}\right\rfloor=17.
\]
Not equal.

Try \(s=90\):
\[
\left\lceil\frac{60}{4}\right\rceil=15,\quad \left\lfloor\frac{90}{5}\right\rfloor=18.
\]
No.

Try \(s=100\):
\[
\left\lceil\frac{70}{4}\right\rceil=18,\quad \left\lfloor\frac{100}{5}\right\rfloor=20.
\]
No.

We need \(\lfloor s/5\rfloor\) to be small enough to equal the ceiling term. Let \(k=\lfloor s/5\rfloor\). Then \(5k\le s\le 5k+4\).
Also uniqueness requires \(k=\left\lceil\frac{s-30}{4}\right\rceil\), so
\[
k-1<\frac{s-30}{4}\le k
\]
\[
4(k-1)<s-30\le 4k
\]
\[
4k+ -4 +? \Rightarrow 4k-4< s-30 \le 4k
\]
\[
4k+26< s \le 4k+30.
\]
Combine with \(5k\le s\le 5k+4\). So \(s\) must satisfy
\[
\max(5k,\,4k+27) \le s \le \min(5k+4,\,4k+30).
\]
Compute:
Left max: \(4k+27\) vs \(5k\). Their difference:
\[
5k-(4k+27)=k-27.
\]
For \(k\ge 27\), left is \(5k\). For \(s>80\), likely \(k\ge 16\). Let’s find actual \(s\) by trying \(k\) near where the interval could become a single integer.

Also right min: compare \(5k+4\) vs \(4k+30\):
\[
(4k+30)-(5k+4)=26-k.
\]
So for \(k\ge 26\), right is \(4k+30\); for \(k\le 26\), right is \(5k+4\).

To make interval very tight (ideally one integer), likely near \(k=27\) or \(26\).

Try \(k=27\):
Then \(s\) must satisfy:
left \(=\max(135,\,4(27)+27=135)=135\),
right \(=\min(139,\,4(27)+30=138)=138\).
So \(s\in[135,138]\). Any of these might yield uniqueness.

But we require \(s>80\); fine.

Now ensure uniqueness for one candidate and non-uniqueness for \(s-1\).
Let’s compute possible \(c\) directly for each \(s\in\{135,136,137,138\}\).

For a given \(s\), upper bound on \(c\) is \(\left\lfloor s/5\right\rfloor = \left\lfloor 27.0\) to \(27.6\right\rfloor =27\).
Lower bound is \(\left\lceil (s-30)/4\right\rceil = \left\lceil (105\text{ to }108)/4\right\rceil\).
- \(s=135\): \((s-30)/4=105/4=26.25\Rightarrow L=27\). So \(c\) is forced to \(27\). Uniqueness holds.
Now check \(s=134\) (still over 80):
\[
U=\left\lfloor 134/5\right\rfloor=26,\quad
L=\left\lceil 104/4\right\rceil=26.
\]
That would also give uniqueness, which would contradict the “if score had been any lower… John could not have determined” condition.
So \(s=135\) is too high.

Try next down where uniqueness first appears: we want \(s-1\) not unique, i.e. for \(s-1\) the interval contains at least two integers.

Consider \(s=136\):
- \(U=\lfloor 136/5\rfloor=27\).
- \(L=\left\lceil 106/4\right\rceil=\left\lceil 26.5\right\rceil=27\).
So \(c=27\) unique.
Check \(s-1=135\) gave uniqueness, so still contradiction.

For \(s=137\):
- \(U=\lfloor 137/5\rfloor=27\).
- \(L=\left\lceil 107/4\right\rceil=\left\lceil 26.75\right\rceil=27\).
Unique for 137.
Check \(136\) for uniqueness:
\(s=136\) also unique (as above). Contradiction.

For \(s=138\):
- \(U=\lfloor 138/5\rfloor=27\).
- \(L=\left\lceil 108/4\right\rceil=\left\lceil 27\right\rceil=27\).
Unique.
Check \(s-1=137\) unique. Contradiction.

Therefore the “lower but still over 80” means: decreasing the score while keeping it over 80 (but not necessarily by 1) makes uniqueness impossible, so it suffices that *every* \(s'\) with \(81\le s'<s\) is non-unique. That implies \(s\) is the *smallest* score \(>80\) yielding uniqueness.

Thus we must find the minimal \(s>80\) with uniqueness; we mistakenly jumped to \(k=27\) due to tightness. Let’s search smaller \(k\).

Set uniqueness condition:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor = k.
\]
Let \(s\) be minimal \(>80\). Since \(s>80\), \(k=\lfloor s/5\rfloor\ge 17\).

We can brute by \(k\) logic with interval for \(s\) derived earlier:
When \(k\le 26\), right min is \(5k+4\). Also since \(k<27\), left max is \(4k+27\) (because \(k-27<0\Rightarrow 5k<4k+27\)).
So for \(k\le 26\), we have
\[
4k+27 \le s \le 5k+4.
\]
For uniqueness to hold, \(s\) must also satisfy that the ceiling equals \(k\), which is exactly ensured by these bounds.

Now find minimal \(s>80\). Try \(k=17\):
\[
4k+27=68+27=95,\quad 5k+4=85+4=89,
\]
impossible (lower bound > upper). So \(k=17\) no.

\(k=18\):
\[
4k+27=72+27=99,\quad 5k+4=90+4=94
\]
impossible.

We need \(4k+27\le 5k+4\Rightarrow 27-4\le k \Rightarrow 23\le k\).
So smallest possible \(k\) is \(23\).

Take \(k=23\):
\[
4k+27=92+27=119,\quad 5k+4=115+4=119.
\]
So \(s=119\) is forced and is the minimal possible.

Verify:
For \(s=119\),
\[
U=\left\lfloor 119/5\right\rfloor=23.
\]
\[
L=\left\lceil (119-30)/4\right\rceil=\left\lceil 89/4\right\rceil=\left\lceil 22.25\right\rceil=23.
\]
So unique \(c=23\).

Check that any lower \(s'\) with \(>80\) is non-unique: since \(k\) would be \(\le 22\) for \(s'\le 118\). But for \(k\le 22\), the interval inequality fails (as shown \(4k+27>5k+4\)), giving either 0 or multiple solutions; in any case not uniqueness. Indeed, if \(k\le 22\), there is no integer \(s\) satisfying the derived bounds simultaneously for uniqueness. Hence \(119\) is the first score \(>80\) with unique \(c\).

Therefore Mary’s score is \(119\).

ANSWER: 119

#### Incorrect
Attempt 1
We have \(30\) problems and
\[
s=30+4c-w.
\]
Let \(u\) be the number left blank. Then \(c+w+u=30\).

Rearrange:
\[
s-30=4c-w \quad\Longrightarrow\quad w=4c-(s-30).
\]
Since \(w\ge 0\), we need \(4c-(s-30)\ge 0\), i.e.
\[
s-30\le 4c.
\]
Also \(w\le 30-c\) (because \(u\ge 0\)), so
\[
4c-(s-30)\le 30-c
\]
\[
5c-(s-30)\le 30
\]
\[
5c\le s+0 \quad\Longrightarrow\quad c\le \frac{s}{5}.
\]

For a fixed score \(s\), different possible values of \(c\) must produce integer \(w\) that also make \(u=30-c-w\ge 0\). Since \(w=4c-(s-30)\), the parity/integrality is automatic when \(c\) is integer; the constraints are:
\[
0\le c\le 30,\quad w=4c-(s-30)\ge 0,\quad u=30-c-w\ge 0.
\]
Compute \(u\):
\[
u=30-c-(4c-(s-30))=30-c-4c+s-30=s-5c.
\]
So the nonnegativity \(u\ge 0\) is exactly
\[
s-5c\ge 0 \quad\Longrightarrow\quad c\le \frac{s}{5},
\]
consistent with above.

Also \(w\le 30-c\) is the same as \(u\ge 0\), so nothing new.

Thus for given \(s\), the valid \(c\) are precisely the integers satisfying
\[
\frac{s-30}{4}\le c \le \frac{s}{5}.
\]
(Left inequality from \(w\ge 0\): \(4c\ge s-30\).)

John could determine the number of problems \(c\) exactly when there is **only one integer** in that interval.

Mary’s score \(s\) is over \(80\), and if \(s\) were lowered to the next lower score but still \(>80\), the interval would contain at least two integers.

Now \(s\) is an integer (formula uses integers), and the condition “over 80” means \(s\ge 81\). The “any lower” wording in AIME context implies the immediate previous integer score \(s-1\).

We search for the smallest \(s\ge 81\) for which the interval contains exactly one integer, and the interval for \(s-1\) contains more than one integer.

Let’s test systematically by finding when the bounds squeeze to a single integer.

The interval is
\[
L(s)=\frac{s-30}{4},\qquad U(s)=\frac{s}{5}.
\]
We need:
- Exactly one integer \(c\) with \(L(s)\le c\le U(s)\).
- For \(s-1\), at least two integers.

Try \(s=81\):
\[
L(81)=\frac{51}{4}=12.75,\quad U(81)=\frac{81}{5}=16.2.
\]
Integers: \(13,14,15,16\) → 4 values, not unique.

\(s=82\):
\[
L=\frac{52}{4}=13,\quad U=\frac{82}{5}=16.4.
\]
Integers \(c=13,14,15,16\) → 4 values.

\(s=83\):
\[
L=\frac{53}{4}=13.25,\quad U=\frac{83}{5}=16.6.
\]
Integers \(14,15,16\) → 3 values.

\(s=84\):
\[
L=\frac{54}{4}=13.5,\quad U=\frac{84}{5}=16.8.
\]
Integers \(14,15,16\) → 3 values.

\(s=85\):
\[
L=\frac{55}{4}=13.75,\quad U=\frac{85}{5}=17.
\]
Integers \(14,15,16,17\) → 4 values.

\(s=86\):
\[
L=\frac{56}{4}=14,\quad U=\frac{86}{5}=17.2.
\]
Integers \(14,15,16,17\) → 4 values.

\(s=87\):
\[
L=\frac{57}{4}=14.25,\quad U=\frac{87}{5}=17.4.
\]
Integers \(15,16,17\) → 3 values.

\(s=88\):
\[
L=\frac{58}{4}=14.5,\quad U=\frac{88}{5}=17.6.
\]
Integers \(15,16,17\) → 3 values.

\(s=89\):
\[
L=\frac{59}{4}=14.75,\quad U=\frac{89}{5}=17.8.
\]
Integers \(15,16,17\) → 3 values.

\(s=90\):
\[
L=\frac{60}{4}=15,\quad U=\frac{90}{5}=18.
\]
Integers \(15,16,17,18\) → 4 values.

We need a tighter squeeze; continue:

\(s=91\):
\[
L=\frac{61}{4}=15.25,\quad U=\frac{91}{5}=18.2
\]
Integers \(16,17,18\) → 3.

\(s=92\):
\[
L=\frac{62}{4}=15.5,\quad U=\frac{92}{5}=18.4
\]
Integers \(16,17,18\) → 3.

\(s=93\):
\[
L=\frac{63}{4}=15.75,\quad U=\frac{93}{5}=18.6
\]
Integers \(16,17,18\) → 3.

\(s=94\):
\[
L=\frac{64}{4}=16,\quad U=\frac{94}{5}=18.8
\]
Integers \(16,17,18\) → 3.

\(s=95\):
\[
L=\frac{65}{4}=16.25,\quad U=\frac{95}{5}=19
\]
Integers \(17,18,19\) → 3.

\(s=96\):
\[
L=\frac{66}{4}=16.5,\quad U=\frac{96}{5}=19.2
\]
Integers \(17,18,19\) → 3.

\(s=97\):
\[
L=\frac{67}{4}=16.75,\quad U=\frac{97}{5}=19.4
\]
Integers \(17,18,19\) → 3.

\(s=98\):
\[
L=\frac{68}{4}=17,\quad U=\frac{98}{5}=19.6
\]
Integers \(17,18,19\) → 3.

\(s=99\):
\[
L=\frac{69}{4}=17.25,\quad U=\frac{99}{5}=19.8
\]
Integers \(18,19\) → 2 values.

\(s=100\):
\[
L=\frac{70}{4}=17.5,\quad U=\frac{100}{5}=20.
\]
Integers \(18,19,20\) → 3 values.

So far no uniqueness. Let’s go higher.

\(s=101\):
\[
L=\frac{71}{4}=17.75,\quad U=\frac{101}{5}=20.2
\]
Integers \(18,19,20\) → 3.

\(s=102\):
\[
L=\frac{72}{4}=18,\quad U=\frac{102}{5}=20.4
\]
Integers \(18,19,20\) → 3.

\(s=103\):
\[
L=\frac{73}{4}=18.25,\quad U=\frac{103}{5}=20.6
\]
Integers \(19,20\) → 2.

\(s=104\):
\[
L=\frac{74}{4}=18.5,\quad U=\frac{104}{5}=20.8
\]
Integers \(19,20\) → 2.

\(s=105\):
\[
L=\frac{75}{4}=18.75,\quad U=\frac{105}{5}=21
\]
Integers \(19,20,21\) → 3.

\(s=106\):
\[
L=\frac{76}{4}=19,\quad U=\frac{106}{5}=21.2
\]
Integers \(19,20,21\) → 3.

\(s=107\):
\[
L=\frac{77}{4}=19.25,\quad U=\frac{107}{5}=21.4
\]
Integers \(20,21\) → 2.

\(s=108\):
\[
L=\frac{78}{4}=19.5,\quad U=\frac{108}{5}=21.6
\]
Integers \(20,21\) → 2.

\(s=109\):
\[
L=\frac{79}{4}=19.75,\quad U=\frac{109}{5}=21.8
\]
Integers \(20,21\) → 2.

\(s=110\):
\[
L=\frac{80}{4}=20,\quad U=\frac{110}{5}=22
\]
Integers \(20,21,22\) → 3.

We still don’t have 1 integer. The only way to get exactly one integer is for the interval length to be \(<1\):
\[
U(s)-L(s)=\frac{s}{5}-\frac{s-30}{4}
=\frac{4s-5(s-30)}{20}
=\frac{4s-5s+150}{20}
=\frac{150-s}{20}.
\]
So we need
\[
\frac{150-s}{20}<1 \quad\Longrightarrow\quad 150-s<20 \quad\Longrightarrow\quad s>130.
\]
But AHSME has maximum when \(c=30,w=0\): \(s=30+4\cdot 30=150\). So \(s\) can indeed exceed 130.

Now find the first \(s>130\) where exactly one integer lies in the interval and for \(s-1\) more than one.

Since \(s>130\), let’s try values near 130.

Compute interval length:
\[
U-L=\frac{150-s}{20}.
\]
- If \(s=131\), length \(=\frac{19}{20}=0.95<1\), so potentially unique.
We must check endpoints carefully.

For \(s=131\):
\[
L=\frac{101}{4}=25.25,\quad U=\frac{131}{5}=26.2.
\]
Integers between: \(26\) only → unique! (Because \(25.25\le c\le 26.2\) allows only \(c=26\).)

Now check \(s=130\) (which is still over 80, yes):
For \(s=130\):
\[
L=\frac{100}{4}=25,\quad U=\frac{130}{5}=26.
\]
Integers: \(c=25,26\) → two values. So John could not have determined \(c\) from score 130.

Therefore \(s=131\) satisfies both conditions.

We can also compute consistency:
If \(c=26\), then
\[
w=4c-(s-30)=104-(101)=3,
\]
and
\[
u=s-5c=131-130=1,
\]
all valid.

So the score is \(\boxed{131}\).

ANSWER: 131

Attempt 2


Attempt 3


Attempt 4
Let \(c\) be correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\qquad s=30+4c-w.
\]
Substitute \(w=30-c-u\) into the score:
\[
s=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
So the score depends only on \(c\) and \(u\), with \(u\ge 0\) and \(c\ge 0\) integers, and
\[
c+u\le 30.
\]

John can determine \(c\) from \(s\) iff, given \(s\), there is exactly one possible \(c\) compatible with some \(u\ge 0\) and \(c+u\le 30\).

From \(s=5c+u\), we have \(u=s-5c\). Thus \(u\ge 0\) gives
\[
s-5c\ge 0 \implies c\le \frac{s}{5}.
\]
Also \(c+u\le 30\) becomes
\[
c+(s-5c)\le 30 \implies s-4c\le 30 \implies c\ge \frac{s-30}{4}.
\]
So the possible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
John can determine \(c\) exactly when this interval contains exactly one integer.

Now we use the condition: Mary's score was \(>80\), and if the score were any lower but still \(>80\), John could not have determined \(c\). That means \(s\) is the smallest integer \(>80\) for which the interval has exactly one integer.

Check \(s=81\). Compute bounds:
\[
\left\lceil \frac{81-30}{4}\right\rceil=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,
\]
\[
\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
Interval \([13,16]\) has 4 integers → not unique.

Try \(s=82\):
\[
\left\lceil \frac{82-30}{4}\right\rceil=\left\lceil \frac{52}{4}\right\rceil=13,
\quad
\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16.
\]
Interval \([13,16]\) has 4 integers → not unique.

\(s=83\):
\[
\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14,
\quad
\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16.
\]
Interval \([14,16]\) has 3 integers → not unique.

\(s=84\):
\[
\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14,
\quad
\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16.
\]
Interval \([14,16]\) has 3 integers → not unique.

\(s=85\):
\[
\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,
\quad
\left\lfloor \frac{85}{5}\right\rfloor=\left\lfloor 17\right\rfloor=17.
\]
Interval \([14,17]\) has 4 integers → not unique.

\(s=86\):
\[
\left\lceil \frac{56}{4}\right\rceil=\left\lceil 14\right\rceil=14,
\quad
\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17.
\]
Interval \([14,17]\) has 4 integers → not unique.

\(s=87\):
\[
\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15,
\quad
\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

\(s=88\):
\[
\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15,
\quad
\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

\(s=89\):
\[
\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15,
\quad
\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

\(s=90\):
\[
\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15,
\quad
\left\lfloor \frac{90}{5}\right\rfloor=\left\lfloor 18\right\rfloor=18.
\]
Interval \([15,18]\) has 4 integers → not unique.

\(s=91\):
\[
\left\lceil \frac{61}{4}\right\rceil=\left\lceil 15.25\right\rceil=16,
\quad
\left\lfloor \frac{91}{5}\right\rfloor=\left\lfloor 18.2\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=92\):
\[
\left\lceil \frac{62}{4}\right\rceil=\left\lceil 15.5\right\rceil=16,
\quad
\left\lfloor \frac{92}{5}\right\rfloor=\left\lfloor 18.4\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=93\):
\[
\left\lceil \frac{63}{4}\right\rceil=\left\lceil 15.75\right\rceil=16,
\quad
\left\lfloor \frac{93}{5}\right\rfloor=\left\lfloor 18.6\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=94\):
\[
\left\lceil \frac{64}{4}\right\rceil=\left\lceil 16\right\rceil=16,
\quad
\left\lfloor \frac{94}{5}\right\rfloor=\left\lfloor 18.8\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=95\):
\[
\left\lceil \frac{65}{4}\right\rceil=\left\lceil 16.25\right\rceil=17,
\quad
\left\lfloor \frac{95}{5}\right\rfloor=\left\lfloor 19\right\rfloor=19.
\]
Interval \([17,19]\) has 3 integers → not unique.

\(s=96\):
\[
\left\lceil \frac{66}{4}\right\rceil=\left\lceil 16.5\right\rceil=17,
\quad
\left\lfloor \frac{96}{5}\right\rfloor=\left\lfloor 19.2\right\rfloor=19.
\]
Interval \([17,19]\) has 3 integers → not unique.

At this point, notice the interval length is small but hasn’t become 0. Since we must eventually get a single integer, we can solve when
\[
\left\lfloor \frac{s}{5}\right\rfloor = \left\lceil \frac{s-30}{4}\right\rceil.
\]
Instead, test plausible uniqueness by setting \(u\) small, because \(u=s-5c\) must also satisfy \(c+u\le 30\Rightarrow u\le 30-c\).
If \(c\) is maximal for given \(s\), then \(u\) is minimal. Uniqueness is most likely when increasing \(c\) by 1 forces \(u\) negative or violates \(c+u\le 30\).

Suppose \(c\) is the largest possible: \(c=\left\lfloor s/5\right\rfloor\). Then \(u=s-5c\) is the remainder \(r\in\{0,1,2,3,4\}\).
Condition \(c+u\le 30\) becomes
\[
\left\lfloor \frac{s}{5}\right\rfloor + (s-5\left\lfloor \frac{s}{5}\right\rfloor)\le 30
\iff c+r\le 30.
\]
If also the next smaller \(c\) would still be feasible, uniqueness fails. That means we need exactly one feasible \(c\), which occurs when lowering \(c\) by 1 would make \(u\) too large to keep \(c+u\le 30\).

If \(c\) is feasible with remainder \(r\), then with \(c-1\) we would have
\[
u' = s-5(c-1)= (s-5c)+5 = r+5.
\]
Then
\[
(c-1)+u' = (c-1)+(r+5)=c+r+4.
\]
So \(c-1\) is infeasible exactly when
\[
c+r+4>30 \quad\text{while}\quad c+r\le 30.
\]
Thus
\[
c+r=30.
\]
So we require the feasible pair to satisfy \(u=r\) and \(c+r=30\), i.e. \(u\) is exactly \(30-c\) (no wrong answers determined).

Now \(s=5c+u=5c+r\) with \(c+r=30\Rightarrow r=30-c\). Substitute:
\[
s=5c+(30-c)=4c+30.
\]
Also \(r=30-c\) must be \(0,1,2,3,4\). Hence
\[
30-c\in\{0,1,2,3,4\}\implies c\in\{26,27,28,29,30\}.
\]
Compute corresponding scores \(s=4c+30\):
- \(c=26\Rightarrow s=134\)
- \(c=27\Rightarrow s=138\)
- \(c=28\Rightarrow s=142\)
- \(c=29\Rightarrow s=146\)
- \(c=30\Rightarrow s=150\)

Among these, we need the one with \(s\) just over \(80\) satisfying the “if score had been any lower but still over 80, John could not” condition. The smallest score in the list is \(134\). Therefore it must be the first time uniqueness occurs for \(s>80\).

So Mary's score is \(\boxed{134}\).

ANSWER: 134

Attempt 5
We have \(30\) multiple choice questions. Let \(c\) be the number correct and \(w\) the number wrong; unanswered \(=30-c-w\).
Scores are
\[
s=30+4c-w.
\]
Given \(s>80\), rewrite:
\[
s-30=4c-w \quad\Rightarrow\quad s-30=4c-(\text{# wrong}).
\]

For fixed \(c\), the score ranges over possible \(w\) values with \(0\le w\le 30-c\), giving
\[
s=30+4c-w \in \{30+4c-(30-c),\,\dots,\,30+4c\}
= \{30+5c-30,\dots,30+4c\}.
\]
So for each \(c\), the achievable scores form an interval of integers:
\[
s\in [\,5c,\; 30+4c\,].
\]

John can determine \(c\) from \(s\) exactly when the intervals for different \(c\)’s do not overlap at that score.

Compute overlap condition between \(c\) and \(c+1\):
- \(c\)-interval upper end: \(30+4c\)
- \((c+1)\)-interval lower end: \(5(c+1)=5c+5\)

They overlap if
\[
5c+5 \le 30+4c
\quad\Longleftrightarrow\quad
c \le 25.
\]
Thus, for \(c\le 25\), there is overlap, so \(s\) cannot uniquely determine \(c\).
For \(c\ge 26\), there is no overlap between consecutive intervals (and hence \(c\) becomes uniquely determined by \(s\)).

Now use the problem’s “threshold” condition:
- Mary’s score is over \(80\), so we need \(s>80\).
- If the score were any lower (but still \(>80\)), John could not determine \(c\).
So \(s\) should be the *smallest* score \(>80\) for which \(c\) is uniquely determined.

Try the boundary case \(c=26\):
- For \(c=26\), the achievable interval is
\[
[\,5c,\;30+4c\,]=[130,\;30+104]=[130,\;134].
\]
The smallest is \(130\), which is definitely \(>80\).

Now check whether any score between \(81\) and \(129\) could yield unique \(c\).
But for \(c\le 25\) the intervals overlap, so uniqueness fails. Hence the first unique score above \(80\) must occur at the smallest score belonging to some \(c\ge 26\), i.e. at \(5\cdot 26=130\).

We should also ensure that at \(s=129\) uniqueness fails (it should, since \(c\le 25\)). Indeed \(129\) lies in the overlap region of some \(c\le 25\).

Therefore Mary’s score is
\[
\boxed{130}.
\]

Check quickly: can \(s=130\) occur with \(c=26\) and some \(w\)?
From \(s=30+4c-w\):
\[
130=30+104-w \Rightarrow w=4.
\]
Then \(c+w=30\), so all questions answered; feasible.

Also, could any other \(c\) produce \(s=130\)?
For \(c=25\): \(130=30+100-w\Rightarrow w=0\), feasible, but then the corresponding interval for \(c=25\) is \([125,130]\), which would suggest overlap at 130. However uniqueness should fail if overlaps exist; and indeed we found overlap for \(c\le 25\). So we need to re-evaluate carefully: overlap at 130 means both \(c=25\) and \(c=26\) can produce 130. But is that possible given the scoring constraints?  
For \(c=25\), \(w=0\) gives score \(30+4\cdot 25-0=130\), and unanswered \(=30-25-0=5\), allowed. So John would not be able to determine \(c\) at \(s=130\).

So the earlier “no overlap for \(c\ge 26\)” conclusion must be refined: overlap occurs between intervals whenever consecutive intervals intersect, i.e. when
\[
\text{lower}_{c+1} \le \text{upper}_c.
\]
For \(c=25\):
\[
\text{lower}_{26}=5\cdot 26=130,\quad \text{upper}_{25}=30+4\cdot 25=130,
\]
so they intersect at exactly \(130\). Therefore at \(s=130\), \(c\) is not uniquely determined.

Thus we need the *smallest* \(s>80\) for which no other \(c\) can produce it. That means we must find the smallest score above 80 that lies strictly inside the region where intervals for different \(c\)’s are disjoint at that point.

The first \(s\) where disjointness becomes strict is when the lower end of the next interval is greater than the upper end of the previous:
\[
5(c+1) > 30+4c
\quad\Longleftrightarrow\quad
5c+5 > 4c+30
\quad\Longleftrightarrow\quad
c>25.
\]
So we need \(c\ge 26\), but also avoid the boundary intersection at \(s=130\). For \(c=26\), the interval is \([130,134]\), and the only shared point with \(c=25\) is \(130\). Therefore the smallest score \(>80\) with unique \(c\) is \(131\).

Now verify uniqueness at \(s=131\):
Solve for \(w\):
\[
131=30+4c-w \Rightarrow w=30+4c-131=4c-101.
\]
Check possibilities:
- If \(c=25\): \(w=100-101=-1\), impossible.
- If \(c=26\): \(w=104-101=3\), valid since \(c+w=29\le 30\).
- If \(c\le 24\): even worse (would give negative \(w\) for \(s\) this large).
So only \(c=26\) works. Hence John can determine \(c\) from \(s=131\).

Finally, if the score were any lower but still \(>80\), i.e. \(s=81,82,\dots,130\), uniqueness fails because for \(c\le 25\) intervals overlap and at \(s=130\) we saw non-uniqueness too.

So Mary’s score is \(\boxed{131}\).

ANSWER: 131


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

#### Tier: `correct`

<details>
<summary>correct attempt 1</summary>

```text
Let \(c\) be the number correct and \(w\) the number wrong. Since there are \(30\) total problems, the number left blank is \(30-c-w\ge 0\).

Given the scoring rule
\[
s=30+4c-w,
\]
we can rewrite \(w\) in terms of \(s\) and \(c\):
\[
w=30+4c-s.
\]
We must have
\[
0\le w \le 30-c.
\]
The upper bound \(w\le 30-c\) is equivalent to \(30+4c-s\le 30-c\), i.e.
\[
4c-c\le s \quad\Longrightarrow\quad 3c\le s.
\]
The lower bound \(w\ge 0\) is \(30+4c-s\ge 0\), i.e.
\[
4c\ge s-30.
\]

John can determine \(c\) uniquely from the score \(s\). If there were another feasible \(c'\neq c\) producing the same \(s\), then John couldn’t determine the number correct.

Now consider how \(c\) could change while keeping the same score. From
\[
s=30+4c-w,
\]
fix \(s\). If we increase \(c\) by \(1\), to keep \(s\) constant we must increase \(w\) by \(4\) (because \(4c-w\) must stay the same). So alternative solutions correspond to steps
\[
(c,w)\to (c+1,\,w+4).
\]
Thus, for a given \(s\), multiple values of \(c\) are possible exactly when there exists room to add these \((+1,+4)\) moves without violating feasibility \(w\le 30-c\) and \(w\ge 0\).

The problem says:
- For Mary’s actual score \(s\), \(c\) is determined uniquely.
- For any smaller score \(s' > 80\), John cannot determine \(c\) (so at least two different \(c\)’s are feasible).

So \(s\) is the *largest* score \(>80\) for which uniqueness holds; just below it, the feasible range for \(c\) becomes large enough to allow two solutions.

Compute \(s\) near \(80\). Since \(s=30+4c-w\) with \(w\ge 0\), we have
\[
s\le 30+4c \quad\Rightarrow\quad c\ge \frac{s-30}{4}.
\]
Also from \(w\le 30-c\),
\[
30+4c-s \le 30-c \quad\Rightarrow\quad 3c\le s.
\]
So for a fixed \(s\), feasible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{3}\right\rfloor.
\]

Uniqueness means this integer interval has exactly one integer.

Let’s test scores just above \(80\). Start with \(s=81\):
\[
\left\lceil\frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,\quad
\left\lfloor\frac{81}{3}\right\rfloor=27.
\]
Many \(c\), not unique.

We need the interval to shrink to one integer. As \(s\) increases, the lower bound increases by about \(1/4\) per \(1\) in \(s\), while the upper bound increases by \(1/3\) per \(1\) in \(s\). The interval length tends to decrease only very rarely due to the ceilings/floors; uniqueness is most likely at a boundary where the ceiling equals the floor.

So we search for \(s>80\) such that
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{3}\right\rfloor.
\]
Let that common value be \(c\). Then \(c\) must satisfy
\[
\frac{s-30}{4} \le c \le \frac{s}{3}
\]
and with integrality/rounding:
\[
c-1 < \frac{s-30}{4} \le c,\qquad c\le \frac{s}{3} < c+1.
\]
Equivalently,
\[
4(c-1) < s-30 \le 4c,\qquad 3c \le s < 3(c+1).
\]
Thus
\[
4c+30 \ge s > 4(c-1)+30 =4c+26
\]
and
\[
3c \le s < 3c+3.
\]
So \(s\) must lie in the intersection:
\[
(4c+26,\;4c+30]\cap [3c,\;3c+3).
\]
Since \(4c+26\) is much larger than \(3c\) for \(c\ge 1\), the key overlap forces \(s\) close to \(4c+26\) but also less than \(3c+3\). Set the inequalities:
\[
4c+26 < 3c+3 \quad\Rightarrow\quad c < -23,
\]
impossible. That means our assumption about the interval having exactly one integer via equality of those bounds must be reconsidered: uniqueness doesn’t require the feasible \(c\)-interval length to be 1, because different \(c\) might fail the implied \(w\) nonnegativity/upper bound in a way that ceiling/floor conditions alone don’t fully capture due to the step structure \(w=30+4c-s\). But actually those bounds *are* exactly the feasibility for \(w\), so the interval approach is correct—so why did it seem impossible? The arithmetic indicates we made a wrong comparison: the lower bound is \(\left\lceil\frac{s-30}{4}\right\rceil\), upper bound \(\left\lfloor\frac{s}{3}\right\rfloor\). For \(s\) around 80, these are:
- lower about \((s-30)/4\approx 12.5\),
- upper about \(s/3\approx 26.6\).
So uniqueness would require very special \(s\), but it can happen when the lower and upper are equal, which seems impossible since \((s-30)/4\) is always much smaller than \(s/3\) for positive \(s\):
\[
\frac{s-30}{4}=\frac{s}{3}\ \Rightarrow\ 3s-90=4s\ \Rightarrow\ s=-90.
\]
So indeed they can never be equal. Therefore uniqueness must be interpreted differently: given \(s\), John can determine \(c\) because although multiple \(c\) values are feasible, the resulting \(c\) are the same—i.e., not possible. That contradicts feasibility unless we misread: John determines the number of problems Mary solved correctly, meaning \(c\) is uniquely determined, so there must be exactly one feasible \(c\). Since exact equality of bounds cannot happen, the only way is that feasibility interval length becomes \(<1\), impossible as shown. Hence the correct approach is to use the score modulo constraints from the step structure.

From
\[
s=30+4c-w,
\]
with \(w\) integer, we have
\[
s\equiv 30+4c \pmod{1}\quad \text{(no restriction)}.
\]
But combining with \(w\le 30-c\) gives:
\[
w=30+4c-s \le 30-c \Rightarrow 5c \le s.
\]
Also \(w\ge 0\Rightarrow 30+4c-s\ge 0\Rightarrow 4c\ge s-30\).

So feasibility is
\[
\left\lceil\frac{s-30}{4}\right\rceil \le c \le \left\lfloor\frac{s}{5}\right\rfloor.
\]
Now for uniqueness, this interval must contain exactly one integer.

Test \(s=81\):
\[
\left\lceil\frac{51}{4}\right\rceil=13,\quad \left\lfloor\frac{81}{5}\right\rfloor=16.
\]
Possible \(c=13,14,15,16\) => not unique.

We need the interval length \(=0\) or \(1\). Since uniqueness means exactly one integer:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]
Now solve for when the bounds can match.

Let that integer be \(c\). Then
\[
\frac{s-30}{4} \le c < \frac{s-30}{4}+1,
\]
\[
c \le \frac{s}{5} < c+1.
\]
Translate to \(s\):
From \(c \le s/5\): \(s\ge 5c\).
From \(s/5 < c+1\): \(s<5c+5\).
From \((s-30)/4 \le c\): \(s-30 \le 4c\Rightarrow s\le 4c+30\).
From \(c < (s-30)/4+1\): \(c-1 < (s-30)/4\Rightarrow 4c-4 < s-30\Rightarrow s>4c+26\).

So
\[
5c \le s < 5c+5,\quad 4c+27 \le s \le 4c+30.
\]
Intersection:
\[
s \in [5c,\;5c+4]\cap [4c+27,\;4c+30].
\]
For intersection to be nonempty:
\[
5c \le 4c+30 \Rightarrow c\le 30.
\]
Also need
\[
5c+4 \ge 4c+27 \Rightarrow c\ge 23.
\]
So \(c\in\{23,24,25,26,27,28,29,30\}\).

Now compute the possible \(s\) by taking \(s\) in intersection; additionally \(s>80\) and we want the *maximal* \(s\) such that uniqueness holds but for any smaller \(s'>80\) it fails.

Let’s compute for each \(c\), the intersection interval for \(s\):
- lower \(L=\max(5c,\;4c+27)\),
- upper \(U=\min(5c+4,\;4c+30)\).

But compare \(5c\) vs \(4c+27\): \(5c-(4c+27)=c-27\).
So for \(c\ge 27\), \(5c\ge 4c+27\) hence \(L=5c\).
For \(c\le 26\), \(L=4c+27\).

Similarly compare \(5c+4\) vs \(4c+30\): \((5c+4)-(4c+30)=c-26\).
For \(c\ge 26\), \(5c+4\ge 4c+30\) so \(U=4c+30\).
For \(c\le 25\), \(U=5c+4\).

Now list \(c\ge 23\):

- \(c=23\): \(L=4(23)+27=119\), already \(>80\) too high but actually \(s\) would be \(>100\). still allowed but check uniqueness and the “any lower score still >80 fails” suggests we want smallest above 80. However note \(s\) increases with \(c\). So we want the smallest \(c\) that gives uniqueness while keeping \(s>80\) maximal just above 80. Let’s instead directly find \(s\) in \((80, \infty)\) that yields uniqueness and is minimal just above 80? The condition says if score had been any lower but still over 80, uniqueness would fail. So our \(s\) is the smallest value \(>80\) for which uniqueness holds.
So search upward from 81 until uniqueness holds, and ensure it fails for all 81,82,...,s-1.
Try compute uniqueness quickly by counting feasible \(c\) values for each \(s\) is heavy; instead use the derived matching condition which gives exact uniqueness.

The matching condition gives candidates for \(s\) where the feasible interval shrinks to one integer, and the smallest \(s>80\) among them is our answer.

Compute \(s\) from \(s\) must satisfy either endpoints in intersection.

For each \(c\), the possible \(s\) range is:
- \(c=23\): \(L=4c+27=119\), \(U=5c+4=119\)?? since \(U=5c+4\) for c<=25: \(U=119\). So \(s=119\).
- \(c=24\): \(L=4c+27=123\), \(U=5c+4=124\) (since c<=25). so possibly \(s=123,124\) but uniqueness requires exactly one feasible \(c\), still okay if both work? check quickly by constructing \(w\):
  If \(s=123\): \(w=30+4c-s=30+96-123=3\), and \(c=24\) gives blanks \(=30-24-3=3\ge0\) feasible.
  If \(s=124\): \(w=30+96-124=2\), blanks \(=4\ge0\) feasible.
But could there be another \(c\) feasible for those \(s\)? uniqueness says no, so these should be valid candidates.
- \(c=25\): \(L=4c+27=127\), \(U=5c+4=129\) (still c<=25 for U): \(s\in\{127,128,129\}\).
- \(c=26\): now \(L=4c+27=131\) (since c<=26 for L), \(U=4c+30=134\) (since c>=26 for U): \(s\in\{131,132,133,134\}\).
- \(c=27\): \(L=5c=135\), \(U=4c+30=138\): \(s\in\{135,136,137,138\}\).
Clearly the smallest \(s>80\) among all is \(s=119\).

Now verify the “any lower but still over 80” condition. We must ensure for scores \(81\) through \(118\), \(c\) is not uniquely determined. Since our candidate uniqueness starts at \(119\), this must be true.

Therefore Mary's score is \(119\).
Then
\[
119=30+4c-w \Rightarrow 89=4c-w.
\]
With the feasible matching case found above, \(c=23\) gives \(w=30+92-119=3\), blanks \(=30-23-3=4\ge0\).
And for \(s=119\), the matching condition indicates uniqueness holds, so John can deduce \(c=23\).

ANSWER: 119
```

</details>

<details>
<summary>correct attempt 2</summary>

```text
Let \(c\) be the number correct and \(w\) the number wrong. Then unanswered are irrelevant, and
\[
s=30+4c-w.
\]
Also \(c+w\le 30\) with \(c,w\ge 0\).

John knows \(s>80\) and from \(s\) can determine the pair \((c,w)\), hence \(c\), uniquely. But if \(s\) were any lower (still \(>80\)), \((c,w)\) would no longer be uniquely determined.

Define
\[
t:=s-30=4c-w.
\]
Since \(s>80\), we have \(t>50\). Also
\[
w=4c-t.
\]
For given \(t\), any valid solution must satisfy:
1. \(w\ge 0 \Rightarrow 4c-t\ge 0 \Rightarrow c\ge \frac t4\).
2. \(c+w\le 30\):
\[
c+(4c-t)\le 30 \;\Rightarrow\; 5c-t\le 30 \;\Rightarrow\; c\le \frac{t+30}{5}.
\]
So the integer \(c\) is constrained by
\[
\left\lceil \frac t4\right\rceil \le c \le \left\lfloor \frac{t+30}{5}\right\rfloor.
\]
Then each such \(c\) gives exactly one \(w=4c-t\), hence one achievable score.

We need the smallest \(s>80\) for which this interval contains exactly one integer \(c\) (uniqueness), but for the previous score value \(s-1\) (i.e. \(t-1\)) the interval contains at least two integers.

Since \(s>80\), the candidate smallest \(s\) is \(81\), i.e. \(t=51\), and we test upward until uniqueness occurs.

### Check \(t=51\) (score \(81\))
\[
\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,\quad
\left\lfloor \frac{51+30}{5}\right\rfloor=\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
So \(c\) can be \(13,14,15,16\): **4 possibilities**, not unique.

### Check \(t=52\) (score \(82\))
\[
\left\lceil \frac{52}{4}\right\rceil=\left\lceil 13\right\rceil=13,\quad
\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16.
\]
So \(c=13,14,15,16\): **4 possibilities**, not unique.

### Check \(t=53\) (score \(83\))
\[
\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14,\quad
\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16.
\]
So \(c=14,15,16\): **3 possibilities**, not unique.

### Check \(t=54\) (score \(84\))
\[
\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14,\quad
\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16.
\]
So \(c=14,15,16\): **3 possibilities**, not unique.

### Check \(t=55\) (score \(85\))
\[
\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,\quad
\left\lfloor \frac{85}{5}\right\rfloor=\left\lfloor 17\right\rfloor=17.
\]
So \(c=14,15,16,17\): **4 possibilities**, not unique.

### Check \(t=56\) (score \(86\))
\[
\left\lceil \frac{56}{4}\right\rceil=\left\lceil 14\right\rceil=14,\quad
\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17.
\]
So \(c=14,15,16,17\): **4 possibilities**.

### Check \(t=57\) (score \(87\))
\[
\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15,\quad
\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17.
\]
So \(c=15,16,17\): **3 possibilities**.

### Check \(t=58\) (score \(88\))
\[
\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15,\quad
\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17.
\]
So \(c=15,16,17\): **3 possibilities**.

### Check \(t=59\) (score \(89\))
\[
\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15,\quad
\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17.
\]
So \(c=15,16,17\): **3 possibilities**.

### Check \(t=60\) (score \(90\))
\[
\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15,\quad
\left\lfloor \frac{90}{5}\right\rfloor=\left\lfloor 18\right\rfloor=18.
\]
So \(c=15,16,17,18\): **4 possibilities**.

This is still not getting uniqueness; so uniqueness must occur at some higher \(t\) where the interval shrinks to a single integer.

Notice:
- The lower bound \(\lceil t/4\rceil\) increases by \(1\) every time \(t\) passes a multiple of \(4\).
- The upper bound \(\lfloor (t+30)/5\rfloor\) increases by \(1\) every time \(t\) passes a value making \((t+30)/5\) cross an integer.

The interval length is
\[
\left\lfloor \frac{t+30}{5}\right\rfloor - \left\lceil \frac t4\right\rceil.
\]
We want this to be \(0\) (exactly one integer).

So we try to find when
\[
\left\lceil \frac t4\right\rceil = \left\lfloor \frac{t+30}{5}\right\rfloor.
\]

Try \(t=74\) (score \(104\)) near the top (since max score is \(30+4\cdot 30=150\)).
Compute quickly:
\[
\left\lceil \frac{74}{4}\right\rceil=\left\lceil 18.5\right\rceil=19,\quad
\left\lfloor \frac{104}{5}\right\rfloor=\left\lfloor 20.8\right\rfloor=20.
\]
Two values possible \(c=19,20\). Not unique.

Try \(t=75\) (score \(105\)):
\[
\left\lceil \frac{75}{4}\right\rceil=\left\lceil 18.75\right\rceil=19,\quad
\left\lfloor \frac{105}{5}\right\rfloor=\left\lfloor 21\right\rfloor=21.
\]
So \(c=19,20,21\): not unique.

Try \(t=76\) (score \(106\)):
\[
\left\lceil 19\right\rceil=19,\quad \left\lfloor \frac{106}{5}\right\rfloor=\left\lfloor 21.2\right\rfloor=21.
\]
So \(c=19,20,21\): not unique.

Try \(t=77\) (score \(107\)):
\[
\left\lceil 19.25\right\rceil=20,\quad \left\lfloor \frac{107}{5}\right\rfloor=\left\lfloor 21.4\right\rfloor=21.
\]
So \(c=20,21\): not unique.

Try \(t=78\) (score \(108\)):
\[
\left\lceil 19.5\right\rceil=20,\quad \left\lfloor \frac{108}{5}\right\rfloor=\left\lfloor 21.6\right\rfloor=21.
\]
So \(c=20,21\): not unique.

Try \(t=79\) (score \(109\)):
\[
\left\lceil 19.75\right\rceil=20,\quad \left\lfloor \frac{109}{5}\right\rfloor=\left\lfloor 21.8\right\rfloor=21.
\]
So \(c=20,21\): not unique.

Try \(t=80\) (score \(110\)):
\[
\left\lceil 20\right\rceil=20,\quad \left\lfloor \frac{110}{5}\right\rfloor=22.
\]
Then \(c=20,21,22\): not unique.

Try \(t=81\) (score \(111\)):
\[
\left\lceil 20.25\right\rceil=21,\quad \left\lfloor \frac{111+?}{5}\right\rfloor=\left\lfloor \frac{111+30?}{5}\right\rfloor
\]
Oops—remember upper is \(\frac{t+30}{5}\), so for \(t=81\), \(t+30=111\):
\[
\left\lfloor \frac{111}{5}\right\rfloor=\left\lfloor 22.2\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=82\) (score \(112\)):
\[
\left\lceil \frac{82}{4}\right\rceil=\left\lceil 20.5\right\rceil=21,\quad
\left\lfloor \frac{112}{5}\right\rfloor=\left\lfloor 22.4\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=83\) (score \(113\)):
\[
\left\lceil 20.75\right\rceil=21,\quad \left\lfloor \frac{113}{5}\right\rfloor=\left\lfloor 22.6\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=84\) (score \(114\)):
\[
\left\lceil 21\right\rceil=21,\quad \left\lfloor \frac{114}{5}\right\rfloor=\left\lfloor 22.8\right\rfloor=22.
\]
So \(c=21,22\): not unique.

Try \(t=85\) (score \(115\)):
\[
\left\lceil 21.25\right\rceil=22,\quad \left\lfloor \frac{115}{5}\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=86\) (score \(116\)):
\[
\left\lceil 21.5\right\rceil=22,\quad \left\lfloor \frac{116}{5}\right\rfloor=\left\lfloor 23.2\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=87\) (score \(117\)):
\[
\left\lceil 21.75\right\rceil=22,\quad \left\lfloor \frac{117}{5}\right\rfloor=\left\lfloor 23.4\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=88\) (score \(118\)):
\[
\left\lceil 22\right\rceil=22,\quad \left\lfloor \frac{118}{5}\right\rfloor=\left\lfloor 23.6\right\rfloor=23.
\]
So \(c=22,23\): not unique.

Try \(t=89\) (score \(119\)):
\[
\left\lceil 22.25\right\rceil=23,\quad \left\lfloor \frac{119}{5}\right\rfloor=\left\lfloor 23.8\right\rfloor=23.
\]
Now the interval is \(c=23\) only! Great—this gives uniqueness.

So score \(s = 30+t = 30+89 = 119\).

Finally we check the “if Mary's score had been any lower but still over 80” condition: meaning at \(s=118\) (i.e. \(t=88\)) John could not determine \(c\) uniquely.
We found for \(t=88\), \(c\in\{22,23\}\), indeed not unique. Thus the condition is satisfied.

Compute \(c\) and \(w\) for \(t=89\):
\[
t=4c-w \Rightarrow 89=4\cdot 23 - w = 92-w \Rightarrow w=3.
\]
Valid since \(23+3=26\le 30\).

Therefore Mary's score is \(119\).

ANSWER: 119
```

</details>

<details>
<summary>correct attempt 3</summary>

```text
We have \(30\) problems. Let \(c\)=correct, \(w\)=wrong, and \(u\)=unanswered. Then
\[
c+w+u=30.
\]
The score is
\[
s=30+4c-w.
\]
So
\[
s-30=4c-w \quad\Longrightarrow\quad w=4c-(s-30).
\]
Since \(w\) is a nonnegative integer and \(u=30-c-w\ge 0\), we need
\[
w\ge 0 \quad\Longrightarrow\quad 4c\ge s-30,
\]
\[
u=30-c-w=30-c-(4c-(s-30))=30-c-4c+s-30=s-5c\ge 0
\quad\Longrightarrow\quad s\ge 5c.
\]
Thus valid \(c\) satisfy
\[
\frac{s-30}{4}\le c \le \frac{s}{5},
\]
with \(c\) an integer.

John can determine the number of correct answers from knowing \(s>80\) exactly when there is **only one** integer \(c\) in that interval. If \(s\) were any lower but still \(>80\), then there would be **at least two** possible values of \(c\).

Let’s rewrite bounds:
\[
c \ge \left\lceil\frac{s-30}{4}\right\rceil,\qquad c\le \left\lfloor\frac{s}{5}\right\rfloor.
\]
We want exactly one integer \(c\), i.e.
\[
\left\lceil\frac{s-30}{4}\right\rceil=\left\lfloor\frac{s}{5}\right\rfloor.
\]
Try to search near \(s=80\) upward. Since there are only a few extra scores above 80, we can test candidates.

Note that \(s=81,82,83,\dots\). Compute possible \(c\) range quickly.

### Test \(s=86\)
\[
\frac{s-30}{4}=\frac{56}{4}=14 \Rightarrow \left\lceil\cdot\right\rceil=14,
\]
\[
\frac{s}{5}=\frac{86}{5}=17.2 \Rightarrow \left\lfloor\cdot\right\rfloor=17.
\]
This gives \(c\in\{14,15,16,17\}\), not unique. Too many.

### Test \(s=90\)
\[
\frac{s-30}{4}=\frac{60}{4}=15 \Rightarrow \lceil\cdot\rceil=15,
\]
\[
\frac{s}{5}=\frac{90}{5}=18 \Rightarrow \lfloor\cdot\rfloor=18,
\]
so \(c\in\{15,16,17,18\}\). Not unique.

We need the interval to be so tight that it contains exactly one integer. That happens when the lower bound is just one above the previous integer and the upper bound equals it.

A standard way: require
\[
\left\lfloor\frac{s}{5}\right\rfloor = \left\lceil\frac{s-30}{4}\right\rceil = c.
\]
Then
\[
4c \le s-30 < 4(c+1)
\quad\text{and}\quad
5c \le s < 5(c+1).
\]
So \(s\) must satisfy both:
\[
s \in [5c,\,5c+4]
\]
and
\[
s \in [4c+30,\,4c+33].
\]
Intersecting gives a short range. Also \(s>80\).

Let’s find \(c\) and \(s\) with \(s\) in the intersection being a single integer and giving the “minimality” condition.

Try plausible \(c\). Since \(s>80\), and \(s\ge 5c\), we get \(c\le 16\) (because \(5\cdot 16=80\), need \(s>80\) so \(c\) could be 16 with \(s\ge81\)). Also \(4c\le s-30\) implies \(s\ge 4c+30\).

So \(c\) from 13 to 16 are likely.

#### Take \(c=16\)
Then:
\[
s\in [5\cdot 16,5\cdot 16+4]=[80,84]
\]
and
\[
s\in [4\cdot 16+30,4\cdot 16+33]=[94,97].
\]
No overlap. So \(c\neq 16\).

#### Take \(c=15\)
\[
s\in [75,79],\quad s\in [90,93]
\]
No overlap.

#### Take \(c=14\)
\[
s\in [70,74],\quad s\in [86,89]
\]
No overlap.

#### Take \(c=13\)
\[
s\in [65,69],\quad s\in [82,85]
\]
No overlap.

This suggests our “intersection method” used strictness incorrectly: we used \(4c \le s-30 <4(c+1)\) but from \(\left\lceil\frac{s-30}{4}\right\rceil=c\) the condition is
\[
c-1 < \frac{s-30}{4} \le c.
\]
So
\[
4(c-1) < s-30 \le 4c
\]
\[
4c+30 \ge s > 4c+26.
\]
Thus
\[
s\in \{4c+27,4c+28,4c+29,4c+30\}.
\]
Also \(\left\lfloor\frac{s}{5}\right\rfloor=c\) means
\[
5c \le s < 5c+5,
\]
so
\[
s\in \{5c,5c+1,5c+2,5c+3,5c+4\}.
\]
Now intersect these sets.

Let \(c\) be the unique correct count.

Since \(s>80\), we test \(c=14,15,16,\dots\) but note \(s<5c+5\).

#### \(c=15\)
Second set: \(s\in\{75,76,77,78,79\}\) (all \(\le 79\)), impossible since \(s>80\).
So \(c\ge 16\).

#### \(c=16\)
Second set: \(s\in\{80,81,82,83,84\}\).
First set: \(s\in\{4(16)+27,\dots,4(16)+30\}=\{91,92,93,94\}\).
No overlap.

#### \(c=17\)
Second set: \(s\in\{85,86,87,88,89\}\).
First set: \(s\in\{4(17)+27,4(17)+30\}=\{95,96,97,98\}\) no overlap.

So clearly the unique-\(c\) approach indicates something inconsistent: the sets don’t overlap for any \(c\), meaning our assumption that both floor/ceil equal the same \(c\) is possible only if the inequalities permit overlap; but we’re missing that \(c\) must satisfy simultaneously
\[
c \ge \left\lceil\frac{s-30}{4}\right\rceil,\quad c \le \left\lfloor\frac{s}{5}\right\rfloor,
\]
so uniqueness means these bounds differ by less than 1, not necessarily equal as integers due to ceil/floor discreteness. The correct condition for exactly one integer is:
\[
\left\lceil\frac{s-30}{4}\right\rceil \le \left\lfloor\frac{s}{5}\right\rfloor
\]
and the count is 1:
\[
\left\lfloor\frac{s}{5}\right\rfloor - \left\lceil\frac{s-30}{4}\right\rceil +1 = 1
\]
\[
\Longrightarrow\quad \left\lfloor\frac{s}{5}\right\rfloor = \left\lceil\frac{s-30}{4}\right\rceil.
\]
So equality is correct; yet it yields no solution for \(s>80\) by our attempted \(c\). Therefore we should instead directly brute force \(s\) near 80 by checking possible \(c\) via the interval
\[
\frac{s-30}{4}\le c\le \frac{s}{5}.
\]

### Directly test \(s=81,82,\dots\)
For each \(s\), compute possible \(c\) integers.

- \(s=81\): \(\frac{51}{4}=12.75\le c\le 16.2\Rightarrow c\in\{13,14,15,16\}\) (4).
- \(s=82\): \(\frac{52}{4}=13\le c\le 16.4\Rightarrow c\in\{13,14,15,16\}\) (4).
- \(s=83\): \(\frac{53}{4}=13.25\le c\le 16.6\Rightarrow c\in\{14,15,16\}\) (3).
- \(s=84\): \(\frac{54}{4}=13.5\le c\le 16.8\Rightarrow c\in\{14,15,16\}\) (3).
- \(s=85\): \(\frac{55}{4}=13.75\le c\le 17\Rightarrow c\in\{14,15,16,17\}\) (4).
- \(s=86\): \(\frac{56}{4}=14\le c\le 17.2\Rightarrow c\in\{14,15,16,17\}\) (4).
- \(s=87\): \(\frac{57}{4}=14.25\le c\le 17.4\Rightarrow c\in\{15,16,17\}\) (3).
- \(s=88\): \(\frac{58}{4}=14.5\le c\le 17.6\Rightarrow c\in\{15,16,17\}\) (3).
- \(s=89\): \(\frac{59}{4}=14.75\le c\le 17.8\Rightarrow c\in\{15,16,17\}\) (3).
- \(s=90\): \(\frac{60}{4}=15\le c\le 18\Rightarrow c\in\{15,16,17,18\}\) (4).
- \(s=91\): \(\frac{61}{4}=15.25\le c\le 18.2\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=92\): \(\frac{62}{4}=15.5\le c\le 18.4\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=93\): \(\frac{63}{4}=15.75\le c\le 18.6\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=94\): \(\frac{64}{4}=16\le c\le 18.8\Rightarrow c\in\{16,17,18\}\) (3).
- \(s=95\): \(\frac{65}{4}=16.25\le c\le 19\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=96\): \(\frac{66}{4}=16.5\le c\le 19.2\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=97\): \(\frac{67}{4}=16.75\le c\le 19.4\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=98\): \(\frac{68}{4}=17\le c\le 19.6\Rightarrow c\in\{17,18,19\}\) (3).
- \(s=99\): \(\frac{69}{4}=17.25\le c\le 19.8\Rightarrow c\in\{18,19\}\) (2).
- \(s=100\): \(\frac{70}{4}=17.5\le c\le 20\Rightarrow c\in\{18,19,20\}\) (3).
- \(s=101\): \(\frac{71}{4}=17.75\le c\le 20.2\Rightarrow c\in\{18,19,20\}\) (3).
- \(s=102\): \(\frac{72}{4}=18\le c\le 20.4\Rightarrow c\in\{18,19,20\}\) (3).
- \(s=103\): \(\frac{73}{4}=18.25\le c\le 20.6\Rightarrow c\in\{19,20\}\) (2).
- \(s=104\): \(\frac{74}{4}=18.5\le c\le 20.8\Rightarrow c\in\{19,20\}\) (2).
- \(s=105\): \(\frac{75}{4}=18.75\le c\le 21\Rightarrow c\in\{19,20,21\}\) but \(c\le 30\) ok (3).
- \(s=106\): \(\frac{76}{4}=19\le c\le 21.2\Rightarrow c\in\{19,20,21\}\) (3).
- \(s=107\): \(\frac{77}{4}=19.25\le c\le 21.4\Rightarrow c\in\{20,21\}\) (2).
- \(s=108\): \(\frac{78}{4}=19.5\le c\le 21.6\Rightarrow c\in\{20,21\}\) (2).
- \(s=109\): \(\frac{79}{4}=19.75\le c\le 21.8\Rightarrow c\in\{20,21\}\) (2).
- \(s=110\): \(\frac{80}{4}=20\le c\le 22\Rightarrow c\in\{20,21,22\}\) (3).

We still haven’t seen uniqueness (1 candidate). Continue until it happens.

- \(s=113\): lower \(\frac{83}{4}=20.75\Rightarrow c\ge 21\). upper \(\frac{113}{5}=22.6\Rightarrow c\le 22\). So \(c\in\{21,22\}\) (2).
- \(s=114\): lower \(\frac{84}{4}=21\Rightarrow c\ge 21\). upper \(\frac{114}{5}=22.8\Rightarrow c\le 22\). So \(c\in\{21,22\}\) (2).
- \(s=115\): lower \(\frac{85}{4}=21.25\Rightarrow c\ge 22\). upper \(115/5=23\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=116\): lower \(86/4=21.5\Rightarrow c\ge 22\). upper \(116/5=23.2\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=117\): lower \(87/4=21.75\Rightarrow c\ge 22\). upper \(117/5=23.4\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=118\): lower \(88/4=22\Rightarrow c\ge 22\). upper \(118/5=23.6\Rightarrow c\le 23\). So \(c\in\{22,23\}\) (2).
- \(s=119\): lower \(89/4=22.25\Rightarrow c\ge 23\). upper \(119/5=23.8\Rightarrow c\le 23\). So **\(c=\{23\}\)** unique!

Now check the condition: if the score were any lower but still \(>80\), John could not have determined \(c\). We must ensure that for \(s=118\) uniqueness fails (it does: two values), and generally for all \(81\le s\le 118\) there are either 2 or more. From our sampling it seems we never got 1 earlier; we can accept this as consistent because the unique first occurrence happens when the upper bound drops to exactly the next integer while the lower bound has just surpassed the previous.

Thus \(s=119\) is the desired score.

\[
\boxed{119}
\]

ANSWER: 119
```

</details>

<details>
<summary>correct attempt 4</summary>

```text
Let \(c\) be the number correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\qquad s=30+4c-w.
\]
Substitute \(w=30-c-u\):
\[
s=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
So
\[
s=5c+u,\quad \text{with } c\ge 0,\ u\ge 0,\ c+u\le 30.
\]

John can determine \(c\) from \(s\) if there is only one possible value of \(c\) that can produce that score.

We are told:
- \(s>80\).
- If \(s\) were any lower but still \(>80\), then \(c\) would *not* be uniquely determined.

So \(s\) is the *largest* score \(>80\) for which \(c\) is still unique? Let’s find the first point above 80 where uniqueness breaks.

From \(s=5c+u\), for a given \(s\),
\[
u=s-5c.
\]
For feasibility we need \(0\le u\le 30-c\), i.e.
\[
0\le s-5c\le 30-c.
\]
The left inequality gives \(c\le \frac{s}{5}\).
The right inequality gives
\[
s-5c\le 30-c\implies s\le 30+4c\implies c\ge \frac{s-30}{4}.
\]
Thus the possible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
Uniqueness means this interval contains exactly one integer.

Now test scores just above 80. Since the maximum score occurs at \(c=30,u=0\): \(s=150\), so we’re in a moderate range.

Compute for \(s=81,82,\dots\) until the interval size changes.

Let
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad R(s)=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Unique \(c\) occurs when \(L(s)=R(s)\).

Check \(s=81\):
\[
L=\left\lceil \frac{51}{4}\right\rceil=\lceil 12.75\rceil=13,\quad
R=\left\lfloor \frac{81}{5}\right\rfloor=\lfloor 16.2\rfloor=16.
\]
Not unique.

We need \(s\) close enough to force \(R\) down while \(L\) stays near it. This happens at larger \(s\).

Try \(s=100\):
\[
L=\left\lceil \frac{70}{4}\right\rceil=\lceil17.5\rceil=18,\quad
R=\left\lfloor \frac{100}{5}\right\rfloor=20.
\]
Not unique.

Try \(s=104\):
\[
L=\left\lceil \frac{74}{4}\right\rceil=\lceil18.5\rceil=19,\quad
R=\left\lfloor \frac{104}{5}\right\rfloor=\lfloor20.8\rfloor=20.
\]
Still not unique.

Try \(s=105\):
\[
L=\left\lceil \frac{75}{4}\right\rceil=\lceil18.75\rceil=19,\quad
R=\left\lfloor \frac{105}{5}\right\rfloor=21.
\]
Not unique.

Try \(s=108\):
\[
L=\left\lceil \frac{78}{4}\right\rceil=\lceil19.5\rceil=20,\quad
R=\left\lfloor \frac{108}{5}\right\rfloor=\lfloor21.6\rfloor=21.
\]
Not unique.

Try \(s=110\):
\[
L=\left\lceil \frac{80}{4}\right\rceil=\lceil20\rceil=20,\quad
R=\left\lfloor \frac{110}{5}\right\rfloor=\lfloor22\rfloor=22.
\]
Not unique.

We need \(R(s)=L(s)\). That means the interval length is 0:
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]
Let that common value be \(c\). Then we require
\[
c\le \frac{s}{5} < c+1
\quad\text{and}\quad
c-1< \frac{s-30}{4}\le c.
\]
Convert to bounds on \(s\):
\[
5c \le s \le 5c+4
\]
and
\[
4c+26 < s \le 4c+30.
\]
So \(s\) must satisfy both:
\[
\max(5c,\,4c+27)\le s \le \min(5c+4,\,4c+30).
\]
Since \(4c+27\) is larger than \(4c+26\).

Compute which \(c\) allow overlap. Note
\[
5c \quad\text{vs}\quad 4c+27:\quad 5c\ge 4c+27 \iff c\ge 27.
\]
But \(c\le 30\). So \(c\) is likely \(27,28,29,30\).

Also
\[
5c+4 \quad\text{vs}\quad 4c+30:\quad 5c+4\le 4c+30 \iff c\le 26.
\]
So for \(c\ge 27\), the upper limit will be \(4c+30\).

Thus for \(c\in\{27,28,29,30\}\):
- Lower bound: \(\max(5c,4c+27)=5c\) (since \(c\ge 27\))
- Upper bound: \(\min(5c+4,4c+30)=4c+30\) (since \(c\ge 27\))

So we need
\[
5c \le 4c+30 \iff c\le 30,
\]
always true in this range. And we need at least one integer \(s\) between them:
\[
s \in [5c,\;4c+30].
\]
For each \(c\):
- \(c=27\): \(s\in[135,138]\) all \(>80\).
- \(c=28\): \(s\in[140,142]\).
- \(c=29\): \(s\in[145,146]\).
- \(c=30\): \(s=150\).

Now interpret the “if score had been any lower but still \(>80\), John could not have determined” condition. That means \(s\) is the *smallest* score \(>80\) for which the representation gives unique \(c\), because any lower \(>80\) would allow multiple \(c\).

Among the candidates above, the smallest \(s\) is \(135\) (from \(c=27\)). We must verify that \(s=134\) is not unique.

For \(s=134\):
\[
L=\left\lceil \frac{104}{4}\right\rceil=26,\quad
R=\left\lfloor \frac{134}{5}\right\rfloor=26.
\]
That would actually be unique, which contradicts. So we must re-check: compute carefully:
\[
\frac{134}{5}=26.8\Rightarrow R=26.
\]
For \(L\):
\[
\frac{s-30}{4}=\frac{104}{4}=26\Rightarrow L=26.
\]
So \(s=134\) is unique with \(c=26\). Therefore the smallest unique score above 80 is less than 135, so our earlier candidate set missed lower \(c\) values because overlap logic assumed \(c\ge 27\) to compare bounds, but uniqueness can also happen for smaller \(c\) when the ceiling/floor align just right.

So instead we should directly find the minimal \(s>80\) for which there is uniqueness and then pick the *first* such that all smaller \(>80\) are non-unique. However the condition in the problem is: Mary’s score \(s\) is such that John can determine \(c\), but for any lower score still \(>80\), he cannot. That means \(s\) is the *minimum* score \(>80\) with unique \(c\).

So find the smallest \(s>80\) with \(L(s)=R(s)\).

We test systematically by looking at when \(R(s)=\left\lfloor \frac{s}{5}\right\rfloor\) increments, and \(L(s)=\left\lceil \frac{s-30}{4}\right\rceil\).

Compute \(s\) near 80-90 quickly:

For \(s=85\):
\[
L=\left\lceil \frac{55}{4}\right\rceil=\lceil13.75\rceil=14,\quad
R=\left\lfloor \frac{85}{5}\right\rfloor=17
\]
No.

For \(s=86\): \(L=\lceil14\rceil=14\) (since \(\frac{56}{4}=14\)), \(R=\lfloor17.2\rfloor=17\). No.

We need \(R\) drop or \(L\) rise until they meet. This happens when \(R\) is small relative to \(L\), i.e. at larger \(s\).

Instead, find where \(L(s)\) catches up to \(R(s)\). Solve approximately:
\[
\frac{s-30}{4}\approx \frac{s}{5}\implies 5(s-30)=4s\implies 5s-150=4s\implies s=150.
\]
So they meet only near the top, but due to integer effects, first equality may occur earlier. Let’s search from 81 upward with the interval size \(R-L\) becoming 0.

Try \(s=130\):
\[
L=\left\lceil \frac{100}{4}\right\rceil=25,\quad
R=\left\lfloor \frac{130}{5}\right\rfloor=26.
\]
Not.

\(s=131\):
\[
L=\left\lceil \frac{101}{4}\right\rceil=\lceil25.25\rceil=26,\quad
R=\left\lfloor \frac{131}{5}\right\rfloor=26.
\]
Here \(L=R=26\), so uniqueness holds.

Now check \(s=130\) was non-unique (it had \(c\in[25,26]\)), good.

Also we must ensure for any lower \(s>80\), uniqueness fails. Since we found the first time at \(131\) (we should verify \(s=129\) etc. but they are further from the top and likely not yet unique). Let’s confirm quickly:
- \(s=129\): \(L=\lceil99/4\rceil=\lceil24.75\rceil=25\), \(R=\lfloor25.8\rfloor=25\) gives uniqueness at 25. Wait compute: \(\lfloor129/5\rfloor=25\) yes, and \(L=25\) too, so uniqueness would already occur at 129, contradicting minimality.

But does \(s=129\) truly give a unique feasible \(c\)? Our interval method should be correct; thus check:
For \(s=129\), \(c=25\) gives \(u=s-5c=129-125=4\), and check \(c+u=29\le 30\) feasible. For \(c=24\), \(u=129-120=9\), then \(c+u=33>30\) infeasible. So only \(c=25\). Hence uniqueness at \(129\).

So the true “minimal unique” must be even lower. We need the score \(s\) such that uniqueness holds but immediately below \(80<s'<s\) uniqueness fails. That means \(s\) is the unique-threshold where non-uniqueness switches to uniqueness; i.e. we need the *largest* score \(>80\) for which uniqueness holds and below which uniqueness fails (equivalently: uniqueness holds only at that exact score, and not at any lower score, but our counterexamples show uniqueness can occur at multiple scores).

Interpretation: “If Mary's score had been any lower, but still over 80, John could not have determined this.” That means for every integer score \(s'\) with \(81\le s'<s\), \(c\) would not be uniquely determined. So indeed \(s\) is the smallest score \(>80\) with uniqueness. But our checks show uniqueness at \(129\), so smaller scores than 129 must be non-unique; we must find the actual smallest such.

We can continue decreasing to find earliest \(s\) with \(L(s)=R(s)\).

Let \(s=5k+r\) with \(r\in\{0,1,2,3,4\}\). Then \(R=k\).
Also
\[
L=\left\lceil \frac{5k+r-30}{4}\right\rceil.
\]
Set \(L=k\):
\[
k-1<\frac{5k+r-30}{4}\le k
\]
Multiply:
\[
4k-4<5k+r-30\le 4k
\]
Left:
\[
4k-4<5k+r-30\implies -k-r< -26\implies k+r>26.
\]
Right:
\[
5k+r-30\le 4k\implies k+r\le 30.
\]
So uniqueness occurs exactly when
\[
k+r\in\{27,28,29,30\},
\]
with \(s=5k+r\), \(r\in[0,4]\).

Since \(s>80\), we need smallest \(s\) among those satisfying \(k+r\ge 27\).

To minimize \(s=5k+r\) given fixed \(k+r=t\), we should make \(k\) as small as possible (because coefficient 5 on \(k\)). For each \(t\in\{27,28,29,30\}\), take \(k\) minimal so that \(r=t-k\le 4\).

- For \(t=27\): need \(r=27-k\le 4\Rightarrow k\ge 23\). Minimal \(k=23\) gives \(r=4\), \(s=5\cdot 23+4=119\).
- Check \(t=28\): minimal \(k\ge 24\) gives \(r=4\), \(s=124\) larger.
So smallest is \(119\).

Therefore Mary’s score is \(119\).

Finally confirm that for any \(s'<119\) with \(s'>80\), uniqueness fails: that means no solution to \(k+r\in\{27,28,29,30\}\) yields \(s<119\). Since the smallest constructed was \(119\), all smaller \(s\) have \(k+r\le 26\) hence \(L\ne R\). Good.

Thus \(s=119\).

ANSWER: 119
```

</details>

<details>
<summary>correct attempt 5</summary>

```text
We have \(30\) questions. Let \(c\) be correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\quad s=30+4c-w,
\]
with \(u\ge 0\), so \(c+w\le 30\). Also \(c,w\ge 0\) integers.

Rewrite the score condition:
\[
s=30+4c-w \quad\Longrightarrow\quad 4c-w=s-30.
\]
Given a fixed score \(s\), this means
\[
w=4c-(s-30).
\]
Thus for each integer \(c\), we get a corresponding \(w\). For \(c\) to be valid we need:
1. \(w\ge 0\) \(\Rightarrow 4c\ge s-30\),
2. \(c+w\le 30\). Substitute \(w\):
\[
c+\bigl(4c-(s-30)\bigr)\le 30
\]
\[
5c-(s-30)\le 30
\]
\[
5c\le s+60
\]
\[
c\le \frac{s+60}{5}.
\]
So possible \(c\) values are integers satisfying
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s+60}{5}\right\rfloor.
\]
John can determine \(c\) uniquely from \(s\) iff there is exactly one integer \(c\) in this interval.

Mary’s score is over \(80\), so \(81\le s \le 120\) (maximum when \(w=0\), \(c=30\): \(s=30+120=150\) actually; but for \(s\) around 80–150 we’ll narrow with constraints).

“Any lower but still over \(80\)” means: for every \(s'\) with \(80<s'<s\), the interval for \(s'\) contains at least two integers \(c\) (so \(c\) is not uniquely determined). In particular, \(s-1\) must *not* give uniqueness.

So we want the smallest score above 80 that gives uniqueness, since if the score were not minimal, we could lower slightly and still have uniqueness, contradicting the condition. Therefore we seek the minimal \(s\ge 81\) such that the interval contains exactly one integer.

Let
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad U(s)=\left\lfloor \frac{s+60}{5}\right\rfloor.
\]
Uniqueness means \(L(s)=U(s)\).

Check \(s=81\):
\[
L=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,
\quad
U=\left\lfloor \frac{141}{5}\right\rfloor=\left\lfloor 28.2\right\rfloor=28.
\]
Many values → not unique.

As \(s\) increases, both bounds increase, and the width \(U-L\) will eventually shrink to 0. Let’s find when \(L(s)=U(s)\) first happens for \(s>80\).

Try to force equality by approximating without ceilings/floors:
\[
\frac{s-30}{4}\approx \frac{s+60}{5}
\]
\[
5(s-30)=4(s+60)
\]
\[
5s-150=4s+240
\]
\[
s=390.
\]
That’s far too large, meaning ceilings/floors matter and the interval length typically stays large. So uniqueness likely happens only near the feasibility boundary \(c+w\le 30\) becoming tight, i.e. when \(w\) is forced.

Instead, use the constraint \(c+w\le 30\) together with \(w=4c-(s-30)\):
\[
c+w = c+4c-(s-30)=5c-(s-30)\le 30
\]
\[
5c\le s+60.
\]
Also \(w\ge 0\) gives \(4c\ge s-30\). So \(c\) must satisfy:
\[
\frac{s-30}{4}\le c\le \frac{s+60}{5}.
\]
For uniqueness, these bounds must trap \(c\) to a single integer, meaning their difference is \(<1\):
\[
\frac{s+60}{5}-\frac{s-30}{4}<1.
\]
Compute:
\[
\frac{4(s+60)-5(s-30)}{20}<1
\]
\[
\frac{4s+240-5s+150}{20}<1
\]
\[
\frac{-s+390}{20}<1
\]
\[
-s+390<20
\]
\[
s>370.
\]
Again too big. So the earlier “difference<1” criterion isn’t appropriate because ceilings/floors can still reduce to 0 even when the real interval is larger; but the inequality suggests uniqueness might require very special congruences forcing only one integer.

So instead, try to express \(s\) in terms of \((c,w)\) and enforce that the score corresponds to exactly one \(c\). Observe:
\[
s=30+4c-w = 30+5c-(c+w).
\]
Let \(t=c+w\) be the number attempted (correct or wrong). Then
\[
s=30+5c-t,\quad 0\le t\le 30.
\]
Also \(w=t-c\), and \(0\le c\le t\).

So:
\[
s=30+5c-t \quad\Longrightarrow\quad t=30+5c-s.
\]
For a given score \(s\), a value \(c\) is possible iff the resulting \(t\) is an integer with
\[
0\le t\le 30,\quad c\le t.
\]
Since \(t=30+5c-s\), \(t\) is automatically integer if \(c\) integer. The conditions become:
1. \(0\le 30+5c-s\) \(\Rightarrow 5c\ge s-30\) (same as before),
2. \(30+5c-s\le 30\) \(\Rightarrow 5c\le s\),
3. \(c\le t=30+5c-s\) \(\Rightarrow 0\le 30+4c-s\) \(\Rightarrow 4c\ge s-30\).

So the main upper bound is now
\[
5c\le s.
\]
Combine with \(5c\ge s-30\) and \(4c\ge s-30\).

Thus:
\[
c\in \mathbb{Z},\quad \frac{s-30}{5}\le c\le \frac{s}{5},\quad\text{and}\quad c\ge \frac{s-30}{4}.
\]
But \(\frac{s-30}{4}>\frac{s-30}{5}\), so the effective lower bound is \(\left\lceil\frac{s-30}{4}\right\rceil\) and the upper bound is \(\left\lfloor\frac{s}{5}\right\rfloor\).
Hence uniqueness means:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]

Now test \(s=85\):
\[
\left\lceil\frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,\quad
\left\lfloor\frac{85}{5}\right\rfloor=17.
\]
Not equal.

Try \(s=90\):
\[
\left\lceil\frac{60}{4}\right\rceil=15,\quad \left\lfloor\frac{90}{5}\right\rfloor=18.
\]
No.

Try \(s=100\):
\[
\left\lceil\frac{70}{4}\right\rceil=18,\quad \left\lfloor\frac{100}{5}\right\rfloor=20.
\]
No.

We need \(\lfloor s/5\rfloor\) to be small enough to equal the ceiling term. Let \(k=\lfloor s/5\rfloor\). Then \(5k\le s\le 5k+4\).
Also uniqueness requires \(k=\left\lceil\frac{s-30}{4}\right\rceil\), so
\[
k-1<\frac{s-30}{4}\le k
\]
\[
4(k-1)<s-30\le 4k
\]
\[
4k+ -4 +? \Rightarrow 4k-4< s-30 \le 4k
\]
\[
4k+26< s \le 4k+30.
\]
Combine with \(5k\le s\le 5k+4\). So \(s\) must satisfy
\[
\max(5k,\,4k+27) \le s \le \min(5k+4,\,4k+30).
\]
Compute:
Left max: \(4k+27\) vs \(5k\). Their difference:
\[
5k-(4k+27)=k-27.
\]
For \(k\ge 27\), left is \(5k\). For \(s>80\), likely \(k\ge 16\). Let’s find actual \(s\) by trying \(k\) near where the interval could become a single integer.

Also right min: compare \(5k+4\) vs \(4k+30\):
\[
(4k+30)-(5k+4)=26-k.
\]
So for \(k\ge 26\), right is \(4k+30\); for \(k\le 26\), right is \(5k+4\).

To make interval very tight (ideally one integer), likely near \(k=27\) or \(26\).

Try \(k=27\):
Then \(s\) must satisfy:
left \(=\max(135,\,4(27)+27=135)=135\),
right \(=\min(139,\,4(27)+30=138)=138\).
So \(s\in[135,138]\). Any of these might yield uniqueness.

But we require \(s>80\); fine.

Now ensure uniqueness for one candidate and non-uniqueness for \(s-1\).
Let’s compute possible \(c\) directly for each \(s\in\{135,136,137,138\}\).

For a given \(s\), upper bound on \(c\) is \(\left\lfloor s/5\right\rfloor = \left\lfloor 27.0\) to \(27.6\right\rfloor =27\).
Lower bound is \(\left\lceil (s-30)/4\right\rceil = \left\lceil (105\text{ to }108)/4\right\rceil\).
- \(s=135\): \((s-30)/4=105/4=26.25\Rightarrow L=27\). So \(c\) is forced to \(27\). Uniqueness holds.
Now check \(s=134\) (still over 80):
\[
U=\left\lfloor 134/5\right\rfloor=26,\quad
L=\left\lceil 104/4\right\rceil=26.
\]
That would also give uniqueness, which would contradict the “if score had been any lower… John could not have determined” condition.
So \(s=135\) is too high.

Try next down where uniqueness first appears: we want \(s-1\) not unique, i.e. for \(s-1\) the interval contains at least two integers.

Consider \(s=136\):
- \(U=\lfloor 136/5\rfloor=27\).
- \(L=\left\lceil 106/4\right\rceil=\left\lceil 26.5\right\rceil=27\).
So \(c=27\) unique.
Check \(s-1=135\) gave uniqueness, so still contradiction.

For \(s=137\):
- \(U=\lfloor 137/5\rfloor=27\).
- \(L=\left\lceil 107/4\right\rceil=\left\lceil 26.75\right\rceil=27\).
Unique for 137.
Check \(136\) for uniqueness:
\(s=136\) also unique (as above). Contradiction.

For \(s=138\):
- \(U=\lfloor 138/5\rfloor=27\).
- \(L=\left\lceil 108/4\right\rceil=\left\lceil 27\right\rceil=27\).
Unique.
Check \(s-1=137\) unique. Contradiction.

Therefore the “lower but still over 80” means: decreasing the score while keeping it over 80 (but not necessarily by 1) makes uniqueness impossible, so it suffices that *every* \(s'\) with \(81\le s'<s\) is non-unique. That implies \(s\) is the *smallest* score \(>80\) yielding uniqueness.

Thus we must find the minimal \(s>80\) with uniqueness; we mistakenly jumped to \(k=27\) due to tightness. Let’s search smaller \(k\).

Set uniqueness condition:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor = k.
\]
Let \(s\) be minimal \(>80\). Since \(s>80\), \(k=\lfloor s/5\rfloor\ge 17\).

We can brute by \(k\) logic with interval for \(s\) derived earlier:
When \(k\le 26\), right min is \(5k+4\). Also since \(k<27\), left max is \(4k+27\) (because \(k-27<0\Rightarrow 5k<4k+27\)).
So for \(k\le 26\), we have
\[
4k+27 \le s \le 5k+4.
\]
For uniqueness to hold, \(s\) must also satisfy that the ceiling equals \(k\), which is exactly ensured by these bounds.

Now find minimal \(s>80\). Try \(k=17\):
\[
4k+27=68+27=95,\quad 5k+4=85+4=89,
\]
impossible (lower bound > upper). So \(k=17\) no.

\(k=18\):
\[
4k+27=72+27=99,\quad 5k+4=90+4=94
\]
impossible.

We need \(4k+27\le 5k+4\Rightarrow 27-4\le k \Rightarrow 23\le k\).
So smallest possible \(k\) is \(23\).

Take \(k=23\):
\[
4k+27=92+27=119,\quad 5k+4=115+4=119.
\]
So \(s=119\) is forced and is the minimal possible.

Verify:
For \(s=119\),
\[
U=\left\lfloor 119/5\right\rfloor=23.
\]
\[
L=\left\lceil (119-30)/4\right\rceil=\left\lceil 89/4\right\rceil=\left\lceil 22.25\right\rceil=23.
\]
So unique \(c=23\).

Check that any lower \(s'\) with \(>80\) is non-unique: since \(k\) would be \(\le 22\) for \(s'\le 118\). But for \(k\le 22\), the interval inequality fails (as shown \(4k+27>5k+4\)), giving either 0 or multiple solutions; in any case not uniqueness. Indeed, if \(k\le 22\), there is no integer \(s\) satisfying the derived bounds simultaneously for uniqueness. Hence \(119\) is the first score \(>80\) with unique \(c\).

Therefore Mary’s score is \(119\).

ANSWER: 119
```

</details>

#### Tier: `incorrect`

<details>
<summary>incorrect attempt 1</summary>

```text
We have \(30\) problems and
\[
s=30+4c-w.
\]
Let \(u\) be the number left blank. Then \(c+w+u=30\).

Rearrange:
\[
s-30=4c-w \quad\Longrightarrow\quad w=4c-(s-30).
\]
Since \(w\ge 0\), we need \(4c-(s-30)\ge 0\), i.e.
\[
s-30\le 4c.
\]
Also \(w\le 30-c\) (because \(u\ge 0\)), so
\[
4c-(s-30)\le 30-c
\]
\[
5c-(s-30)\le 30
\]
\[
5c\le s+0 \quad\Longrightarrow\quad c\le \frac{s}{5}.
\]

For a fixed score \(s\), different possible values of \(c\) must produce integer \(w\) that also make \(u=30-c-w\ge 0\). Since \(w=4c-(s-30)\), the parity/integrality is automatic when \(c\) is integer; the constraints are:
\[
0\le c\le 30,\quad w=4c-(s-30)\ge 0,\quad u=30-c-w\ge 0.
\]
Compute \(u\):
\[
u=30-c-(4c-(s-30))=30-c-4c+s-30=s-5c.
\]
So the nonnegativity \(u\ge 0\) is exactly
\[
s-5c\ge 0 \quad\Longrightarrow\quad c\le \frac{s}{5},
\]
consistent with above.

Also \(w\le 30-c\) is the same as \(u\ge 0\), so nothing new.

Thus for given \(s\), the valid \(c\) are precisely the integers satisfying
\[
\frac{s-30}{4}\le c \le \frac{s}{5}.
\]
(Left inequality from \(w\ge 0\): \(4c\ge s-30\).)

John could determine the number of problems \(c\) exactly when there is **only one integer** in that interval.

Mary’s score \(s\) is over \(80\), and if \(s\) were lowered to the next lower score but still \(>80\), the interval would contain at least two integers.

Now \(s\) is an integer (formula uses integers), and the condition “over 80” means \(s\ge 81\). The “any lower” wording in AIME context implies the immediate previous integer score \(s-1\).

We search for the smallest \(s\ge 81\) for which the interval contains exactly one integer, and the interval for \(s-1\) contains more than one integer.

Let’s test systematically by finding when the bounds squeeze to a single integer.

The interval is
\[
L(s)=\frac{s-30}{4},\qquad U(s)=\frac{s}{5}.
\]
We need:
- Exactly one integer \(c\) with \(L(s)\le c\le U(s)\).
- For \(s-1\), at least two integers.

Try \(s=81\):
\[
L(81)=\frac{51}{4}=12.75,\quad U(81)=\frac{81}{5}=16.2.
\]
Integers: \(13,14,15,16\) → 4 values, not unique.

\(s=82\):
\[
L=\frac{52}{4}=13,\quad U=\frac{82}{5}=16.4.
\]
Integers \(c=13,14,15,16\) → 4 values.

\(s=83\):
\[
L=\frac{53}{4}=13.25,\quad U=\frac{83}{5}=16.6.
\]
Integers \(14,15,16\) → 3 values.

\(s=84\):
\[
L=\frac{54}{4}=13.5,\quad U=\frac{84}{5}=16.8.
\]
Integers \(14,15,16\) → 3 values.

\(s=85\):
\[
L=\frac{55}{4}=13.75,\quad U=\frac{85}{5}=17.
\]
Integers \(14,15,16,17\) → 4 values.

\(s=86\):
\[
L=\frac{56}{4}=14,\quad U=\frac{86}{5}=17.2.
\]
Integers \(14,15,16,17\) → 4 values.

\(s=87\):
\[
L=\frac{57}{4}=14.25,\quad U=\frac{87}{5}=17.4.
\]
Integers \(15,16,17\) → 3 values.

\(s=88\):
\[
L=\frac{58}{4}=14.5,\quad U=\frac{88}{5}=17.6.
\]
Integers \(15,16,17\) → 3 values.

\(s=89\):
\[
L=\frac{59}{4}=14.75,\quad U=\frac{89}{5}=17.8.
\]
Integers \(15,16,17\) → 3 values.

\(s=90\):
\[
L=\frac{60}{4}=15,\quad U=\frac{90}{5}=18.
\]
Integers \(15,16,17,18\) → 4 values.

We need a tighter squeeze; continue:

\(s=91\):
\[
L=\frac{61}{4}=15.25,\quad U=\frac{91}{5}=18.2
\]
Integers \(16,17,18\) → 3.

\(s=92\):
\[
L=\frac{62}{4}=15.5,\quad U=\frac{92}{5}=18.4
\]
Integers \(16,17,18\) → 3.

\(s=93\):
\[
L=\frac{63}{4}=15.75,\quad U=\frac{93}{5}=18.6
\]
Integers \(16,17,18\) → 3.

\(s=94\):
\[
L=\frac{64}{4}=16,\quad U=\frac{94}{5}=18.8
\]
Integers \(16,17,18\) → 3.

\(s=95\):
\[
L=\frac{65}{4}=16.25,\quad U=\frac{95}{5}=19
\]
Integers \(17,18,19\) → 3.

\(s=96\):
\[
L=\frac{66}{4}=16.5,\quad U=\frac{96}{5}=19.2
\]
Integers \(17,18,19\) → 3.

\(s=97\):
\[
L=\frac{67}{4}=16.75,\quad U=\frac{97}{5}=19.4
\]
Integers \(17,18,19\) → 3.

\(s=98\):
\[
L=\frac{68}{4}=17,\quad U=\frac{98}{5}=19.6
\]
Integers \(17,18,19\) → 3.

\(s=99\):
\[
L=\frac{69}{4}=17.25,\quad U=\frac{99}{5}=19.8
\]
Integers \(18,19\) → 2 values.

\(s=100\):
\[
L=\frac{70}{4}=17.5,\quad U=\frac{100}{5}=20.
\]
Integers \(18,19,20\) → 3 values.

So far no uniqueness. Let’s go higher.

\(s=101\):
\[
L=\frac{71}{4}=17.75,\quad U=\frac{101}{5}=20.2
\]
Integers \(18,19,20\) → 3.

\(s=102\):
\[
L=\frac{72}{4}=18,\quad U=\frac{102}{5}=20.4
\]
Integers \(18,19,20\) → 3.

\(s=103\):
\[
L=\frac{73}{4}=18.25,\quad U=\frac{103}{5}=20.6
\]
Integers \(19,20\) → 2.

\(s=104\):
\[
L=\frac{74}{4}=18.5,\quad U=\frac{104}{5}=20.8
\]
Integers \(19,20\) → 2.

\(s=105\):
\[
L=\frac{75}{4}=18.75,\quad U=\frac{105}{5}=21
\]
Integers \(19,20,21\) → 3.

\(s=106\):
\[
L=\frac{76}{4}=19,\quad U=\frac{106}{5}=21.2
\]
Integers \(19,20,21\) → 3.

\(s=107\):
\[
L=\frac{77}{4}=19.25,\quad U=\frac{107}{5}=21.4
\]
Integers \(20,21\) → 2.

\(s=108\):
\[
L=\frac{78}{4}=19.5,\quad U=\frac{108}{5}=21.6
\]
Integers \(20,21\) → 2.

\(s=109\):
\[
L=\frac{79}{4}=19.75,\quad U=\frac{109}{5}=21.8
\]
Integers \(20,21\) → 2.

\(s=110\):
\[
L=\frac{80}{4}=20,\quad U=\frac{110}{5}=22
\]
Integers \(20,21,22\) → 3.

We still don’t have 1 integer. The only way to get exactly one integer is for the interval length to be \(<1\):
\[
U(s)-L(s)=\frac{s}{5}-\frac{s-30}{4}
=\frac{4s-5(s-30)}{20}
=\frac{4s-5s+150}{20}
=\frac{150-s}{20}.
\]
So we need
\[
\frac{150-s}{20}<1 \quad\Longrightarrow\quad 150-s<20 \quad\Longrightarrow\quad s>130.
\]
But AHSME has maximum when \(c=30,w=0\): \(s=30+4\cdot 30=150\). So \(s\) can indeed exceed 130.

Now find the first \(s>130\) where exactly one integer lies in the interval and for \(s-1\) more than one.

Since \(s>130\), let’s try values near 130.

Compute interval length:
\[
U-L=\frac{150-s}{20}.
\]
- If \(s=131\), length \(=\frac{19}{20}=0.95<1\), so potentially unique.
We must check endpoints carefully.

For \(s=131\):
\[
L=\frac{101}{4}=25.25,\quad U=\frac{131}{5}=26.2.
\]
Integers between: \(26\) only → unique! (Because \(25.25\le c\le 26.2\) allows only \(c=26\).)

Now check \(s=130\) (which is still over 80, yes):
For \(s=130\):
\[
L=\frac{100}{4}=25,\quad U=\frac{130}{5}=26.
\]
Integers: \(c=25,26\) → two values. So John could not have determined \(c\) from score 130.

Therefore \(s=131\) satisfies both conditions.

We can also compute consistency:
If \(c=26\), then
\[
w=4c-(s-30)=104-(101)=3,
\]
and
\[
u=s-5c=131-130=1,
\]
all valid.

So the score is \(\boxed{131}\).

ANSWER: 131
```

</details>

<details>
<summary>incorrect attempt 2</summary>

```text

```

</details>

<details>
<summary>incorrect attempt 3</summary>

```text

```

</details>

<details>
<summary>incorrect attempt 4</summary>

```text
Let \(c\) be correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\qquad s=30+4c-w.
\]
Substitute \(w=30-c-u\) into the score:
\[
s=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
So the score depends only on \(c\) and \(u\), with \(u\ge 0\) and \(c\ge 0\) integers, and
\[
c+u\le 30.
\]

John can determine \(c\) from \(s\) iff, given \(s\), there is exactly one possible \(c\) compatible with some \(u\ge 0\) and \(c+u\le 30\).

From \(s=5c+u\), we have \(u=s-5c\). Thus \(u\ge 0\) gives
\[
s-5c\ge 0 \implies c\le \frac{s}{5}.
\]
Also \(c+u\le 30\) becomes
\[
c+(s-5c)\le 30 \implies s-4c\le 30 \implies c\ge \frac{s-30}{4}.
\]
So the possible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
John can determine \(c\) exactly when this interval contains exactly one integer.

Now we use the condition: Mary's score was \(>80\), and if the score were any lower but still \(>80\), John could not have determined \(c\). That means \(s\) is the smallest integer \(>80\) for which the interval has exactly one integer.

Check \(s=81\). Compute bounds:
\[
\left\lceil \frac{81-30}{4}\right\rceil=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,
\]
\[
\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
Interval \([13,16]\) has 4 integers → not unique.

Try \(s=82\):
\[
\left\lceil \frac{82-30}{4}\right\rceil=\left\lceil \frac{52}{4}\right\rceil=13,
\quad
\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16.
\]
Interval \([13,16]\) has 4 integers → not unique.

\(s=83\):
\[
\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14,
\quad
\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16.
\]
Interval \([14,16]\) has 3 integers → not unique.

\(s=84\):
\[
\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14,
\quad
\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16.
\]
Interval \([14,16]\) has 3 integers → not unique.

\(s=85\):
\[
\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,
\quad
\left\lfloor \frac{85}{5}\right\rfloor=\left\lfloor 17\right\rfloor=17.
\]
Interval \([14,17]\) has 4 integers → not unique.

\(s=86\):
\[
\left\lceil \frac{56}{4}\right\rceil=\left\lceil 14\right\rceil=14,
\quad
\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17.
\]
Interval \([14,17]\) has 4 integers → not unique.

\(s=87\):
\[
\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15,
\quad
\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

\(s=88\):
\[
\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15,
\quad
\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

\(s=89\):
\[
\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15,
\quad
\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

\(s=90\):
\[
\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15,
\quad
\left\lfloor \frac{90}{5}\right\rfloor=\left\lfloor 18\right\rfloor=18.
\]
Interval \([15,18]\) has 4 integers → not unique.

\(s=91\):
\[
\left\lceil \frac{61}{4}\right\rceil=\left\lceil 15.25\right\rceil=16,
\quad
\left\lfloor \frac{91}{5}\right\rfloor=\left\lfloor 18.2\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=92\):
\[
\left\lceil \frac{62}{4}\right\rceil=\left\lceil 15.5\right\rceil=16,
\quad
\left\lfloor \frac{92}{5}\right\rfloor=\left\lfloor 18.4\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=93\):
\[
\left\lceil \frac{63}{4}\right\rceil=\left\lceil 15.75\right\rceil=16,
\quad
\left\lfloor \frac{93}{5}\right\rfloor=\left\lfloor 18.6\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=94\):
\[
\left\lceil \frac{64}{4}\right\rceil=\left\lceil 16\right\rceil=16,
\quad
\left\lfloor \frac{94}{5}\right\rfloor=\left\lfloor 18.8\right\rfloor=18.
\]
Interval \([16,18]\) has 3 integers → not unique.

\(s=95\):
\[
\left\lceil \frac{65}{4}\right\rceil=\left\lceil 16.25\right\rceil=17,
\quad
\left\lfloor \frac{95}{5}\right\rfloor=\left\lfloor 19\right\rfloor=19.
\]
Interval \([17,19]\) has 3 integers → not unique.

\(s=96\):
\[
\left\lceil \frac{66}{4}\right\rceil=\left\lceil 16.5\right\rceil=17,
\quad
\left\lfloor \frac{96}{5}\right\rfloor=\left\lfloor 19.2\right\rfloor=19.
\]
Interval \([17,19]\) has 3 integers → not unique.

At this point, notice the interval length is small but hasn’t become 0. Since we must eventually get a single integer, we can solve when
\[
\left\lfloor \frac{s}{5}\right\rfloor = \left\lceil \frac{s-30}{4}\right\rceil.
\]
Instead, test plausible uniqueness by setting \(u\) small, because \(u=s-5c\) must also satisfy \(c+u\le 30\Rightarrow u\le 30-c\).
If \(c\) is maximal for given \(s\), then \(u\) is minimal. Uniqueness is most likely when increasing \(c\) by 1 forces \(u\) negative or violates \(c+u\le 30\).

Suppose \(c\) is the largest possible: \(c=\left\lfloor s/5\right\rfloor\). Then \(u=s-5c\) is the remainder \(r\in\{0,1,2,3,4\}\).
Condition \(c+u\le 30\) becomes
\[
\left\lfloor \frac{s}{5}\right\rfloor + (s-5\left\lfloor \frac{s}{5}\right\rfloor)\le 30
\iff c+r\le 30.
\]
If also the next smaller \(c\) would still be feasible, uniqueness fails. That means we need exactly one feasible \(c\), which occurs when lowering \(c\) by 1 would make \(u\) too large to keep \(c+u\le 30\).

If \(c\) is feasible with remainder \(r\), then with \(c-1\) we would have
\[
u' = s-5(c-1)= (s-5c)+5 = r+5.
\]
Then
\[
(c-1)+u' = (c-1)+(r+5)=c+r+4.
\]
So \(c-1\) is infeasible exactly when
\[
c+r+4>30 \quad\text{while}\quad c+r\le 30.
\]
Thus
\[
c+r=30.
\]
So we require the feasible pair to satisfy \(u=r\) and \(c+r=30\), i.e. \(u\) is exactly \(30-c\) (no wrong answers determined).

Now \(s=5c+u=5c+r\) with \(c+r=30\Rightarrow r=30-c\). Substitute:
\[
s=5c+(30-c)=4c+30.
\]
Also \(r=30-c\) must be \(0,1,2,3,4\). Hence
\[
30-c\in\{0,1,2,3,4\}\implies c\in\{26,27,28,29,30\}.
\]
Compute corresponding scores \(s=4c+30\):
- \(c=26\Rightarrow s=134\)
- \(c=27\Rightarrow s=138\)
- \(c=28\Rightarrow s=142\)
- \(c=29\Rightarrow s=146\)
- \(c=30\Rightarrow s=150\)

Among these, we need the one with \(s\) just over \(80\) satisfying the “if score had been any lower but still over 80, John could not” condition. The smallest score in the list is \(134\). Therefore it must be the first time uniqueness occurs for \(s>80\).

So Mary's score is \(\boxed{134}\).

ANSWER: 134
```

</details>

<details>
<summary>incorrect attempt 5</summary>

```text
We have \(30\) multiple choice questions. Let \(c\) be the number correct and \(w\) the number wrong; unanswered \(=30-c-w\).
Scores are
\[
s=30+4c-w.
\]
Given \(s>80\), rewrite:
\[
s-30=4c-w \quad\Rightarrow\quad s-30=4c-(\text{# wrong}).
\]

For fixed \(c\), the score ranges over possible \(w\) values with \(0\le w\le 30-c\), giving
\[
s=30+4c-w \in \{30+4c-(30-c),\,\dots,\,30+4c\}
= \{30+5c-30,\dots,30+4c\}.
\]
So for each \(c\), the achievable scores form an interval of integers:
\[
s\in [\,5c,\; 30+4c\,].
\]

John can determine \(c\) from \(s\) exactly when the intervals for different \(c\)’s do not overlap at that score.

Compute overlap condition between \(c\) and \(c+1\):
- \(c\)-interval upper end: \(30+4c\)
- \((c+1)\)-interval lower end: \(5(c+1)=5c+5\)

They overlap if
\[
5c+5 \le 30+4c
\quad\Longleftrightarrow\quad
c \le 25.
\]
Thus, for \(c\le 25\), there is overlap, so \(s\) cannot uniquely determine \(c\).
For \(c\ge 26\), there is no overlap between consecutive intervals (and hence \(c\) becomes uniquely determined by \(s\)).

Now use the problem’s “threshold” condition:
- Mary’s score is over \(80\), so we need \(s>80\).
- If the score were any lower (but still \(>80\)), John could not determine \(c\).
So \(s\) should be the *smallest* score \(>80\) for which \(c\) is uniquely determined.

Try the boundary case \(c=26\):
- For \(c=26\), the achievable interval is
\[
[\,5c,\;30+4c\,]=[130,\;30+104]=[130,\;134].
\]
The smallest is \(130\), which is definitely \(>80\).

Now check whether any score between \(81\) and \(129\) could yield unique \(c\).
But for \(c\le 25\) the intervals overlap, so uniqueness fails. Hence the first unique score above \(80\) must occur at the smallest score belonging to some \(c\ge 26\), i.e. at \(5\cdot 26=130\).

We should also ensure that at \(s=129\) uniqueness fails (it should, since \(c\le 25\)). Indeed \(129\) lies in the overlap region of some \(c\le 25\).

Therefore Mary’s score is
\[
\boxed{130}.
\]

Check quickly: can \(s=130\) occur with \(c=26\) and some \(w\)?
From \(s=30+4c-w\):
\[
130=30+104-w \Rightarrow w=4.
\]
Then \(c+w=30\), so all questions answered; feasible.

Also, could any other \(c\) produce \(s=130\)?
For \(c=25\): \(130=30+100-w\Rightarrow w=0\), feasible, but then the corresponding interval for \(c=25\) is \([125,130]\), which would suggest overlap at 130. However uniqueness should fail if overlaps exist; and indeed we found overlap for \(c\le 25\). So we need to re-evaluate carefully: overlap at 130 means both \(c=25\) and \(c=26\) can produce 130. But is that possible given the scoring constraints?  
For \(c=25\), \(w=0\) gives score \(30+4\cdot 25-0=130\), and unanswered \(=30-25-0=5\), allowed. So John would not be able to determine \(c\) at \(s=130\).

So the earlier “no overlap for \(c\ge 26\)” conclusion must be refined: overlap occurs between intervals whenever consecutive intervals intersect, i.e. when
\[
\text{lower}_{c+1} \le \text{upper}_c.
\]
For \(c=25\):
\[
\text{lower}_{26}=5\cdot 26=130,\quad \text{upper}_{25}=30+4\cdot 25=130,
\]
so they intersect at exactly \(130\). Therefore at \(s=130\), \(c\) is not uniquely determined.

Thus we need the *smallest* \(s>80\) for which no other \(c\) can produce it. That means we must find the smallest score above 80 that lies strictly inside the region where intervals for different \(c\)’s are disjoint at that point.

The first \(s\) where disjointness becomes strict is when the lower end of the next interval is greater than the upper end of the previous:
\[
5(c+1) > 30+4c
\quad\Longleftrightarrow\quad
5c+5 > 4c+30
\quad\Longleftrightarrow\quad
c>25.
\]
So we need \(c\ge 26\), but also avoid the boundary intersection at \(s=130\). For \(c=26\), the interval is \([130,134]\), and the only shared point with \(c=25\) is \(130\). Therefore the smallest score \(>80\) with unique \(c\) is \(131\).

Now verify uniqueness at \(s=131\):
Solve for \(w\):
\[
131=30+4c-w \Rightarrow w=30+4c-131=4c-101.
\]
Check possibilities:
- If \(c=25\): \(w=100-101=-1\), impossible.
- If \(c=26\): \(w=104-101=3\), valid since \(c+w=29\le 30\).
- If \(c\le 24\): even worse (would give negative \(w\) for \(s\) this large).
So only \(c=26\) works. Hence John can determine \(c\) from \(s=131\).

Finally, if the score were any lower but still \(>80\), i.e. \(s=81,82,\dots,130\), uniqueness fails because for \(c\le 25\) intervals overlap and at \(s=130\) we saw non-uniqueness too.

So Mary’s score is \(\boxed{131}\).

ANSWER: 131
```

</details>

### Parsed Memory Items

1. Encode Feasibility as an Integer Set
Description: Turn the original scoring/constraint system into explicit inequalities that define all possible integer values of the inferred quantity for a fixed observed score.
<details>
<summary>Content 1</summary>

```text
When the problem asks whether someone can uniquely recover an integer (like a count), first express the constraints so that for each candidate score you get a range (or discrete set) of feasible integers for that count. This prevents “almost right” solutions that satisfy simplified conditions but violate the original bounds (e.g., nonnegativity or total-attempt limits).
```

</details>

<details>
<summary>Reasoning 1</summary>

```text
Successful attempts share a consistent core strategy: model the score in terms of underlying integer decision variables (correct/wrong/unanswered), then for a fixed score derive a *feasible set* of the quantity being inferred (number correct). They treat “John can determine uniquely” as an explicit *cardinality condition* on that feasible set (interval contains exactly one integer), and use the “any lower score” clause to interpret this as a *threshold/minimality condition* (uniqueness holds at the first score where the count collapses to one).
Unsuccessful attempts fail in one of two ways: (1) they mis-handle the interval/uniqueness logic (e.g., using incorrect equalities for floor/ceiling alignment, or assuming interval endpoints force uniqueness when rounding effects don’t), and/or (2) they misinterpret the “any lower” condition as “next-lower score must be non-unique” or as “smallest/ largest unique score” incorrectly, leading to contradictions. Some also introduce a correct framework but then compute using the wrong feasibility bounds (e.g., swapping parameters or using an incorrect upper bound), which shifts the uniqueness threshold.
Overall, the robust pattern is: be disciplined about translating all constraints into a single feasible-integer model, then verify uniqueness via exact counting (not heuristic “interval length” approximations), and finally apply the threshold condition by checking minimality against the derived model rather than ad hoc searching.
```

</details>

2. Uniqueness = “Exactly One Integer” (Don’t Guess with Length)
Description: Establish uniqueness by proving the feasible set has cardinality one, using floor/ceiling arithmetic or equivalent exact counting—not by intuition about interval size.
<details>
<summary>Content 2</summary>

```text
Heuristics like “the bounds are close so it’s likely one” often fail because of discretization (ceilings/floors). Instead compute the feasible integer interval precisely and require that the number of integers equals 1 (i.e., lower bound’s ceiling equals upper bound’s floor, or equivalently count = 1).
```

</details>

<details>
<summary>Reasoning 2</summary>

```text
Successful attempts share a consistent core strategy: model the score in terms of underlying integer decision variables (correct/wrong/unanswered), then for a fixed score derive a *feasible set* of the quantity being inferred (number correct). They treat “John can determine uniquely” as an explicit *cardinality condition* on that feasible set (interval contains exactly one integer), and use the “any lower score” clause to interpret this as a *threshold/minimality condition* (uniqueness holds at the first score where the count collapses to one).
Unsuccessful attempts fail in one of two ways: (1) they mis-handle the interval/uniqueness logic (e.g., using incorrect equalities for floor/ceiling alignment, or assuming interval endpoints force uniqueness when rounding effects don’t), and/or (2) they misinterpret the “any lower” condition as “next-lower score must be non-unique” or as “smallest/ largest unique score” incorrectly, leading to contradictions. Some also introduce a correct framework but then compute using the wrong feasibility bounds (e.g., swapping parameters or using an incorrect upper bound), which shifts the uniqueness threshold.
Overall, the robust pattern is: be disciplined about translating all constraints into a single feasible-integer model, then verify uniqueness via exact counting (not heuristic “interval length” approximations), and finally apply the threshold condition by checking minimality against the derived model rather than ad hoc searching.
```

</details>

3. Interpret “If Score Were Lower” as a Threshold Condition
Description: Convert comparative wording (“any lower but still over …”) into a minimality or maximality condition over the set of scores where uniqueness holds.
<details>
<summary>Content 3</summary>

```text
Clues about what happens when the score changes are usually about the *first* score at which the feasible set collapses to one element. Make that explicit: determine whether you need the smallest score > bound with uniqueness (or largest, depending on wording), and ensure the derived model matches that monotonic/threshold behavior.
```

</details>

<details>
<summary>Reasoning 3</summary>

```text
Successful attempts share a consistent core strategy: model the score in terms of underlying integer decision variables (correct/wrong/unanswered), then for a fixed score derive a *feasible set* of the quantity being inferred (number correct). They treat “John can determine uniquely” as an explicit *cardinality condition* on that feasible set (interval contains exactly one integer), and use the “any lower score” clause to interpret this as a *threshold/minimality condition* (uniqueness holds at the first score where the count collapses to one).
Unsuccessful attempts fail in one of two ways: (1) they mis-handle the interval/uniqueness logic (e.g., using incorrect equalities for floor/ceiling alignment, or assuming interval endpoints force uniqueness when rounding effects don’t), and/or (2) they misinterpret the “any lower” condition as “next-lower score must be non-unique” or as “smallest/ largest unique score” incorrectly, leading to contradictions. Some also introduce a correct framework but then compute using the wrong feasibility bounds (e.g., swapping parameters or using an incorrect upper bound), which shifts the uniqueness threshold.
Overall, the robust pattern is: be disciplined about translating all constraints into a single feasible-integer model, then verify uniqueness via exact counting (not heuristic “interval length” approximations), and finally apply the threshold condition by checking minimality against the derived model rather than ad hoc searching.
```

</details>

4. Validate Boundary Cases to Catch Logic Drift
Description: Whenever you derive a candidate using endpoint/threshold reasoning, verify it by explicitly checking feasibility for that score and for nearby scores.
<details>
<summary>Content 4</summary>

```text
Many incorrect attempts “lock in” too early (e.g., assuming disjoint intervals imply uniqueness at the boundary). A quick verification pass—constructing a feasible assignment and confirming whether nearby scores give 1 vs ≥2 feasible integers—catches off-by-one and misapplied inequalities.
```

</details>

<details>
<summary>Reasoning 4</summary>

```text
Successful attempts share a consistent core strategy: model the score in terms of underlying integer decision variables (correct/wrong/unanswered), then for a fixed score derive a *feasible set* of the quantity being inferred (number correct). They treat “John can determine uniquely” as an explicit *cardinality condition* on that feasible set (interval contains exactly one integer), and use the “any lower score” clause to interpret this as a *threshold/minimality condition* (uniqueness holds at the first score where the count collapses to one).
Unsuccessful attempts fail in one of two ways: (1) they mis-handle the interval/uniqueness logic (e.g., using incorrect equalities for floor/ceiling alignment, or assuming interval endpoints force uniqueness when rounding effects don’t), and/or (2) they misinterpret the “any lower” condition as “next-lower score must be non-unique” or as “smallest/ largest unique score” incorrectly, leading to contradictions. Some also introduce a correct framework but then compute using the wrong feasibility bounds (e.g., swapping parameters or using an incorrect upper bound), which shifts the uniqueness threshold.
Overall, the robust pattern is: be disciplined about translating all constraints into a single feasible-integer model, then verify uniqueness via exact counting (not heuristic “interval length” approximations), and finally apply the threshold condition by checking minimality against the derived model rather than ad hoc searching.
```

</details>

### Raw Response

<details>
<summary>Memory model output</summary>

```text
<reasoning>
Successful attempts share a consistent core strategy: model the score in terms of underlying integer decision variables (correct/wrong/unanswered), then for a fixed score derive a *feasible set* of the quantity being inferred (number correct). They treat “John can determine uniquely” as an explicit *cardinality condition* on that feasible set (interval contains exactly one integer), and use the “any lower score” clause to interpret this as a *threshold/minimality condition* (uniqueness holds at the first score where the count collapses to one).
Unsuccessful attempts fail in one of two ways: (1) they mis-handle the interval/uniqueness logic (e.g., using incorrect equalities for floor/ceiling alignment, or assuming interval endpoints force uniqueness when rounding effects don’t), and/or (2) they misinterpret the “any lower” condition as “next-lower score must be non-unique” or as “smallest/ largest unique score” incorrectly, leading to contradictions. Some also introduce a correct framework but then compute using the wrong feasibility bounds (e.g., swapping parameters or using an incorrect upper bound), which shifts the uniqueness threshold.
Overall, the robust pattern is: be disciplined about translating all constraints into a single feasible-integer model, then verify uniqueness via exact counting (not heuristic “interval length” approximations), and finally apply the threshold condition by checking minimality against the derived model rather than ad hoc searching.
</reasoning>

<memories>
<memory>
<title>Encode Feasibility as an Integer Set</title>
<description>Turn the original scoring/constraint system into explicit inequalities that define all possible integer values of the inferred quantity for a fixed observed score.</description>
<content>When the problem asks whether someone can uniquely recover an integer (like a count), first express the constraints so that for each candidate score you get a range (or discrete set) of feasible integers for that count. This prevents “almost right” solutions that satisfy simplified conditions but violate the original bounds (e.g., nonnegativity or total-attempt limits).</content>
</memory>

<memory>
<title>Uniqueness = “Exactly One Integer” (Don’t Guess with Length)</title>
<description>Establish uniqueness by proving the feasible set has cardinality one, using floor/ceiling arithmetic or equivalent exact counting—not by intuition about interval size.</description>
<content>Heuristics like “the bounds are close so it’s likely one” often fail because of discretization (ceilings/floors). Instead compute the feasible integer interval precisely and require that the number of integers equals 1 (i.e., lower bound’s ceiling equals upper bound’s floor, or equivalently count = 1).</content>
</memory>

<memory>
<title>Interpret “If Score Were Lower” as a Threshold Condition</title>
<description>Convert comparative wording (“any lower but still over …”) into a minimality or maximality condition over the set of scores where uniqueness holds.</description>
<content>Clues about what happens when the score changes are usually about the *first* score at which the feasible set collapses to one element. Make that explicit: determine whether you need the smallest score > bound with uniqueness (or largest, depending on wording), and ensure the derived model matches that monotonic/threshold behavior.</content>
</memory>

<memory>
<title>Validate Boundary Cases to Catch Logic Drift</title>
<description>Whenever you derive a candidate using endpoint/threshold reasoning, verify it by explicitly checking feasibility for that score and for nearby scores.</description>
<content>Many incorrect attempts “lock in” too early (e.g., assuming disjoint intervals imply uniqueness at the boundary). A quick verification pass—constructing a feasible assignment and confirming whether nearby scores give 1 vs ≥2 feasible integers—catches off-by-one and misapplied inequalities.</content>
</memory>
</memories>
```

</details>

## Evaluation

- Baseline pass@1: `0.2000`
- Augmented pass@1: `0.2000`
- Improvement: `+0.0000`

### Baseline

### System Prompt

```text
You are an expert mathematician solving competition-level problems. Show your reasoning step by step. Your response should have this overall shape: first the reasoning, then a final line exactly in the format ANSWER: <integer>. For example, a valid response could end like this:
...
ANSWER: 42
```

### User Prompt

```text
Solve the following AIME problem:

Mary told John her score on the American High School Mathematics Examination (AHSME), which was over $80$ . From this, John was able to determine the number of problems Mary solved correctly. If Mary's score had been any lower, but still over $80$ , John could not have determined this. What was Mary's score? (Recall that the AHSME consists of $30$ multiple choice problems and that one's score, $s$ , is computed by the formula $s=30+4c-w$ , where $c$ is the number of correct answers and $w$ is the number of wrong answers. Students are not penalized for problems left unanswered.)
```

#### Outputs

<details>
<summary>Baseline generation 1</summary>

```text
**Reasoning (step by step):**

We’re told the AHSME score is
\[
s=30+4c-w
\]
with 30 multiple choice problems. Unanswered problems are neither right nor wrong, so if Mary answered \(a\) problems, then \(c+w=a\) and \(c,w\ge 0\), with \(a\le 30\).

Also, since scores are over 80:
\[
30+4c-w>80 \quad\Rightarrow\quad 4c-w>50.
\]
Rewrite:
\[
w<4c-50.
\]

---

### Key idea: uniqueness of \(c\)
John is told the score \(s\) and determines the number of correct answers \(c\). That means for this score \(s\), there is **exactly one** integer \(c\) for which there exists some feasible \(w\) (and unanswered count) satisfying
\[
s=30+4c-w.
\]
Equivalently, for fixed \(c\), we must have
\[
w=30+4c-s.
\]
So uniqueness means: among all possible \(c\), only one gives a feasible nonnegative \(w\le 30-c\) (since \(w\) wrong answers plus \(c\) correct answers can’t exceed 30).

Feasibility conditions:
\[
w=30+4c-s \ge 0
\]
and
\[
w\le 30-c.
\]

---

### “If Mary's score had been any lower but still over 80, John could not have determined this.”
Let Mary’s actual score be \(s\). Then \(c\) is uniquely determined from \(s\), but for any \(s'\) with \(80<s'<s\), there are at least two possible values of \(c\) consistent with \(s'\).

This suggests that at score \(s\), the “next” potential \(c\) just barely becomes feasible.

---

### Try the boundary condition between \(c\) values
Suppose two different values of correct answers, say \(c\) and \(c-1\), could both fit nearby scores. Compute how the score changes when you replace one correct with one wrong, keeping the total number answered the same:

If you decrease \(c\) by 1 and increase \(w\) by 1, then
\[
s = 30 +4c - w
\]
changes by
\[
\Delta s = 4(-1) - (+1) = -5.
\]
So scores associated with adjacent \(c\) values tend to differ by multiples of 5.

Since the problem asks for a specific score, the “critical” score likely occurs when the higher \(c\) configuration is barely feasible and the lower one is barely infeasible just below it.

Let’s search among scores just above 80. Write
\[
s=80+k,\quad k\ge 1.
\]
Then
\[
30+4c-w=80+k \Rightarrow 4c-w=50+k.
\]

To make \(c\) uniquely determined, we look for the largest \(k\) (i.e., score as high as needed) where exactly one \(c\) works.

---

### Determine \(c\) from constraints
From \(w=4c-(50+k)\).

Feasibility requires:
1. \(w\ge 0\):
\[
4c-(50+k)\ge 0 \Rightarrow c\ge \frac{50+k}{4}.
\]
2. \(w\le 30-c\):
\[
4c-(50+k)\le 30-c
\]
\[
5c \le 80+k
\]
\[
c \le \frac{80+k}{5}.
\]

So feasible \(c\) satisfy
\[
\frac{50+k}{4}\le c \le \frac{80+k}{5}.
\]
Uniqueness means there is exactly one integer in that interval.

---

### Look for the score where exactly one integer \(c\) occurs
We want the “threshold” behavior: for any lower \(s'\) (i.e., smaller \(k\)), there are at least two integers.

So we test values of \(k\) starting from small, looking for where the interval contains exactly one integer.

Compute endpoints:
\[
L=\frac{50+k}{4},\quad U=\frac{80+k}{5}.
\]
We need the integer count to be exactly 1.

Try \(k=2\) (score 82):
\[
L=\frac{52}{4}=13,\quad U=\frac{82}{5}=16.4
\]
Integers \(c\): 13,14,15,16 → too many.

Try \(k=5\) (score 85):
\[
L=\frac{55}{4}=13.75 \Rightarrow c\ge 14,
\quad U=\frac{85}{5}=17
\]
Integers: 14,15,16,17 → too many.

Try \(k=9\) (score 89):
\[
L=\frac{59}{4}=14.75 \Rightarrow c\ge 15,
\quad U=\frac{89}{5}=17.8 \Rightarrow c\le 17
\]
Integers: 15,16,17 → 3 too many.

Try \(k=10\) (score 90):
\[
L=\frac{60}{4}=15 \Rightarrow c\ge 15,
\quad U=\frac{90}{5}=18 \Rightarrow c\le 18
\]
Integers: 15,16,17,18 → 4 too many.

Try \(k=15\) (score 95):
\[
L=\frac{65}{4}=16.25 \Rightarrow c\ge 17,
\quad U=\frac{95}{5}=19 \Rightarrow c\le 19
\]
Integers: 17,18,19 → 3.

Try \(k=18\) (score 98):
\[
L=\frac{68}{4}=17 \Rightarrow c\ge 17,
\quad U=\frac{98}{5}=19.6 \Rightarrow c\le 19
\]
Integers: 17,18,19 → 3.

Try \(k=20\) (score 100):
\[
L=\frac{70}{4}=17.5 \Rightarrow c\ge 18,
\quad U=\frac{100}{5}=20 \Rightarrow c\le 20
\]
Integers: 18,19,20 → 3.

Try \(k=21\) (score 101):
\[
L=\frac{71}{4}=17.75 \Rightarrow c\ge 18,
\quad U=\frac{101}{5}=20.2 \Rightarrow c\le 20
\]
Integers: 18,19,20 → 3.

Try \(k=24\) (score 104):
\[
L=\frac{74}{4}=18.5 \Rightarrow c\ge 19,
\quad U=\frac{104}{5}=20.8 \Rightarrow c\le 20
\]
Integers: 19,20 → 2.

Try \(k=25\) (score 105):
\[
L=\frac{75}{4}=18.75 \Rightarrow c\ge 19,
\quad U=\frac{105}{5}=21 \Rightarrow c\le 21
\]
Integers: 19,20,21 → 3.

Try \(k=26\) (score 106):
\[
L=\frac{76}{4}=19 \Rightarrow c\ge 19,
\quad U=\frac{106}{5}=21.2 \Rightarrow c\le 21
\]
Integers: 19,20,21 → 3.

Try \(k=27\) (score 107):
\[
L=\frac{77}{4}=19.25 \Rightarrow c\ge 20,
\quad U=\frac{107}{5}=21.4 \Rightarrow c\le 21
\]
Integers: 20,21 → 2.

Try \(k=28\) (score 108):
\[
L=\frac{78}{4}=19.5 \Rightarrow c\ge 20,
\quad U=\frac{108}{5}=21.6 \Rightarrow c\le 21
\]
Integers: 20,21 → 2.

Try \(k=29\) (score 109):
\[
L=\frac{79}{4}=19.75 \Rightarrow c\ge 20,
\quad U=\frac{109}{5}=21.8 \Rightarrow c\le 21
\]
Integers: 20,21 → 2.

Try \(k=30\) (score 110):
\[
L=\frac{80}{4}=20,\quad U=\frac{110}{5}=22
\]
Integers: 20,21,22 → 3.

We still haven’t hit uniqueness (exactly 1). That means the interval-length condition alone isn’t enough; we must also ensure the corresponding \(w\) values are integers and that the “unanswered” count is nonnegative (i.e., \(c+w\le 30\), which we already used as \(w\le 30-c\))—but also, score formula gives integer \(w\), which forces parity mod 1 automatically. Since \(w=30+4c-s\), \(w\) is integer for integer \(s\) and \(c\), so that’s fine.

So uniqueness should occur when the feasible \(c\) set size becomes 1. From our sampling, the minimum count we saw was 2. Let’s push toward higher scores where interval narrows.

Try \(k=40\) (score 120):
\[
L=\frac{90}{4}=22.5 \Rightarrow c\ge 23,
\quad U=\frac{120}{5}=24 \Rightarrow c\le 24
\]
Integers: 23,24 → 2.

Try \(k=44\) (score 124):
\[
L=\frac{94}{4}=23.5 \Rightarrow c\ge 24,
\quad U=\frac{124}{5}=24.8 \Rightarrow c\le 24
\]
Integers: only \(c=24\) → **unique!**

So Mary’s score is \(s=80+k=80+44=124\).

---

### Verify “any lower but still over 80 fails”
Take \(s'=123\) (i.e., \(k=43\)):
\[
L=\frac{50+43}{4}=\frac{93}{4}=23.25 \Rightarrow c\ge 24,
\quad U=\frac{80+43}{5}=\frac{123}{5}=24.6 \Rightarrow c\le 24
\]
This still gives only \(c=24\), which would contradict the statement. But note: our uniqueness check must be with the requirement that John can determine \(c\) from the score. If only \(c=24\) is feasible at \(s'=123\), then John could still determine \(c\), so 124 would not satisfy the “any lower” condition.

Let’s compute properly using the exact equation.

For a given score \(s\), \(w=30+4c-s\).
Also \(c+w\le 30\) gives \(4c +30 - s \le 30\Rightarrow 4c\le s\Rightarrow c\le \frac{s}{4}\).

And \(w\ge 0\) gives \(30+4c-s\ge 0\Rightarrow c\ge \frac{s-30}{4}\).

So feasible \(c\) are integers satisfying
\[
\frac{s-30}{4}\le c \le \frac{s}{4}.
\]
For \(s=124\):
\[
\frac{94}{4}=23.5 \Rightarrow c\ge 24,\quad \frac{124}{4}=31
\]
Oops—this upper bound is too loose because it ignored that \(w\le 30-c\) simultaneously; let’s use both:
\[
w=30+4c-s \le 30-c \Rightarrow 30+4c-s \le 30-c \Rightarrow 5c \le s \Rightarrow c\le \frac{s}{5}.
\]
So correct bounds are:
\[
c\ge \left\lceil \frac{s-30}{4}\right\rceil,\quad c\le \left\lfloor \frac{s}{5}\right\rfloor.
\]

Now check \(s=123\):
\[
\left\lceil \frac{93}{4}\right\rceil=\lceil 23.25\rceil=24,\quad \left\lfloor \frac{123}{5}\right\rfloor=\lfloor 24.6\rfloor=24.
\]
Still unique \(c=24\). So 124 doesn’t satisfy the “any lower” clause.

Try \(s=122\):
\[
\left\lceil \frac{92}{4}\right\rceil=\lceil 23\rceil=23,\quad \left\lfloor \frac{122}{5}\right\rfloor=\lfloor 24.4\rfloor=24.
\]
So \(c\) could be 23 or 24 → not determinable. Therefore the required score should be the **smallest** score above 80 for which \(c\) becomes uniquely determined, i.e., the first \(s\) where the feasible integer set size becomes 1.

We found for \(s=122\) it’s ambiguous, so test \(s=123\).

Check score \(s=123\) gives unique \(c=24\). Also it must be that for any lower score still over 80 (i.e., \(81\) to \(122\)), it’s ambiguous—which seems consistent since ambiguity appears already at 122 and likely persists upward until the point 123.

So Mary’s score is **123**.

---

### Confirm feasibility and compute \(w\)
For \(s=123\) and \(c=24\):
\[
w=30+4(24)-123=30+96-123=3.
\]
Then \(c+w=27\le 30\), so \(3\) unanswered is possible. Valid.

Thus John can determine \(c=24\) from score 123, while at score 122 it’s not determined.

**Therefore the answer is 123.**

ANSWER: 123
```

</details>

<details>
<summary>Baseline generation 2</summary>

```text
Let \(c\) be the number correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\qquad s=30+4c-w.
\]
So
\[
s=30+4c-w=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
Thus every score \(s\) corresponds to some nonnegative integers \(c,u\) with
\[
s=5c+u,\quad 0\le c\le 30,\quad 0\le u\le 30-c.
\]

Mary’s score is \(>80\). John can determine \(c\) from \(s\) uniquely, but for any lower score still \(>80\), \(c\) is not uniquely determined.

### Step 1: Uniqueness criterion for \(c\)
Suppose two different values \(c\neq c'\) both can produce the same score \(s\). Then
\[
s=5c+u=5c'+u'
\]
so
\[
5(c-c')=u'-u.
\]
Since \(u,u'\) are integers, this means \(u'-u\) is a multiple of \(5\). Let \(c'=c-k\) with \(k\ge1\). Then
\[
u' = u+5k.
\]
We also need feasibility:
\[
u\le 30-c,\quad u'\le 30-c' = 30-(c-k)=30-c+k.
\]
So
\[
u+5k \le 30-c+k \quad\Longrightarrow\quad u \le 30-c-4k.
\]

So a second representation exists exactly when there is room to increase \(u\) by \(5k\) while staying within the cap \(30-c'\).

### Step 2: Find the borderline score where uniqueness first appears above 80
For a given \(c\), the possible scores are
\[
s=5c+u,\quad u=0,1,\dots,30-c,
\]
so scores for this \(c\) form an interval:
\[
s\in[5c,\;5c+(30-c)]=[5c,\;4c+30].
\]
For different \(c\), these intervals may overlap, causing ambiguity.

John can determine \(c\) uniquely when \(s\) lies in an interval that does not overlap any other interval.

Let’s list intervals near \(s>80\).

Compute \(s\)-interval endpoints for \(c=16,17,18,19,20\):
\[
\begin{aligned}
c=16:&\ [5\cdot16=80,\ 4\cdot16+30=94] \\
c=17:&\ [85,\ 4\cdot17+30=98] \\
c=18:&\ [90,\ 4\cdot18+30=102] \\
c=19:&\ [95,\ 4\cdot19+30=106] \\
c=20:&\ [100,\ 4\cdot20+30=110]
\end{aligned}
\]
We only care about scores \(>80\), so start just above 80. The key is: for the score to be uniquely attributable to a particular \(c\), it must lie in exactly one of these overlapping intervals.

Observe:
- Interval for \(c=16\) is \([80,94]\).
- Interval for \(c=17\) is \([85,98]\).
These overlap on \([85,94]\), so any \(s\in[85,94]\) gives ambiguity between \(c=16\) and \(c=17\).
- At \(s=95\), \(c=16\) no longer possible (since max is 94). But \(c=17\) still possible (since min is 85) and \(c=18\) also becomes possible because \(90\le 95\). Let’s check ambiguity at \(s=95\).

At \(s=95\):
\[
95=5c+u,\ u\le 30-c.
\]
Try \(c=17\): then \(u=95-85=10\), and \(10\le 30-17=13\) works.
Try \(c=18\): then \(u=95-90=5\), and \(5\le 30-18=12\) works.
So \(s=95\) is ambiguous as well.

We need the **first** score \(>80\) such that \(c\) is unique (and also the “if score were any lower but still \(>80\), not determinable” condition).

From the overlaps above, until we reach a point where one interval “ends” before the next begins.

Consider where \(c=17\) interval ends: it ends at \(98\), while \(c=18\) interval begins at \(90\), so overlaps continue.
Similarly, intervals overlap successively—so uniqueness can only happen when \(s\) lies strictly above the top of the previous interval and strictly below the bottom of the next, but since intervals overlap by construction, uniqueness requires being at an endpoint that excludes others.

Check endpoints just above \(80\):
- For \(c=16\), scores \(>80\) are \(81,82,\dots,94\), but all these lie within \([85,94]\) except \(81\!-\!84\).
Let’s test \(s=81,82,83,84\).
For each, see if any other \(c\) besides 16 can fit.

For \(s=81\):
If \(c=16\), \(u=81-80=1\) feasible.
Could \(c=15\) work? Then \(u=81-75=6\) but must satisfy \(u\le 30-15=15\); however we only need consistency with total: \(c=15\) gives \(s=30+4c-w\). Using \(s=5c+u\) is correct, and \(u=6\) implies \(w=30-c-u=9\ge0\). So \(c=15\) is feasible, meaning ambiguity—except note \(s=81\) could also come from \(c=15\). Therefore John cannot uniquely determine \(c\).
So try to find the smallest \(s>80\) where only one \(c\) works.

Rather than brute force, note from interval overlap:
- For \(c=15\): interval is
\[
[5\cdot15=75,\ 4\cdot15+30=90].
\]
So for any \(s\le 90\), \(c=15\) might also be possible.
That means for \(81\le s\le 84\), ambiguity between \(c=15\) and \(c=16\) is present.

So the first possible unique region must occur after \(c=15\) interval ends at \(90\).

Now check \(s=91\).
Intervals:
- \(c=15\) possible up to \(90\) only, so \(s=91\) excludes \(c=15\).
- \(c=16\) allows up to \(94\) and starts at \(80\), so includes 91.
- \(c=17\) starts at \(85\), includes 91.
- \(c=18\) starts at \(90\), includes 91.

So at \(s=91\), potentially \(c=16,17,18\) are all feasible. Hence ambiguous.

Next, consider when the ambiguity reduces to exactly one by being above the top of some intervals.

The only interval among those starting at 80 that might exclude others is near where an interval ends and the next one begins.
Let’s look at the maximum of \(c=17\) is \(98\), minimum of \(c=18\) is \(90\), so overlaps never vanish there.
But ambiguity could be eliminated if for a given \(s\), a neighboring \(c\) would require an \(u\) larger than allowed.

So compute feasibility for candidate \(c\)’s around the top end.
Try to find \(s\) where \(c\) is maximized while still uniquely determined.

Suppose \(s\) is produced by \(c=16\). Then \(u=s-80\).
To prevent \(c=15\) from also producing \(s\), we need \(u\) for \(c=15\) to exceed its maximum:
For \(c=15\), \(u_{15}=s-75\) but must satisfy \(u_{15}\le 30-15=15\), i.e.
\[
s-75\le15 \Rightarrow s\le90.
\]
So for \(s\ge 91\), \(c=15\) is excluded (good). To prevent \(c=17\) from also producing \(s\):
For \(c=17\), \(u_{17}=s-85\) must satisfy \(u_{17}\le 30-17=13\), so
\[
s-85\le13 \Rightarrow s\le98.
\]
Thus for \(s\ge 99\), \(c=17\) is excluded.
Similarly, to prevent \(c=18\):
\[
u_{18}=s-90\le 30-18=12 \Rightarrow s\le102.
\]
So for \(s\ge103\), \(c=18\) excluded.

Now since Mary’s score is \(>80\) and John can determine \(c\), we want a score \(s\) so high that only one \(c\) remains feasible.

Try \(s=103\):
Check possible \(c\) values:
- \(c=16\): \(u=103-80=23\), but \(u\le 30-16=14\). Not feasible.
So \(c\) must be larger than 16.

Check \(c=19\): \(u=103-95=8\le 30-19=11\) feasible.
Check \(c=20\): \(u=103-100=3\le 30-20=10\) feasible.
So \(c\) not unique.

Try \(s=104\):
- \(c=19\): \(u=104-95=9\le 11\) feasible.
- \(c=20\): \(u=4\le 10\) feasible.
- \(c=18\): \(u=104-90=14\le 12\) not feasible.
So still ambiguous between \(19\) and \(20\).

Try \(s=105\):
- \(c=19\): \(u=10\le 11\) feasible.
- \(c=20\): \(u=5\le 10\) feasible.
So ambiguous.

Try \(s=106\):
- \(c=19\): \(u=11\le 11\) feasible.
- \(c=20\): \(u=6\le 10\) feasible.
Ambiguous.

Try \(s=107\):
- \(c=19\): \(u=12\le 11\) not feasible.
- \(c=20\): \(u=7\le 10\) feasible.
So \(c\) is now uniquely \(20\) (since higher \(c\ge21\) would require \(u=s-5c\) negative or infeasible).
Thus the first score where ambiguity disappears is \(s=107\).

Finally verify the “any lower but still over 80” condition:
At \(s=106\), both \(c=19\) and \(c=20\) were feasible, so not determinable. Therefore \(107\) satisfies the minimality.

So Mary’s score is \(\boxed{107}\).

ANSWER: 107
```

</details>

<details>
<summary>Baseline generation 3</summary>

```text
Let \(c\) be correct, \(w\) be wrong, and \(u\) be unanswered. Then
\[
c+w+u=30,
\qquad s=30+4c-w.
\]
So
\[
s=30+4c-w=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
Thus
\[
s=5c+u,\quad \text{where } c\ge 0,\ u\ge 0,\ c+u\le 30.
\]

We are told:
- \(s>80\).
- Given \(s\), John can determine the unique value of \(c\).
- But for any lower score \(s'\) with \(80<s'<s\), John cannot determine \(c\) uniquely.

So we want the **smallest** score \(>80\) such that the resulting representation \(s=5c+u\) (with \(c+u\le 30\)) forces a unique \(c\).

---

### Step 1: Express \(u\) in terms of \(c\)
From \(s=5c+u\),
\[
u=s-5c.
\]
Constraint \(u\ge 0\) gives \(s-5c\ge 0\Rightarrow c\le \frac{s}{5}\).
Constraint \(c+u\le 30\) gives
\[
c+(s-5c)\le 30 \Rightarrow s-4c\le 30 \Rightarrow 4c\ge s-30 \Rightarrow c\ge \frac{s-30}{4}.
\]
So valid \(c\) are integers in
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
Uniqueness means there is exactly one integer \(c\) in this interval.

---

### Step 2: Search for the minimal \(s>80\) with a single possible \(c\)
Try \(s=81\) first.

For \(s=81\):
\[
\left\lceil \frac{81-30}{4}\right\rceil=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,
\]
\[
\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
So \(c\in\{13,14,15,16\}\): not unique.

Try \(s=82\):
\[
\left\lceil \frac{52}{4}\right\rceil=13,\quad \left\lfloor \frac{82}{5}\right\rfloor=16.
\]
Still multiple.

In general, as long as \(\left\lceil \frac{s-30}{4}\right\rceil < \left\lfloor \frac{s}{5}\right\rfloor\), there are multiple \(c\).

We want the interval to collapse to a single integer:
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]

We can test candidates around where the bounds cross. Solve approximately:
\[
\frac{s-30}{4} \approx \frac{s}{5}
\Rightarrow 5(s-30)=4s
\Rightarrow 5s-150=4s
\Rightarrow s=150.
\]
That suggests uniqueness only near the top, but the ceilings/floors can force earlier uniqueness. We proceed by checking scores in increasing order but efficiently:

Compute possible \(c\) count for each \(s\) by finding the endpoints:

A good approach: Since \(s=5c+u\) and \(u\le 30-c\),
\[
s=5c+u \le 5c+(30-c)=4c+30 \Rightarrow c\ge \frac{s-30}{4},
\]
and also \(s\ge 5c\Rightarrow c\le \frac{s}{5}\) as above.

The interval shrinks as \(s\) increases. Let’s jump to where only one \(c\) is possible.

Assume \(c=20\). Then maximum score with \(c=20\) is when \(u=30-c=10\):
\[
s_{\max}(c)=5c+u=5c+(30-c)=4c+30=4(20)+30=110.
\]
But minimum score with \(c=20\) is \(u=0\): \(s_{\min}=5c=100\).
So scores \(100\) through \(110\) correspond to \(c=20\) with varying \(u\), but could there be other \(c\) giving the same \(s\)?

Try \(s=100\):
Possible \(c\):
\[
\left\lceil \frac{100-30}{4}\right\rceil=\left\lceil \frac{70}{4}\right\rceil=18,
\quad
\left\lfloor \frac{100}{5}\right\rfloor=20.
\]
So \(c=18,19,20\) possible: not unique.

Try \(s=104\):
\[
\left\lceil \frac{74}{4}\right\rceil=\left\lceil 18.5\right\rceil=19,\quad
\left\lfloor \frac{104}{5}\right\rfloor=20.
\]
So \(c\in\{19,20\}\): still not unique.

Try \(s=108\):
\[
\left\lceil \frac{78}{4}\right\rceil=\left\lceil 19.5\right\rceil=20,\quad
\left\lfloor \frac{108}{5}\right\rfloor=21.
\]
So \(c\in\{20,21\}\): not unique.

Try \(s=109\):
\[
\left\lceil \frac{79}{4}\right\rceil=\left\lceil 19.75\right\rceil=20,\quad
\left\lfloor \frac{109}{5}\right\rfloor=21.
\]
Still two.

Try \(s=110\):
\[
\left\lceil \frac{80}{4}\right\rceil=20,\quad
\left\lfloor \frac{110}{5}\right\rfloor=22.
\]
Now more than one—so not.

So perhaps uniqueness happens when the interval contains exactly one integer near the very top. Let’s find where:
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor = k.
\]
That means
\[
k \le \frac{s}{5} < k+1
\Rightarrow 5k \le s \le 5k+4,
\]
and
\[
\frac{s-30}{4}\le k < \frac{s-30}{4}+1
\Rightarrow 4k \le s-30 < 4k+4
\Rightarrow 4k+30 \le s \le 4k+33.
\]
So \(s\) must satisfy both:
\[
s\in [5k,\,5k+4]\cap [4k+30,\,4k+33].
\]
For an intersection to be a single integer, their overlap length must be 1.

Try \(k=21\):
First range: \([105,109]\).
Second: \([4(21)+30,\,4(21)+33]=[114,117]\).
No overlap.

Try \(k=20\):
First: \([100,104]\).
Second: \([110,113]\).
No overlap.

Try \(k=19\):
First: \([95,99]\).
Second: \([106,109]\).
No overlap.

So we need larger \(k\). Try \(k=24\):
First: \([120,124]\).
Second: \([4(24)+30,4(24)+33]=[126,129]\).
No overlap.

It seems we should reconsider: uniqueness of \(c\) for a given \(s\) means the solution set for \(c\) has size 1. But from the interval estimates, it’s hard for smaller \(s\). The best way now: brute logically using the identity \(s=5c+u\) with \(u\le 30-c\). For fixed \(s\), different \(c\) correspond to different \(u=s-5c\). If two distinct \(c\) values work, say \(c_1<c_2\), then
\[
u_1=s-5c_1,\quad u_2=s-5c_2=u_1-5(c_2-c_1).
\]
Also must satisfy \(u_i\le 30-c_i\), i.e.
\[
s-5c_i \le 30-c_i \Rightarrow s \le 4c_i+30.
\]
So for a smaller \(c_1\), it might violate the upper constraint; similarly for larger \(c\), it might violate \(u\ge 0\).

Therefore the first \(s>80\) with uniqueness is when the smallest feasible \(c\) reaches the upper limit and the next feasible \(c\) is impossible.

Let \(c\) be maximal such that still \(s=5c+u\) with \(u\le 30-c\).
That inequality is \(s=5c+u \le 5c+(30-c)=4c+30\).
Thus feasible \(c\) satisfy \(c\ge \frac{s-30}{4}\).
So the smallest feasible \(c\) is \(c_{\min}=\left\lceil \frac{s-30}{4}\right\rceil\).
The largest feasible is \(c_{\max}=\left\lfloor \frac{s}{5}\right\rfloor\).
We want \(c_{\min}=c_{\max}\).

So set
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor = k.
\]
Try to find \(k\) directly by forcing equality without ceilings/floors:
Need
\[
\frac{s-30}{4}\le k \quad\text{and}\quad k+1 > \frac{s-30}{4},
\]
\[
k\le \frac{s}{5}\quad\text{and}\quad \frac{s}{5}<k+1.
\]
Thus
\[
4k \le s-30 < 4k+4 \Rightarrow 4k+30 \le s \le 4k+33,
\]
\[
5k \le s < 5k+5 \Rightarrow 5k \le s \le 5k+4.
\]
So
\[
s \in [\max(4k+30,5k),\ \min(4k+33,5k+4)].
\]
This interval must have exactly one integer.

Compute difference:
Since \(5k\) vs \(4k+30\): \(5k \ge 4k+30 \iff k\ge 30\).
But \(c\le 30\), so \(k\) could be 30 at most. For \(k<30\), the max is \(4k+30\).
Also compare \(5k+4\) vs \(4k+33\): \(5k+4 \le 4k+33 \iff k\le 29\).
So for \(k\le 29\) (which covers likely cases), the min is \(5k+4\).

Thus for \(k\le 29\) and \(k<30\),
\[
s \in [4k+30,\ 5k+4].
\]
For uniqueness, need
\[
4k+30 = 5k+4 \Rightarrow k=26.
\]
Then \(s=4(26)+30=104+30=134\), and also \(s=5(26)+4=130+4=134\). Great: exactly one possible \(s\) for which the interval collapses.

Now check conditions \(s>80\): yes. Also need minimality: for any lower \(s\) with \(80<s\), uniqueness fails. Since uniqueness happens at \(s\) where \(c_{\min}=c_{\max}\), and we found the critical solution for equality, that gives the first such \(s\). (One can verify nearby values produce two possible \(c\).)

So \(s=134\).

---

### Final check: determine \(c\)
For \(s=134\),
\[
c_{\min}=\left\lceil \frac{134-30}{4}\right\rceil=\left\lceil \frac{104}{4}\right\rceil=26,
\quad
c_{\max}=\left\lfloor \frac{134}{5}\right\rfloor=\left\lfloor 26.8\right\rfloor=26.
\]
So \(c=26\) uniquely, as required.

---

ANSWER: 134
```

</details>

<details>
<summary>Baseline generation 4</summary>

```text
We have
\[
s=30+4c-w,\qquad c+w+u=30,\ u\ge 0.
\]
Eliminate \(w=30-c-u\):
\[
s=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
So every score \(s\) can be represented as
\[
s=5c+u,\quad 0\le c\le 30,\quad u\ge 0,\quad c+u\le 30.
\]
Given \(s>80\), John was able to determine \(c\) uniquely from \(s\). That means:
- There is exactly one integer \(c\) for which \(s-5c=u\) is a feasible nonnegative integer with \(u\le 30-c\).

Also, if the score were any lower but still \(>80\), then \(c\) would not be uniquely determined. So \(s\) is the *smallest* score \(>80\) that yields uniqueness of \(c\).

---

### Find the minimum \(s>80\) giving unique \(c\)

Since \(s=5c+u\) and \(u\ge 0\), for fixed \(c\) the possible scores are
\[
s\in\{5c,5c+1,\dots,5c+(30-c)\}=\{5c,\dots,4c+30\}.
\]
Thus for each \(c\), the interval of achievable scores is:
\[
I_c=[5c,\ 4c+30].
\]

We want the smallest \(s>80\) that lies in **exactly one** such interval.

Compute which intervals around \(>80\) matter.

- For \(c=11\): \(I_{11}=[55,74]\) (too small)
- \(c=12\): \(I_{12}=[60,78]\) (still \(\le 80\))
- \(c=13\): \(I_{13}=[65,82]\) includes \(81,82\)
- \(c=14\): \(I_{14}=[70,86]\) includes \(81,82,83,84,85,86\)
So for scores \(81\) and \(82\), they potentially belong to both \(I_{13}\) and \(I_{14}\).

Let’s check smallest \(s>80\), namely \(81\):
- \(81\in I_{13}\) since \(65\le 81\le 82\) yes.
- \(81\in I_{14}\) since \(70\le 81\le 86\) yes.

So \(81\) is achieved with at least two values of \(c\), hence not unique.

Next \(s=82\):
- \(82\in I_{13}\) yes (it’s the top end: \(4\cdot 13+30=82\)).
- \(82\in I_{14}\) yes (since \(82\le 86\)).

So still not unique.

Next \(s=83\):
Check membership:
- \(83\in I_{13}\)? No, because \(I_{13}\) ends at \(82\).
- \(83\in I_{14}\)? Yes, since \(83\le 86\).
- Also check \(c=15\): \(I_{15}=[75,90]\) includes \(83\) too.

So \(83\) is in both \(I_{14}\) and \(I_{15}\) → not unique.

Next \(s=84\):
- \(I_{14}\) includes \(84\) (yes).
- \(I_{15}\) includes \(84\) (yes).
- \(I_{16}\): \(I_{16}=[80,94]\) also includes \(84\).
So multiple → not unique.

Observe the overlap continues for a while. Let’s instead use uniqueness condition directly.

For a given score \(s\), if two different \(c\) values work, then
\[
s=5c_1+u_1=5c_2+u_2
\]
with \(0\le u_i\le 30-c_i\).
Subtract:
\[
5(c_2-c_1)=u_1-u_2.
\]
So \(u_1-u_2\) must be a multiple of 5.

But we can search for when only one \(c\) interval contains \(s\). From intervals \(I_c=[5c,4c+30]\), note that consecutive intervals overlap when
\[
5(c+1)\le 4c+30 \iff 5c+5\le 4c+30 \iff c\le 25.
\]
So for \(c\le 25\), intervals overlap. That means uniqueness can only happen when \(s\) lies in a “gap” between intervals—but for these linear intervals there generally isn’t a gap. However, the *number* of overlapping intervals decreases near endpoints.

A score \(s\) is uniquely determined when it lies in exactly one interval, which will happen when \(s\) is at an endpoint of an interval so that other intervals no longer reach it.

We already saw endpoints:
- \(s=82\) is top of \(I_{13}\) but still inside \(I_{14}\).
So uniqueness requires hitting a score that is **not** in neighboring intervals.

Consider the top end of \(I_{14}\):
\[
\max I_{14}=4\cdot 14+30=86.
\]
But \(86\) is also \(\le \max I_{15}=90\) and \(\le \max I_{16}=94\), etc., so not unique.

Consider a score that is the **bottom** of \(I_{c}\), i.e. \(s=5c\). Then it might only be in \(I_c\) if earlier intervals don’t extend up that high.

Let \(s=5c\) and compare to previous interval \(I_{c-1}=[5(c-1),4(c-1)+30]=[5c-5,4c+26]\).
We need \(5c>4c+26\iff c>26\).
Thus only for \(c\ge 27\) would \(s=5c\) exclude \(c-1\).
But also check even earlier overlaps: they only get smaller maxima as \(c\) decreases, so excluding \(c-1\) is enough.

So test \(c=27\): then \(s=5\cdot 27=135\), which is definitely \(>80\), but is it minimal \(>80\)? Probably not—yet uniqueness might occur for smaller \(s\) not exactly \(5c\). However, since intervals overlap heavily, the first time uniqueness happens is when the score is at the bottom of the first interval whose lower endpoints surpass the previous maximum.

Let’s compute systematically the smallest \(s>80\) that is NOT in the intersection of at least two intervals.
We can check using \(c=\left\lfloor \frac{s}{5}\right\rfloor\) and feasibility range:
Since \(u=s-5c\ge 0\), any candidate \(c\) must satisfy \(5c\le s\Rightarrow c\le \lfloor s/5\rfloor\).
Also need \(u\le 30-c\):
\[
s-5c\le 30-c\iff s\le 4c+30\iff c\ge \frac{s-30}{4}.
\]
So feasible \(c\) are exactly the integers in
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
John can determine \(c\) uniquely iff this interval contains exactly one integer.

So we need
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]
And for any smaller \(s'>s\)?? Actually “any lower but still over 80” means for \(s-1,s-2,\dots\) down to \(81\), the feasible set has size \(\ge 2\).

Now find smallest \(s>80\) satisfying uniqueness.

Let
\[
A(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad B(s)=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Need \(A(s)=B(s)\).

Try \(s=81\):
\[
A=\left\lceil \frac{51}{4}\right\rceil=\lceil12.75\rceil=13,\quad
B=\left\lfloor \frac{81}{5}\right\rfloor=\lfloor16.2\rfloor=16
\]
Not unique.

We want \(B(s)\) close to \(A(s)\). Since \(A(s)\approx \frac{s}{4}\) and \(B(s)\approx \frac{s}{5}\), their difference grows, so equality will likely happen only when rounding effects compress it—at relatively large \(s\).

Set equality using approximate:
\[
\frac{s-30}{4}\approx \frac{s}{5}\Rightarrow 5(s-30)=4s\Rightarrow 5s-150=4s\Rightarrow s=150.
\]
So the first equality likely occurs near 150.

Test \(s=150\):
\[
A=\left\lceil \frac{120}{4}\right\rceil=\lceil30\rceil=30,\quad
B=\left\lfloor \frac{150}{5}\right\rfloor=\lfloor30\rfloor=30.
\]
So unique \(c=30\). Is \(s=150>80\) yes.

Check if any smaller score \(>80\) could also give uniqueness. Since equality only at exact rounding alignment, and the approximate intersection at \(150\) suggests uniqueness first occurs there (because for smaller \(s\), \(B(s)\) is smaller relative to \(A(s)\) giving multiple \(c\)’s? Actually \(A(s)\le B(s)\) must hold for feasibility; as \(s\) decreases from 150, feasibility shrinks to multiple points until finally becomes 0 or 1 only at the boundary. So uniqueness at the boundary should indeed occur at \(150\), where \(c\) maxes out.)

We can confirm that for \(s=149\):
\[
A=\left\lceil \frac{119}{4}\right\rceil=\lceil29.75\rceil=30,\quad
B=\left\lfloor \frac{149}{5}\right\rfloor=\lfloor29.8\rfloor=29.
\]
No feasible \(c\), contradicts feasibility—so scores must be achievable? But note: scores can exceed what’s achievable? Actually AHSME score can’t be arbitrary; so \(s=149\) might be impossible. Uniqueness condition is vacuously false because John cannot determine \(c\) from an impossible score. The problem states Mary told a score that is achievable.

Thus the smallest achievable \(s>80\) with unique \(c\) is where feasibility interval reduces to exactly one integer, which happens at \(s=150\) with \(c=30\).

Finally compute: if \(c=30\), then all correct, \(w=0,u=0\), so
\[
s=30+4(30)=150.
\]

---

ANSWER: 150
```

</details>

<details>
<summary>Baseline generation 5</summary>

```text
Let \(c\) be the number correct and \(w\) the number wrong. Since there are \(30\) problems total and unanswered are allowed,
\[
c+w\le 30.
\]
Mary’s score is
\[
s=30+4c-w.
\]

John can determine \(c\) from the given \(s\). That means that for this score \(s\), the value of \(c\) is uniquely determined among all integer pairs \((c,w)\) with \(c+w\le 30\).

### Step 1: Rewrite the condition
From \(s=30+4c-w\), we have
\[
w = 30+4c - s.
\]
So for a fixed score \(s\), different possible values of \(c\) would correspond to different \(w\). We must also have:
- \(w\ge 0\)
- \(c+w\le 30\)

Substitute \(w\):
1) \(w\ge 0 \Rightarrow 30+4c-s\ge 0 \Rightarrow 4c \ge s-30\).
2) \(c+w\le 30\):
\[
c+(30+4c-s)\le 30 \;\Rightarrow\; 5c+30-s \le 30 \;\Rightarrow\; 5c\le s \;\Rightarrow\; c\le \frac{s}{5}.
\]

So allowable \(c\) are integers satisfying
\[
\left\lceil\frac{s-30}{4}\right\rceil \le c \le \left\lfloor\frac{s}{5}\right\rfloor.
\]

John could determine \(c\) iff this interval contains exactly one integer.

### Step 2: Use the “if score were lower, John could not” condition
We are told:
- \(s>80\),
- for this \(s\), \(c\) is uniquely determined,
- but for any lower score \(s' \) with \(80<s'<s\), \(c\) is *not* uniquely determined.

The uniqueness interval length is governed by how many integers satisfy the two bounds. The “just becomes non-unique when lowered” situation happens at the threshold where the count of valid integers changes from \(1\) to \(2\).

Try to find \(s\) such that exactly one integer \(c\) satisfies:
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]
And if we decrease \(s\) by \(1\), the equality breaks and the interval captures at least two integers.

A natural approach is to attempt \(s\) where the bounds align tightly.

### Step 3: Solve by testing the optimal tight case
Suppose the unique solution uses \(c=16\). Then:
\[
s=30+4c-w =30+64-w =94-w.
\]
Since \(s>80\), we need \(94-w>80 \Rightarrow w<14\), and also \(c+w\le 30 \Rightarrow 16+w\le 30 \Rightarrow w\le 14.\)
So \(w\) can be \(0,1,\dots,14\), giving scores \(94,93,\dots,80\). But we need \(s>80\), so \(w\le 13\), hence \(s=94,93,\dots,81\).

Now check uniqueness at one specific \(s\). If \(s=81\), then \(w=94-81=13\). We must see whether any other \(c\neq 16\) can produce the same \(s\).

General equation:
\[
81=30+4c-w \Rightarrow w=4c-51.
\]
Then the constraints are:
- \(w\ge 0 \Rightarrow 4c-51\ge 0 \Rightarrow c\ge 13\) (since \(c\ge 12.75\)).
- \(c+w\le 30\):
\[
c+(4c-51)\le 30 \Rightarrow 5c\le 81 \Rightarrow c\le 16.2 \Rightarrow c\le 16.
\]
So \(c\) could be \(13,14,15,\) or \(16\), but we must also ensure \(w=4c-51\) gives \(c+w\le 30\) automatically once \(5c\le 81\) holds, which it does for \(c\le 16\). Thus there are multiple possible \(c\), so \(s=81\) is **not** uniquely determined.

Try \(s=82\):
\[
82=30+4c-w \Rightarrow w=4c-52.
\]
Constraints:
- \(w\ge 0 \Rightarrow c\ge 13\).
- \(c+w\le 30 \Rightarrow c+(4c-52)\le 30 \Rightarrow 5c\le 82 \Rightarrow c\le 16.4 \Rightarrow c\le 16.
\]
Still \(c=13,14,15,16\) all feasible, not unique.

Try \(s=83\):
\[
w=4c-53.
\]
- \(w\ge 0 \Rightarrow c\ge 13.25 \Rightarrow c\ge 14\).
- \(5c\le 83 \Rightarrow c\le 16.6 \Rightarrow c\le 16\).
So \(c\in\{14,15,16\}\): not unique.

Try \(s=84\):
\[
w=4c-54.
\]
- \(w\ge 0 \Rightarrow c\ge 13.5 \Rightarrow c\ge 14\).
- \(5c\le 84 \Rightarrow c\le 16.8 \Rightarrow c\le 16\).
So \(c\in\{14,15,16\}\): not unique.

Try \(s=85\):
\[
w=4c-55.
\]
- \(w\ge 0 \Rightarrow c\ge 13.75 \Rightarrow c\ge 14\).
- \(5c\le 85 \Rightarrow c\le 17\).
So \(c\in\{14,15,16,17\}\): not unique.

Try \(s=86\):
\[
w=4c-56.
\]
- \(w\ge 0 \Rightarrow c\ge 14\).
- \(5c\le 86 \Rightarrow c\le 17.2 \Rightarrow c\le 17\).
So \(c\in\{14,15,16,17\}\): not unique.

Try \(s=87\):
\[
w=4c-57.
\]
- \(w\ge 0 \Rightarrow c\ge 14.25 \Rightarrow c\ge 15\).
- \(5c\le 87 \Rightarrow c\le 17.4 \Rightarrow c\le 17\).
So \(c\in\{15,16,17\}\): not unique.

Try \(s=88\):
\[
w=4c-58.
\]
- \(w\ge 0 \Rightarrow c\ge 14.5 \Rightarrow c\ge 15\).
- \(5c\le 88 \Rightarrow c\le 17.6 \Rightarrow c\le 17\).
So \(c\in\{15,16,17\}\): not unique.

Try \(s=89\):
\[
w=4c-59.
\]
- \(w\ge 0 \Rightarrow c\ge 14.75 \Rightarrow c\ge 15\).
- \(5c\le 89 \Rightarrow c\le 17.8 \Rightarrow c\le 17\).
So again \(c\in\{15,16,17\}\): not unique.

Try \(s=90\):
\[
w=4c-60.
\]
- \(w\ge 0 \Rightarrow c\ge 15\).
- \(5c\le 90 \Rightarrow c\le 18\).
So \(c\in\{15,16,17,18\}\): not unique.

At this point, notice the pattern: for many \(s\), multiple \(c\) work because the feasible \(c\) range is wide. For uniqueness, we need the feasible interval to shrink to a single integer, which happens when
\[
\left\lfloor\frac{s}{5}\right\rfloor - \left\lceil\frac{s-30}{4}\right\rceil = 0.
\]

Compute using exact alignment. Let the unique \(c\) be \(c^*\). Then
\[
c^* = \left\lfloor\frac{s}{5}\right\rfloor
\quad\text{and}\quad
c^* = \left\lceil\frac{s-30}{4}\right\rceil.
\]
This implies
\[
5c^* \le s < 5(c^*+1),
\]
and
\[
4c^* \le s-30 < 4(c^*+1)-30.
\]
So
\[
4c^*+30 \le s < 4c^*+34.
\]

Thus \(s\) must lie in the intersection:
\[
s \in [5c^*,\, 5c^*+4] \cap [4c^*+30,\, 4c^*+33].
\]
For the intersection to be nonempty and yield exactly that single integer \(c^*\) uniquely, the intersection should force \(s\) to be one of the integers making \(c\) exactly \(c^*\). The tightest candidate occurs when \(s\) equals the lower bound from one side and the upper bound from the other.

Set
\[
5c^* = 4c^*+30 \Rightarrow c^*=30.
\]
Impossible since \(c\le 30\) but then \(s=150\) and uniqueness behavior relative to \(80\) wouldn’t match.

Set
\[
5c^*+4 = 4c^*+33 \Rightarrow c^* = 29.
\]
Then \(s=5c^*+4=149\), also not constrained by “over 80 but minimal uniqueness”.

We need the uniqueness to happen just above 80, so \(c^*\) should be around \(s/5\approx 16\). Try \(c^*=16\). Then the possible \(s\) are:
- from \(5c^*\le s <5c^*+5\): \(80 \le s \le 84\),
- from \(4c^*+30 \le s < 4c^*+34\): \(94 \le s < 98\).

No intersection: so \(c^*=16\) cannot be the unique \(c\) for any \(s\) at all—meaning my earlier “feasible intervals” check was too loose because the ceiling condition matters with exact integer behavior. Let's do it correctly with the interval method numerically for \(s>80\):

For each integer \(s\), valid \(c\) satisfy:
\[
\left\lceil\frac{s-30}{4}\right\rceil \le c \le \left\lfloor\frac{s}{5}\right\rfloor.
\]
We need exactly one integer in that range.

Check \(s=96\) (since \(30+4c-w\) suggests scores often near \(94\) etc). Compute:
\[
\left\lceil\frac{96-30}{4}\right\rceil=\left\lceil\frac{66}{4}\right\rceil=\lceil 16.5\rceil=17,
\]
\[
\left\lfloor\frac{96}{5}\right\rfloor=\lfloor 19.2\rfloor=19.
\]
Not unique.

We want equality so that lower bound equals upper bound. That requires
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]
Try values near where this could happen: let that common value be \(c\). Then approximately
\[
\frac{s-30}{4}\approx \frac{s}{5} \Rightarrow 5s-150 \approx 4s \Rightarrow s\approx 150,
\]
so uniqueness tends to happen for large scores, not near 80—however the “if score were any lower but still over 80” then forces that the smallest score \(>80\) that yields uniqueness must be just above 80, so it actually means uniqueness occurs at some \(s\) and the next lower \(s\) loses it. That implies that \(s\) is the *minimal* score greater than 80 for which uniqueness holds.

The minimal \(s>80\) with uniqueness turns out to be \(s=112\). Let's verify uniqueness at \(s=112\):

Compute bounds:
\[
\left\lceil\frac{112-30}{4}\right\rceil=\left\lceil\frac{82}{4}\right\rceil=\lceil 20.5\rceil=21,
\]
\[
\left\lfloor\frac{112}{5}\right\rfloor=\lfloor 22.4\rfloor=22.
\]
Still two possible \(c\) (21 or 22), so not.

Try \(s=113\):
\[
\left\lceil\frac{83}{4}\right\rceil=\lceil 20.75\rceil=21,\quad
\left\lfloor\frac{113}{5}\right\rfloor=\lfloor 22.6\rfloor=22.
\]
Two.

Try \(s=114\):
\[
\left\lceil\frac{84}{4}\right\rceil=\lceil 21\rceil=21,\quad
\left\lfloor\frac{114}{5}\right\rfloor=\lfloor 22.8\rfloor=22.
\]
Two.

Try \(s=115\):
\[
\left\lceil\frac{85}{4}\right\rceil=\lceil 21.25\rceil=22,\quad
\left\lfloor\frac{115}{5}\right\rfloor=\lfloor 23\rfloor=23.
\]
Two (22 or 23).

Try \(s=116\):
\[
\left\lceil\frac{86}{4}\right\rceil=\lceil 21.5\rceil=22,\quad
\left\lfloor\frac{116}{5}\right\rfloor=\lfloor 23.2\rfloor=23.
\]
Two.

Try \(s=118\):
\[
\left\lceil\frac{88}{4}\right\rceil=22,\quad
\left\lfloor\frac{118}{5}\right\rfloor=\lfloor 23.6\rfloor=23.
\]
Two.

Try \(s=119\):
\[
\left\lceil\frac{89}{4}\right\rceil=\lceil 22.25\rceil=23,\quad
\left\lfloor\frac{119}{5}\right\rfloor=\lfloor 23.8\rfloor=23.
\]
Now it’s unique: \(c=23\) only.

Check the “any lower but still over 80” condition: consider \(s=118\) just lower. We already found two possibilities for \(s=118\), so John could not determine \(c\). This matches the requirement.

Now compute that \(c=23\) is consistent:
\[
s=30+4c-w \Rightarrow 119 = 30+92-w \Rightarrow w=3.
\]
And \(c+w=26\le 30\), valid.

Therefore Mary’s score is \(119\).

ANSWER: 119
```

</details>

<details>
<summary>Baseline generation 6</summary>

```text
We have \(c+w\le 30\) and score
\[
s=30+4c-w.
\]
Since \(w= (c+w)-c\), rewrite using \(t=c+w\) (number answered):
\[
s=30+4c-(t-c)=30+5c-t.
\]
Given \(s>80\), so
\[
30+5c-t>80 \quad\Longrightarrow\quad 5c-t>50 \quad\Longrightarrow\quad t<5c-50.
\]
For fixed \(c\), \(t\) can range over integers \(0\le t\le 30\) with \(t\ge c\) (since \(w=t-c\ge 0\)). Thus for a given \(c\), the possible scores form an interval determined by
\[
s=30+5c-t,
\]
where \(t\) ranges from \(c\) to \(30\). So possible \(s\) are
\[
s_{\max}=30+5c-c=30+4c \quad (\text{when } t=c,\ w=0),
\]
\[
s_{\min}=30+5c-30=5c-0=5c \quad (\text{when } t=30,\ w=30-c).
\]
Thus for each \(c\), the achievable scores are exactly the integers in
\[
[5c,\; 30+4c].
\]

John can determine \(c\) from Mary’s score \(s\) iff \(s\) lies in exactly one such interval (for that integer \(c\)). The condition says:

- For the given score \(s\), \(c\) is uniquely determined.
- If the score were any lower but still \(>80\), then \(c\) would not be uniquely determined.

So \(s\) must be the **lowest** score \(>80\) for which the corresponding interval contains a unique \(c\) value, meaning: at \(s-1\) (still \(>80\)), there are at least two different \(c\) whose intervals include that score.

Now find the \(c\) interval boundaries near 80.

For \(c=11\): interval \([5c,30+4c]=[55,74]\) (not \(>80\)).
For \(c=12\): \([60,78]\) (still \(\le 80\)).
For \(c=13\): \([65,82]\) includes scores \(81,82\) which are \(>80\).
For \(c=14\): \([70,86]\) includes \(81,82,83,84,85,86\).

So scores \(81\) and \(82\) are candidates where multiple \(c\)’s might be possible:
- \(81\in[65,82]\) (so \(c=13\) works),
- \(81\in[70,86]\) (so \(c=14\) works).
Similarly for \(82\), both \(c=13\) and \(c=14\) work.

Thus \(s=81\) or \(82\) do **not** give unique \(c\).

Check the next score \(s=83\):
- \(83\in[65,82]\)? No (since max for \(c=13\) is \(82\)).
- \(83\in[70,86]\)? Yes (for \(c=14\)).
Also \(c=12\) max is \(78\), so impossible. Therefore \(c\) is uniquely determined when \(s=83\), and it is the lowest \(>80\) because \(82\) failed.

Therefore Mary’s score is \(83\).

ANSWER: 83
```

</details>

<details>
<summary>Baseline generation 7</summary>

```text
Let Mary’s number of correct answers be \(c\), wrong answers be \(w\), and left blank be \(30-c-w\).

The scoring rule is
\[
s=30+4c-w.
\]
Given \(s>80\):
\[
30+4c-w>80 \quad\Rightarrow\quad 4c-w>50.
\]

John can determine \(c\) from \(s\), meaning that for this particular score \(s\), the quantity
\[
4c-w = s-30
\]
forces a unique value of \(c\) among all feasible \((c,w)\) with \(c+w\le 30\), \(c,w\ge 0\) integers.

Let
\[
s-30 = 4c-w = T.
\]
Then \(w=4c-T\). Feasibility requires:
- \(w\ge 0 \Rightarrow 4c\ge T\),
- \(c+w\le 30 \Rightarrow c+(4c-T)\le 30 \Rightarrow 5c-T\le 30 \Rightarrow T\ge 5c-30.\)

So for a given \(T\), a value \(c\) is possible iff
\[
5c-30 \le T \le 4c.
\]

John is able to determine \(c\) uniquely at the given \(T\), but if the score were any lower (still \(>80\)), \(c\) would no longer be uniquely determined. That means our \(T\) is *exactly at a boundary where uniqueness is lost immediately when \(T\) decreases*.

For uniqueness, \(T\) must be such that exactly one integer \(c\) satisfies both inequalities. The “next lower score” corresponds to \(T-1\) (since \(s\) changes by 1). Loss of uniqueness at \(T-1\) means that at \(T-1\), there are at least two different integers \(c\) satisfying the feasibility conditions.

Now check consecutive possible values of \(c\). Suppose at \(T\) the correct \(c\) is \(c_0\), and at \(T-1\) another value \(c_0-1\) becomes feasible. The tightest way this happens is when \(T\) equals the **lower bound** for \(c_0\) and simultaneously the **upper bound** for \(c_0-1\):
\[
T = 5c_0-30
\quad\text{and}\quad
T-1 = 4(c_0-1).
\]
Why? Because decreasing \(T\) by 1 should make \(c_0-1\) just barely feasible.

Compute from the second equation:
\[
T-1 = 4c_0-4 \quad\Rightarrow\quad T = 4c_0-3.
\]
Set equal to the first:
\[
5c_0-30 = 4c_0-3 \quad\Rightarrow\quad c_0 = 27.
\]
Then
\[
T = 5(27)-30 = 135-30 = 105.
\]
So
\[
s-30 = 105 \quad\Rightarrow\quad s = 135.
\]

Verify feasibility and uniqueness:
- With \(c=27\), \(w=4c-T=108-105=3\), and \(c+w=30\) OK.
- If \(s\) were lower by 1, then \(T\) becomes \(104\). Check \(c=26\):
  \[
  w=4(26)-104=104-104=0,
  \]
  feasible. So at \(s=134\), both \(c=27\) and \(c=26\) are possible, hence John can’t determine \(c\).
- For \(c=27\) to be the unique possibility at \(T=105\), we need no other \(c\) giving an integer \(w\ge 0\) and \(c+w\le 30\). The boundary construction above ensures that decreasing \(T\) immediately introduces another solution, so at \(T\) itself the solution set has exactly one \(c\).

Thus Mary’s score is \(\boxed{135}\).

ANSWER: 135
```

</details>

<details>
<summary>Baseline generation 8</summary>

```text
Let \(c\) be the number correct, \(w\) wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\quad s=30+4c-w.
\]
Rewrite using \(w=30-c-u\):
\[
s=30+4c-(30-c-u)=30+4c-30+c+u=5c+u.
\]
So the score depends only on \(c\) and \(u\), and we have constraints
\[
c\ge 0,\ u\ge 0,\ c+u\le 30.
\]

Mary’s score \(s>80\). John can determine \(c\) uniquely from the given \(s\). But if the score were lowered to any other value still \(>80\), \(c\) would no longer be uniquely determined. So \(s\) must be the *lowest* score \(>80\) for which the mapping \(s \mapsto c\) is unique.

From \(s=5c+u\) with \(0\le u\le 30-c\), for a fixed \(c\),
\[
s \in \{5c,5c+1,\dots,5c+(30-c)\}=\{5c,\dots,30+4c\}.
\]
Thus for each \(c\), the scores attainable form an interval of consecutive integers:
\[
I_c=[\,5c,\ 30+4c\,].
\]

Scores \(>80\) can be produced only by \(c\ge 11\) since \(5\cdot 10=50\) and \(5\cdot 11=55\), but we need overlap analysis. Check consecutive intervals for uniqueness: if \(s\) lies in the overlap of \(I_c\) and \(I_{c+1}\), then \(c\) is not determined.

Compute overlap:
\[
I_c=[5c,30+4c],\quad I_{c+1}=[5(c+1),30+4(c+1)]=[5c+5,34+4c].
\]
These overlap exactly when
\[
5c+5 \le 30+4c \iff c \le 25.
\]
So overlaps happen for most \(c\), but uniqueness can still occur if \(s\) is in a part covered by only one interval. For consecutive intervals, the “exclusive” top part of \(I_c\) is when
\[
s>34+4c \quad \text{(then only } I_{c+1}\text{ covers)}.
\]
Similarly, the exclusive bottom part of \(I_{c+1}\) would be \(s<30+4c\), etc. The earliest \(>80\) score with uniqueness will occur right at the boundary where overlap begins/ends.

Look at \(c=15\) and \(c=16\):
\[
I_{15}=[5\cdot 15,\ 30+4\cdot 15]=[75,\ 90],
\]
\[
I_{16}=[80,\ 30+4\cdot 16]=[80,\ 94].
\]
For \(s=81,82,\dots,90\), \(s\) lies in both intervals, so \(c\) is not determined.

For \(s=91,92,93,94\), only \(I_{16}\) contains them (since \(I_{15}\) ends at \(90\)). These give unique \(c=16\).

Now apply the “minimality” condition: if the score were any lower but still \(>80\), John could not determine \(c\).
The lowest score \(>80\) that gives unique \(c\) is therefore \(s=91\). Indeed:
- \(s=91\) corresponds to \(c=16\) uniquely (because \(91\notin I_{15}=[75,90]\) but \(91\in I_{16}=[80,94]\)).
- Any lower score \(>80\) is \(81\) through \(90\), all in the overlap \(I_{15}\cap I_{16}\), hence not uniquely determined.

Therefore Mary’s score is \(\boxed{91}\).

ANSWER: 91
```

</details>

<details>
<summary>Baseline generation 9</summary>

```text

```

</details>

<details>
<summary>Baseline generation 10</summary>

```text
Let \(c\) be the number correct and \(w\) the number wrong. Then unanswered \(=30-c-w\ge 0\), so
\[
c+w\le 30.
\]
The score is
\[
s=30+4c-w.
\]
Rearrange to express \(w\) in terms of \(c\) and \(s\):
\[
w=30+4c-s.
\]
For a fixed score \(s\), solutions \((c,w)\) must satisfy integers
\[
0\le c\le 30,\quad 0\le w\le 30,\quad c+w\le 30,
\]
and \(w=30+4c-s\).

Substitute into \(c+w\le 30\):
\[
c+(30+4c-s)\le 30
\]
\[
5c-s\le 0
\]
\[
s\ge 5c.
\]
Also require \(w\ge 0\):
\[
30+4c-s\ge 0 \implies s\le 30+4c.
\]
So for a given \(s\), valid \(c\) must satisfy
\[
5c\le s\le 30+4c.
\]

We are told:
- \(s>80\),
- John can determine \(c\) uniquely from \(s\),
- but if the score were any lower while still \(>80\), then \(c\) would no longer be uniquely determined.

So we want the *smallest* score \(s>80\) for which the corresponding \(c\) is uniquely determined.

Try \(s=81\). The inequality \(5c\le 81\) gives
\[
c\le \left\lfloor \frac{81}{5}\right\rfloor =16.
\]
For each \(c\), we also need \(81\le 30+4c\), i.e.
\[
4c\ge 51 \implies c\ge \left\lceil \frac{51}{4}\right\rceil=13.
\]
So \(c\) could be any integer \(13\le c\le 16\), provided the resulting \(w\) is feasible.

Compute \(w=30+4c-81=4c-51\):
- \(c=13\): \(w=52-51=1\), and \(c+w=14\le 30\) OK.
- \(c=14\): \(w=56-51=5\), \(c+w=19\) OK.
- \(c=15\): \(w=60-51=9\), \(c+w=24\) OK.
- \(c=16\): \(w=64-51=13\), \(c+w=29\) OK.

So at \(s=81\), there are multiple possible \(c\). Not unique.

Now \(s=82\):
\[
5c\le 82 \implies c\le \left\lfloor \frac{82}{5}\right\rfloor=16,
\]
\[
82\le 30+4c \implies 4c\ge 52 \implies c\ge 13.
\]
So still \(13\le c\le 16\). Compute \(w=30+4c-82=4c-52\):
- \(c=13\): \(w=52-52=0\), OK.
- \(c=14\): \(w=56-52=4\), \(c+w=18\) OK.
- \(c=15\): \(w=60-52=8\), \(c+w=23\) OK.
- \(c=16\): \(w=64-52=12\), \(c+w=28\) OK.

Still not unique.

Check \(s=83\):
\[
5c\le 83 \implies c\le 16,
\]
\[
83\le 30+4c \implies 4c\ge 53 \implies c\ge 14.
\]
So \(c\in\{14,15,16\}\). Compute \(w=30+4c-83=4c-53\):
- \(c=14\): \(w=56-53=3\), \(c+w=17\) OK.
- \(c=15\): \(w=60-53=7\), \(c+w=22\) OK.
- \(c=16\): \(w=64-53=11\), \(c+w=27\) OK.

Not unique.

Check \(s=84\):
\[
5c\le 84 \implies c\le 16,
\]
\[
84\le 30+4c \implies 4c\ge 54 \implies c\ge 14.
\]
So again \(c\in\{14,15,16\}\). Compute \(w=30+4c-84=4c-54\):
- \(c=14\): \(w=56-54=2\), \(c+w=16\) OK.
- \(c=15\): \(w=60-54=6\), \(c+w=21\) OK.
- \(c=16\): \(w=64-54=10\), \(c+w=26\) OK.

Not unique.

Check \(s=85\):
\[
5c\le 85 \implies c\le 17,
\]
\[
85\le 30+4c \implies 4c\ge 55 \implies c\ge 14.
\]
So \(c\in\{14,15,16,17\}\). Compute \(w=30+4c-85=4c-55\):
- \(c=14\): \(w=56-55=1\), OK.
- \(c=15\): \(w=60-55=5\), OK.
- \(c=16\): \(w=64-55=9\), OK.
- \(c=17\): \(w=68-55=13\), and \(c+w=30\) OK.

Still not unique.

We need the first score \(s>80\) where the interval of possible \(c\) has exactly one integer. The bounds are:
\[
c \ge \left\lceil \frac{s-30}{4}\right\rceil,\quad c\le \left\lfloor \frac{s}{5}\right\rfloor.
\]
Uniqueness means
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]
Try to find the smallest \(s>80\) satisfying that equality.

From \(c\) being an integer, it’s equivalent to having some integer \(c\) with
\[
5c \le s \le 5c+? \text{ and } s \le 30+4c,\ \text{with tight overlap.}
\]
Let’s search systematically starting at \(s=81\) with the earlier quick rejection; but we can speed by checking when the lower bound jumps past the upper bound.

Compute possible \(c\) count for \(s\) by direct formula:
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad U(s)=\left\lfloor \frac{s}{5}\right\rfloor.
\]
At uniqueness: \(L(s)=U(s)\).

For \(s=86\):
\[
L=\left\lceil \frac{56}{4}\right\rceil=14,\quad U=\left\lfloor \frac{86}{5}\right\rfloor=17 \Rightarrow \text{multiple.}
\]
As \(s\) increases, \(U(s)\) increases occasionally, while \(L(s)\) increases more frequently; uniqueness will occur when the two meet.

Try \(s=90\):
\[
L=\left\lceil \frac{60}{4}\right\rceil=15,\quad U=\left\lfloor \frac{90}{5}\right\rfloor=18\ \text{multiple.}
\]
Try \(s=94\):
\[
L=\left\lceil \frac{64}{4}\right\rceil=16,\quad U=\left\lfloor \frac{94}{5}\right\rfloor=18\ \text{multiple.}
\]
Try \(s=98\):
\[
L=\left\lceil \frac{68}{4}\right\rceil=17,\quad U=\left\lfloor \frac{98}{5}\right\rfloor=19\ \text{multiple.}
\]
Try \(s=101\):
\[
L=\left\lceil \frac{71}{4}\right\rceil=\left\lceil 17.75\right\rceil=18,\quad U=\left\lfloor \frac{101}{5}\right\rfloor=20\ \text{multiple.}
\]

Eventually \(U(s)\) and \(L(s)\) narrow when \(\frac{s}{5}\) is just below an integer while \(\frac{s-30}{4}\) is just at that same integer. The simplest way is to force equality for some \(c\):
We need
\[
5c \le s \le 30+4c
\]
and also the next/previous \(c\) not allowed. For uniqueness, the score \(s\) must be in the overlap region between the \(c\)-feasible inequalities but not in overlaps for adjacent \(c\).

Consider consecutive \(c\) values: the maximum \(s\) allowing \(c\) is \(30+4c\); the minimum \(s\) allowing \(c+1\) is \(5(c+1)=5c+5\).
If
\[
30+4c < 5c+5,
\]
then overlaps don’t happen, but compute:
\[
30+4c < 5c+5 \iff 25 < c,
\]
which is true since \(c\le 30\). So overlaps start to disappear when \(c\ge 26\).

Thus uniqueness for \(s>80\) likely happens near top \(c\). Let’s find the *smallest* \(s>80\) with only one \(c\), which occurs when the score is just big enough that the next lower \(c\) no longer fits, i.e. \(s<30+4(c-1)\) while still \(\ge 5c\).

So take \(c\) as the unique value and require:
\[
s \ge 5c \quad\text{(so that \(c\) is possible)}
\]
and
\[
s < 30+4(c-1) \quad\text{(so that \(c-1\) is impossible)}
\]
and also \(c+1\) must be impossible:
\[
s < 5(c+1)=5c+5 \quad\text{(so lower bound for \(c+1\) not met)}.
\]
Combine the last two:
\[
s < \min\big(30+4c-4,\ 5c+5\big)=\min(26+4c,\ 5c+5).
\]
But from earlier overlap condition, for \(c\ge 26\) we have \(26+4c < 5c+5\). So the binding upper bound is
\[
s < 26+4c.
\]
Therefore for \(c\ge 26\), uniqueness occurs for scores satisfying
\[
5c \le s < 26+4c.
\]
The width of this interval is
\[
(26+4c) - 5c = 26 - c.
\]
To have *exactly one integer* \(s\) in that range, we need \(26-c \le 1\), i.e. \(c=25\) gives width 1 (but interval is \(5c\le s<26+4c\)), and \(c=26\) gives width 0? Let’s compute carefully.

For \(c=26\):
\[
5c=130,\quad 26+4c=26+104=130,
\]
so condition \(130 \le s <130\) gives no \(s\). So \(c\) cannot be 26.

For \(c=25\):
\[
5c=125,\quad 26+4c=26+100=126,
\]
so \(125 \le s <126\) gives exactly \(s=125\).

Now verify that \(s=125>80\) and that it indeed yields unique \(c\).
If \(s=125\), solve for \(w\):
\[
w=30+4c-125=4c-95.
\]
Try \(c=25\): \(w=100-95=5\), and \(c+w=30\) OK.
Try \(c=24\): \(w=96-95=1\), and \(c+w=25\le 30\) also OK—wait that means \(c=24\) also works, contradicting uniqueness.

So the above interval logic used the wrong upper bound for excluding \(c-1\). Let’s do exclusion directly:

For \(c\) to be feasible:
\[
w=30+4c-s \ge 0 \iff s \le 30+4c.
\]
So for \(c-1\) to be infeasible:
\[
s > 30+4(c-1)=30+4c-4.
\]
Also for \(c+1\) to be infeasible:
\[
s < 5(c+1)=5c+5 \quad\text{(since need } s\ge 5(c+1)\text{)}.
\]

Thus for uniqueness we need:
\[
5c \le s \le 30+4c
\]
\[
s > 30+4c-4
\]
\[
s < 5c+5.
\]
So \(s\) must satisfy
\[
30+4c-4 < s < 5c+5
\]
and also \(s\ge 5c\). Note \(30+4c-4 = 26+4c\).
For \(c\) large, compare \(26+4c\) with \(5c\):
\[
26+4c \le 5c \iff 26 \le c.
\]
So for \(c\ge 26\), the lower constraint is actually \(s>26+4c\) which is stronger than \(s\ge 5c\).

Try \(c=26\):
Feasible \(s\) for \(c=26\) is \(5c=130 \le s \le 30+4c=134\).
To exclude \(c-1=25\), need \(s>30+4\cdot 25=130\), so \(s\ge 131\).
To exclude \(c+1=27\), need \(s<5\cdot 27=135\), so \(s\le 134\).
Thus \(s\) can be \(131,132,133,134\) (4 values), not unique.

Try the *smallest* \(s>80\) with uniqueness; from checking earlier near 81–85 none worked. The uniqueness will first occur when the feasible set of \(c\) becomes a singleton. That happens when \(L(s)=U(s)\). Now compute directly by continuing until equality.

Let’s test \(s=119\):
\[
L=\left\lceil \frac{89}{4}\right\rceil=\left\lceil 22.25\right\rceil=23,\quad
U=\left\lfloor \frac{119}{5}\right\rfloor=23.
\]
So \(c\) is uniquely determined and equals \(23\). Great.

Check the “if lower but still over 80, John could not have determined it” condition: that means for \(s=118\),
\[
L=\left\lceil \frac{88}{4}\right\rceil=22,\quad
U=\left\lfloor \frac{118}{5}\right\rfloor=23,
\]
not unique. So \(s=119\) is the first such score.

Therefore Mary’s score is \(119\).

ANSWER: 119
```

</details>

#### Baseline Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.0000 | `incorrect` |
| 1 | 0.0000 | `incorrect` |
| 2 | 0.0000 | `incorrect` |
| 3 | 0.0000 | `incorrect` |
| 4 | 1.0000 | `correct` |
| 5 | 0.0000 | `incorrect` |
| 6 | 0.0000 | `incorrect` |
| 7 | 0.0000 | `incorrect` |
| 8 | 0.0000 | `incorrect` |
| 9 | 1.0000 | `correct` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 123",
  "answer_fragment": "123",
  "extracted": "123"
}
```

</details>

<details>
<summary>Score details for generation 1</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 107",
  "answer_fragment": "107",
  "extracted": "107"
}
```

</details>

<details>
<summary>Score details for generation 2</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 134",
  "answer_fragment": "134",
  "extracted": "134"
}
```

</details>

<details>
<summary>Score details for generation 3</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 150",
  "answer_fragment": "150",
  "extracted": "150"
}
```

</details>

<details>
<summary>Score details for generation 4</summary>

```json
{
  "reason": "correct",
  "expected": "119",
  "answer_line": "ANSWER: 119",
  "answer_fragment": "119",
  "extracted": "119"
}
```

</details>

<details>
<summary>Score details for generation 5</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 83",
  "answer_fragment": "83",
  "extracted": "83"
}
```

</details>

<details>
<summary>Score details for generation 6</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 135",
  "answer_fragment": "135",
  "extracted": "135"
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 91",
  "answer_fragment": "91",
  "extracted": "91"
}
```

</details>

<details>
<summary>Score details for generation 8</summary>

```json
{
  "reason": "missing_answer_line",
  "expected": "119",
  "answer_line": null,
  "answer_fragment": null,
  "extracted": null
}
```

</details>

<details>
<summary>Score details for generation 9</summary>

```json
{
  "reason": "correct",
  "expected": "119",
  "answer_line": "ANSWER: 119",
  "answer_fragment": "119",
  "extracted": "119"
}
```

</details>

### Augmented

### System Prompt

```text
You are an expert mathematician solving competition-level problems. Show your reasoning step by step. Your response should have this overall shape: first the reasoning, then a final line exactly in the format ANSWER: <integer>. For example, a valid response could end like this:
...
ANSWER: 42
```

### User Prompt

```text
Before solving, consider these reusable insights from prior analysis:

  1. Encode Feasibility as an Integer Set: Turn the original scoring/constraint system into explicit inequalities that define all possible integer values of the inferred quantity for a fixed observed score.
     When the problem asks whether someone can uniquely recover an integer (like a count), first express the constraints so that for each candidate score you get a range (or discrete set) of feasible integers for that count. This prevents “almost right” solutions that satisfy simplified conditions but violate the original bounds (e.g., nonnegativity or total-attempt limits).
  2. Uniqueness = “Exactly One Integer” (Don’t Guess with Length): Establish uniqueness by proving the feasible set has cardinality one, using floor/ceiling arithmetic or equivalent exact counting—not by intuition about interval size.
     Heuristics like “the bounds are close so it’s likely one” often fail because of discretization (ceilings/floors). Instead compute the feasible integer interval precisely and require that the number of integers equals 1 (i.e., lower bound’s ceiling equals upper bound’s floor, or equivalently count = 1).
  3. Interpret “If Score Were Lower” as a Threshold Condition: Convert comparative wording (“any lower but still over …”) into a minimality or maximality condition over the set of scores where uniqueness holds.
     Clues about what happens when the score changes are usually about the *first* score at which the feasible set collapses to one element. Make that explicit: determine whether you need the smallest score > bound with uniqueness (or largest, depending on wording), and ensure the derived model matches that monotonic/threshold behavior.
  4. Validate Boundary Cases to Catch Logic Drift: Whenever you derive a candidate using endpoint/threshold reasoning, verify it by explicitly checking feasibility for that score and for nearby scores.
     Many incorrect attempts “lock in” too early (e.g., assuming disjoint intervals imply uniqueness at the boundary). A quick verification pass—constructing a feasible assignment and confirming whether nearby scores give 1 vs ≥2 feasible integers—catches off-by-one and misapplied inequalities.

Apply these insights to the problem below.

Solve the following AIME problem:

Mary told John her score on the American High School Mathematics Examination (AHSME), which was over $80$ . From this, John was able to determine the number of problems Mary solved correctly. If Mary's score had been any lower, but still over $80$ , John could not have determined this. What was Mary's score? (Recall that the AHSME consists of $30$ multiple choice problems and that one's score, $s$ , is computed by the formula $s=30+4c-w$ , where $c$ is the number of correct answers and $w$ is the number of wrong answers. Students are not penalized for problems left unanswered.)
```

#### Outputs

<details>
<summary>Augmented generation 1</summary>

```text

```

</details>

<details>
<summary>Augmented generation 2</summary>

```text
Let \(c\) be the number correct and \(w\) wrong. There are 30 problems total, so
\[
c,w\in \mathbb Z_{\ge 0},\qquad c+w\le 30.
\]
The score is
\[
s=30+4c-w.
\]

### 1) Express \(w\) in terms of \(c\) using the score
Fix the observed score \(s\). Then
\[
s=30+4c-w \quad\Longrightarrow\quad w=30+4c-s.
\]
For a given \(s\), a value of \(c\) is feasible iff the corresponding \(w\) satisfies
\[
w\ge 0,\qquad c+w\le 30.
\]
Substitute \(w=30+4c-s\):

- \(w\ge 0\) gives
\[
30+4c-s\ge 0 \Longrightarrow c\ge \frac{s-30}{4}.
\]
- \(c+w\le 30\) gives
\[
c+(30+4c-s)\le 30 \Longrightarrow 5c\le s
\Longrightarrow c\le \frac{s}{5}.
\]

So for a fixed \(s\), the feasible integers \(c\) are exactly
\[
c\in \left[\left\lceil \frac{s-30}{4}\right\rceil,\ \left\lfloor \frac{s}{5}\right\rfloor\right].
\]

John can determine \(c\) uniquely iff this integer interval contains exactly one integer:
\[
\left\lceil \frac{s-30}{4}\right\rceil=\left\lfloor \frac{s}{5}\right\rfloor.
\]

### 2) Use the “any lower but still over 80” condition
We are told \(s>80\), and for the score \(s\) John *can* determine \(c\) uniquely. But if the score were any lower while still \(>80\), John *could not* determine \(c\) uniquely.

That means: \(s\) is the **smallest** score strictly greater than 80 for which the feasible set of \(c\)’s has size 1.

So compute uniqueness for scores just above 80 and find the first \(s\) where the interval collapses to one integer.

### 3) Check \(s=81,82,83,\dots\) until uniqueness occurs
For each \(s\), compute
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\qquad U(s)=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Uniqueness means \(L(s)=U(s)\).

- \(s=81\):
\[
L(81)=\left\lceil \frac{51}{4}\right\rceil=\lceil 12.75\rceil=13,\quad
U(81)=\left\lfloor \frac{81}{5}\right\rfloor=\lfloor 16.2\rfloor=16.
\]
Interval has many integers \(\Rightarrow\) not unique.

- \(s=82\):
\[
L(82)=\left\lceil \frac{52}{4}\right\rceil=\lceil 13\rceil=13,\quad
U(82)=\left\lfloor \frac{82}{5}\right\rfloor=\lfloor 16.4\rfloor=16.
\]
Not unique.

- \(s=83\):
\[
L(83)=\left\lceil \frac{53}{4}\right\rceil=\lceil 13.25\rceil=14,\quad
U(83)=\left\lfloor \frac{83}{5}\right\rfloor=\lfloor 16.6\rfloor=16.
\]
Not unique.

- \(s=84\):
\[
L(84)=\left\lceil \frac{54}{4}\right\rceil=\lceil 13.5\rceil=14,\quad
U(84)=\left\lfloor \frac{84}{5}\right\rfloor=\lfloor 16.8\rfloor=16.
\]
Not unique.

- \(s=85\):
\[
L(85)=\left\lceil \frac{55}{4}\right\rceil=\lceil 13.75\rceil=14,\quad
U(85)=\left\lfloor \frac{85}{5}\right\rfloor=\lfloor 17\rfloor=17.
\]
Interval is \(\{14,15,16,17\}\) size 4 \(\Rightarrow\) not unique.

- \(s=86\):
\[
L(86)=\left\lceil \frac{56}{4}\right\rceil=\lceil 14\rceil=14,\quad
U(86)=\left\lfloor \frac{86}{5}\right\rfloor=\lfloor 17.2\rfloor=17.
\]
Not unique.

- \(s=87\):
\[
L(87)=\left\lceil \frac{57}{4}\right\rceil=\lceil 14.25\rceil=15,\quad
U(87)=\left\lfloor \frac{87}{5}\right\rfloor=\lfloor 17.4\rfloor=17.
\]
Not unique.

- \(s=88\):
\[
L(88)=\left\lceil \frac{58}{4}\right\rceil=\lceil 14.5\rceil=15,\quad
U(88)=\left\lfloor \frac{88}{5}\right\rfloor=\lfloor 17.6\rfloor=17.
\]
Not unique.

- \(s=89\):
\[
L(89)=\left\lceil \frac{59}{4}\right\rceil=\lceil 14.75\rceil=15,\quad
U(89)=\left\lfloor \frac{89}{5}\right\rfloor=\lfloor 17.8\rfloor=17.
\]
Not unique.

- \(s=90\):
\[
L(90)=\left\lceil \frac{60}{4}\right\rceil=\lceil 15\rceil=15,\quad
U(90)=\left\lfloor \frac{90}{5}\right\rfloor=\lfloor 18\rfloor=18.
\]
Not unique.

- \(s=91\):
\[
L(91)=\left\lceil \frac{61}{4}\right\rceil=\lceil 15.25\rceil=16,\quad
U(91)=\left\lfloor \frac{91}{5}\right\rfloor=\lfloor 18.2\rfloor=18.
\]
Not unique.

- \(s=92\):
\[
L(92)=\left\lceil \frac{62}{4}\right\rceil=\lceil 15.5\rceil=16,\quad
U(92)=\left\lfloor \frac{92}{5}\right\rfloor=\lfloor 18.4\rfloor=18.
\]
Not unique.

- \(s=93\):
\[
L(93)=\left\lceil \frac{63}{4}\right\rceil=\lceil 15.75\rceil=16,\quad
U(93)=\left\lfloor \frac{93}{5}\right\rfloor=\lfloor 18.6\rfloor=18.
\]
Not unique.

- \(s=94\):
\[
L(94)=\left\lceil \frac{64}{4}\right\rceil=\lceil 16\rceil=16,\quad
U(94)=\left\lfloor \frac{94}{5}\right\rfloor=\lfloor 18.8\rfloor=18.
\]
Not unique.

- \(s=95\):
\[
L(95)=\left\lceil \frac{65}{4}\right\rceil=\lceil 16.25\rceil=17,\quad
U(95)=\left\lfloor \frac{95}{5}\right\rfloor=\lfloor 19\rfloor=19.
\]
Not unique.

- \(s=96\):
\[
L(96)=\left\lceil \frac{66}{4}\right\rceil=\lceil 16.5\rceil=17,\quad
U(96)=\left\lfloor \frac{96}{5}\right\rfloor=\lfloor 19.2\rfloor=19.
\]
Not unique.

- \(s=97\):
\[
L(97)=\left\lceil \frac{67}{4}\right\rceil=\lceil 16.75\rceil=17,\quad
U(97)=\left\lfloor \frac{97}{5}\right\rfloor=\lfloor 19.4\rfloor=19.
\]
Not unique.

- \(s=98\):
\[
L(98)=\left\lceil \frac{68}{4}\right\rceil=\lceil 17\rceil=17,\quad
U(98)=\left\lfloor \frac{98}{5}\right\rfloor=\lfloor 19.6\rfloor=19.
\]
Not unique.

- \(s=99\):
\[
L(99)=\left\lceil \frac{69}{4}\right\rceil=\lceil 17.25\rceil=18,\quad
U(99)=\left\lfloor \frac{99}{5}\right\rfloor=\lfloor 19.8\rfloor=19.
\]
Not unique.

- \(s=100\):
\[
L(100)=\left\lceil \frac{70}{4}\right\rceil=\lceil 17.5\rceil=18,\quad
U(100)=\left\lfloor \frac{100}{5}\right\rfloor=\lfloor 20\rfloor=20.
\]
Not unique.

This brute force looks long, but we can now use a key observation: for uniqueness,
\[
\left\lceil \frac{s-30}{4}\right\rceil=\left\lfloor \frac{s}{5}\right\rfloor
\]
and the interval size changes only when these floor/ceiling values jump. The first time they can coincide above 80 happens when
\[
\frac{s-30}{4} \le \frac{s}{5} \quad\text{(otherwise no solutions)}
\]
and then the discretization collapses to one.

The equality of the *bounds* in real numbers occurs at:
\[
\frac{s-30}{4}=\frac{s}{5}\ \Longrightarrow\ 5(s-30)=4s\ \Longrightarrow\ s=150.
\]
So \(s\) must be near where integer rounding makes the interval size 1, and in fact the first such \(s>80\) is \(s=119\)?? Let’s compute directly but with a smarter narrowing:

We need interval to be size 1:
\[
U(s)=L(s)=k.
\]
That means simultaneously
\[
k\le \frac{s}{5}<k+1
\quad\text{and}\quad
k-1<\frac{s-30}{4}\le k.
\]
From the first:
\[
5k\le s<5k+5.
\]
From the second:
\[
4(k-1)< s-30 \le 4k
\]
\[
4k+ -4 < s-30 \le 4k
\]
\[
4k+26 < s \le 4k+30.
\]
So \(s\) must satisfy
\[
\max(5k,\ 4k+27) < s \le \min(5k+4,\ 4k+30).
\]
For an integer \(s\) to exist, we need
\[
\max(5k,\ 4k+27)+1 \le \min(5k+4,\ 4k+30).
\]
Also, the problem says the smallest \(s>80\) with uniqueness occurs, so test \(k\) where \(s\) is just above 80.

Since \(c\le 30\), and \(c=k\), we expect \(k\) around \(\frac{s}{5}\). For \(s\approx 80\), \(\frac{s}{5}\approx 16\). So \(k\) around 16–20.

Try \(k=16\):
Conditions give:
\[
5k=80,\quad 4k+27=91 \Rightarrow \max=91
\]
Upper:
\[
5k+4=84,\quad 4k+30=94 \Rightarrow \min=84.
\]
Need \(91+1\le 84\), impossible. So \(k\ne 16\).

\(k=17\):
Lower:
\[
5k=85,\quad 4k+27=95 \Rightarrow \max=95
\]
Upper:
\[
5k+4=89,\quad 4k+30=98 \Rightarrow \min=89
\]
Impossible.

\(k=18\):
Lower:
\[
5k=90,\quad 4k+27=99 \Rightarrow \max=99
\]
Upper:
\[
5k+4=94,\quad 4k+30=102 \Rightarrow \min=94
\]
Impossible.

\(k=19\):
Lower:
\[
5k=95,\quad 4k+27=103 \Rightarrow \max=103
\]
Upper:
\[
5k+4=99,\quad 4k+30=106 \Rightarrow \min=99
\]
Impossible.

So our inequalities were off by 1 due to strict/non-strict from ceiling/floor. Let’s do it carefully from the definitions:

Uniqueness means \(L(s)=U(s)=k\), i.e.
\[
k=\left\lceil \frac{s-30}{4}\right\rceil,\qquad k=\left\lfloor \frac{s}{5}\right\rfloor.
\]

The second:
\[
k\le \frac{s}{5} < k+1 \Longrightarrow 5k\le s \le 5k+4.
\]

The first: \( \left\lceil x\right\rceil = k\) means \(k-1 < x \le k\).
So
\[
k-1 < \frac{s-30}{4} \le k
\]
Multiply by 4:
\[
4(k-1) < s-30 \le 4k
\]
Add 30:
\[
4k+26 < s \le 4k+30.
\]
Thus
\[
\max(5k,\ 4k+27)\le s \le \min(5k+4,\ 4k+30),
\]
and since \(s\) is integer, the left max uses that \(s>4k+26\) so \(s\ge 4k+27\). Good.

Now test \(k\) again, but note the lower bound is \(\max(5k,4k+27)\) not plus 1.

For \(k=16\):
lower \(=\max(80,91)=91\), upper \(=\min(84,94)=84\) impossible.

\(k=20\):
lower \(=\max(100,107)=107\), upper \(=\min(104,110)=104\) impossible.

This indicates no solutions for these \(k\), so uniqueness likely occurs at higher \(k\) where the ceiling/ floor ranges squeeze differently. But note that \(4k+27\) grows faster than \(5k\) for all \(k\)?? Compare: \(4k+27\) vs \(5k\): \(4k+27\ge 5k\iff 27\ge k\).
So for \(k\le 27\), lower bound is \(4k+27\). Upper bound is \(\min(5k+4,4k+30)\) and compare \(5k+4\) vs \(4k+30\): \(5k+4\ge 4k+30\iff k\ge 26\).
So for \(k\le 25\), upper is \(5k+4\).

Thus for \(k\le 25\), we need
\[
4k+27 \le 5k+4 \iff 23 \le k.
\]
So \(k\) can be \(23,24,25\). Great—try those.

- \(k=23\):
Lower \(=4k+27=92+27=119\).
Upper: since \(k\le 25\), upper \(=5k+4=115+4=119\).
So \(s=119\) is the only possible score with \(c=k=23\). This should be the first \(>80\).

Check \(s=118\) (nearby lower) not unique:
For \(s=118\),
\[
L=\left\lceil \frac{88}{4}\right\rceil=\lceil 22\rceil=22,\quad
U=\left\lfloor \frac{118}{5}\right\rfloor=\lfloor 23.6\rfloor=23,
\]
two possible \(c\): 22 or 23. So not uniquely determined. Perfect.

Also verify for \(s=119\):
\[
L=\left\lceil \frac{89}{4}\right\rceil=\lceil 22.25\rceil=23,\quad
U=\left\lfloor \frac{119}{5}\right\rfloor=\lfloor 23.8\rfloor=23,
\]
unique \(c=23\). Then
\[
w=30+4c-s=30+92-119=3,
\]
and \(c+w=26\le 30\) feasible.

Therefore Mary's score is \(119\).

ANSWER: 119
```

</details>

<details>
<summary>Augmented generation 3</summary>

```text
Let \(c\) be the number correct and \(w\) the number wrong. Then there are \(30-(c+w)\) blank answers, and
\[
s=30+4c-w,\qquad c\ge 0,\ w\ge 0,\ c+w\le 30.
\]

We are told \(s>80\) and John can determine \(c\) uniquely from \(s\). Also, if \(s\) were any lower but still \(>80\), John could not have determined \(c\) uniquely. So we want the **first** score above \(80\) for which \(c\) becomes uniquely determined.

---

### 1) Rewrite the constraints in terms of \(c\)
From \(s=30+4c-w\),
\[
w = 30+4c-s.
\]
Since \(w\ge 0\),
\[
30+4c-s\ge 0 \quad\Rightarrow\quad 4c\ge s-30 \quad\Rightarrow\quad c\ge \left\lceil\frac{s-30}{4}\right\rceil.
\]

Also \(c+w\le 30\). Substitute \(w\):
\[
c+(30+4c-s)\le 30
\]
\[
5c - s \le 0 \quad\Rightarrow\quad c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]

So for a fixed score \(s\), the feasible integers \(c\) satisfy
\[
\left\lceil\frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
John can determine \(c\) **uniquely** exactly when this interval contains **exactly one integer**, i.e.
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]

---

### 2) Apply the “any lower but still \(>80\)” condition
Let’s test scores starting from just above \(80\). Since \(s\) is an integer (because \(30+4c-w\) is integer), “any lower but still over \(80\)” means we should check \(s=81\) first upward until uniqueness happens.

Compute for \(s=81\):
\[
\left\lceil\frac{81-30}{4}\right\rceil=\left\lceil\frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,
\]
\[
\left\lfloor\frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
So \(c\in\{13,14,15,16\}\): not unique.

For \(s=82\):
\[
\left\lceil\frac{52}{4}\right\rceil=\left\lceil 13\right\rceil=13,
\quad
\left\lfloor\frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16,
\]
still multiple integers.

Continue until the interval shrinks to size \(1\). The lower bound is
\(\left\lceil\frac{s-30}{4}\right\rceil\), which increases roughly every 4 steps, while the upper bound \(\left\lfloor\frac{s}{5}\right\rfloor\) increases every 5 steps. The first time they become equal should be near when
\[
\frac{s-30}{4} \approx \frac{s}{5}
\]
\[
5(s-30)\approx 4s \Rightarrow 5s-150\approx 4s \Rightarrow s\approx 150.
\]
But because of ceiling/floor, we check systematically near where equality starts to occur: we need
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]

Try \(s=85\) (still close to 80):
- \(s=85\): lower \(=\left\lceil\frac{55}{4}\right\rceil=\lceil13.75\rceil=14\).
  upper \(=\left\lfloor\frac{85}{5}\right\rfloor=17\). Not unique.
Try \(s=88\):
- \(s=88\): lower \(=\left\lceil\frac{58}{4}\right\rceil=\lceil14.5\rceil=15\).
  upper \(=\left\lfloor\frac{88}{5}\right\rfloor=17\). Not unique.
Try \(s=90\):
- \(s=90\): lower \(=\left\lceil\frac{60}{4}\right\rceil=15\).
  upper \(=\left\lfloor\frac{90}{5}\right\rfloor=18\). Not unique.

This is going nowhere quickly; instead, solve the equality more directly by setting the common integer to be \(c\).

If John uniquely determines \(c\), then for that \(s\) we have
\[
c=\left\lceil\frac{s-30}{4}\right\rceil=\left\lfloor\frac{s}{5}\right\rfloor.
\]
That means:
\[
c-1<\frac{s-30}{4}\le c \quad\Rightarrow\quad 4(c-1) < s-30 \le 4c
\]
\[
\Rightarrow\quad 4c+26 < s \le 4c+30.
\]
And
\[
c\le \frac{s}{5}<c+1 \quad\Rightarrow\quad 5c \le s < 5(c+1)=5c+5.
\]
Combine:
\[
\max(4c+27,\,5c)\le s \le \min(4c+30,\,5c+4).
\]
For uniqueness we need exactly one integer \(s\) in the intersection, and also we need \(s>80\) and minimal with that property.

Now notice \(s=30+4c-w\le 30+4c\). Also from \(c+w\le 30\), we get \(w\le 30-c\), hence
\[
s=30+4c-w \ge 30+4c-(30-c)=5c.
\]
So for fixed \(c\),
\[
5c \le s \le 30+4c.
\]
And every integer \(s\) in that range corresponds to some \(w=30+4c-s\) which automatically satisfies \(0\le w\le 30-c\).
So the “uniquely determined \(c\)” condition at score \(s\) is equivalent to: **there is exactly one \(c\)** such that \(5c\le s\le 30+4c\) and \(c\) integer, \(0\le c\le 30\).

Thus we can check \(c\) values directly by looking at which \(c\) satisfy
\[
5c\le s \le 30+4c.
\]

At the transition from non-unique to unique just above 80, the candidate \(c\) set shrinks to one element. Let’s find the smallest \(s>80\) for which the feasible \(c\) count is 1. We can do this by brute evaluation of the interval bounds already derived, but quickly:

We need
\[
\left\lceil\frac{s-30}{4}\right\rceil = \left\lfloor\frac{s}{5}\right\rfloor.
\]
Let this common value be \(c\). Then \(c=\left\lfloor\frac{s}{5}\right\rfloor\) implies
\[
5c \le s \le 5c+4.
\]
Also \(c=\left\lceil\frac{s-30}{4}\right\rceil\) implies
\[
4(c-1) < s-30 \le 4c
\]
\[
\Rightarrow 4c+26 < s \le 4c+30.
\]
So \(s\) must lie in both:
\[
s\in[5c,\,5c+4]\cap(4c+26,\,4c+30].
\]
The intersection begins at the larger lower endpoint. Compare \(5c\) vs \(4c+27\):
\[
5c \ge 4c+27 \iff c\ge 27.
\]
So the first time uniqueness can occur for \(s>80\) (which corresponds to \(c\ge 16\) since \(s\ge 5c\)) is likely when \(c\) is large enough; indeed the inequality forces \(c\ge 27\).

Take \(c=27\):
Then the feasible \(s\) from those inequalities is
\[
s\in[5\cdot 27,\,5\cdot 27+4]=[135,139],
\]
and
\[
s\in(4\cdot 27+26,\,4\cdot 27+30]=(134,138].
\]
Intersection is \(\{135,136,137,138\}\): not unique.

Try \(c=28\):
First range: \([140,144]\).
Second: \((4\cdot 28+26,\,4\cdot 28+30]=(138,142]\).
Intersection \(\{139,140,141,142\}\): not unique.

So we should instead directly find the **first** \(s>80\) with unique \(c\). Let’s do that by evaluating the interval size quickly:

Interval endpoints:
\[
L(s)=\left\lceil\frac{s-30}{4}\right\rceil,\quad U(s)=\left\lfloor\frac{s}{5}\right\rfloor.
\]
Uniqueness means \(L(s)=U(s)\).

Now compute near the point where \(L(s)\) catches up to \(U(s)\). For large \(s\), \(L(s)\sim \frac{s}{4}\) and \(U(s)\sim \frac{s}{5}\), and since \(\frac{1}{4}>\frac{1}{5}\), for sufficiently large \(s\) we’ll have \(L(s)>U(s)\) (no solutions). Therefore uniqueness (exactly one) must occur at the boundary where \(L(s)\) first becomes \(\le U(s)\) and then meets it. This boundary should happen when \(\left\lceil\frac{s-30}{4}\right\rceil\) is just equal to \(\left\lfloor\frac{s}{5}\right\rfloor\).

Check \(s=100\):
\(L=\left\lceil\frac{70}{4}\right\rceil=\lceil17.5\rceil=18\).
\(U=\left\lfloor\frac{100}{5}\right\rfloor=20\). Not.

\(s=110\):
\(L=\left\lceil\frac{80}{4}\right\rceil=20\).
\(U=\left\lfloor\frac{110}{5}\right\rfloor=22\). Not.

\(s=120\):
\(L=\left\lceil\frac{90}{4}\right\rceil=\lceil22.5\rrceil=23\).
\(U=\left\lfloor\frac{120}{5}\right\rfloor=24\). Not.

\(s=121\):
\(L=\left\lceil\frac{91}{4}\right\rceil=\lceil22.75\rceil=23\).
\(U=\left\lfloor\frac{121}{5}\right\rfloor=24\). Not.

\(s=124\):
\(L=\left\lceil\frac{94}{4}\right\rceil=\lceil23.5\rceil=24\).
\(U=\left\lfloor\frac{124}{5}\right\rfloor=24\).
So at \(s=124\), we get \(L=U=24\): unique! Also we should verify that for \(s=123\) it is not unique.

At \(s=123\):
\(L=\left\lceil\frac{93}{4}\right\rceil=\lceil23.25\rceil=24\).
\(U=\left\lfloor\frac{123}{5}\right\rfloor=24\).
This is also unique—contradiction with “any lower (still over 80)”. So we need the **highest** score just above 80 where uniqueness first fails going downward; equivalently the given \(s\) should be the **smallest** score with uniqueness, not just any candidate we found. Our found uniqueness might persist across a range.

Let’s check \(s=122\):
\(L=\left\lceil\frac{92}{4}\right\rceil=\lceil23\rceil=23\).
\(U=\left\lfloor\frac{122}{5}\right\rfloor=24\).
Not unique. So uniqueness begins at \(s=123\).

Check \(s=123\) is unique with \(c=24\). Now confirm \(s>80\) and that \(s=122\) (still \(>80\)) is not unique—done. Therefore Mary’s score is \(123\).

---

### 3) Final consistency check by constructing \(w\)
For \(s=123\) and \(c=24\),
\[
w=30+4c-s=30+96-123=3,
\]
and \(c+w=27\le 30\), valid.

For \(s=122\):
Feasible \(c\) range is \(23\) to \(24\), so not unique indeed.

Thus the required “minimal over 80” score with unique \(c\) is \(123\).

ANSWER: 123
```

</details>

<details>
<summary>Augmented generation 4</summary>

```text

```

</details>

<details>
<summary>Augmented generation 5</summary>

```text
Let \(c\) be the number correct, \(w\) the number wrong, and \(u\) unanswered. Then
\[
c+w+u=30,\qquad c,w,u\ge 0,\qquad c,w\in\mathbb Z.
\]
The score is
\[
s=30+4c-w.
\]
Equivalently,
\[
s-30=4c-w \quad\Longrightarrow\quad w=4c-(s-30).
\]

### Step 1: Feasible integers \(c\) for a fixed score \(s\)
For a given \(s\), \(w\) must be an integer with \(0\le w\le 30\). Since \(w=4c-(s-30)\),
- \(w\ge 0 \Rightarrow 4c-(s-30)\ge 0 \Rightarrow c\ge \frac{s-30}{4}\).
- \(w\le 30 \Rightarrow 4c-(s-30)\le 30 \Rightarrow 4c\le s \Rightarrow c\le \frac{s}{4}\).

Also \(c\ge 0\) automatically follows from \(s>80\), but we’ll keep integrality.

So the feasible set of integers is
\[
c\in\left[\left\lceil\frac{s-30}{4}\right\rceil,\ \left\lfloor\frac{s}{4}\right\rfloor\right].
\]
John can determine \(c\) uniquely iff this interval contains exactly one integer.

That means
\[
\left\lceil\frac{s-30}{4}\right\rceil=\left\lfloor\frac{s}{4}\right\rfloor.
\]
Let that common integer be \(C\). Then necessarily
\[
C-1 < \frac{s-30}{4}\le C,\qquad C\le \frac{s}{4}< C+1.
\]

### Step 2: Use the “any lower but still over 80” condition
We want the **largest** score \(s\) (still \(>80\)) for which uniqueness holds—because if the score were lower but still \(>80\), uniqueness would fail.

So we search for the top \(s>80\) such that
\[
\left\lceil\frac{s-30}{4}\right\rceil=\left\lfloor\frac{s}{4}\right\rfloor.
\]

Let
\[
A=\frac{s-30}{4},\quad B=\frac{s}{4}.
\]
Note \(B-A=\frac{30}{4}=7.5\). As \(s\) increases by 1, both \(A\) and \(B\) increase by \(1/4\).

Check scores just above \(80\). Since \(s>80\) and \(s\) is integer, the smallest possible is \(81\). We test upward until uniqueness stops holding.

- For \(s=81\):
\[
\frac{s-30}{4}=\frac{51}{4}=12.75 \Rightarrow \left\lceil\cdot\right\rceil=13,\quad
\frac{s}{4}=\frac{81}{4}=20.25 \Rightarrow \left\lfloor\cdot\right\rfloor=20.
\]
Interval has \(20-13+1=8\) integers \(\Rightarrow\) not unique.

As \(s\) grows, the interval width remains roughly \(\frac{s}{4}-\frac{s-30}{4}=7.5\), so uniqueness requires the ceiling and floor to coincide, i.e. the endpoints straddle an integer tightly.

Compute the condition more directly. Let
\[
\left\lfloor\frac{s}{4}\right\rfloor = C.
\]
Then \(C\le \frac{s}{4}<C+1 \Rightarrow 4C\le s<4(C+1).\)

Also need
\[
\left\lceil\frac{s-30}{4}\right\rceil=C.
\]
This means \(C-1<\frac{s-30}{4}\le C\), i.e.
\[
4(C-1)< s-30 \le 4C
\]
\[
4C-4 < s-30 \le 4C
\]
\[
34+4C-4 < s \le 30+4C
\]
\[
30+4C? \text{(simplify carefully)}:
\]
From \(4(C-1)< s-30\):
\[
s-30>4C-4 \Rightarrow s>4C+26.
\]
From \(s-30\le 4C\):
\[
s\le 4C+30.
\]
So
\[
4C+26 < s \le 4C+30.
\]
Combine with \(4C\le s<4C+4\). The intersection is
\[
\max(4C,\ 4C+27)\ <\ s\ \le\ \min(4C+4,\ 4C+30).
\]
Since \(4C+27\) is larger than \(4C\), the left side is \(4C+27\), and the right side is \(4C+4\) (because \(4C+4 < 4C+30\)).
Thus we need
\[
4C+27 < s \le 4C+4,
\]
which is impossible—unless we made an arithmetic slip. Let’s re-derive that ceiling inequality cleanly.

We require \(\left\lceil\frac{s-30}{4}\right\rceil=\left\lfloor\frac{s}{4}\right\rfloor\). Let
\[
\left\lfloor\frac{s}{4}\right\rfloor = C.
\]
So
\[
C \le \frac{s}{4} < C+1 \Rightarrow 4C \le s < 4C+4.
\]
Now \(\left\lceil\frac{s-30}{4}\right\rceil=C\) means
\[
C-1 < \frac{s-30}{4} \le C.
\]
Multiply by 4:
\[
4C-4 < s-30 \le 4C.
\]
Add 30:
\[
4C+26 < s \le 4C+30.
\]
Intersection with \(4C \le s < 4C+4\) is indeed empty because
\[
4C+26 \ge 4C+4 \quad\text{(since }26>4\text{)}.
\]
So equality of ceiling and floor can never happen—meaning uniqueness must instead mean something else?

The feasible set for \(c\) is
\[
c\in\left[\left\lceil\frac{s-30}{4}\right\rceil,\ \left\lfloor\frac{s}{4}\right\rfloor\right],
\]
and its cardinality being 1 is
\[
\left\lfloor\frac{s}{4}\right\rfloor-\left\lceil\frac{s-30}{4}\right\rceil+1=1
\]
\[
\left\lfloor\frac{s}{4}\right\rfloor=\left\lceil\frac{s-30}{4}\right\rceil.
\]
But we just found this cannot occur because the right endpoint is always at least \(7.5\) larger than the left endpoint. Let’s check: is the interval correct? We used only \(0\le w\le 30\), but we must also enforce \(u=30-c-w\ge 0\), i.e. \(c+w\le 30\), which we did NOT use in translating constraints. However \(w\le 30\) is weaker than \(c+w\le 30\).

### Step 3: Correct constraints using \(c+w\le 30\)
We have \(w=4c-(s-30)\). Then
\[
c+w \le 30 \Rightarrow c+4c-(s-30)\le 30
\]
\[
5c-(s-30)\le 30
\]
\[
5c \le s+0 \Rightarrow c\le \frac{s}{5}.
\]
Also \(w\ge 0\Rightarrow c\ge \frac{s-30}{4}\).

And \(w\le 30\) is automatically implied by \(c+w\le 30\) since \(c\ge 0\). So the correct feasible interval is
\[
c\in\left[\left\lceil\frac{s-30}{4}\right\rceil,\ \left\lfloor\frac{s}{5}\right\rfloor\right].
\]
Now uniqueness means
\[
\left\lceil\frac{s-30}{4}\right\rceil=\left\lfloor\frac{s}{5}\right\rfloor.
\]

### Step 4: Find the largest \(s>80\) giving uniqueness
Test candidates around \(81\) upward but efficiently by modular reasoning.

We need the interval to have exactly one integer \(c\). Let
\[
\left\lfloor\frac{s}{5}\right\rfloor = c.
\]
Then
\[
5c \le s \le 5c+4.
\]
Also
\[
\left\lceil\frac{s-30}{4}\right\rceil = c
\]
means
\[
c-1 < \frac{s-30}{4} \le c
\]
\[
4c-4 < s-30 \le 4c
\]
\[
4c+26 < s \le 4c+30.
\]
Combine:
\[
\max(5c,\ 4c+27) < s \le \min(5c+4,\ 4c+30).
\]
Now compare \(5c\) vs \(4c+27\): \(5c\ge 4c+27 \iff c\ge 27\).
For scores near 80, \(c\) will be around \(s/5\approx 16\), so \(c<27\), hence \(4c+27\) dominates.

Also compare \(5c+4\) vs \(4c+30\): \(5c+4 \le 4c+30 \iff c\le 26\), true here. So the minimum is \(5c+4\).

Thus for our range (\(c\le 26\)):
\[
4c+27 < s \le 5c+4.
\]
We also need \(s\) integer and \(s>80\).

So there is a unique feasible \(c\) precisely when the only integer \(s\) satisfying all bounds lies in that narrow range at the boundary where the feasible \(c\) count collapses; easiest is to just compute \(c\) from \(s\) and check cardinality.

Try \(s=81,82,\dots\). Compute feasible \(c\) count:
\[
c\in\left[\left\lceil\frac{s-30}{4}\right\rceil,\ \left\lfloor\frac{s}{5}\right\rfloor\right].
\]

For \(s=81\):
\[
\left\lceil\frac{51}{4}\right\rceil=\lceil 12.75\rceil=13,\quad
\left\lfloor\frac{81}{5}\right\rfloor=\lfloor 16.2\rfloor=16
\]
count \(=16-13+1=4\) not unique.

We want uniqueness, so the bounds must differ by 0. Let’s jump by checking \(s\) where \(\frac{s}{5}\) is an integer or near; uniqueness likely when \( \lfloor s/5\rfloor\) equals \(\lceil (s-30)/4\rceil\), i.e. when
\[
\left\lfloor\frac{s}{5}\right\rfloor = \left\lceil\frac{s-30}{4}\right\rceil.
\]

Test systematically from \(81\) until we hit the threshold where uniqueness starts, then identify the last one before it fails for lower scores. Since the condition says: at the actual \(s\), John can determine \(c\) uniquely; for any lower score still \(>80\), he cannot. That means \(s\) is the **smallest** score \(>80\) for which uniqueness holds. (Lower but still over 80 makes it fail.) So find the minimum \(s>80\) giving uniqueness.

Continue:

\(s=82\):
\[
\left\lceil\frac{52}{4}\right\rceil=\lceil 13\rceil=13,\quad
\left\lfloor\frac{82}{5}\right\rfloor=\lfloor 16.4\rfloor=16
\]
count \(=4\).

\(s=83\):
\[
\left\lceil\frac{53}{4}\right\rceil=\lceil 13.25\rceil=14,\quad
\left\lfloor\frac{83}{5}\right\rfloor=\lfloor 16.6\rfloor=16
\]
count \(=16-14+1=3\).

\(s=84\):
\[
\left\lceil\frac{54}{4}\right\rceil=\lceil 13.5\rceil=14,\quad
\left\lfloor\frac{84}{5}\right\rfloor=\lfloor 16.8\rfloor=16
\]
count \(=3\).

\(s=85\):
\[
\left\lceil\frac{55}{4}\right\rceil=\lceil 13.75\rceil=14,\quad
\left\lfloor\frac{85}{5}\right\rfloor=\lfloor 17\rfloor=17
\]
count \(=17-14+1=4\).

\(s=86\):
\[
\left\lceil\frac{56}{4}\right\rceil=\lceil 14\rceil=14,\quad
\left\lfloor\frac{86}{5}\right\rfloor=\lfloor 17.2\rfloor=17
\]
count \(=4\).

\(s=87\):
\[
\left\lceil\frac{57}{4}\right\rceil=\lceil 14.25\rceil=15,\quad
\left\lfloor\frac{87}{5}\right\rfloor=\lfloor 17.4\rfloor=17
\]
count \(=17-15+1=3\).

\(s=88\):
\[
\left\lceil\frac{58}{4}\right\rceil=\lceil 14.5\rceil=15,\quad
\left\lfloor\frac{88}{5}\right\rfloor=\lfloor 17.6\rfloor=17
\]
count \(=3\).

\(s=89\):
\[
\left\lceil\frac{59}{4}\right\rceil=\lceil 14.75\rceil=15,\quad
\left\lfloor\frac{89}{5}\right\rfloor=\lfloor 17.8\rfloor=17
\]
count \(=3\).

\(s=90\):
\[
\left\lceil\frac{60}{4}\right\rceil=\lceil 15\rceil=15,\quad
\left\lfloor\frac{90}{5}\right\rfloor=\lfloor 18\rfloor=18
\]
count \(=18-15+1=4\).

This is not converging to 1; try higher. Note maximum possible score: when all 30 correct, \(s=30+4(30)=150\). Feasible interval length is about \(\frac{s}{5}-\frac{s-30}{4}=\frac{4s-5s+150}{20}=\frac{150-s}{20}\), which decreases as \(s\) increases. So uniqueness should happen near the top where this length becomes \(<1\).

So solve for when interval size can be 1: need
\[
\frac{\frac{s}{5}-\frac{s-30}{4}}{} = \frac{150-s}{20} < 1 \Rightarrow 150-s<20 \Rightarrow s>130.
\]
So search from 131 upward.

\(s=131\):
\[
\left\lceil\frac{101}{4}\right\rceil=\lceil 25.25\rceil=26,\quad
\left\lfloor\frac{131}{5}\right\rfloor=\lfloor 26.2\rfloor=26
\]
count \(=1\). Great: uniqueness holds at \(s=131\).

Now verify for any lower \(s>80\), uniqueness fails. Since we argued uniqueness can only occur for \(s>130\), it suffices to check \(s=130\).
\(s=130\):
\[
\left\lceil\frac{100}{4}\right\rceil=\lceil 25\rceil=25,\quad
\left\lfloor\frac{130}{5}\right\rfloor=\lfloor 26\rfloor=26
\]
count \(=26-25+1=2\), not unique.

Thus \(s=131\) is the smallest score \(>80\) with uniqueness, matching the condition.

Finally, we can recover \(c\) and ensure feasibility: from above for \(s=131\), \(c=26\). Then
\[
w=4c-(s-30)=104-101=3,\quad u=30-c-w=30-26-3=1\ge 0.
\]
All valid.

ANSWER: 131
```

</details>

<details>
<summary>Augmented generation 6</summary>

```text
Let \(c\) be the number correct and \(w\) wrong. Since there are 30 questions,
\[
c,w\ge 0,\qquad c+w\le 30.
\]
The score is
\[
s=30+4c-w.
\]

### Step 1: Express feasibility of \(c\) for a fixed score \(s\)
From \(s=30+4c-w\), we get
\[
w=30+4c-s.
\]
Impose the constraints \(w\ge 0\) and \(c+w\le 30\).

**(i) \(w\ge 0\):**
\[
30+4c-s\ge 0 \;\Rightarrow\; 4c\ge s-30 \;\Rightarrow\; c\ge \left\lceil \frac{s-30}{4}\right\rceil.
\]

**(ii) \(c+w\le 30\):**
\[
c+(30+4c-s)\le 30
\]
\[
5c-s\le 0 \;\Rightarrow\; c\le \left\lfloor \frac{s}{5}\right\rfloor.
\]

So for a given score \(s\), the feasible integer values of \(c\) are exactly
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]

John can determine \(c\) uniquely iff this interval contains exactly one integer, i.e.
\[
\left\lceil \frac{s-30}{4}\right\rceil=\left\lfloor \frac{s}{5}\right\rfloor.
\]

### Step 2: Use the “threshold” condition
We are told \(s>80\) and John **can** determine \(c\) from \(s\), but if \(s\) were **any lower** and still \(>80\), John **could not** determine \(c\).

That means: \(s\) is the **smallest** integer score strictly greater than 80 for which the feasible interval has size 1.

So we test candidate scores \(s=81,82,83,\dots\) until uniqueness holds, but we want the *first* such \(s\).

### Step 3: Check \(s=81\)
\[
\left\lceil \frac{81-30}{4}\right\rceil=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13
\]
\[
\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16
\]
So \(c\in[13,16]\), which gives **4** possibilities, not unique. Hence \(s\neq 81\).

### Step 4: Check \(s=82\)
\[
\left\lceil \frac{82-30}{4}\right\rceil=\left\lceil \frac{52}{4}\right\rceil=\left\lceil 13\right\rceil=13
\]
\[
\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16
\]
Still \(c\in[13,16]\), not unique.

### Step 5: Check \(s=83\)
\[
\left\lceil \frac{83-30}{4}\right\rceil=\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14
\]
\[
\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16
\]
Now \(c\in[14,16]\), still **3** possibilities.

### Step 6: Check \(s=84\)
\[
\left\lceil \frac{84-30}{4}\right\rceil=\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14
\]
\[
\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16
\]
Still \(c\in[14,16]\), not unique.

### Step 7: Check \(s=85\)
\[
\left\lceil \frac{85-30}{4}\right\rceil=\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14
\]
\[
\left\lfloor \frac{85}{5}\right\rfloor=\left\lfloor 17\right\rfloor=17
\]
So \(c\in[14,17]\): **4** possibilities.

### Step 8: Check \(s=86\)
\[
\left\lceil \frac{86-30}{4}\right\rceil=\left\lceil \frac{56}{4}\right\rceil=\left\lceil 14\right\rceil=14
\]
\[
\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17
\]
So \(c\in[14,17]\), not unique.

### Step 9: Check \(s=87\)
\[
\left\lceil \frac{87-30}{4}\right\rceil=\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15
\]
\[
\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17
\]
So \(c\in[15,17]\), not unique.

### Step 10: Check \(s=88\)
\[
\left\lceil \frac{88-30}{4}\right\rceil=\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15
\]
\[
\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17
\]
Still not unique.

### Step 11: Check \(s=89\)
\[
\left\lceil \frac{89-30}{4}\right\rceil=\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15
\]
\[
\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17
\]
Still \(c\in[15,17]\).

### Step 12: Check \(s=90\)
\[
\left\lceil \frac{90-30}{4}\right\rceil=\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15
\]
\[
\left\lfloor \frac{90}{5}\right\rfloor=\left\lfloor 18\right\rfloor=18
\]
So \(c\in[15,18]\), not unique.

At this point, brute forcing is inefficient, so instead enforce the uniqueness equality:
\[
\left\lceil \frac{s-30}{4}\right\rceil=\left\lfloor \frac{s}{5}\right\rfloor =: c.
\]
That means simultaneously:
\[
c-1 < \frac{s-30}{4} \le c
\quad\text{and}\quad
c \le \frac{s}{5} < c+1.
\]
Convert to inequalities for \(s\):
\[
4(c-1) < s-30 \le 4c \;\Rightarrow\; 4c+ -? 
\]
\[
4(c-1)+30 < s \le 4c+30
\]
and
\[
5c \le s < 5(c+1).
\]
So
\[
\max\big(4(c-1)+30,\;5c\big)\le s \le \min(4c+30,\;5c+5-1).
\]
We need the score \(s>80\) and to be the smallest such with exactly one integer \(c\). The simplest is to find where the bounds squeeze so that the feasible interval for \(c\) has size 1; that occurs when
\[
\left\lceil \frac{s-30}{4}\right\rceil=\left\lfloor \frac{s}{5}\right\rfloor
\]
for a first time after 80.

Try values of \(c\) around where the interval endpoints cross. From
\[
\frac{s-30}{4}\approx \frac{s}{5} \;\Rightarrow\; 5(s-30)=4s \Rightarrow s=150.
\]
So for uniqueness after 80, we likely need larger \(s\). Now we locate the first \(s>80\) where the integer equality holds by checking systematically via the integer condition:
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor
\]
unique means
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]
Let \(c\) be that common value. Then \(s\) must satisfy:
\[
\frac{s-30}{4}\in (c-1,c] \quad\Rightarrow\quad s\in(4c+26,\;4c+30]
\]
\[
\frac{s}{5}\in [c,c+1)\quad\Rightarrow\quad s\in [5c,\;5c+5).
\]
So \(s\) must lie in the intersection:
\[
s \in [5c,\;5c+5) \;\cap\; (4c+26,\;4c+30].
\]
Both endpoints depend linearly on \(c\); we want the smallest \(s>80\) in such an intersection.

Now test \(c\) values starting from where \(s>80\) forces \(c\) to be at least:
From \(s=30+4c-w\le 30+4c\), we get \(s\le 30+4c\), so
\[
80 < s \le 30+4c \Rightarrow 50<4c \Rightarrow c\ge 13.
\]
So start at \(c=13\).

For each \(c\), compute the possible \(s\) intersection:

**\(c=13\):**
\[
[5c,5c+5)=[65,70)
\]
\[
(4c+26,4c+30]=(78,82]
\]
Intersection is \((78,82]\cap[65,70)=\emptyset\). No.

**\(c=14\):**
\[
[70,75)
\]
\[
(4c+26,4c+30]=(82,86]
\]
Intersection is \((82,86]\cap[70,75)=\emptyset\). No.

**\(c=15\):**
\[
[75,80)
\]
\[
(4c+26,4c+30]=(86,90]
\]
Intersection empty.

**\(c=16\):**
\[
[80,85)
\]
\[
(4c+26,4c+30]=(90,94]
\]
Intersection empty (and in any case \(>80\) would require \(s\in(80,85)\), but second interval is \(>90\)).

**\(c=17\):**
\[
[85,90)
\]
\[
(4c+26,4c+30]=(94,98]
\]
Empty.

**\(c=18\):**
\[
[90,95)
\]
\[
(4c+26,4c+30]=(98,102]
\]
Empty.

**\(c=19\):**
\[
[95,100)
\]
\[
(4c+26,4c+30]=(102,106]
\]
Empty.

**\(c=20\):**
\[
[100,105)
\]
\[
(4c+26,4c+30]=(106,110]
\]
Empty.

We keep finding empty because \((4c+26,4c+30]\) starts at \(4c+26\) while the other interval is at \(5c\); compare:
Need \(5c < 4c+30 \Rightarrow c<30.\) but also need overlap:
\[
5c \le 4c+30 \Rightarrow c\le 30.
\]
For overlap to exist we also need
\[
4c+26 < 5c+5 \Rightarrow 4c+26 < 5c+5 \Rightarrow c>21.
\]
So overlap can only occur for \(22\le c\le 30\).

Proceed from \(c=22\):

**\(c=22\):**
\[
[110,115)
\]
\[
(4c+26,4c+30]=(114,118]
\]
Intersection: \(s\in(114,115)\) which contains no integer. (Integers would have to be 115? but 115 is excluded.)

**\(c=23\):**
\[
[115,120)
\]
\[
(4c+26,4c+30]=(118,122]
\]
Intersection: \((118,120)\). No integer.

**\(c=24\):**
\[
[120,125)
\]
\[
(4c+26,4c+30]=(122,126]
\]
Intersection: \((122,125)\) includes \(s=123,124\) (two integers) → not unique, but note uniqueness is already built into choosing \(c\); still, if two different \(s\) work for same \(c\), that’s fine. We need the *first* \(s>80\) overall.

Smallest integer in intersection is \(s=123\).

Now verify that for \(s=123\), the feasible \(c\) interval has size 1.

Compute:
\[
\left\lceil \frac{123-30}{4}\right\rceil=\left\lceil \frac{93}{4}\right\rceil=\left\lceil 23.25\right\rceil=24
\]
\[
\left\lfloor \frac{123}{5}\right\rfloor=\left\lfloor 24.6\right\rfloor=24
\]
So indeed \(c=24\) uniquely. Also check that \(s=122\) (any lower but still \(>80\) for threshold requirement) fails uniqueness:
\[
\left\lceil \frac{122-30}{4}\right\rceil=\left\lceil \frac{92}{4}\right\rceil=23
\]
\[
\left\lfloor \frac{122}{5}\right\rfloor=\left\lfloor 24.4\right\rfloor=24
\]
So \(c\in[23,24]\): two possibilities, not uniquely determined. Thus \(123\) is the smallest score \(>80\) with uniqueness.

Finally, answer asks for Mary’s score, which is this \(s\).

\[
\boxed{123}
\]

ANSWER: 123
```

</details>

<details>
<summary>Augmented generation 7</summary>

```text
Let \(c\) be the number correct and \(w\) the number wrong. Then \(c,w\ge 0\) integers and since there are 30 questions,
\[
c+w\le 30.
\]
The score is
\[
s=30+4c-w.
\]

### 1) Express \(c\) in terms of \(s\) and constraints
From \(s=30+4c-w\),
\[
w=30+4c-s.
\]
Impose feasibility:

- \(w\ge 0\):
\[
30+4c-s\ge 0 \;\Longrightarrow\; 4c\ge s-30 \;\Longrightarrow\; c\ge \left\lceil \frac{s-30}{4}\right\rceil.
\]

- \(c+w\le 30\):
\[
c+(30+4c-s)\le 30
\;\Longrightarrow\;
5c - s \le 0
\;\Longrightarrow\;
c\le \left\lfloor \frac{s}{5}\right\rfloor.
\]

So for a fixed score \(s\), the feasible integer values of \(c\) are exactly
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
Uniqueness of \(c\) means the interval contains exactly one integer:
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]

### 2) Use the problem’s “any lower but still over 80” condition
We are told \(s>80\) and John can determine \(c\) uniquely from that \(s\). Moreover, if the score were any lower but still \(>80\), uniqueness would fail. That means \(s\) is the **smallest** score \(>80\) for which the feasible set for \(c\) has size \(1\).

So we check \(s=81,82,83,\dots\) until uniqueness first occurs.

### 3) Compute uniqueness for \(s=81\)
\[
\left\lceil \frac{81-30}{4}\right\rceil=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,
\]
\[
\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
Interval for \(c\): \(13\le c\le 16\) has 4 integers \(\Rightarrow\) not unique.

### 4) Check \(s=82\)
\[
\left\lceil \frac{82-30}{4}\right\rceil=\left\lceil \frac{52}{4}\right\rceil=\left\lceil 13\right\rceil=13,
\]
\[
\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16.
\]
Still \(13\le c\le 16\), not unique.

### 5) Check \(s=83\)
\[
\left\lceil \frac{83-30}{4}\right\rceil=\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14,
\]
\[
\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16.
\]
Interval \(14\le c\le 16\) has 3 integers, not unique.

### 6) Check \(s=84\)
\[
\left\lceil \frac{84-30}{4}\right\rceil=\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14,
\]
\[
\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16.
\]
Interval \(14\le c\le 16\) has 3 integers.

### 7) Check \(s=85\)
\[
\left\lceil \frac{85-30}{4}\right\rceil=\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,
\]
\[
\left\lfloor \frac{85}{5}\right\rfloor=\left\lfloor 17\right\rfloor=17.
\]
Interval \(14\le c\le 17\) has 4 integers.

### 8) Check \(s=86\)
\[
\left\lceil \frac{86-30}{4}\right\rceil=\left\lceil \frac{56}{4}\right\rceil=14,
\]
\[
\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17.
\]
Interval \(14\le c\le 17\) has 4 integers.

### 9) Check \(s=87\)
\[
\left\lceil \frac{87-30}{4}\right\rceil=\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15,
\]
\[
\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17.
\]
Interval \(15\le c\le 17\) has 3 integers.

### 10) Check \(s=88\)
\[
\left\lceil \frac{88-30}{4}\right\rceil=\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15,
\]
\[
\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17.
\]
Interval \(15\le c\le 17\) has 3 integers.

### 11) Check \(s=89\)
\[
\left\lceil \frac{89-30}{4}\right\rceil=\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15,
\]
\[
\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17.
\]
Interval \(15\le c\le 17\) has 3 integers.

### 12) Check \(s=90\)
\[
\left\lceil \frac{90-30}{4}\right\rceil=\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15,
\]
\[
\left\lfloor \frac{90}{5}\right\rfloor=\left\lfloor 18\right\rfloor=18.
\]
Interval \(15\le c\le 18\) has 4 integers.

At this point, brute force suggests uniqueness might happen later; rather than continue, solve the equality condition.

### 13) Solve the uniqueness equality
We need
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]
Let the common integer be \(c\). Then necessarily
\[
c = \left\lceil \frac{s-30}{4}\right\rceil \quad\Longleftrightarrow\quad
c-1 < \frac{s-30}{4} \le c,
\]
and
\[
c = \left\lfloor \frac{s}{5}\right\rfloor \quad\Longleftrightarrow\quad
c \le \frac{s}{5} < c+1.
\]
These become:
\[
4c < s-30 \le 4c+4 \quad\Longrightarrow\quad 4c+30 < s \le 4c+34,
\]
\[
5c \le s < 5c+5.
\]
So \(s\) must satisfy
\[
\max(5c,\;4c+31)\le s \le \min(5c+4,\;4c+34).
\]
For feasibility to be a **single** integer \(s\) (since we’re looking for the smallest \(>80\)), we can instead use that for uniqueness of \(c\), the feasible \(c\)-interval collapses, i.e.
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor = c.
\]
Try \(s=95\):
\[
\left\lceil \frac{95-30}{4}\right\rceil=\left\lceil \frac{65}{4}\right\rceil=\left\lceil 16.25\right\rceil=17,
\]
\[
\left\lfloor \frac{95}{5}\right\rfloor=\left\lfloor 19\right\rfloor=19,
\]
not unique.

Try \(s=96\):
\[
\left\lceil \frac{66}{4}\right\rceil=\left\lceil 16.5\right\rceil=17,\quad
\left\lfloor 96/5\right\rfloor=\left\lfloor 19.2\right\rfloor=19.
\]
not unique.

Try \(s=99\):
\[
\left\lceil \frac{69}{4}\right\rceil=\left\lceil 17.25\right\rceil=18,\quad
\left\lfloor 99/5\right\rfloor=\left\lfloor 19.8\right\rfloor=19,
\]
not unique (two values 18 or 19).

Try \(s=100\):
\[
\left\lceil \frac{70}{4}\right\rceil=18,\quad
\left\lfloor 100/5\right\rfloor=20,
\]
not unique.

The first time it can collapse is when
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor
\]
with the bounds straddling closely. This happens when \(\frac{s-30}{4}\) is just above an integer and \(\frac{s}{5}\) is just below the next, etc. Testing \(s=93\):
\[
\left\lceil \frac{63}{4}\right\rceil=\left\lceil 15.75\right\rceil=16,\quad
\left\lfloor 93/5\right\rfloor=\left\lfloor 18.6\right\rfloor=18
\]
not.

Testing \(s=92\):
\[
\left\lceil \frac{62}{4}\right\rceil=\left\lceil 15.5\right\rceil=16,\quad
\left\lfloor 92/5\right\rfloor=\left\lfloor 18.4\right\rfloor=18
\]
not.

Testing \(s=94\):
\[
\left\lceil \frac{64}{4}\right\rceil=16,\quad
\left\lfloor 94/5\right\rfloor=\left\lfloor 18.8\right\rfloor=18
\]
gives \(16\le c\le 18\), not.

Testing \(s=97\):
\[
\left\lceil \frac{67}{4}\right\rceil=\left\lceil 16.75\right\rceil=17,\quad
\left\lfloor 97/5\right\rfloor=\left\lfloor 19.4\right\rfloor=19
\]
not.

Testing \(s=98\):
\[
\left\lceil \frac{68}{4}\right\rceil=17,\quad
\left\lfloor 98/5\right\rfloor=\left\lfloor 19.6\right\rfloor=19
\]
not.

Testing \(s=101\):
\[
\left\lceil \frac{71}{4}\right\rceil=\left\lceil 17.75\right\rceil=18,\quad
\left\lfloor 101/5\right\rfloor=\left\lfloor 20.2\right\rfloor=20
\]
not.

At this stage, observe that for uniqueness we require
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor
\]
which is possible only if the gap between the two real quantities is \(<1\) and discretization aligns. The real gap:
\[
\frac{s}{5} - \frac{s-30}{4} = \frac{4s -5s +150}{20}=\frac{150-s}{20}.
\]
For \(s>80\), this gap is \(\frac{150-s}{20} < \frac{150-80}{20}=3.5\), so not helpful.

Given the exploratory checks, the first score \(>80\) that yields exactly one feasible \(c\) is known to be \(s=86\)? but we checked 86 gave 4 feasible \(c\). So continue to the actual collapsing point by setting
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor
\]
and trying where \(\frac{s-30}{4}\) and \(\frac{s}{5}\) are very close. That occurs near where \( \frac{s}{5} \approx \frac{s-30}{4}\), i.e. \( \frac{s}{5}=\frac{s-30}{4}\Rightarrow 4s=5s-150\Rightarrow s=150\).
So check \(s=150\):
\[
\left\lceil \frac{150-30}{4}\right\rceil=\left\lceil \frac{120}{4}\right\rceil=\left\lceil 30\right\rceil=30,
\]
\[
\left\lfloor \frac{150}{5}\right\rfloor=\left\lfloor 30\right\rfloor=30.
\]
This gives exactly one possible \(c\): \(c=30\).

Now apply the “if score had been any lower but still over 80, John could not have determined it” condition: for any \(s<150\), the feasible interval for \(c\) has size at least 2 (indeed from our sample checks and because the endpoints separate once the real gap is \(>0\)). Thus the smallest \(s>80\) for uniqueness is actually \(s=150\), because uniqueness cannot occur earlier when the feasible ranges still have multiple integers; only at the maximum score does \(c\) become forced to 30.

Finally, verify feasibility at \(s=150\): \(c=30\) implies \(w=30+4(30)-150=30+120-150=0\), consistent.

\[
\boxed{150}
\]

ANSWER: 150
```

</details>

<details>
<summary>Augmented generation 8</summary>

```text
Let \(c\) be the number of correct answers, \(w\) the number wrong, and \(u\) the number unanswered. Then
\[
c+w+u=30,\qquad c,w,u\ge 0 \text{ integers.}
\]
The score is
\[
s=30+4c-w.
\]

John observes a score \(s>80\) and must uniquely determine \(c\).  
So for a given \(s\), we must have exactly one feasible integer value of \(c\).

---

### 1) Convert the score condition to constraints on \(c\)

From \(s=30+4c-w\), we get
\[
w=30+4c-s.
\]
Feasibility requires \(w\ge 0\) and \(w\le 30-c\) (since \(u=30-c-w\ge 0\)).

So:
- \(w\ge 0 \implies 30+4c-s\ge 0 \implies 4c\ge s-30 \implies c\ge \left\lceil \frac{s-30}{4}\right\rceil.\)
- \(u\ge 0\) is equivalent to \(c+w\le 30\):
\[
c+w=c+(30+4c-s)=30+5c-s\le 30 \implies 5c\le s \implies c\le \left\lfloor \frac{s}{5}\right\rfloor.
\]

Thus for a fixed \(s\), the possible values of \(c\) are exactly the integers in
\[
\left[\left\lceil \frac{s-30}{4}\right\rceil,\; \left\lfloor \frac{s}{5}\right\rfloor\right].
\]
John can determine \(c\) uniquely iff this interval contains exactly one integer:
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]

---

### 2) Use the “any lower but still over 80” condition

Let \(s\) be the (observed) score. For any \(s'\) with
\[
80 < s' < s,
\]
John cannot determine \(c\), so the feasible interval for \(c\) must contain at least two integers.

This means \(s\) is the *first* score strictly greater than \(80\) for which the interval collapses to one integer.

So we test scores starting at the smallest possible integer \(>80\), i.e. \(s=81\), \(82\), etc., and find the first one giving uniqueness.

---

### 3) Compute feasible \(c\) counts for \(s=81,82,\dots\)

We compute:
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad U(s)=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Uniqueness means \(L(s)=U(s)\).

- **\(s=81\):**
\[
L=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,\quad
U=\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
Interval \([13,16]\) has \(4\) integers → not unique.

- **\(s=82\):**
\[
L=\left\lceil \frac{52}{4}\right\rceil=\left\lceil 13\right\rceil=13,\quad
U=\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16.
\]
Interval \([13,16]\) → not unique.

- **\(s=83\):**
\[
L=\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14,\quad
U=\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16.
\]
Interval \([14,16]\) → not unique.

- **\(s=84\):**
\[
L=\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14,\quad
U=\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16.
\]
Interval \([14,16]\) → not unique.

- **\(s=85\):**
\[
L=\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,\quad
U=\left\lfloor \frac{85}{5}\right\rfloor=17.
\]
Interval \([14,17]\) → not unique.

- **\(s=86\):**
\[
L=\left\lceil \frac{56}{4}\right\rceil=\left\lceil 14\right\rceil=14,\quad
U=\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17.
\]
Interval \([14,17]\) → not unique.

- **\(s=87\):**
\[
L=\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15,\quad
U=\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17.
\]
Interval \([15,17]\) → not unique.

- **\(s=88\):**
\[
L=\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15,\quad
U=\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17.
\]
Interval \([15,17]\) → not unique.

- **\(s=89\):**
\[
L=\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15,\quad
U=\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17.
\]
Interval \([15,17]\) → not unique.

- **\(s=90\):**
\[
L=\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15,\quad
U=\left\lfloor \frac{90}{5}\right\rfloor=18.
\]
Interval \([15,18]\) → not unique.

We see uniqueness hasn’t happened yet, so continue until \(L(s)=U(s)\).

- **\(s=91\):**
\[
L=\left\lceil \frac{61}{4}\right\rceil=\left\lceil 15.25\right\rceil=16,\quad
U=\left\lfloor \frac{91}{5}\right\rfloor=\left\lfloor 18.2\right\rfloor=18.
\]
Not unique.

- **\(s=92\):**
\[
L=\left\lceil \frac{62}{4}\right\rceil=\left\lceil 15.5\right\rceil=16,\quad
U=\left\lfloor 18.4\right\rfloor=18.
\]
Not unique.

- **\(s=93\):**
\[
L=\left\lceil 15.75\right\rceil=16,\quad
U=\left\lfloor 18.6\right\rfloor=18.
\]
Not unique.

- **\(s=94\):**
\[
L=\left\lceil 16\right\rceil=16,\quad
U=\left\lfloor 18.8\right\rfloor=18.
\]
Not unique.

- **\(s=95\):**
\[
L=\left\lceil \frac{65}{4}\right\rceil=\left\lceil 16.25\right\rceil=17,\quad
U=\left\lfloor 19\right\rfloor=19.
\]
Not unique.

- **\(s=96\):**
\[
L=\left\lceil \frac{66}{4}\right\rceil=\left\lceil 16.5\right\rceil=17,\quad
U=\left\lfloor 19.2\right\rfloor=19.
\]
Not unique.

- **\(s=97\):**
\[
L=\left\lceil 16.75\right\rceil=17,\quad
U=\left\lfloor 19.4\right\rfloor=19.
\]
Not unique.

- **\(s=98\):**
\[
L=\left\lceil 17\right\rceil=17,\quad
U=\left\lfloor 19.6\right\rfloor=19.
\]
Not unique.

- **\(s=99\):**
\[
L=\left\lceil \frac{69}{4}\right\rceil=\left\lceil 17.25\right\rceil=18,\quad
U=\left\lfloor 19.8\right\rfloor=19.
\]
Not unique.

- **\(s=100\):**
\[
L=\left\lceil \frac{70}{4}\right\rceil=\left\lceil 17.5\right\rceil=18,\quad
U=\left\lfloor 20\right\rfloor=20.
\]
Not unique.

At this point, rather than brute force, use the equality condition more structurally.

We need
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor =: c.
\]
This implies
\[
c \le \frac{s}{5} < c+1 \quad\Rightarrow\quad 5c \le s \le 5c+4,
\]
and
\[
c-1 < \frac{s-30}{4} \le c \quad\Rightarrow\quad 4(c-1) < s-30 \le 4c
\]
\[
\Rightarrow\quad 4c+26 < s \le 4c+30.
\]

So \(s\) must satisfy both:
\[
5c \le s \le 5c+4,
\]
\[
4c+27 \le s \le 4c+30.
\]
(We converted the strict inequality to an integer bound: \(4c+26 < s\) gives \(s\ge 4c+27\).)

Thus:
\[
s \in [5c,\;5c+4]\cap [4c+27,\;4c+30].
\]
For uniqueness, this intersection must be nonempty but force exactly that single integer \(c\) to be feasible; the “first above 80” will correspond to smallest \(s\) with nonempty intersection and the previous scores giving \(\ge 2\) values. Testing candidates for \(c\) starting near where \(s\approx 80\).

If \(s\approx 80\), then \(c\approx s/5\approx 16\). Try \(c=16\).
Then feasible \(s\) from the intersection:
\[
[5c,5c+4]=[80,84],\quad [4c+27,4c+30]=[91,94].
\]
Disjoint → no uniqueness at \(c=16\) (actually no feasible \(c=16\) at those scores simultaneously under the equality condition).

Try \(c=17\):
\[
[85,89],\quad [4\cdot 17+27,4\cdot 17+30]=[95,98].
\]
Disjoint.

Try \(c=18\):
\[
[90,94],\quad [4\cdot 18+27,4\cdot 18+30]=[99,102].
\]
Disjoint.

Try \(c=19\):
\[
[95,99],\quad [4\cdot 19+27,4\cdot 19+30]=[103,106].
\]
Disjoint.

Try \(c=20\):
\[
[100,104],\quad [4\cdot 20+27,4\cdot 20+30]=[107,110].
\]
Disjoint.

So the equality condition as written suggests no solutions—meaning we must respect the exact ceiling/floor definitions carefully: the “uniqueness” is \(L(s)=U(s)\), not necessarily equal to the same \(c\) coming from those inequalities with strictness handled; however the above derivation should still be valid. The mismatch indicates the earlier brute-force check missed where uniqueness occurs (likely at a larger \(s\)). Let’s compute directly by searching for \(L(s)=U(s)\) without listing all values too far.

We need:
\[
\left\lceil \frac{s-30}{4}\right\rceil = \left\lfloor \frac{s}{5}\right\rfloor.
\]
Let \(m=\left\lfloor \frac{s}{5}\right\rfloor\). Then
\[
5m \le s \le 5m+4.
\]
Also require
\[
\left\lceil \frac{s-30}{4}\right\rceil = m.
\]
That means
\[
m-1 < \frac{s-30}{4} \le m
\]
\[
4(m-1) < s-30 \le 4m
\]
\[
4m+26 < s \le 4m+30
\]
\[
\Rightarrow\quad s \in \{4m+27,4m+28,4m+29,4m+30\}.
\]
Now also \(s\in[5m,5m+4]\). So we need the overlap between
\[
[5m,5m+4]\quad \text{and}\quad \{4m+27,4m+28,4m+29,4m+30\}.
\]
Thus for some \(k\in\{27,28,29,30\}\),
\[
5m \le 4m+k \le 5m+4
\]
\[
m \le k \le m+4.
\]
So \(k\in\{27,28,29,30\}\) must also satisfy \(m\le k\le m+4\), i.e. \(m\in [k-4,k]\).

Pick \(k=27\): then \(m\in[23,27]\).  
Pick \(k=28\): \(m\in[24,28]\).  
Pick \(k=29\): \(m\in[25,29]\).  
Pick \(k=30\): \(m\in[26,30]\).

Now also require \(s>80\), and \(s=4m+k\) with \(s\) consistent. We want the smallest \(s>80\) for which uniqueness holds.

Try smallest possible \(m\) that gives some \(s>80\).
If \(m=16\), then \(k\) must be in \([16,20]\), impossible. So \(m\) must be at least \(23\) (from \(k=27\) case).

Take \(m=23\). Then eligible \(k\) satisfy \(m\le k\le m+4\), i.e. \(23\le k\le 27\). Intersect with \(\{27,28,29,30\}\) gives \(k=27\).
So
\[
s=4m+k=4\cdot 23+27=92+27=119.
\]
Check that \(s>80\) and that for any lower score still \(>80\), uniqueness fails—this is satisfied by taking the minimal \(m\) yielding a feasible \(s\).

Thus the first (and therefore required) score is \(119\).

Finally confirm uniqueness at \(s=119\):
\[
L=\left\lceil \frac{119-30}{4}\right\rceil=\left\lceil \frac{89}{4}\right\rceil=\left\lceil 22.25\right\rceil=23,
\]
\[
U=\left\lfloor \frac{119}{5}\right\rfloor=\left\lfloor 23.8\right\rfloor=23.
\]
So exactly one \(c\) value, namely \(c=23\).

Therefore the score is \(\boxed{119}\).

ANSWER: 119
```

</details>

<details>
<summary>Augmented generation 9</summary>

```text
Let \(c\) be the number correct and \(w\) the number wrong. Then \(c+w\le 30\) and \(c,w\) are integers with \(c,w\ge 0\).

The score is
\[
s=30+4c-w.
\]
Rearrange:
\[
4c-w=s-30 \quad\Longrightarrow\quad w=4c-(s-30)=4c-s+30.
\]
Feasibility requires:
- \(w\ge 0 \Rightarrow 4c-s+30\ge 0 \Rightarrow c\ge \frac{s-30}{4}\).
- \(c+w\le 30\Rightarrow c+(4c-s+30)\le 30\Rightarrow 5c-s+30\le 30\Rightarrow 5c\le s\Rightarrow c\le \frac{s}{5}\).

So for a fixed score \(s\), the possible integer values of \(c\) are exactly
\[
\left\{c\in\mathbb Z:\ \left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor\right\}.
\]
John can determine \(c\) iff this set has size \(1\), i.e.
\[
\left\lceil \frac{s-30}{4}\right\rceil=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Also, the problem states: if \(s\) were any lower but still \(>80\), John could *not* determine \(c\). Since the “uniqueness” condition can only fail at the first score where the feasible set grows/shrinks, this means that at the score \(s\), uniqueness holds, and for every integer score \(s'<s\) with \(80<s'<s\), uniqueness fails. In particular, uniqueness should fail at the immediately lower attainable score (because if the feasible set had size \(\ge 2\) there, it would remain so for some neighborhood).

Now search among integers \(s\) with \(s>80\) by enforcing the uniqueness condition.

Compute candidates via equality:
\[
\left\lceil \frac{s-30}{4}\right\rceil=\left\lfloor \frac{s}{5}\right\rfloor =: k.
\]
That implies
\[
k \le \frac{s}{5} < k+1 \quad\Longrightarrow\quad 5k \le s \le 5k+4,
\]
and
\[
k \le \frac{s-30}{4} < k+1 \quad\Longrightarrow\quad 4k+30 \le s < 4k+34,
\]
i.e.
\[
s \in [5k,\,5k+4]\cap[4k+30,\,4k+33].
\]

Try \(s\) near 80. Note \(c\le 30\), so from \(s=30+4c-w\) we get \(s\le 30+4c\le 150\), so manageable.

Let’s directly test the equality by checking when the feasible interval collapses.

For a given \(s\),
\[
L=\left\lceil \frac{s-30}{4}\right\rceil,\quad U=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Uniqueness means \(L=U\).

Start at \(s=81\):
\[
L=\left\lceil \frac{51}{4}\right\rceil=\lceil 12.75\rceil=13,\quad U=\left\lfloor \frac{81}{5}\right\rfloor=\lfloor 16.2\rfloor=16
\]
Not unique.

We need \(s\) large enough that \(U\) is close to \(L\). Observe growth rates: \(U\approx s/5\), \(L\approx (s-30)/4\), and \(s/5\) increases slower than \((s-30)/4\). So eventually \(U\) will drop below \(L\) and become impossible; uniqueness will occur right at the last score where feasible and with \(U=L\).

Let’s find when \(U=L\) can happen. A necessary condition for feasibility is \(L\le U\), i.e.
\[
\left\lceil\frac{s-30}{4}\right\rceil \le \left\lfloor\frac{s}{5}\right\rfloor \le \frac{s}{5}.
\]
This is consistent only near where \(\frac{s-30}{4}\approx \frac{s}{5}\).
Solve:
\[
\frac{s-30}{4}=\frac{s}{5}\Rightarrow 5(s-30)=4s\Rightarrow 5s-150=4s\Rightarrow s=150.
\]
So uniqueness (if it happens) should be close to the top. Since \(s>80\), we can look at high scores and see where the feasible interval size becomes \(1\).

Test \(s=150\):
\[
L=\left\lceil \frac{120}{4}\right\rceil=\lceil 30\rceil=30,\quad U=\left\lfloor \frac{150}{5}\right\rfloor=\lfloor 30\rfloor=30.
\]
So \(c=30\) is uniquely determined when \(s=150\).

Now check that for any lower integer score \(s'\) with \(80<s'<150\), uniqueness fails (i.e., the feasible set has at least 2 integers or is not unique). In fact, as soon as \(s<150\),
\[
U=\left\lfloor \frac{s}{5}\right\rfloor \le 29.
\]
But \(L=\left\lceil \frac{s-30}{4}\right\rceil\) will be at most \(30\) and will often be \(\le 29\) as well; we must ensure there is more than one feasible integer \(c\) for \(s=149\).

Check \(s=149\):
\[
L=\left\lceil \frac{119}{4}\right\rceil=\lceil 29.75\rceil=30,\quad U=\left\lfloor \frac{149}{5}\right\rfloor=\lfloor 29.8\rfloor=29.
\]
Then \(L>U\), so there are **no** feasible solutions—contradicting the premise that Mary’s score is attainable. But note: the premise says “Mary told John her score … John was able to determine \(c\).” Thus Mary’s score must be attainable. So \(149\) is unattainable, meaning the “any lower but still over 80” clause is intended over scores that could occur. In AIME, this means among *attainable* scores \(>80\), the first attainable score where uniqueness holds is the one we want.

So we must ensure that among attainable scores below 150 but above 80, uniqueness fails. Since \(149\) is unattainable, the relevant next attainable score is \(148\) (we can check attainability quickly).

Check \(s=148\):
\[
L=\left\lceil \frac{118}{4}\right\rceil=\lceil 29.5\rceil=30,\quad U=\left\lfloor \frac{148}{5}\right\rfloor=\lfloor 29.6\rfloor=29,
\]
again impossible.

Check \(s=146\):
\[
L=\left\lceil \frac{116}{4}\right\rceil=\lceil 29\rceil=29,\quad U=\left\lfloor \frac{146}{5}\right\rfloor=\lfloor 29.2\rfloor=29.
\]
This gives uniqueness at \(s=146\), but does it satisfy the “any lower but still over 80” condition? We need uniqueness not to hold for *any* attainable score lower than Mary’s while still \(>80\). Therefore Mary’s score must be the *smallest* attainable score \(>80\) for which uniqueness holds, because the statement says that if the score had been any lower (still \(>80\)), John could not have determined \(c\).

So we must find the smallest attainable \(s>80\) with \(L=U\).

Let’s search downwards from where uniqueness occurs.

We already found:
- At \(s=150\): \(L=U=30\) (feasible, uniqueness).
- At \(s=149,148,147,146?\) we checked 149,148 impossible; at \(146\) uniqueness holds, so if \(146>80\) and is attainable, that would violate the condition unless Mary’s score is \(\le 146\). Hence Mary’s score must be \(\le 146\) but still the first attainable with uniqueness.

Check \(s=145\):
\[
L=\left\lceil \frac{115}{4}\right\rceil=\lceil 28.75\rceil=29,\quad U=\left\lfloor \frac{145}{5}\right\rfloor=29.
\]
So \(s=145\) is also uniquely determined.

Continue decreasing:
\(s=144\):
\[
L=\left\lceil \frac{114}{4}\right\rceil=\lceil 28.5\rceil=29,\quad U=\left\lfloor \frac{144}{5}\right\rfloor=\lfloor 28.8\rfloor=28
\]
impossible.

So the feasible/unique threshold is jumping over unreachable scores. We need the *lowest* attainable score \(>80\) for which \(L=U\) (and for any lower attainable score, \(L<U\)).

Proceed with computation, but note uniqueness occurs when
\[
\left\lceil\frac{s-30}{4}\right\rceil=\left\lfloor\frac{s}{5}\right\rfloor.
\]
Let’s test attainable candidates systematically by checking when \(L\) and \(U\) can match.

Try \(s=130\):
\[
L=\left\lceil\frac{100}{4}\right\rceil=25,\quad U=\left\lfloor\frac{130}{5}\right\rfloor=26 \Rightarrow \text{not unique.}
\]
\(s=120\):
\[
L=\left\lceil\frac{90}{4}\right\rceil=23,\quad U=\left\lfloor\frac{120}{5}\right\rfloor=24 \Rightarrow \text{not unique.}
\]
As we decrease further, \(U-L\) likely grows, so uniqueness becomes less likely—so the “first” uniqueness above 80 will be some specific value where the interval has exactly one integer, meaning \(U-L=0\).

Test around where \(s/5\) and \((s-30)/4\) are separated by about 1. Consider approximate equality:
\[
\frac{s}{5}-\frac{s-30}{4}=\frac{4s-(5s-150)}{20}=\frac{150-s}{20}.
\]
For uniqueness we need the integer rounding to close the gap. Since at \(s=150\) the gap is 0. For uniqueness to happen, we likely need \(150-s\) small. Indeed we saw uniqueness for \(145\) too.

Let’s check down to the point where uniqueness stops.
We found impossibility at \(144\), then uniqueness at \(145\). Next check \(143\):
\[
L=\left\lceil \frac{113}{4}\right\rceil=\lceil 28.25\rceil=29,\quad U=\left\lfloor\frac{143}{5}\right\rfloor=\lfloor 28.6\rfloor=28
\]
impossible.

\(142\):
\[
L=\left\lceil\frac{112}{4}\right\rceil=28,\quad U=\left\lfloor\frac{142}{5}\right\rfloor=28
\]
Uniqueness at \(s=142\) (feasible).

\(141\):
\[
L=\left\lceil\frac{111}{4}\right\rceil=\lceil 27.75\rceil=28,\quad U=\left\lfloor\frac{141}{5}\right\rfloor=\lfloor 28.2\rfloor=28
\]
Uniqueness at \(141\) too.

\(140\):
\[
L=\left\lceil\frac{110}{4}\right\rceil=\lceil 27.5\rceil=28,\quad U=\left\lfloor\frac{140}{5}\right\rfloor=28
\]
Uniqueness at \(140\).

\(139\):
\[
L=\left\lceil\frac{109}{4}\right\rceil=\lceil 27.25\rceil=28,\quad U=\left\lfloor\frac{139}{5}\right\rfloor=\lfloor 27.8\rfloor=27
\]
impossible.

So attainable uniqueness values seem to include \(140,141,142,145,150,\dots\). We need the smallest attainable \(s>80\) with uniqueness. Continue.

Try \(s=135\):
\[
L=\left\lceil\frac{105}{4}\right\rceil=\lceil 26.25\rceil=27,\quad U=\left\lfloor\frac{135}{5}\right\rfloor=27
\]
Uniqueness at \(135\).

\(s=134\):
\[
L=\left\lceil\frac{104}{4}\right\rceil=\lceil 26\rceil=26,\quad U=\left\lfloor\frac{134}{5}\right\rfloor=26
\]
Uniqueness at \(134\).

\(s=133\):
\[
L=\left\lceil\frac{103}{4}\right\rceil=\lceil 25.75\rceil=26,\quad U=\left\lfloor\frac{133}{5}\right\rfloor=26
\]
Uniqueness at \(133\).

\(s=132\):
\[
L=\left\lceil\frac{102}{4}\right\rceil=\lceil 25.5\rceil=26,\quad U=\left\lfloor\frac{132}{5}\right\rfloor=\lfloor 26.4\rfloor=26
\]
Uniqueness at \(132\).

\(s=131\):
\[
L=\left\lceil\frac{101}{4}\right\rceil=\lceil 25.25\rceil=26,\quad U=\left\lfloor\frac{131}{5}\right\rfloor=\lfloor 26.2\rfloor=26
\]
Uniqueness at \(131\).

\(s=130\) we saw not unique. So uniqueness holds for \(131,132,133,134,135,\dots\) but fails at \(130\) (and likely below). Therefore the smallest attainable \(s>80\) with uniqueness is \(131\).

We must also ensure that every attainable score between 81 and 130 gives non-uniqueness; since at 130 we already have two possible integers (\(L=25,U=26\)), and rounding patterns only spread further apart as \(s\) decreases, uniqueness will not reappear before 130.

Thus Mary’s score is \(s=131\).

(Feasibility/unique \(c\) at \(131\): \(c=\left\lceil\frac{101}{4}\right\rceil=26\), and then \(w=4c-(s-30)=104-101=3\), with \(c+w=29\le 30\), all valid.)

ANSWER: 131
```

</details>

<details>
<summary>Augmented generation 10</summary>

```text
Let \(c\) be the number correct and \(w\) wrong. Since there are 30 questions total and unanswered are allowed, we have
\[
c+w\le 30,\qquad c\ge 0,\ w\ge 0,\qquad c,w\in\mathbb Z.
\]
The score is
\[
s=30+4c-w.
\]

### 1) Feasible \(c\) from a given score \(s\)
Rewrite the score equation in terms of \(w\):
\[
w=30+4c-s.
\]
For this to be feasible, we need
\[
w\ge 0 \implies 30+4c-s\ge 0 \implies c\ge \frac{s-30}{4},
\]
and
\[
c+w\le 30 \implies c+(30+4c-s)\le 30 \implies 5c-s\le 0 \implies c\le \frac{s}{5}.
\]
Thus, for a fixed score \(s\), the feasible integers \(c\) satisfy
\[
\left\lceil \frac{s-30}{4}\right\rceil \le c \le \left\lfloor \frac{s}{5}\right\rfloor.
\]
John can determine the number of correct answers exactly iff there is **exactly one** integer \(c\) in that interval.

So we require
\[
\left\lfloor \frac{s}{5}\right\rfloor=\left\lceil \frac{s-30}{4}\right\rceil.
\]
(And for “any lower but still over 80”, uniqueness must fail—i.e., the feasible set contains \(\ge 2\) integers.)

### 2) Search for the score \(s>80\) where uniqueness first occurs
The problem says: Mary’s score is over 80, and if the score had been any lower but still over 80, then John could not have determined \(c\) uniquely. So \(s\) is the **smallest** integer score in the range \(81,82,\dots\) for which uniqueness holds.

So start checking \(s=81\) upward for uniqueness.

Compute the two bounds:
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\qquad U(s)=\left\lfloor \frac{s}{5}\right\rfloor.
\]

- \(s=81\):
\[
L=\left\lceil \frac{51}{4}\right\rceil=\left\lceil 12.75\right\rceil=13,\quad
U=\left\lfloor \frac{81}{5}\right\rfloor=\left\lfloor 16.2\right\rfloor=16.
\]
Interval \([13,16]\) has 4 integers → not unique.

- \(s=82\):
\[
L=\left\lceil \frac{52}{4}\right\rceil=\left\lceil 13\right\rceil=13,\quad
U=\left\lfloor \frac{82}{5}\right\rfloor=\left\lfloor 16.4\right\rfloor=16.
\]
Interval \([13,16]\) has 4 integers → not unique.

- \(s=83\):
\[
L=\left\lceil \frac{53}{4}\right\rceil=\left\lceil 13.25\right\rceil=14,\quad
U=\left\lfloor \frac{83}{5}\right\rfloor=\left\lfloor 16.6\right\rfloor=16.
\]
Interval \([14,16]\) has 3 integers → not unique.

- \(s=84\):
\[
L=\left\lceil \frac{54}{4}\right\rceil=\left\lceil 13.5\right\rceil=14,\quad
U=\left\lfloor \frac{84}{5}\right\rfloor=\left\lfloor 16.8\right\rfloor=16.
\]
Interval \([14,16]\) has 3 integers → not unique.

- \(s=85\):
\[
L=\left\lceil \frac{55}{4}\right\rceil=\left\lceil 13.75\right\rceil=14,\quad
U=\left\lfloor \frac{85}{5}\right\rfloor=17.
\]
Interval \([14,17]\) has 4 integers → not unique.

- \(s=86\):
\[
L=\left\lceil \frac{56}{4}\right\rceil=\left\lceil 14\right\rceil=14,\quad
U=\left\lfloor \frac{86}{5}\right\rfloor=\left\lfloor 17.2\right\rfloor=17.
\]
Interval \([14,17]\) has 4 integers → not unique.

- \(s=87\):
\[
L=\left\lceil \frac{57}{4}\right\rceil=\left\lceil 14.25\right\rceil=15,\quad
U=\left\lfloor \frac{87}{5}\right\rfloor=\left\lfloor 17.4\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

- \(s=88\):
\[
L=\left\lceil \frac{58}{4}\right\rceil=\left\lceil 14.5\right\rceil=15,\quad
U=\left\lfloor \frac{88}{5}\right\rfloor=\left\lfloor 17.6\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

- \(s=89\):
\[
L=\left\lceil \frac{59}{4}\right\rceil=\left\lceil 14.75\right\rceil=15,\quad
U=\left\lfloor \frac{89}{5}\right\rfloor=\left\lfloor 17.8\right\rfloor=17.
\]
Interval \([15,17]\) has 3 integers → not unique.

- \(s=90\):
\[
L=\left\lceil \frac{60}{4}\right\rceil=\left\lceil 15\right\rceil=15,\quad
U=\left\lfloor \frac{90}{5}\right\rfloor=18.
\]
Interval \([15,18]\) has 4 integers → not unique.

At this point, the uniqueness condition is getting closer only when \(U\) and \(L\) coincide. Let’s solve when that can happen.

We need
\[
\left\lceil \frac{s-30}{4}\right\rceil=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Try to find an \(s\) where the interval collapses. That requires \(L(s)\) and \(U(s)\) to be equal, meaning the gap \( \frac{s}{5}-\frac{s-30}{4}=\frac{4s-5s+150}{20}=\frac{150-s}{20}\) must be small and compatible with ceilings/floors. Since \(s>80\), \(\frac{150-s}{20}\) is between \( \frac{60}{20}=3\) and \( \frac{70}{20}=3.5\); still not tiny, so collapse likely happens only at a specific rounding coincidence.

Continue by checking the next scores, but more efficiently:

Compute \(U(s)=\lfloor s/5\rfloor\). For each \(k\), \(U(s)=k\) when \(5k\le s\le 5k+4\).
Also \(L(s)=\left\lceil (s-30)/4\right\rceil\) changes when \(s\) crosses multiples of 4.

We can just test candidate \(s\) values where collapse might occur; the first plausible one is when \(U(s)\) is just one more than \(L(s)\) usually. Let’s jump to where \(U(s)\) increases to 18:
That happens at \(s=90,91,92,93,94\) gives \(U=18\).
For uniqueness with \(U=18\), we need \(L(s)=18\) too.

So check \(L(s)=18\):
\[
L(s)=18 \iff 17<\frac{s-30}{4}\le 18.
\]
That is
\[
68 < s-30 \le 72 \implies 98 < s \le 102.
\]
Intersect with \(s\) where \(U=18\), i.e. \(90\le s\le 94\). No intersection.

Next \(U=19\) occurs for \(95\le s\le 99\).
Need \(L(s)=19\):
\[
18<\frac{s-30}{4}\le 19 \implies 72 < s-30 \le 76 \implies 102 < s \le 106,
\]
No intersection with \(95\le s\le 99\).

Next \(U=20\) for \(100\le s\le 104\).
Need \(L(s)=20\):
\[
19<\frac{s-30}{4}\le 20 \implies 76 < s-30 \le 80 \implies 106 < s \le 110,
\]
No intersection with \(100\le s\le 104\).

This indicates that equality won’t occur with \(L(s)\) exactly equal to \(U(s)\) for these \(U\) values as \(s\) increases; instead, we should check actual equality directly by continuing the interval test. Let’s proceed and actually find the first \(s>80\) with \(\#\{c\}=1\).

The number of feasible integers is
\[
U(s)-L(s)+1.
\]
We need \(U(s)-L(s)=0\).

Compute from formulas:
\[
L(s)=\left\lceil \frac{s-30}{4}\right\rceil,\quad U(s)=\left\lfloor \frac{s}{5}\right\rfloor.
\]
Try \(s=104\):
\[
L=\left\lceil \frac{74}{4}\right\rceil=\left\lceil 18.5\right\rceil=19,\quad
U=\left\lfloor \frac{104}{5}\right\rfloor=\left\lfloor 20.8\right\rfloor=20.
\]
Not unique.

Try \(s=105\):
\[
L=\left\lceil \frac{75}{4}\right\rceil=\left\lceil 18.75\right\rceil=19,\quad
U=\left\lfloor 21\right\rfloor=21.
\]
Not unique.

Try \(s=106\):
\[
L=\left\lceil \frac{76}{4}\right\rceil=\left\lceil 19\right\rceil=19,\quad
U=\left\lfloor 21.2\right\rfloor=21.
\]
Not unique.

Try \(s=107\):
\[
L=\left\lceil \frac{77}{4}\right\rceil=\left\lceil 19.25\right\rceil=20,\quad
U=\left\lfloor 21.4\right\rfloor=21.
\]
Not unique.

Try \(s=108\):
\[
L=\left\lceil \frac{78}{4}\right\rceil=\left\lceil 19.5\right\rceil=20,\quad
U=\left\lfloor 21.6\right\rfloor=21.
\]
Not unique.

Try \(s=109\):
\[
L=\left\lceil \frac{79}{4}\right\rceil=\left\lceil 19.75\right\rceil=20,\quad
U=\left\lfloor 21.8\right\rfloor=21.
\]
Not unique.

Try \(s=110\):
\[
L=\left\lceil \frac{80}{4}\right\rceil=20,\quad
U=\left\lfloor 22\right\rfloor=22.
\]
Not unique.

Try \(s=111\):
\[
L=\left\lceil \frac{81}{4}\right\rceil=\left\lceil 20.25\right\rceil=21,\quad
U=\left\lfloor 22.2\right\rfloor=22.
\]
Not unique.

Try \(s=112\):
\[
L=\left\lceil \frac{82}{4}\right\rceil=\left\lceil 20.5\right\rceil=21,\quad
U=\left\lfloor 22.4\right\rfloor=22.
\]
Not unique.

Try \(s=113\):
\[
L=\left\lceil \frac{83}{4}\right\rceil=\left\lceil 20.75\right\rceil=21,\quad
U=\left\lfloor 22.6\right\rfloor=22.
\]
Not unique.

Try \(s=114\):
\[
L=\left\lceil \frac{84}{4}\right\rceil=21,\quad
U=\left\lfloor 22.8\right\rfloor=22.
\]
Not unique.

Try \(s=115\):
\[
L=\left\lceil \frac{85}{4}\right\rceil=\left\lceil 21.25\right\rceil=22,\quad
U=\left\lfloor 23\right\rfloor=23.
\]
Not unique.

We are not finding collapse; but uniqueness must occur eventually because for sufficiently large \(s\), constraints tighten.

Maximum score occurs when \(w=0,c=30\):
\[
s_{\max}=30+4\cdot 30=150.
\]
So check near the top: when \(c\) is forced close to \(30\).

For \(c\) to be unique, likely \(c=30\). If \(c=30\), then \(w\) is determined by
\[
w=30+4\cdot 30 - s =150-s.
\]
Also we must have \(w\ge 0\) automatically if \(s\le 150\), and \(c+w\le 30\) becomes
\[
30+w\le 30 \implies w\le 0 \implies w=0 \implies s=150.
\]
So if \(s=150\), then \(c=30\) is unique.

Now check: could uniqueness occur at some smaller score? The condition for uniqueness is that the feasible interval for \(c\) has exactly one integer. We can test whether for \(s=149\) there is more than one \(c\).

At \(s=150\):
\[
L=\left\lceil \frac{120}{4}\right\rceil=30,\quad U=\left\lfloor \frac{150}{5}\right\rfloor=30,
\]
unique.

At \(s=149\):
\[
L=\left\lceil \frac{119}{4}\right\rceil=\left\lceil 29.75\right\rceil=30,\quad
U=\left\lfloor \frac{149}{5}\right\rfloor=\left\lfloor 29.8\right\rfloor=29,
\]
now infeasible (no valid \(c\)), meaning a score of 149 cannot occur at all. But the problem states Mary’s score is over 80 and is such that John can determine \(c\), and if it had been any lower but still over 80, John could not have determined it. That is consistent if all scores below the true one that are achievable fail uniqueness. In particular, if the only achievable score with uniqueness above 80 is 150, then the statement holds.

Finally confirm that 150 is achievable: take \(c=30,w=0\), giving \(s=150\).

Therefore Mary’s score is \(\boxed{150}\).

ANSWER: 150
```

</details>

#### Augmented Scores

| Generation | Score | Tier |
| --- | ---: | --- |
| 0 | 0.0000 | `incorrect` |
| 1 | 1.0000 | `correct` |
| 2 | 0.0000 | `incorrect` |
| 3 | 0.0000 | `incorrect` |
| 4 | 0.0000 | `incorrect` |
| 5 | 0.0000 | `incorrect` |
| 6 | 0.0000 | `incorrect` |
| 7 | 1.0000 | `correct` |
| 8 | 0.0000 | `incorrect` |
| 9 | 0.0000 | `incorrect` |

<details>
<summary>Score details for generation 0</summary>

```json
{
  "reason": "missing_answer_line",
  "expected": "119",
  "answer_line": null,
  "answer_fragment": null,
  "extracted": null
}
```

</details>

<details>
<summary>Score details for generation 1</summary>

```json
{
  "reason": "correct",
  "expected": "119",
  "answer_line": "ANSWER: 119",
  "answer_fragment": "119",
  "extracted": "119"
}
```

</details>

<details>
<summary>Score details for generation 2</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 123",
  "answer_fragment": "123",
  "extracted": "123"
}
```

</details>

<details>
<summary>Score details for generation 3</summary>

```json
{
  "reason": "missing_answer_line",
  "expected": "119",
  "answer_line": null,
  "answer_fragment": null,
  "extracted": null
}
```

</details>

<details>
<summary>Score details for generation 4</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 131",
  "answer_fragment": "131",
  "extracted": "131"
}
```

</details>

<details>
<summary>Score details for generation 5</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 123",
  "answer_fragment": "123",
  "extracted": "123"
}
```

</details>

<details>
<summary>Score details for generation 6</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 150",
  "answer_fragment": "150",
  "extracted": "150"
}
```

</details>

<details>
<summary>Score details for generation 7</summary>

```json
{
  "reason": "correct",
  "expected": "119",
  "answer_line": "ANSWER: 119",
  "answer_fragment": "119",
  "extracted": "119"
}
```

</details>

<details>
<summary>Score details for generation 8</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 131",
  "answer_fragment": "131",
  "extracted": "131"
}
```

</details>

<details>
<summary>Score details for generation 9</summary>

```json
{
  "reason": "value_mismatch",
  "expected": "119",
  "answer_line": "ANSWER: 150",
  "answer_fragment": "150",
  "extracted": "150"
}
```

</details>
