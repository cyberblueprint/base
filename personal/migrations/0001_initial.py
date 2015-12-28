# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=300)),
                ('datos_generales', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_de_monitores', models.IntegerField()),
                ('numero_de_pasos', models.IntegerField()),
                ('token', models.DateTimeField()),
                ('inicio', models.DateTimeField(auto_now_add=True)),
                ('fin', models.DateTimeField()),
                ('habilitado', models.BooleanField()),
                ('producto', models.IntegerField(choices=[(1, b'Vzor Suite'), (2, b'Vzor Cloud')])),
                ('empresa', models.ManyToManyField(to='personal.Empresa')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
