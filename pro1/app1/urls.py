from django.urls import path, include
from .views import *

urlpatterns = [
    path('pro/', ProductView.as_view()),
    path('total/', TotalCalculationAPIView.as_view()),
    path('update/<int:pk>/', ProductUpdate.as_view()),
    path('delete/<int:pk>/', ProductDelete.as_view()),

]
