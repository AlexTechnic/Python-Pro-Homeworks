""" Модифікуєте клас Замовлення (завдання Лекції 1), додавши реалізацію протоколу послідовностей та ітераційного
протоколу. """


class PriceTypeError(Exception):
    """
    Custom exception class for StoreItem class.
    """
    def __init__(self, item_name, item_price):
        self._item_name = item_name
        self._item_price = item_price

    def __str__(self):
        return f'Item "{self._item_name}" price type error: price type cant be <{str(type(self._item_price))}>. ' \
               f'Expected float type in format "1234.00".'


class ZeroPriceError(Exception):
    """
    Custom exception class for StoreItem class.
    """
    def __init__(self, item_name, item_price):
        self._item_name = item_name
        self._item_price = item_price

    def __str__(self):
        return f'Item "{self._item_name}" price <= 0 error: price cant be <{self._item_price}>. '


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
        self._item_category = item_category
        self._item_name = item_name

        # do check of input value BEFORE assign to 'self._item_price'
        if not isinstance(item_price, float):
            raise PriceTypeError(self._item_name, item_price)
        if item_price <= 0:
            raise ZeroPriceError(self._item_name, item_price)
        self._item_price = item_price

    def set_price(self, item_price):
        self._item_price = item_price

        if not isinstance(item_price, float):
            raise PriceTypeError(self._item_name, self._item_price)
        if item_price <= 0:
            raise ZeroPriceError(self._item_name, self._item_price)

    def get_price(self):
        return self._item_price

    def __str__(self):
        return f'\nItem category: {self._item_category} \n' \
               f'name: {self._item_name} \n' \
               f'price: {self._item_price} \n'


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
        return f'{self.customer_name} {self.customer_surname}, phone: {self.customer_phone}'


class ShoppingCart:
    def __init__(self, cart_customer: StoreCustomer):
        """
        Class that process adding items to e-store shopping cart by some customer,
        making total sum of goods and printing bill.

        Parameters
        ----------
        cart_customer
            Can be any customer instance from class StoreCustomer.
        """
        self.cart_customer = cart_customer
        self._added_cart_items = []
        self._cart_items_qty = []
        self.index = 0

    def add_item(self, cart_item: StoreItem, quantity: int = 1):
        if cart_item in self._added_cart_items:
            index = self._added_cart_items.index(cart_item)
            self._cart_items_qty[index] += quantity
        else:
            self._added_cart_items.append(cart_item)
            self._cart_items_qty.append(quantity)

    def cart_total(self):
        """ return float type sum value of all gathered items """
        return sum(item.get_price() * self._cart_items_qty[index] for index, item in enumerate(self._added_cart_items))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self._added_cart_items):
            self.index += 1
            return self._added_cart_items[self.index - 1]
        raise StopIteration

    def __str__(self):
        """ return total and sub-total bill for each item in shopping cart """
        res = '\n'.join(map(
            lambda item: f'{item[0]} ↳ Ordered {item[1]} pcs = {item[0].get_price() * item[1]} UAH',
            zip(self._added_cart_items, self._cart_items_qty))
        )

        return f'\n{self.cart_customer}\n{res}' \
               f'\n\n{20*"*"}\n\n' \
               f'Total: {self.cart_total()} UAH'


# 'entry point'
if __name__ == '__main__':

    # creating some e-store items
    item_001 = StoreItem('Electrical devices', 'MCB Eaton 16A', 200.00)
    item_002 = StoreItem('Electrical instruments', 'UNIT UT61 Multimeter', 1500.00)
    item_003 = StoreItem('LED lighting', 'E28 10W light lamp', 50.00)

    item_001.set_price(300.00)

    # creating customer instance
    customer_01 = StoreCustomer('X-men','Woolverine','+123456369')

    # ordering some items, adding to the shopping cart
    customer_01_order: ShoppingCart = ShoppingCart(customer_01)
    customer_01_order.add_item(item_001, 3)
    customer_01_order.add_item(item_002, 1)
    customer_01_order.add_item(item_003, 5)

    # printing order items one-by-one with '__next__' iteration
    def customer_01_order_next():
        try:
            res = f'Customer {str(customer_01)}, next ordered item: {customer_01_order.__next__()}'
            return res
        except:
            end_of_order = f'Exception: reached end of order list, please reset __next__ index.'
            return end_of_order

    print(customer_01_order_next())
    print(customer_01_order_next())
    print(customer_01_order_next())
    print(customer_01_order_next())
    print(customer_01_order_next())
    print(customer_01_order_next())
    print('')

    # printing order items one-by-one with 'for' iteration
    def pause():  # define some 'pause' in output
        res = input(f'To print next item '
                    f'from customer {customer_01.customer_name} {customer_01.customer_surname} order list '
                    f'press enter: ')
        return res

    qty_index = 0

    for order_item in customer_01_order:
        pause()
        print(f'Ordered {order_item._item_name}, '  # not good implementation with protected attributes of class 'item'
              f'price {order_item._item_price} UAH, '
              f'qty {customer_01_order._cart_items_qty[qty_index]}, '
              f'subtotal = {(customer_01_order._cart_items_qty[qty_index]) * order_item._item_price} UAH\n')
        qty_index += 1

    qty_index = 0

    # print order total bill
    input('To print total order bill press enter: ')
    print(f'\nTotal order:{customer_01_order}')

