# 28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

texto = input("Introduce una letra: ")

if texto.isalpha():
    if texto.isupper():
        print("La letra es mayúscula")
    else:
        print("La letra es minúscula")
elif texto.isnumeric():
    print("El valor introducido es un número")
else:
    print("El valor introducido es un símbolo")