from django.shortcuts import render
from django.http import HttpResponse

def lesson1_view(request):
    # simple Hello World for /lesson_1/
    return render(request, 'lesson_1.html')

def hello_page(request):
    # for lesson_1_1/ handled via include
    return render(request, 'lesson_1_1.html')
