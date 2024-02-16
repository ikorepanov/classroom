# Generated by Django 4.2 on 2024-02-13 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='arrangement',
            field=models.ForeignKey(blank=True, help_text='Пока не понимаю, как увязать это с рассадкой...', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='seats.arrangement', verbose_name='Место в классе'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='student',
            field=models.ForeignKey(blank=True, help_text='Выберите студента, который будет сидеть на этом месте', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seats', to='seats.student', verbose_name='Студент'),
        ),
    ]
