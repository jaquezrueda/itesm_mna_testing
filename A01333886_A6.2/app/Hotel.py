'''
Archivo de clase hotel
'''
import database_helper


class Hotel:
    '''
    Clase Hotel, tiene datos y comportamiento
    '''

    def __init__(self, id_hotel, nombre, no_cuartos):
        '''
        Constructor, inicializa un hotel
        :param id_hotel: identificador del hotel
        :param nombre: nombre del hotel
        :param no_cuartos: numero de cuartos
        '''
        self.id_hotel = id_hotel
        self.nombre = nombre
        self.no_cuartos = no_cuartos


    def get_id_hotel(self):
        '''
        Obtiene el id del hotel
        :return: id del hotel
        '''
        return self.id_hotel


    def get_nombre(self):
        '''
        Obtiene el nombre del hotel
        :return: nombre del hotel
        '''
        return self.nombre


    def get_no_cuartos(self):
        '''
        Obtiene el numero de cuartos del hotel
        :return: numero de cuartos del hotel
        '''
        return self.no_cuartos


    def set_id_hotel(self, id_hotel):
        '''
        Asigna valor a la variable id del hotel
        :param id_hotel: id del hotel
        :return:
        '''
        self.id_hotel = id_hotel


    def set_nombre(self, nombre):
        '''
        Asigna valor a la variable nombre
        :param nombre: nombre del hotel
        :return:
        '''
        self.nombre = nombre


    def set_no_cuartos(self, no_cuartos):
        '''
        Asigna valor a la variable no_cuartos
        :param no_cuartos: numero de cuartos del hotel
        :return:
        '''
        self.no_cuartos = no_cuartos


    def create_hotel(self):
        '''
        Create hotel
        :return: same object
        '''
        raw_data = []
        raw_data.append(self.id_hotel)
        raw_data.append(self.nombre)
        raw_data.append(self.no_cuartos)
        database_helper.save_to_file("Hotel.txt", raw_data)
        return self

    def delete_hotel(self):
        '''
        delete hotel
        :return: None
        '''
        database_helper.delete_from_file("Hotel.txt", self.id_hotel)

    def display_hotel_information(self):
        '''
        Gets hotel info
        :return: new hotel object
        '''
        database_helper.read_from_file("Hotel.txt", self.id_hotel)

    def modify_hotel_information(self):
        '''
        modify hotel info
        :return: hotel object
        '''
        raw_data = []
        raw_data.append(self.id_hotel)
        raw_data.append(self.nombre)
        raw_data.append(self.no_cuartos)
        database_helper.modify_from_file("Hotel.txt", raw_data)


    def reserve_room(self, id_customer, date):
        '''
        reserve room
        :return:
        '''
        database_helper.modify_from_file("Reservations.txt", id_customer)


    def cancel_reservation(self, id_customer, date):
        '''
        cancel reservation
        :return:
        '''
        database_helper.modify_from_file("Reservations.txt", id_customer)
