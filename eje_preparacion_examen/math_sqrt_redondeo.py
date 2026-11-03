# Importa la librería math. Crea un programa que pida un número positivo por teclado,
# calcule su raíz cuadrada utilizando el método math.sqrt() y, a continuación, utilice math.ceil() 
# para redondear ese resultado hacia arriba y math.floor() para redondearlo hacia abajo. Muestra todos los pasos por pantalla.

import math
numero = float(input("Introduce un valor positivo: "))
raiz_del_valor = math.sqrt(numero)

print("La raiz del número introducido es ", raiz_del_valor, "bananas")
print(f"La raiz del numero introducido es {raiz_del_valor} bananas")
print("La raiz del numero introducido es ", round(raiz_del_valor, 2), "bananas")
print("La raiz del numero introducido es ", int(raiz_del_valor, 2), "bananas")
print("La raiz del numero introducido es ", math.ceil(raiz_del_valor), "bananas")
print("La raiz del numero introducido es ", math.floor(raiz_del_valor), "bananas")
print(f"La raiz del nuemero introducido es {raiz_del_valor} bananas")
print(f"La raiz del numero introducido es {raiz_del_valor} bananas")