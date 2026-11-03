# Carrier model, operational capacity, and exact block factorization

This section fixes the resource model and slot conventions used in the Brownian and reset capacity proofs. All logarithms are to base two unless explicitly written as natural logarithms.

## 1. One qubit in each carrier slot

The input and output spaces for a train of $`N`$ carriers are

```math
\mathcal H_N=(\mathbb C^2)^{\otimes N}.
```

Carrier $`j\in\lbrace 1,\ldots,N\rbrace `$ experiences the unitary

```math
U(\theta_j)=|0\rangle\langle0|+e^{i\theta_j}|1\rangle\langle1|.
\qquad\text{(M1)}
```

Let $`\theta_0`$ be uniform on $`[0,2\pi)`$, and let $`\xi_1,\xi_2,\ldots`$ be independent, identically distributed phase increments, independent of $`\theta_0`$. Define

```math
\theta_j=\theta_0+\sum_{k=1}^j\xi_k.
\qquad\text{(M2)}
```

Only $`\theta_j\bmod2\pi`$ affects (M1). For Gaussian increments we retain the real lift in (M2), which makes the Brownian-bridge decomposition exact. The physical averaged channel is

```math
\mathcal N_N(\rho)
=\mathbb E\!\left[
\left(\bigotimes_{j=1}^N U(\theta_j)\right)
\rho
\left(\bigotimes_{j=1}^N U(\theta_j)\right)^\dagger
\right].
\qquad\text{(M3)}
```

The phase process is classical and independent of the transmitted state. Neither party receives its realization. There is no preshared entanglement, feedback, auxiliary communication channel, or phase record. Arbitrary local quantum operations and ancillary systems are permitted at the encoder and decoder. Each transmitted physical system is exactly one qubit; every slot, including a pilot or dummy carrier, is counted in $`N`$. The model has no loss or additional noise.

The stationary $`N`$-slot law can equivalently be described by a uniform $`\theta_1`$ and the $`N-1`$ increments $`\xi_2,\ldots,\xi_N`$. The increment $`\xi_1`$ is absorbed into the uniform first phase. We keep the virtual time-zero variable $`\theta_0`$, with no carrier at time zero, because the converse will place bridge endpoints at $`0,L,2L,\ldots`$.

For Brownian drift,

```math
\xi_j\sim\mathcal N(0,\kappa),\qquad \kappa\ge0.
\qquad\text{(M4)}
```

For the reset comparison,

```math
\xi_j\sim(1-p)\delta_0+p\,\mathrm{Unif}[0,2\pi),\qquad0\lt p\lt 1.
\qquad\text{(M5)}
```

The increments are independent in both definitions. The resulting carrier noises are correlated because each phase contains all previous increments.

## 2. Operational entanglement-transmission capacity

An $`(N,M)`$ code consists of completely positive, trace-preserving maps

```math
\begin{aligned}
\mathcal E_N&:\mathcal B(\mathbb C^M)\longrightarrow\mathcal B(\mathcal H_N),\\
\mathcal D_N&:\mathcal B(\mathcal H_N)\longrightarrow\mathcal B(\mathbb C^M).
\end{aligned}
\qquad\text{(M6)}
```

The encoder may be nonisometric and may use local randomness. The decoder is a joint operation on the received train. They can depend on the known noise law and on $`N`$, but not on the realized phases. There are no intermediate sender–receiver messages.

For a reference $`R\simeq\mathbb C^M`$, let

```math
|\Phi_M\rangle_{RA}
=\frac1{\sqrt M}\sum_{a=1}^M|a\rangle_R|a\rangle_A.
```

The entanglement fidelity is the singlet fraction

```math
\begin{aligned}
&F_e(N,M,\mathcal E_N,\mathcal D_N)\\
&\quad=\langle\Phi_M|
\bigl[\mathrm{id}_R\otimes
(\mathcal D_N\circ\mathcal N_N\circ\mathcal E_N)\bigr]\\
&\qquad(|\Phi_M\rangle\langle\Phi_M|)
|\Phi_M\rangle.
\end{aligned}
\qquad\text{(M7)}
```

A rate $`R_0\ge0`$ is achievable if a sequence of codes satisfies

```math
\begin{aligned}
&\liminf_{N\to\infty}\frac{\log M_N}{N}\ge R_0,\\
&F_e(N,M_N,\mathcal E_N,\mathcal D_N)\longrightarrow1.
\end{aligned}
\qquad\text{(M8)}
```

The unassisted capacity $`Q`$ is the supremum of achievable rates, in logical qubits per physical carrier. It lies in $`[0,1]`$. The fidelity in (M7) already averages over the stochastic phase process through the channel (M3); a worst-case guarantee for every phase trajectory is not claimed.

The noise parameter is fixed while $`N\to\infty`$. Small-$`\kappa`$ or small-$`p`$ asymptotics are taken after this capacity limit. The results below do not assert a joint finite-$`N`$, vanishing-noise estimate, nor a computationally efficient encoder or decoder.

## 3. Exact matrix elements of the correlated channel

For $`x,y\in\lbrace 0,1\rbrace ^N`$, write

```math
a_j=x_j-y_j,\qquad
w(x)=\sum_{j=1}^N x_j,\qquad
s_k(x)=\sum_{j=k}^N x_j.
```

Let

```math
f(q)=\mathbb E e^{iq\xi_1},\qquad q\in\mathbb Z,
\qquad\text{(M9)}
```

be the increment's characteristic function at integer charges. Substituting (M2),

```math
\sum_{j=1}^N a_j\theta_j
=\theta_0\sum_{j=1}^N a_j
+\sum_{k=1}^N\xi_k\sum_{j=k}^N a_j.
```

The uniform initial phase and independence of the increments therefore give

```math
\mathcal N_N(|x\rangle\langle y|)
=c_N(x,y)|x\rangle\langle y|,
```

```math
c_N(x,y)
=\mathbf1_{w(x)=w(y)}
\prod_{k=1}^N f\bigl(s_k(x)-s_k(y)\bigr).
\qquad\text{(M10)}
```

The first factor in the product is $`f(0)=1`$ whenever the prefactor is nonzero, so the product may equivalently start at $`k=2`$. This is the precise reason that the first increment is redundant for the stationary train.

For Brownian drift, $`f(q)=e^{-\kappa q^2/2}`$, hence

```math
c_N^{\mathrm B}(x,y)
=\mathbf1_{w(x)=w(y)}
\exp\!\left[-\frac\kappa2
\sum_{k=1}^N\bigl(s_k(x)-s_k(y)\bigr)^2\right].
\qquad\text{(M11)}
```

For resets, $`f(0)=1`$ and $`f(q)=1-p`$ for every nonzero integer $`q`$.

## 4. A finite phase grid implements the exact charge twirl

For a block of $`n`$ carriers, define the total-charge operator

```math
W_n=\sum_{j=1}^n |1\rangle\langle1|_j.
```

Its eigenvalues are $`0,1,\ldots,n`$. Define

```math
\mathcal T_n(\rho)
=\frac1{n+1}\sum_{r=0}^{n}
e^{2\pi i rW_n/(n+1)}\rho
e^{-2\pi i rW_n/(n+1)}.
\qquad\text{(M12)}
```

For computational basis vectors,

```math
\frac1{n+1}\sum_{r=0}^n
e^{2\pi i r(w(x)-w(y))/(n+1)}
=\mathbf1_{w(x)=w(y)}.
\qquad\text{(M13)}
```

Indeed, the finite Fourier sum vanishes unless the charge difference is a multiple of $`n+1`$, and its magnitude cannot exceed $`n`$. Consequently

```math
\mathcal T_n(\rho)=\sum_{w=0}^n\Pi_w\rho\Pi_w,
\qquad\text{(M14)}
```

where $`\Pi_w`$ is the weight-$`w`$ projector. Thus $`n+1`$ equally spaced phase values suffice; an ideal continuous random number or a shared random seed is unnecessary. The random choice is local to the sender and is forgotten. Equivalently, the sender can perform and discard a measurement of total charge.

## 5. Exact factorization over coding blocks

### Proposition M1

For every increment law in (M2), every block length $`n\ge1`$, and every number of blocks $`b\ge1`$,

```math
\boxed{
\mathcal N_{bn}\circ\mathcal T_n^{\otimes b}
=\mathcal N_n^{\otimes b}.}
\qquad\text{(M15)}
```

This is an equality of channels on the entire $`bn`$-qubit input space. It holds for inputs entangled across blocks and with external reference systems.

#### Proof

Partition a basis matrix element $`|x\rangle\langle y|`$ into $`b`$ consecutive blocks. Let the total charge difference of block $`r`$ be $`A_r`$.

If some $`A_r\ne0`$, the left side of (M15) vanishes because of $`\mathcal T_n^{\otimes b}`$. The right side also vanishes because that block's factor $`\mathcal N_n`$ contains the uniform-phase prefactor in (M10).

Now suppose $`A_r=0`$ for every block. A global suffix beginning inside block $`r`$ is the sum of its suffix within that block and the total differences of every later block. The latter totals are all zero. Thus every global suffix charge equals its corresponding within-block suffix charge. The product in (M10) separates exactly into the $`b`$ within-block products. The uniform initial-phase prefactor is one, and the corresponding initial-phase prefactor of each block is also one. This proves equality on each matrix unit and hence on every operator. Tensoring the equality with an identity map proves the reference-system statement. $`\square`$

The proposition uses no waiting interval, bath reset, knowledge of a phase realization, or approximation by weakly correlated blocks. Each block contains exactly $`n`$ of the charged physical slots. The inserted twirl is a permitted encoder operation and may reduce the channel's ability to transmit; its purpose is to make a rigorous achievable rate available.

## 6. Consequence for coding

Let 

```math
I_c(\rho,\mathcal M)
=S(\mathcal M(\rho))-S(\mathcal M^c(\rho))
\qquad\text{(M16)}
```

denote coherent information, for any complementary channel $`\mathcal M^c`$. For a fixed inner block $`n`$, the ordinary quantum coding theorem for the finite-dimensional memoryless channel $`\mathcal N_n`$ makes every nonnegative rate strictly below $`I_c(\rho,\mathcal N_n)`$ achievable per use of that block channel [D](../references/related-work.md#d). Equation (M15) realizes those independent uses through the original correlated train by composing the outer encoder with $`\mathcal T_n^{\otimes b}`$. Therefore

```math
Q\ge \sup_{n\ge1}\frac1n
\max\left\{0,\max_\rho I_c(\rho,\mathcal N_n)\right\}.
\qquad\text{(M17)}
```

Only the lower bound is needed here; (M17) is not being used as an assumed general memory-channel capacity formula.

The codes provided initially have lengths $`bn`$. To obtain a sequence for all $`N`$, use $`b=\lfloor N/n\rfloor`$ complete blocks, append a fixed state on the fewer than $`n`$ remaining carriers, and discard their outputs. The first $`bn`$ carriers have exactly the channel $`\mathcal N_{bn}`$, because the classical phase process has no input-dependent back-action. At fixed $`n`$, this changes the rate by $`o(1)`$. The order is therefore: fix the noise parameter and the inner block $`n`$, take the outer code length $`b\to\infty`$, and only then optimize or take $`n\to\infty`$.

In particular, a finite-inner-block estimate

```math
I_c(2^{-n}I,\mathcal N_n)\ge n-B_n
```

proves an achievable asymptotic rate at least $`\max\lbrace 0,1-B_n/n\rbrace `$. It is not, by itself, an explicit finite-outer-length error estimate.

## Inherited ingredients

Coherent-information achievability uses the ordinary quantum coding theorem [D](../references/related-work.md#d) after the exact independent-block construction. Generalized dephasing, diagonal input reduction, and degradability are established ingredients [DBF](../references/related-work.md#dbf). The exact finite-grid identity and block factorization are proved above rather than inferred from decay of noise correlations.

Full bibliographic entries and source locations are collected in [related work](../references/related-work.md).
