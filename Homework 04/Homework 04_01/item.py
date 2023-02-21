""" This module adds e-store item class that represent goods"""

import exceptions


class StoreItem:
    def __init__(self, item_category: str = 'Category', item_name: str = 'Name', item_price=float()):
        """
        Class that represent some goods selling in e-store.

        Have setter and getter methods to work with store item price attribute.

        Parameters
        ----------
        item_category
            String title of category that item belongs, for example - 'Electrical devices', 'Toys', 'Food', etc.
        item_name
            String title of item, for example 'Screwdriver Dexter 001'.
        item_price
            Float value in format '123.00'
        """
        self.__item_category = item_category
        self.__item_name = item_name

        # do check of input value BEFORE assign to 'self.__item_price'
        if not isinstance(item_price, float):
            raise exceptions.PriceTypeError(self.__item_name, item_price)
        if item_price <= 0:
            raise exceptions.ZeroPriceError(self.__item_name, item_price)
        self.__item_price = item_price

    def set_price(self, item_price):
        self.__item_price = item_price

        if not isinstance(item_price, float):
            raise exceptions.PriceTypeError(self.__item_name, self.__item_price)
        if item_price <= 0:
            raise exceptions.ZeroPriceError(self.__item_name, self.__item_price)

    def get_price(self):
        return self.__item_price

    def __str__(self):
        return f'\nItem category: {self.__item_category} \n' \
               f'name: {self.__item_name} \n' \
               f'price: {self.__item_price} \n'
