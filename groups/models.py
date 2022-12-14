from core.models import GroupModel
from django.db import models

# Create your models here.


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
        related_name='headteacher_group',
        # verbose_name='Headteacher of group: '
    )

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name}'
