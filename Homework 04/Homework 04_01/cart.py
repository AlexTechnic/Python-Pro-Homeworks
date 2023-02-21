""" This module adds e-store shopping cart class """

import item
import customer

class ShoppingCart:
    def __init__(self, cart_customer: customer.StoreCustomer):
        """
        Class that process adding items to e-store shopping cart by some customer,
        making total sum of goods and printing bill.

        Parameters
        ----------
        cart_customer
            Can be any customer instance from class StoreCustomer.
        """
        self.cart_customer = cart_customer
        self.__added_cart_items = []
        self.__cart_items_qty = []

    def add_item(self, cart_item: item.StoreItem, quantity: int = 1):
        if cart_item in self.__added_cart_items:
            index = self.__added_cart_items.index(cart_item)
            self.__cart_items_qty[index] += quantity
        else:
            self.__added_cart_items.append(cart_item)
            self.__cart_items_qty.append(quantity)

    def cart_total(self):
        """ return float type sum value of all gathered items """
        return sum(item.get_price() * self.__cart_items_qty[index] for index, item in enumerate(self.__added_cart_items))

    def __str__(self):
        """ return total and sub-total bill for each item in shopping cart """
        res = '\n'.join(map(
            lambda item: f'{item[0]} ↳ Ordered {item[1]} pcs = {item[0].get_price() * item[1]} UAH',
            zip(self.__added_cart_items, self.__cart_items_qty))
        )

        return f'\n{self.cart_customer}\n{res}' \
               f'\n\n{20*"*"}\n\n' \
               f'Total: {self.cart_total()} UAH'

