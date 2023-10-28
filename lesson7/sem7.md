## Boosting

Last seminar recap

Random Forest

- low variance


Boosting idea
$$
Y = \begin{pmatrix}
    y_1 \\
    y_2 \\ 
    \vdots \\
    y_n
\end{pmatrix}
$$
Next prediction corrects mistakes from previous iteration

$$
\hat{y}^1 = \begin{pmatrix}
    \hat{y}_1^1 \\
    \hat{y}_2^1 \\ 
    \vdots \\
    \hat{y}_n^1
\end{pmatrix}
$$

Total solution:
$$
    (Y-\hat{y}^1)
$$

$\mathbf{F}$ -model class 

For boosting we use only one class of model

Resulting prediction is:

$$
    \hat{y}_T(x) = \sum\limits_{t=1}^T b_t(x)
$$
,where $b_i \in F$ are learned on losses of previous predictions $\sum\limits_{j=1}^{i-1} b_{j-1}(x)$
$$
    b_1= \argmin_{b \in F} \frac{1}{2} \sum\limits_{i=1}^n (b(x_i)-Y_i)^2
$$

Delcaration of loss of model in previous step on i-th sample
$$
    e^1_i = Y_i - b_1(x)
$$

Second model is chosen like:

$$
    b_2= \argmin_{b \in F} \frac{1}{2} \sum\limits_{i=1}^n (b(x_i)-Y_i)^2
$$

etc 

## Theoritical proof of concept

Goal of optimization:

$$
    Q(Y,\hat{y}) = \frac{1}{2} \sum\limits_{i=1}^n (\hat{y}-Y_i)^2 \rightarrow \min\limits_{\hat{y}}
$$

Derivative of Q by $\hat{y}$ on object $x_i$ is equal to 
$$
    \hat{y}_{t-1}(x_i) - Y_i = -e_i^{t-1}
$$

Every new iteration steps on gradient 

$$
    e^{t-1} = \nabla Q(Y,z) |_{z=\hat{y}_{t-1}}
$$

## General case of gradient boosting

$\hat{y}_T(x) = \sum\limits_{t=0}^T \gamma_t b_t(x)$ - weighted sum

On step t=0 is simple:
- regression: 
$$
    p = \begin{cases}
        1, most\ frequent\\
        0,\ on\ other 
    \end{cases}
$$
- classification: $b_0 = \frac{1}{n} \sum\limits_{i=1}^n Y_i$


For learning $b_t$


$$
    Q(Y,\hat{y}) = \sum\limits_{i=1}^n L(Y,\hat{y})
$$


$$
    Q(Y,s) = \sum\limits_{i=1}^n L(Y_i,s) \rightarrow \min\limits_{s\in \mathbf{R}^n}
$$

Gradient descent


Recap n is number of samples

$$
    s^t = s^{t-1} - \eta \nabla_s Q(Y,s^{t-1}) = \\
    s^{t-1} - \eta g^t,\\
    g^t = (\nabla_s L(Y,s^{t-1}_i)^n_{i=1}
$$

Ideal case:

$$
    \hat{y}_t(x_i) = \hat{y} \\
    \hat{g}^t = (\nabla_s L(Y_i,s) |_{s=\hat{y}_T})^n_{i=1}
$$

-> $(x_1 - \hat{g}^T_1), \dots, (x_n - \hat{g}^T_n)$

On that data we train model $y_t$ .


$$
    b_t(x) = \argmin\limits_{b \in \mathbf{F}} \sum\limits_{i=1}^n (b(x_i)+\hat{g}^t_i)^2
$$

For weights in $\gamma_t$:

$$
    \hat{\gamma}_t = \argmin\limits_{\gamma \in \mathbf{R}} \sum\limits_{i=1}^n L(Y_i,\hat{y_{t-1}}  + \gamma b_t(x_i))
$$

New $y_t$ will be calculated as:

$$
    \hat{y}_t(x) = \hat{y_{t-1}}(x)+ \eta \hat{\gamma}_t b_t(x)
$$

## Stochastic gradient descent

$b_t$ is learned on subset of training set X: $X_T^{*} \in X$.
Usually cardinality of subset is half of original.
That helps:
- denoise on bad samples and numerical errors
- reduction on calculation
- generalization improvement

## Bias-variance tradeoff 

Two types of ensembles:
- horizontal scaling like *random forest*. Reducts variance with raising number of ensemle exemplars, bias is remain stable
- vertical scaling like *gradient boosting*. Reducts bias, but variance remain stalbe

That leads to choose in base model in ensemble. For boosting we choose low-depth trees which have low variance, which is accessed with better generalization.








  







