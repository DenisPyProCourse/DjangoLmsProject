import datetime

from django.db import models

# Create your models here.
from core.models import GroupModel


class Group(GroupModel):
    # students_number = models.PositiveIntegerField()

    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group'
    )
    headteacher = models.OneToOneField(
        'teachers.Teacher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headteacher_group'
    )
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name}'
