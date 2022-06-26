from classes.storage import Storage
from classes.exceptions import *


class ParentClass(Storage):
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    def add(self, name: str, amount_added: int):
        """Добавляет товары в хранилище"""
        if sum(item for item in self._items.values()) < self._capacity:
            if name not in self._items.keys():
                self._items[name] = amount_added
            else:
                self._items[name] += amount_added
        else:
            raise StorageFull('Место заполнено!')

    def remove(self, name: str, amount: int):
        """Удаляет товары из хранилища"""
        if name not in self._items:
            raise NotFound(f'Товар "{name}" не найден')

        if self._items[name] > amount:
            self._items[name] -= amount
        elif self._items[name] == amount:
            del self._items[name]
        else:
            raise NoRequiredQuantity('Нужного количества нет на складе')

    def get_free_space(self) -> int:
        """Возвращает свободное место"""
        return self._capacity - sum(item for item in self._items.values())

    @property
    def get_items(self) -> dict:
        """Возвращает список товаров"""
        return self._items

    def get_unique_items_count(self) -> int:
        """Возвращает кол-во уникальных элементов"""
        return len(set([item for item in self.items.keys()]))
