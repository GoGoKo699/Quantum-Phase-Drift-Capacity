# A 30-milestone map of phase-drift capacity

The starting point is one qubit whose phase is unknown. The question grows when many qubits experience related phases: what can survive in their relative coherences, what rate can a long code achieve, and what can a short experiment reveal about that rate?

This map has **exactly 30 milestones**. Each describes an understanding target and its place in that scientific story. The authoritative definitions and proofs remain in [the scientific account](../science/README.md); the map points to them instead of repeating their derivations.

The single educational anchor is **John Preskill, *Quantum Information*, Chapter 10: *Quantum Shannon Theory*, updated June 2025** ([official PDF](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf)). Section numbers below refer to that version. The [anchor and bridge](anchor-and-bridge.md) translates its notation and assumptions, develops a small relational-encoding example, and identifies the additional arguments supplied by this project. A pointer to Preskill identifies the underlying information-theoretic idea; the Brownian and reset results themselves are in the linked project sources.

## How the two phases fit together

| Phase | Milestones | Progression |
|---|---|---|
| [Background and preliminaries](#background-and-preliminaries-m01m12) | M01–M12: 12 milestones | From a carrier and a relative coherence to correlated channels, entropy, coding resources, and a complete operational question. |
| [Narrative and innovation](#narrative-and-innovation-m13m30) | M13–M30: 18 milestones | From exact coding blocks through the two capacity arguments to finite-slot indistinguishability and the global separation. |

The allocation gives the shared channel-and-entropy framework twelve milestones. Eighteen then develop the three connected parts of the contribution: the Brownian capacity law, the reset capacity law, and the comparison between short probes and long codes. Each phase ends by integrating its components. The map covers the project's main reasoning and scope; detailed estimates and specialist extensions remain in the scientific pages.

Dependencies name earlier milestones only. They indicate which ideas a target uses, rather than a required reading of every preceding paragraph. Within the narrative, M15–M22 develop Brownian drift and M23–M27 develop resets; M28–M30 bring the branches together.

## Background and preliminaries (M01–M12)

### M01. One carrier and an unknown phase

**Central question.** What does averaging an unknown phase do to a single qubit?

**Understanding target.** Explain how the rotation $U(\theta)=\mathrm{diag}(1,e^{i\theta})$ preserves populations while changing coherence, and why a uniform phase removes the single-carrier off-diagonal terms. Distinguish an unknown rotation from loss of the physical carrier.

**Dependencies and story role.** No earlier milestone. This fixes the local physical action before introducing a train.

**Conceptual connection.** A classical mixture of unitaries becomes a quantum channel when the phase record is inaccessible.

**Source pointers.** Preskill §10.2.2 on mixing and entropy; [carrier model, §1](../science/model-and-blocking.md#1-one-qubit-in-each-carrier-slot), equations (M1)–(M3).

### M02. Relative coherence across two carriers

**Central question.** How can two carriers retain quantum information when each marginal is completely dephasing?

**Understanding target.** Explain why the coherence between $01$ and $10$ is insensitive to a common phase but depends on the phase difference. Identify the two physical carriers and the one logical two-dimensional subspace in this example.

**Dependencies and story role.** M01. The smallest relational example shows why studying a joint channel is essential.

**Conceptual connection.** A phase common to two basis strings cancels when their total excitation numbers agree; temporal correlations can therefore matter even when single-carrier data are identical.

**Source pointers.** Preskill §10.7.1 for the communication question; [the worked bridge](anchor-and-bridge.md); [channel matrix elements, §3](../science/model-and-blocking.md#3-exact-matrix-elements-of-the-correlated-channel).

### M03. Independent increments and correlated phases

**Central question.** Which random variables are independent in the two noise models?

**Understanding target.** Distinguish independent phase increments from correlated absolute carrier phases. Explain the uniform initial phase, Gaussian increments of variance $\kappa$, and the hold-or-uniform-reset law with probability $p$.

**Dependencies and story role.** M01–M02. The two-carrier observation becomes a stationary train model with precisely specified noise.

**Conceptual connection.** Sharing accumulated increments produces memory without any dependence of the noise on the transmitted state. Positive-noise mixing does not make nearby uses independent.

**Source pointers.** Preskill §10.1.2 for correlation and independence; [carrier model, §1](../science/model-and-blocking.md#1-one-qubit-in-each-carrier-slot); [reset model, §1](../science/reset-capacity.md#1-model-operational-rate-and-theorem), equations (R1)–(R2).

### M04. Fourier charges describe the whole channel

**Central question.** How does a phase process determine every matrix element of its quantum channel?

**Understanding target.** Track the ket-minus-bra charges $a_j=x_j-y_j$, their suffix sums, and the characteristic function $f(q)$. Explain why a uniform initial phase enforces equal total weight and why surviving coherences sample specific integer harmonics.

**Dependencies and story role.** M02–M03. This provides the common algebraic description used in blocking, dilation, and channel comparison.

**Conceptual connection.** A stochastic process becomes a Schur multiplier on computational-basis matrix units; first-harmonic correlations reveal only part of that multiplier.

**Source pointers.** Preskill §10.7.3 for the dephasing-channel context; [exact matrix elements, §3](../science/model-and-blocking.md#3-exact-matrix-elements-of-the-correlated-channel), equations (M9)–(M11). The suffix-charge formula is derived locally.

### M05. Classical and quantum entropy have different jobs

**Central question.** Which uncertainty is being counted when a proof subtracts an entropy from the transmitted dimension?

**Understanding target.** Distinguish classical entropy $H(p)$, von Neumann entropy $S(\rho)$, and purity. Explain why a mixture of nonorthogonal quantum states need not have the entropy of its classical labels, and why pinching can increase entropy.

**Dependencies and story role.** M01–M03. These distinctions prepare the environment calculations without identifying classical noise uncertainty with lost quantum information.

**Conceptual connection.** The relevant entropy belongs to a complementary quantum output, even though the phase trajectory is classical.

**Source pointers.** Preskill §§10.1.1 and 10.2.1–10.2.2; [generalized dephasing, §2.1](../science/brownian-capacity.md#21-generalized-dephasing-its-complement-and-diagonal-inputs); [coherent reset flag, §3](../science/reset-capacity.md#3-achievability-a-coherent-reset-flag-and-an-entropy-upper-bound).

### M06. The receiver and the complementary environment

**Central question.** What does a complementary channel represent, and what resources does it imply?

**Understanding target.** Interpret an isometry of the form $V|x\rangle=|x\rangle_B|e_x\rangle_E$ and its two reduced outputs. Distinguish an environment introduced to represent a channel from an extra system that the communication protocol can use.

**Dependencies and story role.** M04–M05. This turns the channel multiplier into overlaps of environment states.

**Conceptual connection.** The same isometry explains dephasing at the receiver and the environment entropy used in a rate bound. A reference system used to define fidelity is also distinct from shared assistance.

**Source pointers.** Preskill §§10.7.1 and 10.7.3; [dephasing and its complement, §2.1](../science/brownian-capacity.md#21-generalized-dephasing-its-complement-and-diagonal-inputs), equations (B13)–(B14).

### M07. What counts as successful quantum transmission

**Central question.** What operational task does the capacity quantify?

**Understanding target.** Describe entanglement transmission of an $M$-dimensional logical system through $N$ qubit slots. Interpret entanglement fidelity and the rate $(\log_2 M)/N$, and include pilots, dummy carriers, and arbitrary CPTP encoding in the resource count.

**Dependencies and story role.** M03 and M06. A physical noise model becomes a definite optimization problem.

**Conceptual connection.** Preserving a reference's entanglement tests the coherent action of the full code; it is more demanding than transmitting one chosen state or estimating a phase.

**Source pointers.** Preskill §§10.7.1–10.7.2; [operational capacity, §2](../science/model-and-blocking.md#2-operational-entanglement-transmission-capacity), equations (M6)–(M8).

### M08. Coherent information links entropy to rate

**Central question.** Why does the difference between receiver entropy and environment entropy enter quantum coding?

**Understanding target.** Interpret $I_c(\rho,\mathcal M)=S(B)-S(E)$ for a fixed input and channel. Distinguish this quantity, its input maximum, and the operational capacity of a correlated train.

**Dependencies and story role.** M05–M07. This introduces the rate-producing quantity before deciding when a coding theorem applies.

**Conceptual connection.** The anchor's independent-channel coding framework motivates an achievable bound, but applying it here requires a construction of independent effective blocks.

**Source pointers.** Preskill §§10.7.1–10.7.2 and 10.9.4; [coding consequence, §6](../science/model-and-blocking.md#6-consequence-for-coding), equations (M16)–(M17).

### M09. Data processing and degradability

**Central question.** When can correlated inputs fail to improve the maximum coherent information of a product channel?

**Understanding target.** Explain a degrading map from the receiver output to its complement and why generalized dephasing admits one. Trace how mutual-information data processing gives additivity for products of degradable factors, including entangled joint inputs.

**Dependencies and story role.** M06 and M08. A property of one channel becomes a tool for controlling a whole product.

**Conceptual connection.** Degradability applies to the effective channel factors used in the proof; it does not declare the original temporal phase process independent.

**Source pointers.** Preskill §§10.2.4, 10.6.6, and 10.7.3; [dephasing facts, §2.1](../science/brownian-capacity.md#21-generalized-dephasing-its-complement-and-diagonal-inputs) and [product additivity, §2.2](../science/brownian-capacity.md#22-additivity-of-maximized-coherent-information-for-degradable-factors).

### M10. Charge sectors and their information content

**Central question.** What remains inside a block after an unknown common phase is averaged?

**Understanding target.** Explain the decomposition into fixed-weight sectors, their dimensions $\binom{\ell}{w}$, and why coherences within a sector survive a collective phase twirl. Distinguish selecting a protected sector from optimizing an arbitrary input distribution.

**Dependencies and story role.** M02, M04, and M05. The two-carrier relative coherence extends to the structure of a whole constant-phase segment.

**Conceptual connection.** Sector dimension becomes a possible coding space and, later, a converse constraint on Schmidt rank after a reset pattern is fixed.

**Source pointers.** Preskill §§10.2.2 and 10.7.1 for mixing and coding; [charge twirl, §4](../science/model-and-blocking.md#4-a-finite-phase-grid-implements-the-exact-charge-twirl); [conditional sector ranks, §2](../science/reset-capacity.md#2-conditional-channels-and-their-sector-ranks). The sector construction is supplied by the project.

### M11. Achievability and a converse make different claims

**Central question.** What must be shown to establish the optimal order of a capacity deficit?

**Understanding target.** Separate a rate obtained from one chosen input from an upper bound that applies to every code. Explain why analyzing uniform-input entropy alone cannot prove optimality and why arbitrary mixed encoder outputs must be covered in a converse.

**Dependencies and story role.** M07–M09. This fixes the quantifiers needed before interpreting either capacity law.

**Conceptual connection.** High final entanglement fidelity forces large reference–receiver coherent information; a channel-wide bound can then rule out excessive rates.

**Source pointers.** Preskill §10.7.2; [arbitrary-encoder finite-code bound, §2.3](../science/brownian-capacity.md#23-a-finite-code-bound-for-arbitrary-cptp-encoders); [finite-inner-block bound](../science/brownian-capacity.md#finite-inner-block-achievable-bound).

### M12. Synthesis of the operational question

**Central question.** How do the local phase model, joint channel, and coding task fit into one comparison?

**Understanding target.** Explain how completely dephasing single-carrier marginals can coexist with a high joint communication rate. State the common carrier budget, inaccessible noise record, allowed operations, and order of limits needed to compare Brownian drift with resets.

**Dependencies and story role.** M01–M11. This closes the background phase with the complete problem rather than another isolated prerequisite.

**Conceptual connection.** A statement about a few selected slots and a statement about an optimal long code are different operational claims about the same process. The remaining milestones establish and connect both.

**Source pointers.** Preskill §§10.7.1–10.7.3; [operational capacity, §2](../science/model-and-blocking.md#2-operational-entanglement-transmission-capacity); [scientific interpretation](../science/README.md#physical-interpretation).

## Narrative and innovation (M13–M30)

### M13. Charge twirling produces exact independent blocks

**Central question.** How can ordinary independent-channel coding be used without resetting the phase process?

**Understanding target.** Explain why the $n+1$ finite phase values implement an exact charge twirl and why zero charge separately in each block removes every cross-boundary suffix contribution. Recognize the resulting identity as an equality of channels, including inputs entangled across blocks.

**Dependencies and story role.** M04, M10, and M12. A local encoder operation supplies the first constructive step of the capacity argument.

**Conceptual connection.** Independence follows from an exact algebraic cancellation, not from replacing a mixing process by approximately independent segments.

**Source pointers.** Preskill §10.7.1 for the coding theorem's setting; [finite twirl, §4](../science/model-and-blocking.md#4-a-finite-phase-grid-implements-the-exact-charge-twirl) and [Proposition M1, §5](../science/model-and-blocking.md#5-exact-factorization-over-coding-blocks).

### M14. A finite inner block yields an asymptotic rate

**Central question.** In what order does a finite-block entropy calculation become a capacity lower bound?

**Understanding target.** Fix the noise parameter and inner block size, send many independently twirled blocks through an outer code, and account for a short final tail. Explain why optimizing the inner block comes after taking the outer coding limit.

**Dependencies and story role.** M07–M08 and M13. This turns the factorization identity into a usable rate statement for both models.

**Conceptual connection.** The finite block is one use of the effective memoryless channel. Its coherent information per physical carrier supplies an asymptotic existence result, not an explicit finite-length error guarantee.

**Source pointers.** Preskill §§10.7.1 and 10.9.4; [coding consequence, §6](../science/model-and-blocking.md#6-consequence-for-coding), equation (M17).

### M15. Brownian coherences as environment overlaps

**Central question.** Which complementary state reproduces the Brownian multiplier exactly?

**Understanding target.** Match the total-weight register and real coherent-state overlaps to the neutral-charge condition and Gaussian suffix-charge factor. Explain the redundant oscillator and why the oscillators are proof variables rather than additional communication resources.

**Dependencies and story role.** M04, M06, and M14. The Brownian branch starts with an exact channel representation, before any entropy approximation.

**Conceptual connection.** A convenient dilation exposes the quantum environment whose entropy controls a chosen input's achievable rate.

**Source pointers.** Preskill §10.7.3 for complementary channels; [exact dilation, §3.1](../science/brownian-capacity.md#31-an-exact-coherent-state-dilation), equations (B23)–(B27). The coherent-state realization is a project derivation.

### M16. Covariance bounds the Brownian environment entropy

**Central question.** How does the accumulated-increment structure enter an entropy upper bound?

**Understanding target.** Explain why Bernoulli suffix sums produce the covariance matrix with entries $\min(i,j)$, including the stated vacuum and quadrature normalization. Understand why a Gaussian state with that covariance bounds the actual mixture's entropy from above.

**Dependencies and story role.** M05 and M15. An exact but large environmental mixture becomes a controlled spectral calculation.

**Conceptual connection.** Covariance is sufficient for an upper bound through Gaussian maximum entropy; the actual environment is not assumed Gaussian.

**Source pointers.** Preskill §§10.2.1–10.2.2 for entropy comparisons; [covariance and Gaussian bound, §3.2](../science/brownian-capacity.md#32-covariance-and-the-gaussian-entropy-upper-bound), equations (B28)–(B32). The Gaussian theorem and its primary attribution are given there.

### M17. The covariance spectrum bounds entropy per carrier

**Central question.** How does a finite sum over covariance modes become a valid large-block integral?

**Understanding target.** Relate the inverse covariance matrix's boundary conditions to its eigenvalues, then explain why the logarithmic endpoint singularity must be controlled before taking the Riemann-sum limit. Track the vanishing charge-register entropy per carrier.

**Dependencies and story role.** M14 and M16. This turns the finite-inner-block estimate into a Brownian achievable rate.

**Conceptual connection.** A bound on entropy per carrier emerges from collective covariance modes, with an explicit estimate covering the modes nearest the singular endpoint. The Gaussian comparison does not give an exact entropy formula for the actual environmental mixture.

**Source pointers.** Preskill §10.7.1 for the rate interpretation; [covariance spectrum, §3.3](../science/brownian-capacity.md#33-spectrum-of-the-discrete-brownian-covariance) and [controlled large-block limit, §3.4](../science/brownian-capacity.md#34-the-large-n-limit-with-the-endpoint-singularity-controlled).

### M18. The achievable square-root scale

**Central question.** Why does the Brownian entropy bound scale as the square root of the increment variance?

**Understanding target.** Explain the rescaling by $\sqrt{\kappa}$ in the entropy integral, the role of an integrable dominating function, and the origin of the coefficient $\pi/(4\ln2)$. Identify that coefficient as belonging to an achievable deficit bound.

**Dependencies and story role.** M11 and M17. This completes the Brownian achievability mechanism while keeping the optimization question open.

**Conceptual connection.** The small-noise scaling follows after the long-block limit; a fixed-input entropy calculation does not supply the converse or an optimal coefficient.

**Source pointers.** Preskill §10.7.1 for the lower-bound framework; [small-noise integral, §3.5](../science/brownian-capacity.md#35-small-noise-limit-and-the-integral-constant); [scope and antecedents, §5](../science/brownian-capacity.md#5-scope-and-inherited-ingredients).

### M19. A cleaner channel made of Brownian bridges

**Central question.** Which enhanced channel makes a universal Brownian converse tractable?

**Understanding target.** Decompose the phase into independent within-block bridges and endpoint interpolation. Explain how postprocessing a product of bridge channels with noiseless endpoint and tail slots reconstructs the actual channel, while counting every physical carrier once.

**Dependencies and story role.** M03, M09, and M12. The converse branch begins with an exact comparison between channels.

**Conceptual connection.** A code for the physical channel also works through the enhanced channel with the postprocessing absorbed into its decoder. Endpoints help prove an upper bound; they are not supplied to the actual code.

**Source pointers.** Preskill §§10.7.2–10.7.3 for data processing and channel comparison; [bridge degradation, §4.1](../science/brownian-capacity.md#41-exact-degradation-to-a-product-of-bridge-channels), equations (B43)–(B47).

### M20. A bridge of the right length loses fixed purity

**Central question.** Why is the relevant bridge length of order $\kappa^{-1/2}$?

**Understanding target.** Interpret the uniform-input complementary purity as an average of exponentials of a quadratic form. Explain how its first and second moments produce a nonzero purity loss when the bridge length has the chosen square-root scale.

**Dependencies and story role.** M05 and M19. This locates a fixed local loss inside an increasingly long block.

**Conceptual connection.** The covariance trace scales as variance times squared block length. This identifies a useful converse scale, but the resulting uniform-input calculation still needs an optimization argument.

**Source pointers.** Preskill §10.2.1 for entropy as a state property; [bridge moments and purity, §4.2](../science/brownian-capacity.md#42-uniform-input-purity-of-one-bridge), equations (B48)–(B53).

### M21. The entropy dichotomy covers every bridge input

**Central question.** How can a bound at the uniform input control all input distributions?

**Understanding target.** First use the diagonal-input reduction, then explain the two cases: an input distribution either already loses a fixed amount of classical entropy, or is close enough to uniform that the environmental purity loss persists. Locate the roles of Pinsker's inequality, trace-norm contraction, and the entropy lower bound from purity.

**Dependencies and story role.** M05, M09, M11, and M20. This is the step that converts a fixed-input observation into a converse uniform over input choices.

**Conceptual connection.** Changing the input cannot simultaneously recover maximal input entropy and erase the environmental distinction created by a bridge.

**Source pointers.** Preskill §§10.1.4 and 10.2.1 for relative entropy and entropy; [diagonal-input reduction, §2.1](../science/brownian-capacity.md#21-generalized-dephasing-its-complement-and-diagonal-inputs) and [input-uniform deficit, §4.3](../science/brownian-capacity.md#43-an-input-uniform-coherent-information-deficit), equations (B54)–(B59). The complete dichotomy is supplied locally.

### M22. Assemble the Brownian capacity law

**Central question.** How does a fixed loss per enhanced block imply the optimal deficit order of the original train?

**Understanding target.** Combine bridge additivity, noiseless endpoint accounting, and the finite-code fidelity bound for arbitrary CPTP encoders. Take the capacity limit and then combine the converse with achievability to obtain the two-sided square-root order.

**Dependencies and story role.** M09, M11, M18, and M21. This closes the Brownian argument as a complete operational theorem.

**Conceptual connection.** The number of bridge blocks converts a fixed information loss into a loss per carrier. Matching exponents leave the optimal leading coefficient and efficient finite-length codes undetermined.

**Source pointers.** Preskill §§10.7.2–10.7.3; [finite-code completion, §4.4](../science/brownian-capacity.md#44-completing-the-finite-code-and-capacity-bounds) and [Theorem B1](../science/brownian-capacity.md#theorem-b1), especially (B8) and (B12).

### M23. Resets divide the train into charge-sector segments

**Central question.** What channel remains when a reset pattern is fixed?

**Understanding target.** Explain why the segment phases are independent and uniform and why each segment undergoes a collective charge twirl. Construct the product sector-rank bound from the segment lengths while keeping the pattern inaccessible to the actual protocol.

**Dependencies and story role.** M03, M10, and M12. The reset branch starts with its local constant-phase pieces.

**Conceptual connection.** The noise now concentrates new phase uncertainty at random boundaries, unlike drift accumulating throughout a segment.

**Source pointers.** Preskill §§10.1.2 and 10.2.2 for independence and mixing; [conditional channels and ranks, §2](../science/reset-capacity.md#2-conditional-channels-and-their-sector-ranks), equations (R7)–(R9).

### M24. A coherent reset flag yields achievability

**Central question.** Why can the entropy of a classical reset pattern be used only as an upper bound on the quantum environment entropy?

**Understanding target.** Retain the reset record coherently in a channel isometry, then explain the entropy-increasing pinching that produces a classical pattern label. Identify the pattern entropy and binomial charge entropies, and use exact blocking to turn the bound into an achievable rate.

**Dependencies and story role.** M05–M06, M14, and M23. This supplies the reset lower bound without giving a reset record to the code.

**Conceptual connection.** Classical segmentation is useful after a justified entropy inequality; replacing the actual complementary state by a classical mixture as an equality would lose an essential step.

**Source pointers.** Preskill §§10.2.2 and 10.7.1; [reset achievability, §3](../science/reset-capacity.md#3-achievability-a-coherent-reset-flag-and-an-entropy-upper-bound), equations (R10)–(R17).

### M25. Sector ranks constrain every reset-channel code

**Central question.** How can the conditional segment structure bound fidelity even for a nonisometric encoder?

**Understanding target.** Follow the encoder, sector projector, and decoder through their Kraus branches. Explain the branch Schmidt-rank bound and its implication for overlap with an $M$-dimensional maximally entangled state, then average over reset patterns.

**Dependencies and story role.** M07, M10–M11, and M23. This gives a finite-length reset converse without optimizing a uniform-input coherent information.

**Conceptual connection.** Supplying the input-independent reset pattern to the receiver strengthens the channel for a converse. Even that decoder cannot increase the Schmidt rank allowed by a branch's sector projector.

**Source pointers.** Preskill §10.4 for pure-state entanglement and §10.7.2 for transmission fidelity; [arbitrary-encoder reset converse, §4](../science/reset-capacity.md#4-a-finite-length-converse-for-arbitrary-cptp-encoders), especially (R18)–(R21), with the primary Schmidt-number attribution given there.

### M26. Renewal averages include the unfinished last segment

**Central question.** How do random finite segments produce a reliable asymptotic loss per carrier?

**Understanding target.** Describe the complete geometric segments and the censored final segment in a finite train. Explain why the boundary reward becomes negligible at fixed $p$, and why bounded rewards give both almost-sure and expected per-carrier limits.

**Dependencies and story role.** M23–M25. This turns the random segment quantities in both reset bounds into deterministic asymptotic rates.

**Conceptual connection.** The common renewal calculation serves entropy rewards and logarithmic rank rewards. Its constants may depend on fixed noise, so it does not establish a joint finite-length, vanishing-noise theorem.

**Source pointers.** Preskill §10.1.1 for the law-of-large-numbers viewpoint; [boundary-safe renewal lemma, §5.1](../science/reset-capacity.md#51-a-boundary-safe-renewal-lemma), equations (R22)–(R24). The censored renewal argument is supplied by the project.

### M27. Assemble the logarithmic cost of rare resets

**Central question.** Why does each rare reset contribute a logarithmic redundancy cost?

**Understanding target.** Relate central sector dimension and binomial entropy to one-half the logarithm of segment length. Combine the geometric-length logarithm and renewal rates to obtain $1-Q_{\mathrm R}(p)=\Theta(p\log(1/p))$ from both sides.

**Dependencies and story role.** M24–M26. This closes the reset capacity argument.

**Conceptual connection.** Long constant-phase segments incur a sublinear charge-sector loss; rare boundaries accumulate those losses. The proven fidelity-decay threshold is an upper bound on capacity, not a demonstrated exact strong-converse threshold.

**Source pointers.** Preskill §§10.1.1 and 10.7.1 for entropy/rate interpretation; [sector entropy and dimension, §5.2](../science/reset-capacity.md#52-entropy-and-dimension-of-a-charge-sector) and [reset theorem, §1](../science/reset-capacity.md#1-model-operational-rate-and-theorem), equations (R5)–(R6).

### M28. Three selected slots cannot distinguish the models

**Central question.** Why does matching the first harmonic imply equality of the complete channels through three slots?

**Understanding target.** Set $p=1-e^{-\kappa/2}$ and use charge neutrality to bound every accessible suffix charge by one for at most three selected carriers. Include arbitrary integer gaps and passive reference systems in the channel identity.

**Dependencies and story role.** M03–M04 and M12. The two process definitions meet in a finite experimental equivalence.

**Conceptual connection.** Equality on all matrix units gives equality of the selected-carrier CPTP maps, which is stronger than matching one correlation function. It does not specify a different adaptive process interface with intervening probes.

**Source pointers.** Preskill §10.7.1 for the channel viewpoint; [selected-slot equality, §1](../science/indistinguishability.md#1-exact-equality-for-any-choice-of-at-most-three-slots), equations (C1)–(C6).

### M29. Four carriers reach the missing Fourier charge

**Central question.** What concrete experiment detects the difference hidden from all three-slot channels?

**Understanding target.** Prepare the equal superposition of $0011$ and $1100$, identify suffix charge two, and obtain the two coherence factors and sign-measurement probabilities. Explain why the preparation and measurement need no shared global phase reference.

**Dependencies and story role.** M02, M04, and M28. A realizable diagnostic gives the finite-slot equality an explicit boundary.

**Conceptual connection.** A selected higher-charge coherence probes information absent from lower-slot data. Strict distinguishability does not imply a constant single-trial advantage at vanishing noise or optimality of this probe among all four-carrier inputs.

**Source pointers.** Preskill §10.6.1 for the measurement-distinguishability viewpoint; [four-carrier diagnostic, §2](../science/indistinguishability.md#2-four-carriers-provide-an-explicit-diagnostic), equations (C7)–(C10).

### M30. Synthesis of short-probe equality and long-code separation

**Central question.** What does the complete result establish about learning a communication cost from small experiments?

**Understanding target.** Combine the two capacity laws at matched parameters to explain the diverging ratio of redundancy fractions, while both capacities approach one. Connect the identical channels through three slots, the four-slot witness, the common resource model, and the two different converse mechanisms.

**Dependencies and story role.** M12, M22, M27–M29. This completes the narrative as one operational statement with its scientific boundaries.

**Conceptual connection.** Short-channel equivalence does not determine optimal long-code redundancy. Separate inherited tools and the earlier Brownian entropy mechanism from the optimized fixed-qubit capacity consequence; distinguish analytical proof from finite diagnostics and scaling order from an exact coefficient or practical code.

**Source pointers.** Preskill §10.7 for the capacity framework; [capacity separation, §3](../science/indistinguishability.md#3-consequence-for-asymptotic-quantum-communication), equations (C11)–(C12); [related work](../references/related-work.md); [verification and its limits](../verification/README.md#relationship-to-the-proofs).
