from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from .views import ping, get_time, CustomerReviewViewSet

router = DefaultRouter()
router.register("reviews", CustomerReviewViewSet)

urlpatterns = [
    path("", lambda request: JsonResponse({"status": "OK"})),
    path("api/ping/", ping),
    path("api/weather/", get_time),
    path("api/", include(router.urls)),
]
