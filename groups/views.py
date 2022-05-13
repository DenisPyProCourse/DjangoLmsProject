from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Group
from .utils import qs2html
from webargs.fields import Str, Int
from webargs import fields
from webargs.djangoparser import use_args, use_kwargs
from .forms import GroupCreateForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

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

@csrf_exempt
def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/groups/')

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
def update_group(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    else:
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/groups/')

    html_form = f"""
            <form method="post">
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Update">
            </form> 
        """

    return HttpResponse(html_form)