# Explicación

El método de cuarto orden de Runge-Kutta es una técnica numérica para aproximar soluciones a ecuaciones diferenciales de la forma:

$$
\frac{dy}{dt}=f(t,y(t))
$$

donde $f(t,y)$ describe la evolución temporal del sistema, y $y(t)$ representa el estado del sistema en un tiempo dado $t$.

> **Nota:** Este módulo resuelve específicamente el caso $f(t, \\mathbf{y}) = -i[\\mathbf{O}, \\mathbf{y}(t)]$, donde la función $f(t, \\mathbf{y})$ no tiene una dependencia explícita con el tiempo.

El método RK4 mejora la precisión en cada paso temporal utilizando cuatro cálculos intermedios ($k_1$, $k_2$, $k_3$, y $k_4$) para estimar el siguiente valor, definidos de la siguiente forma:

$$
k_1 = h \cdot f(t_n, y_n)
$$

$$
k_2 = h \cdot f\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right)
$$

$$
k_3 = h \cdot f\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right)
$$

$$
k_4 = h \cdot f\left(t_n + h, y_n + k_3\right)
$$

La nueva estimación se obtiene como:

$$
y_{n+1} = y_n + \frac{1}{6} \left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$
