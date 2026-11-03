# Finite verification

[check_phase_drift.py](check_phase_drift.py) checks finite instances of the channel identities, covariance decompositions, and entropy bounds used in the proofs. It also evaluates an integral whose value is derived analytically. The calculations are deterministic: they use complete enumeration of small bit-string and reset-pattern spaces, matrix diagonalization, and one-dimensional quadrature.

The recorded reference run passed **41 cases**. Full parameters, numerical outputs, tolerances, and software versions are in [expected-results.json](expected-results.json).

## Reproduce the calculations

From the repository root, install the dependencies and run:

~~~bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_phase_drift.py
~~~

The default command prints a JSON summary and writes no results file. To save every checked case:

~~~bash
python3 verification/check_phase_drift.py --output verification/results.json
~~~

The output path is optional and relative to the current working directory. The script can also be invoked by its absolute path from another directory; it contains no fixed workspace paths. Importing the module does not run the diagnostics or write files.

A failed check raises an explicit exception and returns a nonzero process exit status. Checks remain active when Python optimization is enabled; they do not use Python's removable assertion statements.

### Requirements and recorded environment

[requirements.txt](requirements.txt) specifies NumPy **≥1.24** and SciPy **≥1.10**. The reference output was produced with:

| Component | Version |
|---|---|
| Python | 3.12.14 |
| NumPy | 2.3.5 |
| SciPy | 1.17.0 |

The dependency ranges are not an exact environment lock. Other compatible installations may produce slightly different final floating-point digits. The script checks the analytical identities and inequalities against explicit tolerances; it does not require a byte-for-byte match with the reference JSON.

## Coverage and parameter sets

Here $n$ is the number of qubit carriers, $\kappa$ is the Brownian increment variance, $L$ is the endpoint spacing in the bridge construction, and $p$ is the reset probability. When the two models are compared at a common $\kappa$, the reset parameter is $p=1-e^{-\kappa/2}$.

| Diagnostic | Cases | Tested parameters | Checked statement |
|---|---:|---|---|
| Channels on at most three selected slots | 9 | $n=1,2,3$; $\kappa=0.001,0.1,0.7$. Integer gap lists are respectively empty, $(2)$, and $(2,3)$. | Every entry of the Brownian and matched-reset Schur matrices agrees. |
| Independent block twirling | 6 | Both models; block sizes $(1,2),(2,2),(2,3)$; $\kappa=0.17$. | Applying separate charge twirls to the joint channel gives the tensor product of standalone block channels. |
| Gaussian entropy upper bound | 12 | $n=2,3,4,6$; $\kappa=0.01,0.1,0.5$. | The uniform-input complementary entropy, obtained from the normalized Gram matrix, is bounded by the binomial weight entropy plus the Gaussian covariance bound. |
| Bridge moments and purity | 4 | $L=2,3,4,6$; $\kappa=1/(L^2-1)$. | Direct bit-string enumeration verifies the mean quadratic form, its second-moment bound, and the resulting purity gap. |
| Four-slot witness | 1 | Four consecutive slots; $\kappa=0.2$. | The $\lvert0011\rangle\langle1100\rvert$ multipliers equal $e^{-3\kappa}$ and $e^{-3\kappa/2}$, respectively. |
| Entropy integral | 1 | Quadrature over $u\in(0,\infty)$. | The integral in the achievable coefficient agrees with $\pi^2/(4\ln2)$. |
| Brownian covariance degradation | 4 | $(n,L,\kappa)=(2,2,0.03),(5,2,0.2),(6,3,0.5),(7,3,0.07)$. | Independent bridge and interpolation/tail covariances reconstruct the original covariance, and their channel composition reproduces the original Schur matrix. |
| Reset-pattern enumeration and pinching | 4 | $(n,p)=(1,0.1),(2,0.05),(4,0.2),(5,0.6)$. | Explicit segment-twirl mixtures agree with the increment formula; coherent environment vectors have the correct Gram matrix; pinching the reset flag gives the stated entropy upper bound. |
| **Total** | **41** | | |

The largest selected-carrier Schur matrix is $128\times128$, at $n=7$. The reset checks enumerate $1,2,8,$ and $16$ reset patterns, respectively, for **27 patterns in total**. Their explicitly constructed environment dimensions are $2,7,82,$ and $280$.

The degradation cases include both complete block tilings and a one-slot tail. The tail is noiseless in the enhanced bridge channel and acquires its original correlated phase in the postprocessing. The reset-environment calculation retains coherence between reset records before pinching, rather than assuming that the complementary state is initially block diagonal.

## Reference numerical results

These values summarize the full output in [expected-results.json](expected-results.json).

| Quantity | Recorded value |
|---|---:|
| Largest difference in the nine selected-slot comparisons | $0$ |
| Largest difference in the six block-factorization comparisons | $0$ |
| Largest Brownian covariance reconstruction residual | $2.220446049250313\times10^{-16}$ |
| Largest bridge/postprocessing cross covariance | $5.551115123125783\times10^{-17}$ |
| Largest Brownian channel-composition residual | $2.220446049250313\times10^{-16}$ |
| Largest reset enumeration/Schur residual | $2.220446049250313\times10^{-16}$ |
| Largest reset pinching entropy-formula residual | $8.881784197001252\times10^{-16}$ |

The algebra tolerance is $10^{-12}$, the entropy tolerance is $10^{-10}$, and the integral comparison tolerance is $10^{-6}$. Numerical positivity checks permit eigenvalues down to $-10^{-12}$, accommodating roundoff at singular matrices. A recorded zero is a floating-point result; the exact identity comes from its proof.

For the specified four-carrier probe at $\kappa=0.2$, the Brownian and reset coherence multipliers are **0.5488116360940264** and **0.7408182206817179**. Its equal-prior single-trial discrimination success probability is **0.5480016461469228**. This is the performance of the stated probe and measurement, not an optimization over all four-carrier experiments.

Writing $g(z)=(z+1)\log_2(z+1)-z\log_2z$, the integral check evaluates

```math
\int_0^\infty
g\!\left(\frac{\sqrt{1+u^{-2}}-1}{2}\right)\,du
=\frac{\pi^2}{4\ln2}.
```

The numerical result is **3.559707331246877**, compared with **3.559707331246876** from the analytical expression. SciPy's estimated quadrature error is $1.1757927964595183\times10^{-10}$; this estimate is not a rigorous error certificate. Dividing the integral by $\pi$ gives **1.1330900354567988**, the coefficient $\pi/(4\ln2)$ in the achievable entropy bound.

## Relationship to the proofs

The authoritative mathematical arguments and operational assumptions are in:

- [Model and exact block reduction](../science/model-and-blocking.md): carrier resources, capacity definition, Schur multipliers, and exact input twirling.
- [Brownian capacity](../science/brownian-capacity.md): the Gaussian entropy bound, analytical integral, bridge degradation, and converse covering arbitrary encoders.
- [Reset capacity](../science/reset-capacity.md): coherent environment pinching, renewal boundary terms, and the finite-length Schmidt-number converse.
- [Selected-slot indistinguishability](../science/indistinguishability.md): equality for arbitrary choices of at most three slots and the explicit four-slot diagnostic.

The finite calculations can expose indexing, normalization, covariance, or entropy-inequality mistakes in the checked cases. They do not establish the universal identities for all train lengths or gaps. In particular, these diagnostics do not numerically test every input distribution or substitute for either channel's coding converse.

No quantum code is simulated, no capacity curve is fitted, and no optimal leading coefficient is inferred. The Gaussian bound can exceed the input entropy for a small block without invalidating the inequality; such a bound need not furnish a positive achievable rate at that block size. The coefficient obtained from the integral belongs to an achievable upper bound on the Brownian deficit, not a claimed exact capacity coefficient.

The capacity theorems first take train length to infinity at each fixed positive noise parameter, then study the small-noise limit. These finite checks do not establish a uniform joint finite-length/small-noise theorem. They also make no claim about a stronger adaptive process interface, feedback assistance, or additional uncounted probes.
