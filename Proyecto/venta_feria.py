from utils import validar_numero, validar_palabra, es_narcisista
from classes import*

def venta_feria(bd, msg):

    while True:

        while True:
            opt = validar_numero(msg)
            if 1<= opt <= 2:
                break
            else:
                print('Error, valor introducido no valido')

        if opt == 1:

            verificar_cedula = validar_numero('Ingrese su cedula:\n--> ')

            if verificar_cedula in bd["clients"]:
                print('')
                registro_compra = False
                lista_comidas = []
                lista_bebebidas = []
                aux_comida = 0
                aux_bebida = 0
                while True:
                    opt_2 = validar_numero('¿Que desea ordenar?\n1.Comidas\n2.Bebidas\n3.Salir\n--> ')
                    print('')
                    if 1<= opt_2 <= 3:
                        if opt_2 == 1:
                            while True:
                                opt_5 = None
                                if len(bd["products"]["Comidas"]) == 0:
                                    print('')
                                    print('Lo sentimos, ya no tenemos disponible este tipo de prodcutos')
                                    print('')
                                    break
                                for x in range(len(bd["products"]["Comidas"])):
                                    print(x+1, bd["products"]["Comidas"][x].get_name())
                                    print('Precio: ${}'.format(bd["products"]["Comidas"][x].get_price()))
                                    if bd["products"]["Comidas"][x].get_presentation() == 1:
                                        print('Presentación: Debe prepararse')
                                        print('') 
                                    else:
                                        print('Presentación: En paquete')
                                        print('')
                                print('')
                                print('***TODOS LOS PRECIOS INCLUYEN IVA***')
                                print('')
                                opt_3 = validar_numero('Ingrese el numero del producto que desee comprar\n--> ')   
                                if opt_3 - 1 > len(bd["products"]["Comidas"]) or opt_3 <= 0:
                                    print('')
                                    print('Error, valor introducido no valido')
                                    print('')
                                else:
                                    opt_3 -= 1
                                    while True:
                                        print('')
                                        cantidad = validar_numero('Ingrese la cantidad que desee comprar\n(Ingrese "0" para cancelar):\n\n--> ')
                                        print('')
                                        if cantidad < 0:
                                            print('Error, valor ingresado no valido')
                                        elif cantidad == 0:
                                            break
                                        elif cantidad > bd["products"]["Comidas"][opt_3].get_amount():
                                            print('')
                                            print('Lo sentimos, no tenemos la cantidad que solicita')
                                            print('')
                                        else:
                                            lista_comidas.append([])
                                            lista_comidas[aux_comida].append(bd["products"]["Comidas"][opt_3]) 
                                            lista_comidas[aux_comida].append(cantidad)
                                            registro_compra = True
                                            aux_comida += 1
                                            while True:
                                                opt_5 = validar_numero('¿Quiere comprar algo mas?\n1.Si\n2.No\n--> ')
                                                if 1 <= opt_5 <= 2:
                                                    break
                                                else:
                                                    print('')
                                                    print('Error, valor introucido no valido')
                                                    print('')
                                            break
                                    
                                        break
                                break

                            if opt_5 == 2:
                                break

                         
                                    
                        elif opt_2 == 2:
                            while True:
                                opt_5 = None
                                if len(bd["products"]["Bebidas"]) == 0:
                                    print('')
                                    print('Lo sentimos, ya no tenemos disponible este tipo de prodcutos')
                                    print('')
                                    break
                                for x in range(len(bd["products"]["Bebidas"])):
                                    print(x+1, bd["products"]["Bebidas"][x].get_name())
                                    print('Precios:')
                                    print('Pequeños: ${}'.format(bd["products"]["Bebidas"][x].get_price()))
                                    print('Medianos: ${}'.format(bd["products"]["Bebidas"][x].get_middle_price()))            
                                    print('Grandes: ${}'.format(bd["products"]["Bebidas"][x].get_big_price()))
                                    print('')
                                print('')
                                print('***TODOS LOS PRECIOS INCLUYEN IVA***')
                                print('')
                                opt_3 = validar_numero('Ingrese el numero del producto que desee comprar\n--> ')   
                                if opt_3 - 1 > len(bd["products"]["Bebidas"]) or opt_3 <= 0:
                                    print('')
                                    print('Error, valor introducido no valido')
                                    print('')
                                else:
                                    opt_3 -= 1
                                    while True:
                                        print('')
                                        tamano = validar_numero('Ingrese de que tamano quiere la(s) bebida(s)\n(Ingrese "0" para cancelar):\n1.Pequeñas\n2.Medianas\n3.Grandes\n--> ')
                                        print('')
                                        if tamano < 0 or tamano > 3:
                                            print('Error, valor ingresado no valido')
                                        elif tamano == 0:
                                            break
                                        else:
                                            while True:
                                                if tamano == 1:
                                                    cantidad = validar_numero('Ingrese la cantidad que desea comprar:\n--> ')
                                                    if cantidad > bd["products"]["Bebidas"][opt_3].get_little_amount():
                                                        print('')
                                                        print('Lo sentimos, no tenemos la cantidad que solicita')
                                                        print('')
                                                        break
                                                    else:
                                                        lista_bebebidas.append([])
                                                        lista_bebebidas[aux_bebida].append(bd["products"]["Bebidas"][opt_3])
                                                        lista_bebebidas[aux_bebida].append(tamano)
                                                        lista_bebebidas[aux_bebida].append(cantidad)
                                                        registro_compra = True
                                                        aux_bebida += 1
                                                elif tamano == 2:
                                                    cantidad = validar_numero('Ingrese la cantidad que desea comprar:\n--> ')
                                                    if cantidad > bd["products"]["Bebidas"][opt_3].get_middle_amount():
                                                        print('')
                                                        print('Lo sentimos, no tenemos la cantidad que solicita')
                                                        print('')
                                                        break
                                                    else:
                                                        lista_bebebidas.append([])
                                                        lista_bebebidas[aux_bebida].append(bd["products"]["Bebidas"][opt_3])
                                                        lista_bebebidas[aux_bebida].append(tamano)
                                                        lista_bebebidas[aux_bebida].append(cantidad)
                                                        registro_compra = True
                                                        aux_bebida += 1
                                                else:
                                                    cantidad = validar_numero('Ingrese la cantidad que desea comprar:\n--> ')
                                                    if cantidad > bd["products"]["Bebidas"][opt_3].get_big_amount():
                                                        print('')
                                                        print('Lo sentimos, no tenemos la cantidad que solicita')
                                                        print('')
                                                        break
                                                    else:
                                                        lista_bebebidas.append([])
                                                        lista_bebebidas[aux_bebida].append(bd["products"]["Bebidas"][opt_3])
                                                        lista_bebebidas[aux_bebida].append(tamano)
                                                        lista_bebebidas[aux_bebida].append(cantidad)
                                                        registro_compra = True
                                                        aux_bebida += 1

                                                while True:
                                                    opt_5 = validar_numero('¿Quiere comprar algo mas?\n1.Si\n2.No\n--> ')
                                                    if 1 <= opt_5 <= 2:
                                                        break
                                                    else:
                                                        print('')
                                                        print('Error, valor introucido no valido')
                                                        print('')
                                                break

                                            if 1 <= opt_5 <= 2:
                                                break
                                    break
                            if opt_5 == 2:
                                break
                       
                        else:
                            break
                                
                    else:
                        print('')
                        print('Error, valor introducido no valido')
                        print('')
                
                if registro_compra == True:
                    descuento = 0
                    aplicar_descuento = es_narcisista(verificar_cedula)
                    if aplicar_descuento == True:
                        print('')
                        print('¡Felcidades! usted recibira un "15%" de descuento en su compra total')
                        print('')
                    total = 0
                    print('----------RECIBO----------')
                    print('')
                    print('Subtotal:')
                    for compra in lista_comidas:
                        total += round(compra[0].get_price() * compra[1], 2)
                        print('{}: {} * {} = {}'.format(compra[0].get_name(), compra[0].get_price(), compra[1], round(compra[0].get_price() * compra[1], 2) ))
                    for compra in lista_bebebidas:
                        if compra[1] == 1:
                            total += round(compra[0].get_price() * compra[2], 2)
                            print('{}: {} * {} = {}'.format(compra[0].get_name(), compra[0].get_price(), compra[2], round(compra[0].get_price() * compra[2], 2)))
                        elif compra[1] == 2:
                            total += round(compra[0].get_middle_price() * compra[2], 2)
                            print('{}: {} * {} = {}'.format(compra[0].get_name(), compra[0].get_middle_price(), compra[2], round(compra[0].get_price() * compra[2], 2))) 
                        else:
                            total += round(compra[0].get_big_price() * compra[2], 2)
                            print('{}: {} * {} = {}'.format(compra[0].get_name(), compra[0].get_big_price(), compra[2], round(compra[0].get_price() * compra[2], 2)))
                    if aplicar_descuento == True:
                        descuento = total * 0.15
                        total -= descuento
                    print('Descuento: {}'.format(descuento))
                    print('TOTAL: {}'.format(total))
                    print('')
                    print('---------------------------')
                    print('')
                    while True:
                        final_opt = validar_numero('Proceder con la compra:\n1.Si\n2.No\n--> ')
                        if 1 <= final_opt <= 2:
                            if final_opt == 2:
                                print('')
                                print('RECIBO ELIMINADO')
                                print('')
                                break
                            else:
                                for compra in lista_comidas:
                                    compra[0].set_amount(compra[1])
                                for compra in lista_bebebidas:
                                    compra[0].set_amount(compra[2])
                                    if compra[1] == 1:
                                        compra[0].set_little_amount(compra[2])
                                    elif compra[1] == 2:
                                        compra[0].set_middle_amount(compra[2])
                                    else:
                                        compra[0].set_big_amount(compra[2])
                                print('')
                                print('PAGO REALIZADO CON EXITO')
                                print('')
                                print('GRACIAS POR SU COMPRA')
                                print('')
                                break
                        else:
                            print('Error, valor ingresado no valido')

                    
            
            else:
                print('')
                print('***Su numero de cedula no se encuentra en nuestra base de datos***')
                print('')
                print('***Debe realizar primero la compra de los tickets de cualquiera de los eventos disponibles para poder acceder a la feria***')
                print('')

        else:
            
            return bd


