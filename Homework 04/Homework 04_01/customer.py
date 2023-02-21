""" This module adds e-store customer class """


class StoreCustomer:
    def __init__(self, customer_name: str, customer_surname: str, customer_phone: str):
        """
        Class that represent customer of store and used in 'ShoppingCart' class methods.

        Parameters
        ----------
        customer_name
            Name, string type, in format 'Nick'.
        customer_surname
            Surname, string type, in format 'Smith'.
        customer_phone
            Contact phone, string type, in format '+XXXXXXXXXXX'
        """
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_phone = customer_phone


    def __str__(self):
        return f'Customer name: {self.customer_name} {self.customer_surname}, phone: {self.customer_phone}'
