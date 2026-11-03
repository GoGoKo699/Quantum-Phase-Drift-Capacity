# Scientific account

The central distinction is between noise seen by a few carriers and the information lost by a long, optimally encoded train. Every single-carrier marginal in this model is completely dephasing, yet temporal correlations allow the quantum communication rate to approach one qubit per slot. The way the phase changes determines how rapidly that limit is approached.

## Reading route

1. [Model and exact blocking](model-and-blocking.md) fixes the operational task, the order of limits and the resource count. Its matrix-element formula is the common starting point. The finite charge twirl produces independent coding blocks exactly.
2. [Brownian capacity](brownian-capacity.md) proves both sides of the square-root deficit law. The achievable bound uses the entropy of a mathematical environment; the converse optimizes over all code inputs using independent Brownian bridges.
3. [Reset capacity](reset-capacity.md) proves upper and lower rate bounds for a phase held constant between independent uniform resets. It includes a finite-length fidelity bound for arbitrary encoders and the renewal estimates behind the small-noise law.
4. [Indistinguishability and separation](indistinguishability.md) matches the two parameters, proves equality of every channel through three selected slots, and gives a physical four-carrier diagnostic. It combines the two capacity results to obtain an unbounded ratio of redundancy fractions.

The [related-work account](../references/related-work.md) separates standard tools and model ancestors from this specific consequence. [Reproduction checks](../verification/README.md) provide finite diagnostics of the load-bearing identities.

## What is optimized

Capacity is defined by entanglement transmission with arbitrary completely positive, trace-preserving block encoders and decoders. Both models use the same local carrier dimension and count every transmitted slot. The proofs do not grant the actual sender or receiver a phase trajectory, a reset record, preshared entanglement, or an auxiliary noiseless channel.

For Brownian drift, the theorem identifies the exponent of the optimal deficit. The Gaussian entropy estimate also supplies an achievable coefficient. It does not prove that a uniform input is globally optimal or determine the exact coefficient. For resets, the upper and lower bounds have matching order but different logarithmic coefficients. The explicit fidelity-decay threshold in the reset converse is an upper bound on capacity, rather than a claimed exact strong-converse threshold.

## Physical interpretation

An unknown constant phase removes coherence only between total-charge sectors. Encoding within a large sector therefore loses a sublinear number of logical qubits. Gradual Brownian drift creates additional local phase distinctions throughout the train. The converse identifies blocks of order $\kappa^{-1/2}$ carriers that incur a fixed unavoidable information loss. Rare resets instead create long constant-phase segments; their charge-sector losses accumulate at order $p\log(1/p)$ per carrier.

Matching all channels through three slots fixes only the Fourier charges that such probes can access. A four-slot neutral coherence reaches charge two and detects the difference. Thus the finite-slot equality has an explicit boundary, while the capacity statements concern arbitrary long codes.

The results are asymptotic in train length at fixed noise, followed by weak noise. They do not establish practical coding complexity, an exact finite-size rate, the effect of loss or additional noise, or capacities with feedback or classical assistance.
