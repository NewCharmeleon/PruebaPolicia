# Generated by Django 2.0.3 on 2018-05-29 13:48

import apps.privado.validators
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
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
                ('jerarquia', models.IntegerField(choices=[(1, 'Crio. General'), (2, 'Crio. Mayor'), (3, 'Crio. Inspector'), (4, 'Comisario'), (5, 'SubCrio.'), (6, 'Of. Principal'), (7, 'Of. Inspector.'), (8, 'Of. SubInsp.')], default=1, validators=[apps.privado.validators.tipo_validacion])),
                ('cargo', models.IntegerField(choices=[(1, 'Jefe de Policia'), (2, 'SubJefe de Policia'), (3, 'Secretario General'), (4, 'Jefe de Area'), (5, 'SubJefe de Area'), (6, 'Jefe'), (7, 'SubJefe')], default=1, validators=[apps.privado.validators.tipo_validacion])),
                ('dependencia', models.IntegerField(choices=[(1, 'Jefatura de Policia'), (2, 'Secretaria General'), (3, 'Direccion Seguridad'), (4, 'Direccion Recursos Humanos'), (5, 'Direccion Recursos Materiales'), (6, 'Direccion Policia Judicial')], default=1, validators=[apps.privado.validators.tipo_validacion])),
                ('nombre', models.CharField(max_length=20, validators=[apps.privado.validators.texto_validacion])),
                ('segundo_nombre', models.CharField(max_length=20, validators=[apps.privado.validators.texto_validacion])),
                ('apellido', models.CharField(max_length=20, validators=[apps.privado.validators.texto_validacion])),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='autoridades', validators=[apps.privado.validators.imagen_validacion])),
                ('direccion_laboral', models.CharField(max_length=100, validators=[apps.privado.validators.texto_validacion])),
                ('telefono_laboral', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="El telefono debe tener formato: '+999999999'. Hasta 15 digitos es permitido.", regex='/^(?:(?:00)?549?)?0?(?:11|[2368]\\d)(?:(?=\\d{0,2}15)\\d{2})??\\d{8}$/D')])),
                ('telefono', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="El telefono debe tener formato: '+999999999'. Hasta 15 digitos es permitido.", regex='/^(?:(?:00)?549?)?0?(?:11|[2368]\\d)(?:(?=\\d{0,2}15)\\d{2})??\\d{8}$/D')])),
                ('email', models.EmailField(max_length=254)),
                ('trayectoria', models.TextField(validators=[apps.privado.validators.texto_validacion])),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('is_publicado', models.BooleanField(default=False)),
                ('is_archivado', models.BooleanField(default=False)),
                ('is_para_portada', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(default=django.contrib.auth.models.User, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'articulo'), (2, 'video')], default=1, validators=[apps.privado.validators.tipo_validacion])),
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
    ]
