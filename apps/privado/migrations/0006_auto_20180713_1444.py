# Generated by Django 2.0.3 on 2018-07-13 14:44

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('privado', '0005_auto_20180712_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='contenido',
            field=tinymce.models.HTMLField(),
        ),
    ]