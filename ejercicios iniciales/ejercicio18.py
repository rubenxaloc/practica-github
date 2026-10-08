#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine. 

PRECIO_ENTRADA = 12.0
DESCUENTO_ADULTO = 0.10
DESCUENTO_MENOR = 0.50

precio_adulto = PRECIO_ENTRADA * (1 - DESCUENTO_ADULTO)
precio_menor = PRECIO_ENTRADA * (1 - DESCUENTO_MENOR)

num_adultos = int(input("Introduce el número de adultos: "))
num_menores = int(input("Introduce el número de menores: "))

subtotal_adultos = num_adultos * precio_adulto
subtotal_menores = num_menores * precio_menor

print(f"El precio total del cine para {num_menores} menor/es es: {subtotal_menores:.2f} ")
print(f"El precio total del cine para {num_adultos} adulto/s es: {subtotal_adultos:.2f} ")
