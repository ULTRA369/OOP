from src.classes_description import Product, Category

import pytest

def test_category(
    category_obj_vegetables, product_obj_potato, category_smartphones, category_grass, product_smartphone3
):
    assert category_obj_vegetables.name == "Овощи"
    assert category_obj_vegetables.description == "Полезные штучки"
    assert category_obj_vegetables.products == (
        "Помидор, 150.0 руб. Остаток: 5 шт.\n" "Огурец, 120.0 руб. Остаток: 3 шт.\n"
    )

    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Высокотехнологичные смартфоны"
    assert category_smartphones.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )

    assert category_grass.name == "Газонная трава"
    assert category_grass.description == "Различные виды газонной травы"
    assert category_grass.products == (
        "Газонная трава, 500.0 руб. Остаток: 20 шт.\n" "Газонная трава 2, 450.0 руб. Остаток: 15 шт.\n"
    )

    assert Category.category_count == 3
    assert category_obj_vegetables.category_count == 3
    assert Category.product_count == 6
    assert category_obj_vegetables.product_count == 6
    category_obj_vegetables.add_product(product_obj_potato)
    category_smartphones.add_product(product_smartphone3)
    assert Category.category_count == 3
    assert category_obj_vegetables.category_count == 3
    assert Category.product_count == 8
    assert category_obj_vegetables.product_count == 8
    with pytest.raises(TypeError):
        category_obj_vegetables.add_product(1)
    with pytest.raises(TypeError):
        category_smartphones.add_product("1")
    with pytest.raises(TypeError):
        category_grass.add_product(category_smartphones)

    assert category_obj_vegetables.products == (
        "Помидор, 150.0 руб. Остаток: 5 шт.\n"
        "Огурец, 120.0 руб. Остаток: 3 шт.\n"
        "Картофель, 50 руб. Остаток: 20 шт.\n"
    )
    assert category_smartphones.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
    assert category_grass.products == (
        "Газонная трава, 500.0 руб. Остаток: 20 шт.\n" "Газонная трава 2, 450.0 руб. Остаток: 15 шт.\n"
    )

    assert str(category_obj_vegetables) == "Овощи, количество продуктов: 28 шт."
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 27 шт."
    assert str(category_grass) == "Газонная трава, количество продуктов: 35 шт."

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

    def test_product_new_product():
        obj_potato = Product.new_product(
            {"name": "Кабачок", "description": "Дядя Кабачок", "price": 50, "quantity": 20})
        assert obj_potato.name == "Кабачок"
        assert obj_potato.description == "Дядя Кабачок"
        assert obj_potato.price == 50
        assert obj_potato.quantity == 20

    def test_product_new_product_replica():
        obj_carrot_1 = Product.new_product(
            {"name": "Морковь", "description": "Мисс Морковь", "price": 70, "quantity": 10})
        assert obj_carrot_1.price == 70
        assert obj_carrot_1.quantity == 10

        obj_carrot_2 = Product.new_product(
            {"name": "Морковь", "description": "Мисс Морковь", "price": 30, "quantity": 5})
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
            product_obj_tomato, product_obj_cucumber, product_smartphone1, product_smartphone2, product_grass1,
            product_grass2
    ):
        assert product_obj_tomato + product_obj_cucumber == 1110.0
        assert product_smartphone1 + product_smartphone2 == 2580000.0
        assert product_grass1 + product_grass2 == 16750.0
        with pytest.raises(TypeError):
            res = product_obj_tomato + product_smartphone1
        with pytest.raises(TypeError):
            res = product_smartphone1 + product_grass1
        with pytest.raises(TypeError):
            res = product_obj_tomato + product_grass1
        with pytest.raises(TypeError):
            res = product_obj_tomato + 1