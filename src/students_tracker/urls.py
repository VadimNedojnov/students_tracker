"""students_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import generate_student, students, generate_group, groups
from teachers.views import generate_teacher, teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generate_student),
    path('teacher/', generate_teacher),
    path('group/', generate_group),
    path('students/', students),
    path('teachers/', teachers),
    path('groups/', groups),


]
