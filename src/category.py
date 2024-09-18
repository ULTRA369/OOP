from src.product import Product

class Category:
    name: str                    # Имя
    description: str             # Описание
    products: list               # Cписок товаров категории


def __init__(self, name, description, products):
    self.name = name
    self.description = description
    self.products = products