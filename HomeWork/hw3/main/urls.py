from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task1/', views.task1_view, name='task1'),
    path('task2/', views.welcome_view, name='task2'),
    path('luke/', views.luke_view, name='luke'),
    path('leia/', views.leia_view, name='leia'),
    path('han/', views.han_view, name='han'),
    path('task3/', views.file_custom_response, name='task3'),
    path('task4/file/', views.file_response_view, name='file_resp'),
    path('task4/json/', views.json_response_view, name='json_resp'),
    path('task4/html/', views.html_response_view, name='html_resp'),
    path('task4/text/', views.text_response_view, name='text_resp'),
    path('task5/', views.task5_view, name='task5'),
    path('task6/', views.task6_view, name='task6'),
    path('polls/', views.polls_view, name='polls'),
    path('polls/<int:question_id>/', views.poll_detail, name='poll_detail'),
]
