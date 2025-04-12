def get_tests():
    tests = []
    with open("./data/tests.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]  # Пропускаем заголовок
        for i, line in enumerate(lines, 1):
            parts = line.strip().split(";")
            if len(parts) < 2:
                continue  # пропускаем битые строки
            text, country = parts[:2]
            tests.append((i, text, country))
    return tests
