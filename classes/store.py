from classes.parent_class import ParentClass


class Store(ParentClass):
    """Класс склада"""
    def __init__(self, capacity=100, items={}):
        super().__init__(items, capacity)
        self._capacity = capacity
        self._items = items
