# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-03 00:42
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tipos', models.CharField(choices=[('POR', 'Porções'), ('PAS', 'Pastéis'), ('HOT', 'Hot-Dog'), ('REF', 'Refrigerante'), ('CER', 'Cerveja'), ('COC', 'Coqueteis'), ('MARK', 'Patrocínio')], max_length=6)),
                ('imagem', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='imagem')),
                ('texto', models.TextField(max_length=400)),
            ],
        ),
    ]
