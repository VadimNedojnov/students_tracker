import time


from students.models import Logger


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        response = self.get_response(request)

        end = time.time()
        full_time = end - start
        full_path = request.build_absolute_uri()
        if '/admin/' in full_path:
            Logger.objects.create(path=full_path, method=request.method, time_delta=full_time,
                                  user_id=int(request.user.pk), user_name=request.user.username)

        return response
