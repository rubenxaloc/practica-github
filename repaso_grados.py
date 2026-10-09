grados=float(input("Introduce los grados: "))
#F=C*9/5+32

calculo=grados * 9/5 +32
print("Temperatura:", calculo, "ºF")

#Otra manera de presentar la información con un print
# print(f"Segunda manera de presentar Temperatura: {calculo} ºF")

#primer método de redondeo
print(round(calculo, 2))