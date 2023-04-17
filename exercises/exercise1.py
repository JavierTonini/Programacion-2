"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5

# COMPLETAR - INICIO

print ("El area del cuadrado en el cual uno de sus lados es {} es igual a: {}".format(lado_cuadrado, lado_cuadrado*lado_cuadrado))

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando el operador de potencia.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO

print ("El area del cuadrado en el cual uno de sus lados es {} es igual a: {}".format(lado_cuadrado, lado_cuadrado**2))

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO

print ("El area del cuadrado en el cual uno de sus lados es {} es igual a: {}".format(lado_cuadrado, pow(lado_cuadrado,2)))

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

# COMPLETAR - INICIO

cantidad_a_comprar = presupuesto_disponible // precio
print ("La cantidad que se puede comprar con un presupuesto de {} el producto con el precio {} es de {}".format(presupuesto_disponible, precio, cantidad_a_comprar))

# COMPLETAR - FIN

assert cantidad_a_comprar == 2


"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

# COMPLETAR - INICIO
resto = numero_incalculable % 7
print (resto)
print ("El resto de la division entre {} y 7 es {} por lo tanto es divisible por 7".format(numero_incalculable, resto))
# COMPLETAR - FIN

assert es_divisible_por_siete