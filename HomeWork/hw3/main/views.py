from django.http import HttpResponse, FileResponse, JsonResponse, Http404
from django.shortcuts import render
import io

# Завдання 1
def task1_view(request):
    lets_do_it = [
        {'priority': 100, 'task': 'Скласти перелік справ'},
        {'priority': 150, 'task': 'Вивчати Django'},
        {'priority': 1, 'task': 'Подумати про сенс життя'}
    ]
    return render(request, 'main/task1.html', {'lets_do_it': lets_do_it})

# Завдання 2 - структура сайту
def home(request):
    return render(request, 'main/home.html')

def welcome_view(request):
    return render(request, 'main/welcome.html')

def luke_view(request):
    return render(request, 'main/luke.html')

def leia_view(request):
    return render(request, 'main/leia.html')

def han_view(request):
    return render(request, 'main/han.html')

# Завдання 3 - власна відповідь з кодом 227 та файлом
def file_custom_response(request):
    content = 'Ось ваш файл'
    response = HttpResponse(content, content_type='text/plain', status=227)
    response['Content-Disposition'] = 'attachment; filename="your_file.txt"'
    return response

# Завдання 4 - різні типи відповідей
def file_response_view(request):
    data = 'File content from FileResponse'
    buf = io.BytesIO(data.encode('utf-8'))
    return FileResponse(buf, as_attachment=True, filename='example.txt')

def json_response_view(request):
    data = {'message': 'Це JSON відповідь', 'ok': True}
    return JsonResponse(data)

def html_response_view(request):
    return render(request, 'main/example.html', {'message': 'Привіт з HTML-представлення'})

def text_response_view(request):
    return HttpResponse('Просто текстова відповідь', content_type='text/plain')

# Завдання 5 - сортування за priority спад
def task5_view(request):
    lets_do_it = [
        {'priority': 100, 'task': 'Скласти перелік справ'},
        {'priority': 150, 'task': 'Вчити Django'},
        {'priority': 1, 'task': 'Подумати про сенс життя'}
    ]
    sorted_list = sorted(lets_do_it, key=lambda x: x['priority'], reverse=True)
    return render(request, 'main/task5.html', {'lets_do_it': sorted_list})

# Завдання 6 - список словників
def task6_view(request):
    people = [
        {'name': 'Шаддам IV', 'surname': 'Корріно'},
        {'name': 'Стать', 'surname': 'Атрейдес'},
        {'name': 'Франклін', 'surname': 'Герберт'}
    ]
    return render(request, 'main/task6.html', {'people': people})

# Завдання 7 - polls
def polls_view(request):
    latest_question_list = [
        {'id': 1, 'question_text': 'У чому сенс життя?'},
        {'id': 2, 'question_text': 'Що первинне: дух чи матерія?'},
        {'id': 3, 'question_text': 'Чи існує свобода волі?'}
    ]
    return render(request, 'main/polls.html', {'latest_question_list': latest_question_list})

def poll_detail(request, question_id):
    questions = {
        1: 'У чому сенс життя?',
        2: 'Що первинне: дух чи матерія?',
        3: 'Чи існує свобода волі?'
    }
    question = questions.get(question_id)
    if not question:
        raise Http404("Питання не знайдено")
    return HttpResponse(f"<h1>Питання {question_id}</h1><p>{question}</p>")
