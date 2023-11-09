from django.urls import path
from .views import DataManipulationView

urlpatterns = [
    path('', DataManipulationView.as_view(), name='Data_Manipulation'),
]