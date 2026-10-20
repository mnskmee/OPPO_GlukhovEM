
import unittest

from main import IncomeParser


class TestIncomeParser(unittest.TestCase):
    def setUp(self):
        self.parser = IncomeParser()

    def test_correct_input(self):
        income = self.parser.parse('Доходы 2026.10.20 "Зарплата" 70000')
        self.assertEqual(income.source, "Зарплата")
        self.assertEqual(income.amount, 70000)

    def test_source_with_spaces(self):
        income = self.parser.parse('Доходы 2026.10.20 "Премия за работу" 30000')
        self.assertEqual(income.source, "Премия за работу")

    def test_zero_amount(self):
        income = self.parser.parse('Доходы 2026.10.20 "Подарок" 0')
        self.assertEqual(income.amount, 0)

    def test_negative_amount(self):
        income = self.parser.parse('Доходы 2026.10.20 "Корректировка" -500')
        self.assertEqual(income.amount, -500)

    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Расходы 2026.10.20 "Покупка" 1000')

    def test_wrong_date(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Доходы 2026.13.40 "Зарплата" 70000')

    def test_wrong_amount(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Доходы 2026.10.20 "Зарплата" abc')

    def test_missing_fields(self):
        with self.assertRaises(ValueError):
            self.parser.parse("Доходы 2026.10.20")

    def test_missing_quotes(self):
        with self.assertRaises(ValueError):
            self.parser.parse("Доходы 2026.10.20 Зарплата 70000")


if __name__ == "__main__":
    unittest.main()
