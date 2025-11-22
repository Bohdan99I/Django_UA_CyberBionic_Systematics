import os
import requests
from datetime import datetime
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import CustomerReview
from .serializers import CustomerReviewSerializer
from .permissions import IsAdminOrReadOnly

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@api_view(["GET"])
def ping(request):
    return JsonResponse({"ping": "pong"})

@api_view(["GET"])
def get_time(request):
    city = request.GET.get("city", "Kyiv")
    if not OPENWEATHER_API_KEY:
        return JsonResponse({"error": "API key not set"}, status=500)

    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    try:
        res = requests.get(BASE_URL, params=params)
        data = res.json()
        if res.status_code != 200:
            return JsonResponse({"error": data.get("message", "Unknown error")}, status=res.status_code)

        time_now = datetime.utcfromtimestamp(data["dt"] + data["timezone"]).strftime("%Y-%m-%d %H:%M:%S")
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "time": time_now
        }
        return JsonResponse(weather)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all().order_by("-date")
    serializer_class = CustomerReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
