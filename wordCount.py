'''
Este archivo resuelve el problema 1: calcular estadisticas
de numeros contenidos en un archivo de texto
'''

import sys
import time
import os.path
import json


def read_file(file_name):
    '''
    Esta funcion leer un archivo y convierte su contenido a una lista de numeros
    :param file_name: nombre del archivo que se va a leer
    :return: lista de numeros del contenido del archivo
    '''
    if os.path.isfile(file_name):
        with open(file_name, 'r', encoding="utf-8") as archivo:
            raw_data = archivo.read().split("\n")
            return raw_data
    else:
        print(f"El archivo {file_name} no existe")
        return []


def write_file(word_count_data, start_time, file_name):
    '''
    Esta funcion imprime los resultados y la consola y los escribe en un archivo
    :param word_count_data: informacion de frecuencia de palabras
    :param start_time: hora a la cual comenzo a correr el programa
    :param file_name: nombre del archivo que se va a crear con el resultado
    :return: nada
    '''
    file_name_stats = "WordCountResults.txt"
    end_time = time.time()
    time_to_run = f"El programa tomo {start_time - end_time} en correr"
    with open(file_name_stats, 'w', encoding="utf-8") as archivo:
        archivo.writelines(json.dumps(word_count_data))
        archivo.writelines(time_to_run)

    print(file_name)
    print(word_count_data)
    print(time_to_run)


def word_frequency(raw_data):
    '''
    Esta funcion calculas frequencia de palabras de una lista
    :param raw_data: lista de palabras
    :return: estadisticas
    '''
    dict_palabras = {}
    for palabra in raw_data:
        if str(palabra) in dict_palabras.keys():
            dict_palabras[str(palabra)] += 1
        else:
            dict_palabras[str(palabra)] = 1

    print(dict_palabras)
    return dict_palabras

def run_program():
    '''
    Programa principal, ejecuta todas las funciones
    :return: nada
    '''
    start_time = time.time()
    file_name = sys.argv[1]
    raw_data = read_file(file_name)
    word_count_data = word_frequency(raw_data)
    write_file(word_count_data, start_time, file_name)


run_program()
