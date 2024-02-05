'''
Este archivo resuelve el problema 1: calcular estadisticas
de numeros contenidos en un archivo de texto
'''

import sys
import time
import os.path
import statistics
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


def write_file(stats_data, start_time, file_name):
    '''
    Esta funcion imprime los resultados y la consola y los escribe en un archivo
    :param stats_data: informacion estadistica que sera escrita en el archivo
    :param start_time: hora a la cual comenzo a correr el programa
    :param file_name: nombre del archivo que se va a crear con el resultado
    :return: nada
    '''
    file_name_stats = "StatisticsResults.txt"
    end_time = time.time()
    time_to_run = f"El programa tomo {start_time - end_time} en correr"
    with open(file_name_stats, 'w', encoding="utf-8") as archivo:
        archivo.writelines(json.dumps(stats_data))
        archivo.writelines(time_to_run)

    print(file_name)
    print(stats_data)
    print(time_to_run)


def compute_stats(raw_data):
    '''
    Esta funcion calculas estadisticas requeridas sobre una lista de numeros
    :param raw_data: lista de numeros
    :return: estadisticas
    '''
    dict_stats = {
        "count": 0.0,
        "mean": 0.0,
        "median": 0.0,
        "mode": 0.0,
        "standard_deviation": 0.0,
        "variance": 0.0
    }
    dict_mode = {}
    total_sum = 0
    total_count = 0
    raw_data_num = []
    for numero in raw_data:
        if numero.isnumeric():
            numero = float(numero)
            raw_data_num.append(numero)
            total_sum += numero
            total_count += 1
            if str(numero) in dict_mode.keys():
                dict_mode[str(numero)] += 1
            else:
                dict_mode[str(numero)] = 1
        else:
            print(f"{numero} no es un numero valido")

    numeros_sorteados = sorted(raw_data)
    mode_list = [k for k, i in dict_mode.items() if i == max(dict_mode.values())]
    variance_de = sum([((x - dict_stats["mean"]) ** 2) for x in raw_data_num])
    dict_stats["count"] = total_count
    dict_stats["mean"] = 0 if total_count == 0 else total_sum / total_count
    dict_stats["median"] = numeros_sorteados[round(total_count / 2)]
    dict_stats["mode"] = 0 if len(mode_list) == 0 else mode_list[0]
    dict_stats["standard_deviation"] = statistics.pstdev(raw_data_num)
    dict_stats["variance"] = variance_de / len(raw_data_num)

    return dict_stats


def run_program():
    '''
    Programa principal, ejecuta todas las funciones
    :return: nada
    '''
    start_time = time.time()
    file_name = sys.argv[1]
    raw_data = read_file(file_name)
    stats_data = compute_stats(raw_data)
    write_file(stats_data, start_time, file_name)


run_program()
