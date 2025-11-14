from django.shortcuts import render, HttpResponse
from .models import Author, Book, Category, Product, Customer, Order, OrderItem
from django.db import transaction

def index(request):
    return render(request, 'main/index.html')

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'main/authors.html', {'authors': authors})

def books_list(request):
    books = Book.objects.all()
    return render(request, 'main/books.html', {'books': books})

def products_list(request):
    products = Product.objects.all()
    return render(request, 'main/products.html', {'products': products})

def populate_data(request):
    with transaction.atomic():
        a1 = Author.objects.create(name='Іван Франко')
        a2 = Author.objects.create(name='Леся Українка')
        a3 = Author.objects.create(name='Тарас Шевченко')
        a4 = Author.objects.create(name='Микола Гоголь')
        a5 = Author.objects.create(name='Остап Вишня')

        b1 = Book.objects.create(title='Кайдашева сім\'я')
        b2 = Book.objects.create(title='Захар Беркут')
        b3 = Book.objects.create(title='Лісова пісня')
        b4 = Book.objects.create(title='Маруся Чурай')
        b5 = Book.objects.create(title='Сон')

        b1.authors.add(a1)
        b2.authors.add(a2, a3)
        b3.authors.add(a2)
        b4.authors.add(a1, a4)
        b5.authors.add(a3)

        cat1 = Category.objects.create(name='Ноутбуки')
        cat2 = Category.objects.create(name='Смартфони')

        p1 = Product.objects.create(name='MacBook Air M2', price=1500, category=cat1, stock=5)
        p2 = Product.objects.create(name='Dell XPS 13', price=1300, category=cat1, stock=3)
        p3 = Product.objects.create(name='iPhone 15', price=1200, category=cat2, stock=10)
        p4 = Product.objects.create(name='Samsung Galaxy S23', price=1100, category=cat2, stock=7)
        p5 = Product.objects.create(name='Xiaomi 14', price=800, category=cat2, stock=12)

        c1 = Customer.objects.create(first_name='Богдан', last_name='Войтов', email='bogdan@example.com')
        o1 = Order.objects.create(customer=c1)
        OrderItem.objects.create(order=o1, product=p1, quantity=1)
        OrderItem.objects.create(order=o1, product=p3, quantity=2)
    return HttpResponse('Sample data populated. You can now view /authors/, /books/, /products/')
