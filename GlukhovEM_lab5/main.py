"""Учет страховых поступлений (запись о доходе) для лабораторной работы № 5."""

import re
from datetime import datetime


class Income:
    """Хранит дату, источник и сумму одного дохода."""

    def __init__(self, date, source, amount):
        self.date = date
        self.source = source
        self.amount = amount

    def show(self):
        """Выводит данные о доходе на экран."""
        print(f"Дата: {self.date.strftime('%Y.%m.%d')}")
        print(f"Источник: {self.source}")
        print(f"Сумма: {self.amount}")


class IncomeParser:
    """Проверяет входную строку и создает объект Income."""

    PATTERN = re.compile(
        r'^Доходы\s+(\d{4}\.\d{2}\.\d{2})\s+"((?:[^"\\]|\\")*)"\s+([+-]?\d+)$'
    )

    def parse(self, text):
        """Преобразует строку в Income или вызывает ValueError."""
        match = self.PATTERN.fullmatch(text.strip())
        if match is None:
            raise ValueError("Неверный формат строки")

        date_text, source_text, amount_text = match.groups()
        date = datetime.strptime(date_text, "%Y.%m.%d")
        if date.strftime("%Y.%m.%d") != date_text:
            raise ValueError("Дата должна иметь формат ГГГГ.ММ.ДД")
        if not source_text.strip():
            raise ValueError("Источник дохода не может быть пустым")

        source = source_text.replace('\\"', '"')
        return Income(date, source, int(amount_text))


class IncomeApp:
    """Организует ввод, проверку и вывод данных."""

    def __init__(self):
        self.parser = IncomeParser()

    def run(self):
        """Читает одну строку и сообщает об ошибке, если она есть."""
        try:
            text = input("Введите данные о доходе:\n")
            income = self.parser.parse(text)
        except ValueError as error:
            print("Ошибка:", error)
            return
        except EOFError:
            print("Ошибка: ввод не получен")
            return

        print("\nТип объекта: Доходы")
        income.show()


if __name__ == "__main__":
    IncomeApp().run()
