from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [

    path('order_view/', views.order_view, name='order_view'),

]