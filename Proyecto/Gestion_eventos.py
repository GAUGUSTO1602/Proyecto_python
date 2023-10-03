from utils import*
from Saman_arena import*
from Eventos import*

def evento_funciones(bd,msg):
    while True:
        
        while True:
            opt = validar_numero(msg) 
            if 1 <= opt <= 5:
                break
            else:
                print('Error, valor introducido no valido')

        if opt == 1: #Imprime toda la información de todos los eventos
            print('') 
            for key, value in bd["events"].items():
                print("-------------------------------------------------")
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
                print('')
                print("Asientos general:")
                print('')
                value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                print('')
                print("Asientos vip:")
                print('')
                value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                print('')
                print(f'''Fecha del evento: {value.get_date()}''')
                if value.get_apertura() == True:
                    print('Estado de apertura: Abierto')
                else:
                    print('Estado de apertura: Cerrado')
                print('')
                print(f'''Ingresos: ${value.get_ingresos()}''')
                print("-------------------------------------------------")
        elif opt == 2: #Opcion para abrir o cerrar los eventos
            print('')
            while True:
                for key, value in bd["events"].items():
                    print("{}: {}".format(key, value.get_title()))
                    print('')
                opt_2 = validar_numero('Seleccione el evento el cual desea abrir/cerrar la venta de tickets (Ingrese 0 para salir)\n--> ')
                if opt_2 in bd["events"]:
                    while True:
                        opt_3 = validar_numero('Ingrese para:\n1.Abrir\n2.Cerrar\n3.Salir\n--> ')
                        if opt_3 == 1:
                            bd["events"][opt_2].set_apertura(True)
                            print('')
                            print('***ESTADO DE APERTURA ACTUALIZADO***')
                            print('')
                            print('Se ha reanudado la venta de tickets para este evento')
                            print('')
                            break
                        elif opt_3 == 2:
                            bd["events"][opt_2].set_apertura(False)
                            print('')
                            print('***ESTADO DE APERTURA ACTUALIZADO***')
                            print('')
                            print('Se ha clausurado la venta de tickets para este evento')
                            print('')
                            break
                        elif opt_3 == 3:
                            print('')
                            break
                        else:
                            print('Error, valor introducido no valido')
                elif opt_2 == 0:
                    break
                else:
                    print('Error, valor introducido no valido')
        elif opt == 3: #Buscar evento por filtro
            while True:
                print('')
                opt_2 = validar_numero('Ingrese para buscar por:\n1.Tipo\n2.Fecha\n3.Actor, cantante o banda en el cartel\n4.Nombre del evento\n5.Salir\n--> ')
                if opt_2 == 1:
                    while True:
                        opt_3 = validar_numero('Ingrese:\n1.Musical\n2.Teatral\n3.Salir\n--> ') #Por tipo
                        if 1 <= opt_3 <= 2:
                            for key, value in bd["events"].items():
                                if value.get_tipo() == opt_3:
                                    print('')
                                    print("-------------------------------------------------")
                                    print(f'''Nombre del evento: {value.get_title()} ''')
                                    if value.get_tipo() == 1:
                                        print('Tipo de evento: Musical')
                                        print('Para este evento estaran presentes {} bandas'.format(value.get_bands()))
                                        print('Cantantes/Bandas que se presentaran:')
                                        for banda in value.get_cartel():
                                            print(banda)
                                        print('')
                                        print("Asientos general:")
                                        print('')
                                        value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                                        print('')
                                        print("Asientos vip:")
                                        print('')
                                        value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                                        print('')
                                        print(f'''Fecha del evento: {value.get_date()}''')
                                        if value.get_apertura() == True:
                                            print('Estado de apertura: Abierto')
                                        else:
                                            print('Estado de apertura: Cerrado')
                                        print('')
                                        print(f'''Ingresos: ${value.get_ingresos()}''')
                                        print("-------------------------------------------------")
                                        print('')
                                    else:
                                        print('Tipo de evento: Teatral')
                                        print(f'''Sipnosis: {value.get_synopsis()} ''')
                                        print('Actores estelares:')
                                        for actor in value.get_cartel():
                                            print(actor)
                                        print('')
                                        print("Asientos general:")
                                        print('')
                                        value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                                        print('')                    
                                        print("Asientos vip:")
                                        print('')
                                        value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                                        print('')
                                        print(f'''Fecha del evento: {value.get_date()}''')
                                        if value.get_apertura() == True:
                                            print('Estado de apertura: Abierto')
                                        else:
                                            print('Estado de apertura: Cerrado')
                                        print('')
                                        print(f'''Ingresos: ${value.get_ingresos()}''')
                                        print("-------------------------------------------------")
                                        print('')
                        elif opt_3 == 3:
                            break
                        else:
                            print('Error, valor ingresado no valido')
                elif opt_2 == 2: #Por fecha
                    while True:
                        validacion = False
                        lista_fechas = set()
                        print('')
                        print('Fechas de los eventos registradas en la base de datos:')
                        for key, value in bd["events"].items():
                            lista_fechas.add(value.get_date())
                        for date in lista_fechas:
                            print(date)
                            print('')
                        año = input('Ingrese el año (AAAA):--> ')
                        mes = input('Ingrese el mes (MM):--> ')
                        dia = input('Ingrese el dia (DD):--> ')
                        fecha = "{}-{}-{}".format(año,mes,dia)
                        for key, value in bd["events"].items():
                            if value.get_date() == fecha:
                                validacion = True
                                print('')
                                print("-------------------------------------------------")
                                print(f'''Nombre del evento: {value.get_title()} ''')
                                if value.get_tipo() == 1:
                                    print('Tipo de evento: Musical')
                                    print('Para este evento estaran presentes {} bandas'.format(value.get_bands()))
                                    print('Cantantes/Bandas que se presentaran:')
                                    for banda in value.get_cartel():
                                        print(banda)
                                    print('')
                                    print("Asientos general:")
                                    print('')
                                    value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                                    print('')
                                    print("Asientos vip:")
                                    print('')
                                    value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                                    print('')
                                    print(f'''Fecha del evento: {value.get_date()}''')
                                    print(f'''Ingresos: ${value.get_ingresos()}''')
                                    if value.get_apertura() == True:
                                        print('Estado de apertura: Abierto')
                                    else:
                                        print('Estado de apertura: Cerrado')
                                    print('')
                                    print("-------------------------------------------------")
                                    print('')
                                else:
                                    print('Tipo de evento: Teatral')
                                    print(f'''Sipnosis: {value.get_synopsis()} ''')
                                    print('Actores estelares:')
                                    for actor in value.get_cartel():
                                        print(actor)
                                    print('')
                                    print("Asientos general:")
                                    print('')
                                    value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                                    print('')                    
                                    print("Asientos vip:")
                                    print('')
                                    value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                                    print('')
                                    print(f'''Fecha del evento: {value.get_date()}''')
                                    if value.get_apertura() == True:
                                        print('Estado de apertura: Abierto')
                                    else:
                                        print('Estado de apertura: Cerrado')
                                    print('')
                                    print(f'''Ingresos: ${value.get_ingresos()}''')
                                    print("-------------------------------------------------")
                                    print('')
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
                elif opt_2 ==3: #Por nombre del cantante, banda o actor
                    while True:
                        validacion = False
                        print('')
                        for key, value in bd["events"].items():
                            for member in value.get_cartel():
                                print(member)
                        nombre = input('Ingrese el nombre del cantante, banda o actor\n--> ')
                        for key, value in bd["events"].items():
                            for elemento in value.get_cartel():
                                if elemento.replace(" ", "").lower().capitalize() == nombre.replace(" ", "").lower().capitalize():
                                    validacion = True
                                    print('')
                                    print("-------------------------------------------------")
                                    print(f'''Nombre del evento: {value.get_title()} ''')
                                    if value.get_tipo() == 1:
                                        print('Tipo de evento: Musical')
                                        print('Para este evento estaran presentes {} bandas'.format(value.get_bands()))
                                        print('Cantantes/Bandas que se presentaran:')
                                        for banda in value.get_cartel():
                                            print(banda)
                                        print('')
                                        print("Asientos general:")
                                        print('')
                                        value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                                        print('')
                                        print("Asientos vip:")
                                        print('')
                                        value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                                        print('')
                                        print(f'''Fecha del evento: {value.get_date()}''')
                                        if value.get_apertura() == True:
                                            print('Estado de apertura: Abierto')
                                        else:
                                            print('Estado de apertura: Cerrado')
                                        print('')
                                        print(f'''Ingresos: ${value.get_ingresos()}''')
                                        print("-------------------------------------------------")
                                        print('')
                                    else:
                                        print('Tipo de evento: Teatral')
                                        print(f'''Sipnosis: {value.get_synopsis()} ''')
                                        print('Actores estelares:')
                                        for actor in value.get_cartel():
                                            print(actor)
                                        print('')
                                        print("Asientos general:")
                                        print('')
                                        value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                                        print('')
                                        print("Asientos vip:")
                                        print('')
                                        value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                                        print('')
                                        print(f'''Fecha del evento: {value.get_date()}''')
                                        if value.get_apertura() == True:
                                            print('Estado de apertura: Abierto')
                                        else:
                                            print('Estado de apertura: Cerrado')
                                        print('')
                                        print(f'''Ingresos: ${value.get_ingresos()}''')
                                        print("-------------------------------------------------")
                                        print('')
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
                elif opt_2 == 4: #Por nombre del evento
                    while True:
                        validacion = False
                        print('')
                        print('')
                        for key, value in bd["events"].items():
                            print(value.get_title())
                            print('')
                        titulo = input('Ingrese el nombre del evento\n--> ')
                        for key, value in bd["events"].items():
                            if value.get_title().replace(" ", "").lower().capitalize() == titulo.replace(" ", "").lower().capitalize():
                                validacion = True
                                print('')
                                print("-------------------------------------------------")
                                print(f'''Nombre del evento: {value.get_title()} ''')
                                if value.get_tipo() == 1:
                                    print('Tipo de evento: Musical')
                                    print('Para este evento estaran presentes {} bandas'.format(value.get_bands()))
                                    print('Cantantes/Bandas que se presentaran:')
                                    for banda in value.get_cartel():
                                        print(banda)
                                    print('')
                                    print("Asientos general:")
                                    print('')
                                    value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                                    print('')
                                    print("Asientos vip:")
                                    print('')
                                    value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                                    print('')
                                    print(f'''Fecha del evento: {value.get_date()}''')
                                    if value.get_apertura() == True:
                                        print('Estado de apertura: Abierto')
                                    else:
                                        print('Estado de apertura: Cerrado')
                                    print('')
                                    print(f'''Ingresos: ${value.get_ingresos()}''')
                                    print("-------------------------------------------------")
                                    print('')
                                else:
                                    print('Tipo de evento: Teatral')
                                    print(f'''Sipnosis: {value.get_synopsis()} ''')
                                    print('Actores estelares:')
                                    for actor in value.get_cartel():
                                        print(actor)
                                    print('')
                                    print("Asientos general:")
                                    print('')
                                    value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_general(), value.get_asientos().get_columna_general(), value.get_asientos().get_asientos_general())
                                    print('')                    
                                    print("Asientos vip:")
                                    print('')
                                    value.get_asientos().mostrar_asientos(value.get_asientos().get_fila_vip(), value.get_asientos().get_columna_vip(), value.get_asientos().get_asientos_vip())
                                    print('')
                                    print(f'''Fecha del evento: {value.get_date()}''')
                                    if value.get_apertura() == True:
                                        print('Estado de apertura: Abierto')
                                    else:
                                        print('Estado de apertura: Cerrado')
                                    print('')
                                    print(f'''Ingresos: ${value.get_ingresos()}''')
                                    print("-------------------------------------------------")
                                    print('')
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
        elif opt == 4: #Reestablecer los asientos al estado original junto al numero de tickets disponibles 
            while True:
                opt_2 = validar_numero('¿Restablecer los asientos y tickets de los eventos?\n1.Si\n2.No\n--> ')
                if 1 <= opt_2 <= 2:
                    if opt_2 == 1: #Vacia los asientos y reestablece la cantidad de tickets disponibles para su venta
                        for key, value in bd["events"].items():
                            reestablecer = value.get_asientos().Reestablecer_asientos(value.get_asientos().get_asientos_general())
                            value.get_asientos().set_asientos_general(reestablecer)

                            reestablecer = value.get_asientos().Reestablecer_asientos(value.get_asientos().get_asientos_vip())
                            value.get_asientos().set_asientos_vip(reestablecer)

                            value.get_asientos().set_old_tickets_general()
                            value.get_asientos().set_old_tickets_vip()
                        print('')
                        print('ASIENTOS Y TICKETS REESTABLECIDOS CON EXITO')
                        print('')
                        break
                    else:
                        break
                else:
                    print('Error, valor introducido no valido')

        else:
            print('')
            return bd
                                          



