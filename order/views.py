from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Order, OrderItem


def start_order(request):
    try:
        order = Order.objects.get(customer=request.user)
        order.save()
    except ObjectDoesNotExist:
        order = Order.objects.create(customer=request.user)
        order.save()
    return order


def order_view(request):
    order = Order.objects.get(customer=request.user)
    orders = OrderItem.objects.filter(order=order)
    return render(request, 'order/orders.html', context={'orders': orders})
