from django.contrib import admin    # noqa

# Register your models here.
from groups.models import Group
from teachers.models import Teacher
from courses.models import Course

class CoursesInlineTable(admin.TabularInline):
    model = Course.teachers.through
    # fields = [
    #     'group_name',
    #     'start_date',
    #     'end_date',
    #     'group',
    # ]

    extra = 0
    # readonly_fields = fields


    # def has_add_permission(self, request, obj):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


class TeacherAdmin(admin.ModelAdmin):


    list_display = [
        'first_name',
        'last_name',
        'show_courses'
    ]
    list_display_links = list_display
    list_per_page = 15
    search_fields = [
        'first_name',
        'last_name'
    ]
    list_filter = [
        'courses'
    ]
    fields = [
        ('first_name', 'last_name'),
        ('birthday', 'age'),
        'phone_number',
        'headteacher_group'
    ]

    readonly_fields = ['birthday', 'age', 'headteacher_group']

    inlines = [CoursesInlineTable, ]

    def age(self, instance):
        return instance.get_age()

    def show_courses(self, obj):
        return "\n".join([f' {[a.group_name]}; ' for a in obj.courses.all()])



    age.short_description = 'Age of teacher'
    show_courses.short_description = 'Course'



admin.site.register(Teacher, TeacherAdmin)