print('Welcome')
while True:
    num = input('Give me a number:\n--> ')
    if num.isnumeric() == True:
        suma = 0
        num = int(num)
        for x in range(1,num):
            if num % x == 0:
                suma = suma + x
        if num == suma :
            print('Es un numero perfecto')
        else:
            print('No es un numero perfecto')
    else:
        print('The information entered is not valid')
    option = input('Ingrese "0" para calcular otro numero perfecto, ingrese cualquier otro numero para salir')

    while not(option.isnumeric()):
        option = input('Error, ingrese 0 para pregntar si otro numero es perfecto, ingrese 1 para salir')

    option = int(option)

    while option !=0 and option !=1:
        option = input('Error, ingrese 0 para calcular otro numero, 1 para salir')
        option = int(option)

    if option == 0:
        continue
    else:
        break