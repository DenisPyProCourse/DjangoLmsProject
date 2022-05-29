from django import forms

from .models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            # '__all__'
            'first_name',
            'last_name',
            'phone_number',
            # 'age',
            'birthday'

        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    # cleaned_date
    def clean_first_name(self):
        fn = self.cleaned_data['first_name']
        return fn.title()

    def clean_last_name(self):
        ln = self.cleaned_data['last_name']
        return ln.title()
