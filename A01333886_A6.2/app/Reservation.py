'''
Archivo de clase Reservation
'''
import Hotel

class Reservation:
    '''
    Clase Reservation, tiene datos y comportamiento
    '''

    def create_reservation(self, id_reservation, id_customer, id_hotel, date):
        '''
        creates a new reservation
        :param id_reservation:
        :param customer:
        :param hotel:
        :param date:
        '''
        hotel = Hotel(id_hotel, "Marriot", 500)
        hotel.reserve_room(id_customer, date)


    def cancel_reservation(self, id_reservation):
        '''
        cancels reservation
        :param id_reservation:
        :return:
        '''
        hotel = Hotel(id_hotel, "Marriot", 500)
        hotel.reserve_room(id_customer, date)