from django.urls import path
from .views import DataForgeryView

urlpatterns = [
    path('', DataForgeryView.as_view(), name='Data_Forgery'),
]