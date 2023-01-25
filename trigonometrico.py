"""
calcular el seno y coseno de un angulo dado. 
en este caso 30° grados 

"""
# importamos la libreria de matematicas 

import math

# angulo dado en grados lo pasamos a radianes 

beta = math.radians(30)

# calculamos el seno y coseno

angle_sin = math.sin(beta)
angle_cos = math.cos(beta)

# imprimimos los valores del seno y el coseno

print(f"el seno del angulo {beta} es igual a {angle_sin}")
print(f"el coseno del angulo {beta} es igual a {angle_cos}")












