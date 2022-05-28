from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Teacher
from .utils import gen2html
from webargs.fields import Str, Int

from webargs.djangoparser import use_args, use_kwargs
from .forms import TeacherCreateForm


@use_args(
    {
        'teacher_first_name': Str(required=False),
        'teacher_last_name': Str(required=False),
        'age': Int(required=False)
    },
    location = 'query'
)
def get_teacher(request, args):

    tc = Teacher.objects.all()
    for key, values in args.items():
        tc = tc.filter(**{key: values})
    # html = qs2html(tc)
    # return HttpResponse(html)
    return render(
        request,
        'teachers/list.html',
        {'title': 'List of teachers', 'teachers': tc})

@use_kwargs(
    {
        'cnt': Int(required=False, missing=10),
    },
    location = 'query'
)
def generate_teachers(request, cnt):
    Teacher.gen_teachers(cnt)
    tc = Teacher.objects.order_by('-pk')[:cnt]
    html = gen2html(tc)
    return HttpResponse(html)

def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect((reverse('teachers:list')))

    return render(
        request=request,
        template_name='teachers/create.html',
        context={'form': form}
    )

def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    else:
        form = TeacherCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/update.html', {'form': form})

def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/delete.html', {'teacher': teacher})

