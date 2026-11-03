# 27. Mejora el programa anterior para controlar que el valor introducido es una letra y en 
# caso de introducir un número, aparezca un aviso por pantalla 

texto = input("Introduce una letra: ")

if texto.isalpha():
    if texto.isupper():
        print("La letra es mayúscula")
    else:
        print("La letra es minúscula")
elif texto.isnumeric():
    print("El valor introducido es un número")