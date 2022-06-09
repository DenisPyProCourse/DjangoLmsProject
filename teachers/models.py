import datetime

from core.validators import adult_validator

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from groups.models import Group
from .validators import phone_number_norm
from .validators import phone_number_validator
# Create your models here.


class Teacher(models.Model):
    teacher_first_name = models.CharField(
        max_length=100,
        verbose_name='fname',
        validators=[MinLengthValidator(2)],
        db_column='f_name')
    # age = models.PositiveIntegerField()
    teacher_last_name = models.CharField(
        max_length=100,
        verbose_name='lname',
        validators=[MinLengthValidator(2)],
        db_column='l_name')
    birthday = models.DateField(
        default=datetime.date.today,
        validators=[adult_validator]
        # validators=[AdultValidator(20)]
    )
    phone_number = models.CharField(max_length=25, null=True, validators=[phone_number_validator,
                                                                          phone_number_norm])

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='teachers')
    salary = models.PositiveIntegerField(default=10000)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teacher'
        db_table = 'teachers'

    def __str__(self):
        return f'{self.teacher_first_name} {self.teacher_last_name} - {self.phone_number}'

    def save(self, *args, **kwargs):
        # self.age = relativedelta(datetime.date.today(), self.birthday).years
        #self.phone_number = phone_number_norm(self.phone_number)
        super().save(*args, **kwargs)

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @staticmethod
    def gen_teachers(cnt=10):
        fk = Faker()
        for i in range(cnt):
            tc = Teacher(
                teacher_first_name=fk.first_name(),
                teacher_last_name=fk.last_name()  #,
                # age=fk.random_int(min=24, max=70)
            )
            tc.save()
