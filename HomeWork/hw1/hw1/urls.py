from django.contrib import admin
from django.urls import path, include
from lesson_11 import views as lesson_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson_1/', lesson_views.lesson1_view),
    path('lesson_1_1/', include('lesson_11.urls')),
]
