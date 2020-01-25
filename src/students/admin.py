from django.contrib import admin


from students.models import Student, Group


class StudentInline(admin.TabularInline):
    model = Student
    readonly_fields = ('email',)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('telephone', )
        return readonly_fields


class GroupInline(admin.TabularInline):
    model = Group
    readonly_fields = ('name', )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('start_lessons_time', )
        return readonly_fields


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('email', )
    list_display = ('id', 'first_name', 'last_name', 'email', 'group')
    list_select_related = ('group', )
    list_per_page = 10
    inlines = [GroupInline, ]


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = ('id', 'name', 'students_count', 'group_leader_name', 'headman', 'start_lessons_time')
    list_select_related = ('group_leader_name', 'headman', )
    list_per_page = 10
    inlines = [StudentInline, ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('start_lessons_time', )
        return readonly_fields


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
