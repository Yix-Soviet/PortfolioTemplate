from django.shortcuts import render, redirect
from django.views import View, generic
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import RepoModel
from .forms import RepoForm

# Create your views here.
class RepoView(View):
   template_name = "index.html"

   def get(self, request):
      return render(request, self.template_name)


class RepoCreateView(LoginRequiredMixin, generic.FormView):
   model = RepoModel
   template_name = "create.html"
   form_class = RepoForm
   context = {}

   def post(self, request):
      form = RepoForm(request.POST)
      if form.is_valid():
         form.save()

      self.context['form_repo'] = form
      # return render(request, 'index.html', self.context)
      return redirect('/repos')