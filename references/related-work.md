# Related work and attribution

The contribution is the optimal small-noise capacity deficit for a train of two-dimensional carriers under Brownian phase drift, together with a fully mixing reset comparison having identical complete channels on every selected set of at most three slots. The proof combines established coding and entropy tools with an input-uniform bridge converse. The broad ideas of relational encoding, correlated dephasing, and square-root Brownian entropy flow have antecedents identified below.

The comparisons concern the models and statements in the linked versions. They are a targeted literature comparison, not an exhaustive priority certificate. Bibliographic entries are also available in [BibTeX](references.bib).

## Closest physical and capacity precedents

### W

**Entropy flow of a phase-diffusing laser**

H. M. Wiseman, **Entropy Flow of a Laser Beam**, *Optics Letters* **51**, 3977–3979 (2026). [DOI](https://doi.org/10.1364/OL.599036), [arXiv:2512.01230v3](https://arxiv.org/html/2512.01230v3), especially equations (4)–(11).

Wiseman computes the Rényi-2 entropy flow of a prescribed coherent laser beam with Wiener phase diffusion and obtains a square-root dependence on photon flux times linewidth. This is a substantive precursor to the entropy scale here. The uniform-input complementary state of a dephasing channel has the same nonzero spectrum as its output on the uniform superposition, so the Brownian qubit train is a finite-dimensional relative of that fixed ensemble. A fixed-state Rényi-2 calculation supplies neither the von Neumann entropy upper bound needed for an achievable quantum rate nor a converse covering optimized encoders. Those are the two additional steps in [Brownian capacity](../science/brownian-capacity.md). The square-root entropy mechanism itself is not claimed as new.

### DBF

**Generalized dephasing channels with memory**

A. D'Arrigo, G. Benenti, and G. Falci, **Quantum capacity of dephasing channels with memory**, *New Journal of Physics* **9**, 310 (2007). [DOI](https://doi.org/10.1088/1367-2630/9/9/310), [arXiv:quant-ph/0703014v3](https://arxiv.org/pdf/quant-ph/0703014v3).

Section 2 supplies the generalized-dephasing framework, degradability, concavity and diagonal-input reduction. Section 3.2 gives an exact Markov-Pauli capacity; Section 3.3 treats an oscillator-bath model using numerical and protected-subspace bounds. These are inherited capacity tools. They do not supply the small-diffusion, all-code Brownian qubit deficit proved here. The present account includes short proofs of the specific diagonal reduction and product additivity it uses; it does not assume a general memory-channel capacity formula.

### DKB

**Rotational diffusion along a qubit stream**

R. Demkowicz-Dobrzański, P. Kolenderski, and K. Banaszek, **Effects of imperfect noise correlations on decoherence-free subsystems: SU(2) diffusion model**, *Physical Review A* **76**, 022302 (2007). [DOI](https://doi.org/10.1103/PhysRevA.76.022302), [arXiv:quant-ph/0703193v2](https://arxiv.org/html/quant-ph/0703193v2).

This work already models successive qubits undergoing correlated Markov rotations and derives a general finite-train channel representation. Its detailed coding analysis treats three qubits and noncommuting SU(2) noise. It is an important model ancestor. The present consequence is an asymptotic capacity theorem optimized over arbitrarily long codes, plus a matched temporal-process comparison; changing the rotation group alone would not constitute that contribution.

### Z

**Communication without a phase reference**

Q. Zhuang, **Quantum-Enabled Communication without a Phase Reference**, *Physical Review Letters* **126**, 060502 (2021). [DOI](https://doi.org/10.1103/PhysRevLett.126.060502), [arXiv:2010.11974v2](https://arxiv.org/pdf/2010.11974v2).

The channel applies a common unknown phase to a prescribed block of bosonic modes; total-number sectors support communication, with a logarithm-over-block-length reference penalty. This establishes the collective-phase coding context. A Brownian phase changes within every long block, so substituting its first-harmonic correlation time into a constant-phase block formula is unjustified. The reset proof here treats random segment positions, their unobserved pattern, and a finite-code converse under the same qubit carrier budget.

### LW

**Correlated multimode bosonic dephasing**

L. Lami and M. M. Wilde, **Exact solution for the quantum and private capacities of bosonic dephasing channels**, *Nature Photonics* **17**, 525–530 (2023). [DOI](https://doi.org/10.1038/s41566-023-01190-4), [arXiv:2205.05736v2](https://arxiv.org/html/2205.05736v2), Supplement III.3, Theorem S10.

Theorem S10 genuinely includes arbitrary correlated multimode phase densities. Its exact capacity formula uses unrestricted local Fock dimension; its attaining argument takes every local cutoff to infinity. For the stationary Gaussian-increment law, the unconstrained rate grows logarithmically as the increment noise vanishes. Restricting every carrier to the two levels $0,1$ leaves that upper bound too weak to determine a deficit below one qubit per slot. The present result addresses that fixed local dimension. The source must not be characterized as memoryless or single-mode only.

### PV

**Entropy-rate capacity formulas**

M. B. Plenio and S. Virmani, **Spin chains and channels with memory**, *Physical Review Letters* **99**, 120504 (2007). [DOI](https://doi.org/10.1103/PhysRevLett.99.120504), [arXiv:quant-ph/0702059v3](https://arxiv.org/html/quant-ph/0702059v3).

This work connects correlated channel capacity to environmental entropy rates and many-body models. Its exact phase-error formula uses orthogonal discrete phase unitaries; general random unitaries yield bounds. The continuously distributed qubit phase rotations here are nonorthogonal. Their classical differential entropy cannot simply be inserted into an orthogonal-error capacity formula. The quantum environment entropy and the input-optimized converse must be controlled separately.

### BPM

**Related single-oscillator recovery benchmark**

R. Lin, **Bosonic Phase Memory**, scientific repository, inspected at [aa346e09df1d52381a77ae08ac3677fda8c64b8b](https://github.com/GoGoKo699/Bosonic-Phase-Memory/tree/aa346e09df1d52381a77ae08ac3677fda8c64b8b), particularly its [noise-law comparison](https://github.com/GoGoKo699/Bosonic-Phase-Memory/blob/aa346e09df1d52381a77ae08ac3677fda8c64b8b/science/05-noise-laws-and-architecture.md).

That benchmark concerns one-interval minimax recovery of a fixed logical register from a single oscillator. It already compares noise laws with identical first-harmonic decay and different optimal performance. That broad diagnostic insufficiency is inherited. Here the carrier space is a train of separate qubits with correlated phase coordinates, and the task is asymptotic quantum communication. The new comparison matches complete channels through three selected slots and proves a parametric separation of optimal redundancy, rather than only matching a Ramsey observable.

## Foundational tools used in the proofs

### D

**Ordinary quantum coding**

I. Devetak, **The private classical capacity and quantum capacity of a quantum channel**, *IEEE Transactions on Information Theory* **51**, 44–55 (2005). [DOI](https://doi.org/10.1109/TIT.2004.839515), [arXiv:quant-ph/0304127v6](https://arxiv.org/pdf/quant-ph/0304127v6), Theorem 5 and Proposition 7.

Coherent-information achievability and the equivalence of standard quantum transmission tasks are used only after the exact finite-block factorization. No free bath reset or general forgetful-channel theorem is assumed.

### WGC

**Gaussian maximum entropy**

M. M. Wolf, G. Giedke, and J. I. Cirac, **Extremality of Gaussian quantum states**, *Physical Review Letters* **96**, 080502 (2006). [DOI](https://doi.org/10.1103/PhysRevLett.96.080502), [arXiv:quant-ph/0509154](https://arxiv.org/pdf/quant-ph/0509154).

The maximum von Neumann entropy at fixed covariance bounds the finite-mode mathematical environment. The normalization, covariance eigenvalues and small-noise integral are derived in the Brownian proof.

### HW

**Gaussian entropy from covariance**

A. S. Holevo and R. F. Werner, **Evaluating capacities of bosonic Gaussian channels**, *Physical Review A* **63**, 032312 (2001). [DOI](https://doi.org/10.1103/PhysRevA.63.032312), [arXiv:quant-ph/9912067](https://arxiv.org/pdf/quant-ph/9912067), Section III.C.

The symplectic-eigenvalue entropy formula supplies standard Gaussian-state background. No bosonic communication resource or bosonic capacity theorem is transferred to the qubit carriers.

### S

**Entanglement fidelity and entropy**

B. Schumacher, **Sending entanglement through noisy quantum channels**, *Physical Review A* **54**, 2614–2628 (1996). [DOI](https://doi.org/10.1103/PhysRevA.54.2614), [arXiv:quant-ph/9604023](https://arxiv.org/pdf/quant-ph/9604023).

This is the primary context for entanglement fidelity and the quantum-Fano relation. The finite-dimensional entropy inequality required by the Brownian converse is proved directly in that account.

### TH

**Schmidt-number and singlet-fraction bounds**

B. M. Terhal and P. Horodecki, **Schmidt number for density matrices**, *Physical Review A* **61**, 040301(R) (2000). [DOI](https://doi.org/10.1103/PhysRevA.61.040301), [arXiv:quant-ph/9911117v4](https://arxiv.org/html/quant-ph/9911117v4), Proposition 1 and Lemma 1.

Local operations cannot increase Schmidt number, and overlap with an $M$-dimensional maximally entangled state is at most Schmidt number divided by $M$. The reset converse combines these standard facts with explicit segment charge-sector ranks; it includes a direct proof of the overlap bound.

### BRS

**Reference frames and relational encoding**

S. D. Bartlett, T. Rudolph, and R. W. Spekkens, **Reference frames, superselection rules, and quantum information**, *Reviews of Modern Physics* **79**, 555–609 (2007). [DOI](https://doi.org/10.1103/RevModPhys.79.555), [arXiv:quant-ph/0610030v3](https://arxiv.org/html/quant-ph/0610030v3), Sections II and III.A.

This review explains phase twirling, charge sectors and communication without a shared reference frame. Those concepts are background for the present temporal noise problem. All finite-sector identities needed by the reset proof are derived in the repository.

## Educational anchor

John Preskill, **Quantum Information, Chapter 10: Quantum Shannon Theory**, updated June 2025. [Official author-hosted PDF](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf).

This is the single anchor for the [learning route](../learning/README.md). Its entropy and quantum-capacity framework is connected to the project's exact blocking, Gaussian entropy, bridge and renewal arguments in the [source-to-project bridge](../learning/anchor-and-bridge.md). The research citations above retain their roles in attribution and proof dependencies.
