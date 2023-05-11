#FUNCIONES QUE NORMALIZAN LOS DATOS

import re

def sanitizar_entero(numero_str:str)->int:
    '''
    Brief: analiza el string recibido y determinar si es un número entero positivo
    Parameters:
        numero_str -> un string que representa un posible número entero
    Return: 
        -1 Si contiene carácteres no numéricos
        -2 Si el número es negativo
        -3 Si ocurren otros errores que no permiten convertirlo a entero
        El número casteado a entero en caso que se verifique que el texto contenido en el string 
        es un número entero positivo
    '''
    if type(numero_str) == str:
        numero_str = numero_str.strip()

        if len(numero_str) > 0 and re.search("^-{0,1}[0-9]*$", numero_str) is not None:
            if numero_str.startswith('-'):
                return -2
            
            return int(numero_str)
        
        return -1
        
    return -3

def sanitizar_flotante(numero_str:str)->float:
    '''
    Brief: analiza el string recibido y determinar si es un número flotante positivo
    Parameters:
        numero_str -> un string que representa un posible número flotante
    Return: 
        -1:Si contiene carácteres no numéricos
        -2: Si el número es negativo
        -3: Si ocurren otros errores que no permiten convertir a flotante 
        El número casteado a flotante: en caso de que se verifique que el texto contenido en el string 
        es un número flotante positivo
    '''
    if type(numero_str) == str:
        numero_str = numero_str.strip()

        if len(numero_str) > 0 and re.search("^-{0,1}[0-9]*\.[0-9]*$", numero_str) is not None:
            if numero_str.startswith('-'):
                return -2
            
            return float(numero_str)
        
        return -1
        
    return -3

def sanitizar_string(valor_str:str, valor_por_defecto = '-')->str:
    '''
    Brief: analiza el string recibido y determina si es solo texto (sin números).
    Parameters:
        valor_str -> un string que representa el texto a validar
        valor_por_defecto -> un string que representa un valor por defecto (parámetro opcional, inicializado con ‘-’)
    Return: 
        Un string en caso de que el valor_str no tenga números
        En caso de encontrarse números, retorna “N/A”
        Si el valor_str es vacío, retorna el valor_por_defecto convertido en minusculas
    '''
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()
    valor_str = re.sub("/", " ", valor_str)

    if len(valor_str) == 0 and len(valor_por_defecto) > 0:
        return valor_por_defecto
    
    #el patrón niega todos los números y deja las letras, si no hay letras, entonces devuelve n/a porque hay números
    if re.search("^\D*$", valor_str) is None:
        return "N/A"
    
    return valor_str

def sanitizar_dato(heroe:dict, clave_buscada:str, tipo_dato:str)->bool:
    '''
    Brief: sanitiza el valor del diccionario correspondiente a la clave y al tipo de dato recibido
    Parameters:
        heroe -> un diccionario con los datos del personaje
        clave -> un string que representa el dato a sanitizar (la clave del
                diccionario). Por ejemplo altura
        tipo_dato -> un string que representa el tipo de dato a sanitizar. Puede
                tomar los valores: ‘string’, ‘entero’ y ‘flotante’
    Return: un booleano, True en caso de haber sanitizado algún dato y False en caso contrario.
    '''
    tipo_dato = sanitizar_string(tipo_dato)

    if re.search("^(string|entero|flotante)$",tipo_dato) is None:
        print("Tipo de dato no reconocido")
        return False

    if clave_buscada not in heroe:
        print("La clave especificada no existe en el heroe")
        return False

    for clave, valor in heroe.items():
        if clave == clave_buscada:
            match tipo_dato:
                case "string":
                    heroe[clave] = sanitizar_string(valor)
                case "entero":
                    heroe[clave] = sanitizar_entero(valor)
                case "flotante":
                    heroe[clave] = sanitizar_flotante(valor)

    return heroe

def dragon_ball_normalizar_datos(lista:list)->None|bool:
    '''
    Brief: recorre la lista de personajes y sanitiza los valores solo de las siguientes claves: 
    ‘Poder de pelea’, ‘Poder de ataque’
    Parameters:
        lista: la lista sobre la que se hace la normalización 
    Return: None | False en caso de que los parámetros no cumplan con las validaciones
    '''
    if type(lista) == list and len(lista) > 0:
        for personaje in lista:
                sanitizar_dato(personaje,'Poder de pelea','entero')
                sanitizar_dato(personaje,'Poder de ataque','entero')
                sanitizar_dato(personaje,'Id','entero')

        print("Datos normalizados")
    else:
        return False