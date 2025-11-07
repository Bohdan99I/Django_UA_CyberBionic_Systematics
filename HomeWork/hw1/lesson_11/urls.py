from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_page, name='lesson_1_1'),
]
