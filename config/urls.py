from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('03.14/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('blog.urls')),
    # url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
