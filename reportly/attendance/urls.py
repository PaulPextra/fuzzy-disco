from django.urls import path
from .views import test_view, homePage_view

urlpatterns = [
    path('', homePage_view),
    path('about/', test_view),
]
