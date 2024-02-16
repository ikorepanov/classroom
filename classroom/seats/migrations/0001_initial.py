# Generated by Django 4.2 on 2024-02-13 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, help_text='Укажите месяц', max_length=20, null=True, verbose_name='Месяц')),
                ('year', models.CharField(blank=True, help_text='Укажите учебный год', max_length=20, null=True, verbose_name='Учебный год')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrangements', to=settings.AUTH_USER_MODEL, verbose_name='Классный руководитель')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите имя ученика', max_length=20, unique=True, verbose_name='Ученик')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.IntegerField()),
                ('row', models.IntegerField()),
                ('arrangement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='seats.arrangement', verbose_name='Место в классе')),
                ('student', models.ForeignKey(blank=True, help_text='Введите информацию о месте в классе', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seats', to='seats.student', verbose_name='Место в классе')),
            ],
            options={
                'ordering': ['column', 'row'],
            },
        ),
    ]
