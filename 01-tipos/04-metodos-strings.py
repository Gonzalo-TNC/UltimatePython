animal = "  chanCHito feliz   "

print(animal.upper())  # Devuelve todo en mayuscula
print(animal.lower())  # Devuelve todo en minuscula
print(animal.capitalize())  # Devuelve la primera letra en mayuscula
print(animal.title())  # Devuelve la primera letra de cada palabra en mayuscula
print(animal.strip())  # Elimina todos los espacios a la derecha e izquierda
print(animal.lstrip())  # Elimina todos los espacios a la izquierda
print(animal.rstrip())  # Elimina todos los espacios a la derecha
print(animal.find("CH"))
# Encuentra el string indicado entre parentesis- Debe ser exacto como esta escrito (sensitive case)
print(animal.replace("nCH", "j"))
# Reemplaza el string indicado entre parentesis por el segundo string, separado por una coma (Sensitive case)
print("nCH" in animal)
# Devuelve un boleano, bajo la consulta si el string indicado esta en la variable
