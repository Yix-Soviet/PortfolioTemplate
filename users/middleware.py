from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

from .models import IPAddress

# class SaveIPMiddleware:
#    def process_request(self, request):
#       x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

#       if x_forwarded_for:
#          ip = x_forwarded_for.split(',')[-1].strip()
#       else:
#          ip = request.META.get('REMOTE_ADDR')
#       try:
#          IPAddress.objects.get(ip_address = ip)
#       except IPAddress.DoesNotExist:
#             ip_address = IPAddress(ip_address=ip, pub_date=datetime.now())
#             ip_address.save()
#       return None

class SaveIPMiddleware(MiddlewareMixin):
   def process_request(self, request):
      ip_address = request.META.get("REMOTE_ADDR")

      IPAddress.objects.create(ip_address=ip_address, pub_date=datetime.now())