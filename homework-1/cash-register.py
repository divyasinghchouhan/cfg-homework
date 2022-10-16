"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = {} # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, name, price):
        self.total_items[name.capitalize()] = price
        self.total_price += price

        print('{:<20} {:<10.2f}'.format(name.capitalize(), price))

    def remove_item(self, name):
        try:
            removed = self.total_items.pop(name.capitalize())
        except KeyError:
            print("Item not found.")
        else:
            self.total_price -= removed
            item_cancelled = f"*CANCELLED* {name.capitalize()}"
            price_item_cancelled = f"–{removed:.2f}"
            print('{:<18} {:<10}'.format(item_cancelled, price_item_cancelled))

    def apply_discount(self, discount_percentage):
        self.discount = self.total_price * discount_percentage / 100

    def get_total(self):
        print('-------------------------------------------')

        # printing the sub total, discount and final total
        print('{:<20} £{:<10.2f}'.format('Total Price', self.total_price))
        print('{:<20} £{:<10.2f}'.format('Discount', self.discount))
        print('-------------------------------------------')
        print('{:<20} £{:<10.2f}'.format('Final Price :', self.total_price - self.discount))

    def show_items(self):
        for item in self.total_items:
            print('{:<20} {:<10.2f}'.format(item, self.total_items.get(item)))

        print('-------------------------------------------')
        # printing the sub total, discount and final total, properly formatted
        print('{:<20} £{:<10.2f}'.format('Total', self.total_price))
        print('{:<20} £{:<10.2f}'.format('Discount', self.discount))
        print('-------------------------------------------')
        print('{:<20} £{:<10.2f}'.format('Final', self.get_total()))

    def reset_register(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0


# EXAMPLE code run:

# ADD
if __name__ == '__main__':
    # creating a new register
    my_register1 = CashRegister()
    # adding some items to the register
    print('{:<20} {:<10}'.format('Item', 'Price'))
    my_register1.add_item('Milk', 1.00)
    my_register1.add_item('Bread', 1.50)
    my_register1.add_item('Apples', 1.00)
    my_register1.add_item('Bananas', 1.00)
    # removing 'Bananas' from the register, and updating the price
    my_register1.remove_item('Bananas')
    # applying a 15% discount to total price
    my_register1.apply_discount(15)
    my_register1.get_total()