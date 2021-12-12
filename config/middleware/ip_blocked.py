from django.conf import settings
from django import http

class BlockedIpMiddleware:
    def __init__(self, get_response):
            self.get_response = get_response

    def __call__(self, request):
        BLOCKED_IPS = ['46.228.176.95']
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        if ip in BLOCKED_IPS: # request.META['REMOTE_ADDR']
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')

        return self.get_response(request)
        