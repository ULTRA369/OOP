class Product:
    name: str                    # Имя
    description: str             # Описание
    price: float                 # Цена
    quantity: int                # Rоличество в наличии
    products_list: list = list()


def __init__(self, name, description, price, quantity):
    self.name = name
    self.description = description
    self.price = price
    self.quantity = quantity
    Product.products_list.append(self)
