import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from test_data import DataBurger


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataBurger.INGREDIENT_NAME, DataBurger.INGREDIENT_PRICE)

        assert ingredient.get_price() == DataBurger.INGREDIENT_PRICE

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataBurger.INGREDIENT_NAME, DataBurger.INGREDIENT_PRICE)

        assert ingredient.get_name() == DataBurger.INGREDIENT_NAME

    @pytest.mark.parametrize(
        'type_ingredient, expected_type',
        [
            [INGREDIENT_TYPE_SAUCE, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'FILLING']
        ]
    )
    def test_get_type(self, type_ingredient, expected_type):
        ingredient = Ingredient(type_ingredient, 'TestIngredient', 10000)

        assert ingredient.get_type() == expected_type
