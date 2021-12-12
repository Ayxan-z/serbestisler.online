from django.conf import settings
from django import http

class BlockedIpMiddleware:
    def __init__(self, get_response):
            self.get_response = get_response

    def __call__(self, request):
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        ip = ip[:ip.rfind('.')]
        ip = ip[:ip.rfind('.')]
        if ip in settings.BLOCKED_IPS: # request.META['REMOTE_ADDR']
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')
        
        return self.get_response(request)
        

        
        