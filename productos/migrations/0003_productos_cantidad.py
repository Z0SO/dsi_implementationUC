# Generated by Django 4.2.7 on 2023-11-27 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_productos_estado_productos_tipo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
    ]
