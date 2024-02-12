from src.keyboard import Keyboard


def test_language():
    kb = Keyboard('Dark Project', 1000, 5)
    assert kb.language == 'EN'
    assert str(kb) == 'Dark Project'
    kb.language = 'RU'
    assert kb.language == 'RU'


def test_change_lang():
    kb2 = Keyboard('Project', 1000, 5)
    kb2.change_lang()
    assert str(kb2.language) == "RU"
    kb2.change_lang()
    assert str(kb2.language) == "EN"
