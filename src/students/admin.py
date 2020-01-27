from django.contrib import admin


from students.models import Student, Group
from students.forms import StudentAdminForm


class BaseGroupReadonlyFields:
    readonly_fields = ('name', )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('start_lessons_time', )
        return readonly_fields


class BaseStudentReadonlyFields:
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('telephone', )
        return readonly_fields


class StudentInline(BaseStudentReadonlyFields, admin.TabularInline):
    model = Student
    readonly_fields = ('email',)


class GroupInline(BaseGroupReadonlyFields, admin.TabularInline):
    model = Group


class StudentAdmin(BaseStudentReadonlyFields, admin.ModelAdmin):
    # readonly_fields = ('email', )
    list_display = ('id', 'first_name', 'last_name', 'email', 'group')
    list_select_related = ('group', )
    list_per_page = 10
    inlines = (GroupInline, )
    form = StudentAdminForm


class GroupAdmin(BaseGroupReadonlyFields, admin.ModelAdmin):
    list_display = ('id', 'name', 'students_count', 'group_leader_name', 'headman', 'start_lessons_time')
    list_select_related = ('group_leader_name', 'headman', )
    list_per_page = 10
    inlines = (StudentInline, )


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
