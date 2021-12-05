from django.contrib import admin
from . models import *

# Register your models here.
class catadmin(admin.ModelAdmin):


    list_display = ["name"]
class proadmin(admin.ModelAdmin):

    list_display = ["date","number1","number2","number3"]
admin.site.register(category,catadmin)
admin.site.register(number,proadmin)
