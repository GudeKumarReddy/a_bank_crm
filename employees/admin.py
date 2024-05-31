from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from employees.models import Employees, Product


class EmpClass(admin.ModelAdmin):
    list_display = ('user', 'branch', 'role', 'verified')


# admin.site.register(Employees, EmpClass, EmpClass)
admin.site.register(Employees, SimpleHistoryAdmin)
admin.site.register(Product, SimpleHistoryAdmin)
