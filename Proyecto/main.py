from unicodedata import name
from utils import*
from Gestion_eventos import*
from Gestion_feria import*
from venta_tickets import*
from venta_feria import*
from estadisticas import*
import jsons


def main():
    while True:
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json"
        response = make_request(url) #Llamada al API
        if response.status_code != 200: #Verificar si el API no esta caido
            print('Lo sentimos, el servidor se encuentra caido')
            break
        else:

            bd_api = response.json() #Se gurdan los datos devueltos por el APi

            bd = { #Base de datos local

                "clients": {},
                "events": {},
                "products":{

                    "Comidas":[],
                    "Bebidas":[]
                }
            }

            restablecer_bd = { #Base de datos de respaldo, para resetear ciertos atributos

                "products":{

                    "Comidas":[],
                    "Bebidas":[]
                }
            }

            bd, restablecer_bd = crear_bd(bd, bd_api, restablecer_bd) #Llamada a la función que crea la base de datos local

            bd = recibir_datos_del_txt("C:\\Users\\veronica\\Desktop\\Proyecto\\bd.txt", bd) #Actualiza la información de la base de datos llamando al archivo TXT


            #Menu de opciones
            print('-----------------------------------------------------------------')
            print('')
            print('           ***BIENVENIDO AL SISTEMA DEL SAMAN SHOW***   ')
            print('')
            while True:
                while True:
                    print('-----------------------------------------------------------------')
                    print('')
                    opt = validar_numero('Ingrese para acceder:\n1.Gestion de eventos\n2.Venta de tickets\n3.Gestion Feria de comida\n4.Venta de feria de comida\n5.Estadisticas\n6.Reestablecer toda la base de datos local\n7.Salir\n--> ')
                    if 1 <= opt <= 7:
                        break
                    else:
                        print('Error, valor ingresado no valido')
                        print('')
                if opt == 1:
                    print('')
                    bd = evento_funciones(bd, msg='Ingrese:\n1.Ver eventos disponibles\n2.Cerrar/Abrir la venta de tickets de un evento\n3.Buscar evento\n4.Reestablecer asientos y tickets\n5.Salir\n--> ')
                    cargar_datos_en_txt("C:\\Users\\veronica\\Desktop\\Proyecto\\bd.txt", bd)
                elif opt == 2:
                    print('')
                    bd = venta_tickets(bd, msg='Ingrese:\n1.Registrar una compra\n2.Salir\n--> ')
                    cargar_datos_en_txt("C:\\Users\\veronica\\Desktop\\Proyecto\\bd.txt", bd)
                    print('')
                elif opt == 3:
                    print('')
                    bd = feria_funciones(bd, restablecer_bd, msg= 'Ingrese:\n1.Ver prodcutos en el inventario\n2.Eliminar productos\n3.Buscar Producto\n4.Restablecer inventario y menu\n5.Salir\n--> ')
                    cargar_datos_en_txt("C:\\Users\\veronica\\Desktop\\Proyecto\\bd.txt", bd)
                elif opt == 4:
                    print('')
                    bd = venta_feria(bd, msg="***BIENVENIDO A LA FERIA***\n\nIngrese:\n1.Comprar productos\n2.Salir\n--> ")
                    cargar_datos_en_txt("C:\\Users\\veronica\\Desktop\\Proyecto\\bd.txt", bd)
                elif opt == 5:
                    print('')
                    bd = Estadisticas(bd, msg="Ingrese:\n1.Promedio de gastos de los clientes\n2.Promedio de clientes que no compran en la feria\n3.Top 3 eventos con más ingresos\n4.Clientes de mayor fidelidad\n5.Top 5 productos más vendidos en la feria\n6.Salir\n--> ")
                    cargar_datos_en_txt("C:\\Users\\veronica\\Desktop\\Proyecto\\bd.txt", bd)
                elif opt == 6:
                    while True:
                        opt_2 = validar_numero('¿Quiere reestablecer la base de datos?\n1.Si\n2.No\n--> ')
                        if opt_2 == 1:
                            response = make_request(url)
                            print('')
                            if response.status_code != 200:
                                print('***ERROR***')
                                print('***NO SE PUDO REESTABLCER LA BASE DE DATOS***')
                                break
                            else:
                                 bd, restablecer_bd = crear_bd(bd, bd_api, restablecer_bd)
                                 print('***BASE DE DATOS REESTABLECIDA CON EXITO***')
                                 print('')
                                 cargar_datos_en_txt("C:\\Users\\veronica\\Desktop\\Proyecto\\bd.txt", bd)
                                 break
                        elif opt_2 == 2:
                            break
                        else:
                            print('Error, valor introducido no valido')
                else:
                    print('')
                    print('***ADIOS***')
                    break
        break







main()

