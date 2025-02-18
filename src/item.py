import csv
import os
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    DATA_DIR = Path(__file__).parent.joinpath("items.csv")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        # super.__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return None

    @classmethod
    def instantiate_from_csv(cls):
        '''класс-метод, инициализирующий
        экземпляры класса Item данными
        из файла src/items.csv'''

        try:
            with cls.DATA_DIR.open(newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['name'], row['price'], row['quantity'])
                    name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    cls(name, price, quantity)
            return cls
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except KeyError:
            raise InstantiateCSVError



    @staticmethod
    def string_to_number(string):
        '''статический метод, возвращающий число из числа-строки'''
        int_string = int(float(string))
        return int_string

    @property
    def name(self):
        '''добавить геттер для name'''
        return self.__name

    @name.setter
    def name(self, name_new):
        '''в сеттере name проверять,
         что длина наименования товара
         не больше 10 симвовов. В противном случае,
         взващает None.'''
        if len(name_new) > 10:
            None
        else:
            self.__name = name_new

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


class InstantiateCSVError(Exception):

    def __init__(self):
        self.message = 'Файл item.csv поврежден'

        super().__init__(self.message)

    def __str__(self):
        return self.message
