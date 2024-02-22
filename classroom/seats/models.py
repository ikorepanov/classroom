from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # teacher = models.ForeignKey(User, on_delete=models.CASCADE,
    #                             related_name='students')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Arrangement(models.Model):
    number_of_columns = models.PositiveIntegerField()
    number_of_rows = models.PositiveIntegerField()
    academic_year = models.CharField(max_length=5)
    month = models.CharField(max_length=15)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='arrangements')


class Seat(models.Model):
    column = models.PositiveIntegerField()
    row = models.PositiveIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True,
                                related_name='seats')
    arrangement = models.ForeignKey(Arrangement, on_delete=models.CASCADE,
                                    related_name='seats')
