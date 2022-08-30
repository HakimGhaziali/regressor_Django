from django.contrib import admin

# Register your models here.


from .models import Regres , parameters



admin.register(Regres, parameters)(admin.ModelAdmin)