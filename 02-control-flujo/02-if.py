edad = 18

if edad > 65:
    print("Puede ver la pelicula con super descuento")
elif edad > 54:
    print("Puede ver la pelicula con descuento")
elif edad > 17:
    print("Puedes ver la pelicula")
elif edad <= 17:
    print("No puedes ver esta pelicula")
# else:
#   print("No pudes entrar")
#  print("Ve a otro lado")

print("Listo!!")


# las condiciones se evaluan de arriba hacia abajo, si una se cumple, las demas no se evaluan. En el caso de la edad
# se debe ingresar la mayor edad hacia abajo para hacer cumplir los filtros
