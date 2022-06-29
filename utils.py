from classes.exceptions import *


class Move:
    def __init__(self, product, amount, from_, to):
        self.product = product
        self.amount = amount
        self.from_ = from_
        self.to = to

    def find_product_in(self, place):
        try:
            place.remove(self.product, self.amount)
            print(f'\nНужное количество есть в "{self.from_}"')
        except (StorageFull, NoRequiredQuantity, NotFound) as error:
            print(error)
            return ''

    def move_product_to(self, place):
        try:
            place.add(self.product, self.amount)
            print(f'Курьер забрал {self.amount} "{self.product}" из "{self.from_}" и везет в "{self.to}"')
            print(f'Курьер доставил {self.amount} "{self.product}" в "{self.to}"')
        except (StorageFull, MaxUnique) as error:
            print(error)
            return ''



