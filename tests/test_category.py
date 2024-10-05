import pytest

from src.category import Category


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