from django.urls import path
from django.http import HttpResponse

def lesson_1_test(request):
    return HttpResponse("Lesson 1 URL works!")

urlpatterns = [
    path('', lesson_1_test),
]
