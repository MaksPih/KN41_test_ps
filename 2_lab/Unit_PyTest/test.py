import unittest
from random import choice, randint
from app import Figure  # Імпортуємо клас Figure з файлу app.py

# test.py (оновлений код з тестом для периметра)
class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконується лише раз на початку тестів"""
        pass
    
    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест"""
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        """Тестуємо правильність типу фігури"""
        self.assertEqual(self.figure, self.obj.get_figure_type)

    def test_figure_length(self):
        """Тестуємо правильність довжини фігури"""
        self.assertEqual(self.length, self.obj.get_figure_length)
    
    def test_perimeter(self):
        """Тестуємо правильність обчислення периметра"""
        if self.obj.get_figure_type == "квадрат":
            self.assertEqual(self.obj.get_perimeter(), 4 * self.length)
        elif self.obj.get_figure_type == "прямокутник":
            self.assertEqual(self.obj.get_perimeter(), 2 * self.length + 2 * self.length)

    def test_obj(self):
        """Тестуємо створення об'єкта з недозволеними параметрами"""
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

if __name__ == '__main__':
    unittest.main()