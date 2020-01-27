from django.contrib import admin


from teachers.models import Teacher
from students.admin import GroupInline
from teachers.forms import TeacherAdminForm


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('subject', )
    list_display = ('id', 'first_name', 'last_name', 'email', 'subject')
    list_per_page = 10
    inlines = (GroupInline, )
    form = TeacherAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('telephone', )
        return readonly_fields


admin.site.register(Teacher, TeacherAdmin)
