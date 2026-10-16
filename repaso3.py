import math

radio = float(input("Introduce el valor del radio del círculo: "))

area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"La longitud del círculo es: {longitud:.2f}")

#Redondear con los dos métodos
#Qué dos metodos de redondeo utiliza la libreria math?
#Escoger uno de los métodos de print

#Métodos de redondeo:
print(round(area, 2))
print(f" el resultado es: {area:.2f}")
print(math.ceil(area))
print(math.floor(area))