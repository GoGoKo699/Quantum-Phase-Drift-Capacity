# Matched phase laws for timestamped entanglement

This example specializes the [smooth matched phase laws](growing-diagnostics.md#2-matching-the-increment-harmonics) to $`r=1`$. The same harmonic match controls both the selected carrier channel and the raw state of timestamped entangled links.

## Two increment laws with the same first harmonic

Start each phase uniformly on the circle and use stationary independent increments. Fix $`\kappa\gt0`$. In process A the Brownian variance per unit time is $`\kappa+\kappa^4`$. In process B the Brownian variance per unit time is $`\kappa^4`$ and an independent Poisson process adds $`\pi`$ at rate $`\kappa/4`$. The two smooth laws are the $`r=1`$ instances of the signed-grid construction. The negative stencil weight is at zero, so its jumps leave the phase unchanged.

For an interval of duration $`t`$, their characteristic functions at integer harmonic $`j`$ are

```math
\begin{aligned}
f_{A,t}(j)&=\exp[-t(\kappa+\kappa^4)j^2/2],\\
f_{B,t}(j)&=\exp[-t\kappa^4j^2/2+t(\kappa/4)((-1)^j-1)].
\end{aligned}
```

These agree for $`j=0,\pm1`$ at every gap. The $`\pi`$ jumps leave the second harmonic unchanged, so $`f_{A,t}(2)/f_{B,t}(2)=e^{-2\kappa t}`$.

## The first distinguishing herald count

A clean raw link at time $`t_i`$ is $`(|01\rangle+e^{i\theta(t_i)}|10\rangle)/\sqrt{2}`$. Bob's local bit flip changes its two basis states to $`|00\rangle`$ and $`|11\rangle`$. For $`m`$ links with fixed timestamps, the averaged state in that basis is

```math
\rho_m=2^{-m}\sum_{x,y\in\{0,1\}^m} c_m(x,y)\,|x,x\rangle\langle y,y|,
```

where $`c_m(x,y)`$ is the [selected-carrier multiplier](growing-diagnostics.md#3-the-first-differing-carrier-count) at those times. This is the normalized Choi state of the selected-carrier phase channel. Equality on every matrix unit gives equality of the full raw states through three offered links, since their surviving suffix charges have magnitude at most one.

For four offered links, write $`\Delta_i=t_{i+1}-t_i`$. The only unordered string pair to reach charge two is $`x=0011`$, $`y=1100`$. Its two coherence multipliers satisfy

```math
c_A(x,y)=e^{-2\kappa\Delta_2}\,c_B(x,y),\qquad c_B(x,y)\gt0.
```

Each node can project onto the span of its two labeled strings, preserving their coherence, then measure the surviving logical qubit in the $`X`$ basis and exchange the outcome. Guess at random on projection failure. For equal priors this gives success probability $`1/2+(c_B-c_A)/32`$, attaining the unrestricted measurement optimum because all of the state difference lies in that off-diagonal pair. Four is the first distinguishing count for a trial with fixed timestamps and a total budget on distinct offered links.

## Distillation loss for a Poisson stream

Let the offered timestamps be an independent Poisson process of rate $`\lambda\gt0`$, with clean raw links and ideal storage and control. Define $`R_A`$ and $`R_B`$ as the respective optimal rates of distillation by local operations and classical communication, in ebits per unit time. The [timestamped distillation theorem](https://github.com/GoGoKo699/Quantum-Timestamped-Entanglement/blob/main/science/matched-phase-diagnostics.md) gives, at fixed $`\lambda`$,

```math
\begin{aligned}
\lambda-R_A&=\Theta_\lambda(\sqrt{\lambda\kappa}),\\
\lambda-R_B&=\frac{\kappa}{4}\log_2\!\frac{\lambda}{\kappa}+O_\lambda(\kappa).
\end{aligned}
```

The observation time tends to infinity at fixed noise before $`\kappa`$ tends to zero. The proof uses the entropy of the timestamp-conditioned raw state. Brownian phase fluctuations cost a constant amount of entropy on average per window of duration proportional to $`(\lambda\kappa)^{-1/2}`$. For process B, $`\pi`$-jump parity between consecutive clicks gives the leading binary entropy, with weak Brownian smoothing contributing at most order $`\sqrt{\lambda}\,\kappa^2`$. Thus all three-herald diagnostics agree yet the larger distillation loss divided by the smaller one diverges. The [unit-cadence capacity theorem](growing-diagnostics.md#1-exact-agreement-with-different-capacity-losses) concerns unassisted coding into a qubit channel with a freely chosen input.
