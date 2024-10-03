import json

from src.category import Category
from src.product import Product


def read_json(file_path):
    with open(file_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def get_obj_from_data(data_list: list):
    category_list = []
    for category in data_list:
        products_list = []
        for product in category.get("products"):
            products_list.append(Product(**product))
        category["products"] = products_list
        category_list.append(Category(**category))
    return category_list
