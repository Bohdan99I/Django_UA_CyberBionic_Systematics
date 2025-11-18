from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populate/', views.populate, name='populate'),
    path('search/', views.search_articles, name='search'),
    path('special/', views.special_queries, name='special'),
]
