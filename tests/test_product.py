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

    obj_carrot_3 = Product.new_product({"name": "Морковь", "description": "Мисс Морковь", "price": 100, "quantity": 15})
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