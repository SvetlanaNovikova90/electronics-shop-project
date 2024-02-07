"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


# class TestItem():
#     pay_rate = 0.5
#     all = []

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[0]

    assert item1.name == 'Stove'
    assert item1.price == '100'
    assert item1.quantity == '1'
    assert len(Item.all) == 5
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