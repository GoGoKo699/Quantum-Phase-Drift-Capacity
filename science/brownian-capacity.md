# The quantum-capacity cost of Brownian phase drift

The carrier model and the operational entanglement-transmission capacity are defined in [model-and-blocking.md](model-and-blocking.md). In particular, there is one qubit in each charged slot, the initial phase is uniform, and the independent real phase increments have variance $`\kappa`$. Arbitrary CPTP encoders and collective decoders are allowed, with no feedback or access to the phase realization. All entropies and capacities below are in bits.

The proof consists of a finite-inner-block achievable bound and a finite-train converse valid for arbitrary codes. It does not assume that the maximally mixed input optimizes a correlated dephasing channel.

## 1. Main theorem and explicit bounds

Define the bosonic entropy function

```math
g(z)=(z+1)\log_2(z+1)-z\log_2z,\qquad z\ge0,
\qquad\text{(B1)}
```

with $`g(0)=0`$. For $`\kappa>0`$, define

```math
h(\kappa)=\frac1\pi\int_0^\pi
g\!\left(
\frac{\sqrt{1+\kappa/[4\sin^2(t/2)]}-1}{2}
\right)\,dt.
\qquad\text{(B2)}
```

The singularity at zero is integrable, as proved below. Set

```math
\begin{aligned}
a_0&=\frac7{96},\qquad
\delta=\frac{a_0^2}{32\ln2}
=\frac{49}{294912\ln2}>0,\\
L_\kappa&=\left\lceil\sqrt{1+\kappa^{-1}}\right\rceil.
\end{aligned}
\qquad\text{(B3)}
```

### Theorem B1

The Brownian phase-train capacity $`Q_{\mathrm B}(\kappa)`$ satisfies

```math
Q_{\mathrm B}(\kappa)\ge\max\{0,\,1-h(\kappa)\}
\qquad(\kappa>0),
\qquad\text{(B4)}
```

and

```math
Q_{\mathrm B}(\kappa)\le
1-\frac{\delta}{L_\kappa}
\qquad(0\lt \kappa\le1).
\qquad\text{(B5)}
```

Moreover,

```math
\lim_{\kappa\downarrow0}\frac{h(\kappa)}{\sqrt\kappa}
=\frac{\pi}{4\ln2}.
\qquad\text{(B6)}
```

Consequently,

```math
\boxed{1-Q_{\mathrm B}(\kappa)=\Theta(\sqrt\kappa)}
\qquad(\kappa\downarrow0).
\qquad\text{(B7)}
```

More explicitly,

```math
\begin{aligned}
\delta
&\le
\liminf_{\kappa\downarrow0}
\frac{1-Q_{\mathrm B}(\kappa)}{\sqrt\kappa}\\
&\le
\limsup_{\kappa\downarrow0}
\frac{1-Q_{\mathrm B}(\kappa)}{\sqrt\kappa}
\le\frac{\pi}{4\ln2}.
\end{aligned}
\qquad\text{(B8)}
```

Neither the existence nor the value of an optimal leading coefficient is asserted. The number $`\pi/(4\ln2)`$ comes from the achievable entropy bound. The converse constant $`\delta`$ is deliberately conservative.

At $`\kappa=0`$, the channel is a single collective phase twirl, and $`Q_{\mathrm B}(0)=1`$.

### Finite-inner-block achievable bound

For every integer $`n\ge1`$, put

```math
B_n(\kappa)=\log_2(n+1)+
\sum_{j=1}^n
g\!\left(
\frac{\sqrt{1+\kappa\lambda_{j,n}}-1}{2}
\right),
\qquad\text{(B9)}
```

where

```math
\lambda_{j,n}
=\frac1{4\sin^2\!\left((2j-1)\pi/(4n+2)\right)}.
\qquad\text{(B10)}
```

Then

```math
\begin{aligned}
I_c(2^{-n}I,\mathcal N_n^{\mathrm B})
&\ge n-B_n(\kappa),\\
Q_{\mathrm B}(\kappa)
&\ge\sup_{n\ge1}\max\left\{0,1-\frac{B_n(\kappa)}n\right\}.
\end{aligned}
\qquad\text{(B11)}
```

For a fixed $`n`$, the rate in (B11) is achieved asymptotically by an ordinary outer quantum code on repeated $`n`$-slot blocks, made independent by the exact local twirls of Proposition M1. Equation (B11) is a finite-inner-block entropy bound, not an explicit finite-outer-length rate/error tradeoff.

### Finite-train converse

For $`0\lt \kappa\le1`$, every $`(N,M)`$ code with entanglement fidelity at least $`1-\varepsilon`$, where $`0\le\varepsilon\lt 1/4`$, obeys

```math
\boxed{
(1-4\varepsilon)\log_2M
\le
N-\delta\left\lfloor\frac{N}{L_\kappa}\right\rfloor
+2h_2(\varepsilon).}
\qquad\text{(B12)}
```

Here $`h_2`$ is binary entropy. The encoder need not be an isometry, diagonal, or uniform. Equation (B12) is a weak converse sufficient for the capacity upper bound; a strong converse at the unknown exact Brownian capacity is not claimed.

## 2. Finite-dimensional channel facts used in the proof

We record the needed standard facts with their short proofs so that the arbitrary-code scope is explicit. Generalized dephasing and its use for memory channels are inherited from [DBF](../references/related-work.md#dbf).

### 2.1 Generalized dephasing, its complement, and diagonal inputs

A generalized dephasing channel has an isometry of the form

```math
V|x\rangle=|x\rangle_B|e_x\rangle_E,
\qquad\text{(B13)}
```

where the environment vectors are normalized but need not be orthogonal. Its action and a complement are

```math
\begin{aligned}
\mathcal M(\rho)
&=\sum_{x,y}\rho_{xy}\langle e_y|e_x\rangle
|x\rangle\langle y|,\\
\mathcal M^c(\rho)
&=\sum_x\rho_{xx}|e_x\rangle\langle e_x|.
\end{aligned}
\qquad\text{(B14)}
```

Measuring the output in the $`x`$ basis and preparing $`|e_x\rangle`$ reproduces $`\mathcal M^c`$, so $`\mathcal M`$ is degradable. Its complement is entanglement breaking.

Let $`p_x=\rho_{xx}`$. The complement in (B14) depends only on $`p`$, and pinching the channel output in this basis increases its entropy:

```math
S(\mathcal M(\rho))\le H(p).
```

For the diagonal input $`\rho_p=\sum_xp_x|x\rangle\langle x|`$, equality holds. Hence

```math
\max_\rho I_c(\rho,\mathcal M)
=\max_p\left[
H(p)-S\!\left(\sum_xp_x|e_x\rangle\langle e_x|\right)
\right].
\qquad\text{(B15)}
```

This permits arbitrary correlated distributions $`p`$. It supplies no justification for replacing the maximization by the uniform distribution.

### 2.2 Additivity of maximized coherent information for degradable factors

Write

```math
J(\mathcal M)=\max_\rho I_c(\rho,\mathcal M).
\qquad\text{(B16)}
```

If $`\mathcal M_1,\mathcal M_2`$ are degradable and a joint input produces output $`B_1B_2`$ and environment $`E_1E_2`$, then

```math
\begin{aligned}
&I_c(\rho_{12},\mathcal M_1\otimes\mathcal M_2)\\
&\quad=I_c(\rho_1,\mathcal M_1)+I_c(\rho_2,\mathcal M_2)\\
&\qquad-I(B_1:B_2)+I(E_1:E_2).
\end{aligned}
\qquad\text{(B17)}
```

The state on $`E_1E_2`$ is obtained by applying the local degrading maps to $`B_1B_2`$. Mutual-information data processing gives $`I(E_1:E_2)\le I(B_1:B_2)`$. Product inputs attain the reverse inequality after maximization, so

```math
J(\mathcal M_1\otimes\mathcal M_2)
=J(\mathcal M_1)+J(\mathcal M_2).
\qquad\text{(B18)}
```

The argument includes arbitrary entanglement between the channel inputs. Iteration covers any finite number of factors, and $`J(\mathrm{id}_{2^r})=r`$.

### 2.3 A finite-code bound for arbitrary CPTP encoders

For any finite-dimensional channel $`\mathcal M`$, an $`M`$-dimensional entanglement-transmission code with $`F_e\ge1-\varepsilon`$, $`0\le\varepsilon\lt 1/4`$, satisfies

```math
(1-4\varepsilon)\log_2M
\le J(\mathcal M)+2h_2(\varepsilon).
\qquad\text{(B19)}
```

To prove this, let $`\omega_{RA}`$ be the encoded reference–input state. It may be mixed. Decompose it into pure states,

```math
\omega_{RA}=\sum_zp_z|\psi_z\rangle\langle\psi_z|.
```

Conditional entropy is concave, so coherent information $`I(R\rangle B)=-S(R|B)`$ is convex in the joint state. Applying the channel gives

```math
\begin{aligned}
I(R\rangle B)
&\le\sum_zp_z I(R\rangle B)_{(\mathrm{id}\otimes\mathcal M)(\psi_z)}\\
&=\sum_zp_z I_c(\rho_A^{(z)},\mathcal M)\\
&\le J(\mathcal M).
\end{aligned}
\qquad\text{(B20)}
```

This argument does not impose any restriction on the encoder. Coherent-information data processing under the decoder implies $`I(R\rangle\widehat A)\le I(R\rangle B)`$.

Let $`\tau_{R\widehat A}`$ be the decoded state. Its reference marginal remains $`I_M/M`$. The quantum-Fano entropy bound [S](../references/related-work.md#s) for a state with overlap at least $`1-\varepsilon`$ with the pure state $`\Phi_M`$ is

```math
S(\tau_{R\widehat A})
\le h_2(\varepsilon)+\varepsilon\log_2(M^2-1)
\qquad(M\ge2).
\qquad\text{(B21)}
```

One may obtain (B21) by pinching with the projections onto $`\Phi_M`$ and its orthogonal complement, and maximizing the entropy within the latter. The entropy bound is increasing in the actual error throughout $`0\le\varepsilon\lt 1/4`$. Araki–Lieb now yields

```math
\begin{aligned}
I(R\rangle\widehat A)
&=S(\widehat A)-S(R\widehat A)\\
&\ge\log_2M-2S(R\widehat A)\\
&\ge(1-4\varepsilon)\log_2M-2h_2(\varepsilon),
\end{aligned}
\qquad\text{(B22)}
```

where $`\log_2(M^2-1)\le2\log_2M`$ was used. Equations (B20)–(B22) prove (B19). The $`M=1`$ case is trivial.

An equivalent check specialized to generalized dephasing is to purify the encoder with an environment $`F`$. Its state with the channel environment $`E`$ is separable because $`\mathcal M^c`$ is entanglement breaking, so $`S(F|E)\ge0`$. Purity of $`RFBE`$ then gives $`I(R\rangle B)\le I_c(\rho_A,\mathcal M)\le J(\mathcal M)`$.

## 3. Achievability from complementary entropy

### 3.1 An exact coherent-state dilation

For an $`n`$-bit string $`x`$, let $`w(x)`$ and $`s_k(x)`$ be its total weight and suffix sums. Define

```math
|e_x\rangle
=|w(x)\rangle_W
\otimes\bigotimes_{k=1}^n|\sqrt\kappa\,s_k(x)\rangle_k,
\qquad\text{(B23)}
```

where the first register has orthonormal states $`|0\rangle,\ldots,|n\rangle`$, and the other factors are normalized oscillator coherent states with real amplitudes. Their overlap is

```math
\langle\beta|\alpha\rangle
=e^{-(\alpha-\beta)^2/2}
\qquad(\alpha,\beta\in\mathbb R).
\qquad\text{(B24)}
```

Consequently,

```math
\langle e_y|e_x\rangle
=\mathbf1_{w(x)=w(y)}
\exp\!\left[-\frac\kappa2
\sum_{k=1}^n(s_k(x)-s_k(y))^2\right],
\qquad\text{(B25)}
```

which is exactly the Schur multiplier of $`\mathcal N_n^{\mathrm B}`$. Therefore $`V|x\rangle=|x\rangle|e_x\rangle`$ is a Stinespring isometry for the physical channel.

The first oscillator, whose amplitude is $`\sqrt\kappa\,w(x)`$, is redundant once the orthogonal weight register has been included: it changes no overlap. Including it gives the convenient covariance matrix below and only loosens the entropy estimate. These oscillators are mathematical dilation variables; they are not physical carriers, auxiliary signals, or a supplied bosonic resource.

For the uniform input, let $`X`$ be uniform on $`\lbrace 0,1\rbrace ^n`$. The complementary state is

```math
\rho_E=2^{-n}\sum_x|e_x\rangle\langle e_x|.
\qquad\text{(B26)}
```

Its weight marginal is classical, and subadditivity gives

```math
\begin{aligned}
S(\rho_E)
&\le H(w(X))+S(\rho_{\mathrm{osc}})\\
&\le\log_2(n+1)+S(\rho_{\mathrm{osc}}),
\end{aligned}
\qquad\text{(B27)}
```

where $`\rho_{\mathrm{osc}}`$ is the uniform mixture of the oscillator product states in (B23).

### 3.2 Covariance and the Gaussian entropy upper bound

Use quadratures

```math
\begin{aligned}
Q_k&=\frac{a_k+a_k^\dagger}{\sqrt2},\\
P_k&=\frac{a_k-a_k^\dagger}{i\sqrt2},\\
[Q_k,P_l]&=i\delta_{kl},
\end{aligned}
\qquad\text{(B28)}
```

and the symmetrized covariance convention

```math
\Gamma_{ab}
=\frac12\langle\{R_a-\langle R_a\rangle,
R_b-\langle R_b\rangle\}\rangle.
```

The vacuum covariance is $`I/2`$. The random real amplitudes are $`\alpha_k=\sqrt\kappa\,s_k(X)`$. Reversing their order turns the suffixes into partial sums of independent Bernoulli-$`1/2`$ variables, so

```math
\mathrm{Cov}(\alpha)=\frac\kappa4K_n,
\qquad
(K_n)_{ij}=\min(i,j).
\qquad\text{(B29)}
```

A real displacement changes $`\langle Q\rangle`$ by $`\sqrt2\alpha`$, without changing $`\langle P\rangle`$. After an entropy-preserving displacement that removes the mean, the covariance is

```math
\Gamma
=\frac12
\begin{pmatrix}
I+\kappa K_n&0\\
0&I
\end{pmatrix}
\qquad\text{(B30)}
```

in the ordering $`(Q_1,\ldots,Q_n,P_1,\ldots,P_n)`$.

Among states with the same first and second moments, the Gaussian state has maximum von Neumann entropy [WGC](../references/related-work.md#wgc). Here this fact can also be seen directly: the logarithm of the full-rank Gaussian comparison state $`\gamma`$ is quadratic in the canonical coordinates, so

```math
\mathrm{Tr}(\rho_{\mathrm{osc}}\log\gamma)
=\mathrm{Tr}(\gamma\log\gamma).
```

Nonnegativity of $`D(\rho_{\mathrm{osc}}\Vert\gamma)`$ gives $`S(\rho_{\mathrm{osc}})\le S(\gamma)`$. The covariance has strictly thermal symplectic eigenvalues when $`\kappa>0`$; the $`\kappa=0`$ oscillator state is simply pure vacuum.

An orthogonal diagonalization of $`K_n`$, applied to both $`Q`$ and $`P`$, is symplectic. The resulting symplectic eigenvalues are

```math
\nu_{j,n}=\frac12\sqrt{1+\kappa\lambda_{j,n}},
\qquad\text{(B31)}
```

where $`\lambda_{j,n}`$ are the eigenvalues of $`K_n`$. A one-mode squeezing makes each covariance block equal to $`\nu_{j,n}I_2`$, without changing entropy; the corresponding thermal occupation is $`\nu_{j,n}-1/2`$, with entropy $`g(\nu_{j,n}-1/2)`$ [HW](../references/related-work.md#hw). Thus

```math
S(\rho_{\mathrm{osc}})
\le
\sum_{j=1}^n
g\!\left(\frac{\sqrt{1+\kappa\lambda_{j,n}}-1}{2}\right).
\qquad\text{(B32)}
```

### 3.3 Spectrum of the discrete Brownian covariance

Write $`K_n=T_nT_n^{\mathsf T}`$, where $`T_n`$ is the lower triangular matrix of ones. Then

```math
K_n^{-1}=
\begin{pmatrix}
2&-1&0&\cdots&0\\
-1&2&-1&\cdots&0\\
0&-1&2&\ddots&\vdots\\
\vdots&\vdots&\ddots&2&-1\\
0&0&\cdots&-1&1
\end{pmatrix}.
\qquad\text{(B33)}
```

For $`n=1`$, (B33) means the $`1\times1`$ matrix $`(1)`$. For general $`n`$, the trial vector $`v_i=\sin(it)`$ solves the interior eigenvalue equation with eigenvalue $`4\sin^2(t/2)`$, subject to $`v_0=0`$ and the final boundary condition $`v_{n+1}=v_n`$. The latter gives

```math
t_{j,n}=\frac{(2j-1)\pi}{2n+1},
\qquad j=1,\ldots,n.
\qquad\text{(B34)}
```

These $`n`$ distinct modes yield exactly (B10).

Since the channel preserves the uniform state, its coherent information at that input is $`n-S(\rho_E)`$. Combining (B27), (B32), and (B10) proves the finite-inner-block inequality in (B11). Proposition M1 and the ordinary quantum coding theorem [D](../references/related-work.md#d) turn it into an achievable rate without invoking a coding theorem for forgetful channels.

### 3.4 The large-n limit with the endpoint singularity controlled

For fixed $`\kappa>0`$, define

```math
\begin{aligned}
F_\kappa(t)&=
g\!\left(
\frac{\sqrt{1+\kappa/[4\sin^2(t/2)]}-1}{2}
\right),\\
&\qquad0\lt t\le\pi.
\end{aligned}
\qquad\text{(B35)}
```

This function is positive, continuous, and decreasing. To check integrability at zero, use

```math
g(z)\le\frac{1+\ln(1+z)}{\ln2},
\qquad
\frac{\sqrt{1+a}-1}{2}\le\frac{\sqrt a}{2},
```

and $`\sin(t/2)\ge t/\pi`$ for $`0\le t\le\pi`$. They imply

```math
F_\kappa(t)
\le\frac{1+\ln(1+\pi\sqrt\kappa/(4t))}{\ln2},
\qquad\text{(B36)}
```

an integrable logarithmic upper bound.

Set $`\Delta_n=2\pi/(2n+1)`$. The points in (B34) are $`t_{j,n}=(j-\tfrac12)\Delta_n`$, and $`n\Delta_n\to\pi`$. For any $`0\lt a\lt \pi`$, monotonicity gives

```math
\Delta_n
\sum_{\{j:t_{j,n}\le a\}}F_\kappa(t_{j,n})
\le
2\int_0^a F_\kappa(t)\,dt.
\qquad\text{(B37)}
```

Indeed, on the left half of the $`j`$-th grid interval, the function is at least its midpoint value. The left halves are disjoint. The right side of (B37) tends to zero as $`a\downarrow0`$, uniformly in $`n`$. On an interval bounded away from zero, ordinary Riemann-sum convergence applies. The omitted interval $`[n\Delta_n,\pi]`$ has length $`\Delta_n/2`$ and causes no endpoint difficulty. Therefore

```math
\begin{aligned}
\lim_{n\to\infty}
\frac1n\sum_{j=1}^nF_\kappa(t_{j,n})
&=\frac1\pi\int_0^\pi F_\kappa(t)\,dt\\
&=h(\kappa).
\end{aligned}
\qquad\text{(B38)}
```

Since $`\log_2(n+1)/n\to0`$, equations (B11) and (B38) prove (B4).

### 3.5 Small-noise limit and the integral constant

Let

```math
F(a)=g\!\left(\frac{\sqrt{1+a}-1}{2}\right).
```

The change of variables $`t=\sqrt\kappa\,u`$ gives

```math
\frac{h(\kappa)}{\sqrt\kappa}
=\frac1\pi\int_0^\infty
\mathbf1_{\{u\lt \pi/\sqrt\kappa\}}\,
F\!\left(
\frac{\kappa}{4\sin^2(\sqrt\kappa\,u/2)}
\right)\,du.
\qquad\text{(B39)}
```

For every fixed $`u>0`$, the integrand converges to $`F(u^{-2})`$. On its support, $`\sin(\sqrt\kappa\,u/2)\ge\sqrt\kappa\,u/\pi`$. Since $`F`$ is increasing, this implies

```math
\begin{aligned}
0\le{}&
\mathbf1_{\{u\lt \pi/\sqrt\kappa\}}\,
F\!\left(
\frac{\kappa}{4\sin^2(\sqrt\kappa\,u/2)}
\right)\\
\le{}&F\!\left(\frac{\pi^2}{4u^2}\right).
\end{aligned}
\qquad\text{(B40)}
```

The dominator is integrable. Near zero it is $`O(1+|\ln u|)`$, by the same bound used in (B36). At infinity, $`(\sqrt{1+a}-1)/2\le a/4`$, and $`g(z)=O(z(1+|\ln z|))`$ as $`z\downarrow0`$, so it is $`O((1+\ln u)/u^2)`$. Dominated convergence is therefore valid on the full half-line.

It remains to evaluate

```math
\begin{aligned}
J&=\int_0^\infty
g_{\mathrm{nat}}\!\left(
\frac{\sqrt{1+u^{-2}}-1}{2}
\right)\,du,\\
g_{\mathrm{nat}}&=(\ln2)g.
\end{aligned}
\qquad\text{(B41)}
```

Set $`u=1/\sinh y`$, so that the argument of $`g_{\mathrm{nat}}`$ becomes $`\sinh^2(y/2)`$. If $`H(y)=g_{\mathrm{nat}}(\sinh^2(y/2))`$, then

```math
J=\int_0^\infty H(y)\frac{\cosh y}{\sinh^2y}\,dy.
```

Integration by parts is legitimate: $`H(y)/\sinh y`$ tends to zero both at zero, where it is $`O(y|\ln y|)`$, and at infinity, where it is $`O(ye^{-y})`$. Furthermore,

```math
H'(y)=\sinh y\,\ln\coth(y/2).
```

Thus

```math
\begin{aligned}
J
&=\int_0^\infty\ln\coth(y/2)\,dy\\
&=2\sum_{r=0}^\infty\frac1{(2r+1)^2}
=\frac{\pi^2}{4}.
\end{aligned}
\qquad\text{(B42)}
```

The series follows from
$`\ln\coth(y/2)=2\sum_{r\ge0}e^{-(2r+1)y}/(2r+1)`$; its terms are nonnegative, so Tonelli justifies termwise integration. Equations (B39)–(B42) give

```math
\lim_{\kappa\downarrow0}\frac{h(\kappa)}{\sqrt\kappa}
=\frac{J}{\pi\ln2}
=\frac{\pi}{4\ln2},
```

proving (B6).

## 4. Converse from independent Brownian bridges

### 4.1 Exact degradation to a product of bridge channels

Fix an integer $`L\ge2`$, and write $`N=qL+r`$, with $`0\le r\lt L`$. Complete block $`b\in\lbrace 0,\ldots,q-1\rbrace `$ consists of physical slots $`bL+1,\ldots,(b+1)L`$. Define its residual bridge phases

```math
\begin{aligned}
\beta_{b,i}
&=\theta_{bL+i}
-\left(1-\frac iL\right)\theta_{bL}
-\frac iL\theta_{(b+1)L},\\
&\qquad i=1,\ldots,L-1.
\end{aligned}
\qquad\text{(B43)}
```

For each block these are jointly centered Gaussian, with covariance

```math
\begin{aligned}
V_{ij}
&=\mathbb E\beta_{b,i}\beta_{b,j}
=\kappa\left[\min(i,j)-\frac{ij}{L}\right],\\
&\qquad1\le i,j\lt L.
\end{aligned}
\qquad\text{(B44)}
```

The bridges are independent of each other and of the full vector of endpoint phases. To verify the latter claim without relying on conditioning notation, let $`\eta_1,\ldots,\eta_L`$ be the independent increments within one block. Then

```math
\begin{aligned}
\beta_i&=\sum_{k=1}^i\eta_k-\frac iL\sum_{k=1}^L\eta_k,\\
\mathrm{Cov}\!\left(\beta_i,\sum_{k=1}^L\eta_k\right)&=0.
\end{aligned}
\qquad\text{(B45)}
```

Joint Gaussianity gives independence of the bridge and that block's total increment. Different blocks use independent increments. The initial phase is independent of all increments. The phases of the last $`r`$ carriers depend only on the endpoints and the subsequent increments, so they too are independent of all complete-block bridges.

Let $`\mathcal B_{L,\kappa}`$ denote the generalized dephasing channel on $`m=L-1`$ qubits obtained by averaging their unitaries over the centered Gaussian vector with covariance $`V`$. Define the finite-dimensional product channel

```math
\mathcal A_{N,L}
=\left(\mathcal B_{L,\kappa}\otimes\mathrm{id}_2\right)^{\otimes q}
\otimes\mathrm{id}_{2^r}.
\qquad\text{(B46)}
```

There is an exact CPTP postprocessing $`\mathcal P_{N,L}`$ such that

```math
\boxed{\mathcal N_N^{\mathrm B}
=\mathcal P_{N,L}\circ\mathcal A_{N,L}.}
\qquad\text{(B47)}
```

To construct it, sample the joint law of the real endpoint phases
$`\theta_0,\theta_L,\ldots,\theta_{qL}`$ and the last $`r`$ physical phases, independently of the bridge channel. On each complete block apply the linear interpolation phase
$`(1-i/L)\theta_{bL}+(i/L)\theta_{(b+1)L}`$
to carrier $`i`$, including $`i=L`$; on the remaining carriers apply their sampled full phases. The sum of the independent bridge and interpolation phases has exactly the original joint Gaussian increment law. Averaging these product diagonal unitaries defines $`\mathcal P_{N,L}`$.

Equivalently, a receiver given the endpoints could subtract their interpolation and obtain one independent bridge plus one noiseless endpoint carrier per block. Revealing the remaining phases corrects the last $`r`$ carriers. This is only an upper-bound device. The degradation identity (B47) makes the comparison entirely within finite-dimensional input and output spaces and does not require treating a continuous genie record as a physical output system.

There is no carrier at time zero. The physical endpoint $`j=(b+1)L`$ is counted once, as the last carrier of block $`b`$; it is not reused as an additional carrier of the next block.

### 4.2 Uniform-input purity of one bridge

For the bridge covariance $`V`$, choose any normalized environment vectors with Gram matrix

```math
\langle e_y|e_x\rangle
=\exp[-(x-y)^{\mathsf T}V(x-y)/2].
\qquad\text{(B48)}
```

Such vectors exist, for example as real coherent states with amplitudes $`V^{1/2}x`$. For the uniform distribution $`u`$ on $`\lbrace 0,1\rbrace ^m`$, the complementary-output purity is exactly

```math
\begin{aligned}
P_u
&=\mathrm{Tr}\,\rho_E(u)^2\\
&=\mathbb E_{X,Y\sim u}
\exp[-(X-Y)^{\mathsf T}V(X-Y)].
\end{aligned}
\qquad\text{(B49)}
```

Here $`X,Y`$ are independent. Put $`Z=(X-Y)^{\mathsf T}V(X-Y)`$. The coordinates $`A_i=X_i-Y_i`$ are independent, centered, and satisfy

```math
\mathbb EA_i^2=\frac12,\qquad
\mathbb EA_i^4=\frac12.
```

Consequently,

```math
\mu:=\mathbb EZ
=\frac12\mathrm{Tr}\,V
=\frac{\kappa(L^2-1)}{12},
\qquad\text{(B50)}
```

and a direct fourth-moment expansion gives

```math
\begin{aligned}
\mathbb EZ^2
&=\frac14(\mathrm{Tr}\,V)^2
+\frac12\mathrm{Tr}(V^2)
-\frac14\sum_iV_{ii}^2\\
&\le\frac34(\mathrm{Tr}\,V)^2
=3\mu^2.
\end{aligned}
\qquad\text{(B51)}
```

The inequality uses $`V\ge0`$, hence $`\mathrm{Tr}(V^2)\le(\mathrm{Tr}\,V)^2`$.

Now choose $`L=L_\kappa`$ from (B3), with $`0\lt \kappa\le1`$. Then

```math
\frac1{12}\le\mu\le\frac14.
\qquad\text{(B52)}
```

The lower bound follows directly from $`L^2\ge1+\kappa^{-1}`$. For the upper bound, if $`L=2`$, then $`\kappa(L^2-1)=3\kappa\le3`$. If $`L\ge3`$, the strict inequality $`L-1\lt \sqrt{1+\kappa^{-1}}`$ gives

```math
\kappa\lt \frac1{L(L-2)},\qquad
\kappa(L^2-1)\lt \frac{L^2-1}{L(L-2)}\le3,
```

which also proves (B52).

For every $`z\ge0`$, $`1-e^{-z}\ge z-z^2/2`$. Equations (B49)–(B52) therefore imply

```math
1-P_u
\ge\mu-\frac12\mathbb EZ^2
\ge\mu-\frac32\mu^2
\ge\frac7{96}=a_0.
\qquad\text{(B53)}
```

The final quadratic is increasing throughout $`[1/12,1/4]`$, and its value at $`1/12`$ is $`7/96`$.

### 4.3 An input-uniform coherent-information deficit

By (B15), it is enough to optimize over arbitrary distributions $`p`$ on the bridge's $`2^m`$ computational strings. Write

```math
\begin{aligned}
\rho_E(p)&=\sum_xp_x|e_x\rangle\langle e_x|,\\
D_2(p\Vert u)&=m-H(p),
\end{aligned}
\qquad\text{(B54)}
```

where $`D_2`$ is classical relative entropy in bits.

If $`D_2(p\Vert u)\ge\delta`$, then

```math
I_c(\rho_p,\mathcal B_{L,\kappa})
=H(p)-S(\rho_E(p))
\le m-\delta.
\qquad\text{(B55)}
```

If $`D_2(p\Vert u)\lt \delta`$, Pinsker's inequality gives

```math
\|p-u\|_1\le\sqrt{2\ln2\,\delta}=\frac{a_0}{4}.
\qquad\text{(B56)}
```

The preparation map $`p\mapsto\rho_E(p)`$ contracts this norm, and purity is dimension-independently Lipschitz:

```math
\begin{aligned}
&\left|\mathrm{Tr}\,\rho_E(p)^2
-\mathrm{Tr}\,\rho_E(u)^2\right|\\
&\quad\le2\|\rho_E(p)-\rho_E(u)\|_1\\
&\quad\le2\|p-u\|_1
\le\frac{a_0}{2}.
\end{aligned}
\qquad\text{(B57)}
```

For the first inequality, apply trace-norm/operator-norm duality to
$`\mathrm{Tr}[(\rho-\sigma)(\rho+\sigma)]`$, and use
$`\|\rho+\sigma\|_\infty\le2`$.

Equations (B53) and (B57) give

```math
\mathrm{Tr}\,\rho_E(p)^2\le1-\frac{a_0}{2}.
```

The von Neumann entropy is at least the Rényi-2 entropy, so

```math
S(\rho_E(p))
\ge-\log_2(1-a_0/2)
\ge\frac{a_0}{2\ln2}
\ge\delta.
\qquad\text{(B58)}
```

The last inequality holds because $`0\lt a_0\lt 1`$ and $`\delta=a_0^2/(32\ln2)`$. Thus $`I_c\le m-\delta`$ in this second case as well. We have proved the optimization-independent bound

```math
\boxed{J(\mathcal B_{L_\kappa,\kappa})\le L_\kappa-1-\delta.}
\qquad\text{(B59)}
```

The entropy-deficit dichotomy is essential: the proof does not infer the optimal capacity from the purity or entropy of the uniform input alone.

### 4.4 Completing the finite-code and capacity bounds

Every factor of $`\mathcal A_{N,L}`$ is degradable. Additivity (B18), the bridge bound (B59), and the noiseless endpoint and remainder factors give

```math
\begin{aligned}
J(\mathcal A_{N,L_\kappa})
&\le
\left\lfloor\frac N{L_\kappa}\right\rfloor
(L_\kappa-\delta)\\
&\qquad+\left(N-L_\kappa\left\lfloor\frac N{L_\kappa}\right\rfloor\right)\\
&=N-\delta\left\lfloor\frac N{L_\kappa}\right\rfloor.
\end{aligned}
\qquad\text{(B60)}
```

Every code for $`\mathcal N_N^{\mathrm B}`$ is a code for $`\mathcal A_{N,L_\kappa}`$ with the postprocessing $`\mathcal P_{N,L_\kappa}`$ absorbed into its decoder. Applying (B19) therefore proves (B12).

For a sequence of codes with $`\varepsilon_N\to0`$, divide (B12) by $`N`$. The floor term tends to $`1/L_\kappa`$, and $`h_2(\varepsilon_N)/N\to0`$, giving (B5). Finally $`L_\kappa\sqrt\kappa\to1`$, so (B4)–(B6) imply (B8) and the sharp scaling exponent in (B7).

For completeness, when $`\kappa=0`$, a fixed-weight sector is noiseless and has dimension $`\binom{N}{\lfloor N/2\rfloor}`$. Its logarithm divided by $`N`$ tends to one; the carrier dimension bounds capacity by one. Hence $`Q_{\mathrm B}(0)=1`$.

## 5. Scope and inherited ingredients

The all-code statement is specific to the unassisted entanglement-transmission task in the stated phase-only train. No feedback, two-way-assisted, loss-tolerant, energy-unconstrained bosonic, or worst-trajectory capacity is established. The finite-code converse covers nonuniform and nonisometric encoders. The achievable construction establishes existence of codes, not an efficient implementation.

The proof uses established quantum coding, Gaussian entropy extremality, and generalized-dephasing facts [D](../references/related-work.md#d), [DBF](../references/related-work.md#dbf), and [WGC](../references/related-work.md#wgc). The new calculation is the fixed-qubit Brownian capacity scaling with a converse uniform over all inputs. A square-root entropy mechanism is already present in the Rényi-2 entropy flow of a phase-diffusing coherent laser ensemble [W](../references/related-work.md#w); the result here is not a claim to discover that mechanism. The separate reset comparison makes the operational distinction at equal complete channels on up to three selected slots.

Full bibliographic entries and precise source locations are collected in [related work](../references/related-work.md).
