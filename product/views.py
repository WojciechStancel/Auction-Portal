from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category
from .forms import AddProduct


def auction_view(request):
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.get_all_products_by_category_id(category_id)
    else:
        products = Product.objects.all()

    return render(request, 'product/product_list.html', context={'products': products, 'categories': categories})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product.quantity == 0:
        messages.info(request, 'Sorry, this product is out of stock')
    return render(request, 'product/product_detail.html', context={'product': product})


@login_required(login_url='accounts:login')
def add_product(request):

    form = AddProduct(request.POST or None, request.FILES)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('product:auctions')
    return render(request, 'product/add_product.html', context={'form': form})


def search_by_name(request):
    search_query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=search_query)
    return render(request, 'product/search.html', context={'results': results})