from django.db import models
from product.models import Product
from user_view.models import User


class ShoppingCart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)


class ShoppingCartItem(models.Model):
    cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product_item)
