# What selected-carrier channels determine about capacity

We keep the [phase-train model](model-and-blocking.md): one qubit per counted slot, a uniform initial phase, independent stationary increments, and collective encoding and decoding without a phase record. Capacity uses unit slot spacing. The diagnostic statement also applies at irregularly spaced sampling times. Every logarithm is to base two unless otherwise indicated.

## 1. Exact agreement with different capacity losses

### Theorem G1

For every integer $`r\ge1`$ and every sufficiently small $`\kappa\gt0`$, there are two stationary circle phase processes, $`\mathrm A`$ and $`\mathrm B`$, with independent increments and smooth, strictly positive increment densities at every positive time. Their complete quantum channels are identical on any choice of up to $`2r+1`$ carrier slots, including with a passive reference. The processes have different channels at $`2r+2`$ slots.

For $`\kappa r^2\le1`$, their unassisted capacities at unit slot spacing obey

```math
\begin{aligned}
c\sqrt{\kappa}
&\le 1-Q_{\mathrm A}
\le C\left[\sqrt{\kappa}+\kappa r^2\log_2\!\frac{e}{\kappa r^2}\right],\\
c\kappa^2
&\le 1-Q_{\mathrm B}
\le C\left[\kappa^2+\kappa r^2\log_2\!\frac{e}{\kappa r^2}\right].
\end{aligned}
\qquad\text{(G1)}
```

The positive constants are independent of $`\kappa`$ and $`r`$. At each fixed pair of parameters the train length tends to infinity before the small-noise limit. Thus for any integer-valued $`r=r(\kappa)`$ with

```math
r=o\!\left(\frac{\kappa^{-1/4}}{\sqrt{\log_2(1/\kappa)}}\right),
\qquad\text{(G2)}
```

$`1-Q_{\mathrm A}=\Theta(\sqrt{\kappa})`$ and $`(1-Q_{\mathrm A})/(1-Q_{\mathrm B})\longrightarrow\infty`$. Exact selected-carrier channel data at those sizes cannot determine the capacity deficit within a fixed multiplicative factor uniformly on this family.

The two processes use the same carrier dimension, cadence and coding operations. The selected-channel equality concerns one pass through those carriers. The result places no restriction on joint statistics assembled from probes on more distinct carriers.

## 2. Matching the increment harmonics

Let $`d=2r`$ and $`\theta_j=2\pi j/d`$ for $`0\le j\lt d`$. On this cyclic phase grid define the signed measure $`\sigma=\sum_{j=0}^{d-1}\sigma_j\delta_{\theta_j}`$ by

```math
\sigma_j=\frac1d\sum_{q=-r+1}^{r}(-q^2)e^{-iq\theta_j},
\qquad
\widehat{\sigma}(q)=\sum_{j=0}^{d-1}\sigma_j e^{iq\theta_j}.
\qquad\text{(G3)}
```

Fourier inversion gives $`\widehat{\sigma}(q)=-q^2`$ for $`|q|\le r`$, since the two Nyquist harmonics $`\pm r`$ have the same sampled values and multiplier. The measure is real and symmetric. Its coefficients are the Fourier second-differentiation weights on the periodic grid [Trefethen](https://doi.org/10.1137/1.9780898719598.ch3). Their signs and total mass will control the jump rate.

For $`j\ne0`$, twice differentiate

```math
\sum_{q=-r+1}^{r}e^{-iq\theta}
=e^{-i\theta/2}\,\frac{\sin(r\theta)}{\sin(\theta/2)}
```

at $`\theta=\theta_j`$. Since $`\sin(r\theta_j)=0`$ and $`(e^{-i\theta/2}/\sin(\theta/2))'=-1/[2\sin^2(\theta/2)]`$, this gives

```math
\sigma_j=-\frac{(-1)^j}{2\sin^2(\pi j/d)}.
\qquad\text{(G4)}
```

Also $`\sigma_0\lt0`$ directly from (G3). Combining the alternating signs with $`\widehat{\sigma}(0)=0`$ and $`\widehat{\sigma}(r)=-r^2`$ gives

```math
\sum_j|\sigma_j|=r^2,\qquad
\sigma=\sigma_+-\sigma_-,\qquad
\sigma_\pm(\mathbb S^1)=M:=r^2/2,
\qquad\text{(G5)}
```

where $`\sigma_\pm`$ are the positive and negative parts.

Use two compound-Poisson increments on the grid. The number of sampled jumps during an interval of length $`t`$ has mean $`t\kappa r^2/4`$ in both processes. Each jump is drawn from $`\sigma_-/M`$ for $`\mathrm A`$, and from $`\sigma_+/M`$ for $`\mathrm B`$. A draw at angle zero has no effect. Write $`P_t^-`$ and $`P_t^+`$ for the respective endpoint laws. If $`G_v`$ denotes the wrapped centered Gaussian with variance parameter $`v`$, the increment laws are

```math
\mu_{\mathrm A,t}=G_{t(\kappa+\kappa^4)}*P^-_t,
\qquad
\mu_{\mathrm B,t}=G_{t\kappa^4}*P^+_t.
\qquad\text{(G6)}
```

Here the Brownian motions and jump processes are independent and each initial phase is uniform. For each fixed $`\kappa,r`$, these laws are convolution semigroups. Each positive-time law has a smooth strictly positive density because it is a finite mixture of shifted positive-time wrapped Gaussian densities. A fixed positive-time kernel on the circle therefore has a strictly positive minimum relative to Haar measure. Iterating its uniform minorization gives exponential convergence in total variation to the uniform stationary phase, with a rate that can depend on $`\kappa,r`$.

Summing over the Poisson count gives the increment characteristic functions

```math
\widehat{P^\pm_t}(q)
=\exp\!\left[\frac{t\kappa}{2}
  \bigl(\widehat{\sigma_\pm}(q)-M\bigr)\right].
\qquad\text{(G7)}
```

In particular they are positive real at every integer $`q`$ by symmetry of the jump distributions. The ratio of the two jump characteristic functions is $`\widehat{P_t^+}(q)/\widehat{P_t^-}(q)=\exp(t\kappa\widehat{\sigma}(q)/2)`$. For $`|q|\le r`$, this is exactly the extra Brownian multiplier $`e^{-t\kappa q^2/2}`$ in process $`\mathrm A`$. Hence

```math
\widehat\mu_{\mathrm A,t}(q)=\widehat\mu_{\mathrm B,t}(q)
\qquad(|q|\le r,\ t\ge0).
\qquad\text{(G8)}
```

## 3. The first differing carrier count

For $`m`$ selected carriers at times $`t_1\lt\cdots\lt t_m`$, the matrix-unit multiplier in [(C4)](indistinguishability.md#1-exact-equality-for-any-choice-of-at-most-three-slots) uses the increment characteristic function at each gap duration $`t_j-t_{j-1}`$. The uniform initial phase imposes equal weights on the two strings. Equation (C5) bounds every surviving suffix charge in absolute value by $`\lfloor m/2\rfloor`$. Thus (G8) yields equality on all matrix units whenever $`m\le2r+1`$. The equality remains valid when the channels act on part of a joint state with a reference.

The grid charge $`r+1`$ aliases to $`1-r`$, so $`\widehat{\sigma}(r+1)=-(r-1)^2`$. At the first unmatched harmonic, (G6) and (G7) give

```math
\frac{\widehat\mu_{\mathrm A,t}(r+1)}
     {\widehat\mu_{\mathrm B,t}(r+1)}
=e^{-2t\kappa r}
\qquad(t\gt0).
\qquad\text{(G9)}
```

For any selected $`2r+2`$ increasing times, the balanced strings $`x=0^{r+1}1^{r+1}`$ and $`y=1^{r+1}0^{r+1}`$ give a suffix charge of $`r+1`$ at the middle gap and charges no larger than $`r`$ at all others. If $`\lambda_{\mathrm A}`$ and $`\lambda_{\mathrm B}`$ are their two coherence multipliers, then

```math
\lambda_{\mathrm A}
=e^{-2\kappa r(t_{r+2}-t_{r+1})}\lambda_{\mathrm B},
\qquad \lambda_{\mathrm B}\gt0.
\qquad\text{(G10)}
```

Prepare the equal coherent superposition of $`x,y`$ and measure in the two sign states, as in the [four-carrier diagnostic](indistinguishability.md#2-four-carriers-provide-an-explicit-diagnostic). With equal priors the sign outcome attains success probability $`1/2+(\lambda_{\mathrm B}-\lambda_{\mathrm A})/4`$ on this probe. At unit gaps in the regime (G2), this advantage is of order $`\kappa r`$. Indeed, each jump exponent in (G7) lies between $`-t\kappa r^2/2`$ and zero, and the Gaussian exponents have the same order for the witness charges at unit gap. Across $`2r+1`$ gaps the total exponent is $`O(\kappa r^3)=o(1)`$. This establishes strict detection at the stated count. The single-trial advantage still tends to zero in this regime.

## 4. Bounding the capacity deficits

Write $`P^\pm=P^\pm_1`$ and let $`\lambda=\kappa r^2/4`$ be the unit-time Poisson mean. The individual jump distributions have a Shannon entropy bounded by a universal constant. To see this, write $`s_j=\min(j,d-j)`$. For $`j\ne0`$ equation (G4) gives the mass bound

```math
\frac{|\sigma_j|}{M}
=\frac{1}{r^2\sin^2(\pi j/d)}\le\frac1{s_j^2}.
\qquad\text{(G11)}
```

For either law compare its entropy to the cross entropy with grid weights proportional to $`(1+s_j)^{-2}`$. Their normalizing sum is uniformly bounded, and the expectation of $`\log_2(1+s_j)`$ under either jump law is bounded by $`2\sum_{s\ge1}s^{-2}\log_2(1+s)`$. The atom at zero contributes zero to this expectation. Thus the entropy of the entire sequence of draws, grouped by the Poisson number of jumps $`K`$, bounds the entropy of the endpoint by

```math
H(P^\pm)\le H(K)+C_0\lambda
\le g(\lambda)+C_0\lambda
\le C_1\lambda\log_2(e/\lambda)
\qquad(0\lt\lambda\le1/4).
\qquad\text{(G12)}
```

The middle inequality uses the geometric distribution, which maximizes Shannon entropy among nonnegative integer laws of given mean. Its entropy $`g`$ is given by [(B1)](brownian-capacity.md#1-main-theorem-and-explicit-bounds).

To combine this bound with the Brownian result, consider any grid law $`P`$ convolved into Brownian increments of variance $`v`$. Over an $`n`$-carrier train the grid increments implement an independent random diagonal-unitary channel with deterministic phase zero at the first carrier. The following $`n-1`$ grid increments are independent with law $`P`$. Composing it after the Brownian channel gives exactly the stationary phase channel for $`G_v*P`$, since the Brownian channel supplies the initial uniform phase. Hence

```math
Q(G_v*P)\le Q_{\mathrm B}(v).
\qquad\text{(G13)}
```

For the reverse rate bound, use the maximally mixed input on a finite block. The Brownian and grid dephasing dilations attach one environment state apiece to each computational basis string. The two environment marginals of the composed channel are therefore the respective marginals on the same uniform input. Their joint entropy is bounded by the sum of their entropies. The Brownian marginal entropy is at most $`B_n(v)`$ by [(B11)](brownian-capacity.md#finite-inner-block-achievable-bound). In a dilation of the grid channel, dephasing the environment in the random-unitary label basis gives the distribution of the $`n-1`$ independent increments. Its entropy is $`(n-1)H(P)`$, an upper bound on the grid marginal entropy before dephasing. The receiver output is maximally mixed, so

```math
I_c(2^{-n}I,\mathcal N_n(G_v*P))
\ge n-B_n(v)-(n-1)H(P).
\qquad\text{(G14)}
```

Apply [exact charge blocking and coding](model-and-blocking.md#5-exact-factorization-over-coding-blocks) at each fixed $`n`$, then take $`n\to\infty`$ as in the Brownian entropy bound. This gives $`1-Q(G_v*P)\le h(v)+H(P)`$, with $`h(v)=O(\sqrt v)`$ as $`v\downarrow0`$. Together with (G13) and the Brownian converse (B5), the capacity deficit lies between $`c_0\sqrt v`$ and $`C_2\sqrt v+H(P)`$ at small $`v\gt0`$. Substituting $`(v,P)=(\kappa+\kappa^4,P^-)`$ and $`(v,P)=(\kappa^4,P^+)`$ proves (G1). In (G2) the term $`\kappa r^2\log_2(e/(\kappa r^2))`$ is $`o(\sqrt\kappa)`$. Both deficits are strictly positive.

## 5. An absolute capacity certificate from a finite channel

### Theorem G2

For any increment law in the [phase-train model](model-and-blocking.md), let $`a_n=\max_\rho I_c(\rho,\mathcal N_n)`$. Then for every block size $`n\ge1`$,

```math
\frac{a_n}{n}\le Q\le\frac{a_n+\log_2(n+1)}{n}.
\qquad\text{(G15)}
```

In particular, two laws with identical channels on $`n`$ consecutive carriers have capacities that differ by at most $`\log_2(n+1)/n`$. This is an interval for the asymptotic capacity derived from a fully specified finite channel. It requires an optimization over that channel's inputs.

The lower bound is [(M17)](model-and-blocking.md#6-consequence-for-coding). For the upper bound, divide a train of length $`N=bn+s`$, $`0\le s\lt n`$, into blocks of size $`n`$ and a possible remainder of size $`s`$. The proof of [Proposition M1](model-and-blocking.md#proposition-m1) applies also to these unequal lengths. The diagonal phase twirls commute with the train channel. Placing them at the output produces $`\mathcal N_n^{\otimes b}\otimes\mathcal N_s`$, with the remainder factor omitted at $`s=0`$.

For any input with reference $`R`$, implement the output twirls as independent uniform random phase rotations using [(M12)](model-and-blocking.md#4-a-finite-phase-grid-implements-the-exact-charge-twirl). Retain the tuple $`K`$ of phase choices as a classical register. Given $`K`$, the rotations are invertible. If $`B`$ is the original output and $`B'`$ the rotated output, then $`I(R\rangle B'K)=I(R\rangle B)`$. Discarding the key reduces coherent information by

```math
\begin{aligned}
I(R\rangle B'K)-I(R\rangle B')
&=I(R:K\mid B')\\
&=S(K\mid B')-S(K\mid RB')\\
&\le H(K)
=b\log_2(n+1)+\log_2(s+1).
\end{aligned}
\qquad\text{(G16)}
```

The inequality uses nonnegative entropy of a classical register conditioned on a quantum system and $`S(K\mid B')\le H(K)`$. Each finite phase-train channel is generalized dephasing and therefore degradable. Its maximized coherent information adds under tensor products by [(B18)](brownian-capacity.md#22-additivity-of-maximized-coherent-information-for-degradable-factors). Taking the supremum over purified inputs gives

```math
a_N\le b\,a_n+a_s+b\log_2(n+1)+\log_2(s+1),
\qquad\text{(G17)}
```

where $`a_0=0`$ and $`a_s\le s`$. The [finite-code converse](brownian-capacity.md#23-a-finite-code-bound-for-arbitrary-cptp-encoders) bounds the rate of arbitrary encoders and decoders at vanishing error by the asymptotic $`a_N/N`$. Taking $`N\to\infty`$ at fixed $`n`$ proves (G15).

Theorems G1 and G2 describe two different accuracy criteria. Selected-carrier channel data determine capacity to a uniform additive tolerance that vanishes with block size. A small interval in absolute capacity can still include deficits that differ by a large factor near capacity one. The tight number of carriers needed to resolve the deficit across the full increment-law class remains open.

## Application to timestamped entanglement

At $r=1$, the grid contains only the angles zero and $\pi$. This gives a Brownian law and a law with weak Brownian smoothing and rare $\pi$ jumps. [Timestamped entanglement](timestamped-entanglement.md) applies the same harmonic match to raw entangled links sampled at Poisson times and gives the resulting distillation-rate separation.

## Prior results used here

The matched low-carrier mechanism starts from the existing [three-slot comparison](indistinguishability.md). The jump construction uses a standard Fourier differentiation formula, and the capacity proof uses the existing Brownian theorem, exact charge twirl and standard generalized-dephasing additivity. Channel estimation from pooled measurements of a train, including [Pfister et al.](https://arxiv.org/abs/1611.05411), can access joint statistics beyond the selected-carrier marginals considered here. The [related-work discussion](../references/related-work.md) gives the scope of prior capacity and spectroscopy results.
