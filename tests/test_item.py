"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


class TestItem():
    pay_rate = 0.5
    all = []
    def test_calculate_total_price(self):
        sc1 = Item('Утюг', 1200, 10)
        assert sc1.calculate_total_price() == 12000
        assert sc1.calculate_total_price() != 1200


def test_apply_discount():
    sc1 = Item('Утюг', 1200, 10)
    Item.pay_rate = 0.5
    sc1.apply_discount()
    assert sc1.price == 600