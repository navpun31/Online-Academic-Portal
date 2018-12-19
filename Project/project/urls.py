from django.views.generic import RedirectView
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/portal/')),

    url(r'^admin/', admin.site.urls),
    
    url('^api/v1/', include('social_django.urls', namespace='social')),

    url(r'^portal/', include('portal.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)