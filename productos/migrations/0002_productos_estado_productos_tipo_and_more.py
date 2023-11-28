# Generated by Django 4.2.7 on 2023-11-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='estado',
            field=models.CharField(blank=True, choices=[('En Proceso', 'En Proceso'), ('Finalizado', 'Finalizado')], max_length=20),
        ),
        migrations.AddField(
            model_name='productos',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Otros', 'Otros'), ('PET', 'PET'), ('PEAD', 'PEAD'), ('PEBD', 'PEBD')], max_length=20),
        ),
        migrations.AlterField(
            model_name='productos',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
