# 34. Corrige los 4 errores o añade el código que necesites para que el siguiente programa se 
# ejecute correctamente

# inicializo valores a cada variable
var_numero = str(6 / 34)
var_suma = 0
# obtengo su longitud
var_longitud = len(var_numero)
# sumo cada dígito convirtiéndolo a entero a partir del índice de cada posición
var_suma = int(var_numero[1]) + int(var_numero[2]) + int(var_numero[3]) + int(var_numero[4])
# utilizo una condición y el operador aritmético % para ver si es par
if var_suma % 2 == 0:
    print(f"el valor de {var_suma} es par")
else:
    print(f"el valor de {var_suma} es impar")