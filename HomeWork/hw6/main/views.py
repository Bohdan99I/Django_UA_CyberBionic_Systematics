from django.shortcuts import render, redirect
from .models import Article, Tag

def index(request):
    return render(request, 'main/index.html')

def populate(request):
    # create sample tags and articles
    t1, _ = Tag.objects.get_or_create(name='django')
    t2, _ = Tag.objects.get_or_create(name='news')
    t3, _ = Tag.objects.get_or_create(name='life')

    a1, _ = Article.objects.get_or_create(title='Лісова казка', body='Про ліс...')
    a1.tags.add(t1, t3)
    a2, _ = Article.objects.get_or_create(title='Article 2025', body='Contains a number 2025')
    a2.tags.add(t2)
    a3, _ = Article.objects.get_or_create(title='Людина і світ', body='Starts with Л')
    a3.tags.add(t3)
    a4, _ = Article.objects.get_or_create(title='Test123', body='Has digits 123')
    a4.tags.add(t1)
    a5, _ = Article.objects.get_or_create(title='Легенда 7', body='Starts with Л and has digit 7')
    a5.tags.add(t2, t3)

    return redirect('index')

def search_articles(request):
    q = request.GET.get('q', '')
    tag = request.GET.get('tag', '')
    qs = Article.objects.all()
    if q:
        qs = qs.filter(title__icontains=q)
    if tag:
        qs = qs.filter(tags__name=tag)
    qs = qs.prefetch_related('tags').order_by('-created_at')
    return render(request, 'main/search.html', {'articles': qs, 'q': q, 'tag': tag})

def special_queries(request):
    starts_with_L = Article.objects.filter(title__startswith='Л').order_by('-created_at')
    with_digit = Article.objects.filter(title__regex=r'\d').order_by('-created_at')
    return render(request, 'main/special.html', {'starts_with_L': starts_with_L, 'with_digit': with_digit})
