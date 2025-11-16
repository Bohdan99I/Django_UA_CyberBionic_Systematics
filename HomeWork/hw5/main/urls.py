from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_form, name='login'),
    path('custom-login/', views.custom_login_form, name='custom_login'),
    path('modelform/', views.modelform_example, name='modelform'),
    path('review/', views.review_form, name='review'),
    path('success/', views.success, name='success'),
    path('data/', views.populate_example, name='data'),
]
