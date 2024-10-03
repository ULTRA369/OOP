from unittest.mock import patch

from src.utils import get_obj_from_data, read_json


@patch("json.load")
@patch("builtins.open")
def test_read_json(mock_open, mock_load):
    mock_load.return_value = [1, 2, 3]
    assert read_json("") == [1, 2, 3]


def test_get_obj_from_data():
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации,"
            " но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром,"
            " станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
    obj_list = get_obj_from_data(data)
    assert obj_list[0].name == "Смартфоны"
    assert obj_list[0].description == (
        "Смартфоны, как средство не только коммуникации," " но и получение дополнительных функций для удобства жизни"
    )
    assert obj_list[0].products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
    assert obj_list[1].name == "Телевизоры"
    assert obj_list[1].description == (
        "Современный телевизор, который позволяет наслаждаться просмотром," " станет вашим другом и помощником"
    )
    assert obj_list[1].products == """55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"""