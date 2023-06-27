from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import ShoppingCart, ShoppingCartItem
from product.models import Product
from order.views import start_order
from order.models import OrderItem
from decimal import Decimal
# Create your views here.


def get_user_shopping_cart(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        try:
            cart = ShoppingCart.objects.get(user_id=request.user)
            cart.save()

        except ShoppingCart.DoesNotExist:
            cart = ShoppingCart(user_id=request.user)
            cart.save()

        return cart


@login_required
def add_to_shopping_cart(request, pk):
    cart = get_user_shopping_cart(request)
    product = get_object_or_404(Product, id=pk)
    show_cart = ShoppingCartItem.objects.filter(cart_id=cart)
    try:
        cart_item = ShoppingCartItem.objects.get(product_item=product, cart_id=cart)
        if cart_item.qty < cart_item.product_item.quantity:
            cart_item.product_item.quantity -= 1
            cart_item.qty += 1
        cart_item.product_item.save()
        cart_item.save()

    except ShoppingCartItem.DoesNotExist:
        cart_item = ShoppingCartItem.objects.create(product_item=product, cart_id=cart)
        cart_item.product_item.quantity -= 1
        cart_item.product_item.save()
        cart_item.save()

    context = {'cart': cart, 'product': product, 'cart_item': cart_item, 'show_cart': show_cart}
    return render(request, 'cart/shopping_cart.html', context=context)


@login_required
def cart_view(request):
    cart = get_user_shopping_cart(request)
    show_cart = ShoppingCartItem.objects.filter(cart_id=cart)
    order_total = Decimal(0.0)
    buy = buy_now(request)
    total_quantity = 0
    if buy:
        return render(request, 'cart/order_complete.html', context={'show_cart': show_cart})

    for item in show_cart:
        order_total += item.product_item.price * item.qty

    for quantity in show_cart:
        total_quantity += quantity.qty

    return render(request, 'cart/cart_view.html',
                  context={'show_cart': show_cart, 'order_total': order_total, 'total_quantity': total_quantity})


def buy_now(request):
    order_init = start_order(request)
    cart = get_user_shopping_cart(request)
    show_cart = ShoppingCartItem.objects.filter(cart_id=cart)
    if request.method == 'POST':
        bought = request.POST.get('buy')

        for order_item in show_cart:
            ord_itm = OrderItem.objects.create(order=order_init, product=order_item.product_item.name,
                                               quantity=order_item.qty)
            ord_itm.save()

        if bought:
            show_cart.delete()
        return redirect('main_app:order_complete')


def cart_remove(request, pk):
    cart = get_user_shopping_cart(request)
    product = get_object_or_404(Product, id=pk)
    cart_item = ShoppingCartItem.objects.get(product_item=product, cart_id=cart)
    if cart_item.qty > 0:
        cart_item.qty -= 1
        cart_item.save()
        cart_item.product_item.quantity += 1
        cart_item.product_item.save()

    if cart_item.qty == 0:
        cart_item.delete()
    return redirect("cart:cart_view")


def update_cart(request, pk):

    cart = get_user_shopping_cart(request)
    product = get_object_or_404(Product, id=pk)
    cart_item = ShoppingCartItem.objects.get(product_item=product, cart_id=cart)
    if cart_item.product_item.quantity > 0:
        cart_item.product_item.quantity -= 1
        cart_item.qty += 1
        cart_item.save()
        cart_item.product_item.save()
    else:
        messages.error(request, 'Sorry, there is no more this product in our auction right now')

    return redirect('cart:cart_view')