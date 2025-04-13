"""
Модуль для обработки запросов и отображения страниц в Django-приложении.

Этот модуль содержит представления (views) для отображения различных страниц.
"""

from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import texts_work
from . import tests_work

def index(request):
    """
    Отображает главную страницу.

    :param request: HTTP-запрос.
    :return: Рендеринг страницы index.html.
    """
    return render(request, "index.html")

def terms_list(request):
    """
    Отображает список перечня.

    :param request: HTTP-запрос.
    :return: Рендеринг страницы list.html с контекстом, содержащим список терминов.
    """
    terms = terms_work.get_terms_for_table()
    return render(request, "list.html", context={"terms": terms})

def texts_list(request):
    """
    Отображает список перечня.

    :param request: HTTP-запрос.
    :return: Рендеринг страницы realization.html с контекстом, содержащим список терминов.
    """
    texts = texts_work.get_texts_for_table()
    return render(request, "realization.html", context={"texts": texts})

def test_input(request):
    """
    Отображает форму для ввода тестов и обрабатывает отправленные данные.

    :param request: HTTP-запрос.
    :return: Рендеринг страницы test_input_form.html с контекстом, содержащим тесты или результаты.
    """
    tests = tests_work.get_tests()
    score = None  # Оценка будет по умолчанию None

    if request.method == "POST":
        submitted_data = []
        correct_count = 0
        total_count = len(tests)

        for cnt, text, correct_country in tests:
            user_input = request.POST.get(f"user_input_{cnt}", "").strip()
            is_correct = user_input.lower() == correct_country.lower()
            submitted_data.append((cnt, text, user_input, correct_country, is_correct))

            if is_correct:
                correct_count += 1

        # Подсчитываем процент
        score = (correct_count / total_count) * 100
        return render(request, "test_input_form.html", {
            "submitted_data": submitted_data,
            "score": score
        })

    return render(request, "test_input_form.html", {
        "tests": tests
    })

def add_term(request):
    """
    Отображает страницу для добавления нового термина.

    :param request: HTTP-запрос.
    :return: Рендеринг страницы list_update.html.
    """
    return render(request, "list_update.html")

def send_term(request):
    """
    Обрабатывает отправку нового термина.

    :param request: HTTP-запрос.
    :return: Рендеринг страницы term_request.html с контекстом, содержащим результат операции.
    """
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваше слово добавлено"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        return add_term(request)





def i2c_explanation(request):
    """
    Отображает страницу с объяснением разбора пакета I2C.

    :param request: HTTP-запрос.
    :return: Рендеринг страницы i2c_explanation.html.
    """
    return render(request, "i2c_explanation.html")







def decode_i2c_packet(request):
    """
    Обрабатывает HTTP-запрос и декодирует пакет I2C.

    Эта функция:
    - Принимает пакет I2C в виде строки битов.
    - Декодирует пакет и возвращает результат в двоичном, шестнадцатеричном и десятичном форматах.

    :param request: HTTP-запрос.
    :return: Рендеринг страницы i2c_decoder.html с контекстом, содержащим результат декодирования.
    """
    result = None
    if request.method == 'POST':
        i2c_packet = request.POST.get('i2c_packet')
        result = decode_packet(i2c_packet)
    return render(request, 'i2c_decoder.html', {'result': result})

def decode_packet(packet):
    """
    Декодирует пакет I2C.

    Эта функция:
    - Принимает строку битов, представляющую пакет I2C.
    - Декодирует пакет и возвращает результат в двоичном, шестнадцатеричном и десятичном форматах.

    :param packet: Строка битов, представляющая пакет I2C.
    :return: Словарь с результатами декодирования в dec, hex и bin форматах.
    """
    try:
        # Удаляем пробелы и разбиваем строку на биты
        bits = [int(bit) for bit in packet.replace(" ", "")]

        # Проверяем наличие стартового бита
        if bits[0] != 1:
            return "Ошибка: пакет должен начинаться со стартового бита (1)."

        # Проверяем, что пакет содержит достаточно бит для адреса и R/W
        if len(bits) < 18:
            return "Ошибка: пакет должен содержать минимум 18 бит (старт+адрес+R/W+ACK+данные+ACK)."

        # Извлекаем адрес и бит R/W
        address = bits[1:8]
        rw_bit = bits[8]
        ack_bit = bits[9]

        # Проверяем бит ACK
        if ack_bit != 0:
            return "Ошибка: бит ACK должен быть 0 (подтверждение)."

        # Извлекаем данные и бит ACK для данных
        data = bits[10:18]
        data_ack_bit = bits[18]

        # Проверяем бит ACK для данных
        if data_ack_bit != 0:
            return "Ошибка: бит ACK для данных должен быть 0 (подтверждение)."

        # Проверяем наличие стоп-бита
        if bits[19] != 1:
            return "Ошибка: пакет должен заканчиваться стоп-битом (1)."

        # Преобразуем в строки для отображения
        binary_result = {
            'address': ''.join(map(str, address)),
            'rw_bit': rw_bit,
            'ack_bit': ack_bit,
            'data': ''.join(map(str, data)),
            'data_ack_bit': data_ack_bit
        }

        # Преобразуем в шестнадцатеричный формат
        hex_result = {
            'address': hex(int(''.join(map(str, address)), 2)),
            'rw_bit': hex(rw_bit),
            'ack_bit': hex(ack_bit),
            'data': hex(int(''.join(map(str, data)), 2)),
            'data_ack_bit': hex(data_ack_bit)
        }

        # Преобразуем в десятичный формат
        decimal_result = {
            'address': int(''.join(map(str, address)), 2),
            'rw_bit': rw_bit,
            'ack_bit': ack_bit,
            'data': int(''.join(map(str, data)), 2),
            'data_ack_bit': data_ack_bit
        }

        return {
            'binary': binary_result,
            'hex': hex_result,
            'decimal': decimal_result
        }
    except ValueError:
        return "Ошибка: некорректный формат пакета"
