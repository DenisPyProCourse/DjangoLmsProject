from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .forms import CourseCreateForm, CourseFilterForm, CourseUpdateForm
from .models import Course


def get_course(request):

    gr = Course.objects.all()
    courses_filter = CourseFilterForm(data=request.GET, queryset=gr)

    return render(
        request,
        'courses/list.html',
        {'courses_filter': courses_filter}
    )


def create_course(request):
    if request.method == 'GET':
        form = CourseCreateForm()
    else:
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/create.html',
        context={'form': form}
    )


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'GET':
        form = CourseUpdateForm(instance=course)
    else:
        form = CourseUpdateForm(request.POST, instance=course)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/update.html', {'form': form, 'course': course})


def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/delete.html', {'course': course})
