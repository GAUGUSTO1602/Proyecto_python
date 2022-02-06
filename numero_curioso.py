def main():

    while True:
        print('Bienvenido')
        numero = input('Dame un numero para verificar que sea un numero curioso \n --> ')
        if numero.isnumeric():
            numero = int(numero)
            curioso = numero**2
            numero = str(numero)
            curioso = str(curioso)
            if numero[-1] == curioso[-1]:
                print(numero,'es un numero curioso')
            else:
                print(numero,'no es numero curioso curioso')
        else:
            print('Valor introducio no valido')

main()
