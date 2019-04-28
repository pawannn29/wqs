from django.db import models

# Create your models here.
class Data(models.Model):
    ph = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    dissolved_oxygen = models.DecimalField(max_digits=5, decimal_places=2)
  
