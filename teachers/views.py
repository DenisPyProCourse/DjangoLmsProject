from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
    paginate_by = 15

    def get_filter(self):
        return TeacherFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('headteacher_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter().form

        return context

    # def get_queryset(self):
    #     teachers_filter = TeacherFilterForm(
    #         data=self.request.GET,
    #         queryset=self.model.objects.all().select_related('headteacher_group')
    #     )
    #
    #     return teachers_filter


@login_required
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


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
    form_class = TeacherCreateForm


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
