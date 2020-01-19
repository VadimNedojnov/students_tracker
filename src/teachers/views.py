from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.db.models import Q
from django.urls import reverse


from teachers.models import Teacher
from teachers.forms import TeachersAddForm


def generate_teacher(request):
    return HttpResponse(Teacher.generate_teacher())


def teachers(request):
    queryset = Teacher.objects.all()
    fn = request.GET.get('parameter')
    if fn:
        queryset = queryset.filter(Q(first_name__contains=fn) |
                                   Q(last_name__contains=fn) | Q(email__contains=fn))
    return render(request, 'teachers_list.html', context={'teachers': queryset, 'page_title': 'Teachers List'})


def teachers_add(request):
    if request.method == "POST":
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm()
    return render(request,
                  'teachers_add.html',
                  context={'form': form, 'page_title': 'Add Teachers'})


def teachers_edit(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f'Teacher with id {pk} not found')
    if request.method == "POST":
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm(instance=teacher)
    return render(request,
                  'teachers_edit.html',
                  context={'form': form, 'pk': pk, 'page_title': 'Edit Teachers'})
