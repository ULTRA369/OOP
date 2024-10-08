import pytest

from src.iter_category import IterProductsInCategory


def test_iter_category(category_obj_vegetables):
    iter_vegetables = IterProductsInCategory(category_obj_vegetables)

    assert iter_vegetables.products_list == ['Помидор, 150.0 руб. Остаток: 5 шт.', 'Огурец, 120.0 руб. Остаток: 3 шт.']
    assert iter_vegetables.index == 0

    assert next(iter_vegetables) == "Помидор, 150.0 руб. Остаток: 5 шт."
    assert iter_vegetables.index == 1

    assert next(iter_vegetables) == "Огурец, 120.0 руб. Остаток: 3 шт."
    with pytest.raises(StopIteration):
        next(iter_vegetables)
