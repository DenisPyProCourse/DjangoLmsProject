from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from webargs.djangoparser import use_args, use_kwargs
from webargs.fields import Int, Str

from .forms import TeacherCreateForm, TeacherFilterForm
from .models import Teacher
from .utils import gen2html


def get_teacher(request):
    tc = Teacher.objects.all()
    teachers_filter = TeacherFilterForm(data=request.GET, queryset=tc)
    # html = qs2html(tc)
    # return HttpResponse(html)
    return render(
        request,
        'teachers/list.html',
        {'teachers_filter': teachers_filter})


@use_kwargs(
    {
        'cnt': Int(required=False, missing=10),
    },
    location='query'
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
