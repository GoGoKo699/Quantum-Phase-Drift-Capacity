# Quantum capacity under rare phase resets

This account uses the [carrier model and capacity definition](model-and-blocking.md): one qubit per counted slot, an unknown uniform initial phase, and collective encoding and decoding without a noise record. All logarithms and entropies are in bits unless $`\ln`$ is written explicitly. The comparison with Brownian drift is developed in [indistinguishability and separation](indistinguishability.md).

## 1. Model, operational rate, and theorem

Let $`p\in(0,1)`$. Independently at every step, choose a phase increment equal to zero with probability $`1-p`$, and uniformly distributed on the circle with probability $`p`$. The phase process is stationary because its initial phase is uniform. Its one-step characteristic function is

```math
f_{\mathrm R}(q)=
 \begin{cases}
 1,&q=0,\\
 1-p,&q\in\mathbb Z\setminus\{0\}.
 \end{cases}
 \qquad\text{(R1)}
```

Equivalently, each transition preserves the current phase with probability $`1-p`$, and replaces it by an independent uniform phase with probability $`p`$. Its $`s`$-step transition kernel is

```math
P^s(\theta,d\phi)
  =(1-p)^s\delta_\theta(d\phi)
   +[1-(1-p)^s]\,\frac{d\phi}{2\pi}.
 \qquad\text{(R2)}
```

Thus the model is mixing for every fixed $`p>0`$, and every nonzero phase harmonic decays. It has no conserved nonzero harmonic.

Let $`\mathcal R^{(n)}_p`$ denote the averaged channel on the first $`n`$ carriers. An $`n`$-slot code consists of a CPTP encoder
$`\mathcal E_n:\mathcal B(\mathbb C^{M_n})\to\mathcal B((\mathbb C^2)^{\otimes n})`$
and a CPTP decoder in the reverse direction. Its entanglement fidelity is

```math
\begin{aligned}
F_{e,n}&=\langle\Phi_{M_n}|
\bigl(\mathrm{id}\otimes
\mathcal D_n\circ\mathcal R^{(n)}_p\circ\mathcal E_n\bigr)\\
&\quad (|\Phi_{M_n}\rangle\langle\Phi_{M_n}|)
|\Phi_{M_n}\rangle.
\end{aligned}
\qquad\text{(R3)}
```

The unassisted capacity $`Q_{\mathrm R}(p)`$ is the supremum of asymptotic rates
$`n^{-1}\log_2 M_n`$ attainable with $`F_{e,n}\to1`$. Encoding and decoding may act collectively over all carriers and use local ancillas. The actual communication protocol receives neither the phase trajectory nor the reset locations. Every carrier slot counts in the rate; no waiting slots, phase-reference channel, preshared entanglement, or feedback channel are provided.

Define, for positive integers $`\ell`$,

```math
\begin{aligned}
 a(\ell)&=H\!\left(\mathrm{Bin}(\ell,\tfrac12)\right),\\
 b(\ell)&=\log_2\binom{\ell}{\lfloor\ell/2\rfloor},\\
 d(\ell)&=\ell-b(\ell).
 \end{aligned}
 \qquad\text{(R4)}
```

Let $`G`$ have the geometric distribution
$`\Pr(G=\ell)=p(1-p)^{\ell-1}`$, $`\ell\ge1`$.

**Theorem R.** For every $`0\lt p\lt 1`$,

```math
\begin{aligned}
\max\{0,\;1-h_2(p)-p\,\mathbb E a(G)\}
&\le Q_{\mathrm R}(p)\\
&\le p\,\mathbb E b(G)\\
&=1-p\,\mathbb E d(G).
\end{aligned}
\qquad\text{(R5)}
```

Moreover, for every rate strictly above $`r(p):=p\mathbb E b(G)`$, the entanglement fidelity tends to zero for every sequence of codes. This decay statement concerns the explicit upper-bound threshold $`r(p)`$; we do not claim that $`r(p)`$ is the exact reset capacity.

As $`p\downarrow0`$, the theorem yields

```math
\begin{aligned}
\frac p2\log_2\frac1p-O(p)
&\le 1-Q_{\mathrm R}(p)\\
&\le \frac{3p}{2}\log_2\frac1p+O(p),
\end{aligned}
\qquad\text{(R6)}
```

and hence $`1-Q_{\mathrm R}(p)=\Theta(p\log(1/p))`$. The constants multiplying the leading logarithm in these two bounds are not asserted to coincide.

## 2. Conditional channels and their sector ranks

On an $`n`$-slot train, let
$`R=(R_2,\ldots,R_n)`$ record the $`n-1`$ interior reset indicators. The reset at or before the first carrier is absorbed into the uniform $`\theta_1`$. Given $`R`$, the train splits into consecutive segments of positive lengths
$`\ell_1,\ldots,\ell_K`$, with $`\sum_s\ell_s=n`$.

Conditional on $`R`$, the absolute phases of the segments are independent and uniform. To see independence, write the first phase as a uniform variable $`\alpha_1`$, and each subsequent segment phase as $`\alpha_s=\alpha_{s-1}+\eta_s`$, where the $`\eta_s`$ are independent uniform circle variables. The triangular change of variables from $`(\alpha_1,\eta_2,\ldots,\eta_K)`$ to $`(\alpha_1,\ldots,\alpha_K)`$ preserves product Haar measure.

For $`\ell`$ carriers define the collective phase twirl

```math
\begin{aligned}
\mathcal T_\ell(\rho)
&=\int_0^{2\pi}
U(\phi)^{\otimes\ell}\rho U(\phi)^{\dagger\otimes\ell}
\frac{d\phi}{2\pi}\\
&=\sum_{w=0}^{\ell}P_{\ell,w}\rho P_{\ell,w},
\end{aligned}
\qquad\text{(R7)}
```

where $`P_{\ell,w}`$ projects onto computational strings of Hamming weight $`w`$.
Its rank is $`\binom{\ell}{w}`$. Conditional on $`R`$, the channel is

```math
\begin{aligned}
\mathcal T_R&=\bigotimes_{s=1}^{K}\mathcal T_{\ell_s}
=\sum_{\mathbf w}P_{R,\mathbf w}\,\cdot\,P_{R,\mathbf w},\\
P_{R,\mathbf w}&=\bigotimes_s P_{\ell_s,w_s}.
\end{aligned}
\qquad\text{(R8)}
```

Every projector in this Kraus representation has rank at most

```math
\begin{aligned}
D_R&:=\prod_{s=1}^{K}\binom{\ell_s}{\lfloor\ell_s/2\rfloor},\\
\log_2 D_R&=\sum_{s=1}^{K}b(\ell_s).
\end{aligned}
\qquad\text{(R9)}
```

The collective-twirl/charge-sector structure is standard reference-frame physics; the subsequent treatment of random segment locations is specific to the present reset comparison. See the contextual references [BRS](../references/related-work.md#brs) and [Z](../references/related-work.md#z). Equations (R7)–(R9) also provide the complete finite-dimensional derivation needed here.

## 3. Achievability: a coherent reset flag and an entropy upper bound

The conditional twirl has an isometry

```math
V_R|x\rangle=|x\rangle\,|\mathbf w_R(x)\rangle,
 \qquad\text{(R10)}
```

where $`\mathbf w_R(x)`$ lists the Hamming weights of the restrictions of $`x`$ to all segments. Padding the environmental spaces to a common finite dimension, an isometry for the actual unflagged reset channel is

```math
\begin{aligned}
V|x\rangle&=|x\rangle\,|e_x\rangle,\\
|e_x\rangle&=\sum_R\sqrt{\Pr(R)}\,|R\rangle|\mathbf w_R(x)\rangle.
\end{aligned}
\qquad\text{(R11)}
```

Indeed, the Gram matrix of the environmental vectors is
$`\langle e_y|e_x\rangle =\sum_R\Pr(R)\,\mathbf1\lbrace \mathbf w_R(x)=\mathbf w_R(y)\rbrace `$,
which is the Schur multiplier of the mixture of the conditional twirls.

Use the maximally mixed input $`\tau_n=I/2^n`$. Its complementary output is

```math
\omega_{E,n}=2^{-n}\sum_x|e_x\rangle\langle e_x|.
 \qquad\text{(R12)}
```

In general, $`\omega_{E,n}`$ contains coherence between distinct reset records. It must not be replaced by a classical mixture without an inequality. Apply a pinching $`\Delta_R`$ in the reset-record basis. Pinching is an average of unitaries, so entropy concavity gives
$`S(\omega_{E,n})\le S(\Delta_R\omega_{E,n})`$. The latter state is block diagonal:

```math
\begin{aligned}
\Delta_R\omega_{E,n}
&=\sum_R\Pr(R)\,|R\rangle\langle R|\\
&\quad\otimes\left[
\bigotimes_{s=1}^{K}\sum_{w=0}^{\ell_s}
2^{-\ell_s}\binom{\ell_s}{w}|w\rangle\langle w|
\right].
\end{aligned}
\qquad\text{(R13)}
```

Consequently,

```math
S(\omega_{E,n})
 \le (n-1)h_2(p)
       +\mathbb E_R\sum_{s=1}^{K}a(\ell_s).
 \qquad\text{(R14)}
```

No reset record is available to the actual encoder or decoder in this construction. The flag and its pinching are solely a mathematical dilation and an entropy bound.

The reset channel preserves $`\tau_n`$, so the coherent information at this input is
$`I_c(\tau_n,\mathcal R^{(n)}_p)=n-S(\omega_{E,n})`$.
To make this quantity operational without assuming a general memory-channel coding formula, independently twirl the total charge of each consecutive fixed $`n`$-slot block before transmission. Such a twirl is exact with the $`n+1`$ phases
$`2\pi j/(n+1)`$, $`0\le j\le n`$, and can use unrecorded local randomness.

The [exact block-factorization lemma](model-and-blocking.md#5-exact-factorization-over-coding-blocks) gives

```math
\mathcal R^{(kn)}_p\circ\mathcal T_n^{\otimes k}
   =(\mathcal R^{(n)}_p)^{\otimes k}.
 \qquad\text{(R15)}
```

For completeness, a matrix element surviving the left-hand twirls has zero ket-minus-bra total charge separately in every block. Every suffix charge crossing a block boundary is then zero, and every interior suffix charge depends only on the same block. Independence of phase increments factors the multiplier exactly into the standalone $`n`$-slot multipliers. If a block has nonzero total charge, both sides vanish.

The ordinary finite-dimensional quantum coding theorem [D](../references/related-work.md#d) can therefore be applied to repeated copies of $`\mathcal R^{(n)}_p`$. The preprocessing in (R15) is an allowed part of the encoder; it consumes no additional physical slots and does not reset the noise. A remaining tail of fewer than $`n`$ carriers can be prepared in computational-basis states and discarded, with every such slot still counted; its rate cost vanishes at fixed block size. Taking $`k\to\infty`$ at each fixed $`n,p`$ and then optimizing $`n`$ shows

```math
Q_{\mathrm R}(p)
 \ge \sup_n\frac{n-S(\omega_{E,n})}{n}.
 \qquad\text{(R16)}
```

The renewal estimate below gives

```math
\lim_{n\to\infty}\frac1n
   \mathbb E_R\sum_s a(\ell_s)
 =p\,\mathbb E a(G).
 \qquad\text{(R17)}
```

Together, (R14)–(R17) prove the lower bound in (R5). Zero is an independent trivial achievable rate if the displayed coherent-information estimate is negative.

## 4. A finite-length converse for arbitrary CPTP encoders

Enhance the physical channel by giving its input-independent reset pattern $`R`$ to the receiver. The receiver may choose a different decoder for each pattern. Any code for the original channel is a code for this enhanced channel after ignoring the flag.

Fix $`R`$. Let $`A_\alpha:\mathbb C^M\to(\mathbb C^2)^{\otimes n}`$ be the Kraus operators of an arbitrary CPTP encoder and let $`B_{\beta,R}`$ be the Kraus operators of a decoder allowed to depend on $`R`$. Applying the encoder, conditional channel (R8), and decoder to half of $`|\Phi_M\rangle`$ gives a decomposition into unnormalized pure branches

```math
|\psi_{\alpha,\mathbf w,\beta,R}\rangle
 =\bigl(I\otimes
  B_{\beta,R}P_{R,\mathbf w}A_\alpha\bigr)|\Phi_M\rangle.
 \qquad\text{(R18)}
```

Every branch has Schmidt rank at most
$`\mathrm{rank}(P_{R,\mathbf w})\le D_R`$.
This remains true with mixed local ancillas, discarded encoder environments, or a nonisometric encoder, since all are included by a Kraus representation. Decoder operations act on one side of the reference–receiver partition and cannot increase the branch Schmidt rank. The normalized decoded state thus has Schmidt number at most $`\min\lbrace M,D_R\rbrace `$.

For a normalized pure state of Schmidt rank at most $`D`$, its overlap with an $`M`$-dimensional maximally entangled state is at most $`D/M`$. One direct proof writes the state's coefficient matrix as $`C`$: $`\|C\|_F=1`$, $`\mathrm{rank}\,C\le D`$, and
$`|\mathrm{Tr}\,C|^2/M\le\|C\|_*^2/M\le D/M`$.
Convexity extends the same estimate to every mixed state of Schmidt number at most $`D`$. This standard singlet-fraction inequality is Lemma 1 of [TH](../references/related-work.md#th); our branch argument specifies why it applies to unrestricted encoders here.

The conditional fidelity and its average therefore obey

```math
\begin{aligned}
&F_e(R)\le\min\!\left\{1,\frac{D_R}{M}\right\},\\
&\boxed{\displaystyle F_e\le\mathbb E_R
\min\!\left\{1,\frac{D_R}{M}\right\}.}
\end{aligned}
\qquad\text{(R19)}
```

This bound is finite length and requires no assumption about uniform code input, coherent-information optimality, or a memory-channel coding theorem.

At each fixed $`p>0`$, the renewal calculation below gives

```math
\begin{aligned}
&\frac{\log_2 D_R}{n}\longrightarrow
r(p):=p\,\mathbb E b(G)\\
&\quad\text{almost surely, hence in probability}.
\end{aligned}
\qquad\text{(R20)}
```

If $`\liminf_n n^{-1}\log_2 M_n>r(p)`$, choose $`\eta>0`$ such that
$`M_n\ge2^{n[r(p)+2\eta]}`$ for sufficiently large $`n`$. Equation (R19) implies

```math
F_{e,n}\le
  \Pr\!\left\{\log_2D_R>n[r(p)+\eta]\right\}
  +2^{-n\eta}\longrightarrow0.
 \qquad\text{(R21)}
```

This proves $`Q_{\mathrm R}(p)\le r(p)`$ and the stated decay above that explicit threshold. The reset record is a converse aid only; the actual code is not supplied with it.

## 5. Renewal averages, boundary segments, and small-noise estimates

Here the capacity limit is always $`n\to\infty`$ at fixed $`p>0`$. Small-$`p`$ asymptotics are taken afterwards.

### 5.1 A boundary-safe renewal lemma

Generate independent $`G_1,G_2,\ldots`$ with the geometric law of $`G`$, put
$`S_k=\sum_{i=1}^{k}G_i`$, and let
$`K_n=\min\lbrace k:S_k\ge n\rbrace `$.
The segment lengths observed in the first $`n`$ slots are

```math
G_1,\ldots,G_{K_n-1},\quad A_n:=n-S_{K_n-1}.
 \qquad\text{(R22)}
```

Thus the final segment is censored; it is not incorrectly counted as a complete geometric segment. The first observed segment has a geometric residual length because resets have an independent, constant hazard after every slot.

Let $`f:\mathbb N\to[0,\infty)`$ satisfy $`f(\ell)\le\ell`$. The strong law gives
$`K_n/n\to1/\mathbb EG=p`$ and
$`(K_n-1)^{-1}\sum_{i=1}^{K_n-1}f(G_i)\to\mathbb Ef(G)`$.
The last reward is negligible. In fact $`K_n\le n`$, $`A_n\le G_{K_n}`$, and

```math
\Pr\!\left\{\max_{1\le i\le n}G_i>C\ln n\right\}
 \le n(1-p)^{\lfloor C\ln n\rfloor}.
 \qquad\text{(R23)}
```

For a sufficiently large fixed $`C=C(p)`$, this is summable in $`n`$; Borel–Cantelli gives $`A_n=O(\ln n)`$ almost surely. Hence

```math
\frac1n
 \left[\sum_{i=1}^{K_n-1}f(G_i)+f(A_n)\right]
 \longrightarrow p\,\mathbb Ef(G)
 \quad\text{almost surely}.
 \qquad\text{(R24)}
```

The expression lies in $`[0,1]`$, so bounded convergence also gives convergence of expectations. Each of $`a,b,d`$ in (R4) lies between zero and $`\ell`$, and therefore (R24) supplies every renewal limit used above. The constants in the boundary argument depend on fixed $`p`$; no joint uniform finite-$`n`$, small-$`p`$ estimate is claimed.

### 5.2 Entropy and dimension of a charge sector

Stirling's bounds, separately for even and odd $`\ell`$, imply

```math
d(\ell)=\tfrac12\log_2\ell+O(1),
 \qquad\ell\ge1,
 \qquad\text{(R25)}
```

with an absolute uniform $`O(1)`$ constant.

The binomial entropy obeys

```math
d(\ell)\le a(\ell)
 \le \frac12\log_2\!\left[
     2\pi e\left(\frac{\ell}{4}+\frac1{12}\right)
     \right].
 \qquad\text{(R26)}
```

The lower bound follows because Shannon entropy is at least min-entropy and the largest binomial mass is
$`2^{-\ell}\binom{\ell}{\lfloor\ell/2\rfloor}`$.
For the upper bound, add an independent uniform variable on $`[-1/2,1/2)`$ to the integer-valued binomial variable. Its differential entropy equals the binomial Shannon entropy, while its variance is $`\ell/4+1/12`$; Gaussian maximum entropy gives (R26). Thus

```math
a(\ell)=\tfrac12\log_2\ell+O(1)
 \quad\text{uniformly for }\ell\ge1.
 \qquad\text{(R27)}
```

The logarithm of a geometric length has the elementary bounds

```math
\log_2(1/p)-\frac1{\ln2}
 \ \le\ \mathbb E\log_2G 
 \le\ \log_2(1/p).
 \qquad\text{(R28)}
```

The upper bound is Jensen's inequality. For the lower bound, use
$`\Pr(pG\lt z)\le z`$ for $`0\lt z\le1`$ to obtain

```math
\mathbb E[-\ln(pG)]_+
  =\int_0^\infty\Pr(pG\lt e^{-t})\,dt
  \le1.
 \qquad\text{(R29)}
```

Equations (R25), (R27), and (R28), together with
$`h_2(p)=p\log_2(1/p)+O(p)`$, prove (R6).
