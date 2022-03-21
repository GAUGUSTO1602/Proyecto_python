import requests
from utils import*
import jsons

new_bd = {

    "clients": {},
    "events": {},
    "products":{}
}

bd =	{
		"events": [{
				"title": "Saman Fest",
				"type": 1,
				"bands": 4,
				"cartel": [
					"Los Cocineros",
					"Ramayana",
					"CacetVersus",
					"La vida Hippie"
				],
				"layout": {
					"general": [
						4,
						10
					],
					"vip": [
						1,
						10
					]
				},
				"prices": [50, 100],
				"date": "2022-04-01"
			},
			{
				"title": "KenaAna & Guako",
				"type": 1,
				"bands": 2,
				"cartel": [
					"Guako",
					"kenaAna"
				],
				"layout": {
					"general": [
						4,
						10
					],
					"vip": [
						1,
						6
					]
				},
				"prices": [30, 50],
				"date": "2022-04-01"
			},
			{
				"title": "El famtasma del paraninfo",
				"synopsis": "En esencia, la trama de El Fantasma del Paraninfo es una historia que combina romance, música, terror, misterio y tragedia. Trata de Eric, un hombre misterioso, un genio musical, que se enamora perdidamente de Cristina, una joven y talentosa artista, a quien inspira musicalmente",
				"type": 2,
				"cartel": [
					"Leonardo DeCapo",
					"Cendella",
					"Ed Ramiro"
				],
				"layout": {
					"general": [
						5,
						10
					],
					"vip": [
						4,
						3
					]
				},
				"prices": [5, 10],
				"date": "2022-05-10"
			},
			{
				"title": "Romeo & Julieta",
				"synopsis": "En Verona, dos jóvenes enamorados, de dos familias enemigas, son víctimas de una situación de odio y violencia que ni desean ni pueden remediar. En una de esas tardes de verano en que el calor «inflama la sangre», Romeo, recién casado en secreto con su amada Julieta, mata al primo de ésta",
				"type": 2,
				"cartel": [
					"Romeo Gonzalez",
					"Julieta Hernandez"
				],
				"layout": {
					"general": [
						1,
						5
					],
					"vip": [
						1,
						5
					]
				},
				"prices": [10, 25],
				"date": "2022-12-31"
			}
		],
		"food_fair_inventory": [{
				"name": "Coca Cola",
				"price": [1.99,2.99,3.99],
				"amount": 500,
				"type": 2
			},
			{
				"name": "Pizza",
				"price": 11.99,
				"amount": 230,
				"presentation": 1,
				"type": 1
			},
			{
				"name": "Hamburguesa",
				"price": 25.99,
				"amount": 250,
				"presentation": 1,
				"type": 1
			},
			{
				"name": "Jugo",
				"price": [9.99,10.99,11.99],
				"amount": 250,
				"type": 2
			},
			{
				"name": "Cerveza",
				"price": [5.99,6.99,7.99],
				"amount": 300,
				"type": 2
			},
			{
				"name": "Doritos",
				"price": 4.99,
				"amount": 500,
				"presentation": 2,
				"type": 1
			},
			{
				"name": "Platanitos",
				"price": 3.99,
				"amount": 734,
				"presentation": 2,
				"type": 1
			}
		]
	}


def crear_bd(new_bd, bd):
    for key, value in bd.items():
        if key == "events":
            for evento in value:
                title = evento["title"]
                tipo = evento["type"]
                cartel = evento["cartel"]
                layout = evento["layout"]
                price = evento["prices"]
                date = evento["date"]
                if evento['type'] == 1:
                    bands = evento["bands"]
                    new_bd["events"][title] = {"type": tipo, "cartel": cartel, "layout": layout, "prices": price, "date": date, "bands": bands}
                else:
                    sypnosis = evento["synopsis"]
                    new_bd["events"][title] = {"type": tipo, "cartel": cartel, "layout": layout, "prices": price, "date": date, "sypnosis": sypnosis}
    return new_bd

def evento_funciones(new_bd,msg):
    while True:
        opt = validar_numero(msg)
        if opt == 1:
            print('')
            for evento in lista_eventos:
                print(f'''Nombre del evento: {evento["title"]} ''')
                if evento["type"] == 1:
                    print('Tipo de evento: Musical')
                    print('Para este evento estaran presentes {} bandas'.format(evento["bands"]))
                    print('Cantantes/Bandas que se presentaran:')
                    for banda in evento["cartel"]:
                        print(banda)
                else:
                    print('Tipo de evento: Teatral')
                    print(f'''Sipnosis: {evento["synopsis"]} ''')
                    print('Actores estelares:')
                    for actor in evento["cartel"]:
                        print(actor)
                #Recordar colocar asientos
                print(f'''Fecha del evento: {evento["date"]}''')
                print('')
        elif opt == 2:
            pass
        elif opt == 3:
            while True:
                print('')
                opt_2 = validar_numero('Ingrese para buscar por:\n1.Tipo\n2.Fecha\n3.Actor, cantante o banda en el cartel\n4.Nombre del evento\n5.Salir\n--> ')
                if opt_2 == 1:
                    while True:
                        opt_3 = validar_numero('Ingrese:\n1.Musical\n2.Teatral\n3.Salir\n--> ')
                        if 1 <= opt_3 <= 2:
                            for evento in lista_eventos:
                                if evento["type"] == opt_3:
                                    print(f'''Nombre del evento: {evento["title"]} ''')
                                    if opt_3 == 1:
                                        print('Tipo de evento: Musical')
                                        print('Para este evento estaran presentes {} bandas'.format(evento["bands"]))
                                        print('Cantantes/Bandas que se presentaran:')
                                        for banda in evento["cartel"]:
                                            print(banda)
                                    else:
                                        print('Tipo de evento: Teatral')
                                        print(f'''Sipnosis: {evento["synopsis"]} ''')
                                        print('Actores estelares:')
                                        for actor in evento["cartel"]:
                                            print(actor)
                                    #recordar colocar asientos
                                    print(f'''Fecha del evento: {evento["date"]}''')
                                    print('')
                        elif opt_3 == 3:
                            break
                        else:
                            print('Error, valor ingresado no valido')
                elif opt_2 == 2:
                    while True:
                        print('')
                        validacion = False
                        año = input('Ingrese el año:--> ')
                        mes = input('Ingrese el mes:--> ')
                        dia = input('Ingrese el dia:--> ')
                        fecha = "{}-{}-{}".format(año,mes,dia)
                        for evento in lista_eventos:
                            if evento["date"] == fecha:
                                validacion = True
                                print('')
                                print(f'''Nombre del evento: {evento["title"]} ''')
                                if evento["type"] == 1:
                                    print('Tipo de evento: Musical')
                                    print('Para este evento estaran presentes {} bandas'.format(evento["bands"]))
                                    print('Cantantes/Bandas que se presentaran:')
                                    for banda in evento["cartel"]:
                                        print(banda)
                                    # Recordar colocar asientos
                                    print(f'''Fecha del evento: {evento["date"]}''')
                                    print('')
                                else:
                                    print('Tipo de evento: Teatral')
                                    print(f'''Sipnosis: {evento["synopsis"]} ''')
                                    print('Actores estelares:')
                                    for actor in evento["cartel"]:
                                        print(actor)
                                    #Recordar colocar asientos
                                    print(f'''Fecha del evento: {evento["date"]}''')
                                    print('')
                        if validacion == False:
                            print('')
                            print('No se encuentran eventos o la fecha introducida es incorrecta')
                            print('') 
                        while True:
                            salida = validar_numero('¿Quiere ingresar otra fecha?:\n1.Si\n2.No\n--> ')
                            if 1 <= salida <= 2:
                                break
                            else:
                                print('Error, valor introducido no valido')
                                print('')
                        if salida == 2:
                            break
                elif opt_2 ==3:
                    while True:
                        print('')
                        validacion = False
                        nombre = input('Ingrese el nombre del cantante, banda o actor:\n(Cuide el uso de los espacios y de las mayusculas)\n--> ')
                        for evento in lista_eventos:
                            for artista in evento["cartel"]:
                                if artista == nombre:
                                    validacion = True
                                    print('')
                                    print(f'''Nombre del evento: {evento["title"]} ''')
                                    if evento["type"] == 1:
                                        print('Tipo de evento: Musical')
                                        print('Para este evento estaran presentes {} bandas'.format(evento["bands"]))
                                        print('Cantantes/Bandas que se presentaran:')
                                        for banda in evento["cartel"]:
                                            print(banda)
                                        # Recordar colocar asientos
                                        print(f'''Fecha del evento: {evento["date"]}''')
                                        print('')
                                    else:
                                        print('Tipo de evento: Teatral')
                                        print(f'''Sipnosis: {evento["synopsis"]} ''')
                                        print('Actores estelares:')
                                        for actor in evento["cartel"]:
                                            print(actor)
                                        #Recordar colocar asientos
                                        print(f'''Fecha del evento: {evento["date"]}''')
                                        print('')
                        if validacion == False:
                            print('')
                            print('El nombre introducido no se encuentra en nuestra base de datos o es incorrecto')
                            print('') 
                        while True:
                            salida = validar_numero('¿Quiere ingresar otro nombre?:\n1.Si\n2.No\n--> ')
                            if 1 <= salida <= 2:
                                break
                            else:
                                print('Error, valor introducido no valido')
                                print('')
                        if salida == 2:
                            break       
                elif opt_2 == 4:
                    while True:
                        print('')
                        validacion = False
                        titulo = input('Ingrese el nombre del evento\n(Cuide le uso de espacios y mayusculas)\n--> ')
                        for evento in lista_eventos:
                            if evento["title"] == titulo:
                                validacion = True
                                print('')
                                print(f'''Nombre del evento: {evento["title"]} ''')
                                if evento["type"] == 1:
                                    print('Tipo de evento: Musical')
                                    print('Para este evento estaran presentes {} bandas'.format(evento["bands"]))
                                    print('Cantantes/Bandas que se presentaran:')
                                    for banda in evento["cartel"]:
                                        print(banda)
                                    # Recordar colocar asientos
                                    print(f'''Fecha del evento: {evento["date"]}''')
                                    print('')
                                else:
                                    print('Tipo de evento: Teatral')
                                    print(f'''Sipnosis: {evento["synopsis"]} ''')
                                    print('Actores estelares:')
                                    for actor in evento["cartel"]:
                                        print(actor)
                                    #Recordar colocar asientos
                                    print(f'''Fecha del evento: {evento["date"]}''')
                                    print('')
                        if validacion == False:
                            print('')
                            print('No se encuentran eventos o el nombre introducido es incorrecto')
                            print('') 
                        while True:
                            salida = validar_numero('¿Quiere ingresar otra nombre?:\n1.Si\n2.No\n--> ')
                            if 1 <= salida <= 2:
                                break
                            else:
                                print('Error, valor introducido no valido')
                                print('')
                        if salida == 2:
                            break
                elif opt_2 == 5:
                    break
                else:
                    print('Error, valor introducido no valido')
                                          

url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json"


new_bd = crear_bd(new_bd, bd)
evento_funciones(new_bd, msg='Ingrese:\n1.Ver eventos disponibles\n2.Cerrar/Abrir la venta de tickets\n3.Buscar evento\n4.Salir\n--> ')
