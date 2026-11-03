# Importa la librería math. Pide al usuario el valor del radio de un círculo y calcula su longitud ($2 \cdot \pi \cdot r$)
# y su área ($\pi \cdot r^2$). Utiliza math.pi y muestra el área redondeada a dos decimales usando f-strings

import math

radio = int(input("Introduce el radio del círculo: "))
longitud = 2 * math.pi * radio
area = math.pi * radio ** 2

print(f"La longitud del círculo es {longitud:.2f}")
print(f"El area del círculo es de {area:.2f}")

print("La longitud con el redondeo hacia arriba", math.ceil(longitud))
print("La longitud redondeado hacia abajo", math.floor(longitud))
print("El area redondeada hacia arriba", math.ceil(area))
print("El area redondeada hacia abajo", math.floor(area))
print("La longitud redondeada", int(longitud))
print("El area redondeada", int(area))
print("La longitud redondeada", round(longitud, 2))
print("El area redondeada", round(area, 2))