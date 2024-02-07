from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        if not isinstance(number_of_sim, int):
            raise ValueError ('Количество физических SIM-карт должно быть целым числом больше нуля.')
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim2):
        if not isinstance(number_of_sim2, int):
            raise ValueError ('Количество физических SIM-карт должно быть целым числом больше нуля.')
        if number_of_sim2 <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.number_of_sim = number_of_sim2



    def __repr__(self):
        return f'"{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})"'

    def __str__(self):
        return f'{self.name}'

