bd = {}

while True:
    print('Bienvenido')
    while True:
        option = input('Ingresar:\n1.Para agregar un estuiante a la base de datos\n2.Para eliminar un estudiante de la base de datos\n3.Para mostrar los estudiantes en la base de datos\n--> ')
        if option.isnumeric() and 1 <= option < 4:
            break
        else:
            print('Valor ingresado no valido')
    if option == 1:
        while True:
            name = input('Ingresa el nombre del estuiante\n--> ')
            if name.isalpha():
                break
            else:
                print('Error. Ingrese un nombre valido')
            last_name = input('Ingresa el apellido del estuiante\n--> ')
        while True:
            if last_name.isalpha():
                break
            else:
                print('Error. Ingrese un nombre valido')
        while True:
            dni = input('Ingresa la cedula del estudiante\n --> ')
            if dni.isalpha():
                break
            else:
                print('Error. Ingrese un nombre valido')

        Asignaturas = []
        while True:
            materia = input('Ingresa el nombre de la materia\n--> ')
            if materia.isalpha()==False:
                print('Error, asignatura ingresada no valida')
                continue
            else:
                Asignaturas.append(materia)
            while True:
                op = input('Ingresa "0" para ingresar otra materia o "1" para salir\n -->')
                if op.isnumeric():
                    if int(op) == 1:
                        break
                    elif int(op) != 0:
                        print('Error, la opción introducida no es valida')
                        continue
                    else:
                        break
            if int(op)==1:
                break
        bd[dni]={"name":name, "lastname":last_name, "assigment":Asignaturas}

        