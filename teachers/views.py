from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webargs.djangoparser import use_kwargs
from webargs.fields import Int

from .forms import TeacherCreateForm, TeacherFilterForm
from .models import Teacher
from .utils import gen2html


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        teachers_filter = TeacherFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('headteacher_group')
        )

        return teachers_filter


@use_kwargs(
    {
        'cnt': Int(required=False, missing=10),
    },
    location='query'
)
def generate_teachers(request, cnt):
    Teacher.generate(cnt)
    tc = Teacher.objects.order_by('-pk')[:cnt]
    html = gen2html(tc)
    return HttpResponse(html)


class CreateTeacherView(CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class UpdateTeacherView(UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
    form_class = TeacherCreateForm


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
