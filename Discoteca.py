
'''
2.12
Discoteca
Un discoteca requiere un programa para calcular el precio de sus entradas y te ha contratado para realizarlo. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 18 años no puede entrar 
Si tiene entre 18 y menor que 21 años debe pagar $60
Si es mayor de 22 años, $70
Si tiene 21 anios exacto, se le da un precio de $50.
Como output se espera:
	Imprimir el precio correspondiente a la edad del cliente. '''

print('Welcome')
edad = input('please, give me your age: ')

if edad.isnumeric()==True:
    edad= int(edad)
    if edad < 18:
        print('Sorry, you need to be of legal age to enter')
    elif 18 <= edad < 21:
        print('Entrance fee: $60')
    elif edad > 22:
        print('Entrance fee: $70')
    elif edad >= 21:
        print('Entrace fee: $50')
else:
    print('The caracter entered is not valid')
