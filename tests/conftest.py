import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_obj_tomato():
    return Product("Помидор", "Синьор Помидор", 150.00, 5)


@pytest.fixture
def product_obj_cucumber():
    return Product("Огурец", "Мистер Кукумбер", 120.00, 3)


@pytest.fixture
def category_obj_vegetables(product_obj_tomato, product_obj_cucumber):
    return Category("Овощи", "Полезные штучки", [product_obj_tomato, product_obj_cucumber])


@pytest.fixture
def product_obj_potato():
    return Product("Картофель", "Дядя Картофель", 50, 20)