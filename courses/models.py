from core.models import GroupModel

from django.db import models

# Create your models here.
from teachers.models import Teacher


class Course(GroupModel):
    # students_number = models.PositiveIntegerField()

    group = models.OneToOneField(
        'groups.Group',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='course_of_group'
    )
    teachers = models.ManyToManyField(
        to=Teacher,
        null=True,
        blank=True,
        related_name='courses'
    )

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        db_table = 'courses'

    def __str__(self):
        return f'{self.group_name}'
