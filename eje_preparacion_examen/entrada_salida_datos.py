#Escribe un programa que pida al usuario su nombre y su edad (en formato de número entero). 
# Después, debe mostrar por pantalla un mensaje saludando al usuario e indicando cuántos años tendrá el próximo año.

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
proximo_año = edad + 1 

print("Hola", nombre, ", el próximo año tendrás", proximo_año, "años")