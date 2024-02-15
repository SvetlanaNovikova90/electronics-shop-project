from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        '''Инициализация класса Phone'''
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_value):
        if not isinstance(new_value, int) or new_value <= 0:
            raise ValueError ('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = new_value









