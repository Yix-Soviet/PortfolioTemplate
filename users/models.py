from django.db import models

# Create your models here.
class IPAddress(models.Model):
   pub_date = models.DateTimeField('date published')
   ip_address = models.GenericIPAddressField()

   class Meta:
      db_table = 'ip-address-info'