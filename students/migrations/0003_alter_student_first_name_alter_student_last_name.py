# Generated by Django 4.0.4 on 2022-05-21 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_options_alter_student_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(db_column='s_f_name', max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='fname'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(db_column='s_l_name', max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='lname'),
        ),
    ]