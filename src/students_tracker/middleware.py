import time


from students.models import Logger
from students import model_choices as mch


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        response = self.get_response(request)

        end = time.time()
        full_time = end - start
        admin_url = '/admin/'
        if request.path.startswith(admin_url):
            Logger.objects.create(
                path=request.path,
                method=mch.METHOD_CHOICES_REVERSED[request.method],
                time_delta=full_time,
                user_id=request.user.pk,
                user_name=request.user.username
            )

        return response
