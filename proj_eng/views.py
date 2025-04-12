from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import texts_work
from . import tests_work

def index(request):
    return render(request, "index.html")

def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})

def texts_list(request):
    texts = texts_work.get_texts_for_table()
    return render(request, "text_list.html", context={"texts": texts})

def test_input(request):
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
    return render(request, "term_add.html")

def send_term(request):
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
        add_term(request)

def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)

