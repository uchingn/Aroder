from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productbazare.urls')), 
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('qrcode/', include('qrcodegen.urls')),
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


