from src.product import Product


class Category:
    name: str
    description: str
    products: list
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        products = ""
        for product in self.__products:
            p = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            products += p
        return products

    def add_product(self, product_to_add: Product):
        self.__products.append(product_to_add)
        Category.product_count += 1