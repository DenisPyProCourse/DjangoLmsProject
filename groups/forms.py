# import datetime

from django import forms

from django_filters import FilterSet

from teachers.models import Teacher
from .models import Group


class GroupBaseForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
        # [
        #     'name',
        #     'start_date',
        #     'end_date'
        # ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class GroupFilterForm(FilterSet):

    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],

        }


class GroupUpdateForm(GroupBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[
                (student.pk, f'{student.first_name} {student.last_name}') for student in self.instance.students.all()
            ],
            label='Headman',
            required=False,
        )
        lst = [(self.instance.headteacher.pk, f'{self.instance.headteacher.first_name}'
                                              f' {self.instance.headteacher.last_name} [Now is active]')]
        for teacher in Teacher.objects.filter(headteacher_group=None):
            lst.append((teacher.pk, f'{teacher.first_name} {teacher.last_name} '))
        self.fields['headteacher_field'] = forms.ChoiceField(
            choices=[teacher for teacher in lst],
            label='Amend headteacher',
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        exclude = ['start_date', 'headman', 'headteacher']


class GroupCreateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['headteacher_field'] = forms.ChoiceField(
            choices=[
                (teacher.pk, f'{teacher.first_name} {teacher.last_name}') for teacher in Teacher.objects.filter(
                    headteacher_group=None)
            ],
            label='Headteacher',
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        exclude = ['end_date', 'headman', 'headteacher']

        # fields = [
        #     'group_name',
        #     'headman',
        #     'headteacher',
        #     'start_date',
        #     'end_date'
        # ]
