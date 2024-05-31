from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from customers.models import Address, Customers


class CustAdmin(admin.ModelAdmin):
    list_display = ['user', 'cust_type']


admin.site.register(Address)
admin.site.register(Customers, SimpleHistoryAdmin)
