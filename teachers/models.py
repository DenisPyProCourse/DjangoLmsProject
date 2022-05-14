import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from .validators import adult_validator
from .validators import phone_number_validator
from .validators import phone_number_norm
# Create your models here.


class Teacher(models.Model):
    teacher_first_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    teacher_last_name = models.CharField(max_length=100)
    birthday = models.DateField(
        default=datetime.date.today,
        validators=[adult_validator]
        # validators=[AdultValidator(20)]
    )
    phone_number = models.CharField(max_length=25, null=True, validators=[phone_number_validator,
                                                                          phone_number_norm])

    def __str__(self):
        return f'{self.teacher_first_name} {self.teacher_last_name}, age {self.age} - {self.phone_number}'

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        self.phone_number = phone_number_norm(self.phone_number)
        super().save(*args, **kwargs)

    # def delete_t(self, t_id):
    #     tc = Teacher.objects.get(id=t_id)
    #     return tc.delete()

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