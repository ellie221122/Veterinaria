class Cliente:
    def __init__(self):
        self.nombre="" 
        self.apellido=""
        self.cedula=""
        
    def set_nombre(self, dato_nombre):
        self.nombre = dato_nombre
    def get_nombre(self):
        return self.nombre
    
    def pagar(self):
        return "cliente pobre"
    
    def imprin_dato(self):
        mensaje = "nombre: "+self.nombre
        print(mensaje)
