"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_columna =  0
    
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        for row in data:
            suma_columna += int(row[1])
    print(suma_columna)
    return suma_columna


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        cantidad_letras = {}
    
        for fila in data:
            letra = fila [0][0]
            if letra in cantidad_letras:
                cantidad_letras[letra] += 1
            else:
                cantidad_letras[letra] = 1
    
    resultado = sorted(cantidad_letras.items())
    print(resultado)
    return resultado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        suma_letras = {}
        for fila in data:
            letra = fila[0][0]
            valor = float(fila[1])
            if letra in suma_letras:
                suma_letras[letra] += valor
            else:
                suma_letras[letra] = valor
        
    resultado = sorted(suma_letras.items())
    print(resultado)
    return resultado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        fechas = []
        for fila in data:
            fecha = fila[2]
            fechas.append(fecha)
            
    registros_mes = {}
    for fecha in fechas:
        mes = fecha.split('-')[1]
        if mes in registros_mes:
            registros_mes [mes] += 1
        else:
            registros_mes [mes] = 1
    lista_registros_mes = sorted(registros_mes.items())
    print(lista_registros_mes)
    return lista_registros_mes


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        resultados = {}
        
        for fila in data:
            letra = fila[0]
            valor = int(fila[1])
            
            if letra not in resultados:
                resultados[letra] = [valor, valor]
            else:
                resultados[letra][0] = max(resultados[letra][0], valor)
                resultados[letra][1] = min(resultados[letra][1], valor)
                    
        lista_resultados = [(letra, resultados[letra][0], resultados[letra][1]) for letra in sorted(resultados)]
        print(lista_resultados)
    
    return lista_resultados


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        resultado = {}
        
        for fila in data:
            pares = fila[4].split(',')
            
            for par in pares:
                key, value = par.split(':')
                key = key.strip()
                
                if key in resultado:
                    resultado[key].append(float(value))
                else:
                    resultado[key] = [float(value)]

    resultado_final = []
    for key in sorted(resultado.keys()):
        valores = resultado[key]
        minimo = min(valores)
        maximo = max(valores)
        resultado_final.append((key, minimo, maximo))
    
    print(resultado_final)
    
    return resultado_final


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        valores = {}
        for fila in data:
            if fila[1] not in valores:
                valores[fila[1]] = [fila[0]]
            else:
                valores[fila[1]].append(fila[0])
        resultado = [(float(key),valores[key]) for key in valores]
        resultado.sort()
        print(resultado)
        
    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        valores = {}
        for fila in data:
            if fila[1] not in valores:
                valores[fila[1]] = [fila[0]]
            else:
                valores[fila[1]].append(fila[0])
        resultado = [(float(key),sorted(list(set(valores[key])))) for key in valores]
        resultado.sort()
        print(resultado)
        
    return resultado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        
        contador = {}
        for fila in data:
            dic = fila[4].split(',')
            for elemento in dic:
                key = elemento[:3]
                if key in contador:
                    contador[key] += 1
                else:
                    contador[key] = 1
        print(contador)
    
    
    return contador


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        
        resultado = []
        for fila in data:
            letra = fila[0]
            colum4 = fila[3].split(',')
            colum5 = fila[4].split(',')
            resultado.append((letra, len(colum4), len(colum5)))
                      
        print(resultado)
   
    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        
        sumas = {}
        for fila in data:
            colum4 = fila[3].split(',')
            for letra in colum4:
                if letra not in sumas:
                    sumas[letra] = 0
                sumas[letra] += int(fila[1])
                 
        sumas_ordenadas = dict(sorted(sumas.items()))
        print(sumas_ordenadas)
    
    return sumas_ordenadas


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r") as datafile:
        data = csv.reader(datafile, delimiter="\t")
        
        resultado = {}
        
        for fila in data:
            letra = fila[0]
            cadena = fila[4]
            elementos = cadena.split(',')
            
            diccionario_5 = {}
            
            for elemento in elementos:
                clave, valor = elemento.split(':')
                diccionario_5[clave] = float(valor)
            suma = sum(diccionario_5.values())
        
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += suma
            
    resultado_ordenado = dict(sorted(resultado.items()))
            
    print(resultado_ordenado)
                   
    return resultado_ordenado