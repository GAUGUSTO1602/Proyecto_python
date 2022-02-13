#Contraseña valida: Carbono09.

print("***Bienvenido***")

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0

contraseña = input("Por favor, ingrese una nueva contraseña\n--> ")
if len(contraseña) >= 8:
    for caracter in contraseña:
        if " " in caracter:
            count_6 += 1
        elif caracter.isalpha():
            count_1 += 1
            if caracter.islower():
                count_4 += 1
            elif caracter.isupper():
                count_5 += 1
        elif caracter.isnumeric():
            count_2 += 1
        elif caracter.isalnum() == False:
            count_3 += 1
    if count_1 >= 1 and count_2 >= 1 and count_3 >= 1 and count_4 >= 1 and count_5 >= 1 and count_6 == 0:
        print("Contraseña ingresada correctamente")
    else:
        print("La contraseña elegida no es válida")   
else:
    print("Contaseña no valida. Necesita al menos 8 caracteres ")
    print("")