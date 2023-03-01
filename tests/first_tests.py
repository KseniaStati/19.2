from app.calculator import Calculator
import pytest

class TestCalc:
    def setup(self):
        self.calc = Calculator
    # корректные значение
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 3, 2) == 5

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 3) == 2

    # негативный тест

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 9, 3) == 6

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 2) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 3, 2) == 6

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 2) == 2