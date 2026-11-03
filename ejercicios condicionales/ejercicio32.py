# 32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
# no distinguir entre mayúsculas y minúsculas 

frase = "A quién madruga Dios ayuda"
palabra = input("Introduce una frase: ")

frase_lower = frase.lower()
palabra_lower = palabra.lower()

if palabra_lower in frase_lower:
    indice = frase_lower.find(palabra_lower)
    print(f"La palabra está en la frase y está en el índice {indice}")
else:
    print("La palabra no está en la frase")