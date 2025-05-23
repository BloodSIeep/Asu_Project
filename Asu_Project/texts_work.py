"""
Модуль для работы с текстами.

Этот модуль содержит функции для чтения и обработки данных о текстах из CSV-файла.
"""
def get_texts_for_table():
    """
    Считывает тексты из файла texts.csv и возвращает их в виде списка.

    :return: Список [номер, интерфейс, проект, описание, причина, источник].
    """
    texts = []
    with open("./data/texts.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            interface, project, description, why_exactly, source = line.split(";")
            texts.append([cnt, interface, project, description, why_exactly ])
            cnt += 1
    return texts
