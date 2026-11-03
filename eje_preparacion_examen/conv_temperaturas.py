# Programa una aplicación que convierta una temperatura dada en grados Celsius a Fahrenheit aplicando la fórmula
# $F = C \times \frac{9}{5} + 32$. Utiliza la función round() para mostrar el resultado redondeado a un solo decimal.

grados_cel = int(input("Introduce una temperatura en grados celsius: "))

fahrenheit = grados_cel * 9/5 + 32

print(grados_cel, "grados celsius, es igual a", round(fahrenheit, 2), "grados")


































#Segunda practica
# Programa una aplicación que convierta una temperatura dada en grados Celsius a Fahrenheit aplicando la fórmula
# $F = C \times \frac{9}{5} + 32$. Utiliza la función round() para mostrar el resultado redondeado a un solo decimal.

grados = float(input("Introduce la temperatura en grados celsius: "))
conversion_grados = grados * 9/5 + 32

print(grados, "grados celsius equivalen a", conversion_grados, "grados fahrenheit")
print(f"{grados} grados celsius equivalen a {conversion_grados:.2f} grados fahrenheit")