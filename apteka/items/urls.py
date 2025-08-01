from django.urls import path
from . import views

urlpatterns = [
    path('client_tovars', views.ClientTovarListAPIView.as_view()),
]