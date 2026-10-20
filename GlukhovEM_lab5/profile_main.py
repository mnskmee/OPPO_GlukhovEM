"""Нагрузка для измерения времени работы парсера через cProfile."""

from main import IncomeParser


def main():
    """Разбирает одну корректную запись 100 000 раз."""
    parser = IncomeParser()
    text = 'Доходы 2026.10.20 "Премия за работу" 30000'
    for _ in range(100_000):
        parser.parse(text)


if __name__ == '__main__':
    main()
