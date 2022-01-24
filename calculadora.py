print('Bienvenido a la calculadora')
opcion = input('Que quieres hacer\n1.-Suman\n2.-Resta\n3.-Mutiplicacion\n4.-Division\n')

if 1 <= int(opcion) <= 4:
    opcion = int(opcion)
    if opcion == 1:
        print('Vamos a sumar')
        valor_1 = input('Dame un primer valor: ')
        valor_2 = input('Dame un segundo valor: ')
        if valor_1.isnumeric() == False and valor_2.isnumeric() == False:
            print('Valores ingresados nos son validos')
        else:
            print('El resultado es:', float(valor_1)+float(valor_2))
    elif opcion == 2:
        print('Vamos a restar')
        valor_1 = input('Dame un primer valor: ')
        valor_2 = input('Dame un segundo valor: ')
        if valor_1.isnumeric() == False and valor_2.isnumeric() == False:
           print('Un valor ingresado no es valido')
        else:
            print('El resultado es:', float(valor_1) - float(valor_2))
    elif opcion == 3:
        print('Vamos a multiplicar')
        valor_1 = input('Dame un primer valor: ')
        valor_2 = input('Dame un segundo valor: ')
        if valor_1.isnumeric() == False and valor_2.isnumeric() == False:
            print('Un valor ingresado no es valido')
        else:
            print('El resultado es:', float(valor_1)*float(valor_2))
    else:
        print('Vamos a dividir')
        valor_1 = input('Dame un primer valor: ')
        valor_2 = input('Dame un segundo valor: ')
        if valor_1.isnumeric() == False and valor_2.isnumeric() == False:
            print('Un valor ingresado no es valido')
        else:
            print('El resultado es:', float(valor_1) / float(valor_2))
else:
    print('Valor no valido')