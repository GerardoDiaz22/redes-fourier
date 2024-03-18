import sympy as smp
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumulative_trapezoid

t = smp.symbols('t', real=True)
n = smp.symbols('n', real=True)

T = 8 #Periodo

n_armonicos = int(input("Ingrese el armonico que desea observar: "))

#Se obtiene el valor de g(t) mediante una una funcion definida a trozos
# donde g(t) : 0; 0 < x < 1
#              1; 1 < x < 3
#              0; 3 < x < 6
#              1; 6 < x < 7
#              0; 7 < x < 8

integral_c = 0 #Acumulado de la integral de c
f = 0
integral_c = smp.integrate(f, (t, 0, 1)) + integral_c

f = 1
integral_c = smp.integrate(f, (t, 1, 3)) + integral_c

f = 0
integral_c = smp.integrate(f, (t, 3, 6)) + integral_c

f = 1
integral_c = smp.integrate(f, (t, 6, 7)) + integral_c

f = 0
integral_c = smp.integrate(f, (t, 7, 8)) + integral_c

c = (2/T)*integral_c

#------------------------------------+

integral_an = 0 #Acumulado de la integral de c
integral_bn = 0
total_sum = 0
aux1 = 0
aux2 = 0

#para no escribir tanto solo integrare los intervalos donde g(t) no sea 0

for i in range(n_armonicos):# Sumatoria donde (i+1) es equivalente a "n"
    #inicio integral an-----------------------------------
    f = smp.sin(2 * smp.pi * (i+1) * (1/T) * t)
    integral_an = smp.integrate(f, (t, 1, 3)) + integral_an

    f = smp.sin(2 * smp.pi * (i+1) * (1/T) * t)
    integral_an = smp.integrate(f, (t, 6, 7)) + integral_an

    an = integral_an * (2/T)
    #fin integral an-----------------------------------

    #multiplicacion de an con sen(2 (pi)nft)
    aux1 = an * smp.sin(2 * smp.pi * (i+1) * (1/T) * t)


    #inicio integral bn-----------------------------------
    f = smp.cos(2 * smp.pi * (i+1) * (1/T) * t)
    integral_bn = smp.integrate(f, (t, 1, 3)) + integral_bn

    f = smp.cos(2 * smp.pi * (i+1) * (1/T) * t)
    integral_bn = smp.integrate(f, (t, 6, 7)) + integral_bn

    bn = integral_bn * (2/T)
    #fin integral bn-----------------------------------

    #multiplicacion de bn con sen(2 (pi)nft)
    aux2 = bn * smp.cos(2 * smp.pi * (i+1) * (1/T) * t)

    #suma del lado an y del lado bn
    total_sum = aux1 + aux2 + total_sum

    #reseteo de variables
    integral_an = 0
    integral_bn = 0
armonico = ((1/2) * c ) + total_sum


#-----------------------------------------------------------------------------de aqui para abajo no entiendo muy bien, esto lo hizo la ia


armonico_num = smp.lambdify(t, armonico, modules=['numpy'])

# Crear un array de valores de tiempo
t_values = np.linspace(0, 8, 100)

# Evaluar la función "armonico" en los valores de tiempo
armonico_values = armonico_num(t_values)

# Graficar el resultado
plt.plot(t_values, armonico_values)
plt.xlabel('Tiempo')
plt.ylabel('Valor del armónico')
plt.title('Gráfico del valor del armónico en función del tiempo')
plt.show()