from django.db import models
from simple_history import register
from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model
from bankcrm import settings
from usersapp.models import MyUsers, BaseModel
from auditlog.registry import auditlog
# User = settings.AUTH_USER_MODEL
User = get_user_model()
EMP_ROLES = (
    ('manager', 'Manager'),
    ('ast_manager', 'Ast Manager'),
    ('clerk', 'Clerk')
)


class FileStore(BaseModel):
    file = models.FileField(upload_to="uploads/")


class Employees(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=150)
    role = models.CharField(max_length=50, choices=EMP_ROLES, default='clerk')
    joining_documents = models.ManyToManyField(FileStore, null=True, blank=True)
    verified = models.BooleanField(default=False)
    # changed_by = models.ForeignKey(MyUsers, on_delete=models.CASCADE, related_name="changed_by_related", null=True)
    # history = HistoricalRecords(user_model=MyUsers)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        self.save()

    class Meta:
        verbose_name_plural = 'Employees'

class Product(BaseModel):
    name = models.CharField(max_length=54)
    product_location = models.CharField(max_length=77)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        self.save()
