from django.contrib import admin

from transactions.models import Passbook, Transactions


class PassbookAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_money']


class TnxAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'status']


admin.site.register(Passbook, PassbookAdmin)
admin.site.register(Transactions, TnxAdmin)
