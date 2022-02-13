bd = {}

students = {"28331741": {
        "name": "Gabriel",
        "lastname": "González",
        "Asignaturas": ["Matemática"]
    } }

while True:
    print('Bienvenido\n')
    while True:
        option = input('Ingresar:\n1.Para agregar un estuiante a la base de datos\n2.Para eliminar un estudiante de la base de datos\n3.Para mostrar los estudiantes en la base de datos\n4. Editar los datos de un estudiante\n5.Para salir\n--> ')
        if option.isnumeric() and 1 <= int(option) < 5:
            option = int(option)         
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
                bd[dni]={"name":name, "lastname":last_name, "assigment":Asignaturas}
                break
    elif option == 2:
        for key, value in students.items():
            print(f'''\nCedula {key}\nNombre {value["name"]}\nApellido {"lastname"}''')
            print("Materias")
            for materia in value["Asignaturas"]:
                print(materia)
            print("")
            dni = input("Ingrese la cedula del estudiante que desea eliminar\n--> ")
            students.pop(dni)
    elif option == 3:
        for key, value in students.items():
            print(f'''\nCedula {key}\nNombre {value["name"]}\nApellido {"lastname"}''')
            print("")
            print("Materias")
            for materia in value["Asignaturas"]:
                print(materia)
            print("")
    elif option == 4:
        for key, value in students.items():
            print(f'''\nCedula {key}\nNombre {value["name"]}\nApellido {"lastname"}''')
            print("Materias")
            for materia in value["Asignaturas"]:
                print(materia)
            dni = input("Ingrese la cedula del estudiante que desea editar\n--> ")
            opt = input('Ingresar:\n1.Para cambiar el nombre de un estuiante a la base de datos\n2.Para cambiar el appellido de un estudiante de la base de datos\n3.Para cambiar la cedula de un estudiante en la base de datos\n4. Para cambiar las asignaturas de un estudiante\n5.Para salir--> ')

            while True:
                if opt.isnumeric():
                    opt = int(opt)
                    if opt < 1 or opt > 4:
                        if opt == 1:
                            name = input("Ingrese el nombre\n")
                            students[dni]["name"]= name
                        elif opt == 2:
                            lastname = input("Ingrese el napellido\n")
                            students[dni]["lastname"]= lastname
                        elif opt == 3:
                            lastname = input("Ingrese la cedula\n")
                            student = students[dni]
                            students[dni2] = student
                            students.pop(dni)
                        elif opt == 4:
                            for index in range(len(students[dni]["Asignaturas"])):
                                print(index + 1, students[dni]["Asignaturas"][index])
                                m = input("Eliminar materia\n")
                                students[dni]["Asignaturas"].pop(m-1)
                                materia = input("Materia a agregar\n")
                                students.insert(m-1, materia)
                    else:
                        print("Error")
                    
                else:
                    print('Error')
    else:
        print('Adios')

        