from django.db import models

# Create your models here.


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    students_number = models.PositiveIntegerField()
    teacher_last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Group "{self.group_name}" include [{self.students_number}] students. Leading teacher is {self.teacher_last_name}'