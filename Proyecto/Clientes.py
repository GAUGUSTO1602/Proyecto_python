class Clientes(): #Clase clientes
    def __init__(self, nombre, edad, gastos, status_feria, frecuencia):

        self.nombre = nombre
        self.edad = edad
        self.gastos = gastos
        self.status_feria = status_feria
        self.frecuencia = frecuencia
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_gastos(self):
        return self.gastos
    
    def set_gastos(self, nuevo_gasto):
        self.gastos += nuevo_gasto
        return self.gastos
    
    def get_status_feria(self):
        return self.status_feria
    
    def set_status_feria(self): #Si el cliente que compro tickets también compro en la feria, se activa esta función, indicando que compro en esta ultima
        self.status_feria = True
        return self.status_feria
    
    def get_frecuencia(self):
        return self.frecuencia
    
    def set_frecuencia(self): #Aumenta en relación a las visitas del cliente
        self.frecuencia += 1
        return self.frecuencia





