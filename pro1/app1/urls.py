from django.urls import path, include
from .views import *

urlpatterns = [
    path('pro/', ProductView.as_view()),
    path('total/', Total.as_view())
]
