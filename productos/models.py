from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    TIPO_CHOICES = [
        ('Otros', 'Otros'),
        ('PET', 'PET'),
        ('PEAD', 'PEAD'),
        ('PEBD', 'PEBD'),
    ]

    ESTADO_CHOICES = [
        ('En Proceso', 'En Proceso'),
        ('Finalizado', 'Finalizado'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, blank=True)
    cantidad = models.IntegerField(null=True)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, blank=True)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True , blank=True)
    imagen = models.ImageField(upload_to='productos_imagenes/', blank=True, null=True)

    def __str__(self):
        return self.nombre + ' -   -  ' + self.estado