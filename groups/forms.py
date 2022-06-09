from django import forms

from .models import Group
from django_filters import FilterSet


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            # '__all__'
            'group_name',
            # 'students_number',
            # 'teacher_last_name',
            'start_date',
            'end_date'

        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

    # cleaned_date
    # def clean_first_name(self):
    #     fn = self.cleaned_data['first_name']
    #     return fn.title()
    #
    # def clean_last_name(self):
    #     ln = self.cleaned_data['last_name']
    #     return ln.title()


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
            # 'teacher_last_name': ['exact', 'startswith'],
        }

class GroupUpdateForm(GroupCreateForm):
    class Meta(GroupCreateForm.Meta):
        exclude = ['start_date']