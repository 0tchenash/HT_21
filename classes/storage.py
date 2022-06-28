from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def add(self, name: str, amount: int):
        """Добавляет товары в хранилище"""
        pass

    @abstractmethod
    def remove(self, name: str, amount: int):
        """Удаляет товары из хранилища"""
        pass

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def get_items(self):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass
