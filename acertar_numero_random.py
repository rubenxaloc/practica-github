import random
random=random.randint(1,5)
usuario = input("Introduce un número del 1 al 5: ")
if usuario in "12345":
    if int(usuario)==random:
            print("acertaste")
    else:
        print("fallaste")
else:
    print("No has introducido el rango correcto")