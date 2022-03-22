from utils import validar_numero, validar_palabra, get_vampire
from Saman_arena import mostrar_asientos, Asignar_asiento, Resetear_asientos

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

                for key, value in bd["events"].items():
                    id_evento += 1
                    print("------------------ EVENTO:",id_evento,"------------------")
                    print('')
                    print(f'''Nombre del evento: {value["title"]} ''')
                    if value["type"] == 1:
                        print('Tipo de evento: Musical')
                        print('Para este evento estaran presentes {} bandas'.format(value["bands"]))
                        print('Cantantes/Bandas que se presentaran:')
                        for banda in value["cartel"]:
                            print(banda)
                    else:
                        print('Tipo de evento: Teatral')
                        print(f'''Sipnosis: {value["synopsis"]} ''')
                        print('Actores estelares:')
                        for actor in value["cartel"]:
                            print(actor)
                    print(f'''Fecha del evento: {value["date"]}''')
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

                    price_general_iva, aumento_general = get_price_iva(value["asientos"].get_price_general())
                    price_vip_iva, aumento_vip = get_price_iva(value["asientos"].get_price_vip())

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

                        if tipo_tickects == 1:
                            if value["asientos"].get_tickets_general() == 0:
                                print('')
                                print('Lo sentimos, ya no hay tickets de este tipo para este evento')
                                print('')
                                break
                            num_tickets = validar_numero('Ingrese cuantos tickets desea comprar:\n--> ')
                            if num_tickets <0 or num_tickets > value["asientos"].get_tickets_general():
                                print('')
                                print('Lo sentimos, no hay disponible la cantidad de tickets que solicita')
                                print('')
                            else:
                                break
                        else:
                            if value["asientos"].get_tickets_vip() == 0:
                                print('')
                                print('Lo sentimos, ya no hay tickets de este tipo para este evento')
                                print('')
                                break
                            num_tickets = validar_numero('Ingrese cuantos tickets desea comprar:\n--> ')
                            if num_tickets <0 or num_tickets > value["asientos"].get_tickets_vip():
                                print('')
                                print('Lo sentimos, no hay disponible la cantidad de tickets que solicita')
                                print('')
                            else:
                                break
                    

                    num_asientos = num_tickets
                    puestos = []
                    lista_reset = []
                    while True:
                        if num_asientos == 0:
                            break
                        elif tipo_tickects == 1:
                            print('')
                            mostrar_asientos(value["asientos"].get_fila_general(), value["asientos"].get_columna_general(), value["asientos"].get_asientos_general())
                            print('')
                            fila, letra = Seleccionar_fila(msg="Ingrese fila:\n--> ", filas=value["asientos"].get_fila_general())
                            columna = Seleccionar_columna(msg="Ingrese fila:\n--> " , columnas=value["asientos"].get_columna_general())
                            validar_puesto = Asignar_asiento(fila, columna, value["asientos"].get_asientos_general())
                            if validar_puesto != False:
                                value["asientos"].set_asientos_general(validar_puesto)
                                lista_reset.append([fila, columna])
                                num_asientos -= 1
                                columna += 1
                                puesto = letra + str(columna)
                                puestos.append(puesto)
                        else:
                            print('')
                            mostrar_asientos(value["asientos"].get_fila_vip(), value["asientos"].get_columna_vip(), value["asientos"].get_asientos_vip())
                            print('')
                            fila, letra = Seleccionar_fila(msg="Ingrese fila:\n--> ", filas=value["asientos"].get_fila_vip())
                            columna = Seleccionar_columna(msg="Ingrese fila:\n--> " , columnas=value["asientos"].get_columna_vip())
                            validar_puesto = Asignar_asiento(fila, columna, value["asientos"].get_asientos_vip())
                            if validar_puesto != False:
                                value["asientos"].set_asientos_vip(validar_puesto)
                                lista_reset.append([fila, columna])
                                num_asientos -= 1
                                columna += 1
                                puesto = letra + str(columna)
                                puestos.append(puesto) 
                    
                    aplicar_descuento = get_vampire(cedula)
                    descuento = 0
                    if aplicar_descuento == True:
                        if tipo_tickects == 1:
                            descuento = price_general_iva * 0.50
                            final_price_general = price_general_iva - descuento
                            print('')
                            print('¡Felictaciones! usted recibira un "50%" de descuento')
                            print('')
                        else:
                            descuento = price_vip_iva * 0.50
                            final_price_vip = price_vip_iva - descuento
                            print('')
                            print('¡Felictaciones! usted recibira un "50%" de descuento')
                            print('')
                    else:
                        if tipo_tickects == 1:
                            final_price_general = price_general_iva
                        else:
                            final_price_vip = price_vip_iva
                    print('')
                    print("---------------RECIBO---------------")
                    print('')
                    print("Evento: {}".format(value["title"]))
                    if len(puestos) == 1:
                        print('Asientos: {}'.format(puestos[0]))
                    else:
                        print('Asientos')
                        for puesto in puestos:
                            print(puesto, end=", ")
                    print('')
                    print('')
                    print('***Cuenta***')
                    print('Tickets: {}'.format(num_tickets))
                    if tipo_tickects == 1:
                        print('Ticket general: {}'.format(value["asientos"].get_price_general()))
                        print('IVA: {}'.format(aumento_general)) 
                        print('Descuento: {}'.format(descuento))
                        print('Subtotal: {} x {}'.format(final_price_general, num_tickets))
                        print('')
                        print('TOTAL: {}'.format(final_price_general * num_tickets))
                        total = final_price_general * num_tickets
                    else:
                        print('Ticket VIP: {}'.format(value["asientos"].get_price_vip()))
                        print('IVA: {}'.format(aumento_vip)) 
                        print('Descuento: {}'.format(descuento))
                        print('Subtotal: {} x {}'.format(final_price_vip, num_tickets))
                        print('')
                        print('TOTAL: {}'.format(final_price_vip * num_tickets))
                        total = final_price_vip * num_tickets
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
                    if final_opt == 2:
                        if tipo_tickects == 1:
                            valor_reset = Resetear_asientos(lista= lista_reset, asiento=value["asientos"].get_asientos_general())
                            value["asientos"].set_asientos_general(valor_reset)
                        else:
                            valor_reset = Resetear_asientos(lista= lista_reset, asiento=value["asientos"].get_asientos_vip())
                            value["asientos"].set_asientos_vip(valor_reset)
                        print('')
                        print('RECIBO ELIMINADO')
                        print('')
                    else:
                        if tipo_tickects == 1:
                            value["asientos"].set_tickets_general(num_tickets)
                        else:
                            value["asientos"].set_tickets_vip(num_tickets)
                        bd["clients"][cedula] = {"Nombre": nombre, "Edad": edad, "Gastos": total, "Feria": False}
                        print('')
                        print('PAGO REALIZADO CON EXITO')
                        print('')
                        print('GRACIAS POR SU COMPRA')
                        print('')
                    
                       
        else:
            return bd

def get_price_iva(price):
    iva = 0.16
    aumento = price * iva
    final_price = price + aumento
    final_price = round(final_price, 2)
    return final_price, aumento

def Seleccionar_fila(msg, filas):

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

def Seleccionar_columna(msg, columnas):

    while True:
        columna = validar_numero(msg)
        if columna > 0 and columna <= columnas:
            return columna -1
        else:
            print('Error, valor ingresado no valido')