from django.db import models
from simple_history.models import HistoricalRecords

from employees.models import FileStore
from usersapp.models import BaseModel, MyUsers
CUST_TYPE = (
    ('normal', 'Normal'),
    ('abnormal', 'Abnormal')
)


class Address(BaseModel):
    address_line_1 = models.CharField(max_length=250, null=True, blank=True)
    address_line_2 = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=120, null=True, blank=True)
    pincode = models.CharField(max_length=9, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Addresses"


class Customers(BaseModel):
    user = models.OneToOneField(MyUsers, on_delete=models.CASCADE)
    documents = models.ManyToManyField(FileStore, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    cust_type = models.CharField(max_length=20, choices=CUST_TYPE, default='normal')

    class Meta:
        verbose_name_plural = "Customers"

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        self.save()
