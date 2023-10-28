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







