Datos = {}

while True:
    print('')
    accion = input("Ingrese:\n1.Registar datos\n2.Ver datos\n3.Salir\n--> ")
    if accion.isnumeric():
        accion = int(accion)
        if 0 < accion < 4:
            if accion == 1:
                while True:
                    BMI = None
                    nombre = input('Ingrese el nombre:\--> ')
                    if nombre.isalpha() == False:
                        print('Error')
                        print('')
                        continue
                    apellido = input('Ingrese el apellido:\--> ')
                    if apellido.isalpha() == False:
                        print('Error')
                        print('')
                        continue
                    altura = input('Ingrese la altura (en centrimetros):\n--> ')
                    if altura.isnumeric() == False:
                        print('Error')
                        print('')
                        continue
                    deporte = input('Ingrese deporte favorito (Si no tiene, escriba "Ninguno"):\n --> ')
                    if deporte.isalpha() == False:
                        print('Error')
                        print('')
                        continue
                    notas = input('Ingrese promedio de notas (Redondeadas):\n--> ')
                    if notas.isnumeric() == False:
                        print('Error')
                        print('')
                        continue
                    peso = input('Ingrese el peso (en kilogramos):\n--> ')
                    if peso.isnumeric() == False:
                        print('Error')
                        print('')
                        continue
                    peso = int(peso)
                    if peso < 65:
                        BMI = 'Bajo peso'
                    elif 65 == peso < 73:
                        BMI = "Paso normal"
                    elif 73 == peso < 103:
                        BMI = "Sobrepeso"
                    elif 103 == peso < 120:
                        BMI = "Obeso"
                    else:
                        BMI = 'Obesidad extrema'
                    registro = nombre + ' ' + apellido
                    Datos[registro] = {"Nombre": nombre, "Apellido": apellido, "Altura": altura, "Deporte": deporte, "Notas": notas, "Peso": peso, "BMI": BMI}
                    print(Datos)
                    break
            elif accion == 2:
                while True:
                    print("Alumnos:")
                    print('')
                    for key, value in Datos.items():
                        print('*',key)
                        print('')
                    informacion = input('Escriba el nombre del alumno del cual queira usted ver información:\n--> ')
                    if Datos.get(informacion) == None:
                        print('')
                        print('***Error, el alumno ingresado no se encunetra en la base de datos o el nombre esta mal escrito***')
                        print('')
                        continue
                    for key2, value2 in Datos[informacion].items():
                        print('{}: {}'.format(key2, value2))
                    while True:
                        print('')
                        print('¿Desea ver la infromación de otro alumno?')
                        accion_2 = input('Ingrese:\n0.Ver la información de otro alumno\n1.Salir\n--> ')
                        if accion_2.isnumeric() == True:
                            accion_2 = int(accion_2)
                            if accion_2 == 0 or accion_2 == 1:
                                if accion_2 == 0:
                                    break
                                else:
                                    break
                            else:
                                print('Error')
                                print('')
                        else:
                            print('Error')
                            print('')
                    if accion_2 == 1:
                        break             
            else:
                break
        else:
            print('Error')
            print('')
    else:
        print('Error')
        print('')