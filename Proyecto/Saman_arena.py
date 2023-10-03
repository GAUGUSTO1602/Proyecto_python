alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def crear_matriz(fila, columna): #Función para crear las matrices de los asientos (general y vip) de cada evento
    matriz = []
    for i in range(fila):
        matriz.append([])
        for j in range(columna):
            valor = "O"
            matriz[i].append(valor)
    
    return matriz


class asientos(): #Clase asientos
    def __init__(self, fila_general, columna_general, fila_vip, columna_vip, asientos_general, asientos_vip, tickets_general, tickets_vip, price_general, price_vip):
        
        #Se crean objetos de los asientos a traves de sus filas, columnas y tickets (Tanto general como vip)

        self.fila_general = fila_general
        self.columna_general = columna_general
        self.asientos_general = asientos_general
        self.tickets_general = tickets_general
        self.old_tickets_general = tickets_general
        self.price_general = price_general

        self.fila_vip = fila_vip
        self.columna_vip = columna_vip
        self.asientos_vip = asientos_vip
        self.tickets_vip = tickets_vip
        self.old_tickets_vip = tickets_vip
        self.price_vip = price_vip
    
    def get_fila_general(self):
        return self.fila_general

    def get_columna_general(self):
        return self.columna_general
    
    def get_fila_vip(self):
        return self.fila_vip

    def get_columna_vip(self):
        return self.columna_vip

    def get_asientos_general(self):
        return self.asientos_general
    
    def set_asientos_general(self, asiento_asignado):
        self.asientos_general = asiento_asignado
        return self.asientos_general

    def get_asientos_vip(self):
        return self.asientos_vip
    
    def set_asientos_vip(self, asiento_asignado):
        self.asientos_vip = asiento_asignado
        return self.asientos_vip   

    def get_tickets_general(self):
        return self.tickets_general
    
    def set_tickets_general(self, tickets_vendidos):
        self.tickets_general -= tickets_vendidos
        return self.tickets_general
    
    def set_old_tickets_general(self):
        self.tickets_general = self.old_tickets_general
        return self.tickets_general
    
    def get_tickets_vip(self):
        return self.tickets_vip
    
    def set_tickets_vip(self, tickets_vendidos):
        self.tickets_vip -= tickets_vendidos
        return self.tickets_vip
    
    def set_old_tickets_vip(self):
        self.tickets_vip = self.old_tickets_vip
        return self.tickets_vip
    
    def get_price_general(self):
        return self.price_general
    
    def get_price_vip(self):
        return self.price_vip
    
    def mostrar_asientos(self, fila, columna, matriz): #Función para imprimir de forma prsentable los asientos al usuario
        
        for x in range(columna + 1):
            if x == 0:
                print("  ", end=" ")
            else:
                print(x, end=" ")

        aux = 0
        print('')
        for fila in matriz:
            print(alfabeto[aux],"[", end="")
            aux += 1
            for elemento in fila:
                print("{}".format(elemento), end=" ")
            print("]")

    def Asignar_asiento(self, fila, columna, asientos): #Asigna el asiento escogido y devuelve un mensaje si el asiento ya esta ocupado

        if "X" in asientos[fila][columna]:
            print('')
            print('El asiento escogido esta ocupado')
            print('')
            return False
        else:
            asientos[fila][columna] = "X"
            return asientos

    def Resetear_asientos(self, lista, asiento): #Reestablce los asientos si el usuario decide no realizar la compra de los tickets
        
        for elemento in lista:
            x = elemento[0]
            j = elemento[1]
            if "X" in asiento[x][j]:
                asiento[x][j] = "O"
        
        return asiento

    def Reestablecer_asientos(self, asientos): #Funcion para vaciar todos los asientos

        for x in range(len(asientos)):
            for j in range(len(asientos[x])):
                if "X" in asientos[x][j]:
                    asientos[x][j] = "O"

        return asientos