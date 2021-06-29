from django.urls import path
from core import views

urlpatterns = [
    path('', views.fetch_news, name='fetch')
]
