from django.db import models
from faker import Faker

# Create your models here.


class Teacher(models.Model):
    teacher_first_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    teacher_last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.teacher_first_name} {self.teacher_last_name}, age {self.age}'

    @staticmethod
    def gen_teachers(cnt = 10):
        fk = Faker()
        for i in range(cnt):
            tc = Teacher(
                teacher_first_name = fk.first_name(),
                teacher_last_name = fk.last_name(),
                age = fk.random_int(min = 24, max = 70)
            )
            tc.save()