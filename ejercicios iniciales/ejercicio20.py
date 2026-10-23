#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
num1 = int(input("Introduce un número entre el 0 y 10: "))
num2 = int(input("Introduce un número entre el 0 y 10: "))

#lista_num = [1, 2, 3, 4 ,5, 6 ,7 ,8 ,9, 10]
lista_num="123456789"


if num1 or num2 != lista_num:
    print("el valor no existe")
else:
    if num1>num2:
        print("")
    if num1<num2:
        print("")
    if num1 == num2:
        print("")
