from  Animal import Animal
from Cliente import Cliente

perro = Animal("pequeño", "2 años", "labrador")
auxaccion = perro.comer()
print (auxaccion)

perro.imprimir_info()

objCliente= Cliente()
dato_nombre= objCliente.get_nombre()
print(dato_nombre)
objCliente.set_nombre("Eileen")
print(objCliente.get_nombre())

