from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populate/', views.populate_data, name='populate'),
    path('authors/', views.authors_list, name='authors'),
    path('books/', views.books_list, name='books'),
    path('products/', views.products_list, name='products'),
]
