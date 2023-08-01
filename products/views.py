from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/admin/product_list.html', {'products': products})

def home_view(request):
    return render(request, 'products/user/home.html')

def admin_dashboard_view(request):
    products = Product.objects.all()
    return render(request, 'products/admin/admin_dashboard.html', {'products': products})

def catalog_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'total_products': len(products),
        'products_per_row': 5,
        'rows': [products[i:i + 5] for i in range(0, len(products), 5)],
    }
    return render(request, 'products/user/catalog.html', context)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/admin/product_create.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/admin/product_update.html', {'form': form})

 

def digital_product(request): 
    return render(request, 'products/user/digital_product.html')