from django.urls import path, include
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/personal/about/
    path('about/', views.about),
    # http://127.0.0.1:8000/personal/index/
    path('index/', views.index),
    # http://127.0.0.1:8000/personal/index2/
    path('index2/', views.index2),
]