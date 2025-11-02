from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
 
# from django qrcodegen.views import qrcode_gen
 
 
 

urlpatterns = [
    
    path('',views.home,name='home'),
    path('',views.logout,name='logout'),
    path('dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('sel/man/',views.selsman,name='selsman'),
    path('newpage/forbuyer/',views.newpage_forbuyer,name='newpage_forbuyer'),
    path('buyer/pro/',views.buyers,name='buyers'),
    path('product/',views.product,name='product'),
    path('list/popoler/product/',views.list_populer_product,name='list_populer_product'),
    path('product/entry/',views.product_entry,name='product_entry'),
    path('category/products/',views.category_products,name='category_products'),
    path('buyproduct/<int:id>/', views.buyproduct, name='buyproduct'),
 
 
 
]
 