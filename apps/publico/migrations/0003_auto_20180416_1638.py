# Generated by Django 2.0.3 on 2018-04-16 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publico', '0002_auto_20180411_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Publicacion',
        ),
    ]