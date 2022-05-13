from django.db import models

# Create your models here.

import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from .validators import adult_validator
from .validators import phone_number_validator
from .validators import phone_number_norm
# from .validators import AdultValidator


class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='fname',
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(max_length=100, verbose_name='lname', validators=[MinLengthValidator(2)])
    age = models.PositiveIntegerField()
    birthday = models.DateField(
        default=datetime.date.today,
        validators=[adult_validator]
        # validators=[AdultValidator(20)]
    )
    phone_number = models.CharField(max_length=25, null=True, validators=[phone_number_validator,
                                                                          phone_number_norm])

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age} - {self.phone_number}'

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        self.phone_number = phone_number_norm(self.phone_number)
        super().save(*args, **kwargs)

    @staticmethod
    def gen_students(cnt=10):
        fk = Faker()
        for _ in range(cnt):
            st = Student(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                age=fk.random_int(min=18, max=45),
                birthday=fk.date_between(start_date='-65y', end_date='-15y')
            )

            st.save()