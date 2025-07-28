from django.urls import path
from .views import WheelSpecificationCreateView


urlpatterns = [
    path('wheel-specifications',  WheelSpecificationCreateView.as_view(), name='wheel-specifications'),
]
