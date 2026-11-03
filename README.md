# Quantum Phase Drift Capacity

How much redundancy is needed to transmit quantum information through a slowly drifting phase, and how much can short-carrier experiments reveal about that cost?

This repository studies a train of qubits subject to a stationary, unknown phase process. Two fully mixing processes have exactly the same channel on every selection of at most three carrier slots, yet their optimal communication-capacity losses have different small-noise orders.

## Principal results

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

Four consecutive carriers distinguish the models. The coherence between $0011$ and $1100$ decays by $e^{-3\kappa}$ under Brownian drift and by $e^{-3\kappa/2}$ under resets. An explicit preparation and measurement are given in the [comparison](science/indistinguishability.md).

These are statements about the optimal asymptotic rate under the specified resource model. The train-length limit is taken at a fixed noise parameter before the small-noise limit. Exact optimal coefficients and efficient finite-length codes are not determined.

## Read the science

Start with the [scientific overview](science/README.md), or go directly to the question you need.

| Question | Authoritative account |
|---|---|
| What is the channel, which resources count, and how is capacity defined? | [Model and exact block factorization](science/model-and-blocking.md) |
| Why is the Brownian deficit of square-root order for every code? | [Brownian capacity](science/brownian-capacity.md) |
| What changes when the phase is held constant between random resets? | [Reset capacity](science/reset-capacity.md) |
| Why do all channels through three slots agree, and how do four distinguish them? | [Indistinguishability and capacity separation](science/indistinguishability.md) |
| Which ingredients are inherited, and what is the specific addition? | [Related work and references](references/related-work.md) |
| How can the finite algebraic and entropy checks be reproduced? | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps further questions to these same sources.

## Learn the argument

The [learning route](learning/README.md) uses **Preskill's _Quantum Shannon Theory_, updated June 2025**, as its single educational anchor. The [source-to-project bridge](learning/anchor-and-bridge.md) connects entropy and channel capacity to the phase-noise model through a worked example and a notation guide.

The [30-milestone map](learning/milestones.md) develops 12 background targets and 18 targets through the project's arguments. Each milestone identifies its central question, dependencies, conceptual connection and scientific sources. The route ends by connecting the two capacity laws, the few-carrier experiments and the limits of the result.

## How the bounds work

For achievability, an exact total-charge twirl makes successive coding blocks independent without resetting the physical phase process. A mathematical coherent-state dilation and Gaussian maximum entropy bound then control the Brownian environment's entropy.

For the Brownian converse, independent bridge blocks form a cleaner channel from which the actual correlated channel can be reconstructed by additional phase rotations. Each bridge of length proportional to $\kappa^{-1/2}$ loses a fixed amount of coherent information, even after optimizing over every input. The finite-code argument covers arbitrary completely positive, trace-preserving encoders.

For resets, the environment entropy is bounded using the random segment pattern and its total-charge sectors. A complementary rank argument limits every code: conditional on the reset pattern, each Kraus branch has bounded Schmidt rank. Renewal averages give the logarithmic loss per reset.

## Scope and attribution

The physical model has phase noise only, one two-dimensional carrier per fixed slot, arbitrary local encoding and decoding operations, and no preshared entanglement, feedback, free shared phase reference or extra communication channel. The oscillator dilation is a proof device. Endpoint phases and reset locations are converse aids and are not supplied to the actual coding protocol.

Square-root entropy flow under Brownian phase diffusion already appears in Wiseman's laser-beam analysis. Generalized-dephasing capacity tools, collective-charge encoding and Gaussian entropy extremality are established ingredients. The contribution here is the optimized fixed-qubit capacity law and its comparison with a fully mixing process having identical complete channels through three slots. See the [source-by-source comparison](references/related-work.md); finite diagnostics do not replace the analytical proofs.

## Reproduce

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_phase_drift.py
```

The script checks exact finite channel identities, the four-carrier diagnostic, Gaussian entropy bounds, Brownian-bridge moments and the analytic integral constant. [Verification details](verification/README.md) state the tested sizes, output and limits.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
