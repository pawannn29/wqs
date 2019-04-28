from django.contrib import admin
from .models import Data
# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display=('ph','temperature','dissolved_oxygen') 
admin.site.register(Data,DataAdmin)
