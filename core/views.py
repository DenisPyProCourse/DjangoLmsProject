
from django.shortcuts import render


def index(request):
    return render(
        request,
        'core/index.html',
        {'title': 'Django LMS', 'Welcome': 'Welcome to DjangoLMS!'}
    )
#
# class UpdateBaseView:  #Like a option to use instead of generic
#     model = None
#     success_url = None
#     template_name = None
#     form_class = None
#
#
#     @classmethod
#     def update(cls, request, pk):
#         model_obj = get_object_or_404(cls.model, pk=pk)
#         if request.method == 'POST':
#             form = cls.form_class(request.POST, instance=model_obj)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect(reverse(cls.success_url))
#         else:
#             form = cls.form_class(instance=model_obj)
#
#         return render(
#             request,
#             cls.template_name,
#             {'form': form})
