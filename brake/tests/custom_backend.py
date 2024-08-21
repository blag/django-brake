from brake.backends import cachebe

class MyBrake(cachebe.CacheBackend):
    def get_ip(self, request):
        return request.headers.get(
            'true-client-ip',
            request.META.get('REMOTE_ADDR')
        )
