from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='login'),
    #path('vendor/', views.add_vendor, name='add_vendor'),
   path('product/', views.add_product, name='add_product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('vendor-list/', views.vendor_list, name='vendor_list'),
    path('product-list/', views.product_list, name='product_list'),
    path('customer-login/', views.user_login, name='customer_login'),
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('vendor-login/', views.vendor_login, name='vendor_login'),
    path('vendor-dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('logout/', views.user_logout, name='logout'),

]

