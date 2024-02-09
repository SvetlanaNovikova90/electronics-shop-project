import pytest

from src.phone import Phone


def test_repr():
    '''проврка правильности ввода информации для разработчиков'''
    phone1 = Phone("iPhone", 50_000, 3, 2)
    assert repr(phone1) == "Phone('iPhone', 50000, 3, 2)"
    assert repr(phone1) != "Phone('iPhone', 50000, 4, 2)"
    phone1.name = 'iPhone15'
    assert repr(phone1) == "Phone('iPhone15', 50000, 3, 2)"


def test_number_of_sim():
    '''правильный вывод сеттера'''
    phone2 = Phone("iPhone", 50_000, 3, 2)
    with pytest.raises(ValueError):
        phone2.number_of_sim = 0


def test_number_of_sim():
    phone3 = Phone("iPhone", 50_000, 3, 2)
    phone3.number_of_sim = 3
    assert phone3.number_of_sim == 3
    assert phone3.number_of_sim != 0
    assert str(phone3) == 'iPhone'



