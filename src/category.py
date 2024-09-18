from src.product import Product

class Category:
    name: str                    # Имя
    description: str             # Описание
    products: list               # Cписок товаров категории
    product_count = 0            # Подсчет продуктов
    category_count = 0           # Подсчет категорий

def __init__(self, name, description, products):
    self.name = name
    self.description = description
    self.products = products
    Category.category_count += 1
    Category.product_count += len(products)

