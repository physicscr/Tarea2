#!/usr/bin/env python

import numpy as np

def dyn_generator(oper, state):
    """Crea la dinámica de un sistema de ecuaciones diferenciales.

    Esta función define cómo evoluciona un sistema en el tiempo usando un
    operador lineal (`oper`) y un estado inicial (`state`). La dinámica sigue
    una ecuación de movimiento basada en la conmutación del operador y el estado,
    multiplicada por un factor imaginario para describir el cambio.

    Examples:
        >>> import numpy as np
        >>> oper = np.array([[0, 1], [1, 0]])  # Operador
        >>> state = np.array([[1, 0], [0, 0]]) # Estado inicial
        >>> dyn_generator(oper, state)
        [[0.-0.j 0.+1.j]
         [0.-1.j 0.-0.j]]

    Args:
        oper (np.array): Un operador lineal
        state (np.array): Estado siguiente

    Returns:
        (np.array): El cambio en el estado del sistema.
    """
    return -1j * (np.dot(oper, state) - np.dot(state, oper))

def rk4(func, oper, state, h):
    """Implementa el método de Runge-Kutta de cuarto orden para integrar EDOs.

    Esta función utiliza el método RK4 para estimar el próximo estado del sistema,
    a partir de una función de dinámica, un operador lineal y un estado inicial
    dados. Este proceso permite una integración precisa del sistema.

    Examples:
        >>> import numpy as np
        >>> rk4(dyn_generator, np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]), 0.1)
        [[0.99003333+0.j         0.        +0.09933333j]
         [0.        -0.09933333j 0.00996667+0.j        ]]

    Args:
        func (callable): Una función que representa el sistema de ecuaciones diferenciales.
        oper (np.array): Un parámetro utilizado por la función `func` para influir en la dinámica del sistema.
        state (np.array): El estado actual del sistema.
        h (float): El tamaño del paso para la integración.

    Returns:
        (np.array): El estado siguiente luego de un cambio `h`
    """
    k1 = h * func(oper, state)
    k2 = h * func(oper, state + k1 / 2)
    k3 = h * func(oper, state + k2 / 2)
    k4 = h * func(oper, state + k3)

    return state + (k1 + 2*k2 + 2*k3 + k4) * (1 / 6)
