"""
Модуль для работы с тестами.
Этот модуль содержит функции для чтения и обработки данных о тестах из CSV-файла.
"""
def get_tests():
    """
    Читает данные о тестах из CSV-файла и возвращает их в виде списка.
    Возвращает:
    list:Список кортежей, где каждый кортеж содержит номер строки, текст вопроса и правильный ответ.
    """
    tests = []
    with open("./data/tests.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]  # Пропускаем заголовок
        for i, line in enumerate(lines, 1):
            parts = line.strip().split(";")
            if len(parts) < 2:
                continue  # Пропускаем битые строки
            text, country = parts[:2]
            tests.append((i, text, country))
    return tests
