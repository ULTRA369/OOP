import pytest

from src.product import Product


def test_product_init_tomato(product_obj_tomato):
    assert product_obj_tomato.name == "Помидор"
    assert product_obj_tomato.description == "Синьор Помидор"
    assert product_obj_tomato.price == 150.00
    assert product_obj_tomato.quantity == 5


def test_product_init_cucumber(product_obj_cucumber):
    assert product_obj_cucumber.name == "Огурец"
    assert product_obj_cucumber.description == "Мистер Кукумбер"
    assert product_obj_cucumber.price == 120.00
    assert product_obj_cucumber.quantity == 3


def test_product_zero_quantity():
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_product_new_product():
    obj_potato = Product.new_product({"name": "Кабачок", "description": "Дядя Кабачок", "price": 50, "quantity": 20})
    assert obj_potato.name == "Кабачок"
    assert obj_potato.description == "Дядя Кабачок"
    assert obj_potato.price == 50
    assert obj_potato.quantity == 20


def test_product_new_product_replica():
    obj_carrot_1 = Product.new_product({"name": "Морковь", "description": "Мисс Морковь", "price": 70, "quantity": 10})
    assert obj_carrot_1.price == 70
    assert obj_carrot_1.quantity == 10

    obj_carrot_2 = Product.new_product({"name": "Морковь", "description": "Мисс Морковь", "price": 30, "quantity": 5})
    assert obj_carrot_2.price == 70
    assert obj_carrot_2.quantity == 15
    assert obj_carrot_1.price == 70
    assert obj_carrot_1.quantity == 15

    obj_carrot_3 = Product.new_product(
        {"name": "Морковь", "description": "Мисс Морковь", "price": 100, "quantity": 15}
    )
    assert obj_carrot_1.price == 100
    assert obj_carrot_2.price == 100
    assert obj_carrot_3.price == 100
    assert obj_carrot_1.quantity == 30
    assert obj_carrot_2.quantity == 30
    assert obj_carrot_3.quantity == 30

    obj_carrot_3.price = 1000
    assert obj_carrot_1.price == 1000
    assert obj_carrot_2.price == 1000
    assert obj_carrot_3.price == 1000


def test_product_price(product_obj_tomato):
    assert product_obj_tomato.price == 150.00
    product_obj_tomato.price = 180
    assert product_obj_tomato.price == 180
    product_obj_tomato.price = -1
    assert product_obj_tomato.price == 180
    product_obj_tomato.price = 0
    assert product_obj_tomato.price == 180


def test_product_smartphone(product_smartphone1, product_smartphone2, product_smartphone3):
    assert product_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone1.price == 180000.0
    assert product_smartphone1.quantity == 5
    assert product_smartphone1.efficiency == 95.5
    assert product_smartphone1.model == "S23 Ultra"
    assert product_smartphone1.memory == 256
    assert product_smartphone1.color == "Серый"

    assert product_smartphone2.name == "Iphone 15"
    assert product_smartphone2.description == "512GB, Gray space"
    assert product_smartphone2.price == 210000.0
    assert product_smartphone2.quantity == 8
    assert product_smartphone2.efficiency == 98.2
    assert product_smartphone2.model == "15"
    assert product_smartphone2.memory == 512
    assert product_smartphone2.color == "Gray space"

    assert product_smartphone3.name == "Xiaomi Redmi Note 11"
    assert product_smartphone3.description == "1024GB, Синий"
    assert product_smartphone3.price == 31000.0
    assert product_smartphone3.quantity == 14
    assert product_smartphone3.efficiency == 90.3
    assert product_smartphone3.model == "Note 11"
    assert product_smartphone3.memory == 1024
    assert product_smartphone3.color == "Синий"


def test_product_lawn_grass(product_grass1, product_grass2):
    assert product_grass1.name == "Газонная трава"
    assert product_grass1.description == "Элитная трава для газона"
    assert product_grass1.price == 500.0
    assert product_grass1.quantity == 20
    assert product_grass1.country == "Россия"
    assert product_grass1.germination_period == "7 дней"
    assert product_grass1.color == "Зеленый"

    assert product_grass2.name == "Газонная трава 2"
    assert product_grass2.description == "Выносливая трава"
    assert product_grass2.price == 450.0
    assert product_grass2.quantity == 15
    assert product_grass2.country == "США"
    assert product_grass2.germination_period == "5 дней"
    assert product_grass2.color == "Темно-зеленый"


def test_product_add(
    product_obj_tomato, product_obj_cucumber, product_smartphone1, product_smartphone2, product_grass1, product_grass2
):
    assert product_obj_tomato + product_obj_cucumber == 1110.0
    assert product_smartphone1 + product_smartphone2 == 2580000.0
    assert product_grass1 + product_grass2 == 16750.0
    with pytest.raises(TypeError):
        res = product_obj_tomato + product_smartphone1
        print(res)
    with pytest.raises(TypeError):
        res = product_smartphone1 + product_grass1
        print(res)
    with pytest.raises(TypeError):
        res = product_obj_tomato + product_grass1
        print(res)
    with pytest.raises(TypeError):
        res = product_obj_tomato + 1
        print(res)
