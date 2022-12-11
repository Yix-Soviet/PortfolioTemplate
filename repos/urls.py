from django.urls import path

from .models import RepoModel
from .views import RepoView, RepoCreateView

urlpatterns = [
   path('repos', RepoView.as_view(), name="repos"),
   path('repos/create', RepoCreateView.as_view(), name="create repo"),
]
