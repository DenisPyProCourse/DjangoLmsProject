from django import forms

from .models import Teacher
from django_filters import FilterSet


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            # '__all__'
            'teacher_first_name',
            'teacher_last_name',
            'phone_number',
            # 'age',
            'birthday'

        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    # cleaned_date
    def clean_first_name(self):
        fn = self.cleaned_data['teacher_first_name']
        return fn.title()

    def clean_last_name(self):
        ln = self.cleaned_data['teacher_last_name']
        return ln.title()


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'teacher_first_name': ['exact', 'icontains'],
            'teacher_last_name': ['exact', 'startswith'],
        }