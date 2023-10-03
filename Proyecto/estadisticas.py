from utils import*
import matplotlib.pyplot as plt

def Estadisticas(bd, msg):

    while True:

        while True:
            opt = validar_numero(msg)
            if 1 <= opt <= 6:
                break
            else:
                print('Error, valor introducido no valido')
    
      

        if opt == 1: #Calcula el promedio de gastos del cliente
            gasto_total = 0
            total_clients = 0
            gasto_cliente = []
            num_cliente = []
            print('')
            for key, value in bd["clients"].items():
                total_clients += 1
                num_cliente.append(total_clients)
                gasto = value.get_gastos()
                gasto_cliente.append(gasto)
                gasto_total += value.get_gastos()
            if total_clients == 0: #Si se escoge esta opción sin tener registrado algun cliente en la base de datos, el programa divide entre cero y salta error
                print('')
                print('No se ha registrado ningun cliente en la base de datos para realizar el calculo')
                print('')
            else:
                promedio = gasto_total / total_clients
                promedio = round(promedio, 2)
                print('A fecha de hoy, un cliente gasta aproximadamente: ${}'.format(promedio))
                print('')
         
        
        elif opt == 2: #Indica que porcentaje de clientes no compran en la feria de comida
            print('')
            feria_clients = 0
            total_clients = 0
            nombrar = ["Acceden a la feria", "No acceden a la feria"] #Lista para dar nombre a los elemento de la tabla
            for key, value in bd["clients"].items():
                if value.get_status_feria() == True: #Suma al contador si status_feria es igual a TRUE
                    feria_clients += 1
                total_clients += 1
            no_acceden = (feria_clients * 100)/total_clients
            no_acceden = round(no_acceden, 2)
            acceden= 100 - no_acceden
            porcentaje = [acceden, no_acceden]
            plt.pie(porcentaje, labels=nombrar)
            plt.show()
            print('El porcentaje de clientes que no compra en la feria de comida es de un: {}%'.format(no_acceden))
            print('')
         
            
        elif opt == 3: #Top 3 eventos de mayor ingreso de la feria
            print('')
            lista_evento = ordenar_eventos(bd)
            aux = 0
            top = 1
            print('Estos son los 3 eventos con mayores ingresos:')
            print('')
            nombres = []
            ingresos = []
            for evento in lista_evento:
                print('TOP {}'.format(top))
                print('Evento: {}'.format(evento.get_title()))
                print('Ingresos: ${}'.format(evento.get_ingresos()))
                print('')
                nombres.append(evento.get_title())
                ingresos.append(evento.get_ingresos())
                if aux == 2:
                    break
                aux += 1
                top += 1
            plt.bar(nombres, ingresos)
            plt.show()
            print('')

            
        elif opt == 4: #Top 3 clientes de mayor frecuencia
            print('')
            lista_clientes = ordenar_clientes(bd)
            aux = 0
            top = 1
            nombres = []
            frecuencia = []
            print('Estos son los 3 clientes que mas frecuentan los eventos:')
            print('')
            for cliente in lista_clientes:
                print('TOP {}'.format(top))
                print('Nombre: {}'.format(cliente.get_nombre()))
                print('Frecuencia: {}'.format(cliente.get_frecuencia()))
                print('')
                nombres.append(cliente.get_nombre())
                frecuencia.append(cliente.get_frecuencia())
                if aux == 2:
                    break
                aux += 1
                top += 1
            plt.bar(nombres, frecuencia)
            plt.show()
            print('')
        

        elif opt == 5: #Top 5 productos más vendidos
            print('')
            lista_productos = ordenar_productos(bd)
            aux = 0
            top = 1
            nombres = []
            vendido = []
            print('Estos son los 5 productos mas vendidos:')
            print('')
            for producto in lista_productos:
                print('TOP {}'.format(top))
                print('Producto: {}'.format(producto.get_name()))
                print('Cantidad vendida: {} unidades'.format(producto.get_amount_sell()))
                print('')
                nombres.append(producto.get_name())
                vendido.append(producto.get_amount_sell())
                if aux == 4:
                    break
                aux += 1
                top += 1
            plt.bar(nombres, vendido)
            plt.show()
            print('')
      

        else:
            return bd



def ordenar_eventos(bd): #Función para ordenar lso eventos segun sus ingresos

    lista_eventos = []

    for key, value in bd["events"].items():
        lista_eventos.append(value)

    long = len(lista_eventos)
    for i in range(long - 1):            
        menor = i
        for j in range(i+1, long):
            if lista_eventos[menor].get_ingresos() > lista_eventos[j].get_ingresos():
                menor = j
        temp = lista_eventos[i]
        lista_eventos[i] = lista_eventos[menor]
        lista_eventos[menor] = temp
    
    lista_eventos.reverse()

    return lista_eventos

def ordenar_productos(bd): #Ordena los productos segun la cantidad que se han vendido 

    lista_productos = []

    for key, value in bd["products"].items():
        for producto in value:
            lista_productos.append(producto) 

    long = len(lista_productos)
    for i in range(long - 1):            
        menor = i
        for j in range(i+1, long):
            if lista_productos[menor].get_amount_sell() > lista_productos[j].get_amount_sell():
                menor = j
        temp = lista_productos[i]
        lista_productos[i] = lista_productos[menor]
        lista_productos[menor] = temp
    
    lista_productos.reverse()
    
    return lista_productos

def ordenar_clientes(bd): #Ordena los clientes segun su frecuencia

    lista_clientes = []

    for key, value in bd["clients"].items():
        lista_clientes.append(value) 

    long = len(lista_clientes)
    for i in range(long - 1):            
        menor = i
        for j in range(i+1, long):
            if lista_clientes[menor].get_frecuencia() > lista_clientes[j].get_frecuencia():
                menor = j
        temp = lista_clientes[i]
        lista_clientes[i] = lista_clientes[menor]
        lista_clientes[menor] = temp
    
    lista_clientes.reverse()
    
    return lista_clientes