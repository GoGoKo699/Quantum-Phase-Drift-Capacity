# Learning route

The project asks why phase processes can give identical channels on a growing number of selected carriers while imposing different redundancy costs on a long quantum message. The learning route connects that question to the coding arguments, then shows what a fully characterized finite block can certify about capacity.

The single educational anchor is **John Preskill, _Quantum Information_, Chapter 10: _Quantum Shannon Theory_, updated June 2025**. The [official chapter](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf) supplies the quantum-information framework. The [anchor-to-project bridge](anchor-and-bridge.md) identifies the relevant sections, translates notation and assumptions, and explains the additional phase-process arguments supplied here.

## Two connected phases

The [shared map contains exactly 30 milestones](milestones.md). Its allocation follows the scientific dependencies: the background joins local phase noise to operational channel capacity, and the narrative develops the two capacity laws before comparing their experimental signatures and testing costs.

| Phase | Milestones | Progression |
|---|---|---|
| Background and preliminaries | M01–M12 | A qubit coherence and an unknown phase lead to charge sectors, channels, entropy, coherent information, and the common coding problem. |
| Narrative and innovation | M13–M30 | Exact blocking leads to the Brownian and reset bounds, the first distinguishing tests, a growing family of matched diagnostics, an absolute finite-block capacity certificate, and an application to timestamped distillation. |

Each milestone states a central question, an understanding target, dependencies, a conceptual connection and source pointers. The final target in each phase connects the preceding ideas. The map is a route to understanding the contribution; detailed derivations retain their authoritative homes in the scientific pages.

## Where to begin

Read the [bridge](anchor-and-bridge.md) for the physical setting and a small worked example, then follow the [milestone map](milestones.md). The selected Preskill sections can be read alongside the relevant milestones; the full chapter is not a prerequisite assignment.

For a direct specialist route, use the [scientific overview](../science/README.md), followed by [the model and exact blocking](../science/model-and-blocking.md), [Brownian capacity](../science/brownian-capacity.md), [reset capacity](../science/reset-capacity.md), [the selected-slot comparison](../science/indistinguishability.md), [the discrimination and depth result](../science/discrimination-and-depth.md), and [the growing diagnostic and capacity certificate](../science/growing-diagnostics.md). The [reference account](../references/related-work.md) identifies inherited tools and the project's contribution. The [verification guide](../verification/README.md) connects finite calculations to the analytical proofs.

The [timestamped example](../science/timestamped-entanglement.md) uses the same finite channel identity to compare the distillation losses of clean herald streams at a fixed Poisson intensity.

## Keep the operational question in view

Every transmitted qubit counts, including any carrier used as a pilot or padding. The noise trajectory is unavailable to the actual code. The oscillator environment and the enhanced channels in converse proofs are mathematical constructions. For capacity, the long-train limit at unit cadence precedes weak-noise asymptotics. In the smooth comparison, all channels through $2r+1$ fixed selected carriers agree at arbitrary positive real gaps, and a $2r+2$-carrier coherence distinguishes the two laws. That boundary concerns exact channel identity. The fixed-error discrimination and input-depth law is for the Brownian/reset pair.

[Repository overview](../README.md) · [Scientific account](../science/README.md) · [Anchor and bridge](anchor-and-bridge.md) · [30 milestones](milestones.md)
