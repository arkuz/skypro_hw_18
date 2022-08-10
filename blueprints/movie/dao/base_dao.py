from abc import ABC, abstractmethod


class BaseDAO(ABC):

    @abstractmethod
    def get_one(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def update(self, id: int, data: dict):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
