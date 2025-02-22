# Generated by Django 5.0.7 on 2024-07-19 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='auto',
            name='modelo',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='auto',
            name='precio',
        ),
        migrations.AddField(
            model_name='auto',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='autos.marca'),
        ),
        migrations.DeleteModel(
            name='Modelo',
        ),
    ]
