# Generated by Django 2.0.3 on 2018-05-03 12:46

import apps.privado.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privado', '0005_auto_20180502_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=150, validators=[apps.privado.validators.texto_validacion]),
        ),
    ]