from src.product import Product


class Category:
    """Класс для создания категорий товаров, в качестве списка товаров принимает список объектов класса Product"""
    name: str
    description: str
    products: list
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Конструктор класса Category"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Формат отображения при выводе в консоль и преобразования в строку"""
        products_count = 0
        for product in self.__products:
            products_count += product.quantity
        return f"{self.name}, количество продуктов: {products_count} шт."

    @property
    def products(self) -> str:
        """Атрибут для получения списка продуктов в формате строки"""
        products = ""
        for product in self.__products:
            p = f"{product}\n"
            products += p
        return products

    def add_product(self, product_to_add: Product) -> None:
        """Метод добавления нового продукта в список продуктов категории"""
        if isinstance(product_to_add, Product):
            self.__products.append(product_to_add)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        """Метод для получения средней цены товаров в категории"""
        list_prices = [product.price for product in self.__products]
        try:
            result = sum(list_prices) / len(list_prices)
        except ZeroDivisionError:
            return 0
        else:
            return round(result, 2)
