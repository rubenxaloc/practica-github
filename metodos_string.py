variable1="Hola, que tal estás"
variable2="123123"
variable3="a"

veces=variable1.count("a")
print(veces) #Da dos pq la a con acento no cuenta

indice=variable1.find("a") #Encuentra la letra o palabra en esa variable (variable1), pero solo la primera
print(indice) #Las listas empiezan en cero

minusculas=variable1.lower()
print(minusculas)
print(minusculas.count("a"))
