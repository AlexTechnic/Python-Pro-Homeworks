"""
1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.

2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон тощо.

3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості. Замовлення має містити дані
про користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод str()
для коректного виведення інформації про це замовлення. """


class StoreItem:
    """ Return string with category, name and price of item that can be used in bills. """

    def __init__(self, item_category: str, item_name: str, item_price: float):
        self.item_category = item_category
        self.item_name = item_name
        self.item_price = item_price

    def __str__(self):
        return f'\nItem category: {self.item_category} \n' \
               f'name: {self.item_name} \n' \
               f'price: {self.item_price} \n'


class StoreCustomer:
    """ Return string with e-store customer information. """

    def __init__(self, customer_name: str, customer_surname: str, customer_phone: str):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_phone = customer_phone

    def __str__(self):
        return f'Customer name: {self.customer_name} {self.customer_surname}, phone: {self.customer_phone}'


class ShoppingCart:
    """Class for processing shopping cart, contain methods to calculate total.

    Return string with order bill information.
    """
    def __init__(self, cart_customer: StoreCustomer):
        self.cart_customer = cart_customer
        self.__added_cart_items = []
        self.__cart_items_qty = []

    def add_item(self, cart_item: StoreItem, quantity: int = 1):
        if cart_item in self.__added_cart_items:
            index = self.__added_cart_items.index(cart_item)
            self.__cart_items_qty[index] += quantity
        else:
            self.__added_cart_items.append(cart_item)
            self.__cart_items_qty.append(quantity)

    def cart_total(self):
        """ return shopping cart items price * quantity """
        return sum(item.item_price * self.__cart_items_qty[index] for index, item in enumerate(self.__added_cart_items))

    def __str__(self):
        """ return total and sub-total bill for each item in shopping cart """
        res = '\n'.join(map(
            lambda item: f'{item[0]} ↳ Ordered {item[1]} pcs = {item[0].item_price * item[1]} UAH',
            zip(self.__added_cart_items, self.__cart_items_qty))
        )

        return f'\n{self.cart_customer}\n{res}' \
               f'\n\n{20*"*"}\n\n' \
               f'Total: {self.cart_total()} UAH'


# 'entry point'
if __name__ == '__main__':

    # list of e-store items
    item_001 = StoreItem('Electrical devices', 'MCB Eaton 16A', 200)
    item_002 = StoreItem('Electrical instruments', 'UNIT UT61 Multimeter', 1500)
    item_003 = StoreItem('LED lighting', 'E28 10W light lamp', 50)

    # customer data input
    customer_info = StoreCustomer('X-men','Woolverine','+123456369')

    # order process, adding some items to the cart
    order = ShoppingCart(customer_info)
    order.add_item(item_001, 3)
    order.add_item(item_002, 1)
    order.add_item(item_003, 5)

    # total bill
    print(order)
