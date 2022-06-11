from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

# from webargs.djangoparser import use_args
# from webargs.fields import Int, Str

from .forms import StudentCreateForm
from .forms import StudentFilterForm
from .models import Student


# @use_args(
#     {
#         'first_name': Str(required=False),       # , missing=None)
#         'last_name': Str(required=False),
#         'age': Int(required=False)
#     },
#     location='query'
# )
def get_students(request):  # args par was in that field
    st = Student.objects.all().select_related('group', 'headman_group')
    students_filter = StudentFilterForm(data=request.GET, queryset=st)
    # for key, value in args.items():         # use with decorator use_args
    #     st = st.filter(**{key: value})      # key=value
    return render(
        request,
        'students/list.html',
        {'students_filter': students_filter}
    )


def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    else:
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)
    else:
        form = StudentCreateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request,
        'students/update.html',
        {'form': form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/delete.html', {'student': student})
