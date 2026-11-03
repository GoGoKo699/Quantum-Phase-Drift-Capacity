# Few-carrier indistinguishability and capacity separation

Two stationary phase processes agree on every selected-carrier channel through three slots but require asymptotically different redundancy fractions. The common [operational model](model-and-blocking.md), [Brownian capacity theorem](brownian-capacity.md), and [reset capacity theorem](reset-capacity.md) fix the resources and rate convention used here. For the reset process, $`f_{\mathrm R}(0)=1`$ and $`f_{\mathrm R}(q)=1-p`$ for every nonzero integer $`q`$.

## 1. Exact equality for any choice of at most three slots

Consider the Brownian model with increment characteristic function

```math
f_{\mathrm B}(q)=e^{-\kappa q^2/2},
 \qquad q\in\mathbb Z,
 \qquad\text{(C1)}
```

and match the reset parameter by

```math
p=1-e^{-\kappa/2}.
 \qquad\text{(C2)}
```

Then $`f_{\mathrm B}(q)=f_{\mathrm R}(q)`$ for $`q=0,\pm1`$.
In particular both models have the same stationary one-time phase law and

```math
\mathbb E e^{i(\theta_{j+s}-\theta_j)}
  =e^{-\kappa s/2}
 \qquad\text{(C3)}
```

at every integer lag $`s\ge0`$.

The stronger statement concerns the whole quantum channel. Fix integer times
$`t_1\lt \cdots\lt t_m`$. The reduced $`m`$-carrier channel means the joint input-output CPTP map on those carriers with all other carriers ignored. The stochastic phase process is independent of every input, so ignored slots do not alter this map.

For $`x,y\in\{0,1\}^m`$, put
$`a_j=x_j-y_j\in\{-1,0,1\}`$,
$`S_k=\sum_{j=k}^{m}a_j`$, and
$`g_k=t_k-t_{k-1}`$ for $`2\le k\le m`$.
Independence of increments and the uniform initial phase give the exact multiplier

```math
\mathcal N^{(t_1,\ldots,t_m)}
    (|x\rangle\langle y|)
  =
  \mathbf1\{S_1=0\}
  \prod_{k=2}^{m} f(S_k)^{g_k}
  |x\rangle\langle y|.
 \qquad\text{(C4)}
```

If $`S_1\ne0`$, both models erase the matrix element. Otherwise,

```math
|S_k|
  =\left|\sum_{j=k}^{m}a_j\right|
  =\left|-\sum_{j=1}^{k-1}a_j\right|
  \le\min\{m-k+1,k-1\}.
 \qquad\text{(C5)}
```

For $`m\le3`$, the right side is at most one for every $`2\le k\le m`$.
All factors in (C4) therefore use only $`f(0)`$ and $`f(\pm1)`$, where the models agree. This proves

```math
\begin{gathered}
 \boxed{\mathcal B_{\kappa}^{(t_1,\ldots,t_m)}
  =\mathcal R_{\,1-e^{-\kappa/2}}^{(t_1,\ldots,t_m)}}\\
 \text{for every }m\le3
 \text{ and every }t_1\lt \cdots\lt t_m.
 \qquad\text{(C6)}
\end{gathered}
```

Equality is exact for arbitrary gaps, not an approximation restricted to adjacent carriers. It holds on every matrix unit and hence after tensoring with the identity on any passive reference. Consequently any entangled probe and final measurement on these selected carriers and that reference have identical outcome statistics.

The statement is equality of specified selected-carrier channels. Additional intervening probes, multiple passages through a noisy interaction, access to a phase record, or a different adaptive process interface are not implicit in (C6). A general claim of process-comb equality is unnecessary and is not made.

## 2. Four carriers provide an explicit diagnostic

Use four consecutive slots, and define

```math
x=0011,\qquad y=1100,\qquad
 |\psi_\pm\rangle=\frac{|x\rangle\pm|y\rangle}{\sqrt2}.
 \qquad\text{(C7)}
```

For the matrix element $`|x\rangle\langle y|`$, the suffix charges are
$`(0,1,2,1)`$. Thus its Brownian and reset multipliers are

```math
\lambda_{\mathrm B}=e^{-3\kappa},
 \qquad
 \lambda_{\mathrm R}=e^{-3\kappa/2}.
 \qquad\text{(C8)}
```

Prepare $`|\psi_+\rangle`$, transmit its four carriers once, and measure the projectors onto $`|\psi_+\rangle`$, $`|\psi_-\rangle`$, and their orthogonal complement. The complement outcome has probability zero in the ideal stated model, and

```math
\Pr_{\mathrm B/R}(\pm)
  =\frac{1\pm\lambda_{\mathrm B/R}}2.
 \qquad\text{(C9)}
```

This is a physical four-carrier preparation and measurement. One explicit implementation prepares a four-qubit GHZ state using a Hadamard and three controlled-NOT gates and then applies $`X`$ to carriers 3 and 4. Reversing this preparation circuit implements the two-state measurement, with the first measured bit distinguishing the two signs. All these are known local controls at the sender or receiver. Since both basis strings in (C7) have total excitation number two, the probe density matrix and the final measurement commute with a common phase rotation; the diagnostic requires no shared global phase reference.

The output trace distance and equal-prior single-trial success probability for this probe are

```math
\frac12\|\rho_{\mathrm R}-\rho_{\mathrm B}\|_1
  =\frac{e^{-3\kappa/2}-e^{-3\kappa}}2,
 \qquad
 P_{\mathrm{succ}}
  =\frac12+\frac{e^{-3\kappa/2}-e^{-3\kappa}}4.
 \qquad\text{(C10)}
```

The measurement in (C9), assigning $`+`$ to reset and $`-`$ to Brownian, attains this success probability. This proves strict distinguishability for every $`\kappa>0`$. It does not assert that the displayed probe optimizes discrimination over all four-carrier inputs, or that the single-trial advantage remains constant as $`\kappa\downarrow0`$.

For four arbitrary selected times, the same probe has
$`\lambda_{\mathrm B}=\exp[-\kappa(g_2+4g_3+g_4)/2]`$
and
$`\lambda_{\mathrm R}=\exp[-\kappa(g_2+g_3+g_4)/2]`$.
The consecutive-slot version already proves that the three-slot equality cannot be extended to all four-slot channels.

## 3. Consequence for asymptotic quantum communication

Combining [Theorem R](reset-capacity.md#1-model-operational-rate-and-theorem) with the [Brownian capacity theorem](brownian-capacity.md#1-main-theorem-and-explicit-bounds) gives

```math
\begin{aligned}
 1-Q_{\mathrm B}(\kappa)&=\Theta(\sqrt\kappa),\\
 1-Q_{\mathrm R}(1-e^{-\kappa/2})
   &=\Theta\!\left(\kappa\log(1/\kappa)\right).
 \end{aligned}
 \qquad\text{(C11)}
```

Both processes are stationary and mixing for every positive parameter. They have the same channels in (C6), yet their optimal redundancy fractions differ by

```math
\frac{1-Q_{\mathrm B}(\kappa)}
      {1-Q_{\mathrm R}(1-e^{-\kappa/2})}
  =\Theta\!\left(
     \frac1{\sqrt\kappa\,\log(1/\kappa)}
     \right)\longrightarrow\infty.
 \qquad\text{(C12)}
```

This compares identical carrier dimensions, slot counts, coding resources, and initial phase laws. Equality of low-order channel data supplies no equality of the entire noise process: (C8) is an explicit witness of the higher-order difference. The communication-rate separation relies on the separate Brownian all-code converse as well as the reset bounds. Neither the optimal Brownian coefficient nor the optimal reset coefficient is identified.
