'''
Archivo de ayuda para leer y escribir archivos
'''

def save_to_file(filename, data):
    '''
    Funcion generica para escribir un nuevo registro a un archivo
    :param filename: nombre del archivo a escribir
    :param data: datos
    :return:
    '''
    with open(filename, 'w', encoding="utf-8") as archivo:
        str_data = ";"
        str_data.join(data)
        archivo.write(f"{str_data}\n")


def read_from_file(filename, obj_id):
    '''
    Funcion generica para leer un  registro a un archivo
    :param filename: nombre del archivo
    :param id: id
    :return:
    '''
    with open(filename, 'r', encoding="utf-8") as archivo:
        raw_data = archivo.read().split("\n")
        for row in raw_data:
            columns = row.split(";")
            if columns[0] == obj_id:
                return columns
        return None


def delete_from_file (filename, data):
    '''
    Funcion generica para borrar un nuevo registro a un archivo
    :param filename: nombre del archivo a escribir
    :param data: datos
    :return:
    '''
    with open(filename, 'w', encoding="utf-8") as archivo:
        str_data = ";"
        str_data.join(data)
        archivo.write(f"{str_data}\n")


def modify_from_file (filename, data):
    '''
    Funcion generica para borrar un nuevo registro a un archivo
    :param filename: nombre del archivo a escribir
    :param data: datos
    :return:
    '''
    with open(filename, 'w', encoding="utf-8") as archivo:
        str_data = ";"
        str_data.join(data)
        archivo.write(f"{str_data}\n")
