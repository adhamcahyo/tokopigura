from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('catalog/', views.catalog_view, name='catalog'),  # Make sure this line exists
    path('digital-product/', views.digital_product, name='digital_product'),
    path('admin/', views.admin_dashboard_view, name='admin_dashboard')



]