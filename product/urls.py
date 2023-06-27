from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [

    path('auctions/', views.auction_view, name='auctions'),
    path('<int:pk>/', views.product_detail_view, name='product_detail_view'),
    path('add/', views.add_product, name='add'),
    path('search/', views.search_by_name, name='search'),
]