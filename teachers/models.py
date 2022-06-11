import datetime
import random

from core.models import PersonModel


from django.db import models

from faker import Faker

from groups.models import Group

# Create your models here.


class Teacher(PersonModel):

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='teachers')
    salary = models.PositiveIntegerField(default=10000)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teacher'
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.phone_number}'

    def save(self, *args, **kwargs):
        # self.age = relativedelta(datetime.date.today(), self.birthday).years
        #self.phone_number = phone_number_norm(self.phone_number)
        super().save(*args, **kwargs)

    # def get_age(self):
    #     return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        groups = Group.objects.all()
        obj.group = random.choice(groups)
        obj.salary = random.randint(10000, 99000)
        obj.save()
