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

        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def apply_discount(self):
        pass

    def get_total(self):
        pass

    def show_items(self):
        pass

    def reset_register(self):
        pass


# EXAMPLE code run:

# ADD