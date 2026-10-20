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


def main():
    text = input("Введите данные о доходе:\n")

    object_type, date_text, rest = text.split(maxsplit=2)
    source_text, amount_text = rest.rsplit(maxsplit=1)

    source = source_text[1:-1].replace('\\"', '"')
    date = datetime.strptime(date_text, "%Y.%m.%d")
    amount = int(amount_text)

    income = Income(date, source, amount)

    print("\nТип объекта:", object_type)
    income.show()


if __name__ == "__main__":
    main()
