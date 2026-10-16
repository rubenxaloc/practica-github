import math

radio = float(input("Introduce el valor del radio del círculo: "))

area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"La longitud del círculo es: {longitud:.2f}")