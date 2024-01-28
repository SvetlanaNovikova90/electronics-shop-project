import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_new):
        if len(name_new) > 10:
            self.__name = name_new[0:9]
        else:
            self.__name = name_new

    @classmethod
    def instantiate_from_csv(cls, date):
        with open(date, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print(reader)

    @staticmethod
    def string_to_number():
        return len(Item.all)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_cost_of_poduct = self.price * self.quantity
        return total_cost_of_poduct

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
