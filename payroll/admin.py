from django.contrib import admin

from payroll.models import Timesheet


class TimesheetAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'total_hours', 'period']


admin.site.register(Timesheet, TimesheetAdmin)
