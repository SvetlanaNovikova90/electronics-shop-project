from src.item import Item


class Mixin:
    """Класс-миксин для изменения раскладки клавиатуры"""

    @property
    def language(self):
        return self._language

    _language: str = "EN"

    @property
    def language(self):
        """атрибут language"""
        return self._language

    def change_lang(self):
        """Изменение атрибута language"""
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'

    @language.setter
    def language(self, value):
        """Проверка на Принадлежность языка к ['EN', 'RU']"""
        if value in ['EN', 'RU']:
            self._language = value
        else:
            raise "AttributeError: property 'language' of 'Keyboard' object has no setter"



class Keyboard(Item, Mixin):
    pass
