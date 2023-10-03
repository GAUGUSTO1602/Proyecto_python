import requests
import itertools as it
from Saman_arena import*
from Eventos import Evento, Musical, Teatral
from Productos import Productos, Comidas, Bedidas
import pickle
import os


def recibir_datos_del_txt(nombre_txt,datos): #Funcion para recibir los datos del archivo TXT
    
    lectura_binaria= open(nombre_txt,'rb')
    
    if os.stat(nombre_txt).st_size != 0:
        datos=pickle.load(lectura_binaria)

    lectura_binaria.close()

    return datos



def cargar_datos_en_txt(nombre_txt,datos): #Función para GUARDAR los datos en el archivo TXT

    escritura_binaria=open(nombre_txt,'wb')

    datos=pickle.dump(datos,escritura_binaria)
    
    escritura_binaria.close()


def make_request(url): #Función para llamar al API
    response = requests.get(url)
    return response

def validar_numero(msg): #Validar inputs numeros
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Error, valor ingresado no valido')
            print('')
    return num

def validar_palabra(msg): #Validar inputs palabras
    while True:
        word=input(msg)
        if word.replace(" ","").isalpha():
            break
        else:
            print("Error, valor ingresado no valido")
    
    return word

def crear_bd(bd, bd_api, restablecer_bd): #Funcion que crea la base de datos local
    id_evento = 0
    for key, value in bd_api.items():
        if key == "events":
            for evento in value:
                id_evento += 1
                title = evento["title"]
                tipo = evento["type"]
                cartel = evento["cartel"]
                fila_general = evento["layout"]["general"][0]
                columna_general = evento["layout"]["general"][1]
                tickets_general = fila_general * columna_general
                fila_vip = evento["layout"]["vip"][0]
                columna_vip = evento["layout"]["vip"][1]
                tickets_vip = fila_vip * columna_vip
                asientos_general = crear_matriz(fila_general, columna_general) #Se crea la matriz de los asientos generales
                asientos_vip = crear_matriz(fila_vip, columna_vip) #Se crea la matriz de los asientos vip 
                price_general = evento["prices"][0]
                price_vip = evento["prices"][1]
                asiento = asientos(fila_general, columna_general, fila_vip, columna_vip, asientos_general, asientos_vip, tickets_general, tickets_vip, price_general, price_vip) #Se crea el objeto asiento para el evento
                date = evento["date"]
                ingresos = 0
                apertura = True
                if evento['type'] == 1:
                    bands = evento["bands"]
                    musical = Musical(title, tipo, cartel, asiento, date, ingresos, apertura, bands) #Se crea el objeto evento de tipo Musical
                    bd["events"][id_evento] = musical
                else:
                    synopsis = evento["synopsis"]
                    teatral = Teatral(title, tipo, cartel, asiento, date, ingresos, apertura, synopsis) #Se crea el objeto evento de tipo Teatral
                    bd["events"][id_evento] = teatral
        elif key == "food_fair_inventory":
            iva = 0.16
            bd["products"]["Comidas"] = [] #Reseteo de la lista de productos para cuando se deseee reestablcer la base de datos en su totalidad
            bd["products"]["Bebidas"] = []
            for producto in value:
                if producto["type"] == 1:
                    name = producto["name"]
                    price = producto["price"]
                    aumento = price * iva
                    final_price = price + aumento
                    final_price = round(final_price, 2)
                    amount = producto["amount"]
                    presentation = producto["presentation"]
                    amount_sell = 0
                    comida = Comidas(name, amount, presentation, final_price, amount_sell)
                    bd["products"]["Comidas"].append(comida)
                    restablecer_bd["products"]["Comidas"].append(comida)
                else:
                    name = producto["name"]
                    prices = producto["price"]
                    final_price = []
                    for price in prices:
                        aumento = price * iva
                        new_price = price + aumento
                        new_price = round(new_price, 2)
                        final_price.append(new_price)
                    little_price = final_price[0]
                    middle_price = final_price[1]
                    big_price = final_price[2]
                    amount = producto["amount"]
                    divider_amount = amount // 3
                    little_amount = divider_amount
                    middle_amount = divider_amount
                    big_amount = divider_amount
                    amount_sell = 0
                    bebida = Bedidas(name, amount, little_amount, middle_amount, big_amount, little_price, middle_price, big_price, amount_sell)
                    bd["products"]["Bebidas"].append(bebida)
                    restablecer_bd["products"]["Bebidas"].append(bebida)
    bd["clients"] = {} #Reseteo del diccionario clientes para cuando se desee reestablecer la base de datos en su totalidad
    return bd, restablecer_bd



def es_narcisista(numero): #Codigo tomado de: https://parzibyte.me/blog/2018/10/02/numero-narcisista-python/
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

def get_vampire(num): #Codido tomado de: https://www.geeksforgeeks.org/vampire-number/

    def getFangs(num_str):
   
        num_iter = it.permutations(num_str, len(num_str))
    
        for num_list in num_iter:
            
            v = ''.join(num_list)
            x, y = v[:int(len(v)/2)], v[int(len(v)/2):]
    
            if x[-1] == '0' and y[-1] == '0':
                continue
    
        
            if int(x) * int(y) == int(num_str):
                return x,y
        return False
    
  
    n_str = str(num)
    
    
    if len(n_str) % 2 == 1:
        return False
    

    fangs = getFangs(n_str)
    if not fangs:
        return False
    return True
