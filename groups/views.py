from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Group
from webargs.fields import Str, Int
from webargs.djangoparser import use_args
from .forms import GroupCreateForm


@use_args(
    {
        'group_name': Str(required=False),
        'teacher_last_name': Str(required=False),
        'students_number': Int(required=False)
    },
    location = 'query'
)
def get_group(request, args):

    gr = Group.objects.all()
    for key, values in args.items():
        gr = gr.filter(**{key: values})
    return render(
        request,
        'groups/list.html',
        {'title': 'List of groups', 'groups': gr}
    )
    # html = qs2html(gr)
    # return HttpResponse(html)


def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    else:
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/update.html', {'form': form})


def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))


    return render(request, 'groups/delete.html', {'group': group})