from django.shortcuts import render
from django.http import HttpResponse

def lesson1_view(request):
    """Повертає сторінку lesson_1"""
    # simple Hello World for /lesson_1/
    return render(request, 'lesson_1.html')

def hello_page(request):
    """Повертає сторінку hello"""
    # for lesson_1_1/ handled via include
    return render(request, 'lesson_1_1.html')
