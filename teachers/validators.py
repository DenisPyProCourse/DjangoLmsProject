import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

ADULT_AGE_LIMIT = 25


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 25 y.o.')

def phone_number_norm(phone_number):
    for i in phone_number:
        if not i.isdigit():
            phone_number = phone_number.replace(i, '')
    return phone_number

def phone_number_validator(phone_number):
    from .models import Teacher
    # teachers = Student.objects.filter(phone_number=phone_number)
    correct_number = phone_number_norm(phone_number)
    result = Teacher.objects.filter(phone_number=correct_number).exists()
    # if len(teachers) > 0:
    if result:
        raise ValidationError(f'Phone number {correct_number} is not unique.')
    if len(correct_number) != 12:
        raise ValidationError(f'Phone number {correct_number} must include 12 digits.')
    if not correct_number.isdigit():
        raise ValidationError(f'Phone number {correct_number} must include only digits.')


@deconstructible
class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, *args, **kwargs):
        age = datetime.date.today().year - args[0].year
        if age < self.age_limit:
            raise ValidationError(f'Age should be greater than {self.age_limit} y.o.')