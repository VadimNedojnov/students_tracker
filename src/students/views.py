from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from students.models import Student, Group
from students.forms import StudentsAddForm, GroupsAddForm


def generate_student(request):
    return HttpResponse(Student.generate_student())


def students(request):
    queryset = Student.objects.all()
    response = ''
    fn = request.GET.get('first_name')
    if fn:
        # __contains = LIKE %{}%
        # queryset = queryset.filter(first_name__contains=fn)
        # __contains = LIKE %{}
        # queryset = queryset.filter(first_name__endswith=fn)
        # __contains = LIKE {}%
        queryset = queryset.filter(first_name__istartswith=fn)
    for student in queryset:
        response += student.get_info() + '<br>' + '<br>'
    return render(request, 'students_list.html', context={'students_list': response})


def generate_group(request):
    return HttpResponse(Group.generate_group())


def groups(request):
    queryset = Group.objects.all()
    response = ''
    fn = request.GET.get('name')
    if fn:
        queryset = queryset.filter(name__contains=fn)
    for group in queryset:
        response += group.get_info() + '<br>' + '<br>'
    return render(request, 'groups_list.html', context={'groups_list': response})


def students_add(request):
    if request.method == "POST":
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentsAddForm()
    return render(request,
                  'students_add.html',
                  context={'form': form})


def groups_add(request):
    if request.method == "POST":
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = GroupsAddForm()
    return render(request,
                  'groups_add.html',
                  context={'form': form})
