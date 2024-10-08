from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self, *args, **kwargs):
        pass

    @abstractmethod
    def __add__(self, *args, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
