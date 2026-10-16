import random
random=random.randint(1,5)
usuario = int(input("Introduce un número del 1 al 5: "))

if random > 5:
    print("Valor incorrecto")
elif usuario != random:
    print("fallaste")
else:
    print("acertaste")