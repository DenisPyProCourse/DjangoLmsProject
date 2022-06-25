from django.contrib import admin

# Register your models here.
from courses.models import Course


class TeachersInlineTable(admin.TabularInline):
    model = Course.teachers.through
    model.readonly_fields = 'teachers'
    extra = 0

    # def has_add_permission(self, request, obj):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False

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