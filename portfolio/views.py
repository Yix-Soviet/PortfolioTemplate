# Import Library
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Import Files
from .models import Contact

class PortfolioView(View):
   template_name = 'portfolio.html'

   def get(self, request):
      return render(request, self.template_name)

   def post(self, request):
      if request.method == 'POST':
         # if request.POST.get('name'):
         form = Contact()
         form.name = request.POST.get('name')
         form.email = request.POST.get('email')
         form.message = request.POST.get('message')
         form.save()
         return HttpResponse("Create")
      else:
         return HttpResponse("Error")