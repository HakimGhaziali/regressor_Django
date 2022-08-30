from django.contrib import admin

# Register your models here.


from .models import Regres , parameters , esm



admin.register(Regres, parameters,esm)(admin.ModelAdmin)