from utils import*


def feria_funciones(bd, restablecer_bd, msg):

    while True:
        opt = validar_numero(msg)
        if 1 <= opt <= 5:
            if opt == 1:
                print('')
                for key, value in bd["products"].items(): #Imprime la información de todos los productos presentes en el menu
                    print(key)
                    print('')
                    for producto in value:
                        imprimir_productos(producto, key)
            elif opt == 2: #Opción para eliminar un producto
                while True:
                    opt_2 = validar_numero('Ingrese para eliminar un producto:\n1.Comida\n2.Bebida\n3.Salir\n--> ')
                    print('')
                    if 1 <= opt_2 <= 3:
                        if opt_2 == 1:
                            while True:
                                for x in range(len(bd["products"]["Comidas"])):
                                    print(x + 1, bd["products"]["Comidas"][x].get_name())
                                    print('')
                                if len(bd["products"]["Comidas"]) == 0: #Si ya no quedan productos de este tipo para eliminar se imprime el siguiente mensaje
                                    print('')
                                    print('Ya no hay productos de este tipo en la base de datos')
                                    print('')
                                    break
                                opt_3 = validar_numero('Ingrese el numero del producto que desee eliminar:\n--> ')
                                if opt_3-1 > len(bd["products"]["Comidas"]) or opt_3 <= 0: #Si el valor introducido no coincide
                                    print('Error, valor introducido no valido')
                                    print('')
                                else:
                                    bd["products"]["Comidas"].pop(opt_3-1)
                                    break
                        elif opt_2 == 2:
                            while True:
                                for x in range(len(bd["products"]["Bebidas"])):
                                    print(x + 1, bd["products"]["Bebidas"][x].get_name())
                                    print('')
                                if len(bd["products"]["Bebidas"]) == 0: #Si ya no quedan productos de este tipo se imprime el siguiente mensaje
                                    print('')
                                    print('Ya no hay productos de este tipo en la base de datos')
                                    print('')
                                    break
                                opt_3 = validar_numero('Ingrese el numero del producto que desee eliminar:\n--> ')
                                if opt_3 -1 > len(bd["products"]["Bebidas"]) or opt_3 <= 0: #Si el valor introducido no coincide
                                    print('Error, valor introducido no valido')
                                    print('')
                                else:
                                    bd["products"]["Bebidas"].pop(opt_3-1)
                                    break
                        else:
                            break
                    else:
                        print('Error, valor introducido no valido')         
            elif opt == 3: #Buscar productos por filtros
                while True:
                    opt_2 = validar_numero('Ingrese para buscar por:\n1.Nombre\n2.Tipo\n3.Rango de precios\n4.Salir\n--> ')
                    if 1 <= opt_2 <= 4:
                        if opt_2 == 1: #Busqueda por nombre
                            while True:
                                print('')
                                for key, value in bd["products"].items():
                                    for producto in value:
                                        print(producto.get_name())
                                validacion = False
                                nombre = input('Ingrese el nombre del producto\n--> ')
                                print('')
                                for key, value in bd["products"].items():
                                    for producto in value:
                                        if producto.get_name().replace(" ", "").lower().capitalize() == nombre.replace(" ", "").lower().capitalize():
                                            validacion = True
                                            imprimir_productos(producto, key)
                                            print('')
                                if validacion == False:
                                    print('El producto ingresado no se encuentra en la base de datos')
                                while True:
                                    opt_3 = validar_numero('¿Desea buscar otro producto?:\n1.Si\n2.No\n--> ')
                                    if 1 <= opt_3 <= 2:
                                        break
                                    else:
                                        print('Error, valor introducido no valido')
                                if opt_3 == 2:
                                    break        
                        elif opt_2 == 2: #Busqueda por tipo
                            while True:
                                print('')
                                opt_3 = validar_numero('Ingrese tipo de producto:\n1.Comidas\n2.Bebidas\n3.Salir\n--> ')
                                print('')
                                if 1 <= opt_3 <=3:
                                    if opt_3 == 1:
                                        print('')
                                        for producto in bd["products"]["Comidas"]:
                                            imprimir_productos(producto, key=None)
                                    elif opt_3 == 2:
                                        for producto in bd["products"]["Bebidas"]:
                                            imprimir_productos(producto, key="Bebidas")
                                    else:
                                        break
                                else:
                                    print('Error, valor introducido no valido')
                        elif opt_2 == 3:
                            lista = []
                            for key, value in bd["products"].items():
                                for producto in value:
                                    lista.append(producto) 
                            lista_ordenada = ordenar_productos(lista)
                            while True:
                                opt_3 = validar_numero('Ingrese tipo de busqueda:\n1.Ascendente\n2.Descendente\n3.Salir\n--> ')
                                if 1 <= opt_3 <= 3:
                                    if opt_3 == 1:
                                        for producto in lista_ordenada:
                                            imprimir_productos(producto, key= "ordenar")
                                    elif opt_3 == 2:
                                        lista_ordenada.reverse()
                                        for producto in lista_ordenada:
                                            imprimir_productos(producto, key= "ordenar")
                                    else:
                                        break
                                else:
                                    print('Error, valor introducido no valido')
                        else:
                            break
                    else:
                        print('Error, valor introducido no valido')
            elif opt == 4: #Opción para reestablcer los productos eliminados del menu y las existencias
                while True:
                    opt_2 = validar_numero('¿Quiere restablecer el inventario y el menu?\n1.Si\n2.No\n--> ')
                    if 1 <= opt_2 <= 2:
                        if opt_2 == 1:
                            bd["products"] = restablecer_bd["products"]
                            for key, value in bd["products"].items():
                                for producto in value:
                                    producto.set_old_amount() #Se reestablce las existencias deacuerdo a su cantidad inicial al crear la base de datos local
                                if key == "Bebidas":
                                    for bebida in value:
                                        bebida.set_all_old_amount()
                            print('Inventario y menu reestablecidos exitosamente')
                            print('')
                            break
                        else:
                            break
                    else:
                        print('Error, valor introducido no valido')    
            else:
                print('')
                return bd
        else:
            print('Error, valor introducido no valido')


def imprimir_productos(producto, key): #Función para imprimir los productos de acuerod a unas variables
    print('Producto: {}'.format(producto.get_name()))
    print('Unidades en inventario: {}'.format(producto.get_amount()))
    if key == "Bebidas" or key == "ordenar":
        try: #Para imprimir de forma ordenada sin que resulte en error
            print('Pequeños: {} unidades'.format(producto.get_little_amount()))
            print('Medianos: {} unidades'.format(producto.get_middle_amount()))            
            print('Grandes: {} unidades'.format(producto.get_big_amount()))
            print('')
        except:
            if producto.get_presentation() == 1:
                print('Presentación: Debe prepararse')
                print('') 
            else:
                print('Presentación: En paquete')
                print('')
    else:
        if producto.get_presentation() == 1:
            print('Presentación: Debe prepararse')
            print('') 
        else:
            print('Presentación: En paquete')
            print('')

def ordenar_productos(lista_ordena): #Ordenar los productos segun su precio

    long = len(lista_ordena)
    for i in range(long - 1):            
        menor = i
        for j in range(i+1, long):
            if lista_ordena[menor].get_price() > lista_ordena[j].get_price():
                menor = j
        temp = lista_ordena[i]
        lista_ordena[i] = lista_ordena[menor]
        lista_ordena[menor] = temp
    return lista_ordena
    

