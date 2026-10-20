"""Модульные тесты разбора входных данных."""

import unittest
from datetime import datetime
from unittest.mock import patch

from main import IncomeApp, IncomeParser


class TestIncomeParser(unittest.TestCase):
    """Проверяет корректный и некорректный ввод."""

    def setUp(self):
        self.parser = IncomeParser()

    def test_correct_input(self):
        income = self.parser.parse('Доходы 2026.10.20 "Зарплата" 70000')
        self.assertEqual(income.date, datetime(2026, 10, 20))
        self.assertEqual(income.source, "Зарплата")
        self.assertEqual(income.amount, 70000)

    def test_source_with_spaces(self):
        income = self.parser.parse('Доходы 2026.10.20 "Премия за работу" 30000')
        self.assertEqual(income.source, "Премия за работу")

    def test_extra_spaces(self):
        income = self.parser.parse('  Доходы   2026.10.20  "Подарок"   100  ')
        self.assertEqual(income.amount, 100)

    def test_escaped_quotes(self):
        income = self.parser.parse('Доходы 2026.10.20 "ООО \\"Вектор\\"" 10')
        self.assertEqual(income.source, 'ООО "Вектор"')

    def test_zero_amount(self):
        self.assertEqual(self.parser.parse('Доходы 2026.10.20 "Подарок" 0').amount, 0)

    def test_negative_amount(self):
        self.assertEqual(self.parser.parse('Доходы 2026.10.20 "Возврат" -500').amount, -500)

    def test_leap_day(self):
        income = self.parser.parse('Доходы 2024.02.29 "Подарок" 100')
        self.assertEqual(income.date.day, 29)

    def test_large_amount(self):
        value = 10**40
        income = self.parser.parse(f'Доходы 2026.10.20 "Подарок" {value}')
        self.assertEqual(income.amount, value)

    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Расходы 2026.10.20 "Покупка" 1000')

    def test_wrong_date(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Доходы 2026.13.40 "Зарплата" 70000')

    def test_short_date(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Доходы 2026.1.2 "Зарплата" 70000')

    def test_wrong_amount(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Доходы 2026.10.20 "Зарплата" abc')

    def test_missing_fields(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Доходы 2026.10.20')

    def test_missing_quotes(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Доходы 2026.10.20 Зарплата 70000')

    def test_unescaped_quotes(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Доходы 2026.10.20 "ООО "Вектор"" 100')

    def test_empty_source(self):
        with self.assertRaises(ValueError):
            self.parser.parse('Доходы 2026.10.20 "" 100')

    def test_app_error(self):
        with patch('builtins.input', return_value='неверный ввод'):
            with patch('builtins.print') as output:
                IncomeApp().run()
        self.assertIn('Ошибка:', output.call_args.args[0])

    def test_app_eof(self):
        with patch('builtins.input', side_effect=EOFError):
            with patch('builtins.print') as output:
                IncomeApp().run()
        self.assertIn('Ошибка:', output.call_args.args[0])


if __name__ == '__main__':
    unittest.main()
