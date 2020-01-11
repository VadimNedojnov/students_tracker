from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


from teachers.models import Teacher
from teachers.forms import TeachersAddForm


def generate_teacher(request):
    return HttpResponse(Teacher.generate_teacher())


def teachers(request):
    queryset = Teacher.objects.all()
    response = ''
    fn = request.GET.get('parameter')
    if fn:
        queryset = queryset.filter(Q(first_name__contains=fn) |
                                   Q(last_name__contains=fn) | Q(email__contains=fn))
    for teacher in queryset:
        response += teacher.get_info() + '<br>' + '<br>'
    return render(request, 'teachers_list.html', context={'teachers_list': response})


def teachers_add(request):
    if request.method == "POST":
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeachersAddForm()
    return render(request,
                  'teachers_add.html',
                  context={'form': form})
