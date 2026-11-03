# Crea un programa que pida la nota de un examen (un número decimal o entero del 0 al 10). 
# Utiliza una estructura condicional (if, elif, else) junto con operadores de comparación (>=, <=) 
# para comprobar en qué categoría se encuentra la nota:

nota = float(input("Introduce la nota del examen: "))
if nota >= 0 and nota <= 10:
    if nota <= 5:
        print("Suspenso")
    else:
        print("Aprobado")
else:
    print("Has introducido un valor incorrecto")