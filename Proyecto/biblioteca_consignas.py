#FUNCIONES QUE CUMPLEN LAS CONSIGNAS SOLICITADAS

import os
import re
import random
import datetime
import json

from biblioteca_datos import *

#Corresponde al punto 1
def leer_archivo(path: str) -> list:
    '''
    Brief: Lee un archivo y devuelve su contenido como una lista de líneas.
    Parameters: 
        path: nombre del archivo sobre el que se hace la extracción de los datos
    Return: Una lista en caso de que el archivo exista y no esté vacío, caso contrario False
    '''

    if not os.path.isfile(path):
        print(f"Error. El archivo {path} no existe")
        return False
    
    with open(path, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()

    if not lineas:
        print(f"Error. El archivo {path} está vacío")
        return False
    
    return lineas

def parsear_linea(linea: str) -> dict:
    '''
    Brief: Parsea una línea del archivo y devuelve un diccionario con los datos extraídos.
    Parameters: 
        linea: linea que se requiere parsear
    Return: Un diccionario con los datos de la linea recibida
    '''
    lectura = re.split(r"\s*\,\s*", linea)
    personaje = {}
    personaje['Id'] = lectura[0]
    personaje['Nombre'] = lectura[1]
    razas = lectura[2]
    razas = re.split(r"-", razas)
    personaje['Raza'] = razas
    personaje['Poder de pelea'] = lectura[3]
    personaje['Poder de ataque'] = lectura[4]
    habilidades = lectura[-1]
    habilidades = re.split(r"\s*\|\$\%\s*", habilidades)
    habilidades[-1] = re.sub("\n", "", habilidades[-1])
    personaje['Habilidades'] = habilidades
    
    return personaje

def parser_csv(path: str) -> list:
    '''
    Brief: Abre un archivo .csv y parsea cada línea del archivo creando un diccionario con los datos contenidos en ella,
        luego agrega el diccionario a una lista.
    Parameters: 
        path: nombre del archivo sobre el que se hace la extracción de los datos
    Return: una lista de diccionarios
        
    '''
    lista_personajes = []
    lineas = leer_archivo(path)

    if lineas is False:
        return []

    for linea in lineas:
        personaje = parsear_linea(linea)
        lista_personajes.append(personaje)

    return lista_personajes


#Corresponde al punto 2
def obtener_set_por_clave(lista:list, clave_buscada:str) -> set:
    '''
    Brief: recorre la lista de personajes y extrae las datos únicos de la clave, utilizando un conjunto para asegurarse 
    de que no haya duplicados. 
    Parameters: 
        lista: lista sobre la que se la búsqueda
        clave_buscada: clave sobre la cual se buscan los datos, corresponde a lista
    Return: conjunto con datos únicos | False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(lista) == list and len(lista) > 0 and type(clave_buscada) == str:
        conjunto = set()
        for personaje in lista:
            if clave_buscada in personaje:
                conjunto.update(personaje[clave_buscada])
        return conjunto
    else:
        return False

def contar_personajes_por_clave(lista:list, clave_buscada:str) -> dict:
    '''
    Brief:  cuenta la cantidad de personajes por una clave. Recorre la lista de personajes, obtiene los datos de la clave
    de cada personaje y actualiza un diccionario (cantidad_por_clave) con las cantidades correspondientes. 
    Parameters: 
        lista: lista sobre la que se la búsqueda
        clave_buscada: clave sobre la cual se buscan los datos, corresponde a lista
    Return: un diccionario con los valores de la clave y la cantidad de personajes que corresponden a ese valor
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(lista) == list and len(lista) > 0 and type(clave_buscada) == str:
        cantidad_por_clave = {}
        
        for personaje in lista:
            if clave_buscada in personaje:
                lista_clave = personaje[clave_buscada]

                for elemento in lista_clave:
                    if elemento not in cantidad_por_clave:
                        cantidad_por_clave[elemento] = 1
                    else:
                        cantidad_por_clave[elemento] += 1
            else:
                lista_clave = []

        return cantidad_por_clave
    else:
        return False

def listar_cantidad_por_raza(lista: list)-> None:
    '''
    Brief:  itera sobre las razas obtenidas y muestra la cantidad correspondiente del diccionario
    Parameters: 
        lista: lista sobre la que se la búsqueda
    Return: None | False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(lista) == list and len(lista) > 0:
        diccionario_cantidad_razas = contar_personajes_por_clave(lista,'Raza')
        razas = obtener_set_por_clave(lista, 'Raza')

        if len(diccionario_cantidad_razas) > 0 and len(razas) > 0:
            for raza in razas:
                if raza in diccionario_cantidad_razas:
                    cantidad = diccionario_cantidad_razas[raza]
                    print(f"{raza}: {cantidad}")
        else:
            print("Datos inconsistentes")
    else:
        return False


#Corresponde al punto 3
def listar_personajes_por_raza(lista:list):
    '''
    Brief:  recorre cada raza y, para cada raza, recorre la lista de personajes para encontrar aquellos 
    que pertenecen a esa raza. Luego, muestra el nombre y poder de ataque de cada personaje encontrado.
    Parameters: 
        lista: lista sobre la que se la búsqueda
    Return: None | False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(lista) == list and len(lista) > 0:

        razas = obtener_set_por_clave(lista, 'Raza')

        if len(razas) > 0:
            for raza in razas:
                print(f"\nPersonajes de la raza {raza}: ")
                for personaje in lista:
                    if 'Raza' in personaje and raza in personaje['Raza']:
                        nombre = personaje['Nombre']
                        poder_ataque = personaje['Poder de ataque']

                        print(f"Nombre: {nombre} - Poder de ataque: {poder_ataque}")
        else:
            print("Datos inconsistentes")
    else:
        return False


#Corresponde al punto 4
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

def listar_personajes_por_habilidad(lista:list):
    '''
    Brief: muestra nombre, raza y el promedio entre pelea y ataque del personaje que coincide con la habilidad
    ingresada
    Parameters:
        lista: lista sobre la que se hace la búsqueda
    Return: None 
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(lista) == list and len(lista) > 0:
        habilidad_ingresada = input("Ingrese una habilidad: ").strip()
        conjunto_habilidades = obtener_set_por_clave(lista,'Habilidades')

        if  habilidad_ingresada in conjunto_habilidades:
            for personaje in lista:
                if habilidad_ingresada in personaje['Habilidades']:
                    poder_de_pelea = personaje['Poder de pelea']
                    poder_de_ataque = personaje['Poder de ataque']
                    promedio = calcular_promedio_pelea_ataque(poder_de_pelea,poder_de_ataque)
                    print(f"Nombre: {personaje['Nombre']} - "
                            f"Raza: {personaje['Raza']} - "
                            f"Promedio entre pelea y ataque: {promedio}")
        else:
            print("La habilidad ingresada no existe")
    else:
        return False


#Corresponde al punto 5
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
                if 'Nombre' in personaje and personaje['Nombre'] == personaje1:
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
    Brief: Busca el poder de ataque en una lista según el nombre del personaje recibido como parámetro
    Parameters:
        nombre: string que representa el nombre del personaje
        lista: lista sobre la que se hace la busqueda
    Return: Un entero que representa el poder de ataque del personaje con el nombre indicado
    False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(nombre) == str and type(lista) == list and len(lista) > 0:
        for personaje in lista:
            if 'Nombre' in personaje and personaje['Nombre'] == nombre:
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
    -1 en caso de que el nombre que se ingresó no exista
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


#Corresponde al punto 6
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


#Corresponde al punto 7
def leer_json()->None:
    '''
    Brief: solicita el nombre de un archivo.json y lo lee
    Parameters:
        -
    Return: None | False en caso de que el archivo no exista o esté vacío
    '''
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    
    if not os.path.isfile(nombre_archivo):
        print(f"Error. El archivo {nombre_archivo} no existe")
        return False
    
    with open(nombre_archivo,"r", encoding="UTF-8") as archivo:
        if os.stat(nombre_archivo).st_size == 0:
            print(f"Error. El archivo {nombre_archivo} está vacío")
            return False
        print(json.load(archivo))


#Corresponde al punto 8
def actualizar_personajes(lista:list)->list:
    '''
    Brief: actualiza los datos de los personajes cuya raza es Saiyan y agrega a sus habilidades
        "Transformación nivel dios", en caso de no estar.
    Parameters:
        - lista: lista sobre la cual se hace la actualización
    Return: lista actualizada | False en caso de que el parámetro recibido no cumpla con lo requerido
    '''
    if type(lista) == list and len(lista) > 0:
        for personaje in lista:
            razas = obtener_valor_clave(personaje,'Raza')
            habilidades = obtener_valor_clave(personaje,'Habilidades')
            poder_ataque = obtener_valor_clave(personaje, 'Poder de ataque')
            poder_pelea = obtener_valor_clave(personaje,'Poder de pelea')

            if 'Saiyan' in razas:
                poder_pelea = ((poder_pelea * 50) / 100) + poder_pelea
                poder_ataque = ((poder_ataque * 70) / 100) + poder_ataque
                if 'Tranformación nivel dios' not in habilidades:
                    habilidades.append('Transformación nivel dios')

                personaje['Poder de pelea'] = poder_pelea
                personaje['Poder de ataque'] = poder_ataque
                personaje['Habilidades'] = habilidades

        return lista
    else:
        return False

def generar_csv_personajes_actualizados(lista)->str:
    '''
    Brief: genera un csv con los personajes actualizados 
    Parameters:
        - lista: lista sobre la cual se genera el csv
    Return: None | False en caso de que el parámetro recibido no cumpla con lo requerido
    '''
    if type(lista) == list and len(lista) > 0:
        lista_personajes_actualizados = actualizar_personajes(lista)

        if lista_personajes_actualizados != False:

            with open('personajes_actualizados.csv','w', encoding='utf-8') as archivo:
                for personaje in lista_personajes_actualizados:
                    razas = obtener_valor_clave(personaje,'Raza')

                    if 'Saiyan' in razas:
                        razas_str = "-".join(razas)

                        habilidades = obtener_valor_clave(personaje,"Habilidades")
                        habilidades_str = "-".join(habilidades)

                        registro = "{0},{1},{2},{3},{4},{5}\n"
                        registro = registro.format(personaje['Id'],
                                                    personaje['Nombre'],
                                                    razas_str,
                                                    personaje['Poder de pelea'],
                                                    personaje['Poder de ataque'],
                                                    habilidades_str)
                        archivo.write(registro)
        else:
            print("Error en la lista")
    else:
        return False




