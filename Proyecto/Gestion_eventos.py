from utils import*
from Saman_arena import*

def evento_funciones(bd,msg, apertura_tickets):
    while True:
        
        while True:
            opt = validar_numero(msg)
            if 1 <= opt <= 4:
                break
            else:
                print('Error, valor introducido no valido')

        if opt == 1:
            print('')
            for key, value in bd["events"].items():
                print("-------------------------------------------------")
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
                print('')
                print("Asientos general:")
                print('')
                mostrar_asientos(value["asientos"].get_fila_general(), value["asientos"].get_columna_general(), value["asientos"].get_asientos_general())
                print('')
                print("Asientos vip:")
                print('')
                mostrar_asientos(value["asientos"].get_fila_vip(), value["asientos"].get_columna_vip(), value["asientos"].get_asientos_vip())
                print('')
                print(f'''Fecha del evento: {value["date"]}''')
                print("-------------------------------------------------")
        elif opt == 2:
            print('')
            while True:
                opt_2 = validar_numero('¿Quire cerrar/abrir la tienda de tickets?\n1.Abrir\n2.Cerrar\n3.Salir\n--> ')
                if 1 <= opt_2 <= 3:
                    if opt_2 == 1:
                        apertura_tickets = True
                        print('')
                        print('VENTAS DE TICKETS ABIERTAS')
                        print('')
                    elif opt_2 == 2:
                        apertura_tickets = False
                        print('')
                        print('VENTAS DE TICKETS CERRADAS CON EXITO')
                        print('')
                    else:
                        print('')
                        break
                else:
                    print('')
                    print('Error, valor introducido no valido')
                    print('')
        elif opt == 3:
            while True:
                print('')
                opt_2 = validar_numero('Ingrese para buscar por:\n1.Tipo\n2.Fecha\n3.Actor, cantante o banda en el cartel\n4.Nombre del evento\n5.Salir\n--> ')
                if opt_2 == 1:
                    while True:
                        opt_3 = validar_numero('Ingrese:\n1.Musical\n2.Teatral\n3.Salir\n--> ')
                        if 1 <= opt_3 <= 2:
                            imprimir_eventos(bd, dato_1="type", dato_2=opt_3, dato_3=False)
                        elif opt_3 == 3:
                            break
                        else:
                            print('Error, valor ingresado no valido')
                elif opt_2 == 2:
                    while True:
                        print('')
                        año = input('Ingrese el año:--> ')
                        mes = input('Ingrese el mes:--> ')
                        dia = input('Ingrese el dia:--> ')
                        fecha = "{}-{}-{}".format(año,mes,dia)
                        validacion = imprimir_eventos(bd, dato_1="date", dato_2=fecha, dato_3= False)
                        if validacion == False:
                            print('')
                            print('No se encuentran eventos o la fecha introducida es incorrecta')
                            print('') 
                        while True:
                            salida = validar_numero('¿Quiere ingresar otra fecha?:\n1.Si\n2.No\n--> ')
                            if 1 <= salida <= 2:
                                break
                            else:
                                print('Error, valor introducido no valido')
                                print('')
                        if salida == 2:
                            break
                elif opt_2 ==3:
                    while True:
                        print('')
                        nombre = input('Ingrese el nombre del cantante, banda o actor:\n(Cuide el uso de los espacios y de las mayusculas)\n--> ')
                        validacion = imprimir_eventos(bd, dato_1="cartel", dato_2=nombre, dato_3= True)
                        if validacion == False:
                            print('')
                            print('El nombre introducido no se encuentra en nuestra base de datos o es incorrecto')
                            print('') 
                        while True:
                            salida = validar_numero('¿Quiere ingresar otro nombre?:\n1.Si\n2.No\n--> ')
                            if 1 <= salida <= 2:
                                break
                            else:
                                print('Error, valor introducido no valido')
                                print('')
                        if salida == 2:
                            break       
                elif opt_2 == 4:
                    while True:
                        print('')
                        titulo = input('Ingrese el nombre del evento\n(Cuide le uso de espacios y mayusculas)\n--> ')
                        validacion =imprimir_eventos(bd, dato_1 ="title", dato_2=titulo, dato_3= False)
                        if validacion == False:
                            print('')
                            print('No se encuentran eventos o el nombre introducido es incorrecto')
                            print('') 
                        while True:
                            salida = validar_numero('¿Quiere ingresar otra nombre?:\n1.Si\n2.No\n--> ')
                            if 1 <= salida <= 2:
                                break
                            else:
                                print('Error, valor introducido no valido')
                                print('')
                        if salida == 2:
                            break
                elif opt_2 == 5:
                    break
                else:
                    print('Error, valor introducido no valido')
        elif opt == 4:
            return bd, apertura_tickets
                                          



#evento_funciones(payload, msg='Ingrese:\n1.Ver eventos disponibles\n2.Cerrar/Abrir la venta de tickets\n3.Buscar evento\n4.Salir\n--> ')