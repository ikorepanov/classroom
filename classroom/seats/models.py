from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Student(models.Model):
    """Информация об ученике."""
    name = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Ученик',
        help_text='Введите имя ученика',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Arrangement(models.Model):
    """Информация о рассадках."""
    # teacher = models.ForeignKey(
    #     User,
    #     null=True,
    #     blank=True,
    #     on_delete=models.CASCADE,
    #     related_name='arrangements',
    #     verbose_name='Классный руководитель',
    # )
    month = models.CharField(
        max_length=20,
        # choices=...,
        # null=True,
        blank=True,
        verbose_name='Месяц',
        help_text='Укажите месяц',
    )
    year = models.CharField(
        max_length=20,
        # null=True,
        blank=True,
        verbose_name='Учебный год',
        help_text='Укажите учебный год',
    )
    columns = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(6)],
        verbose_name='Количество "колонок"',
        help_text='Введите количество "колонок"',
    )
    rows = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(6)],
        verbose_name='Количество "строк"',
        help_text='Введите количество "строк"',
    )

    def __str__(self):
        if self.month or self.year:
           return f'Рассадка {self.columns}x{self.rows}, {self.month}, {self.year}'
        return f'Рассадка {self.columns}x{self.rows}'


class Seat(models.Model):
    """Информация о местах в классе."""
    column = models.PositiveIntegerField()
    row = models.PositiveIntegerField()
    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='seats_student',
        verbose_name='Студент',
        help_text='Выберите студента, который будет сидеть на этом месте',
    )
    arrangement = models.ForeignKey(
        Arrangement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='seats_arrangement',
        verbose_name='Место в классе',
        help_text='Пока не понимаю, как увязать это с рассадкой...'
    )

    class Meta:
        ordering = ['column', 'row']

    def __str__(self):
        return f'Место {self.column}, {self.row}'
