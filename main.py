# Encontrar la serie de fourier para 10 componentes de la siguiente función:
# g(t): 0, 0 <= t < 1;
#       1, 1 <= t < 3;
#       0, 3 <= t < 6;
#       1, 6 <= t < 7;
#       0, 7 <= t < 8;
# El periodo es T = 8.

# Importación de librerias
import sympy as smp
import numpy as np
import matplotlib.pyplot as plt

# Definición de variables
period_T = 8

# Definición de simbolos
t_time = smp.symbols("t", real=True)
n_component = smp.symbols("n", integer=True)

# Definición de funciones
g_t_1 = 0
g_t_2 = 1
g_t_3 = 0
g_t_4 = 1
g_t_5 = 0

# Entrada del usuario
component_num = int(input("Ingrese el número de componentes: "))

# Hallamos los coeficientes a_n, b_n y c
# a_n = (2/T) * integral{0}{period_T} de g(t) sin(2 * pi * n * t / period_T) dt
# b_n = (2/T) * integral{0}{period_T} de g(t) cos(2 * pi * n * t / period_T) dt
# c = (2/T) * integral{0}{period_T} de g(t) dt

# a_n
a_n_1 = (2 / period_T) * smp.integrate(
    g_t_1 * smp.sin(2 * smp.pi * n_component * t_time / period_T), (t_time, 0, 1)
)
a_n_2 = (2 / period_T) * smp.integrate(
    g_t_2 * smp.sin(2 * smp.pi * n_component * t_time / period_T), (t_time, 1, 3)
)
a_n_3 = (2 / period_T) * smp.integrate(
    g_t_3 * smp.sin(2 * smp.pi * n_component * t_time / period_T), (t_time, 3, 6)
)
a_n_4 = (2 / period_T) * smp.integrate(
    g_t_4 * smp.sin(2 * smp.pi * n_component * t_time / period_T), (t_time, 6, 7)
)
a_n_5 = (2 / period_T) * smp.integrate(
    g_t_5 * smp.sin(2 * smp.pi * n_component * t_time / period_T), (t_time, 7, 8)
)
a_n = a_n_1 + a_n_2 + a_n_3 + a_n_4 + a_n_5

# b_n
b_n_1 = (2 / period_T) * smp.integrate(
    g_t_1 * smp.cos(2 * smp.pi * n_component * t_time / period_T), (t_time, 0, 1)
)
b_n_2 = (2 / period_T) * smp.integrate(
    g_t_2 * smp.cos(2 * smp.pi * n_component * t_time / period_T), (t_time, 1, 3)
)
b_n_3 = (2 / period_T) * smp.integrate(
    g_t_3 * smp.cos(2 * smp.pi * n_component * t_time / period_T), (t_time, 3, 6)
)
b_n_4 = (2 / period_T) * smp.integrate(
    g_t_4 * smp.cos(2 * smp.pi * n_component * t_time / period_T), (t_time, 6, 7)
)
b_n_5 = (2 / period_T) * smp.integrate(
    g_t_5 * smp.cos(2 * smp.pi * n_component * t_time / period_T), (t_time, 7, 8)
)
b_n = b_n_1 + b_n_2 + b_n_3 + b_n_4 + b_n_5

# c
c_1 = (2 / period_T) * smp.integrate(g_t_1, (t_time, 0, 1))
c_2 = (2 / period_T) * smp.integrate(g_t_2, (t_time, 1, 2))
c_3 = (2 / period_T) * smp.integrate(g_t_3, (t_time, 3, 6))
c_4 = (2 / period_T) * smp.integrate(g_t_4, (t_time, 6, 7))
c_5 = (2 / period_T) * smp.integrate(g_t_5, (t_time, 7, 8))
c = c_1 + c_2 + c_3 + c_4 + c_5

# Computamos la serie de fourier
g_t = (
    c / 2
    + smp.Sum(
        a_n * smp.sin(2 * smp.pi * n_component * t_time / period_T),
        (n_component, 1, component_num),
    )
    + smp.Sum(
        b_n * smp.cos(2 * smp.pi * n_component * t_time / period_T),
        (n_component, 1, component_num),
    )
)

# Graficación de resultados

# Se convierte la función simbólica a una función numérica para poder evaluarla
g_t_numeric = smp.lambdify(t_time, g_t, modules="numpy")

# Esblecimiento de rango de tiempo
time_range = np.linspace(0, 8, 100)

# Evaluación la función sobre el rango de tiempo
g_t_range = g_t_numeric(time_range)

# Graficación
plt.plot(time_range, g_t_range)
plt.title("Serie de Fourier")
plt.xlabel("tiempo t")
plt.ylabel("g(t)")
plt.show()
