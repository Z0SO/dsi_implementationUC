from django.forms import ModelForm
from .models import Productos

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'