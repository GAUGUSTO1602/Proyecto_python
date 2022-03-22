def es_narcisista(numero):
    numero_como_cadena = str(numero)
    longitud_de_numero = len(numero_como_cadena)
    suma = 0
    for letra in numero_como_cadena:
        # Convertir carácter a entero
        cifra_actual = int(letra)

        # Elevar ese carácter a la potencia dada por la longitud del número
        elevado = pow(cifra_actual, longitud_de_numero)

        # El resultado lo añadimos a suma
        suma = suma + elevado
    # Comprobar si la suma al elevar es igual al número que recibimos
    if numero == suma:
        return True
    else:
        return False

num = es_narcisista(32858465)

if num == True:
    print('ok')
elif num == False:
    print('makey')