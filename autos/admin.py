from django.contrib import admin
from .models import Marca, Auto

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'año')
    search_fields = ('modelo', 'marca__nombre')