


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
print("***Welcome***")
print("This program will provide you a tool to calculate a figure's area")
option=input("Enter:\n1.-Triangle.\n2.-Square.\n3.-Circle.\n4.-Rectangle\n5.-Ellipse\n6.-Rhombus")

if option.isnumeric()==True:
	if int(option)>=1 and int(option)<=6:
		if int(option)==1:
			print("Calculate the triangle's area:\n")
			base=input("Enter the base:\n==>")
			height=input("Enter the height:\n==>")
			if base.isnumeric()== False and height.isnumeric()== False: 
				print("The information entered is not valid")
			else:
				print("The triangule area is:", float(base)*float(height))
		elif int(option)==2:
			print("Calculate the square's area:\n")
			side=input("Enter a square side:\n==>")
			if side.isnumeric():
				print("The square area is:", float(side**2))
			else:
				print("The informatio is not valid")
		elif int(option) ==3:
			print("Calculate the circle's area:\n")
			radio=input("Enter the circle's radio:\n==>")
			if radio.isnumeric():
				print("The circle's area is", float(radio**2)*3,14)
			else:
				print("The information entered is not valid")
		elif int(option) ==4:
			print("Calculate the rectangle's area:\n")
			base_rectangle=input("Enter the rectangle's base:\n==>")
			height_rectangle=input("Enter the rectangle's height:\n==>")
			if base_rectangle.isnumeric() == False and height_rectangle.isnumeric() == False:
				print("The information entered is not valid")
			else:
				print("The rectangle's area is", float(base_rectangle)*float(height_rectangle))
		elif int(option) ==5:
			print("Calculate the ellipse's area:\n")
			ellipse_radio_1=input("Enter the ellipse's radio 1:\n==>")
			ellipse_radio_2=input("Enter the ellipse's radio 2:\n==>")
			if ellipse_radio_1.isnumeric() == False and ellipse_radio_2.isnumeric() == False:
				print("The information entered is not valid")
			else:
				print("The ellipse's area is", 3.14*float(ellipse_radio_1)*float(ellipse_radio_2))
		else:
			print("Calculate the rhombus's area:\n")
			mayor_diagonal=input("Enter the rhombus's mayor diagonal:\n==>")
			minor_diagonal=input("Enter the rhombus's minor diagonal:\n==>")
			if mayor_diagonal.isnumeric() == False and minor_diagonal == False :
				print("The information entered is not valid")
			else:
				print("The ellipse's area is", (float.mayor_diagonal*float.minor_diagonal)/2)
else:
	print("The caracter entered is not valid")
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





