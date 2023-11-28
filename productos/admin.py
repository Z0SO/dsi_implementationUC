from django.contrib import admin
from .models import Productos
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
  readonly_fields = ('fecha_inicio', )

admin.site.register(Productos, ProductosAdmin)