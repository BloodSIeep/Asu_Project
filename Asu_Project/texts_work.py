"""
Модуль для работы с текстами.

Этот модуль содержит функции для чтения и обработки данных о текстах из CSV-файла.
"""

def get_texts_for_table():
    """
    Читает данные о текстах из CSV-файла и возвращает их в виде списка.

    Возвращает:
    list:список содержит номер строки, интерфейс, проект, описание, причину и источник.
    """
    texts = []
    try:
        with open("./data/texts.csv", "r", encoding="utf-8") as f:
            cnt = 1
            for line in f.readlines()[1:]:
                parts = line.strip().split(";")
                if len(parts) != 5:
                    print(f"Ошибка: Неверное количество значений в строке {cnt}: {line}")
                    continue  # Пропускаем строки с неверным количеством значений
                interface, project, description, why_exactly, source = parts
                texts.append([cnt, interface, project, description, why_exactly, source])
                cnt += 1
        if not texts:
            print("Внимание: Ни одна строка не была добавлена в список texts.")
    except FileNotFoundError:
        print("Ошибка: Файл texts.csv не найден.")
    except UnicodeDecodeError:
        print("Ошибка: Проблема с кодировкой файла.")
    except ValueError as ve:
        print(f"Ошибка: Проблема с разбором строки: {ve}")
    except OSError as ose:
        print(f"Ошибка: Проблема с доступом к файлу: {ose}")

    return texts
