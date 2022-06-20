# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from django.shortcuts import render
# from django.core.exceptions import ValidationError
# from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

# from webargs.djangoparser import use_args
# from webargs.fields import Int, Str
from students.models import Student
from teachers.models import Teacher

from .forms import GroupCreateForm, GroupFilterForm, GroupUpdateForm

from .models import Group


# def get_group(request):
#
#     gr = Group.objects.all()
#     groups_filter = GroupFilterForm(data=request.GET, queryset=gr)
#
#     return render(
#         request,
#         'groups/list.html',
#         {'groups_filter': groups_filter}
#     )
#     # html = qs2html(gr)
#     # return HttpResponse(html)

class ListGroupView(ListView):
    model = Group
    template_name = 'groups/list.html'

    def get_queryset(self):
        groups_filter = GroupFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )

        return groups_filter

# def create_group(request):
#     if request.method == 'GET':
#         form = GroupCreateForm()
#     else:
#         form = GroupCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(
#         request=request,
#         template_name='groups/create.html',
#         context={'form': form}
#     )


class CreateGroupView(CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            form.instance.headteacher = Teacher.objects.get(pk=form.cleaned_data['headteacher_field'])
            form.instance.save()
        except ValueError:
            pass

        return response

# def update_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     if request.method == 'GET':
#         form = GroupUpdateForm(instance=group)
#     else:
#         form = GroupUpdateForm(request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(
#         request,
#         'groups/update.html',
#         {
#             'form': form,
#             # 'group': group
#             'students': group.students.prefetch_related('headman_group')
#         }
#     )

class UpdateGroupView(UpdateView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'
    form_class = GroupUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')
        try:
            peke = self.object.headteacher.pk
            if peke:
                context['teachers'] = Teacher.objects.filter(pk=peke)
            else:
                pass
        except:
            pass
        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
            initial['headteacher_field'] = self.object.headteacher.pk
        except AttributeError:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            form.instance.headman = Student.objects.get(pk=form.cleaned_data['headman_field'])
            form.instance.headteacher = Teacher.objects.get(pk=form.cleaned_data['headteacher_field'])
            form.instance.save()

        except ValueError:
            pass

        return response


# def delete_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     if request.method == 'POST':
#         group.delete()
#         return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(request, 'groups/delete.html', {'group': group})

class DeleteGroupView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
