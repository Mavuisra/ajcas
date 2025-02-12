# Generated by Django 5.0.6 on 2024-07-17 15:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('birth_info', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('F', 'Féminin'), ('M', 'Masculin'), ('O', 'Autres')], max_length=1)),
                ('address', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('member_declaration', models.BooleanField(default=False)),
                ('monthly_contribution', models.BooleanField(default=False)),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('donation_method', models.CharField(blank=True, max_length=50, null=True)),
                ('donation_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_signed', models.DateField()),
                ('member_signature', models.CharField(max_length=255)),
                ('president_signature', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ajcas_app.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='ajcas_app.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
