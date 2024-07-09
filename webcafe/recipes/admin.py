from django.contrib import admin
from .models import Receta

class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') 

# Register your models here.
admin.site.register(Receta, RecipeAdmin)