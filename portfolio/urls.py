from django.urls import path

from .views import *

urlpatterns = [
   path('', PortfolioView.as_view(), name="index")
]
