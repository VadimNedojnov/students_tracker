from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q


from teachers.models import Teacher


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