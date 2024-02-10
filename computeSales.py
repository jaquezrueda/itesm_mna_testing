'''
Este archivo resuelve el problema 1 de la actividad 5.2:
calcular ventas
'''

import sys
import time
import os.path
import json



def read_file(prices_catalog, sales_record):
    '''
    Esta funcion lee dos archivos y los convierte a json
    :param prices_catalog: archivo de productos y precios
    :param sales_record: archivo con lista de ventas
    :return: dos objetos json
    '''
    try:
        if os.path.isfile(prices_catalog):
            with open(prices_catalog, 'r', encoding="utf-8") as archivo:
                raw_prices = json.load(archivo)
        if os.path.isfile(sales_record):
            with open(sales_record, 'r', encoding="utf-8") as archivo:
                raw_sales = json.load(archivo)
        return raw_prices, raw_sales

    except ValueError as error:
        print("El formato no es un json valido")
        print(error)
        return {}, {}

def write_file(start_time, results):
    '''
    Escribe el resultado en un archivo
    :param start_time: fecha hora que comenzo a correr el programa
    :param results: texto con totales
    :return:
    '''
    file_name_stats = "SalesResults.txt"
    end_time = time.time()
    time_to_run = f"El programa tomo {start_time - end_time} en correr"
    with open(file_name_stats, 'w', encoding="utf-8") as archivo:
        archivo.writelines(results)
        archivo.writelines("\n")
        archivo.writelines(time_to_run)

    print(results)
    print(time_to_run)

def compute_sales(raw_prices, raw_sales):
    '''
    :param raw_prices: json with all products and prices
    :param raw_sales: json with all sales
    :return: Texto con la suma de todas las ventas
    '''
    ventas_totales = 0
    for venta in raw_sales:
        producto = next(precio for precio in raw_prices if precio["title"] == venta["Product"])
        precio = producto["price"]
        cantidad = venta["Quantity"]
        if isinstance(precio, (float, int)) :
            ventas_totales += (precio * cantidad )
        else:
            print(f"{precio} no es numero valido para el precio")
    texto_total = f"Las ventas totales son: {ventas_totales}"
    return texto_total


def run_program():
    '''
    Programa principal, ejecut a todas las funciones
    :return: nada
    '''
    start_time = time.time()
    if len(sys.argv) > 2:
        prices_catalog = sys.argv[1]
        sales_record = sys.argv[2]
        raw_prices, raw_sales = read_file(prices_catalog, sales_record)
        results = compute_sales(raw_prices, raw_sales)
        write_file(start_time, results)
    else:
        print("No se proporcionaron los dos archivos requeridos")


run_program()
