from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from .views import SignupView

urlpatterns = [
   path('accounts/login/', LoginView.as_view(), name="login"),
   path('signup/', SignupView.as_view(), name='signup'),
   path('logout/', logout_then_login, name='logout'),
]
