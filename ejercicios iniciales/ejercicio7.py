#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
#forzar que el resultado de la división tenga 2 decimales?
operando1 = float(input("Introduce el primer operando: "))
operando2 = float(input("Introduce el segundo operando: "))
suma = operando1 + operando2
resta = operando1 - operando2
multiplicacion = operando1 * operando2
division = operando1 / operando2
division_entera = operando1 // operando2
potencia = operando1 ** operando2
modulo = operando1 % operando2

print("La suma de operador1 y operador2 es: ", suma)
print("La resta de operador1 y operador2 es: ", resta)
print("La multiplicación de operador1 y operador2 es: ", multiplicacion)
print("La división de operador1 y operador2 es: ", round(division, 2))
print("La división entera de operador1 y operador2 es: ", division_entera)
print("La potencia de operador1 y operador2 es: ", potencia)
print("El módulo de operador1 y operador2 es: ", modulo)