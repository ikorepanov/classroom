# Generated by Django 4.2 on 2024-02-15 05:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0002_alter_seat_arrangement_alter_seat_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrangement',
            name='columns',
            field=models.PositiveIntegerField(default=1, help_text='Введите количество "колонок"', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Количество "колонок"'),
        ),
        migrations.AddField(
            model_name='arrangement',
            name='rows',
            field=models.PositiveIntegerField(default=1, help_text='Введите количество "строк"', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Количество "строк"'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='column',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='seat',
            name='row',
            field=models.PositiveIntegerField(),
        ),
    ]
