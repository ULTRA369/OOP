from src.category import Category


def test_category(category_obj_vegetables, product_obj_potato):
    assert category_obj_vegetables.name == "Овощи"
    assert category_obj_vegetables.description == "Полезные штучки"
    assert category_obj_vegetables.products == (
        "Помидор, 150.0 руб. Остаток: 5 шт.\n" "Огурец, 120.0 руб. Остаток: 3 шт.\n"
    )

    assert Category.category_count == 1
    assert category_obj_vegetables.category_count == 1
    assert Category.product_count == 2
    assert category_obj_vegetables.product_count == 2

    category_obj_vegetables.add_product(product_obj_potato)
    assert Category.category_count == 1
    assert category_obj_vegetables.category_count == 1
    assert Category.product_count == 3
    assert category_obj_vegetables.product_count == 3

    assert category_obj_vegetables.products == (
        "Помидор, 150.0 руб. Остаток: 5 шт.\n"
        "Огурец, 120.0 руб. Остаток: 3 шт.\n"
        "Картофель, 50 руб. Остаток: 20 шт.\n"
    )