from src.item import Item


class Mixin:
    """Класс-миксин для изменения раскладки клавиатуры"""

    def change_lang(self):
        """Изменение атрибута language"""
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, Mixin):
    _language: str = "EN"

    @property
    def language(self):
        """атрибут language"""
        return self._language
