from src.utils import open_read_json


class Category:
    """класс для категорий"""

    name: str
    description: str
    goods: list

    # общее количество категорий и общее количество уникальных продуктов
    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description, goods):
        """Метод для инициализации экземпляра класса, задаем значение атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.goods = goods

        Category.number_of_categories += 1
        Category.number_of_unique_products += 1


class Product:
    """класс для продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса, задаем значение атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# emp_1 = Category("фрукты", "отечественные", ["яблоки", "слива", "груша"])
emp_2 = Product("яблоки", "отечественные", 15.5, 55)
# emp_3 = Category.number_of_categories
# emp_4 = Category.number_of_unique_products

file_path = "../data/products.json"
result = open_read_json(file_path)
categories = []
for category_data in result:
    products = []
    for product_data in category_data["products"]:
        product = Product(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
        products.append(product)
    category = Category(name=category_data["name"], description=category_data["description"], goods=products)
    categories.append(category)

print(Category.number_of_categories)
print(Category.number_of_unique_products)
