from django.urls import path
from user_view import views

app_name = 'user_view'

urlpatterns = [

    path('user_products/', views.users_products, name='user_products'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),

]