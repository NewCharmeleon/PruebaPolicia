# Generated by Django 2.0.3 on 2018-06-28 16:17

import apps.privado.validators
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autoridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, validators=[apps.privado.validators.texto_validacion])),
                ('segundo_nombre', models.CharField(max_length=20, validators=[apps.privado.validators.texto_validacion])),
                ('apellido', models.CharField(max_length=20, validators=[apps.privado.validators.texto_validacion])),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='autoridades', validators=[apps.privado.validators.imagen_validacion])),
                ('direccion_laboral', models.CharField(max_length=100, validators=[apps.privado.validators.texto_validacion])),
                ('telefono_laboral', models.CharField(blank=True, max_length=35, validators=[apps.privado.validators.telefono_validacion])),
                ('telefono', models.CharField(blank=True, max_length=35, validators=[apps.privado.validators.telefono_validacion])),
                ('email', models.EmailField(max_length=254)),
                ('trayectoria', models.TextField(validators=[apps.privado.validators.texto_validacion])),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('is_publicado', models.BooleanField(default=False)),
                ('is_archivado', models.BooleanField(default=False)),
                ('is_para_portada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jerarquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'Articulo'), (2, 'Video')], validators=[apps.privado.validators.tipo_validacion])),
                ('jurisdiccion', models.IntegerField(choices=[(0, 'Provincial'), (1, 'Jefatura de Policia'), (2, 'Unidad Regional Comodoro Rivadavia'), (3, 'Unidad Regional Esquel'), (4, 'Unidad Regional Puerto Madryn'), (5, 'Unidad Regional Trelew')], validators=[apps.privado.validators.tipo_validacion])),
                ('categoria', models.IntegerField(choices=[(0, 'Informativo'), (1, 'Institucional'), (2, 'Comunidad'), (3, 'Otro')], validators=[apps.privado.validators.tipo_validacion])),
                ('titulo', models.CharField(max_length=100, validators=[apps.privado.validators.texto_validacion])),
                ('contenido', models.TextField(validators=[apps.privado.validators.texto_validacion])),
                ('url', models.URLField()),
                ('fuente', models.CharField(max_length=200, validators=[apps.privado.validators.texto_validacion])),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_archivado', models.DateTimeField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='publicaciones', validators=[apps.privado.validators.imagen_validacion])),
                ('intro', models.CharField(blank=True, max_length=350, null=True)),
                ('is_publicado', models.BooleanField(default=False)),
                ('is_archivado', models.BooleanField(default=False)),
                ('is_para_portada', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(default=django.contrib.auth.models.User, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='autoridad',
            name='cargo',
            field=models.ForeignKey(on_delete='CASCADE', to='privado.Cargo'),
        ),
        migrations.AddField(
            model_name='autoridad',
            name='jerarquia',
            field=models.ForeignKey(on_delete='CASCADE', to='privado.Jerarquia'),
        ),
        migrations.AddField(
            model_name='autoridad',
            name='lugar',
            field=models.ForeignKey(on_delete='CASCADE', to='privado.Lugar'),
        ),
        migrations.AddField(
            model_name='autoridad',
            name='usuario',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
