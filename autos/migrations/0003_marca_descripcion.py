# Generated by Django 5.0.7 on 2024-07-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0002_vendedor_alter_auto_modelo_remove_auto_precio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]
