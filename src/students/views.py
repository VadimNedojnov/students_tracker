from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, authenticate


from students.models import Student, Group, Logger
from students.forms import StudentsAddForm, GroupsAddForm, ContactForm, \
    UserRegistrationForm, LoginUserForm


def generate_student(request):
    return HttpResponse(Student.generate_student())


def students(request):
    queryset = Student.objects.all().select_related('group')
    # response = ''
    fn = request.GET.get('name')
    if fn:
        # __contains = LIKE %{}%
        # queryset = queryset.filter(first_name__contains=fn)
        # __contains = LIKE %{}
        # queryset = queryset.filter(first_name__endswith=fn)
        # __contains = LIKE {}%
        queryset = queryset.filter(first_name__istartswith=fn)
    # for student in queryset:
    #     response += student.get_info() + f'<a href="{reverse("students-edit", args=[student.id])}">' \
    #                                      f'<br>Edit</a>' + '<br>' + '<br>'
    return render(request, 'students_list.html', context={'students': queryset, 'page_title': 'Students List'})


def generate_group(request):
    return HttpResponse(Group.generate_group())


def groups(request):
    queryset = Group.objects.all().select_related('group_leader_name', 'headman')
    fn = request.GET.get('name')
    if fn:
        queryset = queryset.filter(name__contains=fn)
    return render(request, 'groups_list.html', context={'groups': queryset, 'page_title': 'Groups List'})


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
                  context={'form': form, 'page_title': 'Add Students'})


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
                  context={'form': form, 'page_title': 'Add Group'})


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
                  context={'form': form, 'pk': pk, 'page_title': 'Edit Students'})


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
                  context={'form': form, 'pk': pk, 'page_title': 'Edit Group'})


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


def admin_logger(request):
    queryset = Logger.objects.all()
    fn = request.GET.get('name')
    if fn:
        queryset = queryset.filter(name__contains=fn)
    return render(request, 'admin_logger_list.html', context={'admin_logger': queryset,
                                                              'page_title': 'Admin Logger List'})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = UserRegistrationForm()
    return render(request,
                  'registration.html',
                  context={'form': form, 'page_title': 'Registration'})


def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password']
                                )
            login(request, user)
            return HttpResponseRedirect(reverse('students'))
    else:
        form = LoginUserForm()
    return render(request,
                  'login_user.html',
                  context={'form': form, 'page_title': 'Login'})
