"""This module contains custom exceptions for e-store items."""


class PriceTypeError(Exception):
    """
    Custom exception class for StoreItem class.
    """
    def __init__(self, item_name, item_price):
        self.__item_name = item_name
        self.__item_price = item_price

    def __str__(self):
        return f'Item "{self.__item_name}" price type error: price type cant be <{str(type(self.__item_price))}>. ' \
               f'Expected float type in format "1234.00".'


class ZeroPriceError(Exception):
    """
    Custom exception class for StoreItem class.
    """
    def __init__(self, item_name, item_price):
        self.__item_name = item_name
        self.__item_price = item_price

    def __str__(self):
        return f'Item "{self.__item_name}" price <= 0 error: price cant be <{self.__item_price}>. '
