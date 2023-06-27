from django.contrib import admin
from product.models import Product, Category
from order.models import Order, OrderItem
from cart.models import ShoppingCart, ShoppingCartItem

admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
