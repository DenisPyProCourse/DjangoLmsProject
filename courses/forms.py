from django import forms

from .models import Course
from django_filters import FilterSet


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'group_name': ['exact', 'icontains'],
        }


class CourseUpdateForm(CourseCreateForm):
    class Meta(CourseCreateForm.Meta):
        exclude = ['start_date']