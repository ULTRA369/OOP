from src.category import Category


class IterProductsInCategory:
    """Класс для итерации по продуктам в переданной категории"""

    def __init__(self, category: Category) -> None:
        """Конструктор для класса итерации"""
        products_list = category.products.split("\n")
        products_list.remove("")
        self.products_list = products_list
        self.index = 0

    def __iter__(self):
        """Метод, возвращающий итератор"""
        self.index = 0
        return self

    def __next__(self) -> str:
        """Метод, определяющий, что возвращается при каждом шаге итерации"""
        if self.index < len(self.products_list):
            result = self.products_list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
