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
        opcion = input("Ingrese una opción: ")
        opcion = sanitizar_entero(opcion)

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
        "8. Actualizar personajes Saiyan",
        "9. Salir"]
    
    flag_generar_normalizar_datos = False
    
    while True:
        opcion = dragon_ball_menu_principal(menu_principal)
        match opcion:
            case 1:
                lista_personajes = parser_csv("DBZ.csv")
                dragon_ball_normalizar_datos(lista_personajes)
                flag_generar_normalizar_datos = True
            case 2:
                if flag_generar_normalizar_datos == True:
                    listar_cantidad_por_raza(lista_personajes)
                else:
                    print("Error. Debe generar y normalizar los datos primero")
            case 3:
                if flag_generar_normalizar_datos == True:
                    listar_personajes_por_raza(lista_personajes)
                else:
                    print("Error. Debe generar y normalizar los datos primero")
            case 4:
                if flag_generar_normalizar_datos == True:
                    listar_personajes_por_habilidad(lista_personajes)
                else:
                    print("Error. Debe generar y normalizar los datos primero")
            case 5: 
                if flag_generar_normalizar_datos == True:
                    jugar_batalla(lista_personajes)
                else:
                    print("Error. Debe generar y normalizar los datos primero")
            case 6:
                if flag_generar_normalizar_datos == True:
                    generar_json_personajes(lista_personajes)
                else:
                    print("Error. Debe generar y normalizar los datos primero")
            case 7:
                if flag_generar_normalizar_datos == True:
                    leer_json()
                else:
                    print("Error. Debe generar y normalizar los datos primero")
            case 8:
                if flag_generar_normalizar_datos == True:
                    generar_csv_personajes_actualizados(lista_personajes)
                else:
                    print("Error. Debe generar y normalizar los datos primero")
            case 9:
                break