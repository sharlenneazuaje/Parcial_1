#FUNCIONES QUE CUMPLEN LAS CONSIGNAS SOLICITADAS

import re
import random
import datetime
import json

from biblioteca_datos import *


def parser_csv(path:str)->list:
    '''
    Brief: abre un archivo.csv y a partir de cada linea del archivo separado por comas crea un diccionario 
    con los datos contenidos en ella, luego añade el diccionario a una lista
    Parameters:
        path: archivo sobre el que se hace la extracción de los datos
    Return: en caso de existir el archivo y contener datos, una lista de diccionarios con los datos extraídos del mismo.
    En caso de no existir, se le informará al usuario el error y retornará -1.
    En caso de existir pero estar vacío, se le informará al usuario y retornará -2.
    '''
    import re
    import os
    lista_personajes = []

    #Validamos que la ruta del archivo existe:
    if not os.path.isfile(path):
        print(f"Error. El archivo {path} no existe")
        return -1
    
    #Validamos que el archivo no esté vacío
    archivo = open("DBZ.csv","r",encoding="UTF-8")
    if os.stat(path).st_size == 0:
        print(f"Error. El archivo {path} está vacío")
        return -2

    for line in archivo:
        lectura = re.split(r"\s*\,\s*",line) #Leo cada línea y la separo por las comas
        personaje = {}
        personaje['Id'] = lectura[0] #Agrego al diccionario la posición 0 de la lista con la clave Id
        personaje['Nombre'] = lectura[1]
        razas = lectura[2]
        razas = re.split(r"-",razas) #separo el string razas por guiones, en caso de tenerlos
        personaje['Raza'] = razas
        personaje['Poder de pelea'] = lectura[3]
        personaje['Poder de ataque'] = lectura[4]
        habilidades = lectura[-1]
        habilidades = re.split(r"\s*\|\$\%\s*",habilidades) #separo el string habilidades por los símbolos
        habilidades[-1] = re.sub("\n","",habilidades[-1]) #sustituyo el \n por nada
        personaje['Habilidades'] = habilidades
        lista_personajes.append(personaje)
    archivo.close()
    return lista_personajes

def calcular_cantidad_por_clave(lista: list, clave_buscada:str)->dict|int|bool:
    '''
    Brief: recorre la lista de personajes y cada diccionario dentro de ella hasta coincidir con la clave ingresada.
    Al hacerlo, recorre la lista de esa clave y agrega a otro diccionario el valor en caso de no existir.
    Al existir el valor, directamente se suma la cantidad de veces que se repite.
    Parameters:
        lista: la lista sobre la que se hace la búsqueda
        clave_buscada: clave del diccionario sobre la que se hace la búsqueda
    Return: En caso de encontrarse la clave buscada, un diccionario, que contiene los valores y sus cantidades.
    Caso contrario, informará el error al usuario y retornará -1. 
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    clave_buscada = clave_buscada.strip()
    if type(lista) == list and len(lista) > 0 and type(clave_buscada) == str and len(clave_buscada) > 0:
        diccionario = {}
        for personaje in lista:
            for clave, valor in personaje.items():
                if clave == clave_buscada:
                    for elemento in valor: 
                        if elemento not in diccionario:
                            diccionario[elemento] = 1
                        else:
                            diccionario[elemento] += 1
                
        if len(diccionario) == 0:
            print("Error. La clave buscada no existe")
            return -1
        else:
            return diccionario
    else:
        return False

def listar_cantidad_por_clave(lista:list, clave_buscada:str)->None|bool:
    '''
    Brief: calcula la cantidad de personajes por clave e imprime los datos de manera formateada
    Parameters:
        lista: la lista sobre la que se hace la búsqueda
    Return: None | False en caso de que los parámetros no cumplan con las validaciones
    '''
    clave_buscada = clave_buscada.strip()
    if type(lista) == list and len(lista) > 0 and type(clave_buscada) == str and len(clave_buscada) > 0:
        diccionario = calcular_cantidad_por_clave(lista,clave_buscada)
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")
    else:
        return False

def generar_lista_por_clave(lista:list, clave_buscada:str)->list|int|bool:
    '''
    Brief: recorre la lista recibida y genera una lista nueva con los valores de una clave en específico, sin repetirse
    Parameters:
        lista: la lista sobre la que se hace la busqueda 
        clave_buscada: clave del diccionario sobre la que se hace la búsqueda
    Return: Si se cumplen las validaciones, una lista con los valores de la clave buscada, sin repetirse.
    En caso de haber ingresado una clave buscada que no existe, se el informará al usuario y se retornará -1.
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    clave_buscada = clave_buscada.strip()
    if type(lista) == list and len(lista) > 0 and type(clave_buscada) == str and len(clave_buscada) > 0:
        lista_por_clave = []
        for personaje in lista:
            for clave, valor in personaje.items():
                if clave == clave_buscada:
                    for elemento in valor:
                        if elemento not in lista_por_clave:
                            lista_por_clave.append(elemento)

        if len(lista_por_clave) == 0:
            print("Error. La clave buscada no existe")
            return -1
        else:
            return lista_por_clave
    else:
        return False

def listar_personajes_por_clave(lista:list,clave_buscada:str)->None|bool:
    '''
    Brief: imprime el nombre y poder de ataque del personaje que coincide con la clave buscada
    Parameters:
        lista: la lista sobre la que se hace la busqueda
        clave_buscada: clave del diccionario sobre la que se hace la búsqueda
    Return: None | False en caso de que los parámetros no cumplan con las validaciones
    '''
    clave_buscada = clave_buscada.strip()
    if type(lista) == list and len(lista) > 0 and type(clave_buscada) == str and len(clave_buscada) > 0:
        lista_por_clave = generar_lista_por_clave(lista, clave_buscada)
        for dato in lista_por_clave:
            print(f"\n{dato}:")
            for personaje in lista:
                for clave, valor in personaje.items():
                    if clave == clave_buscada:
                        for elemento in valor:
                            if elemento == dato:
                                print(f"Nombre: {personaje['Nombre']} - Poder de ataque: {personaje['Poder de ataque']}")
    else:
        return False

def sumar_datos(dato_1: int, dato_2: int)->int|bool:
    '''
    Brief: suma dos datos
    Parameters:
        dato1: dato de tipo entero
        dato2: dato de tipo entero
    Return: en caso de cumplirse las validaciones, la suma de dos enteros. Caso contrario, False
    '''
    if type(dato_1) == int and type(dato_2) == int:
        suma = dato_1 + dato_2
        return suma
    else:
        return False
    
def calcular_promedio_pelea_ataque(dato_1: int, dato_2: int)->float|bool:
    '''
    Brief: calcula el promedio de dos datos
    Parameters:
        dato1: dato de tipo entero
        dato2: dato de tipo entero
    Return: en caso de cumplirse las validaciones, un float que representa el promedio de dos datos,
    caso contrario, False
    '''
    if type(dato_1) == int and type(dato_2) == int:
        suma = sumar_datos(dato_1,dato_2)
        promedio = suma / 2
        return promedio
    else:
        return False

def mostrar_personajes_por_habilidad(lista: list, clave_buscada:str)->None|bool:
    '''
    Brief: muestra nombre, raza y el promedio entre pelea y ataque del personaje que coincide con la habilidad
    ingresada
    Parameters:
        lista: lista sobre la que se hace la búsqueda
        clave_buscada: clave del diccionario sobre la que se hace la búsqueda
    Return: None 
    False en caso de que los parámetros no cumplan con las validaciones
    En caso de que la habilidad ingresada no esté entre las habilidades de la lista, se le informa al usuario
    y retorna -1
    '''
    if type(lista) == list and len(lista) > 0 and type(clave_buscada) == str and len(clave_buscada) > 0:
        habilidad_ingresada = input("Ingrese una habilidad: ").strip()
        lista_habilidades = generar_lista_por_clave(lista,'Habilidades')
        
        if habilidad_ingresada in lista_habilidades and type(habilidad_ingresada) == str:
            for personaje in lista:
                for clave, valor in personaje.items():
                    if clave == clave_buscada:
                        for elemento in valor:
                            if elemento == habilidad_ingresada:
                                poder_de_pelea = personaje['Poder de pelea']
                                poder_de_ataque = personaje['Poder de ataque']
                                promedio = calcular_promedio_pelea_ataque(poder_de_pelea,poder_de_ataque)
                                print(f"Nombre: {personaje['Nombre']} - "
                                    f"Raza: {personaje['Raza']} - "
                                    f"Promedio entre pelea y ataque: {promedio}")
        else:
            print("Error. La habilidad ingresada no existe")
            return -1
    else:
        return False

def seleccionar_personaje(lista: list)->str|int|bool:
    '''
    Brief: busca en la lista el nombre del personaje ingresado y lo retorna
    Parameters:
        lista: lista sobre la que se hace la búsqueda
    Return: Un string que representa el nombre del personaje ingresado
    -1 en caso de que el nombre ingresado no exista
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    valor_encontrado = False
    if type(lista) == list and len(lista) > 0:
        personaje1 = input("Ingrese un personaje: ").strip()
        if type(personaje1) == str:
            for personaje in lista:
                for clave, valor in personaje.items():
                    if clave == 'Nombre' and valor == personaje1:
                        valor_encontrado = True
                        return personaje['Nombre']
        if valor_encontrado == False:
            print("El nombre no existe")
            return -1
    else:
        return False

def random_personaje(lista:list)-> dict:
    '''
    Brief: selecciona un personaje aleatorio de la lista y retorna su nombre
    Parameters:
        -
    Return: Un string que representa el nombre del personaje elegido
    '''
    personaje2 = random.choice(lista)
    return personaje2['Nombre']

def buscar_poder_ataque(nombre:str,lista:list)->int|bool:
    '''
    Brief: Busca el poder de ataque en una lista según el nombre del personaje ingresado
    Parameters:
        nombre: string que representa el nombre del personaje
        lista: lista sobre la que se hace la busqueda
    Return: Un entero que representa el poder de ataque del personaje con el nombre indicado
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(nombre) == str and type(lista) == list and len(lista) > 0:
        for personaje in lista:
            for clave, valor in personaje.items():
                if clave == "Nombre" and valor == nombre:
                    return personaje['Poder de ataque']
    else:
        return False

def calcular_ataque(poder_1:int, poder_2:int)->int|bool:
    '''
    Brief: Calcula el máximo valor numérico entre dos cantidades
    Parameters:
        dato1: dato de tipo entero
        dato1: dato de tipo entero
    Return: Un entero que representa el máximo valor entre los dos datos que se recibieron
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(poder_1) == int and poder_1 > 0 and type(poder_2) == int and poder_2 > 0:
        if poder_1 > poder_2:
            ganador = poder_1
        else:
            ganador = poder_2
        return ganador
    else:
        return False

def generar_fecha()->str:    
    '''
    Brief: genera la fecha y hora actual
    Parameters:
        -
    Return: Un string formateado con la fecha actual
    '''
    fecha = str(datetime.datetime.now())
    fecha = re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}",fecha)
    fecha_str = str(fecha[0]).replace("-","/")
    return fecha_str

def jugar_batalla(lista:list)->str|bool:
    '''
    Brief: Gestiona la batalla entre dos personajes según el poder de ataque
    Parameters:
        lista = lista sobre la que se hace la búsqueda
    Return: Un archivo text donde se alojan los datos de la batalla: fecha, ganador y perdedor
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(lista) == list and len(lista) > 0:
        personaje1 = seleccionar_personaje(lista) #tengo el nombre del primero
        if personaje1 == -1:
            return -1
        personaje2 = random_personaje(lista) #tengo el nombre del segundo

        poder1 = buscar_poder_ataque(personaje1,lista)
        poder2 = buscar_poder_ataque(personaje2,lista)

        ganador = calcular_ataque(poder1,poder2)

        if ganador == poder1:
            nombre_ganador = personaje1
            nombre_perdedor = personaje2
        else:
            nombre_ganador = personaje2
            nombre_perdedor = personaje1

        fecha = generar_fecha()
        registro = f"{fecha}: Ganador: {nombre_ganador} - Perdedor: {nombre_perdedor}\n"

        with open("registro_batallas.txt","a") as archivo:
            archivo.write(registro)
    else:
        return False

def obtener_valor_clave(diccionario:dict, clave_buscada:str):
    '''
    Brief: Obtiene el valor de una clave específica de un diccionario
    Parameters:
        diccionario: diccionario sobre el cual se busca el valor
    Return: un dato que representa el valor de la clave del diccionario buscada o
    False en caso de que los parámetros no cumplan con las validaciones

    '''
    if type(diccionario) == dict and len(diccionario) > 0 and type(clave_buscada) == str:
        for clave, valor in diccionario.items():
            if clave == clave_buscada:
                return valor
    else:
        return False

def filtrar_personajes(lista:list, raza_obtenida:str, habilidad_obtenida:str)->dict:
    '''
    Brief: Se encarga de filtrar los personajes de acuerdo a una raza y una habilidad 
    Parameters:
        lista = lista sobre la que se hace el filtro
        raza_obtenida = valor que se usa para buscar los personajes que coinciden con ese tipo de raza
        habilidad_obtenida = valor que se usa para buscar los personajes que coinciden con ese tipo de habilidad
    Return: Un diccionario con una lista que contiene el nombre, poder de ataque y habilidades de los personajes 
        que contienen tanto la raza como la habilidad que se recibieron, en caso de haber.
        Caso contrario, retornará False
        -1 en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(lista) == list and len(lista) > 0 and type(raza_obtenida) == str and type(habilidad_obtenida) == str:
        data = {}
        data['personajes'] = []
        for personaje in lista:
            raza = obtener_valor_clave(personaje,'Raza')
            habilidades = obtener_valor_clave(personaje,'Habilidades')
            if raza_obtenida in raza and habilidad_obtenida in habilidades:
                diccionario = {}
                lista_habilidades_filtrada = []
                for habilidad in habilidades:
                    if habilidad != habilidad_obtenida:
                        lista_habilidades_filtrada.append(habilidad)

                diccionario['nombre'] = personaje['Nombre']
                diccionario['poder de ataque'] = personaje['Poder de ataque']
                diccionario['habilidades'] = lista_habilidades_filtrada
                data['personajes'].append(diccionario)
        
        if len(data["personajes"]) == 0:
            return False
        else:
            return data
    else:
        print("Los parámetros no contienen el tipo de dato correcto")
        return -1

def generar_nombre_archivo(raza:str,habilidad:str)->str:
    '''
    Brief: Genera el nombre de un archivo con un determinado formato
    Parameters:
        raza: corresponde al nombre de la raza que formará parte del nombre del archivo
        habilidad: corresponde al nombre de la habilidad que formará parte del nombre del archivo
    Return: un string formateado con la raza y la habilidad recibidas
    False en caso de los parámetros no cumplan con las validaciones
    '''
    if type(raza) == str and type(habilidad) == str:
        raza = raza.strip()
        raza = raza.replace(" ", "_")
        habilidad = habilidad.replace(" ","_")
        nombre_archivo = f'{raza}_{habilidad}.json'
        return nombre_archivo
    else:
        return False

def guardar_personajes_json(diccionario:dict, raza:str, habilidad:str)->str:
    '''
    Brief: Crea un archivo.json con un diccionario
    Parameters:
        diccionario: diccionario que contiene los datos de los personajes filtrados
    Return: un archivo.json o False en caso de los parámetros no cumplan con las validaciones
    '''
    if type(diccionario) == dict and type(raza) == str and type(habilidad) == str:
        nombre_archivo = generar_nombre_archivo(raza,habilidad)
        with open(nombre_archivo, 'w',encoding="UTF-8") as archivo:
            json.dump(diccionario, archivo, indent = 4, ensure_ascii=False)
    else:
        return False

def generar_json_personajes(lista:list)->str:
    '''
    Brief: Genera un archivo.json con los personajes filtrados por la raza y la habilidad ingresadas por el usuario
    Parameters:
        lista: lista sobre la que se hace el filtro
    Return: un archivo.json que contiene los personajes que hayan coincidido con la raza y la habilidad ingresadas,
    caso contrario, se informará al usuario y se retornará False.
    -1 en caso de los parámetros no cumplan con las validaciones
    '''
    if type(lista) == list and len(lista) > 0:
        raza_ingresada = input("Ingrese una raza: ")
        habilidad_ingresada = input("Ingrese una habilidad: ")
        if type(raza_ingresada) == str and type(habilidad_ingresada) == str:
            diccionario = filtrar_personajes(lista, raza_ingresada, habilidad_ingresada)
            if diccionario == False:
                print("No hay personajes que cumplan con los dos criterios ingresados")
                return False
            guardar_personajes_json(diccionario, raza_ingresada, habilidad_ingresada)
    else:
        return -1

def leer_json()->None:
    '''
    Brief: solicita el nombre de un archivo.json y lo lee
    Parameters:
        -
    Return: None | -1 en caso de que el archivo no exista | -2 si el archivo existe pero está vacío
    '''
    import os
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    #Validamos que la ruta del archivo existe:
    if not os.path.isfile(nombre_archivo):
        print(f"Error. El archivo {nombre_archivo} no existe")
        return -1
    
    #Validamos que el archivo no esté vacío
    with open(nombre_archivo,"r", encoding="UTF-8") as archivo:
        if os.stat(nombre_archivo).st_size == 0:
            print(f"Error. El archivo {nombre_archivo} está vacío")
            return -2
        print(json.load(archivo))

