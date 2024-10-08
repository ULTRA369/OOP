import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def product_obj_tomato():
    return Product("Помидор", "Синьор Помидор", 150.00, 5)


@pytest.fixture
def product_obj_cucumber():
    return Product("Огурец", "Мистер Кукумбер", 120.00, 3)


@pytest.fixture
def product_obj_potato():
    return Product("Картофель", "Дядя Картофель", 50, 20)


@pytest.fixture
def product_smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def product_smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_smartphone3():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def product_grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_obj_vegetables(product_obj_tomato, product_obj_cucumber):
    return Category("Овощи", "Полезные штучки", [product_obj_tomato, product_obj_cucumber])


@pytest.fixture
def category_smartphones(product_smartphone1, product_smartphone2):
    return Category("Смартфоны", "Высокотехнологичные смартфоны", [product_smartphone1, product_smartphone2])


@pytest.fixture
def category_grass(product_grass1, product_grass2):
    return Category("Газонная трава", "Различные виды газонной травы", [product_grass1, product_grass2])
