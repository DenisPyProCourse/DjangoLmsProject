#
# from django.core.exceptions import ValidationError
#
#
# def phone_number_norm(phone_number):
#     for i in phone_number:
#         if not i.isdigit():
#             phone_number = phone_number.replace(i, '')
#     return phone_number
#
#
# def phone_number_validator(phone_number):
#     from .models import Teacher
#     correct_number = phone_number_norm(phone_number)
#     result = Teacher.objects.filter(phone_number=correct_number).exists()
#     # if result:
#     #     raise ValidationError(f'Phone number {correct_number} is not unique.')
#     # if len(correct_number) != 12:
#     #     raise ValidationError(f'Phone number {correct_number} must include 12 digits.')
#     if not correct_number.isdigit():
#         raise ValidationError(f'Phone number {correct_number} must include only digits.')
