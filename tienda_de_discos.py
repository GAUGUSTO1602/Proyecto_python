vinyls = {
  "1": { "name": "Cuando Los Acéfalos Predominan",
        "author": "Rawayana",
        "release_year": "2021",
        "stock": 1000,
        "sold": 0,
        "price": 10,
      },
  "2": { "name": "Notes on a Conditional Form",
        "author": "The 1975",
        "release_year": "2020",
        "stock": 1200,
        "sold": 0,
        "price": 20,
      },
  "3": { "name": "Call Me If You Get Lost",
        "author": "Tyler, the Creator",
        "release_year": "2021",
        "stock": 900,
        "sold": 0,
        "price": 30,
      },
  "4": { "name": "El Mal Querer",
        "author": "Rosalía",
        "release_year": "2018",
        "stock": 980,
        "sold": 0,
        "price": 40,
      },
    "5": { "name": "The Dark Side of the Moon",
        "author": "Pink Floyd",
        "release_year": "1973",
        "stock": 500,
        "sold": 0,
        "price": 50,
      },
}

ventas = {}

ingresos = 0

while True:
    print('****Bienvenido****')
    print('')
    accion = input('Ingrese:\n1.Ver inventario\n2.Registrar compra\n3.Salir\n--> ')
    if accion.isnumeric():
        accion = int(accion)
        if 0 < accion < 4:
            if accion == 1:
                while True:
                    for key, value in vinyls.items():
                        print('ID:',key)
                        print(f'''Nombre: {value['name']}''')
                        print('')
                    informacion = input('Ingrese el ID del disco del cual quiera ver más información:\n--> ')
                    if informacion.isnumeric():
                        if 0 < int(informacion) < 6:
                            for key2, value2 in vinyls[informacion].items():
                                print('{}: {}'.format(key2,value2))
                        else:
                            print('Error')
                            print('')
                            continue 
                    else:
                        print('Error')
                        print('')
                        continue
                    while True:
                        print('')
                        accion_2 = input('Ingrese:\n1.Para ver información de otro disco\n2.Para salir\n--> ')
                        if accion_2.isnumeric():
                            accion_2 = int(accion_2)
                            if 0 < accion_2 < 3:
                                if accion_2 == 1:
                                    break
                                else:
                                    break
                            else:
                                print('Error')
                        else:
                            print('Error')
                    if accion_2 == 2:
                        break
            elif accion == 2:
                while True:
                    nombre = input('Ingrese su nombre:\n--> ')
                    if nombre.isalpha():
                        dni = input('Ingrese su dni:\n--> ')
                        if dni.isnumeric():
                            while True:
                                print('')
                                for key, value in vinyls.items():
                                    print('ID:',key)
                                    print(f'''Nombre: {value['name']}''')
                                    print('')
                                informacion = input('Ingrese el ID del disco que desea comprar:\n--> ')
                                if informacion.isnumeric():
                                    if 0 < int(informacion) < 6:
                                        ventas[nombre] = {"Comprador": nombre, "DNI": dni, "ID": informacion, "Disco": vinyls[informacion]["name"], "Precio": vinyls[informacion]['price']}
                                        vinyls[informacion]["sold"] += 1
                                        vinyls[informacion]["stock"] -= 1
                                        ingresos += vinyls[informacion]['price']
                                        print('Factura:')
                                        print('')
                                        for key3, value3 in ventas[nombre].items():
                                            print('{}: {}'.format(key3,value3))
                                        while True:
                                            print('')
                                            accion_3 = input('Ingrese:\n1.Para ver total de ventas\n2.Salir\n--> ')
                                            if accion_3.isnumeric():
                                                accion_3 = int(accion_3)
                                                if 0 < accion_3 < 3:
                                                    if accion_3 == 1:
                                                        aux = 0
                                                        print('Ventas relizadas:')
                                                        print('')
                                                        for key4, value4 in ventas.items():
                                                            for key5, value5 in ventas[key4].items():
                                                                print('{}: {}'.format(key5,value5))
                                                            print('')
                                                            aux += 1
                                                        print('')
                                                        print('Se realizaron',aux, 'ventas en total')
                                                        print('')
                                                        print('Se han acumulado $', ingresos, 'en ventas')
                                                        print('')
                                                        continue
                                                    else:
                                                        break   
                                                else:
                                                    print('Error')
                                            else:
                                                print('Error')
                                        if accion_3 == 2:
                                            break
                                    else:
                                        print('Error')
                                        print('')
                                else:
                                    print('Error')
                                    print('')
                        else:
                            print('Error')
                            print('')
                    else:
                        print('Error')
                        print('')
                    if accion_3 == 2:
                        break
            else:
                print('Adios')
                break
        else:
            print('Error') 
    else:
        print('Error')