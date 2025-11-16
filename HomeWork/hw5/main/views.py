from django.shortcuts import render, redirect
from .forms import LoginForm, CustomAuthForm, ProductForm, ReviewForm
from .models import Category, Product, ProductReview

def home(request):
    return render(request, 'main/base.html')

def login_form(request):
    form = LoginForm()
    return render(request, 'main/login_form.html', {'form': form})

def custom_login_form(request):
    form = CustomAuthForm()
    return render(request, 'main/login_form.html', {'form': form})

def modelform_example(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductForm()

    return render(request, 'main/modelform_example.html', {'form': form})


def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ReviewForm()
    return render(request, 'main/review_form.html', {'form': form})

def success(request):
    return render(request, 'main/success.html')

def populate_example(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    reviews = ProductReview.objects.all()
    return render(request, 'main/populate.html', {'categories': categories, 'products': products, 'reviews': reviews})
