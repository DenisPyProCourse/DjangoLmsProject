from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from groups.models import Group

from .forms import CourseCreateForm, CourseFilterForm, CourseUpdateForm

from .models import Course


class ListCoursesView(ListView):
    model = Course
    template_name = 'courses/list.html'
    paginate_by = 5

    def get_filter(self):
        return CourseFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter().form

        return context

    # def get_queryset(self):
    #     courses_filter = CourseFilterForm(
    #         data=self.request.GET,
    #         queryset=self.model.objects.all()
    #     )
    #
    #     return courses_filter


class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            form.instance.group = Group.objects.get(pk=form.cleaned_data['create_group'])
            form.instance.save()
        except ValueError:
            pass

        return response


class UpdateCourseView(LoginRequiredMixin, UpdateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'
    form_class = CourseUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = self.get_object().teachers.prefetch_related('courses')
        # context['groups'] = self.get_object().groups.pregetch_related('course_of_group')
        # context['groups'] = self.object.group
        return context


class DeleteCourseView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
