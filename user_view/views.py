from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from product.models import Product
from product.forms import AddProduct


@login_required
def users_products(request):

    product = Product.objects.filter(user=request.user)
    return render(request, 'user_view/user_products.html', context={'product': product})


def update_product(request, pk):
    product_to_update = get_object_or_404(Product, id=pk)
    update_form = AddProduct(request.POST or None, request.FILES or None, instance=product_to_update)
    if request.method == 'GET':
        return render(request, 'user_view/update_product.html',
                      context={'update_form': update_form, 'product_to_update': product_to_update})

    if request.method == 'POST':
        if update_form.is_valid():
            update_form.save()
        else:
            messages.error(request, "You can't add negative value")
            return render(request, 'user_view/update_product.html')
        return redirect('product:auctions')


def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'GET':
        return render(request, 'user_view/delete_product.html', context={'product': product})

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm:
            product.delete()

    return redirect('user_view:user_products')
