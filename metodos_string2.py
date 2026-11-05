respuesta=input("Introduce una letra: ")
if respuesta.isnumeric()==False:
    if respuesta.isupper():
        print("Es mayuscula")
    else:
        print("Es minúscula")
else:
    print("El valor introducido no es una letra")