#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
num1 = int(input("Introduce el primer valor: "))
num2 = int(input("Introduce el primer valor: "))
if num1 > num2:
    print("El número", num1, "es mayor que el número", num2)
elif num1 < num2:
    print("El número", num2, "es mayor que el número", num1)
else:
    print("Ambos números son iguales")