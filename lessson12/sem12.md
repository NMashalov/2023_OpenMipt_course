# Related samples

## Wilcoxon sign test 

$$
    Z_i = Y_i - X_i = \theta +\varepsilon_i
$$


$$
    U_i = I\{Z_i >0\} \sim Bern(p)
$$

$H_0$: $p=\frac{1}{2}$

$H_1$: $p>\frac{1}{2}$

Suppose $\varepsilon$:
- independent 
- continuous 
- median is equal to zero

Statistic:

$$
    S = U_1 + \dots + U_n \sim Bin(n,\frac{1}{2})
$$

$$
    \frac{S - \frac{n}{2} - \frac{1}{2}}{\sqrt{\frac{n}{4}}} \xrightarrow{H_0} \mathbb{N}(0,1)
$$


$$
    \hat{\theta} = med\{Z_i, i=1,\dots,n\}
$$

Confidence interval are defined as:


$$
    k_\alpha=[\frac{n}{2} - \frac{1}{2} - z_{1-\alpha}\sqrt{\frac{n}{4}}]
$$

## Wilcoxon rank sign test

Also notes absolute difference

To get intuition let's consider variation row:

$$  
    -0.45, -0.25, -0.05, 2.5, 3, 3.5
$$

Purely sign test won't see shift. Yet in some cases it's useful to take in account that positive values by comparison with negative are greater. It's From rank perspective  


Rank R is defined by absolute value of $|Z_i| \sim R_i \in \mathbb{N}$

Result statistic is sum weighted with ranks

$$
    T = R_1U_1 + \dots + R_nU_n
$$


$$
    \frac{T - \frac{n(n+1)}{4} - \frac{1}{2}}{\frac{n(n+1)(2n+1)}{24}} \xrightarrow{H_0} \mathbb{N}(0,1)
$$

Shift:


$$
    \theta = med\{V_{i,j} = {z_i +z_j}{2}, 1 \le i \le j \le n\} 
$$

$$
    k_\alpha = [\frac{n(n+1)}{4} - \frac{1}{2} - z_{1-\alpha}\sqrt{\frac{n(n+1)(2n+1)}{24}}]
$$

Confidence interval:
$$
    V_{k_\alpha+1}, V_{\frac{n(n+1)}{2}} - k_\alpha-1
$$

## Minimal detectable effect (MDE)

Three pillars:

1. $\alpha$ - significance,
2. $n$ - number of samples
3.  $\beta$ - method power

---
**Intuition:**

- H_0 is rejected, when it's true  -> very significant error. Defined by alpha in range around 0.01 and 0.05

- H_0 not rejected, when it's not true -> less significant error.  Defined by beta in range around 0.8



Beta and alpha is estimated through corresponding synthetic AA and AB tests.

Confidence interval is estimated through equations

$$
    \beta_l = \hat{\beta} - 2\sqrt{\frac{\hat{\beta}(1-\hat{\beta})}{\hat{\beta}}} \\
    
    \beta_r = \hat{\beta} +2\sqrt{\frac{\hat{\beta}(1-\hat{\beta})}{\hat{\beta}}}
$$
---
Suppose we have two samples:
- $X_1, \dots, X_n$ - sample $Ex_i=a_1, Dx_i=\sigma_1^2$ 
- $Y_1, \dots, Y_n$ - sample $Ey_i=a_2, Dy_i=\sigma_2^2$ 

### t-test
$$
\frac{\bar{X}-\bar{Y}}{\sqrt{\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m}}} \xrightarrow{H_0} \mathbb{N}(0,1)
$$

$S={T(\bar{X},\bar{Y}) > z_{1-\alpha}}$

$\varepsilon = a_1 - a_2$ - effect

$\bar{X} - \bar{Y} \sim N(\varepsilon,\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m})$

$$
    \varepsilon \ge (z_{1-\alpha}+z_{\beta})\sqrt{\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m}}
$$

### Stratification 

$Y_1, \dots, Y_n$ - sample 
$X_1, \dots, X_n$ - strats, which are noted before experiments

|Strat| Size| Elements| Mean| Theoretical| Weights|
|-----|-----|----|-------| ---|---|
|1| n_1| $Y_1, \dots,Y_{n_1}$| $\bar{Y}_1$| $\mu_1,\sigma_1$| $\omega_1$ |
|2| n_2| $Y_{n_1+1}, \dots,Y_{n_1+n_2}$| $\bar{Y}_2$| $\mu_2,\sigma_2$|  $\omega_2$ |

Two approaches for mean estimation:
1. $\bar{Y} = \frac{1}{n} \sum\limits_{i=1}^n Y_i$
2. Stratified mean $\bar{Y}_{st} =\sum\limits \omega_k$

Note that algebraically means are equal. Difference will come in dispersion of estimation

Sampling methods:
1. Random sampling
2. Stratified sampling with sampling $n_k = n  \omega_k$
$$
    p(x_k) = p(x_k| x_k \in k) p(k)
$$

1. Stratified sampling +  stratified mean

$$
    \mathbb{D}[\bar{Y}_st | n_k = n \omega_k] = \mathbb{D}[ \sum| n_k = n \omega_k] = 
    \sum_{k=1}^K D[\bar{Y_k}|n_k = w_k n] = \\ 
    \sum_{k=1}^K \omega_k^2 \frac{1}{n \omega_k} \sigma_k^2 =\frac{1}{n} \sum_{k=1}^K \omega_k \sigma_k^2 
$$

1. Random sampling + random mean

During derivation we'll use [Law of total variance](https://ru.wikibrief.org/wiki/Law_of_total_variance)


$$
    \mathbb{D}Y= \mathbb{E_x}\mathbb{D_y}[Y_i|x] + \mathbb{D_y}\mathbb{E_x}[Y_i|x] = \\
    \mathbb{E_x}\sum_{k=1}^K \sigma_k^2 I\{x=k\}+
    \mathbb{D_x}\sum_{k=1}^K \mu_k I\{x=k\} =\\
    = \sum_{k=1}^K \omega_k \sigma_k^2 + E[\sum_{k=1}^K \mu_k I\{x=k\}]^2 -(E[\sum_{k=1}^K \mu_k I\{x=k\}])^2 = \\

    = \sum^K_{k=1} \omega_k \sigma^2_k + \sum^K_{k=1} \omega_k (\mu_k - \mu)^2
$$

3. Random sampling + stratified mean (post stratification)

$$
    D \bar{Y}_{S_t} = E_xD_y[\bar{Y}_{st}|n_1,\dots,n_k] +  D_xE_y[\bar{Y}_{st}|n_1,\dots,n_k] = \\
    E \sum_{k=1}^K \omega_k^2 D[\bar{Y}|n_k] + \cancel{D\mu} = E \sum_{k=1}^K \omega_k^2 \sigma_k^2 \frac{1}{n_k} = \\ \sum_{k=1}^K \omega_k^2 \sigma_k^2 E \frac{1}{n_k} = \\
    \sum_{k=1}^K \omega_k^2 \sigma_k^2 (\frac{1}{n \omega_k} + \frac{1-\omega_k}{n^2\omega_k} + O(\frac{1}{n^2}))
$$