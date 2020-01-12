from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse


from students.models import Student, Group
from students.forms import StudentsAddForm, GroupsAddForm, ContactForm


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
        response += student.get_info() + f'<a href="{reverse("students-edit-for-link")}{student.id}">' \
                                         f'<br>Edit</a>' + '<br>' + '<br>'
    return render(request, 'students_list.html', context={'students_list': response})


def generate_group(request):
    return HttpResponse(Group.generate_group())


def groups(request):
    queryset = Group.objects.all()
    response = ''
    fn = request.GET.get('name')
    if fn:
        queryset = queryset.filter(name__contains=fn)
        queryset = queryset.filter(name__contains=fn)
    for group in queryset:
        response += group.get_info() + f'<a href="{reverse("groups-edit-for-link")}{group.id}">' \
                                       f'<br>Edit</a>' + '<br>' + '<br>'
    return render(request, 'groups_list.html', context={'groups_list': response})


def students_add(request):
    if request.method == "POST":
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
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
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm()
    return render(request,
                  'groups_add.html',
                  context={'form': form})


def students_edit(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student with id {pk} not found')
    if request.method == "POST":
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm(instance=student)
    return render(request,
                  'students_edit.html',
                  context={'form': form, 'pk': pk})


def groups_edit(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Group with id {pk} not found')
    if request.method == "POST":
        form = GroupsAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm(instance=group)
    return render(request,
                  'groups_edit.html',
                  context={'form': form, 'pk': pk})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = ContactForm()
    return render(request,
                  'contact.html',
                  context={'form': form})
