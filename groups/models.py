import datetime

from django.db import models

# Create your models here.


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    # students_number = models.PositiveIntegerField()
    # teacher_last_name = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True)
    create_datetime = models.DateField(auto_now_add=True)
    update_datetime = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name}'
