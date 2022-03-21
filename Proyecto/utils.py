import requests
import itertools as it
from classes import*
from Saman_arena import*


def make_request(url):
    response = requests.get(url)
    return response

def validar_numero(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Error, valor ingresado no valido')
            print('')
    return num

def validar_palabra(msg):
    while True:
        word=input(msg)
        if word.replace(" ","").isalpha():
            break
        else:
            print("Error, valor ingresado no valido")
    
    return word

def crear_bd(bd, bd_api, restablecer_bd):
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
                asientos_general = crear_matriz(fila_general, columna_general)
                asientos_vip = crear_matriz(fila_vip, columna_vip)
                price_general = evento["prices"][0]
                price_vip = evento["prices"][1]
                asiento = asientos(fila_general, columna_general, fila_vip, columna_vip, asientos_general, asientos_vip, tickets_general, tickets_vip, price_general, price_vip)
                date = evento["date"]
                if evento['type'] == 1:
                    bands = evento["bands"]
                    bd["events"][id_evento] = {"title": title, "type": tipo, "cartel": cartel, "asientos": asiento, "date": date, "bands": bands}
                else:
                    synopsis = evento["synopsis"]
                    bd["events"][id_evento] = {"title": title, "type": tipo, "cartel": cartel, "asientos": asiento, "date": date, "synopsis": synopsis}
        elif key == "food_fair_inventory":
            iva = 0.16
            for producto in value:
                if producto["type"] == 1:
                    name = producto["name"]
                    price = producto["price"]
                    aumento = price * iva
                    final_price = price + aumento
                    final_price = round(final_price, 2)
                    amount = producto["amount"]
                    presentation = producto["presentation"]
                    comida = comidas(name, amount, presentation, final_price)
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
                    bebida = bedidas(name, amount, little_amount, middle_amount, big_amount, little_price, middle_price, big_price)
                    bd["products"]["Bebidas"].append(bebida)
                    restablecer_bd["products"]["Bebidas"].append(bebida)
    return bd, restablecer_bd



def imprimir_eventos(bd, dato_1, dato_2, dato_3):
    for key, value in bd["events"].items():
        if value[dato_1] == dato_2:
            print('')
            print("-------------------------------------------------")
            print(f'''Nombre del evento: {value["title"]} ''')
            if value["type"] == 1:
                print('Tipo de evento: Musical')
                print('Para este evento estaran presentes {} bandas'.format(value["bands"]))
                print('Cantantes/Bandas que se presentaran:')
                for banda in value["cartel"]:
                    print(banda)
                print('')
                print("Asientos general:")
                print('')
                mostrar_asientos(value["asientos"].get_fila_general(), value["asientos"].get_columna_general(), value["asientos"].get_asientos_general())
                print('')
                print("Asientos vip:")
                print('')
                mostrar_asientos(value["asientos"].get_fila_vip(), value["asientos"].get_columna_vip(), value["asientos"].get_asientos_vip())
                print('')
                print(f'''Fecha del evento: {value["date"]}''')
                print("-------------------------------------------------")
                print('')
            else:
                print('Tipo de evento: Teatral')
                print(f'''Sipnosis: {value["synopsis"]} ''')
                print('Actores estelares:')
                for actor in value["cartel"]:
                    print(actor)
                print('')
                print("Asientos general:")
                print('')
                mostrar_asientos(value["asientos"].get_fila_general(), value["asientos"].get_columna_general(), value["asientos"].get_asientos_general())
                print('')                    
                print("Asientos vip:")
                print('')
                mostrar_asientos(value["asientos"].get_fila_vip(), value["asientos"].get_columna_vip(), value["asientos"].get_asientos_vip())
                print('')
                print(f'''Fecha del evento: {value["date"]}''')
                print("-------------------------------------------------")
                print('')

    if dato_3 == True:
        for key, value in bd["events"].items():
            for elemento in value[dato_1]:
                if elemento == dato_2:
                    print('')
                    print("-------------------------------------------------")
                    print(f'''Nombre del evento: {value["title"]} ''')
                    if value["type"] == 1:
                        print('Tipo de evento: Musical')
                        print('Para este evento estaran presentes {} bandas'.format(value["bands"]))
                        print('Cantantes/Bandas que se presentaran:')
                        for banda in value["cartel"]:
                            print(banda)
                        print('')
                        print("Asientos general:")
                        print('')
                        mostrar_asientos(value["asientos"].get_fila_general(), value["asientos"].get_columna_general(), value["asientos"].get_asientos_general())
                        print('')
                        print("Asientos vip:")
                        print('')
                        mostrar_asientos(value["asientos"].get_fila_vip(), value["asientos"].get_columna_vip(), value["asientos"].get_asientos_vip())
                        print('')
                        print(f'''Fecha del evento: {value["date"]}''')
                        print("-------------------------------------------------")
                        print('')
                    else:
                        print('Tipo de evento: Teatral')
                        print(f'''Sipnosis: {value["synopsis"]} ''')
                        print('Actores estelares:')
                        for actor in value["cartel"]:
                            print(actor)
                        print('')
                        print("Asientos general:")
                        print('')
                        mostrar_asientos(value["asientos"].get_fila_general(), value["asientos"].get_columna_general(), value["asientos"].get_asientos_general())
                        print('')
                        print("Asientos vip:")
                        print('')
                        mostrar_asientos(value["asientos"].get_fila_vip(), value["asientos"].get_columna_vip(), value["asientos"].get_asientos_vip())
                        print('')
                        print(f'''Fecha del evento: {value["date"]}''')
                        print("-------------------------------------------------")
                        print('')
                    return True

        return False
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