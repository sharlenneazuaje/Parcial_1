#FUNCIONES DEL MENÚ Y LA APP

from biblioteca_consignas import *

def imprimir_menu(menu:list)->None:
    '''
    Brief: Imprime un menu
    Parameters:
        menu -> Lista que contiene las opciones del menu
    Return: None | False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(menu) == list and len(menu) > 0:
        for opcion in menu:
            print(opcion)
    else:
        return False

def dragon_ball_menu_principal(menu:list):
    '''
    Brief: Imprime un menú y evalúa si la opción que ingresa el usuario está contemplada en el mismo
    Parameters:
        menu -> Lista que contiene las opciones del menu
    Return: Un entero en caso de ser la opción correcta
    None 
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(menu) == list and len(menu) > 0:
        imprimir_menu(menu)
        numero_opciones = len(menu)
        opcion = int(input("Ingrese una opción: "))

        if opcion <= numero_opciones:
            return opcion
        else:
            print("Error. Ingrese una opción válida dentro del menú")
    else:
        return False

def dragon_ball_app():
    '''
    Brief: Se encarga de la ejecuión principal
    Parameters:
        lista -> Lista que se le pasa como parámetro a cada una de las funciones para la ejecución
    Return: None
    '''
    menu_principal = ["1. Normalizar datos",
        "2. Listar cantidad por raza",
        "3. Listar personajes por raza",
        "4. Listar personajes por habilidad",
        "5. Jugar batalla",
        "6. Guardar Json",
        "7. Leer Json",
        "8. Salir"]
    flag_generar_normalizar_datos = False
    while True:
        opcion = dragon_ball_menu_principal(menu_principal)
        match opcion:
            case 1:
                lista_personajes = parser_csv("DBZ.csv")
                dragon_ball_normalizar_datos(lista_personajes)
                flag_generar_normalizar_datos = True
            case 2:
                listar_cantidad_por_clave(lista_personajes,'Raza')
            case 3:
                listar_personajes_por_clave(lista_personajes,'Raza')
            case 4:
                mostrar_personajes_por_habilidad(lista_personajes,'Habilidades')
            case 5: 
                if flag_generar_normalizar_datos == True:
                    jugar_batalla(lista_personajes)
                else:
                    print("Error. Debe generar y normalizar los datos primero")
            case 6:
                generar_json_personajes(lista_personajes)
            case 7:
                leer_json()
            case 8:
                break