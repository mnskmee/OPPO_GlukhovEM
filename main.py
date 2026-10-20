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


def read_data():
    return input("Введите данные о доходе:\n")


def parse_data(text):
    object_type, date_text, rest = text.split(maxsplit=2)
    source_text, amount_text = rest.rsplit(maxsplit=1)
    source = source_text[1:-1].replace('\\"', '"')
    return object_type, date_text, source, amount_text


def create_income(date_text, source, amount_text):
    date = datetime.strptime(date_text, "%Y.%m.%d")
    amount = int(amount_text)
    return Income(date, source, amount)


def main():
    text = read_data()
    object_type, date_text, source, amount_text = parse_data(text)
    income = create_income(date_text, source, amount_text)
    print("\nТип объекта:", object_type)
    income.show()


if __name__ == "__main__":
    main()
