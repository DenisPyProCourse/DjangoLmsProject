from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .forms import StudentCreateForm
from .models import Student
from .utils import qs2html

from webargs.fields import Str, Int
from webargs.djangoparser import use_args



def index(request):
    # return HttpResponse('LMS System!')
    return render(
        request,
        'students/index.html',
        {'title': 'Django LMS', 'Welcome': 'Welcome to DjangoLMS!'}
    )


@use_args(
    {
        'first_name': Str(required=False),       # , missing=None)
        'last_name': Str(required=False),
        'age': Int(required=False)
    },
    location='query'
)
def get_students(request, args):
    st = Student.objects.all()
    for key, value in args.items():
        st = st.filter(**{key: value})      # key=value

    # html_form = """
    #     <form method="get">
    #         <label for="fname">First name:</label><br>
    #         <input type="text" id="fname" name="first_name" placeholder="Bob"><br>
    #         <label for="lname">Last name:</label><br>
    #         <input type="text" id="lname" name="last_name" placeholder="Dilan"><br>
    #         <label for="age_id">Age:</label><br>
    #         <input type="number" id="age_id" name="age" placeholder="45"><br>	<br>
    #
    #         <input type="submit" value="Search">
    #     </form>
    # """
    # html = qs2html(st)
    # response = html_form + html

    # return HttpResponse(response)
    return render(
        request,
        'students/list.html',
        {'title': 'List of students', 'students': st}
    )


@csrf_exempt
def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    else:
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/students/')

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
def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)
    else:
        form = StudentCreateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/students/')

    html_form = f"""
            <form method="post">
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Update">
            </form> 
        """

    return HttpResponse(html_form)
