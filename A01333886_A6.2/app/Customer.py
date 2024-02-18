'''
Archivo de clase Customer
'''
import database_helper


class Customer:
    '''
    Clase Customer, tiene datos y comportamiento
    '''

    def __init__(self, id_customer, nombre, ciudad):
        '''
        Constructor, inicializa un customer
        :param id_customer: identificador del customer
        :param nombre: nombre del customer
        :param ciudad: ciudad
        '''
        self.id_customer = id_customer
        self.nombre = nombre
        self.ciudad = ciudad


    def get_id_customer(self):
        '''
        Obtiene el id del customer
        :return: id del customer
        '''
        return self.id_customer


    def get_nombre(self):
        '''
        Obtiene el nombre del customer
        :return: nombre del customer
        '''
        return self.nombre


    def get_ciudad(self):
        '''
        Obtiene el numero de cuartos del customer
        :return: numero de cuartos del customer
        '''
        return self.ciudad


    def set_id_customer(self, id_customer):
        '''
        Asigna valor a la variable id del customer
        :param id_customer: id del customer
        :return:
        '''
        self.id_customer = id_customer


    def set_nombre(self, nombre):
        '''
        Asigna valor a la variable nombre
        :param nombre: nombre del customer
        :return:
        '''
        self.nombre = nombre


    def set_no_cuartos(self, ciudad):
        '''
        Asigna valor a la variable ciudad
        :param ciudad: ciudad del customer
        :return:
        '''
        self.ciudad = ciudad


    def create_customers(self):
        '''
        Create customer
        :return: same object
        '''
        raw_data = []
        raw_data.append(self.id_customer)
        raw_data.append(self.nombre)
        raw_data.append(self.ciudad)
        database_helper.save_to_file("Customers.txt", raw_data)
        return self

    def delete_customer(self):
        '''
        delete customer
        :return: None
        '''
        database_helper.delete_from_file("Customers.txt", self.id_customer)


    def display_customer_information(self):
        '''
        Gets customer info
        :return: new customer object
        '''
        database_helper.read_from_file("Customers.txt", self.id_customer)


    def modify_customer_information(self):
        '''
        modify customer info
        :return: customer object
        '''
        raw_data = []
        raw_data.append(self.id_customer)
        raw_data.append(self.nombre)
        raw_data.append(self.ciudad)
        database_helper.modify_from_file("Customer.txt", raw_data)
