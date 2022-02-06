print('***Bienvenido***')
while True:
    numero = input('Dame un numero para verificar si es compuesto, escribe "salir" para cerrar el programa\n--> ')
    if numero.isnumeric():
        numero = int(numero)
        flag = False
        if numero == 1:
            print('1 no es un numero compuesto')
        elif numero == 2:
            print('2 es compuesto')
        else:
            for x in range(2, numero):
                if numero % x == 0:
                    flag = True
                    break
            if flag == True:
                print('Es compuesto')
            else:
                print('No es compuesto')
    elif numero.lower() == "salir":
        break
    else:
        print('Error, información introducida no valida')