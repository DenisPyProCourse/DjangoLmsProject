from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher
from .utils import qs2html, gen2html
from webargs.fields import Str, Int
from webargs import fields
from webargs.djangoparser import use_args, use_kwargs

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
    html = qs2html(tc)
    return HttpResponse(html)

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