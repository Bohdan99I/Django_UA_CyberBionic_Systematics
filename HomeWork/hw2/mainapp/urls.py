from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home-view'),
    path('book/<str:title>/', views.book, name='book'),
    path('lesson_2/', include('lesson_2.urls')),

    path('index/', views.index, name='index-view'),
    path('bio/<str:username>/', views.bio, name='bio'),
    path('lesson_1/', include('mainapp.lesson_1.urls')),

    path('weather/', views.weather, name='weather'),
]
