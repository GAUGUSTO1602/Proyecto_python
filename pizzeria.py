print('Bienvenido')
orden = input('¿Que tipo de pizza quieres?\n1.-Vegetariana\n2.-No vegetariana\n-->') 
if orden.isnumeric() == True:
    if 1<= int(orden) <=2:
        orden =int(orden)
        if orden == 1:
            print('Pizza vegetariana')
            ingrediente = input('¿Con que quieres tu pizza\n1.-Pimiento\n2.-Tofu\n-->')
            if ingrediente.isnumeric() == True:
                ingrediente = int(ingrediente)
                if 1<= ingrediente <= 2:
                    if ingrediente == 1:
                        print('Pizza vegetariana con: \n*Mozzarella\n*Tomate\n*Pimiento')
                    else:
                        print('Pizza vegetariana con: \n*Mozzarella\n*Tomate\n*Tofu') 
                else:
                    print('El vaor no es valido')
            else:
                print('El vaor no es valido')   
        else :
            print('Pizza no vegetariana')
            ingrediente = input('¿Con que quieres tu pizza\n1.-Peperoni\n2.-Jamón\n3.-Salmón\n-->')
            if ingrediente.isnumeric() == True:
                ingrediente = int(ingrediente)
                if 1<= ingrediente <= 3:
                    if ingrediente == 1:
                        print('Pizza vegetariana con: \n*Mozzarella\n*Tomate\n*Peperoni')
                    elif ingrediente ==2:
                        print('Pizza vegetariana con: \n*Mozzarella\n*Tomate\n*Jamón')
                    else:
                        print('Pizza vegetariana con: \n*Mozzarella\n*Tomate\n*Salmón')
                else:
                    print('El vaor no es valido') 
            else:
                print('El vaor no es valido')
    else:
        print('El vaor no es valido')
else:
     print('El vaor no es valido')