import json

from django.utils.deprecation import MiddlewareMixin
from .models import AuditLog


class LogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method in ['POST', 'PUT', 'PATCH']:
            request._body = request.body

    def process_response(self, request, response):
        user = request.user if request.user.is_authenticated else None
        description = f"Called {request.method} method"
        # if request.method in ['POST', 'PUT', 'PATCH']:
        #     input_data = request.body.decode('utf-8')
        # else:
        #     input_data = None
        # if request.method in ['POST', 'PUT', 'PATCH']:
        #     input_data = request.POST.dict()
        # else:
        #     input_data = None
        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                input_data = json.loads(request._body)
            except json.JSONDecodeError:
                input_data = request._body
        else:
            input_data = None

        AuditLog.objects.create(
            user=user,
            action=request.method,
            api=request.path,
            description=description,
            status_code=response.status_code,
            success=request.user.is_authenticated,
            input_data=input_data
        )
        return response
