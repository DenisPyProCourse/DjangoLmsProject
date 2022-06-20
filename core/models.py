import datetime

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models    # noqa

# Create your models here.
from faker import Faker

from .validators import adult_validator


class PersonModel(models.Model):
    class Meta:
        abstract = True
    first_name = models.CharField(
        max_length=100,
        verbose_name='first_name',
        validators=[MinLengthValidator(2)],
        db_column='first_name'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last_name',
        validators=[MinLengthValidator(2)],
        db_column='last_name'
        )
    # age = models.PositiveIntegerField()
    birthday = models.DateField(
        default=datetime.date.today,
        validators=[adult_validator]
        # validators=[AdultValidator(20)]
    )
    phone_number = models.CharField(
        max_length=25,
        null=True,
        # validators=[phone_number_validator, phone_number_norm]
    )

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        fk = Faker()
        obj = cls(
            first_name=fk.first_name(),
            last_name=fk.last_name(),
            birthday=fk.date_between(start_date='-65y', end_date='-15y'),
            phone_number=fk.phone_number()
        )
        obj.save()
        return obj

    @classmethod
    def generate(cls, cnt):
        for i in range(cnt):
            cls._generate()


class GroupModel(models.Model):
    class Meta:
        abstract = True

    group_name = models.CharField(max_length=100, verbose_name='Name')
    # students_number = models.PositiveIntegerField()
    # teacher_last_name = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True)
    create_datetime = models.DateField(auto_now_add=True)
    update_datetime = models.DateField(auto_now=True)
