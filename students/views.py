# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

# from webargs.djangoparser import use_args
# from webargs.fields import Int, Str
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

# from core.views import UpdateBaseView
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
# def get_students(request):  # args par was in that field
#     st = Student.objects.all().select_related('group', 'headman_group')
#     students_filter = StudentFilterForm(data=request.GET, queryset=st)
#     # for key, value in args.items():         # use with decorator use_args
#     #     st = st.filter(**{key: value})      # key=value
#     return render(
#         request,
#         'students/list.html',
#         {'students_filter': students_filter}
#     )

class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'
    paginate_by = 15

    def get_filter(self):
        return StudentFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_group')
        )


    def get_queryset(self):

        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter().form

        # params = self.request.GET
        # if 'page' in params:
        #     params = copy(params)
        #     del params['page']
        #
        # context['params'] = f'&{params.urlencode()}' if params else ''

        return context


# def create_student(request):
#     if request.method == 'GET':
#         form = StudentCreateForm()
#     else:
#         form = StudentCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponseRedirect(reverse('students:list'))
#
#     return render(
#         request=request,
#         template_name='students/create.html',
#         context={'form': form}
#     )

class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'

# def update_student(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'GET':
#         form = StudentCreateForm(instance=student)
#     else:
#         form = StudentCreateForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     return render(
#         request,
#         'students/update.html',
#         {'form': form})


# class UpdateStudent(UpdateBaseView):
#     model = Student
#     success_url = 'students:list'
#     template_name = 'students/update.html'
#     form_class = StudentCreateForm

class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'
    form_class = StudentCreateForm
    pk_url_kwarg = 'identity'

# def delete_student(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('students:list'))
#     return render(request, 'students/delete.html', {'student': student})


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
