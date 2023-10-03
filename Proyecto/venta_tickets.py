from utils import validar_numero, validar_palabra, get_vampire
from Saman_arena import*
from Clientes import Clientes

def venta_tickets(bd,msg):
    
    while True:

        while True:
            opt = validar_numero(msg)
            if 1 <= opt <= 2:
                break
            else:
                print('Error, valor introducido no valido')

        if opt == 1:
            print('')
            nombre = validar_palabra('Ingrese el nombre:\n--> ')
            print('')
            cedula = validar_numero('Ingrese la cedula:\n--> ')
            print('')
            
            while True:
                print('')
                edad = validar_numero('Ingrese la edad:\n--> ')
                print('')
                if 1 <= edad <= 100:
                    break
                else:
                    print('')
                    print('Error')
                    print('')
                    print('Por favor, ingresar una edad valida')

            while True:
                
                id_evento = 0
                # Imprimir los eventos y se le asigna un id que coincide con el que tienen como key en la base de datos
                for key, value in bd["events"].items():
                    id_evento += 1
                    print("------------------ EVENTO:",id_evento,"------------------")
                    print('')
                    print(f'''Nombre del evento: {value.get_title()} ''')
                    if value.get_tipo() == 1:
                        print('Tipo de evento: Musical')
                        print('Para este evento estaran presentes {} bandas'.format(value.get_bands()))
                        print('Cantantes/Bandas que se presentaran:')
                        for banda in value.get_cartel():
                            print(banda)
                    else:
                        print('Tipo de evento: Teatral')
                        print(f'''Sipnosis: {value.get_synopsis()} ''')
                        print('Actores estelares:')
                        for actor in value.get_cartel():
                            print(actor)
                    print(f'''Fecha del evento: {value.get_date()}''')
                    if value.get_apertura() == True:
                        print('Estado de apertura: Abierto')
                    else:
                        print('Estado de apertura: Cerrado')
                    print('')
                    print("----------------------------------------------------")
                print('')
                

                while True:
                    opt_evento = validar_numero('Ingrese el número del evento al cual desea asistir:\n--> ')
                    if 1 <= opt_evento <= 4:
                        break
                    else:
                        print('')
                        print('Error, valor introducido no valido')
                        print('')
                
                if 1 <= opt_evento <= 4:
                        break


            for key, value in bd["events"].items():
                if key == opt_evento:

                    if value.get_apertura() == False: #Si el evento esta clausurado se entra aquí
                        print('')
                        print('Lo sentimos, este evento se encuentra cerrado')
                        print('')
                        break

                    #Obtiene el aumento por IVA y el precio nuevo con este 
                    price_general_iva, aumento_general = get_price_iva(value.get_asientos().get_price_general())
                    price_vip_iva, aumento_vip = get_price_iva(value.get_asientos().get_price_vip())

                    while True:
                        print('')
                        tipo_tickects = validar_numero('Ingrese el tipo de tickets que desee comprar:\n1.General ${}\n2.VIP ${}\n--> '.format(price_general_iva, price_vip_iva))
                        print('')
                        if 1 <= tipo_tickects <= 2:
                            break
                        else:
                            print('')
                            print('Error, valor introducido no valido')
                            print('')

                    while True:
                        tickets_agotados = False
                        if tipo_tickects == 1:
                            if value.get_asientos().get_tickets_general() == 0: #Si no quedan tickets generales para la función (Asientos llenos)
                                print('')
                                print('Lo sentimos, ya no hay tickets de este tipo para este evento')
                                print('')
                                tickets_agotados = True
                                break
                            num_tickets = validar_numero('Ingrese cuantos tickets desea comprar:\n--> ')
                            if num_tickets <0 or num_tickets > value.get_asientos().get_tickets_general(): #Si la cantidad de tickets solicitados es mayor a la disponible
                                print('')
                                print('Lo sentimos, no hay disponible la cantidad de tickets que solicita')
                                print('')
                            else:
                                break
                        else:
                            if value.get_asientos().get_tickets_vip() == 0: #Si no quedan tickets vip para la función (Asientos llenos)
                                print('')
                                print('Lo sentimos, ya no hay tickets de este tipo para este evento')
                                print('')
                                tickets_agotados = True
                                break
                            num_tickets = validar_numero('Ingrese cuantos tickets desea comprar:\n--> ')
                            if num_tickets <0 or num_tickets > value.get_asientos().get_tickets_vip(): #Si la cantidad de tickets solicitados es mayor a la disponible
                                print('')
                                print('Lo sentimos, no hay disponible la cantidad de tickets que solicita')
                                print('')
                            else:
                                break
                    if tickets_agotados == True: #Devuelve al cliente al menu si ya no hay tikets para el evento que solicito
                        break
                    

                    num_asientos = num_tickets #Asientos que debe asignar el cliente
                    puestos = [] #Se guardan los asientos seleccionados
                    lista_reset = [] #Lista en caso del cliente decida no realizar la compra
                    while True:
                        if num_asientos == 0:
                            break
                        elif tipo_tickects == 1:
                            print('')
                            # Se imprime la matriz de los asientos
                            value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                            print('')
                            fila, letra = Seleccionar_fila(msg="Ingrese fila:\n--> ", filas=value.get_asientos().get_fila_general())
                            columna = Seleccionar_columna(msg="Ingrese Columna:\n--> " , columnas=value.get_asientos().get_columna_general())
                            validar_puesto = value.get_asientos().Asignar_asiento(fila, columna, value.get_asientos().get_asientos_general())
                            if validar_puesto != False: #Si entra, se asigna y se guarda el asiento
                                value.get_asientos().set_asientos_general(validar_puesto)
                                lista_reset.append([fila, columna])
                                num_asientos -= 1
                                columna += 1
                                puesto = letra + str(columna)
                                puestos.append(puesto)
                        else:
                            print('')
                            value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                            print('')
                            fila, letra = Seleccionar_fila(msg="Ingrese fila:\n--> ", filas=value.get_asientos().get_fila_vip())
                            columna = Seleccionar_columna(msg="Ingrese Columna:\n--> " , columnas=value.get_asientos().get_columna_vip())
                            validar_puesto = value.get_asientos().Asignar_asiento(fila, columna, value.get_asientos().get_asientos_vip())
                            if validar_puesto != False: #Si entra, se asigna y se guarda el asiento
                                value.get_asientos().set_asientos_vip(validar_puesto)
                                lista_reset.append([fila, columna])
                                num_asientos -= 1
                                columna += 1
                                puesto = letra + str(columna)
                                puestos.append(puesto) 
                    
                    aplicar_descuento = get_vampire(cedula) #Verificar numero vampiro
                    descuento = 0
                    if aplicar_descuento == True:
                        if tipo_tickects == 1:
                            descuento = round(price_general_iva * num_tickets, 2) * 0.50
                            final_price_general = round(price_general_iva * num_tickets, 2) - descuento
                            print('')
                            print('¡Felictaciones! usted recibira un "50%" de descuento en el total de su compra')
                            print('')
                        else:
                            descuento = round(price_vip_iva * num_tickets, 2) * 0.50
                            final_price_vip = round(price_vip_iva * num_tickets, 2) - descuento
                            print('')
                            print('¡Felictaciones! usted recibira un "50%" de descuento en el total de su compra')
                            print('')
                    else:
                        if tipo_tickects == 1:
                            final_price_general = round(price_general_iva * num_tickets, 2)
                        else:
                            final_price_vip = round(price_vip_iva * num_tickets, 2)
                    print('')
                    print("---------------RECIBO---------------")
                    print('')
                    print("Evento: {}".format(value.get_title()))
                    if len(puestos) == 1:
                        print('Asiento: {}'.format(puestos[0]))
                    else:
                        print('Asientos:')
                        for puesto in puestos:
                            print(puesto, end=", ")
                    print('')
                    print('')
                    print('           ****CUENTA****')
                    print('Tickets: {}'.format(num_tickets))
                    if tipo_tickects == 1:
                        print('Ticket general: ${}'.format(value.get_asientos().get_price_general()))
                        print('IVA: ${}'.format(aumento_general)) 
                        print('Subtotal: ${} x {} = {}'.format(round(price_general_iva, 2), num_tickets, round(price_general_iva * num_tickets, 2)))
                        print('Descuento: ${}'.format(descuento))
                        print('')
                        print('TOTAL: ${}'.format(final_price_general))
                        total = final_price_general
                    else:
                        print('Ticket VIP: ${}'.format(value.get_asientos().get_price_vip()))
                        print('IVA: ${}'.format(aumento_vip)) 
                        print('Subtotal: ${} x {} = {}'.format(round(price_vip_iva, 2), num_tickets, round(price_vip_iva * num_tickets, 2)))
                        print('Descuento: ${}'.format(descuento))
                        print('')
                        print('TOTAL: ${}'.format(final_price_vip))
                        total = final_price_vip
                    print('')
                    print('---------------------------------------')
                    print('')
                    while True:
                        final_opt = validar_numero('Proceder con la compra:\n1.Si\n2.No\n--> ')
                        if 1 <= final_opt <= 2:
                            break
                        else:
                            print('')
                            print('Error, valor introducido no valido')
                            print('')
                    if final_opt == 2: #Si se decide no realizar la compra, se resetean los asientos que se asignaron en la operación
                        if tipo_tickects == 1:
                            valor_reset = value.get_asientos().Resetear_asientos(lista= lista_reset, asiento=value.get_asientos().get_asientos_general())
                            value.get_asientos().set_asientos_general(valor_reset)
                        else:
                            valor_reset = value.get_asientos().Resetear_asientos(lista= lista_reset, asiento=value.get_asientos().get_asientos_vip())
                            value.get_asientos().set_asientos_vip(valor_reset)
                        print('')
                        print('RECIBO ELIMINADO')
                        print('')
                        
                    else:
                        if tipo_tickects == 1: #Se restan los tickets comprados
                            value.get_asientos().set_tickets_general(num_tickets)
                        else:
                            value.get_asientos().set_tickets_vip(num_tickets)

                        if cedula in bd["clients"]: #Si el cliente ya esta en la base de datos
                            bd["clients"][cedula].set_frecuencia()
                            bd["clients"][cedula].set_gastos(total)

                        else: #Si el cliente es nuevo
                            gastos = total
                            status_feria = False
                            frecuencia = 1
                            cliente = Clientes(nombre, edad, gastos, status_feria, frecuencia)
                            bd["clients"][cedula] = cliente
                        
                        value.set_ingresos(total) #Se suman los ingresos que obtuvo el evento con la venta
                        print('')
                        print('PAGO REALIZADO CON EXITO')
                        print('')
                        print('GRACIAS POR SU COMPRA')
                        print('')
                    
                       
        else:
            print('')
            return bd

def get_price_iva(price): #Función para obtener los precios con IVa
    iva = 0.16
    aumento = price * iva
    final_price = price + aumento
    final_price = round(final_price, 2)
    return final_price, aumento

def Seleccionar_fila(msg, filas): #Función para validar la fila ingresada

    while True:
        fila = validar_palabra(msg)
        fila = fila.upper()
        if fila == "A" and filas >= 1:            
            return 0, fila
        elif fila == "B" and filas >= 2:
            return 1, fila
        elif fila == "C" and filas >= 3:
            return 2, fila
        elif fila == "D" and filas >= 4:
            return 3, fila
        elif fila == "E" and filas >= 5:
            return 4, fila
        else:
            print('Fila ingresada no valida')

def Seleccionar_columna(msg, columnas): #Función para ingresar la columna ingresada

    while True:
        columna = validar_numero(msg)
        if columna > 0 and columna <= columnas:
            return columna -1
        else:
            print('Error, valor ingresado no valido')