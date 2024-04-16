# Importa la clase Te_artesanal del módulo te
from te import Te_artesanal

# Obtiene la preparacion recomendada para el tipo de te 1
eleccion1 = Te_artesanal.obt_preparacion_recomendacion(1)

# Obtiene la preparacion recomendada para el tipo de te 3
eleccion2 = Te_artesanal.obt_preparacion_recomendacion(3)

# Imprime el tipo de datos de ambas elecciones
print(type(eleccion1), type(eleccion2))

# Compara los tipos de datos de las elecciones
if type(eleccion1) == type(eleccion2):
    # Si ambos objetos son del mismo tipo, imprime este mensaje
    print("Ambos objetos son del mismo tipo")
else:
    # Si los objetos no son del mismo tipo, imprime este mensaje
    print("Los objetos no son del mismo tipo")