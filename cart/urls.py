from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [

    path('cart/<int:pk>/', views.add_to_shopping_cart, name='add_to_shopping_cart'),
    path('cart_view/', views.cart_view, name='cart_view'),
    path('order_complete/', views.buy_now, name='order_complete'),
    path('remove/<int:pk>/', views.cart_remove, name='cart_remove'),
    path('update_cart/<int:pk>/', views.update_cart, name='update_cart'),

]