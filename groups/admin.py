from django.contrib import admin

# Register your models here.
from groups.models import Group
from students.models import Student


class StudentsInlineTable(admin.TabularInline):
    model = Student
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
    ]

    extra = 0
    readonly_fields = fields
    # [
    #     'first_name',
    #     'last_name',
    # ]
    # show_change_link = True
    #

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_name',
        'start_date',
        'end_date',
        'headman',
        'headteacher'
    ]

    fields = [
        'group_name',
        ('start_date', 'end_date'),
        'headman',
        'headteacher',
        ('create_datetime', 'update_datetime')
    ]

    readonly_fields = ['create_datetime', 'update_datetime']

    inlines = [StudentsInlineTable, ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        form.base_fields['headteacher'].widget.can_add_related = False
        return form


admin.site.register(Group, GroupAdmin)