from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Int, Str

from .forms import GroupCreateForm, GroupFilterForm, GroupUpdateForm
from .models import Group


def get_group(request):

    gr = Group.objects.all()
    groups_filter = GroupFilterForm(data=request.GET, queryset=gr)

    return render(
        request,
        'groups/list.html',
        {'groups_filter': groups_filter}
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
        form = GroupUpdateForm(instance=group)
    else:
        form = GroupUpdateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
