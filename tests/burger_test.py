from test_data import DataBun
from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import *
from test_data import DataBurger


class TestBurger:
    def test_set_bun(self):
        mock = Mock()
        mock.get_name.return_value = DataBun.BUN_NAME
        mock.get_price.return_value = DataBun.BUN_PRICE
        burger = Burger()
        burger.set_buns(mock)

        assert burger.bun.get_name() == DataBun.BUN_NAME and burger.bun.get_price() == DataBun.BUN_PRICE

    def test_add_ingredient(self):
        mock = Mock()
        mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock.get_name.return_value = DataBurger.INGREDIENT_NAME
        mock.get_price.return_value = DataBurger.INGREDIENT_PRICE
        burger = Burger()
        burger.add_ingredient(mock)

        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE and burger.ingredients[
            0].get_name() == DataBurger.INGREDIENT_NAME and burger.ingredients[
                   0].get_price() == DataBurger.INGREDIENT_PRICE

    def test_remove_ingredient(self):
        mock = Mock()
        burger = Burger()
        burger.add_ingredient(mock)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        mock_1 = Mock()
        mock_2 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_1)
        burger.add_ingredient(mock_2)
        id_element_0 = id(burger.ingredients[0])

        burger.move_ingredient(0, 1)
        assert id(burger.ingredients[0]) != id_element_0

    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = DataBun.BUN_PRICE
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = DataBurger.INGREDIENT_PRICE
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == DataBurger.BURGER_PRICE

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = DataBun.BUN_NAME
        mock_bun.get_price.return_value = DataBun.BUN_PRICE
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = DataBurger.INGREDIENT_NAME
        mock_ingredient.get_price.return_value = DataBurger.INGREDIENT_PRICE
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_receipt() == DataBurger.RECEIPT
