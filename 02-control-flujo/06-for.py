# for numero in range(5):
#     print(numero, numero * "Hola Mundo")

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontré el numero buscado")

for auto in "ultimate python":
    print(auto)
