from django import forms

from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            # '__all__'
            'group_name',
            'students_number',
            'teacher_last_name',

        ]

        # widgets = {
        #     'birthday': forms.DateInput(attrs={'type': 'date'})
        # }

    # cleaned_date
    # def clean_first_name(self):
    #     fn = self.cleaned_data['first_name']
    #     return fn.title()
    #
    # def clean_last_name(self):
    #     ln = self.cleaned_data['last_name']
    #     return ln.title()
