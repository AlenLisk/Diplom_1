from praktikum.bun import Bun
from test_data import DataBun


class TestBun:
    def test_get_name(self):
        bun = Bun(DataBun.BUN_NAME, DataBun.BUN_PRICE)

        assert bun.get_name() == DataBun.BUN_NAME

    def test_get_price(self):
        bun = Bun(DataBun.BUN_NAME, DataBun.BUN_PRICE)

        assert bun.get_price() == DataBun.BUN_PRICE
