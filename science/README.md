# Scientific account

Every single-carrier marginal in this model is completely dephasing. Temporal correlations can still support a quantum communication rate close to one qubit per slot. How the phase changes determines the redundancy needed to approach that limit. Even complete channel data on a growing number of carriers can leave that redundancy ambiguous.

## Reading route

1. [Model and exact blocking](model-and-blocking.md) fixes the operational task, the order of limits and the resource count. Its matrix-element formula is the common starting point. The finite charge twirl produces independent coding blocks exactly.
2. [Brownian capacity](brownian-capacity.md) proves both sides of the square-root deficit law. The achievable bound uses the entropy of a mathematical environment; the converse optimizes over all code inputs using independent Brownian bridges.
3. [Reset capacity](reset-capacity.md) proves upper and lower rate bounds for a phase held constant between independent uniform resets. It includes a finite-length fidelity bound for arbitrary encoders and the renewal estimates behind the small-noise law.
4. [Indistinguishability and separation](indistinguishability.md) matches the two parameters, proves equality of every channel through three selected slots, and gives a physical four-carrier diagnostic. It combines the two capacity results to obtain an unbounded ratio of redundancy fractions.
5. [Discrimination and entanglement depth](discrimination-and-depth.md) proves optimality on any four fixed slots and determines the consecutive train length needed at fixed error. The lower bounds cover joint readout, and the constructions attain them at each input entanglement depth.
6. [Growing diagnostic window](growing-diagnostics.md) constructs two smooth phase processes with exactly matched channels through $2r+1$ carriers, a first difference at $2r+2$, and parametrically different capacity deficits. It also bounds the absolute capacity using the optimized coherent information of any finite block in the independent-increment model.

The [related-work account](../references/related-work.md) separates standard tools and model ancestors from this specific consequence. [Reproduction checks](../verification/README.md) provide finite diagnostics of the load-bearing identities.

## What is optimized

Capacity is defined by entanglement transmission with arbitrary completely positive, trace-preserving block encoders and decoders. Both models use the same local carrier dimension and count every transmitted slot. The proofs do not grant the actual sender or receiver a phase trajectory, a reset record, preshared entanglement, or an auxiliary noiseless channel.

For Brownian drift, the theorem identifies the exponent of the optimal deficit. The Gaussian entropy estimate also supplies an achievable coefficient. It does not prove that a uniform input is globally optimal or determine the exact coefficient. For resets, the upper and lower bounds have matching order but different logarithmic coefficients. The explicit fidelity-decay threshold in the reset converse is an upper bound on capacity, rather than a claimed exact strong-converse threshold.

For discrimination, the $N$ carriers are consecutive, with one pass per carrier and no feedback. The two matched parameter values are supplied. At fixed error, the shortest train with input entanglement depth at most $d$ has order $\max\left(\kappa^{-1/3},(\kappa d)^{-1/2}\right)$. Depth constrains the input groups and their private references. The receiver can measure jointly. The capacity law quantifies the coding overhead for each process. The discrimination law quantifies the train needed to identify which process applies.

## Physical interpretation

An unknown constant phase removes coherence only between total-charge sectors. Encoding within a large sector therefore loses a sublinear number of logical qubits. Gradual Brownian drift creates additional local phase distinctions throughout the train. The converse identifies blocks of order $\kappa^{-1/2}$ carriers that incur a fixed unavoidable information loss. Rare resets instead create long constant-phase segments; their charge-sector losses accumulate at order $p\log(1/p)$ per carrier.

Total-charge balance limits the Fourier harmonics accessible to an $m$-carrier probe to order $\lfloor m/2\rfloor$. For Brownian drift and uniform resets, the first separating coherence reaches charge two on four carriers. In the growing-window construction, a signed periodic differentiation stencil is split into two compound-Poisson generators. One Gaussian component compensates for their difference on the accessible harmonics. A finite block still bounds absolute capacity because removing interblock phase correlations costs at most the entropy of one discrete phase key per block.

The capacity limits take long trains at fixed noise first. The discrimination result fixes a target error and studies train length as the noise weakens. Both use the same ideal phase-only channel.
