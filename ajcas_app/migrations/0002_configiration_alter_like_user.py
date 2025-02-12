# Generated by Django 5.0.6 on 2024-07-20 07:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajcas_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configiration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='ajcas', max_length=44)),
                ('site_adresse', models.CharField(default='ajcascongoasbl@gmail.com', max_length=56)),
                ('site_phone', models.CharField(default=' +243 828 757 690', max_length=56)),
                ('site_location', models.CharField(default=' Av, mateko n°26, kinshasa/lemba', max_length=233)),
                ('site_intro', models.TextField(default='ENSEMBLE LUTTONS POUR L’AMÉLIORATION DE NOTRE ÉTAT SANITAIRE !!!!')),
                ('site_intro_description', models.TextField(default='PROGRAMME ANNUEL DE L’ASSOCIATION DES JEUNES CONGOLAIS POUR L’ACCES A LA SANTE')),
                ('assisted_people', models.IntegerField(default=125, max_length=6)),
                ('projects', models.IntegerField(default=85, max_length=6)),
                ('years_experiences', models.IntegerField(default=85, max_length=6)),
                ('achievement', models.IntegerField(default=48, max_length=6)),
            ],
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
