from django.db import models

from customers.models import Customers
from usersapp.models import BaseModel, MyUsers


class Passbook(BaseModel):
    customer = models.OneToOneField(Customers, on_delete=models.CASCADE)
    total_money = models.DecimalField(max_digits=10, decimal_places=2, default=0)


PAYMENT_STATUS = (
    ("completed", "Completed"),
    ("processing", "Processing"),
    ("pending", "Pending"),
    ("initiated", "Initiated")
)


class Transactions(BaseModel):
    user = models.ForeignKey(MyUsers, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=24, choices=PAYMENT_STATUS, default='initiated')
    details = models.JSONField(null=False)

    class Meta:
        verbose_name_plural = 'Transactions'
