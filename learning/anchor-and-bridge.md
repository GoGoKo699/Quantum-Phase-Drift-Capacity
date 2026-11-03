# From Preskill to phase-drift capacity

A sender wants to transmit an unknown quantum state through a phase that drifts between successive carriers. Each individual qubit sees a completely unknown phase, but nearby carriers share enough of that uncertainty to preserve relative information. The question is how efficiently a long train can use those correlations, and whether experiments on a few carriers reveal the resulting communication cost.

This guide connects the selected educational source to the [scientific account](../science/README.md). The [30-milestone map](milestones.md) organizes the understanding targets; the proof pages remain the authoritative statements.

## 1. Selected source and focused route

The single educational anchor is **John Preskill, *Quantum Information*, Chapter 10: *Quantum Shannon Theory*, updated June 2025**. Use the [official author-hosted PDF](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf). The links below open relevant parts of that version. Page ranges refer to the chapter’s printed numbering.

| Preskill sections | Printed pages | Connection to this project |
|---|---:|---|
| [10.1.1–10.1.2](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=8) | 2–6 | Classical entropy, correlations, and logarithmic segment costs. |
| [10.2.1–10.2.4](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=21) | 15–20 | Entropy inequalities behind pinching, subadditivity, and information processing. |
| [10.6.6](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=56) | 50–51 | Measuring and preparing as a way to recognize the complementary channel’s structure. |
| [10.7.1–10.7.2](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=57) | 51–56 | Coherent information, recoverability, and capacity converses. |
| [10.7.3](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=62) | 56–58 | Degradability and additivity for the finite channels used here. |
| [10.9.4](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=81) | 75–76 | The unassisted coding step after independent blocks have been obtained. |

These sections provide the information-theoretic framework. The phase-process identities, Gaussian environment estimate, Brownian-bridge converse, and reset renewal argument are supplied by this repository. The [primary research references](../references/related-work.md) document their separate mathematical ingredients and antecedents.

## 2. Translate notation and resources

| In the anchor | In this repository | Meaning to preserve |
|---|---|---|
| Quantum entropy written as $H$ | Quantum entropy $S$; classical entropy $H$ | All are in bits. Binary entropy is $h_2$. |
| Reference $R$, input $A$, output $B$, environment $E$ | The same system roles | A reference tests preservation of entanglement; it is not preshared assistance. |
| Input-dependent coherent information | $I_c(\rho,\mathcal M)=S(\mathcal M(\rho))-S(\mathcal M^c(\rho))$ | The sign is receiver entropy minus environment entropy. |
| Optimized coherent information $Q_1(\mathcal M)$ | $J(\mathcal M)=\max_\rho I_c(\rho,\mathcal M)$ | An optimization for a finite channel; its operational use still requires a coding argument. |
| Repeated independent uses of one channel | $b$ independent uses of an $n$-carrier block channel | Each block costs $n$ physical slots, so block rates must be divided by $n$. |

The temporal notation is specific to the project. Carrier $j$ acquires phase $\theta_j$, and the increments $\xi_j$ are independent. The phases themselves are correlated because each contains earlier increments. Brownian increments have variance $\kappa$; resets occur with probability $p$ per transition. These are different parameters from any similarly named example in the source.

The [operational definition](../science/model-and-blocking.md#2-operational-entanglement-transmission-capacity) permits arbitrary collective CPTP encoders and decoders, including local ancillas and discarded local systems. Every transmitted qubit counts, including a pilot or dummy. The parties know the noise law but receive neither its phase trajectory nor a reset record. A mathematical environment used to prove a bound is not an additional communication resource.

## 3. A complete two-carrier example

Encode one logical qubit in the weight-one subspace:

```math
|0\rangle_L=|01\rangle,\qquad
|1\rangle_L=|10\rangle.
```

For an input $\alpha|0\rangle+\beta|1\rangle$, prepare an ancillary qubit in $|1\rangle$ and apply a controlled-NOT from the input to the ancilla. This produces $\alpha|01\rangle+\beta|10\rangle$. Transmit both carriers in consecutive slots. Their state, for a particular phase realization, becomes

```math
\alpha e^{i\theta_2}|01\rangle
+\beta e^{i\theta_1}|10\rangle
=e^{i\theta_1}
\left(\alpha e^{i\xi_2}|01\rangle+\beta|10\rangle\right).
```

The unknown common phase appears only as a global factor. The relative phase is the single increment $\xi_2$. At the receiver, applying the same controlled-NOT decodes the first qubit and returns the second to $|1\rangle$, which can be discarded.

For both noise laws considered here, $\lambda:=\mathbb E e^{i\xi_2}$ is real. Averaging and decoding therefore give

```math
\rho_L^{\mathrm{out}}=
\begin{pmatrix}
|\alpha|^2&\lambda\alpha\beta^*\\
\lambda\alpha^*\beta&|\beta|^2
\end{pmatrix},
\qquad
\lambda_{\mathrm B}=e^{-\kappa/2},\quad
\lambda_{\mathrm R}=1-p.
```

Equivalently, this logical channel applies $Z$ with probability $\eta=(1-\lambda)/2$ and the identity with probability $1-\eta$. Its entanglement fidelity is $(1+\lambda)/2$: sending half of a maximally entangled pair preserves the pair in the identity branch, while the $Z$ branch produces an orthogonal Bell state. This calculation includes reference-entangled inputs.

A directly observable check prepares the logical plus state $(|01\rangle+|10\rangle)/\sqrt2$. Measuring the decoded qubit in the $X$ basis gives probabilities $(1+\lambda)/2$ and $(1-\lambda)/2$. Both carriers were used once and counted. The logical preparation and measurement are invariant under a common phase rotation.

At zero increment noise, the encoding transmits one qubit perfectly through two slots. At positive noise, the unknown increment still dephases it. This example explains how correlations preserve quantum information and why matching $p=1-e^{-\kappa/2}$ makes the two models look identical to this experiment. Its fixed one-qubit-per-pair budget also shows why longer collective encodings are needed to obtain rates approaching one per carrier. The general channel formula is derived in [model Section 3](../science/model-and-blocking.md#3-exact-matrix-elements-of-the-correlated-channel).

## 4. From a correlated train to independent coding blocks

The single-carrier channel completely removes off-diagonal matrix elements. Taking its tensor powers would discard the temporal correlations that made the two-carrier example work. The relevant finite object is the entire $n$-carrier channel $\mathcal N_n$.

Before transmission, independently twirl the total charge in each block. This operation preserves coherence within each weight sector and removes coherence between different sectors. The sender can implement it using $n+1$ equally spaced phase choices and then forget the choice. The [exact factorization](../science/model-and-blocking.md#5-exact-factorization-over-coding-blocks) is

```math
\mathcal N_{bn}\circ\mathcal T_n^{\otimes b}
=\mathcal N_n^{\otimes b}.
```

The reason is visible in the matrix elements. A surviving element has zero total ket-minus-bra charge in every block. Its suffix charge at a boundary is consequently zero, so increments outside a block cannot couple its surviving coherence to another block. Independence of the increments then factors the multiplier exactly. This holds even when the input is entangled across blocks.

This identity is the bridge to the source’s independent-channel coding framework. At fixed noise and fixed block size $n$, an ordinary outer code uses the block channel $b$ times. Its coherent-information rate per block becomes a rate per physical carrier after division by $n$. The twirl is part of the allowed encoder; the physical phase process continues throughout the train.

Keep the limits in this order: fix the noise and $n$, let the outer code length $b$ grow, then optimize over $n$. Only after defining capacity in this way is the weak-noise behavior studied. [Model Section 6](../science/model-and-blocking.md#6-consequence-for-coding) also handles a final incomplete block while counting every slot.

## 5. The Brownian law needs two different arguments

### Achievability: bound the environment entropy

For generalized dephasing, an isometry can be written as

```math
V|x\rangle=|x\rangle_B|e_x\rangle_E.
```

The overlaps of the environment vectors equal the channel’s coherence multipliers. The vectors need not be orthogonal, so their mixture’s quantum entropy matters; the entropy of a classical list of phase histories cannot simply replace it.

For the uniform input $\tau_n=I/2^n$, the receiver output is again $\tau_n$. Hence

```math
I_c(\tau_n,\mathcal N_n)
=n-S(\rho_{E,n}),
\qquad
\rho_{E,n}=2^{-n}\sum_x|e_x\rangle\langle e_x|.
```

An upper bound on $S(\rho_{E,n})$ therefore produces a lower bound on an achievable communication rate, through exact blocking. Choosing this input proves achievability without assuming that it maximizes coherent information.

The Brownian proof constructs the correct overlaps using a charge register and oscillator coherent states. Those oscillators exist only in the mathematical dilation. Their covariance reduces the entropy estimate to a matrix with entries $K_{ij}=\min(i,j)$. A Gaussian state with that covariance supplies an entropy upper bound. The covariance spectrum and a controlled limiting integral give an upper bound of order $\sqrt\kappa$ on the environment entropy per carrier. Follow [Brownian Section 3](../science/brownian-capacity.md#3-achievability-from-complementary-entropy) for the normalization, spectral calculation, and treatment of the integral’s endpoint.

### Converse: control every input and every encoder

An achievable rate leaves open the possibility of a better encoding. The converse starts with a cleaner channel consisting of independent Brownian bridges, noiseless endpoint carriers, and a noiseless remainder. Additional correlated phase rotations reconstruct the actual train. Every code for the actual train can therefore be run on this cleaner channel by including those rotations in its decoder. The [degradation construction](../science/brownian-capacity.md#41-exact-degradation-to-a-product-of-bridge-channels) accounts for each endpoint carrier exactly once.

A bridge with endpoint spacing $L$ has an accumulated quadratic phase difference whose mean is $\kappa(L^2-1)/12$ for the uniform comparison ensemble. Taking $L$ proportional to $\kappa^{-1/2}$ makes this quantity of constant order. For generalized dephasing, [output pinching reduces the coherent-information optimization](../science/brownian-capacity.md#21-generalized-dephasing-its-complement-and-diagonal-inputs) to arbitrary diagonal input distributions, without assuming uniformity. The proof first obtains a fixed environment-purity gap at the chosen bridge scale, then covers all those distributions:

- An input distribution with a substantial entropy deficit has already lost coherent information through that deficit.
- A distribution with little entropy deficit is close enough to uniform for the environment-purity gap to persist.

Thus every bridge loses a fixed positive amount of optimized coherent information. Degradability makes the optimized quantity additive over the independent bridge factors, including inputs entangled across them. There are order $N/L$ such factors in $N$ slots, giving a deficit per carrier of order $1/L=\sqrt\kappa$.

The final step is the [finite-code inequality for arbitrary CPTP encoders](../science/brownian-capacity.md#23-a-finite-code-bound-for-arbitrary-cptp-encoders). It handles mixed encoded reference–carrier states and converts the channel bound into a constraint on entanglement fidelity. Together, the two directions establish the exponent in [Theorem B1](../science/brownian-capacity.md#1-main-theorem-and-explicit-bounds). The achievable coefficient $\pi/(4\ln2)$ does not determine an optimal leading coefficient; the theorem does not assert that the normalized deficit has a limit.

## 6. Why resets have a different cost

Between uniform resets, every carrier in a segment sees the same phase. On a segment of length $\ell$, that phase separates total-weight sectors while preserving each sector internally. The largest sector has dimension

```math
\binom{\ell}{\lfloor\ell/2\rfloor},
```

whose logarithm is $\ell-\tfrac12\log_2\ell+O(1)$. A segment can therefore retain almost all of its Hilbert-space dimension, with a logarithmic charge-sector penalty. Resets typically leave segments of length of order $1/p$, at a density of order $p$ per carrier. This identifies the scale $p\log(1/p)$, but the unknown boundaries must still be treated.

For achievability, the complement retains a coherent superposition of reset patterns. Pinching its pattern register increases entropy, giving an upper bound consisting of the pattern entropy and the average segment-weight entropy. The pattern entropy itself is of order $p\log(1/p)$ per carrier. Neither the actual sender nor receiver is handed this record. See [reset Section 3](../science/reset-capacity.md#3-achievability-a-coherent-reset-flag-and-an-entropy-upper-bound).

For the converse, revealing the reset pattern to the receiver defines an easier comparison task. Conditional on that pattern, the charge-sector projectors bound the Schmidt rank of every encoder–channel–decoder branch. This yields the finite-code fidelity bound in [reset Section 4](../science/reset-capacity.md#4-a-finite-length-converse-for-arbitrary-cptp-encoders), with arbitrary CPTP encoding included. The [renewal argument](../science/reset-capacity.md#5-renewal-averages-boundary-segments-and-small-noise-estimates) averages complete geometric segments and controls the last, truncated segment separately.

The upper and lower rate bounds consequently give $1-Q_{\mathrm R}(p)=\Theta(p\log(1/p))$. Their leading logarithmic coefficients differ. The stated fidelity-decay threshold is a proved upper bound on capacity, rather than a known exact strong-converse threshold.

## 7. What a few carriers can identify

Matching the two-carrier example fixes the first phase harmonic. A stronger fact explains the equality of all selected-slot channels through three carriers. A matrix element surviving the unknown common phase must have zero total ket-minus-bra charge. With at most three qubits, every suffix charge of such an element has magnitude at most one. These are exactly the charges where the matched increment characteristic functions agree. Arbitrary integer gaps only raise the same factors to integer powers. The [selected-slot proof](../science/indistinguishability.md#1-exact-equality-for-any-choice-of-at-most-three-slots) therefore establishes channel equality, including passive reference systems.

Four carriers can support a neutral coherence with a larger intermediate charge:

```math
|0011\rangle\langle1100|
\quad\text{has suffix charges}\quad (0,1,2,1).
```

The charge-two factor differs between the models. For consecutive slots the multipliers are $e^{-3\kappa}$ and $e^{-3\kappa/2}$. Preparing the plus superposition of these two strings and measuring in the plus/minus basis exposes that difference. The [four-carrier diagnostic](../science/indistinguishability.md#2-four-carriers-provide-an-explicit-diagnostic) supplies the probabilities and a gate implementation.

The diagnostic concerns a specified probe and final measurement. It does not supply extra adaptive interactions or a phase record. Its single-trial advantage decreases with weak noise, while the ratio of optimal redundancy fractions diverges. Distinguishing two channels in one experiment and determining their optimal long-code communication rates are different operational questions; the capacity comparison needs both complete proofs above.

## 8. A connected reading path

Use the [milestone map](milestones.md) to connect the local objects—phase rotations, charge sectors, entropy, and channel complements—to the full result. The narrative then passes through exact blocking, the two Brownian bounds, reset segments, and the channel comparison. The [science overview](../science/README.md) gives a shorter route directly to the authoritative arguments.

The final synthesis is an operational statement under one shared resource budget: the models agree on all selected-carrier channels through three slots, yet their optimized asymptotic deficits scale differently. The limits are taken at fixed noise first. The result establishes capacity orders under phase-only noise, with no feedback or assistance; practical encoding complexity, additional loss, exact optimal coefficients, and a joint finite-size/weak-noise theorem require further results.

The [verification guide](../verification/README.md) identifies the finite calculations that check the channel formulas and entropy estimates. Those calculations help expose algebraic mistakes at the tested sizes. The linked analytical arguments establish the universal statements.
