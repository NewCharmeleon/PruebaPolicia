# Generated by Django 2.0.3 on 2018-05-30 01:27

import apps.privado.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privado', '0003_auto_20180530_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoridad',
            name='telefono',
            field=models.CharField(blank=True, max_length=35, validators=[apps.privado.validators.telefono_validacion]),
        ),
        migrations.AlterField(
            model_name='autoridad',
            name='telefono_laboral',
            field=models.CharField(blank=True, max_length=35, validators=[apps.privado.validators.telefono_validacion]),
        ),
    ]
