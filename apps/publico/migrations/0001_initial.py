# Generated by Django 2.0.3 on 2018-04-04 14:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'articulo'), (2, 'video')])),
                ('descripcion', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.TextField()),
                ('url', models.URLField()),
                ('fecha_creacion', models.DateField()),
                ('fuente', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
