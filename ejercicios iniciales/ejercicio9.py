#9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos = int(input("Introduce un número de segundos: "))
minutos = segundos / 60
horas = segundos / 3600
print("El número de minutos es:", minutos, "y en horas es: ", horas)