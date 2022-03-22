from unicodedata import name
from utils import*
from Gestion_eventos import*
from Gestion_feria import*
from venta_tickets import*
from venta_feria import*
import jsons


def main():
    while True:
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json"
        response = make_request(url)
        if response.status_code != 200:
            print('Lo sentimos, el servidor se encuentra caido')
            break
        else:

            bd_api = response.json()

            bd = {

                "clients": {},
                "events": {},
                "products":{

                    "Comidas":[],
                    "Bebidas":[]
                }
            }

            restablecer_bd = {

                "products":{

                    "Comidas":[],
                    "Bebidas":[]
                }
            }

            bd, restablecer_bd = crear_bd(bd, bd_api, restablecer_bd)

            print('***BIENVENIDO AL SISTEMA DEL SAMAN SHOW***\n')
            apertura_tickets = True
            while True:
                while True:
                    opt = validar_numero('Ingrese para acceder:\n1.Gestion de eventos\n2.Venta de tickets\n3.Gestion Feria de comida\n4.Venta de feria de comida\n5.Estadisticas\n6.salir\n--> ')
                    if 1 <= opt <= 6:
                        break
                    else:
                        print('Error, valor ingresado no valido')
                        print('')
                if opt == 1:
                    print('')
                    bd, apertura_tickets = evento_funciones(bd, msg='Ingrese:\n1.Ver eventos disponibles\n2.Cerrar/Abrir la venta de tickets\n3.Buscar evento\n4.Salir\n--> ', apertura_tickets= apertura_tickets)
                elif opt == 2:
                    print('')
                    if apertura_tickets != False:
                        bd = venta_tickets(bd, msg='Ingrese:\n1.Registrar una compra\n2.Salir\n--> ')
                    else:
                        print('')
                        print('Lo sentimos, la tienda de tickets se encuentra cerrada en este momento')
                        print('')
                elif opt == 3:
                    print('')
                    bd = feria_funciones(bd, restablecer_bd, msg= 'Ingrese:\n1.Ver prodcutos en el inventario\n2.Eliminar productos\n3.Buscar Producto\n4.Restablecer inventario y menu\n5.Salir\n--> ')
                elif opt == 4:
                    print('')
                    bd = venta_feria(bd, msg="***BIENVENIDO A LA FERIA***\n\nIngrese:\n1.Comprar productos\n2.Salir\n--> ")
                else:
                    print('')
                    print('***ADIOS***')
                    break







main()

