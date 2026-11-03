# Learning route

The project asks why two phase processes can look identical to a few carriers while imposing different redundancy costs on a long quantum message. The learning route connects that physical question to the entropy, coding and converse arguments in the scientific account.

The single educational anchor is **John Preskill, _Quantum Information_, Chapter 10: _Quantum Shannon Theory_, updated June 2025**. The [official chapter](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf) supplies the quantum-information framework. The [anchor-to-project bridge](anchor-and-bridge.md) identifies the relevant sections, translates notation and assumptions, and explains the additional phase-process arguments supplied here.

## Two connected phases

The [shared map contains exactly 30 milestones](milestones.md). Its allocation follows the scientific dependencies: the background joins local phase noise to operational channel capacity, and the narrative develops the two capacity laws before comparing their experimental signatures.

| Phase | Milestones | Progression |
|---|---|---|
| Background and preliminaries | M01–M12 | A qubit coherence and an unknown phase lead to charge sectors, channels, entropy, coherent information, and the common coding problem. |
| Narrative and innovation | M13–M30 | Exact blocking leads to the Brownian and reset bounds, then to equality through three slots, a four-slot diagnostic, and the global capacity comparison. |

Each milestone states a central question, an understanding target, dependencies, a conceptual connection and source pointers. The final target in each phase connects the preceding ideas. The map is a route to understanding the contribution; detailed derivations retain their authoritative homes in the scientific pages.

## Where to begin

Read the [bridge](anchor-and-bridge.md) for the physical setting and a small worked example, then follow the [milestone map](milestones.md). The selected Preskill sections can be read alongside the relevant milestones; the full chapter is not a prerequisite assignment.

For a direct specialist route, use the [scientific overview](../science/README.md), followed by [the model and exact blocking](../science/model-and-blocking.md), [Brownian capacity](../science/brownian-capacity.md), [reset capacity](../science/reset-capacity.md), and [the selected-slot comparison](../science/indistinguishability.md). The [reference account](../references/related-work.md) identifies inherited tools and the specific addition. The [verification guide](../verification/README.md) connects finite calculations to the analytical proofs.

## Keep the operational question in view

Every transmitted qubit counts, including any carrier used as a pilot or padding. The noise trajectory is unavailable to the actual code. The oscillator environment and the enhanced channels in converse proofs are mathematical constructions. The long-train limit precedes weak-noise asymptotics, and the matching deficit orders do not determine exact optimal coefficients or efficient codes.

[Repository overview](../README.md) · [Scientific account](../science/README.md) · [Anchor and bridge](anchor-and-bridge.md) · [30 milestones](milestones.md)
