'''
Este archivo resuelve el problema 2: convertir numeros binarios a hex
de numeros contenidos en un archivo de texto
'''

import sys
import time
import os.path
import json


def read_file(file_name):
    '''
    Esta funcion leer un archivo y convierte los valores binarios a hex
    :param file_name: nombre del archivo que se va a leer
    :return: lista de numeros binarios del contenido del archivo
    '''
    if os.path.isfile(file_name):
        with open(file_name, 'r', encoding="utf-8") as archivo:
            raw_data = archivo.read().split("\n")
            return raw_data
    else:
        print(f"El archivo {file_name} no existe")
        return []


def write_file(binary_data, hex_data, start_time, file_name):
    '''
    Esta funcion imprime los resultados y la consola y los escribe en un archivo
    :param hex_data: informacion estadistica que sera escrita en el archivo
    :param start_time: hora a la cual comenzo a correr el programa
    :param file_name: nombre del archivo que se va a crear con el resultado
    :return: nada
    '''
    file_name_stats = " ConvertionResults.txt"
    end_time = time.time()
    time_to_run = f"El programa tomo {start_time - end_time} en correr"
    with open(file_name_stats, 'w', encoding="utf-8") as archivo:
        archivo.writelines(json.dumps(binary_data))
        archivo.writelines(json.dumps(hex_data))
        archivo.writelines(time_to_run)

    print(file_name)
    print(binary_data)
    print(hex_data)
    print(time_to_run)


def convert_numbers(raw_data):
    '''
    Esta funcion convierte numeros deciamles a binario y hexadecimal
    :param raw_data: lista de numeros en string
    :return: lista de numeros binarios y hexadecimal
    '''
    binary_data = []
    hex_data = []
    map_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                        13: 'D', 14: 'E', 15: 'F'}
    for numero in raw_data:
        if numero.isnumeric():
            numero = int(numero)
            binary_data.append(convert_to_binary(numero))
            hex_data.append(convert_to_hex(numero, map_hex))
        else:
            print(f"{numero} no es un numero valido")

    return binary_data, hex_data

def convert_to_binary(numero):
    '''
    Convierte un numero especifico de decimal a binario
    :param numero: numero decimal
    :return: numero binario
    '''
    binario = ""
    if numero == 0:
        return 0
    while numero:
        binario += str(numero & 1)
        numero = numero >> 1
    binario = binario[::-1]
    return binario

def convert_to_hex(numero, map_hex):
    '''
    Esta funcion convierte un decimal a hexadecimal
    :param numero: numero decimal
    :param map_hex: diccionario con mapeo a hexadecimal
    :return: numero hexadecimal
    '''
    hex = ""
    while numero > 0:
        r = numero % 16
        hex = map_hex[r] + hex
        numero = numero // 16

    return hex

def run_program():
    '''
    Programa principal, ejecuta todas las funciones
    :return: nada
    '''
    start_time = time.time()
    file_name = sys.argv[1]
    raw_data = read_file(file_name)
    binary_data, hex_data = convert_numbers(raw_data)
    write_file(binary_data, hex_data, start_time, file_name)


run_program()
