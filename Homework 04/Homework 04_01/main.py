"""
1. Рознесіть класи, які використовували під час вирішення завдання про замовлення та групу студентів по модулям.
Переконайтеся у працездатності проєктів. """

import item
import customer
import cart


# 'entry point'
if __name__ == '__main__':

    # creating some e-store items
    item_001 = item.StoreItem('Electrical devices', 'MCB Eaton 16A', 200.00)
    item_002 = item.StoreItem('Electrical instruments', 'UNIT UT61 Multimeter', 1500.00)
    item_003 = item.StoreItem('LED lighting', 'E28 10W light lamp', 50.00)

    item_001.set_price(300.00)

    # creating customer instance
    customer_info = customer.StoreCustomer('X-men','Woolverine','+123456369')

    # ordering some items, adding to the shopping cart
    order = cart.ShoppingCart(customer_info)
    order.add_item(item_001, 3)
    order.add_item(item_002, 1)
    order.add_item(item_003, 5)

    # print order total bill
    print(order)