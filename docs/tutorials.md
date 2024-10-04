![](sample-implementation.png)
# Implementación de ejemplo

## Importación de módulos necesarios

Para ejecutar estas funciones, es necesario contar con `np.array` de `numpy`, junto con una librería para graficar como `matplotlib`.

```
import numpy as np
import matplotlib.pyplot as plt
```

# Funciones del módulo

```
# Función que genera la evolución temporal (ver Referencia)
def dyn_generator(oper, state):
    return -1j * (np.dot(oper, state) - np.dot(state, oper))

# Función que aplica el método RK4 (ver Referencia)
def rk4(func, oper, state, h):
    k1 = h * func(oper, state)
    k2 = h * func(oper, state + k1 / 2)
    k3 = h * func(oper, state + k2 / 2)
    k4 = h * func(oper, state + k3)

    return state + (k1 + 2*k2 + 2*k3 + k4) * (1 / 6)
```

# Insumos

```
oOper = np.array([[0, 1], [1, 0]]) # Ejemplo de operador
yInit = np.array([[1, 0], [0, 0]]) # Estado inicial
times = np.linspace(0, 10, 50)
h = times[1] - times[0]

# Arreglos para guardar estados
stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)
```

# Cálculo

```
for tt in range(times.size):
    stateQuant00[tt] = yInit[0, 0].real
    stateQuant11[tt] = yInit[1, 1].real

    yInit = rk4(dyn_generator, oOper, yInit, h)
```

# Visualizar

```
plt.plot(times, stateQuant00)
plt.plot(times, stateQuant11)
```
