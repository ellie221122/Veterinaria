from Cliente import Cliente

class Animal:
   
   def __init__(self, dato_tamaño, dato_edad, dato_raza):
      
      self.tamaño = dato_tamaño
      self.edad = dato_edad
      self.raza = dato_raza
      self.estado = self.llorar()
      self.objCliente= Cliente()

   def llorar(self):
        mensaje= "animal llorando..."
        print(mensaje)
      

   def comer(self):
        
        mensaje= "animal comiendo..."
        return mensaje
   
   def dormir():
        mensaje="animal dormido"

   def imprimir_info(self):
       mensaje = "tamaño: "+self.tamaño+" raza: "+self.raza
       print(mensaje)
       self.objCliente.imprin_dato()

