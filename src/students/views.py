from django.http import HttpResponse


from .models import Student


def generate_student(request):
    return HttpResponse(Student.generate_student())


