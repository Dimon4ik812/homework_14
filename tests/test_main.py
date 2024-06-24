import unittest

import pytest

from src.main import Category, Product


@pytest.fixture
def category_fruits():
    return Category("фрукты", "отечественные", ["яблоки", "слива", "груша"])


@pytest.fixture
def product_apple():
    return Product("яблоки", "отечественные", 15.5, 55)


def test_category(category_fruits):
    assert category_fruits.name == "фрукты"
    assert category_fruits.description == "отечественные"
    assert category_fruits.goods == ["яблоки", "слива", "груша"]


def test_product(product_apple):
    assert product_apple.name == "яблоки"
    assert product_apple.description == "отечественные"
    assert product_apple.price == 15.5
    assert product_apple.quantity == 55


class TestCategory(unittest.TestCase):

    def test_number_of_categories(self):
        initial_count = Category.number_of_categories
        category = Category("овощи", "отечественные", ["морковь", "картофель", "лук"])
        self.assertEqual(Category.number_of_categories, initial_count + 1)
