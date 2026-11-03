#Crea un programa que pida al usuario el total de minutos transcurridos y calcule cuántas horas completas 
#son y cuántos minutos sobrantes quedan, utilizando los operadores de división entera (//) y resto (%).

minutos = int(input("Introduce el número de minutos transcurridos: "))
horas_completas = minutos // 60
minutos_sobrantes = minutos % 60

print(horas_completas)
print(minutos_sobrantes)