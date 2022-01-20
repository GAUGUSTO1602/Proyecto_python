


'''
2.7
CÁLCULO DE ÁREAS
Se requiere un sistema para calcular el área de figuras geométricas sencillas, 
donde el usuario ingresará en qué figura está interesado.
 El sistema debe permitir la solicitud de circunferencias, elipses, cuadrados, rectángulos, triángulos y rombos; 
 solicitando para cada uno la información necesaria. Si existe información que sea constante, deben manejarla como tal.

'''




# import math


# print("***WELCOME***")
# print("This program will provide you a tool to calculate a figure's area")
# option = input(
#     "Enter:\n1.-Triangle.\n2.-Square.\n3.-Circle.\n")

# if option.isnumeric():
#     option=int(option)

#     if option>=1 and option<=3:

#         if  option==1:
#             print("Calculate the triangle's area:\n")

#             base=input("Enter the base:\n===> ")
#             height=input("Enter the height:\n===> ")

#             print(f"The triangle's area is:{(int(base)*int(height)) /2}")

#         elif option==2:
#             print("Calculate the square's area:\n")
#             side = input("Enter the side:\n===> ")
#             print(f"The squared's area is:{int(side)**2}")
			
#         elif option==3:
#             print("Calculate the circle's area:\n")
#             radio = input("Enter the radio:\n===> ")
#             print(f"The circle's area is:{((int(radio)**2)*math.pi)}")

#     else:
#         print("The opcion entered is wrong")
# else:
#     print("Character entered as option is wrong.")





'''
2.11
PARIDAD
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
impar.
'''

# print("***WELCOME***")
# print("This program will help you to know if a number is pair or odd... So:\n")
# number= input("Please, introduce a number:\n===>")


# if number.isnumeric():
    
#     if int(number)%2==0:
#         print("The number is par")
#     else:
#         print("The number is impar")

# else:
#     print("What you introduced is not valid")






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

# print("***WELCOME***")
# print("This software will help you to calculate the ticket's price taking into account the people's age.")


# name = input("Enter the name:\n===>")

# if (name.isalpha()):

#     years_old = input("Enter How old he/she is:\n===>")

#     if not (years_old.isnumeric()):
#         print(f"The {name}'s age is not correct.")

#     else:
#         years_old = int(years_old)
#         if years_old == 21:
#             print(f"There is a promotion for you so, {name} must pay $50.")
#         elif years_old >= 18 and years_old < 22:
#             print(f"{name} must pay $60")
#         elif years_old >= 22:
#             print(f"{name} must pay 70$")
#         else:
#             print("You are not old enough  to enter.")
# else:
# 	print("The client's name is not valid.")



#TAREAS DE REDACCION

'''
2.2
PALÍNDROMOS
Una palabra o número palíndromo son aquellos que se leen igual de izquierda a derecha. Por ejemplo: 101 es un número palíndromo, y 236 no lo es. Ana es una palabra palíndroma y pan no lo es.
Diseña un programa que determine si un número o palabra ingresados por teclado, son palíndromos o no.
'''


'''
2.8
FECHA (1)
Elabore un programa que se encargue de solicitar 3 números que serán el día, mes y año de una fecha. 
El programa debe indicar si la fecha es correcta y leerla por consola. 
El programa debe cumplir las siguientes características:
Manejar meses de 28, 30 y 31 días.
No trabajar con años bisiestos.
Por ejemplo, al ingresar día: 45, mes: 1, año: 2018, 
el programa debe enviar una alerta de que la fecha no es correcta. 
Por el contrario, si el programa recibe datos adecuados, debe indicar que la fecha es correcta e imprimirla (e.g., 25 de enero de 2018).
'''



# print("***WELCOME***")

# print("This program will provide a way to know a specific date:\n")

# day=input("Enter the Day:\n===> ")
# month=input("Enter the Mounth:\n===> ")
# year=input("Enter the Year:\n===> ")

# if not(day.isnumeric() and month.isnumeric() and year.isnumeric()):
#     print("The Character entered is not valid.\n")


# elif (int(day)<=0 or int(day)>31) or (int(month)<=0 or int(month)>12) or int(year)<=0:

#     print("The date entered is not valid.\n")


# else:
#     day= int(day)
#     if not (month=="2" and day>29):

#         if month=="1":
#             month="January"

#         elif month=="2":
#             month="February"

#         elif month=="3":
#             month="March"

#         elif month=="4":
#             month="April"

#         elif month=="5":
#             month="May"

#         elif month=="6":
#             month="June"

#         elif month=="7":
#             month="July"

#         elif month=="8":
#             month="August"

#         elif month=="9":
#             month="September"

#         elif month=="10":
#             month="October"

#         elif month=="11":
#             month="November"

#         elif month=="12":
#             month="December"
        
#         print(f"The date is: {month} {day}, {year}")

#     else:
#         print("This day is not valid")





