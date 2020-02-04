from django.urls import path


from students.views import (generate_student, students,
                            students_add, students_edit,
                            contact, admin_logger)
from students.views import (generate_group, groups_add,
                            groups, groups_edit)


urlpatterns = [
    path('gen', generate_student),
    path('list/', students, name='students'),
    path('add/', students_add, name='students-add'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('contact/', contact, name='contact'),
    path('admin_logger/', admin_logger, name='admin_logger'),
    path('groups/gen', generate_group),
    path('groups/list/', groups, name='groups'),
    path('groups/add/', groups_add, name='groups-add'),
    path('groups/edit/<int:pk>/', groups_edit, name='groups-edit'),
]
