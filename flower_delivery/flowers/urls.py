from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('catalog/', views.catalog, name='catalog'),
    path('order/', views.order, name='order'),
    path('order_history/', views.order_history, name='order_history'),
]

