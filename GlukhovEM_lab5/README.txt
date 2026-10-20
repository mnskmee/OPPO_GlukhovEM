Лабораторная № 5: инструментальные средства анализа кода

main.py          - улучшенная программа
original_lab3.py - точная копия кода лабораторной № 3 (для сравнения)
test_main.py     - модульные тесты улучшенной программы
profile_main.py - нагрузка для cProfile
requirements.txt - инструменты анализа

Команды (PowerShell в папке проекта):
python -m pip install -r requirements.txt
python -m ruff check main.py test_main.py profile_main.py
python -m pylint main.py
python -m coverage run -m unittest -v test_main.py
python -m coverage report -m
python -m cProfile -s cumulative profile_main.py
python -m pdoc -o docs main

Результаты всех инструментов нужны для отчета. Команды не заменяют реальные замеры.
