from django.contrib import admin

# Register your models here.
from courses.models import Course


class TeachersInlineTable(admin.TabularInline):
    model = Course.teachers.through
    extra = 0
    can_delete = False

    fields = [
        'first_name',
        'last_name',
        'salary',
    ]

    readonly_fields = fields


    # def has_add_permission(self, request, obj):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
    def first_name(self, obj):

        return obj.teacher.first_name

    def last_name(self, obj):

        return obj.teacher.last_name

    def salary(self, obj):

        return obj.teacher.salary


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'group_name',
        'start_date',
        'end_date',
        'group'
    ]

    fields = [
        'group_name',
        ('start_date', 'end_date'),
        'group',
        ('create_datetime', 'update_datetime')
    ]

    readonly_fields = ['create_datetime', 'update_datetime']

    inlines = (TeachersInlineTable, )
    exclude = ('teachers',)



admin.site.register(Course, CourseAdmin)