# Realiza un programa que pida al usuario el valor del lado de un cubo, calcule su volumen utilizando 
# el operador de potencia (**) y muestre el resultado formateado exactamente con 2 decimales utilizando f-strings.

lado = int(input("Introduce el valor del lado: "))
volumen = lado ** 3

print(f"El volumen del cubo es de {volumen:.2f} ")