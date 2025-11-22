from django.contrib import admin
from django.urls import path, include
from main.views import ping, get_time, CustomerReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("reviews", CustomerReviewViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", get_time),  # або JsonResponse({"status":"OK"})
    path("api/ping/", ping),
    path("api/time/", get_time),
    path("api/", include(router.urls)),
]
