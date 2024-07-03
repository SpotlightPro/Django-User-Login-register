from django.shortcuts import render, redirect
from .forms import Product, ProductForm
from .models import Product


# Create your views here.
# GRUD = Create, Read, Update, Delete


# Home view
def home_view(request):
    return render(request, 'invApp/home.html')


# Create veiw
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.seve()
            return redidect('product_list')
        return render('invApp/product_form.html', {'form': form})


# Read view
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})


# Update view
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instanse=product)
    if request == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return redirect('invApp/product_form.html', {'form': form})

# Delete view
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request == 'POST':
        product.delete()
        return redirect('product_list')
    return redirect('invApp/product_confirm_delete.html', {'product': product})


