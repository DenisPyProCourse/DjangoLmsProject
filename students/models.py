# import datetime
import random

# from dateutil.relativedelta import relativedelta

from django.db import models

# from faker import Faker

# from .validators import AdultValidator
from core.models import PersonModel
from groups.models import Group


class Student(PersonModel):

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.phone_number}'

    def save(self, *args, **kwargs):
        # self.age = relativedelta(datetime.date.today(), self.birthday).years
        # self.phone_number = phone_number_norm(self.phone_number)
        super().save(*args, **kwargs)

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        groups = Group.objects.all()
        obj.group = random.choice(groups)
        obj.save()
