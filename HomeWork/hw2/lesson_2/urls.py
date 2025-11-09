from django.urls import path
from django.http import HttpResponse

def lesson_2_test(request):
    return HttpResponse("Lesson 2 URL works!")

urlpatterns = [
    path('', lesson_2_test),
]
