# Generated by Django 2.0.5 on 2020-07-13 16:47

import apps.privado.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publico', '0002_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='file_category',
            field=models.IntegerField(choices=[(0, 'SINIC-SAT'), (1, 'Anexo RRHH '), (2, 'ModusOperandis '), (3, 'Vivienda '), (4, 'Área Finanzas '), (5, 'Área Comunicaciones e Informatica '), (6, 'Departamento de Educacion Fisica ')], validators=[apps.privado.validators.tipo_validacion]),
        ),
    ]
