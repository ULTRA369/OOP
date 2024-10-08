def test_mixin_print(capsys, product_obj_tomato, product_smartphone1, product_grass1):
    assert capsys.readouterr().out == (
        "Product('Помидор', 'Синьор Помидор', 150.0, 5)\n"
        "Smartphone('Samsung Galaxy S23 Ultra', '256GB,"
        " Серый цвет, 200MP камера', 180000.0, 5)\n"
        "LawnGrass('Газонная трава', 'Элитная трава для газона', 500.0, 20)\n"
    )
