# 33. Programa un código que permita contar el número de vocales de la siguiente frase: No 
# hay mal que dure cien años 

frase = "No hay mal que dure cien años"
frase_lower = frase.lower()

num_a = frase_lower.count('a')
num_e = frase_lower.count('e')
num_i = frase_lower.count('i')
num_o = frase_lower.count('o')
num_u = frase_lower.count('u')

print(f"El número de a es {num_a} el número de e es {num_e} el número de i es {num_i} el número de o es {num_o} y el número de u es {num_u}")