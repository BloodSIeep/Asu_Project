def get_terms_for_table():
    terms = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            parts = line.strip().split(";")
            if len(parts) < 3:
                continue  # Пропускаем строки, которые не соответствуют ожидаемому формату
            term, definition, source = parts[0], ";".join(parts[1:-1]), parts[-1]
            terms.append([cnt, term, definition])
            cnt += 1
    return terms

def write_term(new_term, new_definition):
    updated = False

    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]

    # Проверка существования термина и обновление или добавление
    for i, line in enumerate(old_terms):
        parts = line.split(";")
        if len(parts) < 3:
            continue  # Пропускаем строки, которые не соответствуют ожидаемому формату
        term, definition, _ = parts[0], ";".join(parts[1:-1]), parts[-1]
        if term == new_term:
            # Дополняем существующее описание новым
            updated_definition = f"{definition}; {new_definition}".strip()
            old_terms[i] = f"{term};{updated_definition};user"
            updated = True
            break

    if not updated:
        # Добавляем новый термин, если он не существует
        new_term_line = f"{new_term};{new_definition};user"
        old_terms.append(new_term_line)

    terms_sorted = sorted(old_terms)
    new_terms = [title] + terms_sorted

    with open("./data/terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))

def get_terms_stats():
    db_terms = 0
    user_terms = 0
    defin_len = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            parts = line.strip().split(";")
            if len(parts) < 3:
                continue  # Пропускаем строки, которые не соответствуют ожидаемому формату
            term, defin, added_by = parts[0], ";".join(parts[1:-1]), parts[-1]
            words = defin.split()
            defin_len.append(len(words))
            if "user" in added_by:
                user_terms += 1
            elif "db" in added_by:
                db_terms += 1
