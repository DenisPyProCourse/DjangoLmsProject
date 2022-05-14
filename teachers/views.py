from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Teacher
from .utils import qs2html, gen2html
from webargs.fields import Str, Int
from webargs import fields
from webargs.djangoparser import use_args, use_kwargs
from .forms import TeacherCreateForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

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

@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/teachers/')

    html_form = f"""
            <form method="post">
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Create">
            </form> 
        """

    return HttpResponse(html_form)

@csrf_exempt
def update_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    else:
        form = TeacherCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/teachers/')

    html_form = f"""
            <form method="post">
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Update">
            </form> 
        """

    return HttpResponse(html_form)

@csrf_exempt
def delete_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    teacher.delete()


    return HttpResponseRedirect('/teachers/')

