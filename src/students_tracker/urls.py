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
from django.urls import path, include


from students.views import generate_group, groups_add, groups, groups_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('group/', generate_group),
    path('groups/list/', groups, name='groups'),
    path('groups/add/', groups_add, name='groups-add'),
    path('groups/edit/<int:pk>/', groups_edit, name='groups-edit'),
    path('groups/edit/', groups_edit, name='groups-edit-for-link'),
]
