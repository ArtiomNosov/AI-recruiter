from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('home/', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('download/', include('download.urls')),
    path('view_resume/', include('view_resume.urls')),
    path('payment/', include('payment.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)