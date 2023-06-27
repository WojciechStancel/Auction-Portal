from django.db import models


class Order(models.Model):
    customer = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)