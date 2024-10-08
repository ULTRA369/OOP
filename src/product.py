from src.base_product import BaseProduct
from src.mixin_log import MixinLog


class Product(BaseProduct, MixinLog):
    """Класс для создания продуктов"""
    name: str
    description: str
    price: float
    quantity: int
    products_list: list = list()

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Конструктор создания продуктов"""
        if not quantity:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append(self)
        super().__init__()

    def __str__(self) -> str:
        """Метод для отображения при выводе в консоль и преобразования в строку"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> int | float:
        """Метод для сложения объектов, суммирует общую стоимость товара на остатках в категориях"""
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_param: dict):
        """
        Принимает словарь с ключами: "name"(название), "description"(описание),
        "price"(цена), "quantity"(количество на складе)
        """
        name, description, price, quantity = product_param.values()
        for product in cls.products_list:
            if product.name.lower() == name.lower():
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return product
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Метод для получения значения приватного атрибута __price"""
        return self.__price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Метод для изменения цены"""
        if new_price > 0:
            if new_price < self.__price:
                agreement = input(
                    "Старая цена товара выше введенной.\n"
                    "Вы уверены, что хотите снизить цену на товар?\n"
                    "y - да / n - нет\n"
                )
                if agreement.lower() != "y":
                    return
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    """Конструктор создания продуктов типа Смартфон"""
    def __init__(self, name: str, description: str, price: float | int, quantity: int, efficiency: float,
                 model: int | str, memory: int | float, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other) -> int | float:
        """Метод для сложения объектов, суммирует общую стоимость товара на остатках в категориях"""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class LawnGrass(Product):
    """Конструктор создания продуктов типа Трава для газона"""
    def __init__(self, name: str, description: str, price: float | int, quantity: int, country: str,
                 germination_period: str, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other) -> float | int:
        """Метод для сложения объектов, суммирует общую стоимость товара на остатках в категориях"""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
