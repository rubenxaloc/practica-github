#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
#y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro. 

lado = float(input("Introduce el valor del lado del trapecio: "))
base_menor = float(input("Introduce el valor de la base menor del trapecio: "))
base_mayor = float(input("Introduce el valor de la base mayor del trapecio: "))
altura = float(input("Introduce el valor de la altura del trapecio: "))

perimetro = base_mayor + base_menor + (2 * lado)
area = ((base_mayor + base_menor) * altura) / 2

print(f"El perímetro es: {perimetro}")
print(f"El área es: {area}")