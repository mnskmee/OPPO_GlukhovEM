"""Исходный код практической работы № 3 (до улучшений)."""

from datetime import datetime


class Income:
    def __init__(self, date, source, amount):
        self.date = date
        self.source = source
        self.amount = amount

    def show(self):
        print(f"Дата: {self.date.strftime('%Y.%m.%d')}")
        print(f"Источник: {self.source}")
        print(f"Сумма: {self.amount}")


class IncomeParser:
    def parse(self, text):
        parts = text.split(maxsplit=2)
        if len(parts) != 3 or parts[0] != "Доходы":
            raise ValueError("Неверный тип объекта или формат строки")

        _, date_text, rest = parts
        source_text, amount_text = self.split_fields(rest)
        date = datetime.strptime(date_text, "%Y.%m.%d")
        return Income(date, self.get_source(source_text), int(amount_text))

    def split_fields(self, text):
        parts = text.rsplit(maxsplit=1)
        if len(parts) != 2:
            raise ValueError("Не указаны источник или сумма")
        return parts

    def get_source(self, text):
        if len(text) < 2 or not text.startswith('"') or not text.endswith('"'):
            raise ValueError("Источник должен быть в кавычках")
        return text[1:-1].replace('\\"', '"')


class IncomeApp:
    def __init__(self):
        self.parser = IncomeParser()

    def run(self):
        try:
            text = input("Введите данные о доходе:\n")
            income = self.parser.parse(text)
            print("\nТип объекта: Доходы")
            income.show()
        except ValueError as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    IncomeApp().run()
