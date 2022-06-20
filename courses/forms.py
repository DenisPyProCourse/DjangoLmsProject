from django import forms

from groups.models import Group

from .models import Course

from django_filters import FilterSet


class CourseCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['create_group'] = forms.ChoiceField(
            choices=[
                (group.pk, f'{group.group_name}') for group in Group.objects.filter(course_of_group=None)
            ],
            label='Group',
            required=False
        )

    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
        exclude = ['group']


class CourseFilterForm(FilterSet):

    class Meta:
        model = Course
        fields = {
            'group_name': ['exact', 'icontains'],
        }


class CourseUpdateForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = [
            'group_name',
            'end_date',
            'group',
            'teachers'

        ]
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

        exclude = ['start_date', 'create_group']
