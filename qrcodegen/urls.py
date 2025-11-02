from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
 
 
 
 

urlpatterns = [
    path('',views.qrcode_gen,name='qrcode_gen'),
    path('post/',views.posthome,name='posthome')
]
 