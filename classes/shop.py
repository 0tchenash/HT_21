from classes.exceptions import *
from classes.parent_class import ParentClass


class Shop(ParentClass):
    """Класс магазина"""
    def __init__(self, unique=5):
        super().__init__(capacity=20, items={})
        # self._capacity = capacity
        # self._items = items
        self._unique = unique

    def add(self, name: str, amount: int):
        """Добавляет товары в магазин"""
        if self.get_free_space() < amount:
            raise StorageFull('Свободного места меньше, чем кол-во товара')
        elif name not in self._items and self.get_unique_items_count >= self._unique:
            raise MaxUnique('Превышен лимит уникальных товаров')

        self._items[name] = self._items.get(name, 0) + amount
