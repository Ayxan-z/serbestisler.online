from django.conf import settings
from django import http

class BlockedIpMiddleware:
    def __init__(self, get_response):
            self.get_response = get_response

    def __call__(self, request):
        BLOCKED_IPS = ['46.228.176.95']
        if request.META['REMOTE_ADDR'] in BLOCKED_IPS:
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')

        return self.get_response(request)
        