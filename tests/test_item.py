"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


def test_str():
    item_str = Item('LapTop', 120000, 10)
    assert str(item_str) == 'LapTop'


def test_add():
    item_add = Item('LapTop', 120000, 10)
    phone_add = Phone("iPhone", 50000, 3, 2)
    assert item_add + phone_add == 13
    assert item_add + 10 is None


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[0]

    assert item1.name == 'Чайник'
    assert item1.price == 100
    assert item1.quantity == 25
    assert len(Item.all) == 8


def test_calculate_total_price():
    sc1 = Item('Утюг', 1200, 10)
    assert sc1.calculate_total_price() == 12000
    assert sc1.calculate_total_price() != 1200


def test_apply_discount():
    sc1 = Item('Утюг', 1200, 10)
    Item.pay_rate = 0.5
    sc1.apply_discount()
    assert sc1.price == 600


def test_string_to_number():
    assert Item.string_to_number('1') == 1
    assert Item.string_to_number('1.23') == 1
    assert Item.string_to_number('1.99') == 1


def test_name():
    item3 = Item('Чайник', "100", "25")
    assert item3.name == 'Чайник'
    name_new = "Чайник электрический"
    item3.name = name_new
    assert item3.name == 'Чайник'
    name_new_2 = "Термопод"
    item3.name = name_new_2
    assert item3.name == 'Термопод'


def test_repr():
    item3 = Item('Чайник', 100, 25)
    assert repr(item3) == "Item('Чайник', 100, 25)"


def test_str():
    item3 = Item('Чайник', 100, 25)
    assert str(item3) == 'Чайник'
