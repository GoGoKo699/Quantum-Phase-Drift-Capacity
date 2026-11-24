# Quantum Phase Drift Capacity

How much redundancy does a drifting phase impose on quantum communication, and what can a measurement on a limited number of carriers tell us about that cost?

This repository studies a train of qubits subject to a stationary, unknown phase process. Brownian drift and random resets give a simple example of identical few-carrier channels with different long-train capacity losses. The same phenomenon persists when the number of carriers available for diagnosis grows as the noise weakens.

## What can a finite set of carriers reveal?

For each positive integer $`r`$, the [growing diagnostic window](science/growing-diagnostics.md) constructs two smooth, mixing phase processes with identical quantum channels on every selection of at most $`2r+1`$ carriers. Equality holds at arbitrary time gaps and with a passive reference. The first unequal channel occurs at $`2r+2`$ carriers, where a balanced two-string input detects the next Fourier harmonic.

At a fixed unit cadence, write $`Q_A`$ and $`Q_B`$ for their unassisted capacities and $`\kappa`$ for the difference between their Brownian variance parameters. The redundancy ratio $`(1-Q_A)/(1-Q_B)`$ diverges even for a growing $`r=o(\kappa^{-1/4}/\sqrt{\log(1/\kappa)})`$. In this regime, $`1-Q_A`$ has order $`\sqrt{\kappa}`$, whereas $`1-Q_B`$ is at most of order $`\kappa^2+\kappa r^2\log(e/(\kappa r^2))`$.

Absolute capacity can still be bounded from a complete $`n`$-carrier block channel. If $`a_n`$ is its optimized coherent information, every stationary independent-increment process in this model satisfies

```math
\frac{a_n}{n}\le Q\le\frac{a_n+\log_2(n+1)}{n}.
```

The interval width vanishes with $`n`$. The optimal window size for estimating the much smaller redundancy $`1-Q`$ to relative accuracy remains open.

## Timestamped entanglement

The two smooth laws at $`r=1`$ give identical raw entangled states through three offered heralds. Four suffice to distinguish the laws by local measurements. At fixed Poisson herald intensity the Brownian distillation loss is of square-root order, while the loss from rare $`\pi`$ jumps scales as the jump rate times its logarithmic inverse. See [the matched-phase connection](science/timestamped-entanglement.md) and the [distillation theorem in Quantum Timestamped Entanglement](https://github.com/GoGoKo699/Quantum-Timestamped-Entanglement/blob/main/science/matched-phase-diagnostics.md).

## Quantum communication capacity

One qubit is transmitted in each equally spaced slot. The initial phase is uniform, the phase trajectory is inaccessible, and the encoder and decoder may act collectively on the whole train. Every carrier is counted. Let $Q$ denote unassisted quantum capacity in logical qubits per transmitted qubit.

| Phase process | Capacity deficit |
|---|---|
| Independent Gaussian phase increments of variance $\kappa$ | $1-Q_{\mathrm B}(\kappa)=\Theta(\sqrt{\kappa})$ |
| A reset to an independent uniform phase with probability $p$ per step | $1-Q_{\mathrm R}(p)=\Theta(p\log(1/p))$ |

Choose $p=1-e^{-\kappa/2}$. The two models then have the same first-harmonic correlation at every separation and the same complete quantum channel on any selected set of one, two, or three slots, including reference-entangled probes. Their optimal redundancy fractions nevertheless satisfy

```math
\frac{1-Q_{\mathrm B}(\kappa)}
     {1-Q_{\mathrm R}(1-e^{-\kappa/2})}
=\Theta\!\left(\frac{1}{\sqrt{\kappa}\,\log(1/\kappa)}\right)
\longrightarrow\infty.
```

These capacity laws take the train-length limit at fixed noise before the small-noise limit. They determine the orders of the optimal deficits.

## How many carriers distinguish Brownian drift from uniform resets?

The [four-carrier test](science/indistinguishability.md#2-four-carriers-provide-an-explicit-diagnostic) measures the coherence between $0011$ and $1100$. For four consecutive carriers, it decays by $e^{-3\kappa}$ under Brownian drift and by $e^{-3\kappa/2}$ under resets. The same two-string probe is [optimal on any four fixed selected slots](science/discrimination-and-depth.md#exact-four-carrier-optimum), including when the receiver has a passive reference. Its success probability tends to one half as the noise weakens on four consecutive slots.

For the known matched hypotheses above, the [minimum number of consecutive carriers](science/discrimination-and-depth.md#fixed-error-resource-law) at fixed error $\varepsilon\in(0,1/2)$ and input entanglement depth at most $d$ is

```math
N_\varepsilon(\kappa,d)
=\Theta_\varepsilon\!\left(\max\left\{\kappa^{-1/3},(\kappa d)^{-1/2}\right\}\right).
```

The constants are uniform in $d$. Depth one requires order $\kappa^{-1/2}$ carriers. Unrestricted probes reach order $\kappa^{-1/3}$, and depth of order $\kappa^{-1/3}$ already attains that scale. The test uses one pass through a fixed train and permits joint readout. Depth limits the size of the entangled input groups, with any retained reference private to its group.

## Read the science

Start with the [scientific overview](science/README.md), or go directly to the question you need.

| Question | Authoritative account |
|---|---|
| What is the channel, which resources count, and how is capacity defined? | [Model and exact block factorization](science/model-and-blocking.md) |
| Why is the Brownian deficit of square-root order for every code? | [Brownian capacity](science/brownian-capacity.md) |
| What changes when the phase is held constant between random resets? | [Reset capacity](science/reset-capacity.md) |
| Why do all channels through three slots agree? | [Indistinguishability and capacity separation](science/indistinguishability.md) |
| Can exact agreement persist for a growing number of carriers, and what does a finite block certify? | [Growing diagnostic window](science/growing-diagnostics.md) |
| How does the matched phase pair affect a Poisson stream of heralded links? | [Timestamped entanglement](science/timestamped-entanglement.md) |
| How many carriers and how much input entanglement give a fixed error? | [Discrimination and entanglement depth](science/discrimination-and-depth.md) |
| Which ingredients are inherited, and what is the specific addition? | [Related work and references](references/related-work.md) |
| How can the finite algebraic and entropy checks be reproduced? | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps further questions to these same sources.

## Learn the argument

The [learning route](learning/README.md) uses **Preskill's _Quantum Shannon Theory_, updated June 2025**, as its single educational anchor. The [source-to-project bridge](learning/anchor-and-bridge.md) connects entropy and channel capacity to the phase-noise model through a worked example and a notation guide.

The [30-milestone map](learning/milestones.md) develops 12 background targets and 18 targets through the project's arguments. The final milestones connect the Brownian/reset comparison to the growing-window construction, the finite-block capacity interval and the timestamped distillation example.

## How the bounds work

For achievability, an exact total-charge twirl makes successive coding blocks independent without resetting the physical phase process. A mathematical coherent-state dilation and Gaussian maximum entropy bound then control the Brownian environment's entropy.

For the Brownian converse, independent bridge blocks form a cleaner channel from which the actual correlated channel can be reconstructed by additional phase rotations. Each bridge of length proportional to $\kappa^{-1/2}$ loses a fixed amount of coherent information, even after optimizing over every input. The finite-code argument covers arbitrary completely positive, trace-preserving encoders.

For resets, the environment entropy is bounded using the random segment pattern and its total-charge sectors. A complementary rank argument limits every code: conditional on the reset pattern, each Kraus branch has bounded Schmidt rank. Renewal averages give the logarithmic loss per reset.

For discrimination, the common-phase channel bounds both hypotheses when the train is too short. On a longer train, probes in two halves turn the accumulated phase difference into a measurable signal. Balanced superpositions amplify that signal within their entangled groups. Product probes use paired singlet measurements to detect changes in relative phase.

## Scope and attribution

The physical model has phase noise only, one two-dimensional carrier per fixed slot, arbitrary local encoding and decoding operations, and no preshared entanglement, feedback, free shared phase reference or extra communication channel. The oscillator dilation is a proof device. Endpoint phases and reset locations are converse aids and are not supplied to the actual coding protocol.

Square-root entropy flow under Brownian phase diffusion appears in Wiseman's laser-beam analysis. Generalized-dephasing capacity tools, collective-charge encoding, Gaussian entropy extremality and periodic Fourier differentiation are established ingredients. The [related-work account](references/related-work.md) traces their roles in the fixed-qubit capacity laws, the growing-window construction and the sharp discrimination law for the Brownian and uniform-reset pair.

## Reproduce

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_phase_drift.py
```

The script checks the finite channel identities, the diagnostics at both window sizes, the signed Fourier stencil, Gaussian entropy bounds, Brownian-bridge moments and the analytic integral constant. [Verification details](verification/README.md) state the tested sizes, output and limits.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
