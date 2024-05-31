from django.contrib.auth.middleware import get_user
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from simple_history.signals import pre_create_historical_record, post_create_historical_record

from employees.models import Employees
from usersapp.models import UsersLog
@receiver(post_create_historical_record)
def log_activity(sender, instance, history_instance, **kwargs):
    print("Im in signal")
    print("sender", sender)
    print("instance", instance)
    print("hu",history_instance)
    if history_instance.history_user:
        action = 'created' if history_instance.history_type == '+' else 'deleted' if history_instance.history_type == '-' else 'updated'
        changes = ''
        if history_instance.prev_record:
            diff = history_instance.diff_against(history_instance.prev_record)
            changes = ', '.join(f'{change.field}: {change.old} -> {change.new}' for change in diff.changes)
        description = "dp"
        status_code = 200
        object_repr = str(history_instance.history_object)
        print("user is", history_instance.history_user)
        print("action", action)
        UsersLog.objects.create(
            user=history_instance.history_user,
            action=action,
            description=description,
            status_code=status_code,
            changes=changes,
            object_repr=object_repr
        )

