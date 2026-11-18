# Discriminating phase drift from resets

[Scientific account](README.md) · [Carrier model](model-and-blocking.md) · [Few-carrier equality](indistinguishability.md)

Brownian phase drift and random resets have the same channel on every choice of up to three carrier slots. Their communication-capacity deficits have different small-noise orders. To use that distinction as a diagnostic, a receiver also needs to know how many carriers suffice to identify the noise process reliably.

## Fixed-error resource law

Fix a known Brownian increment variance $`\kappa>0`$ and the matched reset probability $`p=1-e^{-\kappa/2}`$. The two hypotheses have equal prior probability. A probe uses one qubit per consecutive slot with no feedback, phase record or repeated passage. All slots count. The receiver can perform an arbitrary joint measurement of the output and any permitted reference. The preparation and readout are ideal.

An input has **entanglement depth at most $`d`$** if it is a mixture of states that factor into groups of at most $`d`$ transmitted carriers each. A group can include a private passive reference. The partition can change across the mixture and may join nonadjacent slots. Coherent references shared across nominal groups are part of the input entanglement resource. The unrestricted comparator permits any joint probe and passive reference. This definition constrains preparation, while reception remains collective even at depth one.

For any fixed target error $`\varepsilon\in(0,1/2)`$, the minimum consecutive carrier count obeys, uniformly in integers $`d\ge1`$ as $`\kappa\downarrow0`$,

```math
N_*(\kappa,d,\varepsilon)
=\Theta_{\varepsilon}\!\left(\max\left\{
\kappa^{-1/3},\; (\kappa d)^{-1/2}\right\}\right).
```

Product probes need order $`\kappa^{-1/2}`$ slots even with a joint receiver. Depth of order $`\kappa^{-1/3}`$ suffices to attain the unrestricted order $`\kappa^{-1/3}`$. The bounds address the two calibrated noise models. Estimating the calibration and adding other sources of error are separate tasks.

## Exact four-carrier optimum

For four fixed slots, write $`g_2,g_3,g_4`$ for the successive positive gaps and put $`x=e^{-\kappa g_3/2}`$. Only one unordered pair of basis strings, $`u=0011`$ and $`v=1100`$, has equal total excitation and a suffix-charge difference of magnitude two. Its successive absolute suffix charges are $`1,2,1`$. All other matrix elements agree by equations (C4)–(C5) of the [few-carrier comparison](indistinguishability.md). Thus the reset-minus-Brownian difference acts only on the two conjugate entries of this pair with coefficient

```math
\Delta=e^{-\kappa(g_2+g_4)/2}(x-x^4).
```

For a joint probe state with a passive reference, let $`A=\rho_{uv}`$ be its off-diagonal block and $`p_u,p_v`$ the traces of the corresponding diagonal blocks. Positivity gives $`\lVert A\rVert_1\le\sqrt{p_up_v}`$ by factoring the off-diagonal block through a contraction and applying the Schatten Cauchy–Schwarz inequality. The Hermitian output difference has trace norm $`2\Delta\lVert A\rVert_1\le\Delta`$. The balanced superposition of $`u,v`$ and the sign measurement from the existing diagnostic attain equality. The optimal equal-prior success is $`1/2+\Delta/4`$, including when a passive reference is allowed. In consecutive slots the advantage is of order $`\kappa`$.

## Lower bounds

Compare both hypotheses to the same common-phase twirl $`\mathcal T`$ in which every carrier receives the first slot's uniform phase. The reset channel coincides with this twirl conditional on no reset in the internal $`N-1`$ gaps. Its output trace distance from the twirl, even with a passive reference, is at most $`1-e^{-\kappa(N-1)/2}\le\kappa(N-1)/2`$. We use half the trace norm for trace distance.

### Arbitrary inputs

Let $`n_i=|1\rangle\langle1|_i`$, $`Q=\sum_i n_i`$ and $`S_j=\sum_{i>j}n_i`$. Averaging the independent Gaussian increments factors the Brownian channel into $`\mathcal T`$ followed by the commuting channels $`\exp[-(\kappa/2)\operatorname{ad}(S_j)^2]`$, where $`\operatorname{ad}(S)(X)=[S,X]`$. After $`\mathcal T`$ only equal-$`Q`$ blocks remain. In any such block the spectral width of $`S_j`$ is at most $`w_j=\min(j,N-j)`$. Indeed, the suffix count in charge-$`q`$ ranges from $`\max(0,q-j)`$ to $`\min(q,N-j)`$. Subtracting the sector midpoint as a function of $`Q`$ therefore preserves the action on the twirled operators and gives a generator with operator norm at most $`w_j/2`$.

For a centered generator of that norm, the trace norm of its commutator on a joint carrier-reference operator is bounded by $`w_j`$ times the input norm. The Gaussian channel is a mixture of unitaries and is contractive in the same norm. Integrating its generator and telescoping the channels gives

```math
\lVert\mathcal B_\kappa-\mathcal T\rVert_\diamond
\le\frac{\kappa}{2}\sum_{j=1}^{N-1} w_j^2.
```

Adding the reset bound shows that constant trace distance requires $`\kappa N^3`$ bounded below. Equal-prior error at most $`\varepsilon`$ requires trace distance at least $`1-2\varepsilon`$ by the binary state discrimination formula.

### Depth-limited inputs

Fix a Brownian trajectory and set $`\delta_j=\theta_j-\theta_1`$ on its real lift. A pure group probe with private reference undergoes the relative unitary $`e^{iA_G}`$, where $`A_G=\sum_{j\in G}\delta_j n_j`$. With an independent copy of the spectral random variable of $`A_G`$ in this probe and $`1-\cos t\le t^2/2`$,

```math
1-|\langle e^{iA_G}\rangle|^2\le\operatorname{Var}(A_G)
\le\frac{|G|}{4}\sum_{j\in G}\delta_j^2.
```

The last step uses the triangle inequality for centered number operators applied to the probe, $`\operatorname{Var}(n_j)\le1/4`$, and Cauchy–Schwarz. For a product over groups the loss of squared overlap is at most the sum of group losses. The pure-state trace distance is the square root of this loss. Averaging by convexity and Jensen, and using $`\mathbb E\delta_j^2=\kappa(j-1)`$, bounds the trace distance to the twirl by $`\sqrt{\kappa\min(d,N)N(N-1)/8}`$. Partial trace of private purifications and averaging over mixtures preserve the bound. The real lift is valid because the physical rotations are periodic. The reset term adds at most $`\kappa(N-1)/2`$. Together these bounds force $`\kappa dN^2`$ to be bounded below for fixed error.

## Attaining the law

### Entangled input groups

For $`d\ge2`$ and $`\kappa\le1/64`$, use

```math
m=\min\{\lfloor d/2\rfloor,\lfloor\kappa^{-1/3}/2\rfloor\},
\qquad r=\left\lceil(\kappa m^3)^{-1/2}\right\rceil,
\qquad N=2mr.
```

Divide the first $`L=mr`$ slots into $`r`$ sets of $`m`$ consecutive positions. Pair each set with the corresponding set offset by $`L`$. Each resulting group carries the balanced superposition of the two patterns with all $`m`$ excitations placed in one set or the other. Measure the corresponding plus/minus basis in each group. The preparation is a product across groups. Both patterns have the same total charge, so the tests are invariant under a common phase.

Under Brownian drift the group's relative phase $`\Phi_i`$ is a centered Gaussian. Its variance follows from squaring the suffix charges, which rise from one to $`m`$, stay at $`m`$, and fall back to one. For every group this gives

```math
v=\kappa\left[m^2 L-\frac{m^3-m}{3}\right].
```

In particular $`v\le\kappa m^3r`$, $`rv\ge8/9`$, and $`rv\le(1+1/\sqrt8)^2`$, since $`\kappa m^3\le1/8`$ and $`r\ge3`$. Also $`v\le\sqrt{\kappa m^3}+\kappa m^3<1/2`$.

Conditional on a trajectory the minus outcomes are independent across disjoint groups, with probabilities $`q_i=(1-\cos\Phi_i)/2`$. The phases themselves can be correlated. Write $`X`$ for the total number of minus outcomes and $`\mu=\mathbb E X`$. Gaussian averaging gives $`\mu=r(1-e^{-v/2})/2\ge rv/8`$. The inequalities $`q_i\le\Phi_i^2/4`$ and $`\mathbb E[\Phi_i^2\Phi_j^2]\le3v^2`$ yield

```math
\mathbb E X^2\le\mu+\frac{3}{16}(rv)^2\le\mu+12\mu^2.
```

Cauchy–Schwarz applied to $`X\mathbf1_{X>0}`$ now gives $`\Pr_{\mathrm B}(X>0)\ge1/24`$. In a no-reset window the phase is common and the minus outcomes are absent. Thus the probability of a false reset-to-Brownian declaration is bounded above by the probability of any reset. Since $`N=\Theta((\kappa m)^{-1/2})`$ with $`m`$ of order $`\min(d,\kappa^{-1/3})`$, the window has the desired length.

### Product input

Use $`N=2r`$ with $`r=\lceil\kappa^{-1/2}\rceil`$ and send $`|+\rangle`$ on every slot. For each $`1\le i\le r`$, test carriers $`i,i+r`$ against the singlet. The singlet probability conditional on the path is $`(1-\cos\Phi_i)/4``, with $`\operatorname{Var}(\Phi_i)=v=\kappa r`$ under Brownian drift. These tests use disjoint pairs and commute with a common phase rotation. A common randomization of the preparation phase gives the same statistics.

Now $`\mu\ge rv/16\ge1/16`$. The conditional probabilities are bounded by $`\Phi_i^2/8`$, giving $`\mathbb E X^2\le\mu+3(rv)^2/64\le\mu+12\mu^2`$ for the singlet count. Consequently $`\Pr_{\mathrm B}(X>0)\ge1/28`$. A no-reset window has zero singlet probability.

### Fixing the error on one continuous train

Use $`b_\varepsilon`$ disjoint consecutive windows with the same preparations and measurements. Declare Brownian when any window has a minus or singlet outcome. The test in each window is insensitive to its common input phase, so its distribution depends only on increments internal to that window. These sets of increments are disjoint under Brownian drift, and the preparations and measurements factor across windows. The Brownian miss probability is at most $`(27/28)^{b_\varepsilon}`$. Choose $`b_\varepsilon`$ so this is at most $`\varepsilon`$.

Under resets a false declaration requires at least one reset among the internal gaps in the used windows. Its probability is at most $`\kappa b_\varepsilon N/2`$, which tends to zero uniformly in $`d`$ since $`N=O(\kappa^{-1/2})`$. Thus each conditional error is at most $`\varepsilon`$ for sufficiently small $`\kappa`$, with a threshold uniform in $`d`$. No restart of the phase process is used. The preparation and reception require ordinary ideal local gates and storage, including coherent buffering across the two halves at the receiver. The depth-one claim concerns the transmitted probe, while its receiver uses two-carrier tests.

These diagnostic lengths concern deciding between the two specified noise processes. The [capacity comparison](indistinguishability.md#3-consequence-for-asymptotic-quantum-communication) then tells which redundancy law applies in that model.
