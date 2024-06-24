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


emp_1 = Category("фрукты", "отечественные", ["яблоки", "слива", "груша"])
emp_2 = Product("яблоки", "отечественные", 15.5, 55)
emp_3 = Category.number_of_categories
emp_4 = Category.number_of_unique_products

