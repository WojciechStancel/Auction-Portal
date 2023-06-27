from django.shortcuts import render, redirect
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


def orders(request):
    order = Order.objects.get(customer=request.user)
    order_view = OrderItem.objects.filter(order=order)
    return render(request, 'main_app/orders.html', context={'order_view': order_view})
